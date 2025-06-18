"""
Clase Especialidad - Representa una especialidad médica con sus días de atención
"""
from typing import List

class Especialidad:
    def __init__(self, tipo: str, dias: List[str]):
        """
        Constructor de la clase Especialidad
        
        Args:
            tipo: Nombre de la especialidad (ej: "Pediatría", "Cardiología")
            dias: Lista de días en que se atiende esta especialidad
        """
        # Validaciones
        if not tipo or not tipo.strip():
            raise ValueError("El tipo de especialidad no puede estar vacío")
        if not dias:
            raise ValueError("La lista de días no puede estar vacía")
        
        # Validar días de la semana
        dias_validos = ['lunes', 'martes', 'miércoles', 'miercoles', 'jueves', 'viernes', 'sábado', 'sabado', 'domingo']
        dias_lower = [dia.lower() for dia in dias]
        
        for dia in dias_lower:
            if dia not in dias_validos:
                raise ValueError(f"Día inválido: {dia}")
        
        self.__tipo = tipo.strip()
        self.__dias = dias_lower
    
    def obtener_especialidad(self) -> str:
        """Devuelve el nombre de la especialidad"""
        return self.__tipo
    
    def verificar_dia(self, dia: str) -> bool:
        """Verifica si la especialidad está disponible en el día proporcionado"""
        # Normalizar 'miércoles' con y sin tilde
        dia_normalizado = dia.lower()
        if dia_normalizado == 'miércoles':
            return 'miércoles' in self.__dias or 'miercoles' in self.__dias
        elif dia_normalizado == 'miercoles':
            return 'miércoles' in self.__dias or 'miercoles' in self.__dias
        return dia_normalizado in self.__dias
    
    def __str__(self) -> str:
        """Devuelve una cadena legible con el nombre y días de atención"""
        dias_str = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias_str})"