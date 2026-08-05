"""Core algorithm tests for crs-transformation."""
import math
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(__file__))
from conftest import mod as M


class TestEPSGTransform:
    def test_4326_to_3857_known_value(self):
        t = M.make_transformer("EPSG:4326", "EPSG:3857")
        xs, ys = M.transform_points([0.0], [0.0], t)
        # 原点 (0,0) 在 Web Mercator 下应为 (0,0)
        assert xs[0] == pytest.approx(0.0, abs=1e-3)
        assert ys[0] == pytest.approx(0.0, abs=1e-3)

    def test_roundtrip_4326_3857(self):
        t_fwd = M.make_transformer("EPSG:4326", "EPSG:3857")
        t_rev = M.make_transformer("EPSG:3857", "EPSG:4326")
        lon, lat = 116.4, 39.9
        mx, my = M.transform_points([lon], [lat], t_fwd)
        blon, blat = M.transform_points(mx, my, t_rev)
        assert blon[0] == pytest.approx(lon, abs=1e-7)
        assert blat[0] == pytest.approx(lat, abs=1e-7)

    def test_invalid_crs_raises(self):
        with pytest.raises(M.UsageError):
            M.make_transformer("EPSG:99999999", "EPSG:4326")

    def test_vectorized_multiple_points(self):
        t = M.make_transformer("EPSG:4326", "EPSG:3857")
        xs, ys = M.transform_points([0.0, 90.0, -90.0], [0.0, 0.0, 0.0], t)
        assert len(xs) == 3
        # 经度 90 在赤道上对应约 10018754 m
        assert xs[1] == pytest.approx(10018754.17, abs=1.0)


class TestChineseSystems:
    def test_wgs84_to_gcj02_offset_positive(self):
        """北京地区 GCJ02 相对 WGS84 有可见偏移（经度偏移量级约 0.005 度）"""
        glon, glat = M.wgs84_to_gcj02(116.4, 39.9)
        assert abs(glon - 116.4) > 0.001
        assert abs(glat - 39.9) > 0.0001

    def test_gcj02_to_wgs84_roundtrip(self):
        """WGS84 -> GCJ02 -> WGS84 往返误差 < 1e-6 度"""
        lon, lat = 116.4, 39.9
        glon, glat = M.wgs84_to_gcj02(lon, lat)
        wlon, wlat = M.gcj02_to_wgs84(glon, glat)
        assert wlon == pytest.approx(lon, abs=1e-6)
        assert wlat == pytest.approx(lat, abs=1e-6)

    def test_bd09_to_gcj02_to_bd09_roundtrip(self):
        """GCJ02 -> BD09 -> GCJ02 往返误差 < 1e-6 度（BD09 反算为近似公式）"""
        glon, glat = 116.4, 39.9
        blon, blat = M.gcj02_to_bd09(glon, glat)
        g2lon, g2lat = M.bd09_to_gcj02(blon, blat)
        assert g2lon == pytest.approx(glon, abs=1e-6)
        assert g2lat == pytest.approx(glat, abs=1e-6)

    def test_outside_china_identity(self):
        """中国境外坐标不做偏移"""
        assert M.wgs84_to_gcj02(0.0, 0.0) == (0.0, 0.0)
        assert M.wgs84_to_gcj02(-122.4, 37.8) == (-122.4, 37.8)

    def test_convert_system_identity(self):
        assert M.convert_system(116.4, 39.9, "wgs84", "wgs84") == (116.4, 39.9)

    def test_convert_system_unknown_raises(self):
        with pytest.raises(M.UsageError):
            M.convert_system(116.4, 39.9, "wgs84", "mars")

    def test_wgs84_bd09_chain_consistent(self):
        """wgs84_to_bd09 应等于 wgs84_to_gcj02 再 gcj02_to_bd09"""
        lon, lat = 116.4, 39.9
        direct = M.wgs84_to_bd09(lon, lat)
        glon, glat = M.wgs84_to_gcj02(lon, lat)
        chain = M.gcj02_to_bd09(glon, glat)
        assert direct[0] == pytest.approx(chain[0], abs=1e-12)
        assert direct[1] == pytest.approx(chain[1], abs=1e-12)


class TestGeoDataFrameTransform:
    def test_transform_to_3857(self):
        gdf = M.generate_synthetic([116, 39, 117, 40], n=5)
        out = M.transform_geodataframe(gdf, "EPSG:3857")
        assert out.crs.to_epsg() == 3857
        # x 坐标量级应为百万米
        assert abs(out.geometry.iloc[0].x) > 1e6

    def test_transform_invalid_raises(self):
        gdf = M.generate_synthetic([116, 39, 117, 40], n=5)
        with pytest.raises(M.ValidationError):
            M.transform_geodataframe(gdf, "EPSG:99999999")


class TestSynthetic:
    def test_generate_points(self):
        gdf = M.generate_synthetic([116, 39, 117, 40], n=10)
        assert len(gdf) == 10
        assert gdf.crs.to_epsg() == 4326
        # 所有点在 bbox 内
        for g in gdf.geometry:
            assert 116.0 <= g.x <= 117.0
            assert 39.0 <= g.y <= 40.0


class TestIO:
    def test_geojson_roundtrip(self, tmp_path):
        gdf = M.generate_synthetic([116, 39, 117, 40], n=5)
        path = str(tmp_path / "pts.geojson")
        M.write_geojson(path, gdf)
        back = M.read_vector(path)
        assert len(back) == 5

    def test_read_missing_raises(self):
        with pytest.raises(M.UsageError):
            M.read_vector("/nonexistent/pts.shp")
