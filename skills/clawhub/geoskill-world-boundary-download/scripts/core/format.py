"""Format conversion: downloaded ZIP/GeoJSON -> requested output format.

Supported input shapes:

* a ZIP containing a Shapefile set (``.shp``/``.shx``/``.dbf``/``.prj``/
  ``.cpg``) - typical geoBoundaries ``all.zip``
* a ZIP or single-file GeoJSON - typical simplified geometry
* a TopoJSON file - rare but supported

Supported output formats:

* ``shp``     - a re-zipped SHP set
* ``geojson`` - a single ``.geojson`` file
* ``gpkg``    - a single ``.gpkg`` (GeoPackage) file
* ``topojson`` - a single ``.topojson`` file

We always reproject outputs to WGS84 (EPSG:4326) so the result is
drop-in for any consumer.
"""

from __future__ import annotations

import io
import json
import os
import re
import shutil
import tempfile
import zipfile
from pathlib import Path
from typing import Optional, Tuple

try:
    import geopandas as gpd  # type: ignore
except ImportError as e:  # pragma: no cover
    raise ImportError("geopandas is required for format conversion") from e

try:
    import pyogrio  # type: ignore  # noqa: F401
    _FAST_READ = True
except ImportError:
    _FAST_READ = False

from .exceptions import FormatError


# ---------------------------------------------------------------------------
# Public format constants
# ---------------------------------------------------------------------------

FORMAT_SHAPEFILE = "shp"
FORMAT_GEOJSON = "geojson"
FORMAT_GEOPACKAGE = "gpkg"
FORMAT_TOPOJSON = "topojson"

SUPPORTED_OUTPUT_FORMATS = (
    FORMAT_SHAPEFILE,
    FORMAT_GEOJSON,
    FORMAT_GEOPACKAGE,
    FORMAT_TOPOJSON,
)

OUTPUT_SUFFIX = {
    FORMAT_SHAPEFILE: ".zip",
    FORMAT_GEOJSON: ".geojson",
    FORMAT_GEOPACKAGE: ".gpkg",
    FORMAT_TOPOJSON: ".topojson",
}


def normalize_format(fmt: str) -> str:
    f = (fmt or "").strip().lower()
    aliases = {
        "shapefile": FORMAT_SHAPEFILE,
        "shape": FORMAT_SHAPEFILE,
        "shp.zip": FORMAT_SHAPEFILE,
        "esri shp": FORMAT_SHAPEFILE,
        "json": FORMAT_GEOJSON,
        "geojson": FORMAT_GEOJSON,
        "gson": FORMAT_GEOJSON,
        "geopackage": FORMAT_GEOPACKAGE,
        "gpkg": FORMAT_GEOPACKAGE,
        "topo": FORMAT_TOPOJSON,
        "topojson": FORMAT_TOPOJSON,
        "topjson": FORMAT_TOPOJSON,
    }
    f = aliases.get(f, f)
    if f not in SUPPORTED_OUTPUT_FORMATS:
        raise FormatError(
            f"unsupported output format: {fmt!r}; expected one of {SUPPORTED_OUTPUT_FORMATS}"
        )
    return f


# ---------------------------------------------------------------------------
# Reading inputs
# ---------------------------------------------------------------------------

def _looks_like_zip(p: Path) -> bool:
    if not p.is_file():
        return False
    try:
        with open(p, "rb") as f:
            sig = f.read(4)
    except OSError:
        return False
    return sig[:2] == b"PK"


def _shp_files_in_zip(zf: zipfile.ZipFile) -> Optional[str]:
    """Return the path of the main SHP inside a zip (relative to the zip root)."""

    shp_names = [n for n in zf.namelist() if n.lower().endswith(".shp")]
    if not shp_names:
        return None
    return shp_names[0]


def _geojson_in_zip(zf: zipfile.ZipFile) -> Optional[str]:
    for n in zf.namelist():
        if n.lower().endswith(".geojson"):
            return n
    return None


def _topojson_in_zip(zf: zipfile.ZipFile) -> Optional[str]:
    for n in zf.namelist():
        if n.lower().endswith((".topojson", ".json")):
            return n
    return None


