import unittest
from prueba import probar

class TestProbar(unittest.TestCase):
    def test_validar_usuario(self):
        self.assertTrue(probar('mpleado','Duoc.2019'))