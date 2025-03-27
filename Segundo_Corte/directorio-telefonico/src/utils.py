def validar_telefono(telefono):
    if len(telefono) != 10 or not telefono.isdigit():
        raise ValueError("El número de teléfono debe tener 10 dígitos y solo contener números.")
    return True

def validar_correo(correo):
    import re
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(patron, correo):
        raise ValueError("El correo electrónico no es válido.")
    return True

def validar_fecha_nacimiento(fecha):
    from datetime import datetime
    try:
        datetime.strptime(fecha, '%Y-%m-%d')
    except ValueError:
        raise ValueError("La fecha de nacimiento debe estar en el formato YYYY-MM-DD.")
    return True