def read_input(input_path: Path) -> gpd.GeoDataFrame:
    """Read any supported input file (zip / geojson / shp / gpkg / topojson).

    The result is always reprojected to WGS84.
    """

    if not input_path.exists():
        raise FormatError(f"input file not found: {input_path}")

    # If a directory was passed (e.g. an extracted SHP set), find the .shp
    # inside it and delegate to the SHP reader.
    if input_path.is_dir():
        shp_candidates = sorted(input_path.glob("*.shp"))
        if not shp_candidates:
            raise FormatError(
                f"directory {input_path} contains no .shp file"
            )
        return _read_shapefile(shp_candidates[0])

    if _looks_like_zip(input_path):
        return _read_from_zip(input_path)

    # Single-file inputs.
    suffix = input_path.suffix.lower()
    if suffix in (".geojson", ".json"):
        df = _read_geojson(input_path)
    elif suffix in (".shp",):
        df = _read_shapefile(input_path)
    elif suffix in (".gpkg",):
        df = gpd.read_file(input_path)
    elif suffix in (".topojson",):
        df = _read_topojson(input_path)
    else:
        # Last-ditch: try fiona's auto-detect.
        try:
            df = gpd.read_file(input_path)
        except Exception as e:
            raise FormatError(f"could not read input as vector: {input_path} ({e})") from e

    return _ensure_wgs84(df)


def _read_from_zip(zip_path: Path) -> gpd.GeoDataFrame:
    """Open a zipped boundary archive and return its data as a GDF."""

    with zipfile.ZipFile(zip_path) as zf:
        # Preference order: SHP > GeoJSON > TopoJSON (TopoJSON is lossier).
        shp_name = _shp_files_in_zip(zf)
        if shp_name is not None:
            with tempfile.TemporaryDirectory() as td:
                _extract_sibling_files(zf, shp_name, Path(td))
                shp_path = Path(td) / Path(shp_name).name
                return _read_shapefile(shp_path)
        gj = _geojson_in_zip(zf)
        if gj is not None:
            with zf.open(gj) as f:
                df = gpd.read_file(f)
            return _ensure_wgs84(df)
        tj = _topojson_in_zip(zf)
        if tj is not None:
            with tempfile.TemporaryDirectory() as td:
                tpath = Path(td) / Path(tj).name
                with zf.open(tj) as src, open(tpath, "wb") as dst:
                    shutil.copyfileobj(src, dst)
                return _read_topojson(tpath)
    raise FormatError(f"no recognised vector content in {zip_path}")


def _extract_sibling_files(zf: zipfile.ZipFile, shp_name: str, target_dir: Path) -> None:
    """Extract all files that share the .shp's base name (sibling .dbf, .prj, ...)."""

    base = Path(shp_name).name
    # Strip the .shp extension to compare against sibling files.
    if base.lower().endswith(".shp"):
        base = base[:-4]
    suffixes = (".shp", ".shx", ".dbf", ".prj", ".cpg", ".sbn", ".sbx", ".fbn", ".fbx", ".ain", ".aih", ".atx", ".ixs", ".mxs", ".qix", ".qpj")
    for name in zf.namelist():
        if name.endswith("/"):
            continue
        if Path(name).name.startswith(base) and any(name.lower().endswith(s) for s in suffixes):
            target = target_dir / Path(name).name
            with zf.open(name) as src, open(target, "wb") as dst:
                shutil.copyfileobj(src, dst)


def _read_shapefile(path: Path) -> gpd.GeoDataFrame:
    if _FAST_READ:
        try:
            return gpd.read_file(str(path), engine="pyogrio")
        except Exception:
            pass
    return gpd.read_file(str(path))


def _read_geojson(path: Path) -> gpd.GeoDataFrame:
    return gpd.read_file(str(path))


def _read_topojson(path: Path) -> gpd.GeoDataFrame:
    # geopandas can read topojson via the fiona engine. Fall back to
    # converting to GeoJSON in memory using json + manual unwrap if
    # needed.
    try:
        return gpd.read_file(str(path), engine="fiona")
    except Exception:
        pass
    try:
        return gpd.read_file(str(path))
    except Exception as e:
        raise FormatError(f"could not read TopoJSON: {path} ({e})") from e


