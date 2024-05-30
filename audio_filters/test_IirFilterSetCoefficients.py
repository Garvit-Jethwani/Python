from __future__ import annotations
import pytest
from audio_filters.iir_filter import IIRFilter

class Test_IirFilterSetCoefficients:

    @pytest.mark.positive
    def test_set_coefficients_success(self):
        # Arrange
        iir_filter = IIRFilter(2)
        a_coeffs = [1.0, 0.5, 0.25]
        b_coeffs = [1.0, 0.5, 0.25]

        # Act
        iir_filter.set_coefficients(a_coeffs, b_coeffs)

        # Assert
        assert iir_filter.a_coeffs == a_coeffs
        assert iir_filter.b_coeffs == b_coeffs

    @pytest.mark.negative
    def test_set_coefficients_a_coeffs_too_small(self):
        # Arrange
        iir_filter = IIRFilter(2)
        a_coeffs = [1.0, 0.5]
        b_coeffs = [1.0, 0.5, 0.25]

        # Act & Assert
        with pytest.raises(ValueError, match=r"Expected a_coeffs to have 3 elements for 2-order filter, got 2"):
            iir_filter.set_coefficients(a_coeffs, b_coeffs)

    @pytest.mark.negative
    def test_set_coefficients_b_coeffs_too_small(self):
        # Arrange
        iir_filter = IIRFilter(2)
        a_coeffs = [1.0, 0.5, 0.25]
        b_coeffs = [1.0, 0.5]

        # Act & Assert
        with pytest.raises(ValueError, match=r"Expected b_coeffs to have 3 elements for 2-order filter, got 3"):
            iir_filter.set_coefficients(a_coeffs, b_coeffs)

    @pytest.mark.positive
    def test_set_coefficients_a_coeffs_with_default(self):
        # Arrange
        iir_filter = IIRFilter(2)
        a_coeffs = [1.0, 0.5]
        b_coeffs = [1.0, 0.5, 0.25]

        # Act
        iir_filter.set_coefficients(a_coeffs, b_coeffs)

        # Assert
        assert iir_filter.a_coeffs == [1.0, *a_coeffs]
        assert iir_filter.b_coeffs == b_coeffs
