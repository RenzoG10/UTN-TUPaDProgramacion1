#Ejercicio 1
lista = [10,9,8,8,10,6,5,9,7,10]
suma = 0
prom = 0
notamax = 0
notamin = 0
print("Los elementos de la lista son:")
print(lista)

for i in range(len(lista)):
    suma += lista[i]

    if lista[i] > notamax:
        notamax = lista[i]
    if lista[i] < notamin or notamin == 0:
        notamin = lista[i]
prom = suma / len(lista)
print("El promedio de los elementos de la lista es: ", prom)
print("La nota maxima es: ", notamax)
print("La nota minima es: ", notamin)

#Ejercicio 2
productos = []

for i in range(5):
    producto = input(f"Ingrese el nombre del producto {i+1}: ")
    productos.append(producto)

productos_ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
print(productos_ordenados)

producto_eliminar = input("\nIngrese el producto que desea eliminar: ")

if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print("\nLista actualizada:")
    print(productos)
else:
    print(f"\nEl producto '{producto_eliminar}' no se encuentra en la lista.")

#Ejercicio 3
import random

numeros = []
for i in range(15):
    numero_aleatorio = random.randint(1, 100)
    numeros.append(numero_aleatorio)

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Numeros pares:", pares)
print("Cantidad de numeros pares:", len(pares))
print("Numeros impares:", impares)
print("Cantidad de numeros impares:", len(impares))

#Ejercicio 4
lista = [1,3,5,3,7,1,9,5,3]
sinrepetir = []
for i in lista:
    if i not in sinrepetir:
        sinrepetir.append(i)
print("Lista sin elementos repetidos:", sinrepetir)

#Ejercicio 5
estudiantes = ["Ana", "Luis", "Renzo", "Aylen", "Marcos", "Eva", "Lucía", "Diego"]

print("Lista de estudiantes:", estudiantes)

accion = input("¿Desea agregar un nuevo estudiante o eliminar uno existente? (a/e): ").lower()

if accion == "a":
    nuevo = input("Ingrese el nombre del estudiante a agregar: ")
    estudiantes.append(nuevo)
    print("\nEstudiante agregado correctamente.")
elif accion == "e":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print("\nEstudiante eliminado correctamente.")
    else:
        print(f"\nEl estudiante '{eliminar}' no se encuentra en la lista.")
else:
    print("\nAcción no válida.")

print("Lista final de estudiantes:", estudiantes)

#Ejercicio 6

numeros = [10, 20, 30, 40, 50, 60, 70]
ultimo = numeros[-1]

for i in range(len(numeros)-1, 0, -1):
    numeros[i] = numeros[i-1]
numeros[0] = ultimo

print("Lista rotada una posición a la derecha:", numeros)

#Ejercicio 7
temperaturas = [
    [12, 22],
    [14, 25],
    [10, 20],
    [15, 28],
    [11, 21],
    [13, 23],
    [9, 19]
]

suma_min = suma_max = 0
for dia in temperaturas:
    suma_min += dia[0]
    suma_max += dia[1]

promedio_min = suma_min / len(temperaturas)
promedio_max = suma_max / len(temperaturas)

print("Promedio mínimas:", promedio_min)
print("Promedio máximas:", promedio_max)

amplitud_max = 0
dia_amplitud = 0
for i, dia in enumerate(temperaturas):
    amplitud = dia[1] - dia[0]
    if amplitud > amplitud_max:
        amplitud_max = amplitud
        dia_amplitud = i + 1 

print("Mayor amplitud térmica en el día:", dia_amplitud)

#Ejercicio 8
notas = [
    [8, 7, 9],
    [6, 5, 7],
    [9, 8, 10],
    [7, 6, 8],
    [10, 9, 9]
]

for i, est in enumerate(notas):
    promedio = sum(est) / len(est)
    print(f"Promedio del estudiante {i+1}: {promedio}")

num_materias = len(notas[0])
for j in range(num_materias):
    suma = sum(notas[i][j] for i in range(len(notas)))
    promedio = suma / len(notas)
    print(f"Promedio de la materia {j+1}: {promedio}")

#Ejercicio 9
tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
    print()

for turno in range(5):
    jugador = "X" if turno % 2 == 0 else "O"
    fila = int(input(f"Jugador {jugador}, ingrese fila (0-2): "))
    col = int(input(f"Jugador {jugador}, ingrese columna (0-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = jugador
    else:
        print("Casilla ocupada, intente otra.")
    mostrar_tablero(tablero)

#Ejercicio 10
ventas = [
    [5, 3, 4, 6, 2, 5, 3],
    [2, 4, 3, 5, 4, 3, 6],
    [6, 5, 7, 3, 4, 5, 4],
    [3, 2, 4, 5, 3, 4, 2]
]
for i, prod in enumerate(ventas):
    total = sum(prod)
    print(f"Total vendido del producto {i+1}: {total}")

ventas_por_dia = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
dia_max = ventas_por_dia.index(max(ventas_por_dia)) + 1
print("Día con mayores ventas totales:", dia_max)

totales_productos = [sum(prod) for prod in ventas]
producto_max = totales_productos.index(max(totales_productos)) + 1
print("Producto más vendido en la semana:", producto_max)




