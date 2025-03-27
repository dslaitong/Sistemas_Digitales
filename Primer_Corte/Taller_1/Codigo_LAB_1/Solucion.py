# Directorio Telefónico usando Listas y Diccionarios en Python

# Lista para almacenar la base de datos de personas (diccionarios)

directorio = []

# Lista de textos para mostrar en pantalla
textos = [
    "Digite el Nombre de la persona: ",
    "Digite el teléfono celular de la persona: ",
    "Digite el cumpleaños de la persona (DD/MM/AAAA): ",
    "Digite el correo de la persona: ",
    "Bienvenido al directorio telefónico",
    "Gracias por usar el directorio telefónico. ¡Hasta luego!",
    "Opción no válida. Intente de nuevo.",
    "Registro agregado exitosamente.",
    "No se encontró ninguna persona con ese teléfono celular.",
    "Registro borrado exitosamente.",
    "¿Está seguro que desea salir? (S/N): "
]

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar un nuevo registro")
    print("2. Buscar una persona por teléfono celular")
    print("3. Borrar un registro")
    print("4. Salir de la aplicación")

def agregar_persona():
    nombre = input(textos[0])
    telefono = input(textos[1])
    cumpleaños = input(textos[2])
    correo = input(textos[3])
    persona = {"nombre": nombre, "telefono": telefono, "cumpleaños": cumpleaños, "correo": correo}
    directorio.append(persona)  # Agregar el diccionario a la lista
    print("la nueva persona es: ",persona)
    print(textos[7])

def buscar_por_telefono():
    telefono = input("Ingrese el teléfono a buscar: ")
    for persona in directorio:
        if persona["telefono"] == telefono:
            print("\n--- Información encontrada ---")
            print(f"Nombrey Apellido: {persona['nombre']}")
            print(f"Cumpleaños: {persona['cumpleaños']}")
            print(f"Correo: {persona['correo']}")
            return
    print(textos[8])

def borrar_persona():
    telefono = input("Ingrese el teléfono de la persona a eliminar: ")
    for persona in directorio:
        if persona["telefono"] == telefono:
            directorio.remove(persona)
            print(textos[9])
            return
    print(textos[8])

def main():
    print(textos[4])
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_persona()
        elif opcion == "2":
            buscar_por_telefono()
        elif opcion == "3":
            borrar_persona()
        elif opcion == "4":
            salir = input(textos[10])
            if salir.lower() == "s":
                print(textos[5])
                break
        else:
            print(textos[6])

main()
