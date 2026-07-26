#!/usr/bin/env python3
"""
Remote Sensing Index Calculator
Pure Python GeoTIFF spectral index calculation tool.
No external dependencies - uses only Python standard library.

Privacy disclosure
------------------
This tool reads only local files. No data is sent over the network.

Public domain notice
--------------------
This tool does not transmit any data and does not access any
external services. All processing is local.

License
-------
MIT-0 — No Attribution.
"""

import argparse
import ast
import json
import math
import operator
import os
import struct
import sys
from typing import Dict, List, Optional, Tuple

VERSION = "0.1.0"


def write_qa_summary(qa_path: str, args, run_kind: str, results) -> None:
    """Write a JSON run-summary sidecar to qa_path (Phase 5 optimization).

    Args:
        qa_path: destination JSON file path
        args: argparse.Namespace (we read input / index / output / batch / batch_dir / formula)
        run_kind: one of "single", "batch", "batch_dir"
        results: list of dicts with at least "index" and optionally "output" / "error" / "input"
    """
    import json as _json
    from datetime import datetime as _dt, timezone as _tz

    summary = {
        "skill": "rs-index-calc",
        "version": VERSION,
        "timestamp": _dt.now(_tz.utc).isoformat(),
        "run_kind": run_kind,
        "input": getattr(args, "input", None),
        "index": getattr(args, "index", None),
        "output": getattr(args, "output", None),
        "batch": bool(getattr(args, "batch", False)),
        "batch_dir": getattr(args, "batch_dir", None),
        "formula": getattr(args, "formula", None),
        "computed_indices": sorted({r.get("index") for r in results if r.get("index")}),
        "outputs": [r.get("output") for r in results if r.get("output")],
        "errors": [r.get("error") for r in results if r.get("error")],
        "n_ok": sum(1 for r in results if r.get("ok") is True or r.get("output")),
        "n_err": sum(1 for r in results if r.get("ok") is False or r.get("error")),
    }
    parent = os.path.dirname(os.path.abspath(qa_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(qa_path, "w", encoding="utf-8") as f:
        _json.dump(summary, f, ensure_ascii=False, indent=2)


# Safe AST evaluator — replaces eval() to prevent code execution
_SAFE_BINOPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_SAFE_UNARYOPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}
_SAFE_FUNCTIONS = {
    name: getattr(math, name)
    for name in ("sin", "cos", "tan", "sqrt", "log", "log10", "exp",
                 "abs", "ceil", "floor", "pow")
    if hasattr(math, name)
}


def _safe_eval(node: ast.AST) -> float:
    """Safely evaluate a mathematical AST expression node."""
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return float(node.value)
        raise ValueError(f"Unsupported constant: {node.value!r}")
    if isinstance(node, ast.BinOp):
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        op_type = type(node.op)
        if op_type not in _SAFE_BINOPS:
            raise ValueError(f"Unsupported operator: {op_type.__name__}")
        return _SAFE_BINOPS[op_type](left, right)
    if isinstance(node, ast.UnaryOp):
        operand = _safe_eval(node.operand)
        op_type = type(node.op)
        if op_type not in _SAFE_UNARYOPS:
            raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
        return _SAFE_UNARYOPS[op_type](operand)
    if isinstance(node, ast.Name):
        if node.id in _SAFE_FUNCTIONS:
            return _SAFE_FUNCTIONS[node.id]
        raise ValueError(f"Unsupported name: {node.id}")
    if isinstance(node, ast.Call):
        # Support both simple functions (sin, cos, ...) and math.sqrt style
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name not in _SAFE_FUNCTIONS:
                raise ValueError(f"Unsupported function: {func_name}")
            args = [_safe_eval(a) for a in node.args]
            return _SAFE_FUNCTIONS[func_name](*args)
        elif isinstance(node.func, ast.Attribute):
            # Handle math.sqrt, math.sin, etc.
            if isinstance(node.func.value, ast.Name) and node.func.value.id == "math":
                func_name = node.func.attr
                if func_name not in _SAFE_FUNCTIONS:
                    raise ValueError(f"Unsupported math function: {func_name}")
                args = [_safe_eval(a) for a in node.args]
                return _SAFE_FUNCTIONS[func_name](*args)
            raise ValueError(f"Only math.* attribute calls allowed")
        else:
            raise ValueError("Only simple function calls allowed")
    raise ValueError(f"Unsupported expression: {ast.dump(node)}")


def safe_eval_expr(expr: str) -> float:
    """Parse and safely evaluate a mathematical expression string."""
    try:
        tree = ast.parse(expr, mode="eval")
        return _safe_eval(tree.body)
    except (SyntaxError, ValueError) as e:
        raise ValueError(f"Invalid expression: {expr!r} — {e}")

INDEX_FORMULAS = {
    "NDVI": {"bands": ["nir", "red"], "formula": "(NIR - RED) / (NIR + RED)"},
    "NDBI": {"bands": ["swir1", "nir"], "formula": "(SWIR1 - NIR) / (SWIR1 + NIR)"},
    "NDWI": {"bands": ["green", "nir"], "formula": "(GREEN - NIR) / (GREEN + NIR)"},
    "EVI": {"bands": ["nir", "red", "blue"], "formula": "2.5 * (NIR - RED) / (NIR + 6*RED - 7.5*BLUE + 1)"},
    "SAVI": {"bands": ["nir", "red"], "formula": "(NIR - RED) / (NIR + RED + 0.5) * 1.5"},
    "MNDWI": {"bands": ["green", "swir1"], "formula": "(GREEN - SWIR1) / (GREEN + SWIR1)"},
    "AWEI": {"bands": ["green", "swir1", "nir"], "formula": "4*(GREEN-SWIR1) - (0.25*NIR + 2.75*SWIR1)"},
    "NBR": {"bands": ["nir", "swir2"], "formula": "(NIR - SWIR2) / (NIR + SWIR2)"},
    "BSI": {"bands": ["swir1", "red", "nir", "blue"], "formula": "((SWIR1+RED)-(NIR+BLUE)) / ((SWIR1+RED)+(NIR+BLUE))"},
    "UI": {"bands": ["swir2", "nir"], "formula": "(SWIR2 - NIR) / (SWIR2 + NIR)"},
}

BAND_ALIASES = {
    "red": ["red", "r", "band4", "b4", "band 4", "red band"],
    "green": ["green", "g", "band3", "b3", "band 3", "green band"],
    "blue": ["blue", "b", "band2", "b2", "band 2", "blue band"],
    "nir": ["nir", "near infrared", "band5", "b5", "band 5", "nir band", "near-infrared"],
    "swir1": ["swir1", "swir", "shortwave infrared 1", "band6", "b6", "band 6", "swir 1"],
    "swir2": ["swir2", "shortwave infrared 2", "band7", "b7", "band 7", "swir 2"],
}

TIFF_TAGS = {
    256: "ImageWidth",
    257: "ImageLength",
    258: "BitsPerSample",
    259: "Compression",
    262: "PhotometricInterpretation",
    273: "StripOffsets",
    274: "Orientation",
    277: "SamplesPerPixel",
    278: "RowsPerStrip",
    279: "StripByteCounts",
    282: "XResolution",
    283: "YResolution",
    284: "PlanarConfiguration",
    296: "ResolutionUnit",
    305: "Software",
    339: "SampleFormat",
    33550: "ModelPixelScaleTag",
    33922: "ModelTiepointTag",
    34735: "GeoKeyDirectoryTag",
    34736: "GeoDoubleParamsTag",
    34737: "GeoAsciiParamsTag",
}


def read_tiff_header(filepath: str) -> dict:
    """Read TIFF file header and IFD entries."""
    with open(filepath, "rb") as f:
        byte_order = f.read(2)
        if byte_order == b"II":
            endian = "<"
        elif byte_order == b"MM":
            endian = ">"
        else:
            raise ValueError(f"Invalid TIFF byte order: {byte_order}")

        magic = struct.unpack(f"{endian}H", f.read(2))[0]
        if magic != 42:
            raise ValueError(f"Invalid TIFF magic number: {magic}")

        ifd_offset = struct.unpack(f"{endian}I", f.read(4))[0]

        f.seek(ifd_offset)
        num_entries = struct.unpack(f"{endian}H", f.read(2))[0]

        tags = {}
        for _ in range(num_entries):
            tag_id = struct.unpack(f"{endian}H", f.read(2))[0]
            type_id = struct.unpack(f"{endian}H", f.read(2))[0]
            count = struct.unpack(f"{endian}I", f.read(4))[0]

            type_sizes = {1: 1, 2: 1, 3: 2, 4: 4, 5: 8, 6: 1, 7: 1, 8: 2, 9: 4, 10: 8, 11: 4, 12: 8}
            type_formats = {1: "B", 2: "B", 3: "H", 4: "I", 5: "I", 6: "b", 7: "B", 8: "h", 9: "i", 10: "i", 11: "f", 12: "d"}

            value_size = type_sizes.get(type_id, 1) * count

            if value_size <= 4:
                raw = f.read(4)
                if type_id == 2:
                    value = raw[:count].decode("ascii", errors="replace").rstrip("\x00")
                elif type_id in (5, 10):
                    if count == 1:
                        value = struct.unpack(f"{endian}{type_formats[type_id]}", raw[:type_sizes[type_id]])[0]
                    else:
                        value = []
                        for i in range(count):
                            value.append(struct.unpack(f"{endian}{type_formats[type_id]}", raw[i*type_sizes[type_id]:(i+1)*type_sizes[type_id]])[0])
                else:
                    if count == 1:
                        value = struct.unpack(f"{endian}{type_formats[type_id]}", raw[:type_sizes[type_id]])[0]
                    else:
                        value = []
                        for i in range(count):
                            value.append(struct.unpack(f"{endian}{type_formats[type_id]}", raw[i*type_sizes[type_id]:(i+1)*type_sizes[type_id]])[0])
            else:
                offset = struct.unpack(f"{endian}I", f.read(4))[0]
                current_pos = f.tell()
                f.seek(offset)

                if type_id == 2:
                    value = f.read(count).decode("ascii", errors="replace").rstrip("\x00")
                else:
                    value = []
                    for i in range(count):
                        if type_id in (5, 10):
                            num = struct.unpack(f"{endian}I", f.read(4))[0]
                            den = struct.unpack(f"{endian}I", f.read(4))[0]
                            value.append((num, den))
                        else:
                            value.append(struct.unpack(f"{endian}{type_formats[type_id]}", f.read(type_sizes[type_id]))[0])
                    if len(value) == 1:
                        value = value[0]

                f.seek(current_pos)

            tags[tag_id] = value

        return {"endian": endian, "tags": tags}


def read_geotiff(filepath: str) -> dict:
    """Read a GeoTIFF file and return image data with metadata."""
    header = read_tiff_header(filepath)
    tags = header["tags"]
    endian = header["endian"]

    width = tags.get(256, 0)
    height = tags.get(257, 0)
    bits_per_sample = tags.get(258, 8)
    samples_per_pixel = tags.get(277, 1)
    sample_format = tags.get(339, 1)
    compression = tags.get(259, 1)

    if isinstance(bits_per_sample, list):
        bps = bits_per_sample[0]
    else:
        bps = bits_per_sample

    if isinstance(sample_format, list):
        sf = sample_format[0]
    else:
        sf = sample_format

    if compression != 1:
        raise ValueError(f"Compression not supported: {compression}. Only uncompressed TIFF is supported.")

    type_map = {1: {1: "B", 8: "B", 16: "H", 32: "I"}, 2: {8: "b", 16: "h", 32: "i"}, 3: {32: "f", 64: "d"}}
    pack_format = type_map.get(sf, type_map[1]).get(bps, "B")

    strip_offsets = tags.get(273, [])
    strip_byte_counts = tags.get(279, [])

    if not isinstance(strip_offsets, list):
        strip_offsets = [strip_offsets]
    if not isinstance(strip_byte_counts, list):
        strip_byte_counts = [strip_byte_counts]

    with open(filepath, "rb") as f:
        all_data = bytearray()
        for offset, byte_count in zip(strip_offsets, strip_byte_counts):
            f.seek(offset)
            all_data.extend(f.read(byte_count))

    bands = []
    bytes_per_pixel = bps // 8

    for band_idx in range(samples_per_pixel):
        band_data = []
        for y in range(height):
            for x in range(width):
                pixel_offset = (y * width + x) * samples_per_pixel * bytes_per_pixel + band_idx * bytes_per_pixel
                if pixel_offset + bytes_per_pixel <= len(all_data):
                    value = struct.unpack(f"{endian}{pack_format}", all_data[pixel_offset:pixel_offset + bytes_per_pixel])[0]
                    band_data.append(value)
                else:
                    band_data.append(0)
        bands.append(band_data)

    pixel_scale = tags.get(33550, [1.0, 1.0, 0.0])
    tiepoint = tags.get(33922, [0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    if isinstance(pixel_scale, (int, float)):
        pixel_scale = [pixel_scale, pixel_scale, 0.0]
    if isinstance(tiepoint, (int, float)):
        tiepoint = [tiepoint, 0, 0, 0, 0, 0]

    transform = {
        "origin_x": tiepoint[3] if len(tiepoint) > 3 else 0,
        "origin_y": tiepoint[4] if len(tiepoint) > 4 else 0,
        "pixel_width": pixel_scale[0] if len(pixel_scale) > 0 else 1.0,
        "pixel_height": pixel_scale[1] if len(pixel_scale) > 1 else 1.0,
    }

    band_descriptions = []
    geo_ascii = tags.get(34737, "")
    if geo_ascii:
        band_descriptions = [d.strip() for d in geo_ascii.split("|") if d.strip()]

    return {
        "width": width,
        "height": height,
        "bands": bands,
        "samples_per_pixel": samples_per_pixel,
        "bits_per_sample": bps,
        "sample_format": sf,
        "transform": transform,
        "band_descriptions": band_descriptions,
        "tags": tags,
        "endian": endian,
    }


def write_geotiff(filepath: str, data: dict) -> None:
    """Write a single-band GeoTIFF file."""
    width = data["width"]
    height = data["height"]
    band_data = data["band"]
    transform = data.get("transform", {})
    endian = "<"

    origin_x = transform.get("origin_x", 0)
    origin_y = transform.get("origin_y", 0)
    pixel_width = transform.get("pixel_width", 1)
    pixel_height = transform.get("pixel_height", 1)

    header_size = 8
    ifd_entries = 17
    ifd_size = 2 + ifd_entries * 12 + 4
    pixel_data_offset = header_size + ifd_size

    pixel_data = bytearray()
    for value in band_data:
        pixel_data.extend(struct.pack(f"{endian}f", float(value)))

    geo_double_offset = pixel_data_offset + len(pixel_data)
    geo_ascii_offset = geo_double_offset + 48

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
        write_tag(277, 3, 1, 1)
        write_tag(278, 4, 1, height)
        write_tag(279, 4, 1, len(pixel_data))
        write_tag(284, 3, 1, 1)
        write_tag(339, 3, 1, 3)

        write_tag(33550, 12, 3, geo_double_offset)
        write_tag(33922, 12, 6, geo_double_offset + 24)

        write_tag(34735, 3, 0, 0)
        write_tag(34736, 12, 0, 0)
        write_tag(34737, 2, len("RS Index Calculator\x00"), geo_ascii_offset)

        f.write(struct.pack(f"{endian}I", 0))

        f.write(pixel_data)

        f.write(struct.pack(f"{endian}d", pixel_width))
        f.write(struct.pack(f"{endian}d", abs(pixel_height)))
        f.write(struct.pack(f"{endian}d", 0.0))

        f.write(struct.pack(f"{endian}d", 0.0))
        f.write(struct.pack(f"{endian}d", 0.0))
        f.write(struct.pack(f"{endian}d", 0.0))
        f.write(struct.pack(f"{endian}d", origin_x))
        f.write(struct.pack(f"{endian}d", origin_y))
        f.write(struct.pack(f"{endian}d", 0.0))

        geo_ascii = "RS Index Calculator\x00"
        f.write(geo_ascii.encode("ascii"))


def detect_band_mapping(band_descriptions: List[str]) -> Dict[str, int]:
    """Auto-detect band mapping from band descriptions."""
    import re
    mapping = {}

    for i, desc in enumerate(band_descriptions):
        desc_lower = desc.lower().strip()
        for band_name, aliases in BAND_ALIASES.items():
            for alias in aliases:
                alias_lower = alias.lower()
                if len(alias_lower) <= 2:
                    pattern = r'\b' + re.escape(alias_lower) + r'\b'
                    if re.search(pattern, desc_lower):
                        if band_name not in mapping:
                            mapping[band_name] = i
                        break
                else:
                    if alias_lower in desc_lower:
                        if band_name not in mapping:
                            mapping[band_name] = i
                        break

    return mapping


def parse_bands_argument(bands_str) -> Dict[str, int]:
    """Parse manual band order argument."""
    if isinstance(bands_str, list):
        parts = [b.lower() for b in bands_str]
    else:
        parts = bands_str.lower().split()
    mapping = {}

    band_names = ["red", "green", "blue", "nir", "swir1", "swir2"]
    for i, part in enumerate(parts):
        if part in band_names and i < len(parts):
            mapping[part] = i

    return mapping


def safe_divide(numerator: float, denominator: float) -> float:
    """Safe division that returns 0 for zero denominator."""
    if abs(denominator) < 1e-10:
        return 0.0
    return numerator / denominator


def calculate_index(index_name: str, bands_data: List[List[float]], band_mapping: Dict[str, int],
                    width: int, height: int, custom_formula: Optional[str] = None) -> List[float]:
    """Calculate a spectral index from band data."""
    if custom_formula:
        return calculate_custom_formula(custom_formula, bands_data, band_mapping, width, height)

    index_name = index_name.upper()
    if index_name not in INDEX_FORMULAS:
        raise ValueError(f"Unknown index: {index_name}. Supported: {', '.join(INDEX_FORMULAS.keys())}")

    formula_info = INDEX_FORMULAS[index_name]
    required_bands = formula_info["bands"]

    for band_name in required_bands:
        if band_name not in band_mapping:
            raise ValueError(f"Band '{band_name}' not mapped. Required bands: {required_bands}")

    # Validate band indices against actual band count
    num_bands = len(bands_data)
    for band_name in required_bands:
        band_idx = band_mapping[band_name]
        if band_idx >= num_bands:
            raise ValueError(
                f"Band index {band_idx} (for '{band_name}') exceeds image band count {num_bands}. "
                f"Image has {num_bands} band(s) but --bands mapping references index {band_idx}."
            )

    result = []
    for i in range(width * height):
        values = {}
        for band_name in required_bands:
            band_idx = band_mapping[band_name]
            values[band_name.upper()] = bands_data[band_idx][i]

        try:
            if index_name == "NDVI":
                val = safe_divide(values["NIR"] - values["RED"], values["NIR"] + values["RED"])
            elif index_name == "NDBI":
                val = safe_divide(values["SWIR1"] - values["NIR"], values["SWIR1"] + values["NIR"])
            elif index_name == "NDWI":
                val = safe_divide(values["GREEN"] - values["NIR"], values["GREEN"] + values["NIR"])
            elif index_name == "EVI":
                denominator = values["NIR"] + 6 * values["RED"] - 7.5 * values["BLUE"] + 1
                val = 2.5 * safe_divide(values["NIR"] - values["RED"], denominator)
            elif index_name == "SAVI":
                val = safe_divide(values["NIR"] - values["RED"], values["NIR"] + values["RED"] + 0.5) * 1.5
            elif index_name == "MNDWI":
                val = safe_divide(values["GREEN"] - values["SWIR1"], values["GREEN"] + values["SWIR1"])
            elif index_name == "AWEI":
                val = 4 * (values["GREEN"] - values["SWIR1"]) - (0.25 * values["NIR"] + 2.75 * values["SWIR1"])
            elif index_name == "NBR":
                val = safe_divide(values["NIR"] - values["SWIR2"], values["NIR"] + values["SWIR2"])
            elif index_name == "BSI":
                numerator = (values["SWIR1"] + values["RED"]) - (values["NIR"] + values["BLUE"])
                denominator = (values["SWIR1"] + values["RED"]) + (values["NIR"] + values["BLUE"])
                val = safe_divide(numerator, denominator)
            elif index_name == "UI":
                val = safe_divide(values["SWIR2"] - values["NIR"], values["SWIR2"] + values["NIR"])
            else:
                val = 0.0
        except (ZeroDivisionError, KeyError):
            val = 0.0

        result.append(val)

    return result


def calculate_custom_formula(formula: str, bands_data: List[List[float]],
                             band_mapping: Dict[str, int], width: int, height: int) -> List[float]:
    """Calculate index using custom formula (safe AST eval, no eval())."""
    import re

    band_pattern = re.compile(r'\bB(\d+)\b', re.IGNORECASE)

    result = []
    for i in range(width * height):
        eval_formula = formula

        def replace_band(match):
            band_num = int(match.group(1))
            band_idx = band_num - 1
            if 0 <= band_idx < len(bands_data):
                return str(bands_data[band_idx][i])
            return "0"

        eval_formula = band_pattern.sub(replace_band, eval_formula)

        try:
            val = safe_eval_expr(eval_formula)
            if not isinstance(val, (int, float)) or math.isnan(val) or math.isinf(val):
                val = 0.0
        except Exception:
            val = 0.0

        result.append(float(val))

    return result


def compute_statistics(data: List[float]) -> dict:
    """Compute basic statistics for a list of values."""
    valid_data = [v for v in data if not (math.isnan(v) or math.isinf(v))]

    if not valid_data:
        return {"min": 0, "max": 0, "mean": 0, "std": 0, "count": 0}

    n = len(valid_data)
    mean = sum(valid_data) / n
    variance = sum((x - mean) ** 2 for x in valid_data) / n if n > 1 else 0
    std = math.sqrt(variance)

    return {
        "min": min(valid_data),
        "max": max(valid_data),
        "mean": mean,
        "std": std,
        "count": n,
    }


def process_single_index(input_path: str, index_name: str, output_path: Optional[str] = None,
                          band_mapping: Optional[Dict[str, int]] = None,
                          custom_formula: Optional[str] = None, quiet: bool = False) -> dict:
    """Process a single index calculation."""
    tiff_data = read_geotiff(input_path)

    if band_mapping is None:
        if tiff_data["band_descriptions"]:
            band_mapping = detect_band_mapping(tiff_data["band_descriptions"])
        if not band_mapping:
            num_bands = tiff_data["samples_per_pixel"]
            default_mapping = {
                4: {"red": 0, "green": 1, "blue": 2, "nir": 3},
                5: {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4},
                6: {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4, "swir2": 5},
                7: {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4, "swir2": 5},
                8: {"red": 0, "green": 1, "blue": 2, "nir": 3, "swir1": 4, "swir2": 5},
            }
            band_mapping = default_mapping.get(num_bands, {"red": 0, "green": 1, "blue": 2, "nir": 3})

    if output_path is None:
        base, ext = os.path.splitext(input_path)
        output_path = f"{base}_{index_name.lower()}{ext}"

    index_data = calculate_index(
        index_name, tiff_data["bands"], band_mapping,
        tiff_data["width"], tiff_data["height"], custom_formula
    )

    write_geotiff(output_path, {
        "width": tiff_data["width"],
        "height": tiff_data["height"],
        "band": index_data,
        "transform": tiff_data["transform"],
    })

    stats = compute_statistics(index_data)

    if not quiet:
        print(f"\n{'='*50}")
        print(f"Index: {index_name}")
        print(f"Input: {input_path}")
        print(f"Output: {output_path}")
        print(f"{'='*50}")
        print(f"Statistics:")
        print(f"  Min:    {stats['min']:.6f}")
        print(f"  Max:    {stats['max']:.6f}")
        print(f"  Mean:   {stats['mean']:.6f}")
        print(f"  Std:    {stats['std']:.6f}")
        print(f"  Pixels: {stats['count']}")
        print(f"{'='*50}\n")

    return {"index": index_name, "output": output_path, "stats": stats}


def process_batch(input_path: str, output_dir: Optional[str] = None,
                  band_mapping: Optional[Dict[str, int]] = None, quiet: bool = False) -> List[dict]:
    """Process all supported indices for a given input file."""
    results = []

    if output_dir is None:
        output_dir = os.path.dirname(input_path) or "."

    for index_name in INDEX_FORMULAS:
        output_path = os.path.join(output_dir, f"{os.path.splitext(os.path.basename(input_path))[0]}_{index_name.lower()}.tif")
        try:
            result = process_single_index(input_path, index_name, output_path, band_mapping, quiet=quiet)
            results.append(result)
        except Exception as e:
            if not quiet:
                print(f"Error processing {index_name}: {e}")
            results.append({"index": index_name, "error": str(e)})

    return results


def _print_index_list(output_format: str = "text") -> None:
    """Print the list of supported spectral indices.

    Args:
        output_format: 'text' (default) prints a human-readable, comma-separated
            list and a per-index one-line summary. 'json' prints a structured
            list with formula and required bands for each index.
    """
    if output_format == "json":
        indices = []
        for name in sorted(INDEX_FORMULAS.keys()):
            info = INDEX_FORMULAS[name]
            indices.append({
                "name": name,
                "bands": list(info.get("bands", [])),
                "formula": info.get("formula", ""),
            })
        print(json.dumps({"count": len(indices), "indices": indices},
                         ensure_ascii=False, indent=2))
    else:
        names = sorted(INDEX_FORMULAS.keys())
        print("Available indices:", ", ".join(names))
        print()
        for name in names:
            info = INDEX_FORMULAS[name]
            bands = ", ".join(info.get("bands", []))
            print(f"  {name:<8s} bands=[{bands}]")


def main():
    parser = argparse.ArgumentParser(
        description="Remote Sensing Index Calculator - Calculate spectral indices from GeoTIFF imagery",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Supported Indices:
  NDVI   - Normalized Difference Vegetation Index
  NDBI   - Normalized Difference Built-up Index
  NDWI   - Normalized Difference Water Index
  EVI    - Enhanced Vegetation Index
  SAVI   - Soil-Adjusted Vegetation Index
  MNDWI  - Modified Normalized Difference Water Index
  AWEI   - Automated Water Extraction Index
  NBR    - Normalized Burn Ratio
  BSI    - Bare Soil Index
  UI      - Urban Index

Examples:
  %(prog)s input.tif NDVI
  %(prog)s input.tif NDVI --output ndvi_result.tif
  %(prog)s input.tif --batch
  %(prog)s input.tif custom --formula "(B4-B3)/(B4+B3)"
  %(prog)s input.tif NDVI --bands red nir green blue swir1 swir2
        """
    )

    parser.add_argument("input", nargs="?", help="Input GeoTIFF file path")
    parser.add_argument("index", nargs="?", help="Index name to calculate (or 'custom')")
    parser.add_argument("--output", "-o", help="Output GeoTIFF file path")
    parser.add_argument("--batch", "-b", action="store_true", help="Calculate all indices")
    parser.add_argument("--batch-dir",
                        help="Process all supported GeoTIFFs in a directory; "
                             "outputs go to <dir>_indices/<basename>_<index>.tif")
    parser.add_argument("--bands", nargs="+", help="Manual band order: red nir green blue swir1 swir2")
    parser.add_argument("--formula", "-f", help="Custom formula (e.g., '(B4-B3)/(B4+B3)')")
    parser.add_argument("--quiet", "-q", action="store_true", help="Suppress output")
    parser.add_argument("--version", "-v", action="version", version=f"%(prog)s {VERSION}")
    parser.add_argument("--stats",
                        help="Output summary statistics (mean/min/max/std) to the given JSON path")
    parser.add_argument("--qa", default=None, metavar="PATH",
                        help="Write a JSON run-summary sidecar to PATH (e.g. --qa run.qa.json). "
                             "Records the input file, requested index, output paths, and "
                             "the set of computed indices.")
    parser.add_argument("--list-indices", action="store_true",
                        help="List all available indices and exit")
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format for --list-indices (and other structured outputs). "
             "Default: 'text' (human-readable). 'json' produces a machine-readable "
             "list with formulas and required bands.",
    )

    args = parser.parse_args()

    if getattr(args, "list_indices", False):
        _print_index_list(args.format)
        return 0

    # Handle missing input: show help and exit(0)
    if args.input is None and not args.batch and not args.batch_dir:
        parser.print_help()
        sys.exit(0)

    if args.input is not None and not os.path.exists(args.input):
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    band_mapping = None
    if args.bands:
        band_mapping = parse_bands_argument(args.bands)

    try:
        if args.batch_dir:
            in_dir = Path(args.batch_dir)
            if not in_dir.is_dir():
                print(f"Error: not a directory: {args.batch_dir}", file=sys.stderr)
                sys.exit(1)
            out_dir = in_dir.parent / (in_dir.name + "_indices")
            out_dir.mkdir(parents=True, exist_ok=True)
            tifs = [p for p in in_dir.iterdir() if p.suffix.lower() in (".tif", ".tiff")]
            if not tifs:
                print(f"No .tif files in {args.batch_dir}", file=sys.stderr)
                sys.exit(1)
            all_results = []
            for src in tifs:
                for idx_name in INDICES:
                    out = out_dir / f"{src.stem}_{idx_name}.tif"
                    try:
                        process_single_index(str(src), idx_name, str(out),
                                             band_mapping, args.formula, True)
                        all_results.append({"input": str(src), "index": idx_name,
                                            "output": str(out), "ok": True})
                    except Exception as e:
                        all_results.append({"input": str(src), "index": idx_name,
                                            "error": str(e), "ok": False})
            print(f"Batch: {len(tifs)} file(s) × {len(INDICES)} indices → {out_dir}")
            ok = sum(1 for r in all_results if r.get("ok"))
            print(f"  OK: {ok}/{len(all_results)}")
            if getattr(args, "qa", None):
                write_qa_summary(args.qa, args, "batch_dir", all_results)
                print(f"QA: {args.qa}")
        elif args.batch:
            results = process_batch(args.input, args.output, band_mapping, args.quiet)
            if not args.quiet:
                print(f"\nBatch processing complete: {len(results)} indices calculated")
                for r in results:
                    if "error" in r:
                        print(f"  {r['index']}: ERROR - {r['error']}")
                    else:
                        print(f"  {r['index']}: {r['output']}")
            if getattr(args, "qa", None):
                write_qa_summary(args.qa, args, "batch", results)
                print(f"QA: {args.qa}")
        elif args.index:
            result = process_single_index(
                args.input, args.index, args.output,
                band_mapping, args.formula, args.quiet
            )
            # Compute and write stats if requested
            if getattr(args, "stats", None) and result:
                try:
                    import numpy as _np
                    import rasterio as _rio
                    with _rio.open(result) as src:
                        arr = src.read(1, masked=True)
                        stats = {
                            "input": args.input,
                            "index": args.index,
                            "output": result,
                            "mean": float(_np.nanmean(arr)) if hasattr(arr, "filled") else float(arr.mean()),
                            "min": float(arr.min()),
                            "max": float(arr.max()),
                            "std": float(arr.std()),
                            "shape": list(arr.shape),
                        }
                    with open(args.stats, "w", encoding="utf-8") as f:
                        json.dump(stats, f, ensure_ascii=False, indent=2)
                    print(f"Stats: {args.stats}")
                except Exception as e:
                    print(f"WARN: stats failed: {e}", file=sys.stderr)
            if getattr(args, "qa", None):
                qa_record = [{"index": args.index, "output": result, "ok": bool(result)}]
                write_qa_summary(args.qa, args, "single", qa_record)
                print(f"QA: {args.qa}")
        else:
            parser.print_help()
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
