#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años.
# ● Adolescente: mayor o igual que 12 años y menor que 18 años.
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ● Adulto/a: mayor o igual que 30 años

edad2 = int(input("Ingrese su edad: "))
if edad2 < 12:
    print("Niño/a")
elif edad2 >= 12 and edad2 < 18:
    print("Adolescente")
elif edad2 >= 18 and edad2 < 30:
    print("Adulto/a joven")
elif edad2 >= 30:
    print("Adulto/a")

#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contraseña = input("Ingrese una contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. 
# ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. 
# ● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. 
# ● Sin sesgo: cuando la media, la mediana y la moda son iguales.

import random
num_aleatorios = [random.randint(1,100) for i in range(59)]

from statistics import mode, median, mean
media = mean (num_aleatorios)
mediana = median (num_aleatorios)
moda = mode (num_aleatorios)

sesgo_pos = media > mediana > moda
sesgo_neg = media < mediana < moda
sin_sesgo = media == mediana == moda

if sesgo_pos:
    print("Sesgo positivo o a la derecha")
elif sesgo_neg:
    print("Sesgo negativo o a la izquierda")
elif sin_sesgo:
    print("Sin sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase_palabra = input("Ingrese una frase o palabra: ")
vocales = ["aeiou"]

if frase_palabra[-1].lower() in vocales:
    print(frase_palabra + "!")
else:
    print(frase_palabra)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 

nombre = input("Ingrese su nombre: ")
opcion = int(input("1 para mayusculas, 2 para minusculas, 3 para primera letra mayuscula: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Ingrese la magnitud del terremoto: "))
cat = ""
if magnitud < 3:
    cat = "Muy leve (imperceptible)"
elif magnitud >= 3 and magnitud < 4:
    cat = "Leve (ligeramente perceptible)"
elif magnitud >= 4 and magnitud < 5:
    cat = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud >= 5 and magnitud < 6:
    cat = "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud >= 6 and magnitud < 7:
    cat = "Muy Fuerte (puede causar daños significativos)"
elif magnitud >= 7:
    cat = "Extremo (puede causar graves daños a gran escala)"
print(cat)

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("Ingrese su hemisferio (N/S): ")
mes = input("Ingrese el mes: ")
dia = int(input("Ingrese el dia (num): "))

if hemisferio.upper() == "N":
    if (mes.lower() == "marzo" and dia >= 21) or (mes.lower() == "abril") or (mes.lower() == "mayo") or (mes.lower() == "junio" and dia <= 20):
        print("Se encuentra en primavera")
    elif (mes.lower() == "junio" and dia >= 21) or (mes.lower() == "julio") or (mes.lower() == "agosto") or (mes.lower() == "septiembre" and dia <= 22):
        print("Se encuentra en verano")
    elif (mes.lower() == "septiembre" and dia >= 23) or (mes.lower() == "octubre") or (mes.lower() == "noviembre") or (mes.lower() == "diciembre" and dia <= 20):
        print("Se encuentra en otoño")
    elif (mes.lower() == "diciembre" and dia >= 21) or (mes.lower() == "enero") or (mes.lower() == "febrero") or (mes.lower() == "marzo" and dia <= 20):
        print("Se encuentra en invierno")
elif hemisferio.upper() == "S":
    if (mes.lower() == "marzo" and dia >= 21) or (mes.lower() == "abril") or (mes.lower() == "mayo") or (mes.lower() == "junio" and dia <= 20):
        print("Se encuentra en otoño")
    elif (mes.lower() == "junio" and dia >= 21) or (mes.lower() == "julio") or (mes.lower() == "agosto") or (mes.lower() == "septiembre" and dia <= 22):
        print("Se encuentra en invierno")
    elif (mes.lower() == "septiembre" and dia >= 23) or (mes.lower() == "octubre") or (mes.lower() == "noviembre") or (mes.lower() == "diciembre" and dia <= 20):
        print("Se encuentra en primavera")
    elif (mes.lower() == "diciembre" and dia >= 21) or (mes.lower() == "enero") or (mes.lower() == "febrero") or (mes.lower() == "marzo" and dia <= 20):
        print("Se encuentra en verano")