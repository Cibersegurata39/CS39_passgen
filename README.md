# CS39_passgen

<img src="https://img.shields.io/badge/-python-3776AB?style=for-the-badge&logo=python&logoColor=white" />

Programa creado en Ptyhon para generar contraseñas seguras.

El programa se controla con un *while* que ejecutará hasta que el usuario no quiera generar más contraseñas, lo cual se pregunta al final. En caso de respuesta negativa, se sale del bucle y se muestra un mensaje de despedida.
Primero se pregunta por el tamaño con el que se desea crear la contraseña, para después preguntar de que tipología. Estas serían: contraseña formada exclusivamente por letras, formada exclusivamente por números o por una mezcla de letras, dígitos y signos. Para ambas preguntas se espera un número entero como respuesta y esto es lo que se valida en la función *validar_inputs*. En caso de insertar una longitud negativa, se vuelve a pedir un nuevo valor, y si se proporciona cualquier otro tipo de valor, se informa de ello y se vuelve a pedir otra respuesta.

Si a la hora de elegir la tipología de la contraseña se proporciona un valor que no se encuentra en el rango 1-3, se vuelve a pedir una respuesta.

Para la creación de la contraseña, se utiliza la función 'generar_contraseña', a la cual se le pasa la longitud y el tipo de contraseña a crear. Primero se forma un string 'componentes' con los carácteres que pueden conformar la *password*, dependiendo del tipo elegido estos serán sólo letras, sólo dígitos o una mezcla de letras, dígitos y signos. En caso de elegir la tipología 3 y que la longitud sea mayor que 3, se fuerza a la creación de una contraseña que contenga una letra mayúscula, una minúscula, un dígito y un signo. Esto se hace con la función *choice* de la librería *random*. Una vez tenemos estos requisitos mínimos, se genera el resto de la contaseña con lo contenido en el string 'componentes' antes creado. Por último, se mezclan todos los caracteres de la cadena con la función *sample* de la librería *random*. Si se elige otro tipo de tipología que no es la 3, directamente se cogen los valores del *string* 'componentes'. En caso de error, se pide intentarlo de nuevo.
