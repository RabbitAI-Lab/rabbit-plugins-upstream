"""Build Ovitalmap-compatible vertex and boundary CSV files."""

import json
import os
import sys
import tempfile
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from utils import (
    build_boundary_string,
    check_duplicate_vertices,
    get_workspace_root,
    read_json_stdin,
    validate_coordinates,
    validate_country_code,
    write_csv,
    write_json_stdout,
)

try:
    import fcntl
except ImportError:  # pragma: no cover - Windows fallback
    fcntl = None


WORKSPACE_ROOT = get_workspace_root()
EXPORTS_DIR = WORKSPACE_ROOT / "ovitalmap_exports"

VERTICES_HEADERS = [
    "文件夹", "名称", "经度", "纬度", "海拔", "文本显示风格", "图标样式", "Comment",
]
BOUNDARY_HEADERS = [
    "文件夹", "名称", "经纬度[经度+纬度]", "线条宽度", "线条颜色",
    "线条不透明度", "闭合", "线型", "轨迹风格", "Comment",
]


def _build_comment(parcel):
    parts = []
    if parcel.get("resolved_provider_name"):
        parts.append(f'提供者:{parcel["resolved_provider_name"]}')
    if parcel.get("archive_date"):
        parts.append(f'归档日期:{parcel["archive_date"]}')
    if parcel.get("cadastre_code"):
        parts.append(f'地籍号:{parcel["cadastre_code"]}')
    return " ".join(parts)


def _validate_parcel_code(value):
    code = str(value or "").strip()
    if not code or len(code) > 120 or any(char in code for char in "/\\\r\n,"):
        raise ValueError("parcel_code contains unsafe characters")
    return code


def prepare_parcels(parcels):
    """Validate and deduplicate a copy of each parcel before any file write."""
    if not isinstance(parcels, list) or not parcels:
        raise ValueError("parcels must be a non-empty list")

    prepared = []
    warnings = []
    errors = []
    seen_codes = set()
    for index, source in enumerate(parcels):
        if not isinstance(source, dict):
            errors.append(f"Parcel {index + 1}: expected an object")
            continue
        parcel = dict(source)
        try:
            parcel["parcel_code"] = _validate_parcel_code(parcel.get("parcel_code"))
        except ValueError as exc:
            errors.append(f"Parcel {index + 1}: {exc}")
            continue

        code = parcel["parcel_code"]
        if code in seen_codes:
            errors.append(f"Parcel {index + 1}: duplicate parcel_code {code}")
        seen_codes.add(code)

        vertices = parcel.get("vertices", [])
        coordinate_errors = validate_coordinates(vertices, require_polygon=True)
        if coordinate_errors:
            errors.extend(f"[{code}] {message}" for message in coordinate_errors)
            continue

        deduped, duplicate_warnings = check_duplicate_vertices(vertices)
        if len(deduped) < 3:
            errors.append(f"[{code}] fewer than three distinct vertices remain")
            continue
        parcel["vertices"] = deduped
        altitudes = parcel.get("altitude", [])
        if altitudes is None:
            altitudes = []
        if not isinstance(altitudes, list):
            errors.append(f"[{code}] altitude must be a list")
            continue
        if len(altitudes) > len(vertices):
            errors.append(
                f"[{code}] altitude has more values than vertices"
            )
            continue
        parcel["altitude"] = altitudes
        warnings.extend(f"[{code}] {message}" for message in duplicate_warnings)
        prepared.append(parcel)

    if errors:
        raise ValueError("; ".join(errors))
    return prepared, warnings


def build_vertices_rows(parcels):
    rows = []
    for parcel in parcels:
        code = parcel["parcel_code"]
        altitudes = parcel.get("altitude", [])
        comment = _build_comment(parcel)
        for index, (lon, lat) in enumerate(parcel["vertices"]):
            altitude = ""
            if index < len(altitudes) and altitudes[index] is not None:
                altitude = str(altitudes[index])
            rows.append(
                {
                    "文件夹": code,
                    "名称": f"{code}_A{index + 1:02d}",
                    "经度": str(lon),
                    "纬度": str(lat),
                    "海拔": altitude,
                    "文本显示风格": "",
                    "图标样式": "1",
                    "Comment": comment,
                }
            )
    return rows


def build_boundary_rows(parcels):
    return [
        {
            "文件夹": parcel["parcel_code"],
            "名称": parcel["parcel_code"],
            "经纬度[经度+纬度]": build_boundary_string(parcel["vertices"]),
            "线条宽度": "3",
            "线条颜色": "0X00FF0000",
            "线条不透明度": "50",
            "闭合": "1",
            "线型": "0",
            "轨迹风格": "1",
            "Comment": _build_comment(parcel),
        }
        for parcel in parcels
    ]


@contextmanager
def _export_lock(export_dir):
    export_dir.mkdir(parents=True, exist_ok=True)
    lock_path = export_dir / ".export.lock"
    with lock_path.open("a+") as handle:
        if fcntl:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            if fcntl:
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def _available_paths(export_dir, identity):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    for sequence in range(1, 1000):
        suffix = "" if sequence == 1 else f"_{sequence:02d}"
        export_id = f"{identity}_{timestamp}{suffix}"
        vertices_path = export_dir / f"{export_id}_vertices.csv"
        boundary_path = export_dir / f"{export_id}_boundary.csv"
        if not vertices_path.exists() and not boundary_path.exists():
            return export_id, vertices_path, boundary_path
    raise RuntimeError("Could not allocate a unique export filename")


def _atomic_write(path, headers, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    os.close(descriptor)
    try:
        write_csv(temporary, headers, rows)
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def build_csvs(parcels, first_code, count, country_code):
    country_code = validate_country_code(country_code)
    first_code = _validate_parcel_code(first_code)
    prepared, warnings = prepare_parcels(parcels)
    if int(count) != len(prepared):
        raise ValueError("count must equal the number of parcels")
    if first_code != prepared[0]["parcel_code"]:
        raise ValueError("first_code must match the first parcel")

    vertices_rows = build_vertices_rows(prepared)
    boundary_rows = build_boundary_rows(prepared)
    export_dir = EXPORTS_DIR / country_code
    identity = (
        prepared[0]["parcel_code"]
        if len(prepared) == 1
        else f"{country_code}_batch_N{len(prepared)}"
    )
    with _export_lock(export_dir):
        export_id, vertices_path, boundary_path = _available_paths(
            export_dir, identity
        )
        _atomic_write(vertices_path, VERTICES_HEADERS, vertices_rows)
        _atomic_write(boundary_path, BOUNDARY_HEADERS, boundary_rows)

    return {
        "export_id": export_id,
        "filename_scheme": "descriptive-v2",
        "vertices_path": str(vertices_path),
        "boundary_path": str(boundary_path),
        "vertices_count": len(vertices_rows),
        "boundary_count": len(boundary_rows),
        "validation_errors": [],
        "duplicate_vertex_warnings": warnings,
    }


def build_single_csvs(parcel, country_code):
    return build_csvs(
        [parcel],
        parcel["parcel_code"],
        1,
        country_code,
    )


def main():
    try:
        data = read_json_stdin()
        result = build_csvs(
            data["parcels"],
            data["first_code"],
            data["count"],
            data.get("country_code", data.get("iso3", "")),
        )
        write_json_stdout(result)
    except (KeyError, TypeError, ValueError, RuntimeError) as exc:
        write_json_stdout({"error": str(exc)})
        raise SystemExit(2)


if __name__ == "__main__":
    main()
