import unittest
from datetime import datetime
from modelos import HistoriaClinica, Paciente, Medico, Especialidad, Turno, Receta

class TestHistoriaClinica(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para cada test"""
        self.paciente = Paciente("Juan Pérez", "12345678", "01/01/1990")
        especialidad = Especialidad("Pediatría", ["lunes", "miércoles"])
        self.medico = Medico("Dr. García", "54321", [especialidad])
        self.fecha_hora = datetime(2025, 12, 10, 14, 30)
    
    def test_crear_historia_clinica_exitoso(self):
        """Test para crear historia clínica con datos válidos"""
        historia = HistoriaClinica(self.paciente)
        self.assertEqual(len(historia.obtener_turnos()), 0)
        self.assertEqual(len(historia.obtener_recetas()), 0)
    
    def test_crear_historia_clinica_paciente_invalido(self):
        """Test para verificar error con paciente inválido"""
        with self.assertRaises(TypeError):
            HistoriaClinica("paciente_string")
    
    def test_agregar_turno_exitoso(self):
        """Test para agregar turno exitosamente"""
        historia = HistoriaClinica(self.paciente)
        turno = Turno(self.paciente, self.medico, self.fecha_hora, "Pediatría")
        historia.agregar_turno(turno)
        self.assertEqual(len(historia.obtener_turnos()), 1)
    
    def test_agregar_turno_invalido(self):
        """Test para verificar error al agregar turno inválido"""
        historia = HistoriaClinica(self.paciente)
        with self.assertRaises(TypeError):
            historia.agregar_turno("turno_string")
    
    def test_agregar_receta_exitoso(self):
        """Test para agregar receta exitosamente"""
        historia = HistoriaClinica(self.paciente)
        receta = Receta(self.paciente, self.medico, ["Paracetamol"])
        historia.agregar_receta(receta)
        self.assertEqual(len(historia.obtener_recetas()), 1)
    
    def test_agregar_receta_invalida(self):
        """Test para verificar error al agregar receta inválida"""
        historia = HistoriaClinica(self.paciente)
        with self.assertRaises(TypeError):
            historia.agregar_receta("receta_string")

if __name__ == '__main__':
    unittest.main()