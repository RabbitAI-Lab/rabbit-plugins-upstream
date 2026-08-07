"""Core algorithm tests for virtual-globe-export."""
import os
import re
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod


class TestKmlCoord:
    def test_coord_order_lon_lat_alt(self):
        s = mod.format_kml_coord(116.5, 39.5, 120.0)
        assert s == "116.500000,39.500000,120.0"

    def test_coords_space_separated(self):
        pts = [(116.0, 39.0, 0.0), (117.0, 40.0, 10.0)]
        s = mod.format_kml_coords(pts)
        parts = s.split(" ")
        assert len(parts) == 2
        assert parts[0].startswith("116.000000,39.000000")
        assert parts[1].startswith("117.000000,40.000000")

    def test_coord_two_tuple_defaults_alt0(self):
        s = mod.format_kml_coords([(100.0, 30.0)])
        assert s == "100.000000,30.000000,0.0"


class TestKml:
    def _feats(self):
        return [
            {"name": "stationA", "coords": [(116.5, 39.5, 100.0)],
             "time": "2020-01-01T00:00:00Z",
             "properties": {"value": 42, "type": "sensor"}},
        ]

    def test_kml_header_and_namespace(self):
        kml = mod.build_kml(self._feats(), name="Doc")
        assert kml.startswith('<?xml version="1.0"')
        assert 'xmlns="http://www.opengis.net/kml/2.2"' in kml
        assert "<Document>" in kml and "</kml>" in kml

    def test_kml_point_coordinates(self):
        kml = mod.build_kml(self._feats())
        assert "<Point><coordinates>116.500000,39.500000,100.0</coordinates></Point>" in kml

    def test_kml_timestamp(self):
        kml = mod.build_kml(self._feats())
        assert "<TimeStamp><when>2020-01-01T00:00:00Z</when></TimeStamp>" in kml

    def test_kml_extended_data(self):
        kml = mod.build_kml(self._feats())
        assert '<Data name="value"><value>42</value></Data>' in kml

    def test_kml_linestring_for_multi(self):
        feats = [{"name": "path", "coords": [(0, 0, 0), (1, 1, 0), (2, 0, 0)]}]
        kml = mod.build_kml(feats)
        assert "<LineString>" in kml
        assert kml.count("<coordinates>") == 1


class TestCzml:
    def _feats(self):
        return [{"name": "A", "coords": [(116.0, 39.0, 50.0)],
                 "time": "2020-01-01T00:00:00Z", "time_end": "2020-01-01T01:00:00Z",
                 "properties": {"v": 1}}]

    def test_document_packet_first(self):
        packets = mod.build_czml(self._feats(), name="X")
        assert packets[0]["id"] == "document"
        assert packets[0]["version"] == "1.0"

    def test_position_cartographic_degrees(self):
        packets = mod.build_czml(self._feats())
        pos = packets[1]["position"]["cartographicDegrees"]
        assert pos == [116.0, 39.0, 50.0]

    def test_availability_interval(self):
        packets = mod.build_czml(self._feats())
        assert packets[1]["availability"] == "2020-01-01T00:00:00Z/2020-01-01T01:00:00Z"


class TestSynthetic:
    def test_track_generated(self):
        feats, info = mod.generate_synthetic([116, 39, 117, 40], n_points=8)
        # 8 个轨迹点 + 1 条完整 LineString
        assert len(feats) == 9
        assert info["n_points"] == 8
        times = [f["time"] for f in feats if f.get("time")]
        assert all(re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", t) for t in times)

    def test_iso_time_format(self):
        import datetime as dt
        assert mod.iso_time(dt.datetime(2021, 3, 4, 5, 6, 7)) == "2021-03-04T05:06:07Z"


class TestDensity:
    def test_density_counts(self):
        feats = [{"coords": [(0.25, 0.25, 0), (0.75, 0.75, 0)]}]
        grid = mod.track_density_raster(feats, [0, 0, 1, 1], 4, 4)
        assert grid.sum() == 2


class TestGeoTiff:
    def test_write(self, tmp_path):
        arr = np.ones((6, 6), dtype=np.float32)
        path = str(tmp_path / "t.tif")
        mod.write_geotiff(path, arr, [0, 0, 1, 1])
        assert os.path.exists(path)
