import unittest

from server.operators import add, divide, multiply, subtract


class TestOperators(unittest.TestCase):
    def test_add_returns_sum(self):
        """L'addition retourne la somme des deux opérandes."""
        self.assertEqual(add(2, 3), 5)

    def test_subtract_returns_first_operand_minus_second(self):
        """La soustraction suit l'ordre des opérandes de l'expression."""
        self.assertEqual(subtract(8, 3), 5)

    def test_multiply_returns_product(self):
        """La multiplication retourne le produit des deux opérandes."""
        self.assertEqual(multiply(3, 4), 12)

    def test_divide_returns_quotient(self):
        """La division conserve le quotient, y compris sa partie décimale."""
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero_raises(self):
        """Une division par zéro signale une erreur arithmétique."""
        with self.assertRaises(ZeroDivisionError):
            divide(7, 0)


if __name__ == "__main__":
    unittest.main()