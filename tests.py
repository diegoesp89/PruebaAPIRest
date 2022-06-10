import rest
import expected_test
from unittest import TestCase

class TestIntegrations(TestCase):
    def setUp(self):
        self.NombreComuna = rest.NombreComuna
        self.IdLocal = rest.IdLocal
        self.Fecha = rest.Fecha
        self.LocalidadNombre = rest.LocalidadNombre
        self.LocalDireccion = rest.LocalDireccion
        self.HoraApertura = rest.HoraApertura
        self.HoraCierre = rest.HoraCierre
        self.LocalTelefono = rest.LocalTelefono
        self.LocalLat = rest.LocalLat
        self.LocalLng = rest.LocalLng
        self.FuncionamientoDia = rest.FuncionamientoDia
        self.FkRegion = rest.FkRegion
        self.FkComuna = rest.FkComuna

    def test_NombreComuna_output_type(self):
        response = self.NombreComuna.get(self, "BUIN")
        self.assertEqual(type(response), type([]), "Output type incorrect")

    def test_IdLocal_output_type(self):
        response = self.IdLocal.get(self, "757")
        self.assertEqual(type(response), type([]), "Output type incorrect")

    def test_IdLocal_output_value(self):
        response = self.IdLocal.get(self, "757")
        self.assertEqual(response, expected_test.id_local_value, "Output value incorrect")
        
    def test_Fecha_output_type(self):
        response = self.Fecha.get(self, "757")
        self.assertEqual(type(response), type([]), "Output type incorrect")

    def test_LocalidadNombre_output_type(self):
        response = self.LocalidadNombre.get(self, "RECOLETA")
        self.assertEqual(type(response), type([]), "Output type incorrect")

    def test_LocalDireccion_output_type(self):
        response = self.LocalDireccion.get(self, "JOSE MANUEL BALMACEDA 114")
        self.assertEqual(type(response), type([]), "Output type incorrect")

    def test_HoraApertura_output_type(self):
        response = self.HoraApertura.get(self, "09:00 hrs.")
        self.assertEqual(type(response), type([]), "Output type incorrect")

    def test_HoraCierre_output_type(self):
        response = self.HoraCierre.get(self, "21:00 hrs.")
        self.assertEqual(type(response), type([]), "Output type incorrect")

    def test_LocalLat_output_type(self):
        response = self.LocalLat.get(self, "-33.734744")
        self.assertEqual(type(response), type([]), "Output type incorrect")
        
    def test_LocalLat_output_value(self):
        response = self.LocalLat.get(self, "-33.734744")
        self.assertEqual(response, expected_test.local_lat_value, "Output value incorrect")

    def test_LocalLng_output_type(self):
        response = self.LocalLng.get(self, "-70.738417")
        self.assertEqual(type(response), type([]), "Output type incorrect")

    def test_FuncionamientoDia_output_type(self):
        response = self.FuncionamientoDia.get(self, "viernes")
        self.assertEqual(type(response), type([]), "Output type incorrect")

    def test_FkRegion_output_type(self):
        response = self.FkRegion.get(self, "7")
        self.assertEqual(type(response), type([]), "Output type incorrect")

    def test_FkComuna_output_type(self):
        response = self.FkComuna.get(self, "85")
        self.assertEqual(type(response), type([]), "Output type incorrect")
