import random

#Ejercicio 1:
for i in range(101):
    print(i)

#Ejercicio 2:
cant = 0
num = input("Ingrese un numero: ")
for i in range(len(num)):
    cant += 1
print("La cantidad de digitos es: ", cant)

#Ejercicio 3:
suma = 0
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
for i in range(num1+1, num2):
    suma += i
print("La suma de los numeros entre ", num1, " y ", num2, " es: ", suma)

#Ejerciocio 4:
opc = ""
sumasec = 0
while opc != "0":
    opc = input("Ingrese un numero (0 para salir): ")
    sumasec += int(opc)
print("La suma de los numeros ingresados es: ", sumasec)

#Ejercicio 5:
numerorandom = random.randint(0, 9)
intento = 1 
num3 = int(input("Adivina el numero entre 0 y 9: "))
while numerorandom != num3:
    print("Intenta de nuevo")
    num3 = int(input("Ingrese otro numero: "))
    intento += 1
print(f"Correcto el numero era {numerorandom}.")
print(f"Cantidad de intentos: {intento}")

#Ejercicio 6:
for i in range(100, -1, -2):
    print(i)

#Ejercicio 7:
suma = 0
num4 = int(input("Ingrese un numero: "))
for i in range(0, num4+1):
    suma += i
print("La suma de los numeros desde 0 hasta ", num4, " es: ", suma)

#Ejercicio 8:
impar = 0
par = 0
positivo = 0
negativo = 0
for i in range(10):
    num5 = int(input(f"{i+1}. Ingrese un numero: "))
    if num5 % 2 == 0:
        par += 1
    else:
        impar += 1
    if num5 > 0:
        positivo += 1
    elif num5 < 0:
        negativo += 1
print("Cantidad de numeros pares:", par)
print("Cantidad de numeros impares:", impar)
print("Cantidad de numeros positivos:", positivo)
print("Cantidad de numeros negativos:", negativo)

#Ejercicio 9:
suma = 0
for i in range(100):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    suma += numero
media = suma / 100
print(f"La media de los {100} numeros es: {media}")

#Ejercicio 10:
numero = input("Ingrese un número: ")
numero_invertido = int(numero[::-1])
print(f"El número invertido es: {numero_invertido}")


