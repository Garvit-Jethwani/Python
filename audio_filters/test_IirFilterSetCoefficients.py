from __future__ import annotations
import pytest
from audio_filters.iir_filter import IIRFilter

class Test_IirFilterSetCoefficients:

    def test_set_coefficients_valid_order(self):
        # Arrange
        order = 2
        a_coeffs = [1.0, 0.5, 0.25]
        b_coeffs = [1.0, 0.5, 0.25]
        filter = IIRFilter(order)

        # Act
        filter.set_coefficients(a_coeffs, b_coeffs)

        # Assert
        assert filter.a_coeffs == a_coeffs
        assert filter.b_coeffs == b_coeffs

    def test_set_coefficients_lesser_order(self):
        # Arrange
        order = 2
        a_coeffs = [0.5, 0.25]
        b_coeffs = [1.0, 0.5, 0.25]
        filter = IIRFilter(order)

        # Act
        filter.set_coefficients(a_coeffs, b_coeffs)

        # Assert
        assert filter.a_coeffs == [1.0, *a_coeffs]
        assert filter.b_coeffs == b_coeffs

    def test_set_coefficients_greater_order(self):
        # Arrange
        order = 2
        a_coeffs = [1.0, 0.5, 0.25, 0.125]
        b_coeffs = [1.0, 0.5, 0.25, 0.125]
        filter = IIRFilter(order)

        # Act & Assert
        with pytest.raises(ValueError, match=r"Expected a_coeffs to have 3 elements for 2-order filter, got 4"):
            filter.set_coefficients(a_coeffs, b_coeffs)

    def test_set_coefficients_invalid_order(self):
        # Arrange
        order = 2
        a_coeffs = [1.0, 0.5]
        b_coeffs = [1.0, 0.5]
        filter = IIRFilter(order)

        # Act & Assert
        with pytest.raises(ValueError, match=r"Expected a_coeffs to have 3 elements for 2-order filter, got 2"):
            filter.set_coefficients(a_coeffs, b_coeffs)
