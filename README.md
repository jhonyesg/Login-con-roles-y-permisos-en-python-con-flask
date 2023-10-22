# Login-con-roles-y-permisos-en-python-con-flask
Es un proyecto robusto base, en el cual se tiene un login con las metricas intermedias de seguridad, que tiene un manejo de usuarios por roles, el cual segun los roles, lo redireciona a su respectiva carpeta, donde pueden almacenar todos los archivos, con un sistema de manejo de acceso, respuesta ante errores.

ESCTRUTURA DE LA BASE DE DATOS

Es una base de datos sencillas, su objectivo es brindar al usuario una plataforma lista, para comenzar a trabajar y no estresarse con crear login ni politicas, por que ya vienen definidas:

![captura de la base de datos para proyecto base con python](https://github.com/jhonyesg/Login-con-roles-y-permisos-en-python-con-flask/assets/29180546/380a110b-551b-4359-acb5-afd3cdf84a46)

LA VISTA DEL LOGIN

El login es  sencillo, pero tiene un html el cual se puede personalizar fuerte, para dejarlo al gusto:

![login](https://github.com/jhonyesg/Login-con-roles-y-permisos-en-python-con-flask/assets/29180546/24ac0963-441b-4c8f-b0e5-3a572334848c)

deje el login en base a uno que vi en youtobe, que me parecio minimalista

VISTA DE ACCESO AL PANEL DEL ADMIN

Como mencione es un proyecto que deja todo listo para empezar a crear el panel, al momento solo or roles maneja paginas de bienvenida, segun el rol:

![dashboart](https://github.com/jhonyesg/Login-con-roles-y-permisos-en-python-con-flask/assets/29180546/cc3ea939-f137-4ce1-9fa3-dfa11af329f6)

VISTA DE CUANDO UN RECURSO NO EXISTE  O NO ES PERMITIDO

Construi esta aplicacion, debido que use laravel, y no me gusto ya que soy mas amigo de python, por su minimalismo, por tanto con el fin de hacer lo mas segura esta app, 
trabaje en hacer el testin, de todo tipo de violacion de metricas, por lo cual si intento acceder a un recurso que no exite tenenemos el siguiente mensaje:

![Cuando el recurso no existe](https://github.com/jhonyesg/Login-con-roles-y-permisos-en-python-con-flask/assets/29180546/6adab6f8-4f2f-48c3-b304-c17f0234ee43)

Cuando alguien quiera acceder a otro panel, fuera de su rol, la vista del manejo a esta intruccion es:

![Prueba de mensaje de intento de acceso a otro panel que no es del rol](https://github.com/jhonyesg/Login-con-roles-y-permisos-en-python-con-flask/assets/29180546/dd7b9027-9399-4eb4-b867-2db788800228)

LLAMADO DE ARCHIVO DENTRO DE LA CARPETA SEGUN EL ROL DE USUARIO

Construi una logica simple pero inquebrantable, el cual consta que puedo llamar los archivos html sin necesidad de poner la extension asi:

![prueba de llamado de otro archivos en la carpeta con el rol del usuario](https://github.com/jhonyesg/Login-con-roles-y-permisos-en-python-con-flask/assets/29180546/44b08ff3-7851-49c4-b0f8-e32b62b1dfea)

En el caso de querer llamar otros archivos, toca colocar la extension, pero  es algo muy sencillo.

Espro que el usuario que lo use, le sea de utilidad lo unico que deseo es que dejen buenos comentarios y si usan linkedin, https://www.linkedin.com/in/jhon-efrain-suarez-gomez/ me agregue o creen post, mencionando que le fue de utilidad
este codigo que construi, con un poco de esfuerzo, ya que mi fuerte son los Script y no los desarrollos Webs.


