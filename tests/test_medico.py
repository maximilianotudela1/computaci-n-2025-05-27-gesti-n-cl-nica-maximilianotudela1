import unittest
from modelos import Medico, Especialidad

class TestMedico(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.especialidad1 = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.especialidad2 = Especialidad("Cardiología", ["martes", "jueves"])
    
    def test_crear_medico_exitoso(self):
        """Test para crear un médico con datos válidos"""
        medico = Medico("Dr. Juan Pérez", "12345", [self.especialidad1])
        self.assertEqual(medico.obtener_matricula(), "12345")
    
    def test_crear_medico_sin_nombre(self):
        """Test para verificar error cuando no se proporciona nombre"""
        with self.assertRaises(ValueError) as context:
            Medico("", "12345", [])
        self.assertIn("nombre", str(context.exception).lower())
    
    def test_crear_medico_sin_matricula(self):
        """Test para verificar error cuando no se proporciona matrícula"""
        with self.assertRaises(ValueError) as context:
            Medico("Dr. Juan Pérez", "", [])
        self.assertIn("matrícula", str(context.exception).lower())
    
    def test_agregar_especialidad_exitoso(self):
        """Test para agregar especialidad exitosamente"""
        medico = Medico("Dr. Juan Pérez", "12345")
        medico.agregar_especialidad(self.especialidad1)
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), "Pediatría")
    
    def test_agregar_especialidad_duplicada(self):
        """Test para verificar error al agregar especialidad duplicada"""
        medico = Medico("Dr. Juan Pérez", "12345", [self.especialidad1])
        with self.assertRaises(ValueError) as context:
            medico.agregar_especialidad(self.especialidad1)
        self.assertIn("ya existe", str(context.exception).lower())
    
    def test_obtener_especialidad_para_dia(self):
        """Test para obtener especialidad por día"""
        medico = Medico("Dr. Juan Pérez", "12345", [self.especialidad1, self.especialidad2])
        self.assertEqual(medico.obtener_especialidad_para_dia("lunes"), "Pediatría")
        self.assertEqual(medico.obtener_especialidad_para_dia("martes"), "Cardiología")
        self.assertIsNone(medico.obtener_especialidad_para_dia("viernes"))

if __name__ == '__main__':
    unittest.main()