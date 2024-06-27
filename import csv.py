import csv
import time

stock = "stockk.csv"

# Función para cargar los datos del archivo CSV
def cargar_archivo():
    productos = []
    with open(stock, "r", newline="") as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            nombre = fila[0]
            precio = fila[1]
            cantidad = fila[2]
            productos.append([nombre, precio, cantidad])
    return productos

# Función para guardar los datos en el archivo CSV
def guardar_archivo(productos):
    with open(stock, "w", newline="") as archivo:
        escritor_csv = csv.writer(archivo)
        for producto in productos:
            escritor_csv.writerow(producto)

# Función para mostrar el stock
def mostrar_stock(productos):
    print("=" * 80)
    print("|{:<3}|{:<33}|{:<5}|{:<3}|".format("ID", "Producto", "Precio", "Cantidad"))
    print("=" * 80)
    for i, producto in enumerate(productos, start=1):
        nombre, precio, cantidad = producto
        print("|{:<2}|{:<35}|{:<5}|{:<3}|".format(i, nombre, f"${precio}", cantidad))
    print("=" * 80)

# Función para modificar la cantidad de un producto
def modificar_cantidad(productos):
    nombre_producto = input("Ingrese el nombre del producto a modificar: ")
    encontrado = False
    for producto in productos:
        if producto[0] == nombre_producto:
            nueva_cantidad = input("Ingrese la nueva cantidad: ")
            producto[2] = nueva_cantidad  # Modificar la cantidad en el producto encontrado
            encontrado = True
            break
    
    if encontrado:
        guardar_archivo(productos)
        time.sleep(1)
        print("Cantidad modificada con éxito.")
    else:
        print(f"Producto '{nombre_producto}' no encontrado en el stock.")

# Ejemplo de uso
def main():
    productos = cargar_archivo()
    if not productos:
        print(f"No se encontraron productos en '{stock}'")
        return
    
    while True:
        print("\n1. Mostrar stock")
        print("2. Modificar cantidad de un producto")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_stock(productos)
        elif opcion == "2":
            modificar_cantidad(productos)
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()