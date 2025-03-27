class Estudiante: 
    def __init__ (self, nombre, universidad, materias): 
        self.nombre = nombre 
        self.universidad = universidad
        self.materias = materias 
    def presentarse (self): 
        materias_str="". join (self.materias) 
        return f"Hola, soy (self nombre), estudio en { self.universidad } y estoy inscrito en: (materias_str)."

if __name__ == "__main__": 
    estudiante1 = Estudiante("Carlos", "Universidad ECCI", ["Fisica", "Sistemas Digitales 3", "Matemáticas"]) 
    print(estudiante1.presentarse())