# cli/interfaz_consola.py
from datetime import datetime
from modelos.clinica      import Clinica
from modelos.paciente     import Paciente
from modelos.medico       import Medico
from modelos.especialidad import Especialidad
from excepciones.excepciones_clinica import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException,
)

class CLI:
    """Interfaz de línea de comandos"""

    def __init__(self) -> None:
        self.clinica = Clinica()

    # ---------------------- MENÚ ----------------------
    def mostrar_menu(self) -> None:
        print(
            "\n--- Menú Clínica ---",
            "\n1) Agregar paciente",
            "2) Agregar médico",
            "3) Agendar turno",
            "4) Agregar especialidad",
            "5) Emitir receta",
            "6) Ver historia clínica",
            "7) Ver todos los turnos",
            "8) Ver todos los pacientes",
            "9) Ver todos los médicos",
            "0) Salir",
            sep="\n",
        )

    def ejecutar(self) -> None:
        while True:
            self.mostrar_menu()
            opcion = input("\nSeleccione una opción: ").strip()

            if not opcion.isdigit():
                print("\nDebe ingresar un número (0-9). Intente nuevamente.")
                continue

            match opcion:
                case "0":  print("\n¡Hasta luego!"); break
                case "1":  self.agregar_paciente()
                case "2":  self.agregar_medico()
                case "3":  self.agendar_turno()
                case "4":  self.agregar_especialidad()
                case "5":  self.emitir_receta()
                case "6":  self.ver_historia_clinica()
                case "7":  self.ver_todos_turnos()
                case "8":  self.ver_todos_pacientes()
                case "9":  self.ver_todos_medicos()
                case _:    print("\nOpción inválida. Intente nuevamente.")

    # ------------------ PACIENTES ------------------
    def agregar_paciente(self) -> None:
        print("\n--- Agregar Paciente ---")
        try:
            nombre = input("Nombre completo: ").strip()
            dni = input("DNI: ").strip()
            fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()

            datetime.strptime(fecha_nac, "%d/%m/%Y")  # Valida formato
            paciente = Paciente(nombre, dni, fecha_nac)
            self.clinica.agregar_paciente(paciente)
            print(f"\nPaciente agregado exitosamente: {paciente}")

        except ValueError:
            print("\nError: El formato de fecha debe ser dd/mm/aaaa")
        except Exception as e:
            print(f"\nError al agregar paciente: {e}")

    # -------------------- MÉDICOS --------------------
    def agregar_medico(self) -> None:
        print("\n--- Agregar Médico ---")
        try:
            nombre = input("Nombre completo: ").strip()
            matricula = input("Matrícula: ").strip()

            especialidades = []
            while True:
                if input("\n¿Agregar especialidad? (s/n): ").strip().lower() != "s":
                    break
                tipo = input("Tipo de especialidad: ").strip()
                dias = [
                    d.strip().lower()
                    for d in input("Días de atención (separados por coma): ").split(",")
                    if d.strip()
                ]
                especialidades.append(Especialidad(tipo, dias))

            medico = Medico(nombre, matricula, especialidades)
            self.clinica.agregar_medico(medico)
            print(f"\nMédico agregado exitosamente: {medico}")

        except Exception as e:
            print(f"\nError al agregar médico: {e}")

    # -------------------- TURNOS --------------------
    def agendar_turno(self) -> None:
        print("\n--- Agendar Turno ---")
        try:
            dni        = input("DNI del paciente: ").strip()
            matricula  = input("Matrícula del médico: ").strip()
            especialidad = input("Especialidad: ").strip()

            fecha_str = input("Fecha del turno (dd/mm/aaaa): ").strip()
            hora_str  = input("Horario del turno (hora:minutos): ").strip()

            fecha_hora = datetime.strptime(f"{fecha_str} {hora_str}", "%d/%m/%Y %H:%M")
            self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
            print("\nTurno agendado exitosamente")

        except ValueError:
            print("\nFormato incorrecto. Use dd/mm/aaaa y hora:minutos")
        except (
            PacienteNoEncontradoException,
            MedicoNoDisponibleException,
            TurnoOcupadoException,
        ) as e:
            print(f"\nError al agendar turno: {e}")

    # ------------ ESPECIALIDAD A MÉDICO -------------
    def agregar_especialidad(self) -> None:
        print("\n--- Agregar Especialidad a Médico ---")
        try:
            matricula = input("Matrícula del médico: ").strip()
            medico = self.clinica.obtener_medico_por_matricula(matricula)

            tipo = input("Tipo de especialidad: ").strip()
            dias = [
                d.strip().lower()
                for d in input("Días de atención (separados por coma): ").split(",")
                if d.strip()
            ]
            medico.agregar_especialidad(Especialidad(tipo, dias))
            print(f"\nEspecialidad agregada exitosamente al médico: {medico}")

        except (MedicoNoDisponibleException, ValueError) as e:
            print(f"\nError al agregar especialidad: {e}")

    # -------------------- RECETAS --------------------
    def emitir_receta(self) -> None:
        print("\n--- Emitir Receta ---")
        try:
            dni       = input("DNI del paciente: ").strip()
            matricula = input("Matrícula del médico: ").strip()

            medicamentos: list[str] = []
            while True:
                med = input("Medicamento (ENTER para terminar): ").strip()
                if not med:
                    if not medicamentos:            # ← Insiste si la lista está vacía
                        print("Debe ingresar al menos un medicamento.")
                        continue
                    break
                medicamentos.append(med)

            self.clinica.emitir_receta(dni, matricula, medicamentos)
            print("\nReceta emitida exitosamente")

        except (
            PacienteNoEncontradoException,
            MedicoNoDisponibleException,
            RecetaInvalidaException,
        ) as e:
            print(f"\nError al emitir receta: {e}")

    # ----------------- HISTORIA / LISTADOS -----------------
    def ver_historia_clinica(self) -> None:
        print("\n--- Ver Historia Clínica ---")
        try:
            dni = input("DNI del paciente: ").strip()
            historia = self.clinica.obtener_historia_clinica_por_dni(dni)
            print(f"\n{historia}")
        except PacienteNoEncontradoException as e:
            print(f"\nError: {e}")

    def ver_todos_turnos(self) -> None:
        print("\n--- Todos los Turnos ---")
        turnos = self.clinica.obtener_turnos()
        if turnos:
            for i, t in enumerate(turnos, 1):
                print(f"{i}. {t}")
        else:
            print("No hay turnos agendados")

    def ver_todos_pacientes(self) -> None:
        print("\n--- Todos los Pacientes ---")
        pacientes = self.clinica.obtener_pacientes()
        if pacientes:
            for i, p in enumerate(pacientes, 1):
                print(f"{i}. {p}")
        else:
            print("No hay pacientes registrados")

    def ver_todos_medicos(self) -> None:
        print("\n--- Todos los Médicos ---")
        medicos = self.clinica.obtener_medicos()
        if medicos:
            for i, m in enumerate(medicos, 1):
                print(f"{i}. {m}")
        else:
            print("No hay médicos registrados")