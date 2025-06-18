import unittest
from modelos import Paciente

class TestPaciente(unittest.TestCase):
    
    def test_crear_paciente_exitoso(self):
        """Test para crear un paciente con datos válidos"""
        paciente = Paciente("Juan Pérez", "12345678", "01/01/1990")
        self.assertEqual(paciente.obtener_dni(), "12345678")
        self.assertEqual(str(paciente), "Juan Pérez, 12345678, 01/01/1990")
    
    def test_crear_paciente_sin_nombre(self):
        """Test para verificar error cuando no se proporciona nombre"""
        with self.assertRaises(ValueError) as context:
            Paciente("", "12345678", "01/01/1990")
        self.assertIn("nombre", str(context.exception).lower())
    
    def test_crear_paciente_sin_dni(self):
        """Test para verificar error cuando no se proporciona DNI"""
        with self.assertRaises(ValueError) as context:
            Paciente("Juan Pérez", "", "01/01/1990")
        self.assertIn("dni", str(context.exception).lower())
    
    def test_crear_paciente_sin_fecha_nacimiento(self):
        """Test para verificar error cuando no se proporciona fecha de nacimiento"""
        with self.assertRaises(ValueError) as context:
            Paciente("Juan Pérez", "12345678", "")
        self.assertIn("fecha", str(context.exception).lower())
    
    def test_crear_paciente_fecha_invalida(self):
        """Test para verificar error con formato de fecha inválido"""
        with self.assertRaises(ValueError) as context:
            Paciente("Juan Pérez", "12345678", "01-01-1990")
        self.assertIn("formato", str(context.exception).lower())
    
    def test_crear_paciente_fecha_invalida_mes(self):
        """Test para verificar error con mes inválido"""
        with self.assertRaises(ValueError) as context:
            Paciente("Juan Pérez", "12345678", "01/13/1990")
        self.assertIn("formato", str(context.exception).lower())

if __name__ == '__main__':
    unittest.main()