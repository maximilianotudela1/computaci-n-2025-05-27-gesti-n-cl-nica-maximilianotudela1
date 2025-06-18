"""
Clase Turno - Representa un turno médico
"""
from datetime import datetime
from .paciente import Paciente
from .medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        """
        Constructor de la clase Turno
        
        Args:
            paciente: Paciente que asiste al turno
            medico: Médico asignado al turno
            fecha_hora: Fecha y hora del turno
            especialidad: Especialidad para la cual se agendó el turno
        """
        # Validaciones
        if not isinstance(paciente, Paciente):
            raise TypeError("Se esperaba un objeto de tipo Paciente")
        if not isinstance(medico, Medico):
            raise TypeError("Se esperaba un objeto de tipo Medico")
        if not isinstance(fecha_hora, datetime):
            raise TypeError("Se esperaba un objeto de tipo datetime")
        if not especialidad or not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacía")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad.strip()
    
    def obtener_medico(self) -> Medico:
        """Devuelve el médico asignado al turno"""
        return self.__medico
    
    def obtener_fecha_hora(self) -> datetime:
        """Devuelve la fecha y hora del turno"""
        return self.__fecha_hora
    
    def __str__(self) -> str:
        """Devuelve una representación legible del turno"""
        return (f"Turno(Paciente({self.__paciente}), "
                f"Medico({self.__medico}), "
                f"{self.__fecha_hora}, "
                f"{self.__especialidad})")