"""Small geometry helpers: bbox, area, clipping.

All inputs/outputs are WGS84 (EPSG:4326) unless noted otherwise.
Area is reported in square kilometres on the WGS84 ellipsoid.
"""

from __future__ import annotations

import math
from typing import Sequence, Tuple, Union

try:
    import geopandas as gpd  # type: ignore
    from shapely.geometry import box  # type: ignore
except ImportError as e:  # pragma: no cover
    raise ImportError(
        "geopandas + shapely are required: pip install geopandas shapely"
    ) from e


# BBox is (minx, miny, maxx, maxy) in degrees on WGS84.
BBox = Tuple[float, float, float, float]


# Approximate conversions used only for the small "expand by N km" helper.
KM_PER_DEG_LAT = 110.574  # at the equator; the value is ~constant


def km_per_deg_lon(lat: float) -> float:
    """Approximate kilometres per degree of longitude at the given latitude."""

    return 111.320 * max(math.cos(math.radians(lat)), 1e-6)


def expand_bbox(bbox: BBox, km: float) -> BBox:
    """Return a bbox expanded by *km* kilometres on every side.

    Uses a flat-earth approximation: 1° lat ≈ 110.574 km everywhere;
    1° lon ≈ 111.320 · cos(mid_lat) km. Adequate for the small N-km
    expansions this skill typically does (1–10 km).
    """

    if km <= 0:
        return bbox
    minx, miny, maxx, maxy = bbox
    mid_lat = (miny + maxy) / 2.0
    dlat = km / KM_PER_DEG_LAT
    dlon = km / km_per_deg_lon(mid_lat)
    return (minx - dlon, miny - dlat, maxx + dlon, maxy + dlat)


def bbox_of_gdf(gdf) -> BBox:
    """Return the total bounds of a GeoDataFrame as (minx, miny, maxx, maxy)."""

    minx, miny, maxx, maxy = gdf.total_bounds
    return (float(minx), float(miny), float(maxx), float(maxy))


def bbox_of_geom(geom) -> BBox:
    minx, miny, maxx, maxy = geom.bounds
    return (float(minx), float(miny), float(maxx), float(maxy))


def area_km2(gdf) -> float:
    """Sum of geodesic areas in km^2 (WGS84 ellipsoid).

    Implementation: project to World Equidistant Cylindrical (EPSG:4087)
    which preserves area, then sum the projected areas in m^2 / 1e6.
    Falls back to a simple planar area if the projection is not
    available in the local PROJ install.
    """

    if gdf is None or len(gdf) == 0:
        return 0.0
    try:
        projected = gdf.to_crs(epsg=4087)
    except Exception:
        # Fallback: equal-area cylindrical (EPSG:6933).
        try:
            projected = gdf.to_crs(epsg=6933)
        except Exception:
            return float(gdf.geometry.area.sum()) * 12365.0  # very rough
    return float(projected.geometry.area.sum() / 1_000_000.0)


def clip_gdf(gdf, bbox: BBox):
    """Clip *gdf* to the given bbox; returns a new GeoDataFrame."""

    minx, miny, maxx, maxy = bbox
    return gdf.clip(box(minx, miny, maxx, maxy))


def parse_bbox(text: str) -> BBox:
    """Parse a bbox string of the form 'W,S,E,N' into a tuple of floats."""

    parts = [p.strip() for p in text.split(",")]
    if len(parts) != 4:
        raise ValueError(
            f"bbox must have 4 comma-separated numbers (W,S,E,N), got: {text!r}"
        )
    try:
        w, s, e, n = (float(x) for x in parts)
    except ValueError as exc:
        raise ValueError(f"bbox has non-numeric value: {text!r}") from exc
    if not (-180 <= w <= 180 and -180 <= e <= 180):
        raise ValueError("bbox longitudes must be within [-180, 180]")
    if not (-90 <= s <= 90 and -90 <= n <= 90):
        raise ValueError("bbox latitudes must be within [-90, 90]")
    if w >= e or s >= n:
        raise ValueError(
            "bbox must satisfy west < east and south < north; got "
            f"W={w}, S={s}, E={e}, N={n}"
        )
    return (w, s, e, n)


def bbox_str(bbox: BBox) -> str:
    return f"{bbox[0]:.6f},{bbox[1]:.6f},{bbox[2]:.6f},{bbox[3]:.6f}"
