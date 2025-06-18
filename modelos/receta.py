"""
Clase Receta - Representa una receta médica
"""
from datetime import datetime
from typing import List
from .paciente import Paciente
from .medico import Medico

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: List[str]):
        """
        Constructor de la clase Receta
        
        Args:
            paciente: Paciente al que se le emite la receta
            medico: Médico que emite la receta
            medicamentos: Lista de medicamentos recetados
        """
        # Validaciones
        if not isinstance(paciente, Paciente):
            raise TypeError("Se esperaba un objeto de tipo Paciente")
        if not isinstance(medico, Medico):
            raise TypeError("Se esperaba un objeto de tipo Medico")
        if not medicamentos:
            raise ValueError("La lista de medicamentos no puede estar vacía")
        
        # Validar que todos los medicamentos tengan contenido
        medicamentos_limpios = []
        for med in medicamentos:
            if med and med.strip():
                medicamentos_limpios.append(med.strip())
        
        if not medicamentos_limpios:
            raise ValueError("La lista de medicamentos no puede contener solo valores vacíos")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos_limpios
        self.__fecha = datetime.now()
    
    def agregar_receta(self, receta):
        """Agrega una receta (método para compatibilidad)"""
        # Este método existe para mantener compatibilidad con el diseño
        pass
    
    def __str__(self) -> str:
        """Devuelve una representación en cadena de la receta"""
        medicamentos_str = ", ".join(self.__medicamentos)
        return (f"Receta(Paciente({self.__paciente}), "
                f"Medico({self.__medico}), "
                f"[{medicamentos_str}], "
                f"{self.__fecha})")