import unittest
from src.modules.modules import validate_professor_name


class TestValidateProfessorName(unittest.TestCase):
    """
    Test cases for the validate_professor_name function.
    """

    """------------------- Success cases -------------------"""

    def test_valid_professor_name_common(self):
        """
        Success case: Valid common professor name.
        """
        self.assertEqual(
            validate_professor_name("Marcelo Cisneyros"), "Marcelo Cisneyros"
        )

    def test_valid_professor_name_with_spaces(self):
        """
        Success case: Valid name with leading/trailing spaces.
        """
        self.assertEqual(validate_professor_name("  Chris Lima  "), "  Chris Lima  ")

    def test_valid_professor_name_single_word(self):
        """
        Success case: Valid single word name.
        """
        self.assertEqual(validate_professor_name("RenZo"), "RenZo")

    def test_valid_professor_name_with_special_characters(self):
        """
        Success case: Valid name with special characters.
        """
        self.assertEqual(
            validate_professor_name("ThiThi Miguelito!"), "ThiThi Miguelito!"
        )

    def test_valid_professor_name_lowercase(self):
        """
        Success case: Valid lowercase name.
        """
        self.assertEqual(
            validate_professor_name("evandro cesar vilas boas"),
            "evandro cesar vilas boas",
        )

    """------------------- Failure cases -------------------"""

    def test_invalid_professor_name_empty_string(self):
        """
        Failure case: Invalid empty string name.
        """
        with self.assertRaises(ValueError):
            validate_professor_name("")

    def test_invalid_professor_name_none(self):
        """
        Failure case: Invalid None as a name.
        """
        with self.assertRaises(ValueError):
            validate_professor_name(None)

    def test_invalid_professor_name_numeric(self):
        """
        Failure case: Invalid numeric input as a name.
        """
        with self.assertRaises(ValueError):
            validate_professor_name(1234)

    def test_invalid_professor_name_list(self):
        """
        Failure case: Invalid list input as a name.
        """
        with self.assertRaises(ValueError):
            validate_professor_name(["Marcelo Cisneyros"])

    def test_invalid_professor_name_dict(self):
        """
        Failure case: Invalid dictionary input as a name.
        """
        with self.assertRaises(ValueError):
            validate_professor_name({"name": "Marcelo Cisneyros"})

    def test_invalid_professor_name_with_numbers(self):
        """
        Failure case: Invalid name with numbers in it.
        """
        with self.assertRaises(ValueError):
            validate_professor_name("Marcelo123")

    def test_invalid_professor_name_tuple(self):
        """
        Failure case: Invalid input as a tuple.
        """
        with self.assertRaises(ValueError):
            validate_professor_name(("Marcelo", "Cisneyros"))