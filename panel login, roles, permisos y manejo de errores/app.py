from aplicacion.conexion import init_app

app = init_app()

if __name__ == '__main__':
    app.secret_key = "pinchellave"
    app.run(debug=True, host='0.0.0.0', port=8000, threaded=True)
