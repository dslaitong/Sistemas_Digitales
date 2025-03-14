# Taller 1 - 📞 Directorio Telefónico en Python
En este apartado Vamos describir la documentacion del primer taller del primer corte

Este es un programa en Python que permite gestionar un directorio telefónico utilizando **listas y diccionarios**.


## 🚀 **Características del Programa**
✅ **Gestión de contactos**: Agregar, buscar y eliminar personas del directorio.  
✅ **Interfaz interactiva**: Menú dinámico con opciones claras y mensajes personalizados.  
✅ **Almacenamiento en memoria**: Uso de listas para gestionar la base de datos sin necesidad de archivos externos.  
✅ **Validación de datos**: Evita registros duplicados y proporciona mensajes adecuados en caso de errores.  

---

---

## 🛠 **Tecnologías Utilizadas**
- **Python 3** 🐍: Lenguaje principal del programa.
- **Listas y Diccionarios** 📄: Estructuras clave para almacenar información.
- **Programación Modular** 🔄: Uso de funciones organizadas para cada operación.

---

## 🎯 **Objetivo del Proyecto**
El objetivo es desarrollar un sistema funcional de gestión de contactos telefónicos, aplicando las bases de la **programación estructurada en Python** y el uso adecuado de **listas y diccionarios**.

---

## **Uso del Programa**

Cuando ejecutes el script, verás el siguiente menú de opciones en pantalla:

--- MENÚ PRINCIPAL ---
1. Agregar un nuevo registro
2. Buscar una persona por teléfono celular
3. Borrar un registro
4. Salir de la aplicación
Seleccione una opción:

-📌 Selecciona una opción escribiendo el número correspondiente y presionando Enter.

-📌 Para salir, selecciona la opción 4 y confirma escribiendo S.

📂 Estructura del Proyecto

La organización del código es la siguiente:

📂 Taller_1
 ├── 📜 Solucion.py   # Código fuente del programa
 ├── 📜 README.md     # Documentación del proyecto
 └── 📜  # instrucciones


## 🛠 Explicación del Código

El programa está dividido en varias funciones:

    - mostrar_menu() → Muestra las opciones disponibles.

    - agregar_persona() → Solicita datos y los guarda en el directorio.

    - buscar_por_telefono() → Busca un contacto por su número de teléfono.

    - borrar_persona() → Elimina un contacto del directorio.

    - main() → Controla el flujo principal del programa.

📌 Los datos de cada persona se almacenan en un diccionario, dentro de una lista global llamada directorio.

persona = {
    "nombre": "Juan Pérez",
    "telefono": "3001234567",
    "cumpleaños": "10/04/1995",
    "correo": "juanperez@email.com"
}
