#Ejercicio 1 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Ejercicio 3
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#Ejercicio 4
agenda = {}

for i in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input("Ingresá el número telefónico: ")
    agenda[nombre] = numero

consulta = input("Ingresá el nombre que querés buscar: ")

if consulta in agenda:
    print("El número es:", agenda[consulta])
else:
    print("Ese contacto no existe.")

#Ejercicio 5
frase = input("Ingresá una frase: ")

palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

frecuencias = {}
for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

print("Frecuencia de palabras:", frecuencias)

#Ejercicio 6
alumnos = {}

for i in range(3):
    nombre = input("Ingresá el nombre del alumno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"El promedio de {nombre} es {promedio:.2f}")

#Ejercicio 7
parcial1 = {1, 2, 3, 4, 8}
parcial2 = {3, 4, 5, 6}

print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

#Ejercicio 8
stock = {"Pan": 20, "Leche": 15, "Huevos": 30}

producto = input("Ingresá el nombre del producto: ")

if producto in stock:
    agregar = int(input("¿Cuántas unidades querés agregar? "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto no existe. Ingresá stock inicial: "))
    stock[producto] = nuevo_stock

print(stock)

#Ejercicio 9
agenda = {
    ("Lunes", "10:00"): "Gimnasio",
    ("Martes", "15:00"): "Dentista"
}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora: ")

if (dia, hora) in agenda:
    print("Actividad:", agenda[(dia, hora)])
else:
    print("No hay actividad en ese horario.")

#Ejercicio 10
paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio"
}

capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)
