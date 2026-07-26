---
description: 'Download OpenStreetMap features via Overpass API. Query by bbox, tag filter, or administrative place name (e.g. 北京市朝阳区). Output GeoJSON and/or Shapefile (UTF-8 with .cpg). Supports roads, buildings, POIs, landuse, natural features, semantic presets (water/road/building/green), multi-format export, and an automatic QA summary.'
name: osm-data-download
---

# OSM Data Download

Download OpenStreetMap features via the Overpass API. Query by bounding box, raw tag, semantic preset, or **administrative place name** (e.g. "北京市朝阳区"). Output GeoJSON and/or Shapefile, optionally zipped, with an automatic QA summary.

## Features

- **By bbox + tag**: Download roads, buildings, POIs, landuse, natural features
- **By place name (NEW)**: `download-place --place "北京市朝阳区" --preset water` resolves the admin polygon via Nominatim, queries within it, optionally clips to the boundary, and writes a QA summary
- **Semantic presets (NEW)**: `water` / `road` / `building` / `green` combine multiple tag filters in one Overpass query
- **Multi-format export (NEW)**: `--formats geojson,shapefile` writes both at once; mixed geometry is auto-split
- **Shapefile zip (NEW)**: `--zip-shapefile` produces a complete .zip bundle (`.shp/.shx/.dbf/.prj/.cpg`) ready for QGIS/ArcGIS
- **Boundary clipping (NEW)**: cross-border features are clipped to the admin polygon so the output exactly matches the requested area
- **QA summary (NEW)**: `--qa` writes a JSON next to the outputs with feature count, geometry stats, bbox, CRS, the resolved place (OSM id, admin level, display name), the Overpass query that ran, and the list of output files
- **Custom Overpass QL**: Run your own queries
- **Multiple outputs**: GeoJSON and Shapefile
- **Rate limiting & endpoint fallback**: tries multiple Overpass mirrors on 429/504
- **UTF-8 encoded Shapefile DBF + .cpg**: Chinese names survive into QGIS/ArcGIS
- **Tag reference**: Built-in list of common OSM tags

## Common Feature Types

| Type | OSM Tag | Examples |
|------|---------|----------|
| Roads | `highway=*` | motorway, primary, residential |
| Buildings | `building=*` | yes, residential, commercial |
| POIs | `amenity=*` | restaurant, school, hospital |
| Landuse | `landuse=*` | residential, forest, farmland |
| Natural | `natural=*` | water, wood, grassland |
| Waterways | `waterway=*` | river, stream, canal |

## Usage

### Download roads in a bounding box
```bash
python scripts\osm-data-download.py download \
  --bbox "116.0,39.5,116.8,40.2" \
  --feature highway --output roads.geojson
```

### Download buildings
```bash
python scripts\osm-data-download.py download \
  --bbox "116.3,39.8,116.5,40.0" \
  --feature building --output buildings.geojson --format geojson
```

### Custom Overpass QL query
```bash
python scripts\osm-data-download.py query \
  --query '[out:json][timeout:60];(node["amenity"="restaurant"](39.8,116.3,40.0,116.5););out body;' \
  --output restaurants.geojson
```

### Download by place name (NEW)
```bash
# One-shot: water features in Chaoyang District, Beijing
python scripts\osm-data-download.py download-place \
  --place "北京市朝阳区" \
  --preset water \
  --formats "geojson,shapefile" \
  --zip-shapefile \
  --qa \
  -o chaoyang_water
```

Outputs (with mixed geometry auto-split into Point/LineString/Polygon shapefiles):
- `chaoyang_water.geojson` — all features
- `chaoyang_water_Point.shp` + sidecars
- `chaoyang_water_LineString.shp` + sidecars
- `chaoyang_water_Polygon.shp` + sidecars
- `chaoyang_water.zip` — all shapefile sidecars in one archive
- `chaoyang_water.qa.json` — feature count, bbox, CRS, OSM place, query, output files

### Download by place + raw feature
```bash
python scripts\osm-data-download.py download-place \
  --place "成都市" \
  --feature highway \
  -o chengdu_roads.geojson
```

### Disable boundary clipping
By default, features are clipped to the admin polygon. To get the raw bbox-only result:
```bash
python scripts\osm-data-download.py download-place --place "朝阳区" --preset water --no-clip -o x
```

### List common tags and presets
```bash
python scripts\osm-data-download.py list-tags
```

## Installation

```bash
pip install requests>=2.28.0 tqdm>=4.64.0
# Or: pip install -r scripts/requirements.txt
```

## Parameters

