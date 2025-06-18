import unittest
from modelos import Especialidad

class TestEspecialidad(unittest.TestCase):
    
    def test_crear_especialidad_exitoso(self):
        """Test para crear especialidad con datos válidos"""
        especialidad = Especialidad("Pediatría", ["lunes", "miércoles", "viernes"])
        self.assertEqual(especialidad.obtener_especialidad(), "Pediatría")
        self.assertTrue(especialidad.verificar_dia("lunes"))
        self.assertTrue(especialidad.verificar_dia("LUNES"))  # Case insensitive
        self.assertFalse(especialidad.verificar_dia("martes"))
    
    def test_crear_especialidad_sin_tipo(self):
        """Test para verificar error cuando no se proporciona tipo"""
        with self.assertRaises(ValueError) as context:
            Especialidad("", ["lunes"])
        self.assertIn("tipo", str(context.exception).lower())
    
    def test_crear_especialidad_sin_dias(self):
        """Test para verificar error cuando no se proporcionan días"""
        with self.assertRaises(ValueError) as context:
            Especialidad("Pediatría", [])
        self.assertIn("días", str(context.exception).lower())
    
    def test_crear_especialidad_dia_invalido(self):
        """Test para verificar error con día inválido"""
        with self.assertRaises(ValueError) as context:
            Especialidad("Pediatría", ["lunes", "invalid_day"])
        self.assertIn("inválido", str(context.exception).lower())
    
    def test_str_especialidad(self):
        """Test para verificar representación en string"""
        especialidad = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.assertEqual(str(especialidad), "Pediatría (Días: lunes, miércoles)")

if __name__ == '__main__':
    unittest.main()