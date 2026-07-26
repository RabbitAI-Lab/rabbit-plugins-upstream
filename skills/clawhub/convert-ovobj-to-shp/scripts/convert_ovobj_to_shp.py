from __future__ import annotations

import argparse
import json
import math
import struct
import sys
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path

try:
    import geopandas as gpd
    from shapely.geometry import Point
except ImportError as exc:
    raise SystemExit(
        "Missing dependency. Run this script in a Python environment containing "
        "geopandas, shapely, and a Shapefile writer such as pyogrio or fiona."
    ) from exc


PI = math.pi
A = 6378245.0
EE = 0.00669342162296594323
RECORD_MARKER = b"\xab\x00\x00\x00"
SHAPEFILE_SUFFIXES = (".shp", ".shx", ".dbf", ".prj", ".cpg", ".qix")
SUPPORTED_SUFFIXES = {".ovobj", ".ovkml"}


def out_of_china(lon: float, lat: float) -> bool:
    return not (72.004 <= lon <= 137.8347 and 0.8293 <= lat <= 55.8271)


def transform_lat(x: float, y: float) -> float:
    result = -100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y
    result += 0.2 * math.sqrt(abs(x))
    result += (20.0 * math.sin(6.0 * x * PI) + 20.0 * math.sin(2.0 * x * PI)) * 2.0 / 3.0
    result += (20.0 * math.sin(y * PI) + 40.0 * math.sin(y / 3.0 * PI)) * 2.0 / 3.0
    result += (160.0 * math.sin(y / 12.0 * PI) + 320.0 * math.sin(y * PI / 30.0)) * 2.0 / 3.0
    return result


def transform_lon(x: float, y: float) -> float:
    result = 300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y
    result += 0.1 * math.sqrt(abs(x))
    result += (20.0 * math.sin(6.0 * x * PI) + 20.0 * math.sin(2.0 * x * PI)) * 2.0 / 3.0
    result += (20.0 * math.sin(x * PI) + 40.0 * math.sin(x / 3.0 * PI)) * 2.0 / 3.0
    result += (150.0 * math.sin(x / 12.0 * PI) + 300.0 * math.sin(x / 30.0 * PI)) * 2.0 / 3.0
    return result


def wgs84_to_gcj02(lon: float, lat: float) -> tuple[float, float]:
    if out_of_china(lon, lat):
        return lon, lat
    dlat = transform_lat(lon - 105.0, lat - 35.0)
    dlon = transform_lon(lon - 105.0, lat - 35.0)
    radlat = lat / 180.0 * PI
    magic = 1.0 - EE * math.sin(radlat) ** 2
    sqrt_magic = math.sqrt(magic)
    dlat = dlat * 180.0 / ((A * (1.0 - EE)) / (magic * sqrt_magic) * PI)
    dlon = dlon * 180.0 / (A / sqrt_magic * math.cos(radlat) * PI)
    return lon + dlon, lat + dlat


def gcj02_to_wgs84(lon: float, lat: float) -> tuple[float, float]:
    if out_of_china(lon, lat):
        return lon, lat
    wgs_lon, wgs_lat = lon, lat
    for _ in range(10):
        calc_lon, calc_lat = wgs84_to_gcj02(wgs_lon, wgs_lat)
        dlon, dlat = calc_lon - lon, calc_lat - lat
        wgs_lon -= dlon
        wgs_lat -= dlat
        if max(abs(dlon), abs(dlat)) < 1e-10:
            break
    return wgs_lon, wgs_lat


def resolve_coordinates(lon: float, lat: float, source_crs: str) -> tuple[float, float]:
    return gcj02_to_wgs84(lon, lat) if source_crs == "gcj02" else (lon, lat)


def marker_offsets(payload: bytes) -> list[int]:
    offsets: list[int] = []
    start = 0
    while True:
        found = payload.find(RECORD_MARKER, start)
        if found < 0:
            return offsets
        offsets.append(found)
        start = found + len(RECORD_MARKER)


