import os

ruta_archivo = os.path.join(os.path.dirname(__file__), "productos.txt")

productos = []

with open(ruta_archivo, "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        productos.append({
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        })

print("Lista de productos:")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

nuevo_nombre = input("\nIngrese el nombre del nuevo producto: ")
nuevo_precio = float(input("Ingrese el precio: "))
nueva_cantidad = int(input("Ingrese la cantidad: "))

nuevo_producto = {
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nueva_cantidad
}

productos.append(nuevo_producto)

buscar = input("\nIngrese el nombre del producto a buscar: ")
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print(f"Producto encontrado: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("El producto no existe.")

with open("productos.txt", "w") as archivo:
    for p in productos:
        linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
        archivo.write(linea)

print("\nArchivo productos.txt actualizado correctamente.")
