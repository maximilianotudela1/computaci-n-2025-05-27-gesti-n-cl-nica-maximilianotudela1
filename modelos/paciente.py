"""
Clase Paciente - Representa a un paciente de la clínica
"""

class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        """
        Constructor de la clase Paciente
        
        Args:
            nombre: Nombre completo del paciente
            dni: DNI del paciente (identificador único)
            fecha_nacimiento: Fecha de nacimiento en formato dd/mm/aaaa
        """
        # Validaciones
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del paciente no puede estar vacío")
        if not dni or not dni.strip():
            raise ValueError("El DNI del paciente no puede estar vacío")
        if not fecha_nacimiento or not fecha_nacimiento.strip():
            raise ValueError("La fecha de nacimiento no puede estar vacía")
        
        # Validar formato de fecha
        if not self._validar_formato_fecha(fecha_nacimiento):
            raise ValueError("El formato de fecha debe ser dd/mm/aaaa")
        
        self.__nombre = nombre.strip()
        self.__dni = dni.strip()
        self.__fecha_nacimiento = fecha_nacimiento.strip()
    
    def _validar_formato_fecha(self, fecha: str) -> bool:
        """Valida que la fecha tenga el formato dd/mm/aaaa"""
        partes = fecha.split('/')
        if len(partes) != 3:
            return False
        
        try:
            dia, mes, anio = partes
            dia_int = int(dia)
            mes_int = int(mes)
            anio_int = int(anio)
            
            if dia_int < 1 or dia_int > 31:
                return False
            if mes_int < 1 or mes_int > 12:
                return False
            if anio_int < 1900 or anio_int > 2100:
                return False
            
            return True
        except ValueError:
            return False
    
    def obtener_dni(self) -> str:
        """Devuelve el DNI del paciente"""
        return self.__dni
    
    def __str__(self) -> str:
        """Devuelve una representación legible del paciente"""
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}"