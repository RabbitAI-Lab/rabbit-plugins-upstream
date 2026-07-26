---
name: convert-ovobj-to-shp
description: 将奥维互动地图 `.ovobj` 点标签文件和 `.ovkml` 点导出转换为经过校验的 ESRI Shapefile。Use when Codex needs to inspect or convert 奥维互动地图/奥维地图 sampling points, preserve Chinese label names and source coordinates, read declared OVKML coordinate types, avoid GCJ-02/WGS84 offsets, convert geometry to WGS84 EPSG:4326, process one file or a directory, or diagnose incorrect point counts and coordinate shifts.
---

# Convert OVOBJ to SHP

Use the bundled deterministic parser for supported `OviO` zlib-compressed point labels and XML `OVKML` point exports. Do not parse either format ad hoc when the script supports the file.

## 中文说明

将奥维互动地图的点数据转换为 WGS84（EPSG:4326）Shapefile，并保留点名称、原始经纬度和转换后的经纬度。支持两种输入：

- `.ovobj`：在已验证的 OviO 点标签布局中，二进制坐标默认视为 WGS84，不要因为界面显示 GCJ-02 而再次偏移转换。
- `.ovkml`：读取每个点的 `OvCoordType`。`CGCS2000` 与 `WGS84` 直接写入；只有 `GCJ-02` 才转换为 WGS84。

优先使用点数完整的 `.ovkml`。转换报告中的 `point_count`、`parse` 和 `validation.ok` 是核查是否漏点、是否发生坐标偏移的依据。

## Workflow

1. Locate `.ovobj` and `.ovkml` inputs and identify the most complete source file before conversion.
2. Leave `--source-crs` at `auto` unless the user has authoritative coordinate information. In the supported OVOBJ layout, numeric coordinates are stored as WGS84. For OVKML, `OvCoordType` controls automatic detection: `CGCS2000` and `WGS84` remain WGS84; `GCJ-02` is converted to WGS84.
3. Find a Python environment containing `geopandas`, `shapely`, and a Shapefile writer. Prefer an environment explicitly requested by the user.
4. Run `scripts/convert_ovobj_to_shp.py` with an absolute input path.
5. Read the emitted JSON summary and verify the generated `.shp`, `.shx`, `.dbf`, `.prj`, and `.cpg` files.
6. Report the point count, source-coordinate assumption, output CRS, bounds, skipped records, and output path.

## Commands

Convert one OVOBJ with automatic coordinate handling:

```powershell
python scripts/convert_ovobj_to_shp.py "C:\data\samples.ovobj"
```

Convert every OVOBJ and OVKML directly inside a directory:

```powershell
python scripts/convert_ovobj_to_shp.py "C:\data\ovital" --output-dir "C:\data\shp"
```

Add `--recursive` to include subdirectories. Add `--overwrite` only when replacing existing outputs is intended.

## Coordinate Rules

- Write output geometry as WGS84 longitude/latitude with `EPSG:4326`.
- Preserve source values in `src_lon` and `src_lat`, and write converted values in `wgs_lon` and `wgs_lat`.
- Treat GCJ-02 as a coordinate encoding without an EPSG identifier. Do not assign EPSG:4326 directly to unconverted GCJ-02 geometry.
- OVOBJ's user-interface coordinate display may be GCJ-02 while its binary numeric fields are WGS84. Do not convert those fields merely because the source is in mainland China.
- If the source CRS is uncertain and a wrong choice would affect fieldwork, compare against a known point or an OVKML export before using `--source-crs gcj02`.

## Supported Scope

The OVOBJ parser supports point-label files with the `OviO` header, zlib payload beginning at byte 24, point records marked by `AB 00 00 00`, little-endian latitude/longitude at record offsets 136/144, and length-prefixed UTF-8 names. The OVKML parser supports `Placemark > Point > coordinates` records and `OvCoordType`. Stop with a clear error for unsupported headers, compression layouts, coordinate types, tracks, polygons, attachments, encrypted files, ODB databases, or arbitrary future OVOBJ versions.

## Output Contract

Each Shapefile contains `id`, `name`, `source_crs`, `src_lon`, `src_lat`, `wgs_lon`, `wgs_lat`, and point geometry. The script writes UTF-8 `.cpg`, WGS84 `.prj`, and a sibling `*_conversion_report.json`. Treat conversion as successful only when the report shows `validation.ok: true`, including input/output point-count equality and zero geometry-versus-attribute discrepancy.
