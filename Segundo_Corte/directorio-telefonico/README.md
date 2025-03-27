# Directorio Telefónico

Este proyecto es un sistema de directorio telefónico implementado en Python utilizando programación orientada a objetos. Permite gestionar contactos de manera eficiente, incluyendo funcionalidades avanzadas como búsqueda, eliminación y persistencia de datos.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
directorio-telefonico
├── src
│   ├── __init__.py          # Indica que src es un paquete de Python
│   ├── contacto.py          # Define la clase Contacto
│   ├── directorio.py        # Define la clase ContactManager
│   ├── main.py              # Punto de entrada del programa
├── data
│   └── contactos.json       # Almacena los contactos en formato JSON
├── requirements.txt         # Lista de dependencias del proyecto
└── README.md                # Documentación del proyecto
```

## Funcionalidades

- **Añadir Contactos**: Permite al usuario añadir nuevos contactos al directorio.
- **Búsqueda Avanzada**:
  - Por teléfono.
  - Por ID.
  - Por área.
- **Eliminación de Contactos**:
  - Por ID.
  - Por teléfono.
  - Por área.
- **Mostrar Todos los Contactos**: Lista todos los contactos ordenados alfabéticamente por nombre.
- **Persistencia de Datos**:
  - Guardar contactos en un archivo JSON.
  - Cargar contactos desde un archivo JSON.
- **Validaciones**:
  - Validación de números de teléfono (10 dígitos).
  - Validación de correos electrónicos.
  - Validación de fechas de nacimiento (formato YYYY-MM-DD).

## Requisitos

Para ejecutar este proyecto, asegúrate de tener instaladas las dependencias listadas en el archivo `requirements.txt`. Puedes instalarlas utilizando el siguiente comando:

```
pip install -r requirements.txt
```

## Uso

Para iniciar el programa, ejecuta el archivo `main.py` desde la línea de comandos:

```
python src/main.py
```

Esto abrirá un menú interactivo donde podrás gestionar tu directorio telefónico.

## Áreas Disponibles

El sistema permite clasificar contactos en las siguientes áreas:

- Ventas
- Soporte
- Desarrollo
- Marketing
- Recursos Humanos

## Ejemplo de Uso

1. **Añadir un Contacto**:
   - Ingresa los datos solicitados, como ID, nombre, teléfono, fecha de nacimiento, correo y área.
   - El sistema validará los datos antes de añadir el contacto.

2. **Buscar un Contacto**:
   - Selecciona la opción de búsqueda (por teléfono, ID o área).
   - Ingresa el criterio de búsqueda y el sistema mostrará los resultados.

3. **Eliminar un Contacto**:
   - Selecciona la opción de eliminación (por ID, teléfono o área).
   - Ingresa el criterio correspondiente y el sistema eliminará el contacto.

4. **Guardar y Cargar Datos**:
   - Guarda los contactos en un archivo JSON para mantener la persistencia.
   - Carga los contactos desde un archivo JSON previamente guardado.

## Desafíos Resueltos

- Implementación de validaciones robustas para garantizar la integridad de los datos.
- Manejo eficiente de índices para búsquedas rápidas.
- Persistencia de datos utilizando archivos JSON.
- Diseño de un menú interactivo y fácil de usar.

## Contribuciones

Si deseas contribuir a este proyecto, por favor realiza un fork del repositorio, realiza tus cambios y envía un pull request.