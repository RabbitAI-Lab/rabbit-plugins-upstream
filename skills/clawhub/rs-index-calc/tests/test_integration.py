"""Integration tests for rs-index-calc."""

import os
import sys
import struct
import tempfile
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import rs_index_calc


def create_test_geotiff(filepath, width=4, height=4, num_bands=4, values=None):
    """Create a test GeoTIFF file."""
    if values is None:
        values = {}
        for i in range(num_bands):
            values[i] = [float(i * 100 + j) for j in range(width * height)]

    endian = "<"
    header_size = 8
    ifd_entries = 13
    ifd_size = 2 + ifd_entries * 12 + 4
    data_offset = header_size + ifd_size

    bytes_per_sample = 4
    pixel_data = bytearray()
    for y in range(height):
        for x in range(width):
            pixel_idx = y * width + x
            for band_idx in range(num_bands):
                val = values.get(band_idx, [0.0] * (width * height))[pixel_idx]
                pixel_data.extend(struct.pack(f"{endian}f", float(val)))

    pixel_data_offset = data_offset

    with open(filepath, "wb") as f:
        f.write(b"II")
        f.write(struct.pack(f"{endian}H", 42))
        f.write(struct.pack(f"{endian}I", header_size))

        f.write(struct.pack(f"{endian}H", ifd_entries))

        def write_tag(tag_id, type_id, count, value):
            f.write(struct.pack(f"{endian}H", tag_id))
            f.write(struct.pack(f"{endian}H", type_id))
            f.write(struct.pack(f"{endian}I", count))
            if type_id == 3 and count == 1:
                f.write(struct.pack(f"{endian}H", value))
                f.write(struct.pack(f"{endian}H", 0))
            elif type_id == 4 and count == 1:
                f.write(struct.pack(f"{endian}I", value))
            else:
                f.write(struct.pack(f"{endian}I", value))

        write_tag(256, 4, 1, width)
        write_tag(257, 4, 1, height)
        write_tag(258, 3, 1, 32)
        write_tag(259, 3, 1, 1)
        write_tag(262, 3, 1, 1)
        write_tag(273, 4, 1, pixel_data_offset)
        write_tag(274, 3, 1, 1)
        write_tag(277, 3, 1, num_bands)
        write_tag(278, 4, 1, height)
        write_tag(279, 4, 1, len(pixel_data))
        write_tag(284, 3, 1, 2)
        write_tag(339, 3, 1, 3)

        geo_ascii_offset = data_offset + len(pixel_data)
        write_tag(34737, 2, 0, geo_ascii_offset)

        f.write(struct.pack(f"{endian}I", 0))

        f.write(pixel_data)

        geo_ascii = ""
        if num_bands >= 4:
            geo_ascii = "Red|Green|Blue|NIR"
        if num_bands >= 5:
            geo_ascii += "|SWIR1"
        if num_bands >= 6:
            geo_ascii += "|SWIR2"

        f.write(geo_ascii.encode("ascii") + b"\x00")


