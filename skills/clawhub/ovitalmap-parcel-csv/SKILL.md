---
name: ovitalmap-parcel-csv
description: Generate and archive Ovitalmap parcel vertex/boundary CSVs. Use when users provide parcel coordinates or images and request 奥维地图 CSV export, archive re-export, or coordinate correction.
---

# Ovitalmap Parcel CSV

Use scripts via JSON stdin/stdout; never reproduce processing manually. Reply with `reply_zh` in Chinese unless another language is requested.

## Setup

Set `OVITALMAP_WORKSPACE` to the user's working directory; otherwise scripts use the current directory.

Parcel input:

```json
{"vertices":[[114.13472,22.50422],[114.13564,22.50411],[114.135,22.503]],"provider_name":"张三","official_id":null,"altitude":[]}
```

Use WGS84 longitude, latitude order. For batches, keep one country per run and providers per parcel unless shared. The pipeline assigns stable `parcel_ref` values (`P01`, `P02`, ...).

## Workflow

1. Extract and display the raw coordinate text.
2. Convert decimal, DMS, or UTM input with `scripts/coordinate_converter.py`. Pass `format` and `coordinates`; also pass decimal `order`, or UTM `zone` and `hemisphere`.
3. Display converted vertices and obtain explicit confirmation of coordinates and providers. Do not write files before confirmation.
4. Obtain the ISO alpha-2 country code from explicit context; ask if uncertain.
5. Run pipeline `--step 1` with `parcels`, `country_code`, and optional `date` (`YYMMDD`). Retain `run_id`; on `needs_input`, ask only for `required_input`.
6. Resolve provider candidates: reuse exact matches; ask before every non-exact or ambiguous match.
7. With the same `run_id`, run:
   - `--step 2b` to classify archive hits and new parcels.
   - `--step 2` to propose codes for new parcels.
   - After the user approves codes, pass `confirmed_codes: true` to `--step 3`.
8. Attach or link every generated file. Label vertex files 顶点表 and boundary files 边界表.

Use `--step all` only with explicit `"confirmed": true` and `"auto_accept_codes": true`.

## Hard Rules

- Treat `error` and `needs_input` as blocking. Do not translate `reply_zh` or expose internal JSON unless asked.
- Never edit archive CSVs manually or guess country, provider, altitude, official ID, UTM zone, or hemisphere.
- Reuse an archive hit's parcel code; never append it again.
- Resolve batch conflicts by `parcel_ref`; never infer whether identical coordinates mean the same parcel.
- Do not replace a non-empty cadastre code without confirmation.
- Preserve vertex order; scripts close polygons.
- Deliver both CSV types. Scripts own the CSV headers and defaults.

## Targeted Archive Actions

Call `scripts/archive_manager.py` with `action`: `scan`, `check_duplicate`, `extract_single`, `update_cadastre`, `backup`, or `correct`.

## References

- Read [references/csv-contract.md](references/csv-contract.md) only when checking or changing CSV compatibility.
- Read [references/reply-contract.md](references/reply-contract.md) when changing interaction gates or user-facing replies.
- Read [references/interaction-and-edge-cases.md](references/interaction-and-edge-cases.md) for delivery, mixed hits, provider ambiguity, official IDs, or corrections.
