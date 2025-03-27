class Contacto:
    def __init__(self, id, nombre, telefono, fecha_nacimiento, correo, area):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.area = area

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}, Fecha de Nacimiento: {self.fecha_nacimiento}, Correo: {self.correo}, Área: {self.area}"


class Directorio:
    def __init__(self):
        self.contactos = []
        self.indice_telefonos = {}
        self.indice_ids = {}
        self.indice_areas = {}
        self.areas = set()

    def agregar_contacto(self, contacto):
        if contacto.telefono in self.indice_telefonos:
            raise ValueError("El teléfono ya está registrado.")
        if contacto.id in self.indice_ids:
            raise ValueError("El ID ya está registrado.")
        
        self.contactos.append(contacto)
        self.indice_telefonos[contacto.telefono] = contacto
        self.indice_ids[contacto.id] = contacto
        self.indice_areas.setdefault(contacto.area, []).append(contacto)
        self.areas.add(contacto.area)

    def buscar_contacto(self, id=None, telefono=None):
        if id:
            return self.indice_ids.get(id, None)
        if telefono:
            return self.indice_telefonos.get(telefono, None)
        return None

    def eliminar_contacto(self, id):
        contacto = self.indice_ids.pop(id, None)
        if contacto:
            self.contactos.remove(contacto)
            del self.indice_telefonos[contacto.telefono]
            self.indice_areas[contacto.area].remove(contacto)
            if not self.indice_areas[contacto.area]:
                del self.indice_areas[contacto.area]
                self.areas.remove(contacto.area)

    def mostrar_contactos(self):
        return [str(contacto) for contacto in self.contactos]

    def cargar_contactos(self, archivo):
        import json
        with open(archivo, 'r') as f:
            datos = json.load(f)
            for dato in datos:
                contacto = Contacto(**dato)
                self.agregar_contacto(contacto)

    def guardar_contactos(self, archivo):
        import json
        with open(archivo, 'w') as f:
            json.dump([contacto.__dict__ for contacto in self.contactos], f)