def decode_name(record: bytes, fallback: str) -> str:
    for length_offset in range(max(0, len(record) - 128), len(record)):
        length = record[length_offset]
        if length == 0 or length_offset + 1 + length > len(record):
            continue
        raw = record[length_offset + 1 : length_offset + 1 + length]
        try:
            value = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        if value.isprintable() and any(ch.isalnum() or "\u4e00" <= ch <= "\u9fff" for ch in value):
            fallback = value
    return fallback


def local_name(element: ET.Element) -> str:
    return element.tag.rsplit("}", 1)[-1]


def child_text(element: ET.Element, name: str) -> str | None:
    for child in element:
        if local_name(child) == name:
            return child.text.strip() if child.text else None
    return None


def crs_from_ovkml(values: set[str], requested: str) -> tuple[str, str]:
    if requested != "auto":
        return requested, f"command line override: {requested.upper()}"
    normalized = {value.upper().replace("-", "").replace("_", "") for value in values if value}
    if not normalized:
        raise ValueError("OVKML has no OvCoordType; pass --source-crs wgs84 or gcj02")
    if normalized <= {"WGS84", "CGCS2000"}:
        return "wgs84", "OvCoordType=" + ",".join(sorted(values))
    if normalized <= {"GCJ02"}:
        return "gcj02", "OvCoordType=" + ",".join(sorted(values))
    raise ValueError(f"OVKML has mixed or unsupported OvCoordType values: {sorted(values)}")


def parse_ovobj(path: Path, requested_crs: str) -> tuple[list[dict[str, object]], dict[str, object]]:
    raw = path.read_bytes()
    if raw[:4] != b"OviO":
        raise ValueError("missing OviO header")
    try:
        payload = zlib.decompress(raw[24:])
    except zlib.error as exc:
        raise ValueError("unsupported OVOBJ compression or layout") from exc

    # The numeric coordinates in the verified OviO point-label layout are stored as WGS84.
    source_crs = "wgs84" if requested_crs == "auto" else requested_crs
    offsets = marker_offsets(payload)
    if not offsets:
        raise ValueError("no supported point records found")

    points: list[dict[str, object]] = []
    invalid_records = 0
    for record_number, start in enumerate(offsets, start=1):
        end = offsets[record_number] if record_number < len(offsets) else len(payload)
        record = payload[start:end]
        if len(record) < 152:
            invalid_records += 1
            continue
        src_lat = struct.unpack_from("<d", record, 136)[0]
        src_lon = struct.unpack_from("<d", record, 144)[0]
        if not (-90.0 <= src_lat <= 90.0 and -180.0 <= src_lon <= 180.0):
            invalid_records += 1
            continue
        wgs_lon, wgs_lat = resolve_coordinates(src_lon, src_lat, source_crs)
        points.append(
            {
                "id": record_number,
                "name": decode_name(record, f"point_{record_number}"),
                "source_crs": source_crs.upper(),
                "src_lon": src_lon,
                "src_lat": src_lat,
                "wgs_lon": wgs_lon,
                "wgs_lat": wgs_lat,
            }
        )
    if not points:
        raise ValueError("records were found, but none contained valid longitude/latitude values")
    return points, {
        "source_format": "OVOBJ",
        "coordinate_basis": (
            "OVOBJ raw coordinates default to WGS84 in this verified OviO point-label layout"
            if requested_crs == "auto"
            else f"command line override: {source_crs.upper()}"
        ),
        "source_crs": source_crs,
        "record_markers": len(offsets),
        "invalid_records": invalid_records,
    }


