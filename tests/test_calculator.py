import unittest

from server.app import app, calculate


class TestCalculate(unittest.TestCase):
    def test_calculate_addition(self):
        """Une expression d'addition simple est évaluée."""
        self.assertEqual(calculate("2+3"), 5)

    def test_calculate_expression_with_spaces(self):
        """Les espaces autour des opérandes et de l'opérateur sont ignorés."""
        self.assertEqual(calculate(" 2 + 3 "), 5)

    def test_calculate_subtraction(self):
        """La soustraction respecte l'ordre écrit dans l'expression."""
        self.assertEqual(calculate("8-3"), 5)

    def test_calculate_multiplication(self):
        """L'opérateur de multiplication calcule un produit."""
        self.assertEqual(calculate("3*4"), 12)

    def test_calculate_division(self):
        """La division retourne un quotient décimal lorsque nécessaire."""
        self.assertEqual(calculate("7/2"), 3.5)

    def test_calculate_rejects_invalid_expressions(self):
        """Les expressions vides, incomplètes ou ambiguës sont rejetées."""
        invalid_expressions = ("", "2+", "2+3+4", "abc+2")
        for expression in invalid_expressions:
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    calculate(expression)


class TestCalculatorRoute(unittest.TestCase):
    def setUp(self):
        """Prépare un client Flask isolé pour chaque test de route."""
        self.client = app.test_client()

    def test_get_displays_calculator(self):
        """Une requête GET affiche la page de la calculatrice."""
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn("Flask Calculator", response.get_data(as_text=True))

    def test_post_displays_calculation_result(self):
        """Une soumission POST affiche le résultat dans le champ d'affichage."""
        response = self.client.post("/", data={"display": "2+3"})

        self.assertEqual(response.status_code, 200)
        self.assertIn('value="5.0"', response.get_data(as_text=True))

    def test_post_displays_validation_error(self):
        """Une expression invalide affiche une erreur sans faire échouer la route."""
        response = self.client.post("/", data={"display": "2+3+4"})
        page = response.get_data(as_text=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn("Error: only one operator is allowed", page)


if __name__ == "__main__":
    unittest.main()