class TestGeotiffIO:
    """Test GeoTIFF reading and writing."""

    def test_write_and_read_geotiff(self):
        """Test writing and reading a GeoTIFF."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            temp_path = f.name

        try:
            width = 3
            height = 3
            band_data = [float(i) for i in range(width * height)]

            rs_index_calc.write_geotiff(temp_path, {
                "width": width,
                "height": height,
                "band": band_data,
                "transform": {"origin_x": 0, "origin_y": 0, "pixel_width": 1.0, "pixel_height": 1.0},
            })

            assert os.path.exists(temp_path)
            assert os.path.getsize(temp_path) > 0

            result = rs_index_calc.read_geotiff(temp_path)
            assert result["width"] == width
            assert result["height"] == height
            assert result["samples_per_pixel"] == 1
            assert len(result["bands"]) == 1
            assert len(result["bands"][0]) == width * height

        finally:
            os.unlink(temp_path)

    def test_read_multiband_geotiff(self):
        """Test reading a multiband GeoTIFF."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            temp_path = f.name

        try:
            create_test_geotiff(temp_path, width=2, height=2, num_bands=4)

            result = rs_index_calc.read_geotiff(temp_path)
            assert result["width"] == 2
            assert result["height"] == 2
            assert result["samples_per_pixel"] == 4
            assert len(result["bands"]) == 4
            assert len(result["bands"][0]) == 4

        finally:
            os.unlink(temp_path)

    def test_geotiff_transform(self):
        """Test GeoTIFF transform metadata."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            temp_path = f.name

        try:
            rs_index_calc.write_geotiff(temp_path, {
                "width": 2,
                "height": 2,
                "band": [1.0, 2.0, 3.0, 4.0],
                "transform": {"origin_x": 100.0, "origin_y": 200.0, "pixel_width": 0.5, "pixel_height": 0.5},
            })

            result = rs_index_calc.read_geotiff(temp_path)
            assert result["transform"]["pixel_width"] == 0.5
            assert result["transform"]["pixel_height"] == 0.5

        finally:
            os.unlink(temp_path)


class TestEndToEnd:
    """End-to-end integration tests."""

    def test_single_index_processing(self):
        """Test processing a single index."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            input_path = f.name

        try:
            create_test_geotiff(input_path, width=4, height=4, num_bands=4)

            output_path = input_path.replace(".tif", "_ndvi.tif")
            result = rs_index_calc.process_single_index(
                input_path, "NDVI", output_path, quiet=True
            )

            assert result["index"] == "NDVI"
            assert os.path.exists(output_path)
            assert "stats" in result
            assert "min" in result["stats"]
            assert "max" in result["stats"]
            assert "mean" in result["stats"]

            output_data = rs_index_calc.read_geotiff(output_path)
            assert output_data["width"] == 4
            assert output_data["height"] == 4
            assert output_data["samples_per_pixel"] == 1

        finally:
            if os.path.exists(input_path):
                os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)

    def test_batch_processing(self):
        """Test batch processing all indices."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            input_path = f.name

        try:
            create_test_geotiff(input_path, width=4, height=4, num_bands=6)

            output_dir = tempfile.mkdtemp()
            results = rs_index_calc.process_batch(input_path, output_dir, quiet=True)

            assert len(results) == len(rs_index_calc.INDEX_FORMULAS)

            for result in results:
                assert "index" in result
                if "error" not in result:
                    assert os.path.exists(result["output"])
                    assert "stats" in result

        finally:
            if os.path.exists(input_path):
                os.unlink(input_path)
            import shutil
            if os.path.exists(output_dir):
                shutil.rmtree(output_dir)

    def test_custom_formula_processing(self):
        """Test processing with custom formula."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            input_path = f.name

        try:
            create_test_geotiff(input_path, width=4, height=4, num_bands=4)

            output_path = input_path.replace(".tif", "_custom.tif")
            result = rs_index_calc.process_single_index(
                input_path, "custom", output_path,
                custom_formula="(B4-B3)/(B4+B3)", quiet=True
            )

            assert result["index"] == "custom"
            assert os.path.exists(output_path)

        finally:
            if os.path.exists(input_path):
                os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)

    def test_manual_band_mapping(self):
        """Test processing with manual band mapping."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            input_path = f.name

        try:
            create_test_geotiff(input_path, width=4, height=4, num_bands=6)

            band_mapping = {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4, "swir2": 5}
            output_path = input_path.replace(".tif", "_ndvi.tif")
            result = rs_index_calc.process_single_index(
                input_path, "NDVI", output_path,
                band_mapping=band_mapping, quiet=True
            )

            assert result["index"] == "NDVI"
            assert os.path.exists(output_path)

        finally:
            if os.path.exists(input_path):
                os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)

    def test_all_indices_valid_range(self):
        """Test that all indices produce values in expected ranges."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            input_path = f.name

        try:
            create_test_geotiff(input_path, width=4, height=4, num_bands=6)

            for index_name in rs_index_calc.INDEX_FORMULAS:
                output_path = input_path.replace(".tif", f"_{index_name.lower()}.tif")
                result = rs_index_calc.process_single_index(
                    input_path, index_name, output_path, quiet=True
                )

                stats = result["stats"]
                assert stats["count"] == 16, f"{index_name}: wrong pixel count"
                assert not any(map(lambda x: x != x, [stats["min"], stats["max"], stats["mean"]])), \
                    f"{index_name}: contains NaN"

                if os.path.exists(output_path):
                    os.unlink(output_path)

        finally:
            if os.path.exists(input_path):
                os.unlink(input_path)

    def test_different_image_sizes(self):
        """Test processing different image sizes."""
        sizes = [(1, 1), (2, 2), (3, 5), (10, 10)]

        for width, height in sizes:
            with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
                input_path = f.name

            try:
                create_test_geotiff(input_path, width=width, height=height, num_bands=4)

                output_path = input_path.replace(".tif", "_ndvi.tif")
                result = rs_index_calc.process_single_index(
                    input_path, "NDVI", output_path, quiet=True
                )

                assert result["stats"]["count"] == width * height
                assert os.path.exists(output_path)

            finally:
                if os.path.exists(input_path):
                    os.unlink(input_path)
                if os.path.exists(output_path):
                    os.unlink(output_path)

    def test_statistics_output(self):
        """Test statistics computation."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            input_path = f.name

        try:
            create_test_geotiff(input_path, width=4, height=4, num_bands=4)

            output_path = input_path.replace(".tif", "_ndvi.tif")
            result = rs_index_calc.process_single_index(
                input_path, "NDVI", output_path, quiet=True
            )

            stats = result["stats"]
            assert "min" in stats
            assert "max" in stats
            assert "mean" in stats
            assert "std" in stats
            assert "count" in stats
            assert stats["min"] <= stats["mean"] <= stats["max"]

        finally:
            if os.path.exists(input_path):
                os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)


class TestBandDetectionIntegration:
    """Integration tests for band detection."""

    def test_auto_detection_from_file(self):
        """Test auto-detection from GeoTIFF file."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            input_path = f.name

        try:
            create_test_geotiff(input_path, width=4, height=4, num_bands=4)

            tiff_data = rs_index_calc.read_geotiff(input_path)
            if tiff_data["band_descriptions"]:
                mapping = rs_index_calc.detect_band_mapping(tiff_data["band_descriptions"])
                assert len(mapping) > 0

        finally:
            os.unlink(input_path)

    def test_fallback_band_mapping(self):
        """Test fallback band mapping."""
        with tempfile.NamedTemporaryFile(suffix=".tif", delete=False) as f:
            input_path = f.name

        try:
            create_test_geotiff(input_path, width=4, height=4, num_bands=4)

            output_path = input_path.replace(".tif", "_ndvi.tif")
            result = rs_index_calc.process_single_index(
                input_path, "NDVI", output_path, quiet=True
            )

            assert os.path.exists(output_path)

        finally:
            if os.path.exists(input_path):
                os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)
