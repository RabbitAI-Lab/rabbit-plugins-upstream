"""Core algorithm tests for spatial-data-validation."""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


@pytest.fixture
def shapely():
    import shapely
    from shapely.geometry import Polygon
    return shapely, Polygon


class TestGeometryValidity:
    def test_valid_polygon(self, shapely):
        _, Polygon = shapely
        ok, reason = M.geometry_validity(Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)]))
        assert ok is True
        assert reason == "valid"

    def test_bowtie_invalid(self, shapely):
        _, Polygon = shapely
        bowtie = Polygon([(0, 0), (1, 1), (1, 0), (0, 1), (0, 0)])
        ok, reason = M.geometry_validity(bowtie)
        assert ok is False
        assert "Self-intersection" in reason

    def test_null_geometry(self):
        ok, reason = M.geometry_validity(None)
        assert ok is False
        assert reason == "null geometry"

    def test_empty_geometry(self, shapely):
        _, Polygon = shapely
        ok, reason = M.geometry_validity(Polygon())
        assert ok is False
        assert "empty" in reason


class TestCheckGeometry:
    def test_counts_valid_invalid(self):
        gdf = M.generate_synthetic([116, 39, 117, 40])
        res = M.check_geometry(gdf)
        assert len(res) == len(gdf)
        invalid_idx = {r["index"] for r in res if not r["valid"]}
        assert invalid_idx == {0, 1}  # bowtie + null


class TestCheckTopology:
    def test_duplicate_detection(self, shapely):
        import geopandas as gpd
        from pyproj import CRS
        _, Polygon = shapely
        poly = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
        gdf = gpd.GeoDataFrame(geometry=[poly, poly], crs=CRS.from_epsg(4326))
        topo = M.check_topology(gdf)
        assert topo["duplicate_geometries"] == 1

    def test_overlap_detection(self, shapely):
        import geopandas as gpd
        from pyproj import CRS
        _, Polygon = shapely
        a = Polygon([(0, 0), (2, 0), (2, 2), (0, 2), (0, 0)])
        b = Polygon([(1, 1), (3, 1), (3, 3), (1, 3), (1, 1)])  # 与 a 重叠 1x1
        gdf = gpd.GeoDataFrame(geometry=[a, b], crs=CRS.from_epsg(4326))
        topo = M.check_topology(gdf)
        assert topo["n_overlaps"] == 1
        assert topo["overlapping_pairs"][0]["overlap_area"] == pytest.approx(1.0)

    def test_disjoint_no_overlap(self, shapely):
        import geopandas as gpd
        from pyproj import CRS
        _, Polygon = shapely
        a = Polygon([(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)])
        b = Polygon([(5, 5), (6, 5), (6, 6), (5, 6), (5, 5)])
        gdf = gpd.GeoDataFrame(geometry=[a, b], crs=CRS.from_epsg(4326))
        topo = M.check_topology(gdf)
        assert topo["n_overlaps"] == 0
        assert topo["duplicate_geometries"] == 0


class TestCheckAttributes:
    def test_null_fraction(self):
        gdf = M.generate_synthetic([116, 39, 117, 40])
        attr = M.check_attributes(gdf, ["id", "name", "class"])
        assert attr["fields"]["id"]["null_count"] == 0
        assert attr["fields"]["name"]["null_count"] == 1  # 制造的一个缺失
        assert attr["attribute_completeness"] < 1.0

    def test_missing_field_fraction_one(self):
        gdf = M.generate_synthetic([116, 39, 117, 40])
        attr = M.check_attributes(gdf, ["does_not_exist"])
        assert attr["fields"]["does_not_exist"]["present"] is False
        assert attr["fields"]["does_not_exist"]["null_fraction"] == 1.0


class TestCheckCrs:
    def test_consistent(self):
        gdf = M.generate_synthetic([116, 39, 117, 40])
        res = M.check_crs(gdf, 4326)
        assert res["consistent"] is True
        assert res["actual_epsg"] == 4326

    def test_inconsistent(self):
        gdf = M.generate_synthetic([116, 39, 117, 40])
        res = M.check_crs(gdf, 3857)
        assert res["consistent"] is False


class TestGrade:
    def test_grade_boundaries(self):
        assert M.grade_from_score(0.96) == "A"
        assert M.grade_from_score(0.90) == "B"
        assert M.grade_from_score(0.75) == "C"
        assert M.grade_from_score(0.55) == "D"
        assert M.grade_from_score(0.10) == "F"


class TestValidateVector:
    def test_synthetic_overall(self):
        gdf = M.generate_synthetic([116, 39, 117, 40])
        rep = M.validate_vector(gdf, M.DEFAULT_REQUIRED_FIELDS, 4326)
        assert rep["n_features"] == 6
        assert rep["geometry"]["invalid_count"] == 2
        assert 0.0 <= rep["overall_score"] <= 1.0
        assert rep["grade"] in {"A", "B", "C", "D", "F"}


class TestIO:
    def test_geojson_roundtrip(self, tmp_path):
        gdf = M.generate_synthetic([116, 39, 117, 40])
        path = str(tmp_path / "out.geojson")
        M.write_geojson(path, gdf)
        assert os.path.exists(path)
        back = M.read_vector(path)
        assert len(back) == len(gdf)

    def test_write_empty_geojson(self, tmp_path):
        gdf = M.generate_synthetic([116, 39, 117, 40])
        empty = gdf.iloc[0:0]
        path = str(tmp_path / "empty.geojson")
        M.write_geojson(path, empty)
        assert os.path.exists(path)

    def test_read_missing_raises(self):
        with pytest.raises(M.UsageError):
            M.read_vector("/nonexistent/nope.shp")
