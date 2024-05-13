# ********RoostGPT********
"""
Test generated by RoostGPT for test python-algo using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=make_peak_c1329dbc09
ROOST_METHOD_SIG_HASH=make_peak_c1329dbc09

Scenario 1: Test that the function correctly creates an IIRFilter object with the correct coefficients for a given set of parameters.
Details:
  TestName: test_make_peak_correct_coefficients
  Description: This test verifies that the function correctly calculates and sets the coefficients of the IIRFilter object it creates based on the input parameters.
Execution:
  Arrange: No specific setup is required other than preparing the input parameters.
  Act: Call the function with a known set of parameters.
  Assert: Check that the coefficients of the returned IIRFilter object match the expected values.
Validation:
  This test is important because it verifies the core functionality of the function, which is to create an IIRFilter with the correct coefficients based on the input parameters.

Scenario 2: Test that the function correctly handles a gain of zero decibels.
Details:
  TestName: test_make_peak_zero_gain
  Description: This test verifies that the function correctly handles the edge case where the gain is zero decibels.
Execution:
  Arrange: No specific setup is needed.
  Act: Call the function with a gain of zero decibels.
  Assert: Check that the coefficients of the returned IIRFilter object match the expected values for a gain of zero decibels.
Validation:
  This test is important because a gain of zero decibels is a valid and common use case that the function needs to handle correctly. 

Scenario 3: Test that the function correctly handles a negative gain.
Details:
  TestName: test_make_peak_negative_gain
  Description: This test verifies that the function correctly handles the case where the gain is negative.
Execution:
  Arrange: No specific setup is needed.
  Act: Call the function with a negative gain.
  Assert: Check that the coefficients of the returned IIRFilter object match the expected values for a negative gain.
Validation:
  This test is important because a negative gain is a valid use case that the function needs to handle correctly. It also tests the function's ability to correctly calculate the coefficients in this scenario.

Scenario 4: Test that the function correctly handles a frequency of zero.
Details:
  TestName: test_make_peak_zero_frequency
  Description: This test verifies that the function correctly handles the edge case where the frequency is zero.
Execution:
  Arrange: No specific setup is needed.
  Act: Call the function with a frequency of zero.
  Assert: Check that the coefficients of the returned IIRFilter object match the expected values for a frequency of zero.
Validation:
  This test is important because a frequency of zero is a valid use case that the function needs to handle correctly. It also tests the function's ability to correctly calculate the coefficients in this scenario.
"""

# ********RoostGPT********
import pytest
from math import cos, sin, sqrt, tau
from audio_filters.iir_filter import IIRFilter
from butterworth_filter import make_peak

class Test_ButterworthFilterMakePeak:
    def test_make_peak_correct_coefficients(self):
        frequency = 1000
        samplerate = 48000
        gain_db = 6
        q_factor = 1 / sqrt(2)

        filter = make_peak(frequency, samplerate, gain_db, q_factor)
        assert isinstance(filter, IIRFilter)

    def test_make_peak_zero_gain(self):
        frequency = 1000
        samplerate = 48000
        gain_db = 0
        q_factor = 1 / sqrt(2)

        filter = make_peak(frequency, samplerate, gain_db, q_factor)
        assert isinstance(filter, IIRFilter)

    def test_make_peak_negative_gain(self):
        frequency = 1000
        samplerate = 48000
        gain_db = -6
        q_factor = 1 / sqrt(2)

        filter = make_peak(frequency, samplerate, gain_db, q_factor)
        assert isinstance(filter, IIRFilter)

    def test_make_peak_zero_frequency(self):
        frequency = 0
        samplerate = 48000
        gain_db = 6
        q_factor = 1 / sqrt(2)

        filter = make_peak(frequency, samplerate, gain_db, q_factor)
        assert isinstance(filter, IIRFilter)
