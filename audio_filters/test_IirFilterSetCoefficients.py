from __future__ import annotations
import unittest
from unittest.mock import patch
from iir_filter import IIRFilter, set_coefficients

class Test_IirFilterSetCoefficients(unittest.TestCase):

    @patch('iir_filter.IIRFilter')
    def test_set_coefficients_shorter_a_coeffs(self, MockIIRFilter):
        filter_instance = MockIIRFilter(2)
        set_coefficients(filter_instance, [0.0], [1.0, 0.0, 0.0])
        MockIIRFilter.set_coefficients.assert_called_with([1.0, 0.0], [1.0, 0.0, 0.0])

    @patch('iir_filter.IIRFilter')
    def test_set_coefficients_correct_length(self, MockIIRFilter):
        filter_instance = MockIIRFilter(2)
        set_coefficients(filter_instance, [1.0, 0.0, 0.0], [1.0, 0.0, 0.0])
        MockIIRFilter.set_coefficients.assert_called_with([1.0, 0.0, 0.0], [1.0, 0.0, 0.0])

    @patch('iir_filter.IIRFilter')
    def test_set_coefficients_incorrect_length_a_coeffs(self, MockIIRFilter):
        filter_instance = MockIIRFilter(2)
        with self.assertRaises(ValueError) as context:
            set_coefficients(filter_instance, [0.0, 0.0], [1.0, 0.0, 0.0])
        self.assertTrue("Expected a_coeffs to have 3 elements for 2-order filter, got 2" in str(context.exception))
        
    @patch('iir_filter.IIRFilter')
    def test_set_coefficients_incorrect_length_b_coeffs(self, MockIIRFilter):
        filter_instance = MockIIRFilter(2)
        with self.assertRaises(ValueError) as context:
            set_coefficients(filter_instance, [1.0, 0.0, 0.0], [0.0, 0.0])
        self.assertTrue("Expected b_coeffs to have 3 elements for 2-order filter, got 2" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