### `download` (bbox + tag)
- `--bbox`: Bounding box as `lon_min,lat_min,lon_max,lat_max`
- `--feature`: Feature type (`highway`, `building`, `amenity`, `shop`, `tourism`, `landuse`, `natural`, `waterway`)
- `--value`: Specific tag value (e.g., `restaurant`, `motorway`). Omit for all values.
- `--output`: Output file path
- `--format`: Output format (`geojson`, `shapefile`)
- `--query`: Custom Overpass QL query string
- `--timeout`: API timeout in seconds (default: 60)
- `--rate-delay`: Delay between requests in seconds (default: 1.0)

### `download-place` (NEW: by admin place name)
- `--place`: Chinese or English place name (e.g. `北京市朝阳区`, `Chaoyang District, Beijing`)
- `--preset`: Semantic preset (`water`, `road`, `building`, `green`) — combines multiple tag filters in one Overpass query
- `--feature`: Alternative to `--preset`; same choices as `download`
- `--value`: Specific tag value (with `--feature`)
- `-o/--output`: Base output path (extensions are auto-set per format)
- `--formats`: Comma-separated list, e.g. `geojson,shapefile`. Default: single format from `--format`.
- `--zip-shapefile`: Also write a complete .zip of the shapefile sidecars
- `--no-clip`: Skip clipping to the admin polygon (default: clip)
- `--qa`: Write a QA summary JSON
- `--timeout`, `--rate-delay`: same as `download`

## Output

- **GeoJSON**: Standard GeoJSON with OSM tags as properties
- **Shapefile**: ESRI Shapefile with attribute table

## Geometry Types

OSM features come in three geometry types — choose based on your use case:

| Type | OSM Element | Typical Features | Use For |
|------|-------------|-----------------|---------|
| Points | `node` | POIs, amenities, shops | Point-based analysis, heatmaps |
| Lines | `way` (open) | roads, rivers, boundaries | Network analysis, routing |
| Polygons | `way` (closed), `relation` | buildings, landuse, lakes | Area calculations, spatial join |

The tool automatically detects geometry type. Use `--geometry-type` to filter.

## Maximum Bounding Box Size

Large bounding boxes cause timeouts and excessive data:

| Area Size | Recommendation |
|-----------|---------------|
| <0.25°×0.25° | Safe for most queries |
| 0.25°–0.5°×0.25°–0.5° | Recommended maximum for dense urban areas |
| >0.5°×0.5° | Split into smaller tiles; use `--split-bbox 4` |

```bash
# Auto-split large bbox into 4 sub-queries
python scripts\osm-data-download.py download \
  --bbox "115.5,39.0,117.5,41.0" \
  --feature building --output buildings.geojson --split-bbox 4
```

## Shapefile Output

Export directly to ESRI Shapefile format:

```bash
python scripts\osm-data-download.py download \
  --bbox "116.3,39.8,116.5,40.0" \
  --feature building --output buildings.shp --format shapefile
```

**Note**: Shapefile column names are truncated to 10 characters. Use `--format geojson` for full attribute names.

## Character Encoding

Shapefile attribute tables use UTF-8 encoding by default. If you see garbled text in ArcGIS:

- Set environment variable: `SHAPE_ENCODING=UTF-8`
- Or open in QGIS (handles UTF-8 natively)
- GeoJSON output is always UTF-8

## Error Handling and Retry Logic

The tool handles common HTTP errors automatically:

| HTTP Code | Meaning | Tool Behavior |
|-----------|---------|---------------|
| 400 | Bad query syntax | Reports error, suggests fixes |
| 429 | Rate limit exceeded | Waits 60s, retries up to 3 times |
| 504 | Server timeout | Increases timeout, retries up to 3 times |
| 500 | Server error | Waits 30s, retries |

Use `--max-retries 5` and `--retry-delay 120` to customize retry behavior.

## Alternative Overpass Endpoints

If the primary endpoint is slow or unavailable:

| Endpoint | Location | Notes |
|----------|----------|-------|
| `https://overpass-api.de/api/interpreter` | Germany | Default, most stable |
| `https://z.overpass-api.de/api/interpreter` | Germany | Mirror |
| `https://lz4.overpass-api.de/api/interpreter` | Germany | Mirror |
| `https://overpass.kumi.systems/api/interpreter` | Finland | Alternative |
| `https://overpass.openstreetmap.ru/api/interpreter` | Russia | Alternative |

Specify with `--endpoint https://overpass.kumi.systems/api/interpreter`.

## Empty Results Handling

If a query returns no features:

1. Verify bbox coordinates (lon/lat order, sign)
2. Check tag spelling against OSM wiki
3. Try larger bbox — the area may have no mapped features
4. Use `list-tags` to see available features in the area

The tool prints a warning and exits gracefully on empty results.

## Semantic Presets

Presets combine multiple tag filters in a single Overpass query, so the result
covers everything matching that semantic concept without you having to know
the OSM tag vocabulary:

| Preset | OSM tags covered | What you get |
|--------|------------------|--------------|
| `water` | `natural=water`, `waterway=*`, `landuse=reservoir`, `water=river|lake|pond|reservoir` | Rivers, lakes, ponds, reservoirs, moats, canals, streams |
| `road` | `highway=*` | All roads, paths, footways, service roads |
| `building` | `building=*` | All building footprints |
| `green` | `leisure=park/garden`, `landuse=forest/grass/meadow`, `natural=wood/grassland/heath` | Parks, forests, meadows, grasslands |

## QA Summary

When `--qa` is used, a JSON file is written next to the outputs with this shape:

```json
{
  "generated_at": "2026-07-25T12:44:15+00:00",
  "generator": "osm-data-download",
  "feature_count": 979,
  "geometry_types": {"Point": 2, "Polygon": 793, "LineString": 184},
  "property_keys": ["name", "name:zh", "natural", "waterway", "..."],
  "bbox": [116.3447, 39.8089, 116.6392, 40.1101],
  "crs": "EPSG:4326 (WGS84)",
  "place": {
    "query": "北京市朝阳区",
    "display_name": "朝阳区, 北京市, 中国",
    "osm_type": "relation", "osm_id": 2988933,
    "admin_level": "6",
    "bbox": [116.3447, 39.8089, 116.6392, 40.1101],
    "clipped_to_boundary": true
  },
  "preset": {"name": "water", "filters": ["..."]},
  "output_formats": ["geojson", "shapefile"],
  "output_files": ["chaoyang_water.geojson", "chaoyang_water.zip"]
}
```

## Chinese Place Name Resolution

`download-place` calls Nominatim with `countrycodes=cn` and runs multiple
attempts (the raw place string, a structured `{state, city, county}` query,
and the original string with whitespace) so a name like `朝阳区`,
`北京市朝阳区`, or `朝阳区, 北京市` all resolve to the same relation
(OSM relation/2988933 for Chaoyang, Beijing). If the top candidate is
ambiguous (multiple admin polygons with the same name), the command
raises `AmbiguousPlaceError` and lists the candidates rather than
silently picking one.

Please cite OpenStreetMap data (required by ODbL license):

```bibtex
@misc{osm_contributors,
  author       = {{OpenStreetMap contributors}},
  title        = {OpenStreetMap Data},
  howpublished = {\url{https://www.openstreetmap.org}},
  year         = {2024},
  note         = {ODbL License}
}

@software{osm_data_download,
  author  = {ruiduobao},
  title   = {OSM Data Download Tool},
  url     = {https://github.com/ruiduobao/osm-data-download},
  version = {0.1.0},
  year    = {2024},
}
```

When using OSM data, display: `© OpenStreetMap contributors (ODbL)`.

## Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `ConnectionError` | Network issue | Check internet, retry |
| `HTTP 429` | Rate limit | Wait 60s, retry |
| `ValueError` | Invalid bbox format | Check `lon_min,lat_min,lon_max,lat_max` |
| Empty output | No features in area | Verify bbox, check tag spelling |
| `ModuleNotFoundError` | Missing dep | Run pip install |
| `HTTP 504` | Server timeout | Reduce bbox size, increase `--timeout` |
| Garbled text in ArcGIS | Encoding issue | Use UTF-8 or output GeoJSON |

## API Information

- **Endpoint**: `https://overpass-api.de/api/interpreter` (with fallback to `overpass.kumi.systems` and `overpass.private.coffee` on 429/504)
- **No API key required**
- **Nominatim**: `https://nominatim.openstreetmap.org/search` (with fallback to `nominatim.openstreetmap.fr` when the main endpoint is rate-limited)
- **Rate limits**: Please be respectful. Large queries may take time.
- **Data license**: ODbL (OpenStreetMap contributors)

## Dependencies

```
requests>=2.28.0
tqdm>=4.64.0
```

## Data Source

OpenStreetMap via Overpass API. Data © OpenStreetMap contributors (ODbL).

## Visualization

- **QGIS**: Load output GeoJSON/Shapefile directly → Layer → Add Layer → Add Vector Layer
- **Python (geopandas)**: `gdf = gpd.read_file('output.geojson'); gdf.plot()`
- **Leaflet/Mapbox**: Convert to GeoJSON and load in web map
- **Kepler.gl**: Drag-and-drop GeoJSON for interactive visualization

---

## Advanced Usage

### Batch Multi-City Download
```bash
# Download buildings for multiple cities
declare -A cities=( ["北京"]="116.0 39.8 116.8 40.2" ["上海"]="121.0 30.8 122.0 31.5" )
for city in "${!cities[@]}"; do
  python scripts\osm-data-download.py download     --feature building --bbox ${cities[$city]}     --output osm_${city}_buildings.geojson
  sleep 2
done
```

### CI/CD Integration (GitHub Actions)
```yaml
# .github/workflows/update-osm.yml
name: Update OSM Data
