import unittest
from datetime import datetime
from modelos import Turno, Paciente, Medico, Especialidad

class TestTurno(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.paciente = Paciente("Juan Pérez", "12345678", "01/01/1990")
        especialidad = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.medico = Medico("Dr. García", "54321", [especialidad])
        self.fecha_hora = datetime(2025, 12, 10, 14, 30)
    
    def test_crear_turno_exitoso(self):
        """Test para crear turno con datos válidos"""
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Pediatría")
        self.assertEqual(turno.obtener_medico(), self.medico)
        self.assertEqual(turno.obtener_fecha_hora(), self.fecha_hora)
    
    def test_crear_turno_paciente_invalido(self):
        """Test para verificar error con paciente inválido"""
        with self.assertRaises(TypeError):
            Turno("paciente_string", self.medico, self.fecha_hora, "Pediatría")
    
    def test_crear_turno_medico_invalido(self):
        """Test para verificar error con médico inválido"""
        with self.assertRaises(TypeError):
            Turno(self.paciente, "medico_string", self.fecha_hora, "Pediatría")
    
    def test_crear_turno_fecha_invalida(self):
        """Test para verificar error con fecha inválida"""
        with self.assertRaises(TypeError):
            Turno(self.paciente, self.medico, "2025-12-10", "Pediatría")
    
    def test_crear_turno_sin_especialidad(self):
        """Test para verificar error sin especialidad"""
        with self.assertRaises(ValueError):
            Turno(self.paciente, self.medico, self.fecha_hora, "")

if __name__ == '__main__':
    unittest.main()