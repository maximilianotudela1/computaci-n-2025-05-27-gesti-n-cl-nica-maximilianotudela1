import unittest
from datetime import datetime
from modelos import Clinica, Paciente, Medico, Especialidad
from excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestClinica(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Pérez", "12345678", "01/01/1990")
        self.especialidad = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.medico = Medico("Dr. García", "54321", [self.especialidad])
    
    def test_agregar_paciente_exitoso(self):
        """Test para agregar paciente exitosamente"""
        self.clinica.agregar_paciente(self.paciente)
        pacientes = self.clinica.obtener_pacientes()
        self.assertEqual(len(pacientes), 1)
        self.assertEqual(pacientes[0].obtener_dni(), "12345678")
    
    def test_agregar_paciente_duplicado(self):
        """Test para verificar error al agregar paciente duplicado"""
        self.clinica.agregar_paciente(self.paciente)
        with self.assertRaises(ValueError) as context:
            self.clinica.agregar_paciente(self.paciente)
        self.assertIn("Ya existe", str(context.exception))
    
    def test_agregar_medico_exitoso(self):
        """Test para agregar médico exitosamente"""
        self.clinica.agregar_medico(self.medico)
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(medicos), 1)
        self.assertEqual(medicos[0].obtener_matricula(), "54321")
    
    def test_agregar_medico_duplicado(self):
        """Test para verificar error al agregar médico duplicado"""
        self.clinica.agregar_medico(self.medico)
        with self.assertRaises(ValueError) as context:
            self.clinica.agregar_medico(self.medico)
        self.assertIn("Ya existe", str(context.exception))
    
    def test_agendar_turno_exitoso(self):
        """Test para agendar turno exitosamente"""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        
        # Agendar para un lunes (día que atiende el médico)
        fecha_lunes = datetime(2025, 12, 8, 14, 30)  # 8 de dic 2025 es lunes
        self.clinica.agendar_turno("12345678", "54321", "Pediatría", fecha_lunes)
        
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
    
    def test_agendar_turno_paciente_no_existe(self):
        """Test para verificar error cuando paciente no existe"""
        self.clinica.agregar_medico(self.medico)
        fecha = datetime(2025, 12, 8, 14, 30)
        
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "54321", "Pediatría", fecha)
    
    def test_agendar_turno_medico_no_existe(self):
        """Test para verificar error cuando médico no existe"""
        self.clinica.agregar_paciente(self.paciente)
        fecha = datetime(2025, 12, 8, 14, 30)
        
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "99999", "Pediatría", fecha)
    
    def test_agendar_turno_dia_no_disponible(self):
        """Test para verificar error cuando médico no atiende ese día"""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        
        # Intentar agendar un martes (día que NO atiende pediatría)
        fecha_martes = datetime(2025, 12, 9, 14, 30)
        
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("12345678", "54321", "Pediatría", fecha_martes)
    
    def test_agendar_turno_duplicado(self):
        """Test para verificar error al agendar turno duplicado"""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        
        fecha = datetime(2025, 12, 8, 14, 30)
        self.clinica.agendar_turno("12345678", "54321", "Pediatría", fecha)
        
        # Intentar agendar otro turno en la misma fecha/hora
        paciente2 = Paciente("María García", "87654321", "15/05/1985")
        self.clinica.agregar_paciente(paciente2)
        
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("87654321", "54321", "Pediatría", fecha)
    
    def test_emitir_receta_exitoso(self):
        """Test para emitir receta exitosamente"""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        
        medicamentos = ["Paracetamol", "Ibuprofeno"]
        self.clinica.emitir_receta("12345678", "54321", medicamentos)
        
        historia = self.clinica.obtener_historia_clinica_por_dni("12345678")
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
    
    def test_emitir_receta_sin_medicamentos(self):
        """Test para verificar error al emitir receta sin medicamentos"""
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("12345678", "54321", [])
    
    def test_obtener_historia_clinica_exitoso(self):
        """Test para obtener historia clínica exitosamente"""
        self.clinica.agregar_paciente(self.paciente)
        historia = self.clinica.obtener_historia_clinica_por_dni("12345678")
        self.assertIsNotNone(historia)
    
    def test_obtener_historia_clinica_paciente_no_existe(self):
        """Test para verificar error al obtener historia de paciente inexistente"""
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.obtener_historia_clinica_por_dni("99999999")
    
    def test_obtener_dia_semana_espanol(self):
        """Test para verificar traducción de días de la semana"""
        fecha_lunes = datetime(2025, 12, 8, 14, 30)
        fecha_martes = datetime(2025, 12, 9, 14, 30)
        fecha_domingo = datetime(2025, 12, 14, 14, 30)
        
        self.assertEqual(self.clinica.obtener_dia_semana_en_espanol(fecha_lunes), "lunes")
        self.assertEqual(self.clinica.obtener_dia_semana_en_espanol(fecha_martes), "martes")
        self.assertEqual(self.clinica.obtener_dia_semana_en_espanol(fecha_domingo), "domingo")

if __name__ == '__main__':
    unittest.main()