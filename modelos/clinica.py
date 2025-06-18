"""
Clase Clinica - Clase principal que representa el sistema de gestión
"""
from typing import Dict, List, Optional
from datetime import datetime

from .paciente          import Paciente
from .medico            import Medico
from .turno             import Turno
from .receta            import Receta
from .historia_clinica  import HistoriaClinica
from .especialidad      import Especialidad

# ------------------------------------------------------------
# Excepciones
# ------------------------------------------------------------
try:
    from excepciones.excepciones_clinica import (
        PacienteNoEncontradoException,
        MedicoNoDisponibleException,
        TurnoOcupadoException,
        RecetaInvalidaException,
    )
except ImportError:  # ejecución fuera del paquete
    import os, sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from excepciones.excepciones_clinica import (
        PacienteNoEncontradoException,
        MedicoNoDisponibleException,
        TurnoOcupadoException,
        RecetaInvalidaException,
    )


class Clinica:
    def __init__(self) -> None:
        """Constructor de la clase Clinica"""
        self.__pacientes: Dict[str, Paciente] = {}
        self.__medicos: Dict[str, Medico] = {}
        self.__turnos: List[Turno] = []
        self.__historias_clinicas: Dict[str, HistoriaClinica] = {}

    # ============================================================
    # REGISTRO DE PACIENTES Y MÉDICOS
    # ============================================================
    def agregar_paciente(self, paciente: Paciente) -> None:
        """Registra un paciente y crea su historia clínica"""
        if not isinstance(paciente, Paciente):
            raise TypeError("Se esperaba un objeto de tipo Paciente")

        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError(f"Ya existe un paciente con DNI {dni}")

        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico: Medico) -> None:
        """Registra un médico"""
        if not isinstance(medico, Medico):
            raise TypeError("Se esperaba un objeto de tipo Medico")

        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError(f"Ya existe un médico con matrícula {matricula}")

        self.__medicos[matricula] = medico

    # ============================================================
    # TURNOS
    # ============================================================
    def agendar_turno(
        self,
        dni: str,
        matricula: str,
        especialidad: str,
        fecha_hora: datetime,
    ) -> None:
        """Agenda un turno si se cumplen todas las condiciones"""

        # Validar existencia de paciente y médico
        if not self.validar_existencia_paciente(dni):
            raise PacienteNoEncontradoException(
                f"No existe un paciente con DNI {dni}"
            )

        if not self.validar_existencia_medico(matricula):
            raise MedicoNoDisponibleException(
                f"No existe un médico con matrícula {matricula}"
            )

        paciente = self.__pacientes[dni]
        medico   = self.__medicos[matricula]

        # Turno duplicado
        if not self.validar_turno_no_duplicado(matricula, fecha_hora):
            raise TurnoOcupadoException(
                "Ya existe un turno para ese médico en esa fecha y hora"
            )

        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)

        # Especialidad y día
        if not self.validar_especialidad_en_dia(medico, especialidad, dia_semana):
            raise MedicoNoDisponibleException(
                f"El médico no atiende la especialidad {especialidad} los días {dia_semana}"
            )

        # Crear y registrar el turno
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    # ============================================================
    # RECETAS
    # ============================================================
    def emitir_receta(
        self,
        dni: str,
        matricula: str,
        medicamentos: List[str],
    ) -> None:
        """
        Emite una receta para un paciente y la guarda en su historia clínica.
        Lanza:
            • RecetaInvalidaException    si la lista de medicamentos está vacía.
            • PacienteNoEncontradoException si el DNI no existe.
            • MedicoNoDisponibleException   si la matrícula no existe.
        """

        # 1) Validar medicamentos
        if not medicamentos:
            raise RecetaInvalidaException(
                "Debe indicar al menos un medicamento"
            )

        # 2) Validar existencia de paciente y médico
        if not self.validar_existencia_paciente(dni):
            raise PacienteNoEncontradoException(
                f"No existe un paciente con DNI {dni}"
            )

        if not self.validar_existencia_medico(matricula):
            raise MedicoNoDisponibleException(
                f"No existe un médico con matrícula {matricula}"
            )

        paciente = self.__pacientes[dni]
        medico   = self.__medicos[matricula]

        # 3) Crear y registrar la receta
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)

    # ============================================================
    # OBTENCIÓN DE INFORMACIÓN
    # ============================================================
    def obtener_pacientes(self) -> List[Paciente]:
        return list(self.__pacientes.values())

    def obtener_medicos(self) -> List[Medico]:
        return list(self.__medicos.values())

    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        if matricula not in self.__medicos:
            raise MedicoNoDisponibleException(
                f"No existe un médico con matrícula {matricula}"
            )
        return self.__medicos[matricula]

    def obtener_turnos(self) -> List[Turno]:
        return self.__turnos.copy()

    def obtener_historia_clinica_por_dni(self, dni: str) -> HistoriaClinica:
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(
                f"No existe un paciente con DNI {dni}"
            )
        return self.__historias_clinicas[dni]

    # ============================================================
    # VALIDACIONES INTERNAS
    # ============================================================
    def validar_existencia_paciente(self, dni: str) -> bool:
        return dni in self.__pacientes

    def validar_existencia_medico(self, matricula: str) -> bool:
        return matricula in self.__medicos

    def validar_turno_no_duplicado(
        self,
        matricula: str,
        fecha_hora: datetime,
    ) -> bool:
        for turno in self.__turnos:
            if (
                turno.obtener_medico().obtener_matricula() == matricula
                and turno.obtener_fecha_hora() == fecha_hora
            ):
                return False
        return True

    # Día de la semana en español
    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias_ingles_espanol = {
            "Monday":    "lunes",
            "Tuesday":   "martes",
            "Wednesday": "miércoles",
            "Thursday":  "jueves",
            "Friday":    "viernes",
            "Saturday":  "sábado",
            "Sunday":    "domingo",
        }
        return dias_ingles_espanol.get(
            fecha_hora.strftime("%A"),
            fecha_hora.strftime("%A").lower(),
        )

    # Comprueba que el médico atienda la especialidad solicitada ese día
    def validar_especialidad_en_dia(
        self,
        medico: Medico,
        especialidad_solicitada: str,
        dia_semana: str,
    ) -> bool:
        for esp in medico.obtener_especialidades():
            if (
                esp.obtener_especialidad() == especialidad_solicitada
                and esp.verificar_dia(dia_semana)
            ):
                return True
        return False