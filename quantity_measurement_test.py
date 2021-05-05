import unittest
from quantity_measurement import QuantityMeasurement


class TestQuantityMeasurement(unittest.TestCase):

    def test_lengths_given_0_ft_and_0_ft_should_compare_and_return_true(self):
        self.assertTrue(QuantityMeasurement().compare_length("ft", "ft", 0, 0))

    def test_lengths_given_1_ft_and_5_ft_should_compare_and_return_false(self):
        self.assertFalse(QuantityMeasurement().compare_length("ft", "ft", 1, 5))

    def test_lengths_given_None_ft_and_5_ft_should_return_none(self):
        self.assertIsNone(QuantityMeasurement().compare_length("ft", "ft", 5, None))

    def test_lengths_given_5_ft_and_5_ft_should_return_not_none(self):
        self.assertIsNotNone(QuantityMeasurement().compare_length("ft", "ft", 5, 5))

    def test_lengths_given_0_in_and_0_in_should_compare_and_return_true(self):
        self.assertTrue(QuantityMeasurement().compare_length("in", "in", 0, 0))

    def test_lengths_given_1_in_and_5_in_should_compare_and_return_false(self):
        self.assertFalse(QuantityMeasurement().compare_length("in", "in", 1, 5))

    def test_lengths_given_0_ft_and_0_in_should_compare_and_return_true(self):
        self.assertTrue(QuantityMeasurement().compare_length("ft", "in", 0, 0))


if __name__ == '__main__':
    unittest.main()
