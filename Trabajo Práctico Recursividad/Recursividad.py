# 1)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Ingresa un numero entero positivo: "))
for i in range(1, num + 1):
    print(f"{i}! = {factorial(i)}")

#2
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
pos = int(input("Ingresa la posicion mqxima de Fibonacci: "))
serie = [fibonacci(i) for i in range(pos + 1)]
print("Serie de Fibonacci:", serie)

#3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
b = int(input("Ingresa la base: "))
e = int(input("Ingresa el exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

#4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
numero = int(input("Ingresa un numero entero positivo: "))
print(f"El numero {numero} en binario es {decimal_a_binario(numero)}")