def _ensure_wgs84(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    if gdf.crs is None:
        # Assume WGS84 — geoBoundaries zips always include a .prj with this CRS.
        gdf = gdf.set_crs(epsg=4326, allow_override=True)
    elif gdf.crs.to_epsg() != 4326:
        gdf = gdf.to_crs(epsg=4326)
    return gdf


# ---------------------------------------------------------------------------
# Writing outputs
# ---------------------------------------------------------------------------

def write_output(
    gdf: gpd.GeoDataFrame,
    output_path: Path,
    fmt: str,
) -> Path:
    """Write *gdf* to *output_path* in the requested format.

    The output directory is created if missing. Returns the resolved
    output path.
    """

    fmt = normalize_format(fmt)
    output_path = output_path.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Strip any user-supplied suffix; we'll add the right one.
    base = output_path.with_suffix("")
    suffix = OUTPUT_SUFFIX[fmt]

    if fmt == FORMAT_GEOJSON:
        out = base.with_suffix(suffix)
        gdf.to_file(out, driver="GeoJSON")
        return out
    if fmt == FORMAT_GEOPACKAGE:
        out = base.with_suffix(suffix)
        gdf.to_file(out, driver="GPKG")
        return out
    if fmt == FORMAT_TOPOJSON:
        # geopandas cannot write TopoJSON directly. Round-trip through
        # GeoJSON then through the topojson Python package if present.
        out = base.with_suffix(suffix)
        try:
            import topojson as topo  # type: ignore
        except ImportError as e:
            raise FormatError(
                "Writing TopoJSON requires the 'topojson' package. "
                "Install it with: pip install topojson"
            ) from e
        geo = json.loads(gdf.to_json())
        tj = topo.Topology(geo, object_name="boundary")
        out.write_text(json.dumps(tj.to_dict()), encoding="utf-8")
        return out
    if fmt == FORMAT_SHAPEFILE:
        return _write_shapefile_zip(gdf, base.with_name(base.name + suffix))

    raise FormatError(f"unhandled format: {fmt}")


def _write_shapefile_zip(gdf: gpd.GeoDataFrame, zip_path: Path) -> Path:
    """Write the GDF to a temp dir, then zip the SHP set into a single archive."""

    # Shapefile field names are limited to 10 chars; truncate defensively.
    rename_map = {}
    used: set[str] = set()
    for col in gdf.columns:
        if col == gdf.geometry.name:
            continue
        new = col[:10]
        if new in used or new == col:
            # Disambiguate by index suffix.
            i = 1
            while f"{new[:8]}_{i}" in used:
                i += 1
            new = f"{new[:8]}_{i}"
        used.add(new)
        if new != col:
            rename_map[col] = new
    if rename_map:
        gdf = gdf.rename(columns=rename_map)

    with tempfile.TemporaryDirectory() as td:
        td_path = Path(td)
        # Pick a stable base name from the zip_path stem.
        base = re.sub(r"[^A-Za-z0-9_-]", "_", zip_path.stem) or "boundary"
        shp_base = td_path / base
        gdf.to_file(str(shp_base) + ".shp", driver="ESRI Shapefile")

        files = [
            str(shp_base) + ext
            for ext in (".shp", ".shx", ".dbf", ".prj", ".cpg")
            if Path(str(shp_base) + ext).exists()
        ]
        zip_path.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for f in files:
                zf.write(f, arcname=Path(f).name)
    return zip_path


# ---------------------------------------------------------------------------
# End-to-end convenience
# ---------------------------------------------------------------------------

def convert(
    input_path: Path,
    output_path: Path,
    fmt: str,
    *,
    clip_bbox: Optional[Tuple[float, float, float, float]] = None,
) -> Path:
    """Read *input_path* (any supported form), optionally clip, write as *fmt*."""

    gdf = read_input(input_path)
    if clip_bbox is not None:
        from .geometry import clip_gdf
        gdf = clip_gdf(gdf, clip_bbox)
    return write_output(gdf, output_path, fmt)
