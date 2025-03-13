# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------



# --------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------


# Lista para almacenar los textos que se mostrarán en pantalla
textos = [
    "Bienvenido al directorio telefónico",
    "Digite el Nombre y Apellido de la persona: ",
    "Digite el teléfono celular de la persona: ",
    "Digite el cumpleaños de la persona (formato DD/MM/AAAA): ",
    "Digite el correo de la persona: ",
    "Gracias por usar el directorio telefónico. ¡Hasta luego!",
    "Opción no válida. Intente de nuevo.",
    "Registro agregado exitosamente.",
    "No se encontró ninguna persona con ese teléfono celular.",
    "Registro borrado exitosamente.",
    "¿Está seguro que desea salir? (S/N): "
]


# Lista para almacenar la información de las personas
directorio = []

# Diccionario temporal para almacenar la información de una persona
persona = {
    "Nombre y Apellido": "",
    "Teléfono": 0,
    "Cumpleaños": "",
    "Correo": ""
}

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar un nuevo registro")
    print("2. Buscar una persona por teléfono celular")
    print("3. Borrar un registro")
    print("4. Salir de la aplicación")
    opcion = input("Seleccione una opción: ")
    return opcion

# Función para agregar un nuevo registro
def agregar_registro():
    print("\n" + textos[1])
    persona["Nombre y Apellido"] = input(textos[1])
    persona["Teléfono"] = int(input(textos[2]))
    persona["Cumpleaños"] = input(textos[3])
    persona["Correo"] = input(textos[4])
    directorio.append(persona.copy())  # Se agrega una copia del diccionario a la lista
    print(textos[7])

# Función para buscar una persona por teléfono celular
def buscar_por_telefono():
    telefono = int(input("Digite el teléfono celular a buscar: "))
    encontrado = False
    for p in directorio:
        if p["Teléfono"] == telefono:
            print("\nInformación encontrada:")
            print(f"Nombre y Apellido: {p['Nombre y Apellido']}")
            print(f"Teléfono: {p['Teléfono']}")
            print(f"Cumpleaños: {p['Cumpleaños']}")
            print(f"Correo: {p['Correo']}")
            encontrado = True
            break
    if not encontrado:
        print(textos[8])

# Función para borrar un registro
def borrar_registro():
    telefono = int(input("Digite el teléfono celular del registro a borrar: "))
    encontrado = False
    for p in directorio:
        if p["Teléfono"] == telefono:
            directorio.remove(p)
            print(textos[9])
            encontrado = True
            break
    if not encontrado:
        print(textos[8])

# Función principal
def main():
    print(textos[0])  # Mensaje de bienvenida
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            agregar_registro()
        elif opcion == "2":
            buscar_por_telefono()
        elif opcion == "3":
            borrar_registro()
        elif opcion == "4":
            confirmacion = input(textos[10])
            if confirmacion.upper() == "S":
                print(textos[5])  # Mensaje de despedida
                break
            else:
                continue
        else:
            print(textos[6])  # Opción no válida

# Ejecutar el programa
if _name_ == "_main_":
    main()