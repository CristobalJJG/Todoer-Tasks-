<----------(Para crear este mismo programa desde 0)---------->

1.- Crear la carpeta del proyecto, entrar en esa carpeta desde cmd

2.-Escribir en cmd python "-m venv venv" para crear la carpeta venv dentro de la carpeta del proyecto.

3.-(con el cmd de Windows)  cd  venv -> cd Scripts -> activate
(Se ve si está activado o no porque aparece a la izquierda de la línea de comandos un "(venv)")

4.-
	4.1.- Instalar werkzeug -> pip install werkzeug
	4.2.- Instalar conector python-mysql -> pip install mysql-connector-python
	(En el caso de MAC) 4.3.-> Instalar neovim (pip3 install neovim)
	4.4.- Instalar Flask -> pip install Flask

5.- Se crea "__init__.py", así sabremos cual es el "main" del programa.

6.- Escribimos el código, lo que importamos, y creamos la función create_app(), la cual nos servirá para probar la aplicacion.

7.-Creamos una ruta y nos aseguramos de que funcione.

8.- Desde cmd
	8.1.- Declaramos la carpeta (todo) como Principal para venv -> set FLASK_APP=todo
	8.2.- Declaramos Flask como ambiente de desarrollo -> set FLASK_ENV=development

flask run para comprobar que todo ha ido bien, y empezar a programar



<----------(Para utilizar este programa)---------->

1.-Escribir en cmd python "-m venv venv" para crear la carpeta venv dentro de la carpeta del proyecto.

2.-(con el cmd de Windows)  cd  venv -> cd Scripts -> activate
(Se ve si está activado o no porque aparece a la izquierda de la línea de comandos un "(venv)")

3.- Desde cmd
	8.1.- Declaramos la carpeta (todo) como Principal para venv -> set FLASK_APP=todo
	8.2.- Declaramos Flask como ambiente de desarrollo -> set FLASK_ENV=development

4.- En cmd colocamos flask run para inciar y hacemos ctrl+click en la ip que nos muestra(Para salir de aqui hacemos ^c)

5.-Necesitamos tener alguna base de datos de MySQL para poder conectarnos a ella.

6.-En el fichero "db.py" cambiamos las entradas de la base de datos para conectarnos a la nuestra.

7.-Para iniciar la base de datos una vez hemos colocado los datos, flask init-db, y deberá mostrar por consola "Base de datos inicializada."

A partir de ahí sería usar la webapp
