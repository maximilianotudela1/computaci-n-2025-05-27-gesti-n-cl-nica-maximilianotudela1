"""
Excepciones personalizadas para el sistema de gestión de clínica
"""

class PacienteNoEncontradoException(Exception):
    """Se lanza cuando no se encuentra un paciente en el sistema"""
    pass

class MedicoNoDisponibleException(Exception):
    """Se lanza cuando un médico no está disponible o no existe"""
    pass

class TurnoOcupadoException(Exception):
    """Se lanza cuando se intenta agendar un turno en un horario ya ocupado"""
    pass

class RecetaInvalidaException(Exception):
    """Se lanza cuando se intenta emitir una receta inválida"""
    pass