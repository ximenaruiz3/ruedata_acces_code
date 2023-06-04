# Ruedata_acces_code
  Un método de seguridad habitual en la banca electrónica consiste en pedir al usuario tres caracteres aleatorios 
  de un código de acceso. Por ejemplo, si el código de acceso era 531278, pueden pedir los caracteres 2o, 3o y 5o; la respuesta esperada sería: 317.
# Descarga de repositorio
  
  Para descargar el repositorio, abrimos una terminal, realizamos un git clone en la carpeta donde se desea obtener el repositorio, 
  seguido del enlace que se encuentra en la opción "code" en GitHub:
  
 ``` git clone https://github.com/ximenaruiz3/ruedata_acces_code.git```
  
# Instalar dependencias
  Ingresamos a la carpeta "ruedata_acces_code" y ejecutamos:
   ``` pip install -r requirements.txt```
# Ejecucion de la aplicación
  Para ejecutar la aplicación digitamos el siguiente comando:
  flak run y debera aparecernos el siguiente mensaje
  
```
flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
# Consumo de api
El enpoint se consume de la siguiente manera :
```
  curl --location --request GET 'http://127.0.0.1:5000/acces_code'
```
Para ontener una respuesta similar a la siguiente:
```
El codigo de acceso es: 73162890
```
