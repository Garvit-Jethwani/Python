from __future__ import annotations
import pytest
from iir_filter import IIRFilter

class Test_IirFilterSetCoefficients:

    def test_successful_set_coefficients(self):
        # Arrange
        iir_filter = IIRFilter(2)
        a_coeffs = [1.0, 0.5, 0.25]
        b_coeffs = [1.0, 0.5, 0.25]

        # Act
        iir_filter.set_coefficients(a_coeffs, b_coeffs)

        # Assert
        assert iir_filter.a_coeffs == a_coeffs
        assert iir_filter.b_coeffs == b_coeffs

    def test_a_coeffs_less_than_order(self):
        # Arrange
        iir_filter = IIRFilter(2)
        a_coeffs = [0.5, 0.25]

        # Act
        iir_filter.set_coefficients(a_coeffs, a_coeffs)

        # Assert
        assert iir_filter.a_coeffs == [1.0, *a_coeffs]

    def test_a_coeffs_not_equal_order_plus_one(self):
        # Arrange
        iir_filter = IIRFilter(2)
        a_coeffs = [1.0, 0.5]

        # Act & Assert
        with pytest.raises(ValueError):
            iir_filter.set_coefficients(a_coeffs, a_coeffs)

    def test_b_coeffs_not_equal_order_plus_one(self):
        # Arrange
        iir_filter = IIRFilter(2)
        b_coeffs = [1.0, 0.5]

        # Act & Assert
        with pytest.raises(ValueError):
            iir_filter.set_coefficients(b_coeffs, b_coeffs)
