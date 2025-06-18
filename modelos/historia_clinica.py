"""
Clase HistoriaClinica - Representa la historia clínica de un paciente
"""
from typing import List
from .paciente import Paciente
from .turno import Turno
from .receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        """
        Constructor de la clase HistoriaClinica
        
        Args:
            paciente: Paciente al que pertenece la historia clínica
        """
        if not isinstance(paciente, Paciente):
            raise TypeError("Se esperaba un objeto de tipo Paciente")
        
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []
    
    def agregar_turno(self, turno: Turno):
        """Agrega un nuevo turno a la historia clínica"""
        if not isinstance(turno, Turno):
            raise TypeError("Se esperaba un objeto de tipo Turno")
        
        self.__turnos.append(turno)
    
    def agregar_receta(self, receta: Receta):
        """Agrega una nueva receta a la historia clínica"""
        if not isinstance(receta, Receta):
            raise TypeError("Se esperaba un objeto de tipo Receta")
        
        self.__recetas.append(receta)
    
    def obtener_turnos(self) -> List[Turno]:
        """Devuelve una copia de la lista de turnos del paciente"""
        return self.__turnos.copy()
    
    def obtener_recetas(self) -> List[Receta]:
        """Devuelve una copia de la lista de recetas del paciente"""
        return self.__recetas.copy()
    
    def __str__(self) -> str:
        """Devuelve una representación textual de la historia clínica"""
        elementos = []
        elementos.extend(self.__turnos)
        elementos.extend(self.__recetas)
        
        if elementos:
            elementos_str = ",\n    ".join([str(elem) for elem in elementos])
            return (f"HistoriaClinica(Paciente({self.__paciente}),\n"
                   f"  [\n    {elementos_str}\n  ]\n)")
        else:
            return f"HistoriaClinica(Paciente({self.__paciente}),\n  []\n)"