def parse_ovkml(path: Path, requested_crs: str) -> tuple[list[dict[str, object]], dict[str, object]]:
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as exc:
        raise ValueError("invalid OVKML XML") from exc

    raw_points: list[tuple[str, str, float, float]] = []
    coordinate_types: set[str] = set()
    skipped_placemarks = 0
    for placemark in (element for element in root.iter() if local_name(element) == "Placemark"):
        point = next((element for element in placemark.iter() if local_name(element) == "Point"), None)
        if point is None:
            skipped_placemarks += 1
            continue
        coordinates = next((element.text for element in point.iter() if local_name(element) == "coordinates"), None)
        if not coordinates:
            skipped_placemarks += 1
            continue
        try:
            values = coordinates.strip().split()[0].split(",")
            lon, lat = float(values[0]), float(values[1])
        except (IndexError, ValueError) as exc:
            raise ValueError(f"invalid Point coordinates: {coordinates!r}") from exc
        if not (-90.0 <= lat <= 90.0 and -180.0 <= lon <= 180.0):
            skipped_placemarks += 1
            continue
        name = child_text(placemark, "name") or f"point_{len(raw_points) + 1}"
        coord_type = child_text(placemark, "OvCoordType") or ""
        coordinate_types.add(coord_type)
        raw_points.append((name, coord_type, lon, lat))
    if not raw_points:
        raise ValueError("OVKML contains no valid Point placemarks")

    source_crs, basis = crs_from_ovkml(coordinate_types, requested_crs)
    points = []
    for record_number, (name, _, src_lon, src_lat) in enumerate(raw_points, start=1):
        wgs_lon, wgs_lat = resolve_coordinates(src_lon, src_lat, source_crs)
        points.append(
            {
                "id": record_number,
                "name": name,
                "source_crs": source_crs.upper(),
                "src_lon": src_lon,
                "src_lat": src_lat,
                "wgs_lon": wgs_lon,
                "wgs_lat": wgs_lat,
            }
        )
    return points, {
        "source_format": "OVKML",
        "coordinate_basis": basis,
        "source_crs": source_crs,
        "placemarks": len(raw_points) + skipped_placemarks,
        "point_placemarks": len(raw_points),
        "skipped_placemarks": skipped_placemarks,
    }


def parse_input(path: Path, requested_crs: str) -> tuple[list[dict[str, object]], dict[str, object]]:
    if path.suffix.lower() == ".ovobj":
        return parse_ovobj(path, requested_crs)
    if path.suffix.lower() == ".ovkml":
        return parse_ovkml(path, requested_crs)
    raise ValueError(f"unsupported input format: {path.suffix}")


def remove_existing_output(output: Path) -> None:
    for suffix in SHAPEFILE_SUFFIXES:
        sidecar = output.with_suffix(suffix)
        if sidecar.exists():
            sidecar.unlink()
    report = output.with_name(output.stem + "_conversion_report.json")
    if report.exists():
        report.unlink()


def validate_output(output: Path, source_crs: str, expected_count: int) -> dict[str, object]:
    required = [output.with_suffix(suffix) for suffix in (".shp", ".shx", ".dbf", ".prj", ".cpg")]
    frame = gpd.read_file(output, encoding="UTF-8")
    geometry_errors = [
        max(abs(point.x - float(row.wgs_lon)), abs(point.y - float(row.wgs_lat)))
        for row, point in zip(frame.itertuples(), frame.geometry)
    ]
    max_roundtrip_error = None
    if source_crs == "gcj02" and len(frame):
        errors = []
        for row in frame.itertuples():
            lon, lat = wgs84_to_gcj02(float(row.wgs_lon), float(row.wgs_lat))
            errors.append(max(abs(lon - float(row.src_lon)), abs(lat - float(row.src_lat))))
        max_roundtrip_error = max(errors)
    checks = {
        "components_complete": all(path.exists() for path in required),
        "record_count_matches_input": len(frame) == expected_count,
        "crs_is_epsg_4326": frame.crs is not None and frame.crs.to_epsg() == 4326,
        "all_geometry_is_point": bool((frame.geometry.geom_type == "Point").all()),
        "empty_geometry_count": int(frame.geometry.is_empty.sum()),
        "null_geometry_count": int(frame.geometry.isna().sum()),
        "max_geometry_vs_attribute_degree_error": max(geometry_errors, default=None),
        "max_roundtrip_degree_error": max_roundtrip_error,
    }
    checks["ok"] = bool(
        checks["components_complete"]
        and checks["record_count_matches_input"]
        and checks["crs_is_epsg_4326"]
        and checks["all_geometry_is_point"]
        and checks["empty_geometry_count"] == 0
        and checks["null_geometry_count"] == 0
        and (checks["max_geometry_vs_attribute_degree_error"] is None or checks["max_geometry_vs_attribute_degree_error"] < 1e-12)
        and (max_roundtrip_error is None or max_roundtrip_error < 1e-8)
    )
    return checks


