# QA Rules Reference

## Rule ID Convention

Rules follow the pattern `{CATEGORY}_{CHECK}` where category is one of:
- `FILE` - file-level checks
- `RASTER` - raster-specific checks
- `VECTOR` - vector-specific checks
- `CSV` - table-specific checks
- `NETCDF` - NetCDF-specific checks
- `SHP` - Shapefile companion file checks
- `CROSS` - cross-file consistency checks
- `RULE` - user-configurable rules

## Severity Levels

| Level | Meaning | Default Exit Impact |
|---|---|---|
| `error` | Data is unusable or violates spec | Exit 6 |
| `warning` | Potential issue, needs review | None (unless `--fail-on warning`) |
| `info` | Informational finding | None |

## Built-in Rules

### File-level
- `FILE_READABLE` - file exists and is non-empty
- `FILE_SIZE` - suspiciously small files

### Raster
- `RASTER_CRS` - CRS must be defined
- `RASTER_NODATA` - nodata value should be set
- `RASTER_SIZE` - dimensions must be >= 2x2
- `RASTER_ALL_NODATA` - sample region all nodata
- `RASTER_READ_ERROR` - cannot open with rasterio

### Vector
- `VECTOR_CRS` - CRS must be defined
- `VECTOR_EMPTY` - zero features
- `VECTOR_INVALID_GEOM` - invalid geometries detected
- `SHP_COMPANION` - missing .shx/.dbf/.prj

### Table
- `CSV_ENCODING` - UTF-8 decode errors or null bytes
- `CSV_DUPLICATE_COLS` - duplicate column names
- `CSV_EMPTY` - no header row
- `CSV_NO_DATA` - header only

### NetCDF
- `NETCDF_READ_ERROR` - cannot open with netCDF4

### Cross-file
- `CROSS_CRS_RASTER` - rasters have different CRS
- `CROSS_CRS_VECTOR` - vectors have different CRS
- `CROSS_EXTENT_OVERLAP` - non-overlapping rasters

## Custom Rules (via --rules JSON)

```json
{
  "max_file_size_mb": 500,
  "required_crs": "EPSG:4326",
  "forbidden_extensions": [".tmp", ".bak"]
}
```

## QA Score

```
score = max(0, 100 - errors * 10 - warnings * 2)
```
