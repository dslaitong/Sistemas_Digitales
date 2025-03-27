import json
import re
from datetime import datetime
from contacto import Contacto

class ContactManager:
    def __init__(self):
        self.contacts = []
        self.phone_index = {}
        self.id_index = {}
        self.area_index = {}
        self.valid_areas = ["Ventas", "Soporte", "Desarrollo", "Marketing", "Recursos Humanos"]

    def display_menu(self):
        while True:
            print("\n--- Gestor de Contactos ---")
            print("1. Añadir nuevo contacto")
            print("2. Buscar por teléfono")
            print("3. Buscar por ID")
            print("4. Buscar por área")
            print("5. Eliminar por ID")
            print("6. Eliminar por área")
            print("7. Eliminar por teléfono")
            print("8. Mostrar todos")
            print("9. Guardar datos")
            print("10. Cargar datos")
            print("11. Salir")
            
            choice = input("Seleccione una opción: ")
            
            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.search_by_phone()
            elif choice == "3":
                self.search_by_id()
            elif choice == "4":
                self.search_by_area()
            elif choice == "5":
                self.remove_by_id()
            elif choice == "6":
                self.remove_by_area()
            elif choice == "7":
                self.remove_by_phone()
            elif choice == "8":
                self.show_all()
            elif choice == "9":
                self.save_data()
            elif choice == "10":
                self.load_data()
            elif choice == "11":
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def add_contact(self):
        contact_data = {
            'id': input("Ingrese el ID del contacto: "),
            'nombre': input("Ingrese el nombre completo: "),
            'telefono': input("Ingrese el número de teléfono (10 dígitos): "),
            'fecha_nacimiento': input("Ingrese la fecha de nacimiento (YYYY-MM-DD): "),
            'correo': input("Ingrese el correo electrónico: ")
        }
        
        if not self._validate_phone(contact_data['telefono']):
            print("Número de teléfono inválido.")
            return
        if not self._validate_email(contact_data['correo']):
            print("Correo electrónico inválido.")
            return
        if not self._validate_birthdate(contact_data['fecha_nacimiento']):
            print("Fecha de nacimiento inválida.")
            return
        
        self._show_areas()
        area_choice = int(input("Seleccione el área (número): ")) - 1
        contact_data['area'] = self.valid_areas[area_choice]
        
        new_contact = Contacto(**contact_data)
        self._add_to_indexes(new_contact)
        print("Contacto añadido exitosamente.")

    def _show_areas(self):
        print("\nÁreas disponibles:")
        for idx, area in enumerate(self.valid_areas, 1):
            print(f"{idx}. {area}")

    def _add_to_indexes(self, contact):
        self.contacts.append(contact)
        self.phone_index[contact.telefono] = contact
        self.id_index[contact.id] = contact
        
        if contact.area not in self.area_index:
            self.area_index[contact.area] = []
        self.area_index[contact.area].append(contact)

    def search_by_phone(self):
        phone = input("Ingrese el número de teléfono: ")
        contact = self.phone_index.get(phone)
        print(contact if contact else "Contacto no encontrado.")

    def search_by_id(self):
        id = input("Ingrese el ID: ")
        contact = self.id_index.get(id)
        print(contact if contact else "Contacto no encontrado.")

    def search_by_area(self):
        area = input("Ingrese el área: ")
        contacts = self.area_index.get(area, [])
        if contacts:
            for contact in contacts:
                print(contact)
        else:
            print("No hay contactos en esa área.")

    def remove_by_id(self):
        id = input("Ingrese el ID: ")
        contact = self.id_index.get(id)
        if contact:
            self._remove_contact(contact)
            print("Contacto eliminado exitosamente.")
        else:
            print("Contacto no encontrado.")

    def remove_by_phone(self):
        phone = input("Ingrese el número de teléfono: ")
        contact = self.phone_index.get(phone)
        if contact:
            self._remove_contact(contact)
            print("Contacto eliminado exitosamente.")
        else:
            print("Contacto no encontrado.")

    def remove_by_area(self):
        print("Áreas disponibles:", ", ".join(self.valid_areas))
        area = input("Ingrese el área que desea eliminar: ")
        if area in self.area_index:
            for contact in self.area_index[area][:]:
                self._remove_contact(contact)
            print(f"Todos los contactos del área '{area}' han sido eliminados.")
        else:
            print(f"No hay contactos en el área '{area}'.")

    def _remove_contact(self, contact):
        self.contacts.remove(contact)
        del self.phone_index[contact.telefono]
        del self.id_index[contact.id]
        self.area_index[contact.area].remove(contact)
        if not self.area_index[contact.area]:
            del self.area_index[contact.area]

    def show_all(self):
        if not self.contacts:
            print("No hay contactos registrados.")
            return
            
        for contact in sorted(self.contacts, key=lambda x: x.nombre):
            print(contact)

    def save_data(self):
        filename = input("Ingrese el nombre del archivo: ")
        data = [vars(contact) for contact in self.contacts]
        with open(filename, 'w') as f:
            json.dump(data, f)
        print("Datos guardados exitosamente.")

    def load_data(self):
        filename = input("Ingrese el nombre del archivo: ")
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            for contact_data in data:
                contact = Contacto(**contact_data)
                self._add_to_indexes(contact)
            print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

    def _validate_phone(self, phone):
        return re.match(r"^\d{10}$", phone) is not None

    def _validate_email(self, email):
        return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email) is not None

    def _validate_birthdate(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False