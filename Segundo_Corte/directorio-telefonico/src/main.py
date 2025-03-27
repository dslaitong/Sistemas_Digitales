# main.py

from directorio import Directorio

def main():
    directorio = Directorio()
    directorio.cargar_contactos()

    while True:
        print("\n--- Menú del Directorio Telefónico ---")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar contactos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            directorio.agregar_contacto()
        elif opcion == '2':
            directorio.buscar_contacto()
        elif opcion == '3':
            directorio.eliminar_contacto()
        elif opcion == '4':
            directorio.mostrar_contactos()
        elif opcion == '5':
            directorio.guardar_contactos()
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()