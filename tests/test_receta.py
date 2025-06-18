import unittest
from modelos import Receta, Paciente, Medico, Especialidad

class TestReceta(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.paciente = Paciente("Juan Pérez", "12345678", "01/01/1990")
        especialidad = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.medico = Medico("Dr. García", "54321", [especialidad])
        self.medicamentos = ["Paracetamol", "Ibuprofeno"]
    
    def test_crear_receta_exitoso(self):
        """Test para crear receta con datos válidos"""
        receta = Receta(self.paciente, self.medico, self.medicamentos)
        self.assertIn("Paracetamol", str(receta))
        self.assertIn("Ibuprofeno", str(receta))
    
    def test_crear_receta_paciente_invalido(self):
        """Test para verificar error con paciente inválido"""
        with self.assertRaises(TypeError):
            Receta("paciente_string", self.medico, self.medicamentos)
    
    def test_crear_receta_medico_invalido(self):
        """Test para verificar error con médico inválido"""
        with self.assertRaises(TypeError):
            Receta(self.paciente, "medico_string", self.medicamentos)
    
    def test_crear_receta_sin_medicamentos(self):
        """Test para verificar error sin medicamentos"""
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, [])
    
    def test_crear_receta_medicamentos_vacios(self):
        """Test para verificar error con medicamentos vacíos"""
        with self.assertRaises(ValueError):
            Receta(self.paciente, self.medico, ["", " ", "  "])

if __name__ == '__main__':
    unittest.main()