from unittest import TestCase

from program.mutante02 import ladosTriangulo


class TrianguloTest(TestCase):
    def setUp(self):
        return super().setUp()

    def test_equilatero_valid(self):
        result = ladosTriangulo(1, 1, 1)
        self.assertEqual(result, "Equilatéro")

    def test_isoceles_valid(self):
        result = ladosTriangulo(2, 2, 1)
        self.assertEqual(result, "Isóceles")

    def test_escaleno_valid(self):
        result = ladosTriangulo(2, 3, 4)
        self.assertEqual(result, "Escaleno")

    def test_not_triangulo(self):
        result = ladosTriangulo(1, 2, 3)
        self.assertEqual(result, "Não é possível formar um triangulo")
