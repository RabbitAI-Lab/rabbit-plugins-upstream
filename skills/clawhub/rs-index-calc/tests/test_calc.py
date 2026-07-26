"""Tests for index calculations."""

import os
import sys
import math
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import rs_index_calc


class TestSafeDivide:
    """Test safe division function."""

    def test_normal_division(self):
        assert rs_index_calc.safe_divide(10, 2) == 5.0

    def test_zero_denominator(self):
        assert rs_index_calc.safe_divide(10, 0) == 0.0

    def test_near_zero_denominator(self):
        assert rs_index_calc.safe_divide(10, 1e-11) == 0.0

    def test_negative_values(self):
        assert rs_index_calc.safe_divide(-10, 2) == -5.0

    def test_both_zero(self):
        assert rs_index_calc.safe_divide(0, 0) == 0.0


class TestIndexCalculations:
    """Test spectral index calculations."""

    def setup_method(self):
        """Setup test data."""
        self.width = 2
        self.height = 2
        self.n_pixels = self.width * self.height

        self.red = [0.1, 0.2, 0.3, 0.4]
        self.green = [0.05, 0.15, 0.25, 0.35]
        self.blue = [0.02, 0.08, 0.18, 0.28]
        self.nir = [0.5, 0.6, 0.7, 0.8]
        self.swir1 = [0.3, 0.4, 0.5, 0.6]
        self.swir2 = [0.2, 0.3, 0.4, 0.5]

        self.bands_data = [self.red, self.green, self.blue, self.nir, self.swir1, self.swir2]
        self.band_mapping = {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4, "swir2": 5}

    def test_ndvi(self):
        """Test NDVI calculation."""
        result = rs_index_calc.calculate_index("NDVI", self.bands_data, self.band_mapping, self.width, self.height)
        assert len(result) == self.n_pixels

        expected = (0.5 - 0.1) / (0.5 + 0.1)
        assert abs(result[0] - expected) < 1e-6

    def test_ndbi(self):
        """Test NDBI calculation."""
        result = rs_index_calc.calculate_index("NDBI", self.bands_data, self.band_mapping, self.width, self.height)
        assert len(result) == self.n_pixels

        expected = (0.3 - 0.5) / (0.3 + 0.5)
        assert abs(result[0] - expected) < 1e-6

    def test_ndwi(self):
        """Test NDWI calculation."""
        result = rs_index_calc.calculate_index("NDWI", self.bands_data, self.band_mapping, self.width, self.height)
        assert len(result) == self.n_pixels

        expected = (0.05 - 0.5) / (0.05 + 0.5)
        assert abs(result[0] - expected) < 1e-6

    def test_evi(self):
        """Test EVI calculation."""
        result = rs_index_calc.calculate_index("EVI", self.bands_data, self.band_mapping, self.width, self.height)
        assert len(result) == self.n_pixels

        denom = 0.5 + 6 * 0.1 - 7.5 * 0.02 + 1
        expected = 2.5 * (0.5 - 0.1) / denom
        assert abs(result[0] - expected) < 1e-6

    def test_savi(self):
        """Test SAVI calculation."""
        result = rs_index_calc.calculate_index("SAVI", self.bands_data, self.band_mapping, self.width, self.height)
        assert len(result) == self.n_pixels

        expected = (0.5 - 0.1) / (0.5 + 0.1 + 0.5) * 1.5
        assert abs(result[0] - expected) < 1e-6

    def test_mndwi(self):
        """Test MNDWI calculation."""
        result = rs_index_calc.calculate_index("MNDWI", self.bands_data, self.band_mapping, self.width, self.height)
        assert len(result) == self.n_pixels

        expected = (0.05 - 0.3) / (0.05 + 0.3)
        assert abs(result[0] - expected) < 1e-6

    def test_awei(self):
        """Test AWEI calculation."""
        result = rs_index_calc.calculate_index("AWEI", self.bands_data, self.band_mapping, self.width, self.height)
        assert len(result) == self.n_pixels

        expected = 4 * (0.05 - 0.3) - (0.25 * 0.5 + 2.75 * 0.3)
        assert abs(result[0] - expected) < 1e-6

    def test_nbr(self):
        """Test NBR calculation."""
        result = rs_index_calc.calculate_index("NBR", self.bands_data, self.band_mapping, self.width, self.height)
        assert len(result) == self.n_pixels

        expected = (0.5 - 0.2) / (0.5 + 0.2)
        assert abs(result[0] - expected) < 1e-6

    def test_bsi(self):
        """Test BSI calculation."""
        result = rs_index_calc.calculate_index("BSI", self.bands_data, self.band_mapping, self.width, self.height)
        assert len(result) == self.n_pixels

        num = (0.3 + 0.1) - (0.5 + 0.02)
        den = (0.3 + 0.1) + (0.5 + 0.02)
        expected = num / den
        assert abs(result[0] - expected) < 1e-6

    def test_ui(self):
        """Test UI calculation."""
        result = rs_index_calc.calculate_index("UI", self.bands_data, self.band_mapping, self.width, self.height)
        assert len(result) == self.n_pixels

        expected = (0.2 - 0.5) / (0.2 + 0.5)
        assert abs(result[0] - expected) < 1e-6

    def test_unknown_index(self):
        """Test unknown index raises error."""
        with pytest.raises(ValueError, match="Unknown index"):
            rs_index_calc.calculate_index("UNKNOWN", self.bands_data, self.band_mapping, self.width, self.height)

    def test_missing_band(self):
        """Test missing band raises error."""
        incomplete_mapping = {"red": 0}
        with pytest.raises(ValueError, match="not mapped"):
            rs_index_calc.calculate_index("NDVI", self.bands_data, incomplete_mapping, self.width, self.height)

    def test_ndvi_range(self):
        """Test NDVI is in valid range [-1, 1]."""
        result = rs_index_calc.calculate_index("NDVI", self.bands_data, self.band_mapping, self.width, self.height)
        for val in result:
            assert -1 <= val <= 1, f"NDVI out of range: {val}"

    def test_zero_pixels(self):
        """Test calculation with zero pixel values."""
        red = [0.0, 0.0]
        nir = [0.0, 0.0]
        bands = [red, [0]*2, [0]*2, nir, [0]*2, [0]*2]
        mapping = {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4, "swir2": 5}
        result = rs_index_calc.calculate_index("NDVI", bands, mapping, 2, 1)
        assert result[0] == 0.0

    def test_custom_formula(self):
        """Test custom formula calculation."""
        result = rs_index_calc.calculate_custom_formula(
            "(B4-B3)/(B4+B3)", self.bands_data, self.band_mapping, self.width, self.height
        )
        assert len(result) == self.n_pixels

        expected = (0.5 - 0.02) / (0.5 + 0.02)
        assert abs(result[0] - expected) < 1e-6

    def test_custom_formula_division_by_zero(self):
        """Test custom formula with division by zero."""
        bands = [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0]]
        result = rs_index_calc.calculate_custom_formula(
            "(B1+B2)/(B1-B2)", bands, self.band_mapping, 1, 1
        )
        assert result[0] == 0.0


