import string
import random

#Validación de la entrada
def validar_input(msg, tipo='int'):
    while True:
        try:
            if tipo == 'int':
                valor = int(input(msg))
                if valor <= 0:
                    print("Ingrese una longitud positiva.")
                    continue #genera nueva iteración
                return valor #se devuelve el valor pues cumple con los requisitos
        except ValueError:
            print("Entrada no valida. Pruebe de nuevo.")

#Carácteres a utilizar para la generacion de la contraseña
def generar_contraseña(longitud, tipo_pwd):
    try:
        if tipo_pwd == 1:
            componentes = string.ascii_letters
        elif tipo_pwd == 2:
            componentes = string.digits
        else:
            componentes = string.ascii_letters + string.digits + string.punctuation
        #Nos aseguramos que cada pwd tenga una letra mayuscula, minuscula, un digito y un signo,
        #siempre que la longitud de esta sea mayor de 3
        if tipo_pwd == 3 and longitud > 3:
            #Caracter de cada tipo
            mayuscula = random.choice(string.ascii_uppercase)
            minuscula = random.choice(string.ascii_lowercase)
            numeros = random.choice(string.digits)
            signos = random.choice(string.punctuation)
            #Resto de la contraseña
            resto = "".join(random.choice(componentes) for i in range(longitud-4))
            #Concateación de todo
            password = mayuscula + minuscula + numeros + signos + resto
            #Mezcla de todos los caracteres
            password = ''.join(random.sample(password, len(password))) 
            return password
        else:
            password = "".join(random.choice(componentes) for i in range(longitud))
            return password
    except ValueError:
        print("Opción no válida. Intenta nuevamente.")

##Main##
while True: #búcle hasta que el usuario no quiera generar más contraseñas
    long = validar_input("Tamaño de la contraseña deseado: ", 'int')
    tipo_pwd = validar_input("Tipo de password deseada letras (1), digitos (2) o letras, digitos y signos (3):  ", "int")

    while tipo_pwd not in [1, 2, 3]: #controlamos la entrada
        print("Opción no válida. Intenta nuevamente.")
        tipo_pwd = validar_input("Tipo de password deseada letras (1), digitos (2) o letras, digitos y signos (3):  ", "int")

    #Generacion de la contraseña
    password = generar_contraseña(long, tipo_pwd)
    print("La contraseña generada es: " + password)

    #Se ofrece guardar la contraseña
    guardar =  input("¿Quieres guardar la contraseña en un archivo? (S/N)").strip().lower()
    if guardar == 's':
        archivo = input("Introduce el nombre del archivo (sin extensión): ") + ".txt"
        #estrucutra de control (with) que simpifica el manejo del archivo y lo cierra una vez se sale del bloque
        with open(archivo, 'w') as f: 
            f.write(password)
        print(f"Contraseña guardada en {archivo}")

    #Se ofrece generar otra contraseña
    otra =  input("¿Quieres generar una nueva contraseña? (S/N)").strip().lower()
    if otra != 's': #Se sale del búcle de generación de contaseñas
        print("¡Gracias, hasta la proxima!")
        break