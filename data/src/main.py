import pandas as pd

inventario = []

def registrar():
    nombre = input("nombre: ")
    precio = float(input("precio: "))
    prenda = {"nombre": nombre, "precio": precio}
    inventario.append(prenda)
    print("guardado")

def promedio():
    if not inventario:
        print("vacio")
    else:
        suma = 0
        for i in inventario:
            suma += i["precio"]
        p = suma / len(inventario)
        print("promedio:", p)

while True:
    print("\n1.registrar\n2.promedio\n3.salir")
    op = input("opcion: ")
    if op == "1":
        registrar()
    elif op == "2":
        promedio()
    elif op == "3":
        break
    else:
        print("error")