class TestComputeStatistics:
    """Test statistics computation."""

    def test_normal_data(self):
        """Test statistics with normal data."""
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        stats = rs_index_calc.compute_statistics(data)
        assert stats["min"] == 1.0
        assert stats["max"] == 5.0
        assert stats["mean"] == 3.0
        assert stats["count"] == 5
        assert abs(stats["std"] - math.sqrt(2.0)) < 1e-6

    def test_single_value(self):
        """Test statistics with single value."""
        data = [42.0]
        stats = rs_index_calc.compute_statistics(data)
        assert stats["min"] == 42.0
        assert stats["max"] == 42.0
        assert stats["mean"] == 42.0
        assert stats["std"] == 0.0
        assert stats["count"] == 1

    def test_empty_data(self):
        """Test statistics with empty data."""
        data = []
        stats = rs_index_calc.compute_statistics(data)
        assert stats["min"] == 0
        assert stats["max"] == 0
        assert stats["mean"] == 0
        assert stats["count"] == 0

    def test_nan_values(self):
        """Test statistics with NaN values."""
        data = [1.0, float("nan"), 3.0, float("inf"), 5.0]
        stats = rs_index_calc.compute_statistics(data)
        assert stats["count"] == 3
        assert stats["min"] == 1.0
        assert stats["max"] == 5.0

    def test_negative_values(self):
        """Test statistics with negative values."""
        data = [-1.0, -2.0, -3.0]
        stats = rs_index_calc.compute_statistics(data)
        assert stats["min"] == -3.0
        assert stats["max"] == -1.0
        assert stats["mean"] == -2.0


class TestBandDetection:
    """Test band detection and mapping."""

    def test_detect_from_descriptions(self):
        """Test band detection from descriptions."""
        descriptions = ["Red Band", "Green Band", "Blue Band", "NIR Band", "SWIR1 Band", "SWIR2 Band"]
        mapping = rs_index_calc.detect_band_mapping(descriptions)
        assert mapping["red"] == 0
        assert mapping["green"] == 1
        assert mapping["blue"] == 2
        assert mapping["nir"] == 3
        assert mapping["swir1"] == 4
        assert mapping["swir2"] == 5

    def test_detect_partial_descriptions(self):
        """Test partial band detection."""
        descriptions = ["Band 4 - Red", "Band 3 - Green", "Band 2 - Blue", "Band 5 - NIR"]
        mapping = rs_index_calc.detect_band_mapping(descriptions)
        assert mapping["red"] == 0
        assert mapping["green"] == 1
        assert mapping["blue"] == 2
        assert mapping["nir"] == 3

    def test_parse_bands_argument(self):
        """Test manual band argument parsing."""
        mapping = rs_index_calc.parse_bands_argument("red nir green blue swir1 swir2")
        assert mapping["red"] == 0
        assert mapping["nir"] == 1
        assert mapping["green"] == 2
        assert mapping["blue"] == 3
        assert mapping["swir1"] == 4
        assert mapping["swir2"] == 5

    def test_empty_descriptions(self):
        """Test empty band descriptions."""
        mapping = rs_index_calc.detect_band_mapping([])
        assert len(mapping) == 0

    def test_unknown_descriptions(self):
        """Test unknown band descriptions."""
        descriptions = ["Alpha", "Beta", "Gamma"]
        mapping = rs_index_calc.detect_band_mapping(descriptions)
        assert len(mapping) == 0
