#Actividad 1:
print ("Hola Mundo!")

#Actividad 2:
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Actividad 3:
nomb = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lug_res = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lug_res}")

#Actividad 4:
radio = float(input("Ingrese el radio del circulo: "))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"El area del circculo es: {area}, y el perimetro es: {perimetro}")

#Actividad 5:
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos // 3600
print(f"{segundos} segundos son {horas} horas")

#Actividad 6:
numero = int(input("Ingrese un numero para calcular su tabla de multiplicar: "))
print(f"1- {numero} * 1 = {numero * 1}")
print(f"2- {numero} * 2 = {numero * 2}")
print(f"3- {numero} * 3 = {numero * 3}")
print(f"4- {numero} * 4 = {numero * 4}")
print(f"5- {numero} * 5 = {numero * 5}")
print(f"6- {numero} * 6 = {numero * 6}")
print(f"7- {numero} * 7 = {numero * 7}")
print(f"8- {numero} * 8 = {numero * 8}")
print(f"9- {numero} * 9 = {numero * 9}")
print(f"10- {numero} * 10 = {numero * 10}")

#Actividad 7:
numero1 = float(input("Ingrese el primer numero distinto de cero: "))
numero2 = float(input("Ingrese el segundo numero distinto de cero: "))

print("Suma de los dos numeros: ", numero1 + numero2)
print("Resta de los dos numeros: ", numero1 - numero2)
print("Multiplicacion de los dos numeros: ", numero1 * numero2)
print("Division de los dos numeros: ", numero1 / numero2)

#Actividad 8:
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
masa_corporal = peso / (altura ** 2)
print(f"Su indice de masa corporal es: {masa_corporal}")

#Actividad 9:
grados_celsius = float(input("Ingrese la temperatura en grados celsius: "))
grados_fahrenheit = 9/5 * grados_celsius + 32
print(f"La temperatura en grados fahrenheit es: {grados_fahrenheit}")

#Actividad 10:
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres numeros es: {promedio}")