from flask import Flask, render_template, request, session, abort, redirect, url_for, send_from_directory
from .database_operations import insert_data, query_data
from jinja2.exceptions import TemplateNotFound
from flask_mysqldb import MySQL
from decouple import Config
import bcrypt
import os

from dotenv import load_dotenv  # Importa load_dotenv desde dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Función para inicializar la app de Flask
def init_app():

    # Crea una instancia de la app
    app = Flask(__name__, template_folder='../templates')

   # Configura la conexión a la base de datos
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') 
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    mysql = MySQL(app)


    # Función para verificar el rol requerido
    def verify_role(required_role, current_role):
      if required_role != current_role:
        abort(403)

    # Función para autenticar usuario
    def authenticate_user(mysql, identifier, password):
       # Busca usuario en la BD
       # Verifica contraseña    
       # Devuelve datos del usuario
        cur = mysql.connection.cursor()
        try:
    # Buscar por correo o nombre de usuario
            cur.execute('SELECT * FROM usuarios WHERE correo = %s OR username = %s', (identifier, identifier,))
            account = cur.fetchone()
    
            if account:
        # Verificar la contraseña encriptada
                if bcrypt.checkpw(password.encode('utf-8'), account['password'].encode('utf-8')):
                    return account
        finally:
        # Asegúrate de cerrar el cursor, incluso si ocurre una excepción
            cur.close()
        return None
    
    # Administrador de errores para 403
    @app.errorhandler(403)
    def forbidden_error(e):
        return render_template('403.html'), 403
    # Administrador de errores para 404
    @app.errorhandler(404)
    def forbidden_error(e):
        return render_template('404.html'), 404

    @app.route('/<string:folder>/<path:file_name>', methods=["GET"])
    def check_role_and_serve_page(folder, file_name):
        # Ruta para verificar rol y servir archivos
        role_map = {'admin': 1, 'client': 2, 'cloud': 3}
        # Mapeo de roles a números para comparar
        if folder in role_map:
                # Verificar que la carpeta esté en el mapeo
                if 'id_rol' not in session or session['id_rol'] != role_map[folder]:
                 # Comparar rol de sesión con el de la carpeta
                 abort(403)
                 # Si no coinciden, abortar la petición

    # Determinar la extensión del archivo
        file_ext = os.path.splitext(file_name)[1]
      

    # Si no hay extensión, asumir que es un archivo HTML
        if not file_ext:
            file_name += '.html'
            file_ext = '.html'

        try:     
            if file_ext == '.html':
                return render_template(f'{folder}/{file_name}')
            else:
                return send_from_directory(os.path.abspath(os.path.join('templates', folder)), file_name)
        except TemplateNotFound:
            abort(404)
        except FileNotFoundError:
            abort(404)



    @app.route('/acceso-login', methods=["GET", "POST"])
    def login():
        if request.method == 'POST':
            identifier = request.form.get('txtCorreo') or request.form.get('txtUsername')
            password = request.form['txtPassword']

            account = authenticate_user(mysql, identifier, password)

            if account:
                session['logueado'] = True
                session['id_user'] = account['id_user']
                session['id_rol'] = account['id_rol']

                if session['id_rol'] == 1:
                    return redirect(url_for('admin'))
                elif session['id_rol'] == 2:
                    return redirect(url_for('client'))
                elif session['id_rol'] == 3:
                    return redirect(url_for('cloud'))
            else:
                return render_template('index.html', mensaje="Usuario O Contraseña Incorrectas")
        # Asegúrate de devolver una respuesta válida si no se cumplen las condiciones anteriores
        return render_template('index.html')

    #validar rol administrador
    @app.route('/admin')
    def admin():
        if 'id_rol' not in session or session['id_rol'] != 1:
            abort(403)
        return render_template('admin/admin.html')
    #validar rol cliente
    @app.route('/client')
    def client():
        if 'id_rol' not in session or session['id_rol'] != 2:
            abort(403)
        return render_template('client/admin.html')
    #validar rol cloud
                 
    @app.route('/cloud')
    def cloud():
        if 'id_rol' not in session or session['id_rol'] != 3:
            abort(403)
        return render_template('cloud/admin.html')
    
    #validador de roles y redirecion a pagina segun el panel
    @app.route('/')
    def home():
        if 'logueado' not in session:
         return redirect(url_for('login'))  # Si no está logueado, redirige a la página de login

        if session['id_rol'] == 1:
         return redirect(url_for('admin'))
        elif session['id_rol'] == 2:
         return redirect(url_for('client'))
        elif session['id_rol'] == 3:
            return redirect(url_for('cloud'))
        else:
        # Maneja otros roles o situaciones según sea necesario.
            return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        # Elimina la información de la sesión para cerrarla
        session.clear()
        # Redirige al usuario a la página de inicio de sesión (cambia '/login' al URL correcto)
        return redirect(url_for('login'))

    return app
# Devuelve la app configurada y lista para ser utilizada