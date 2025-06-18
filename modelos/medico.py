"""
Clase Medico - Representa a un médico del sistema
"""
from typing import List, Optional
from .especialidad import Especialidad

class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: List[Especialidad] = None):
        """
        Constructor de la clase Medico
        
        Args:
            nombre: Nombre completo del médico
            matricula: Matrícula profesional del médico (clave única)
            especialidades: Lista de especialidades con sus días de atención
        """
        # Validaciones
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del médico no puede estar vacío")
        if not matricula or not matricula.strip():
            raise ValueError("La matrícula del médico no puede estar vacía")
        
        self.__nombre = nombre.strip()
        self.__matricula = matricula.strip()
        self.__especialidades = especialidades if especialidades is not None else []
    
    def agregar_especialidad(self, especialidad: Especialidad):
        """Agrega una especialidad a la lista del médico"""
        if not isinstance(especialidad, Especialidad):
            raise TypeError("Se esperaba un objeto de tipo Especialidad")
        
        # Verificar que no exista ya la especialidad
        for esp in self.__especialidades:
            if esp.obtener_especialidad() == especialidad.obtener_especialidad():
                raise ValueError(f"La especialidad {especialidad.obtener_especialidad()} ya existe para este médico")
        
        self.__especialidades.append(especialidad)
    
    def obtener_matricula(self) -> str:
        """Devuelve la matrícula del médico"""
        return self.__matricula
    
    def obtener_especialidad_para_dia(self, dia: str) -> Optional[str]:
        """Devuelve el nombre de la especialidad disponible en el día especificado"""
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia):
                return especialidad.obtener_especialidad()
        return None
    
    def obtener_especialidades(self) -> List[Especialidad]:
        """Devuelve la lista de especialidades del médico"""
        return self.__especialidades.copy()
    
    def __str__(self) -> str:
        """Devuelve una representación legible del médico"""
        if self.__especialidades:
            especialidades_str = ", ".join([str(esp) for esp in self.__especialidades])
            return f"{self.__nombre}, {self.__matricula}, [{especialidades_str}]"
        else:
            return f"{self.__nombre}, {self.__matricula}, []"