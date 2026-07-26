"""Security tests for rs-index-calc."""

import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import rs_index_calc


class TestSecurity:
    """Security-related tests."""

    def test_custom_formula_no_code_injection(self):
        """Test that custom formulas cannot execute arbitrary code."""
        bands = [[1.0], [2.0], [3.0], [4.0], [5.0], [6.0]]
        mapping = {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4, "swir2": 5}

        malicious_formulas = [
            "__import__('os').system('echo hacked')",
            "exec('import os; os.system(\"echo hacked\")')",
            "eval('__import__(\"os\").system(\"echo hacked\")')",
            "open('/etc/passwd').read()",
        ]

        for formula in malicious_formulas:
            result = rs_index_calc.calculate_custom_formula(formula, bands, mapping, 1, 1)
            assert result[0] == 0.0, f"Formula should return 0: {formula}"

    def test_formula_safe_math(self):
        """Test that math module is available in formulas."""
        bands = [[1.0], [2.0], [3.0], [4.0], [5.0], [6.0]]
        mapping = {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4, "swir2": 5}

        result = rs_index_calc.calculate_custom_formula("math.sqrt(B1)", bands, mapping, 1, 1)
        assert abs(result[0] - 1.0) < 1e-6

    def test_formula_invalid_expression(self):
        """Test invalid formula returns 0."""
        bands = [[1.0], [2.0], [3.0], [4.0], [5.0], [6.0]]
        mapping = {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4, "swir2": 5}

        result = rs_index_calc.calculate_custom_formula("invalid+++", bands, mapping, 1, 1)
        assert result[0] == 0.0

    def test_formula_overflow_protection(self):
        """Test formula with overflow protection."""
        bands = [[1e300], [1e300], [0.0], [0.0], [0.0], [0.0]]
        mapping = {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4, "swir2": 5}

        result = rs_index_calc.calculate_custom_formula("B1*B2", bands, mapping, 1, 1)
        assert result[0] == 0.0 or abs(result[0]) < float('inf')

    def test_formula_nan_protection(self):
        """Test formula with NaN protection."""
        bands = [[float('nan')], [1.0], [0.0], [0.0], [0.0], [0.0]]
        mapping = {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4, "swir2": 5}

        result = rs_index_calc.calculate_custom_formula("B1 + B2", bands, mapping, 1, 1)
        assert result[0] == 0.0

    def test_file_not_found(self):
        """Test handling of non-existent files."""
        with pytest.raises(Exception):
            rs_index_calc.read_geotiff("nonexistent_file.tif")

    def test_invalid_tiff_byte_order(self):
        """Test handling of invalid TIFF byte order."""
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            f.write(b"XX\x00\x00\x00\x00\x00\x08")
            temp_path = f.name

        try:
            with pytest.raises(ValueError, match="Invalid TIFF byte order"):
                rs_index_calc.read_tiff_header(temp_path)
        finally:
            os.unlink(temp_path)

    def test_invalid_tiff_magic(self):
        """Test handling of invalid TIFF magic number."""
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            f.write(b"II\x00\x01\x00\x00\x00\x08")
            temp_path = f.name

        try:
            with pytest.raises(ValueError, match="Invalid TIFF magic number"):
                rs_index_calc.read_tiff_header(temp_path)
        finally:
            os.unlink(temp_path)

    def test_version_string(self):
        """Test version string is defined."""
        assert hasattr(rs_index_calc, "VERSION")
        assert isinstance(rs_index_calc.VERSION, str)
        assert len(rs_index_calc.VERSION) > 0
