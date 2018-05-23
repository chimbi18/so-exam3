# so-exam3

**Nombre:** Victor Andrés Calambás Hurtado    
**Código:** A00059956   
**Materia:** Sistemas operacionales  
**Correo:** victor.1818@hotmail.es
**Repositorio:** https://github.com/chimbi18/so-exam3

##implementación del servicio Flask

Para la implementación del servicio flask, creamos primeramente un ambiente virtual como lo hicimos en clase con flaskdev, luego añadimos los archivos como los utilizamos en la tarea workshop3, con los nombres de requirements.txt y requirements_dev.txt utilizando el codigo fuente que esta almacenado en el repositorio del curso.  (El codigo fuente de estos archivos estan en el repositorio con sus respectivos nombres).

Luego creamos una carpeta op_stats en la cual vamos vamos a tener nuestros archivos de python llamados app.py(en este archivo se se crean los métodos que permiten realizar la implementación del servicio web de flaksk) y el stats.py (en este archivo se encuntran los metodos que retornan los estados de la memoria, disco duro y la CPU)

Aqui se evidencian las imagenes de la maquina virtual:

imagen mv1 
imagen mv2

Aqui se evidencian las imagenes mediante el uso de la extensión de google chrome llamada Postman

imagen Postman3  
imagen Postman3  
imagen Postman3  



# Implementación de pruebas usando Fixtures y Mocks

para la realización de las pruebas unitarias, creamos una carpeta llamada test para poder separar las funcionalidades de las pruebas, esto con el fin de utilizar buenas practicas de programación. Luego de haber creado la carpeta tests, creamos el archivo test_stats.py como lo habiamos hecho en clase y aqui en este archivo creamos las pruebas de los estados de la cpu, memoria y disco, debido a que estos valores son cambiantes les asignamos un valor por defecto para saber en tiempo de ejecución si el metodo que se esta probando funciona correctamente, sin embargo no podremos ver los verdaderos valores en las pruebas. Los valores que les asignamos a los metodos de test pueden ser retornando y validando un valor diferente (usualmente es utilizado para identificar cuales son las pruebas que fallan y cuales estan funcionando orrectamente).Por motivos de que solo estamos usando 3 pruebas no considere hacer necesario esta asignación de diferentes valores a cada una de las pruebas, 
para correrlas utilizamos el comano pytest -v

imagen prueba pytest1
imagen prueba pytest

## Integración Continua

Luego que funcionaran las pruebas, creamos en el repositorio un archivo tox.ini en el cual se especifian las librerias que van a ser usadas y el ambiente de desarrollo, y el comando a realizar. para ejecutar estas pruebas en consola utilizamos el comando para instalar el requirements_dev.txt y posteriormente escribimos el comando tox .Con este comando se ejecutarán todas las pruebas y mostrara en pantallla las siguientes imagenes:

imagen prueba tox

Luego de que hallan funcionado las pruebas correctamente como la imagen anterior, procedemos a crear el archivo .travis.yml con la configuración del repositorio del curso , y procedemos a hacer el pull request a nuestro fork para poder que se ejecuten de forma automatica las pruebas desde travis-ci.org e ingresando con nuestra cuenta de git y activando el repositorio so-exam3 se ejecutará y el resultado de esta ejecución son las siguientes imagenes:

imagen travis 1
imagen travis 2
