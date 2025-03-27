class Contacto:
    def __init__(self, id, nombre, telefono, fecha_nacimiento, correo, area):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento
        self.correo = correo
        self.area = area

    def __str__(self):
        return (f"ID: {self.id}\nNombre: {self.nombre}\nTeléfono: {self.telefono}\n"
                f"Fecha Nacimiento: {self.fecha_nacimiento}\nCorreo: {self.correo}\nÁrea: {self.area}\n")