def convert_file(source: Path, output: Path, requested_crs: str, overwrite: bool) -> dict[str, object]:
    existing = [output.with_suffix(suffix) for suffix in SHAPEFILE_SUFFIXES if output.with_suffix(suffix).exists()]
    if existing and not overwrite:
        raise FileExistsError(f"output exists; pass --overwrite to replace it: {output}")
    if overwrite:
        remove_existing_output(output)
    output.parent.mkdir(parents=True, exist_ok=True)

    points, parse_stats = parse_input(source, requested_crs)
    source_crs = str(parse_stats["source_crs"])
    frame = gpd.GeoDataFrame(
        points,
        geometry=[Point(float(item["wgs_lon"]), float(item["wgs_lat"])) for item in points],
        crs="EPSG:4326",
    )
    frame.to_file(output, driver="ESRI Shapefile", encoding="UTF-8", index=False)
    output.with_suffix(".cpg").write_text("UTF-8", encoding="ascii")
    validation = validate_output(output, source_crs, len(frame))

    report = {
        "source": str(source),
        "output": str(output),
        "point_count": len(frame),
        "source_coordinate_system": source_crs.upper(),
        "output_coordinate_system": "WGS 84 / EPSG:4326",
        "source_bounds": [
            float(frame.src_lon.min()),
            float(frame.src_lat.min()),
            float(frame.src_lon.max()),
            float(frame.src_lat.max()),
        ],
        "wgs84_bounds": list(map(float, frame.total_bounds)),
        "fields": list(frame.columns),
        "parse": parse_stats,
        "validation": validation,
    }
    report_path = output.with_name(output.stem + "_conversion_report.json")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def find_inputs(input_path: Path, recursive: bool) -> list[Path]:
    if input_path.is_file():
        if input_path.suffix.lower() not in SUPPORTED_SUFFIXES:
            raise ValueError(f"input is not a supported .ovobj or .ovkml file: {input_path}")
        return [input_path]
    if not input_path.is_dir():
        raise FileNotFoundError(f"input does not exist: {input_path}")
    iterator = input_path.rglob("*") if recursive else input_path.glob("*")
    return sorted(path for path in iterator if path.is_file() and path.suffix.lower() in SUPPORTED_SUFFIXES)


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert Ovital OVOBJ or OVKML point labels to validated WGS84 Shapefiles")
    parser.add_argument("input", type=Path, help="OVOBJ, OVKML, or a directory containing them")
    parser.add_argument("--source-crs", choices=("auto", "wgs84", "gcj02"), default="auto")
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--recursive", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    input_path = args.input.resolve()
    inputs = find_inputs(input_path, args.recursive)
    if not inputs:
        raise SystemExit(f"No .ovobj or .ovkml files found in {input_path}")
    if args.output_dir:
        output_dir = args.output_dir.resolve()
    elif input_path.is_dir():
        output_dir = input_path / "converted_shp"
    else:
        output_dir = input_path.parent

    reports = []
    errors = []
    for source in inputs:
        output = output_dir / f"{source.stem}_WGS84.shp"
        try:
            reports.append(convert_file(source, output, args.source_crs, args.overwrite))
        except Exception as exc:
            errors.append({"source": str(source), "error": str(exc)})

    summary = {
        "converted_count": len(reports),
        "error_count": len(errors),
        "requested_source_crs": args.source_crs.upper(),
        "outputs": reports,
        "errors": errors,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if reports and not errors and all(item["validation"]["ok"] for item in reports) else 1


if __name__ == "__main__":
    sys.exit(main())
