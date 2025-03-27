# Directorio Telefónico

Este proyecto es un sistema de directorio telefónico implementado en Python utilizando programación orientada a objetos. Permite gestionar contactos de manera eficiente, incluyendo funcionalidades para agregar, buscar, eliminar y mostrar contactos.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
directorio-telefonico
├── src
│   ├── __init__.py          # Indica que src es un paquete de Python
│   ├── contacto.py          # Define la clase Contacto
│   ├── directorio.py        # Define la clase Directorio
│   ├── main.py              # Punto de entrada del programa
│   └── utils.py             # Funciones de validación
├── data
│   └── contactos.json       # Almacena los contactos en formato JSON
├── requirements.txt         # Lista de dependencias del proyecto
└── README.md                # Documentación del proyecto
```

## Funcionalidades

- **Agregar Contactos**: Permite al usuario añadir nuevos contactos al directorio.
- **Buscar Contactos**: Facilita la búsqueda de contactos por nombre, teléfono o área.
- **Eliminar Contactos**: Permite eliminar contactos existentes del directorio.
- **Mostrar Contactos**: Muestra todos los contactos almacenados en el directorio.
- **Persistencia de Datos**: Utiliza archivos JSON para almacenar los contactos, asegurando que los datos se mantengan entre ejecuciones del programa.

## Desafíos Encontrados

Durante el desarrollo del proyecto, se presentaron varios desafíos, incluyendo:

- Implementación de validaciones para asegurar que los datos ingresados sean correctos.
- Manejo de excepciones al trabajar con archivos para garantizar que el programa no falle ante errores de lectura o escritura.
- Creación de una interfaz de usuario amigable para facilitar la interacción con el sistema.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instaladas las dependencias listadas en el archivo `requirements.txt`. Puedes instalar las dependencias utilizando el siguiente comando:

```
pip install -r requirements.txt
```

## Uso

Para iniciar el programa, ejecuta el archivo `main.py` desde la línea de comandos:

```
python src/main.py
```

Esto abrirá un menú interactivo donde podrás gestionar tu directorio telefónico.