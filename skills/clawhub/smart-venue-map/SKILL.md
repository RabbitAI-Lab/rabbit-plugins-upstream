---
name: smart-venue-map
description: Generate or update an offline IMDF indoor venue map with sensor placement, zone groups, and optional camera analytics overlays.
version: 1.0.0
metadata:
  openclaw:
    requires:
      bins:
        - python3
        - npm
---

# Smart Venue Map Skill

Generate a **fully offline, single-file HTML** indoor map with:
- IMDF floor plan rendered via Leaflet.js (bundled inline)
- Per-floor navigation; units colored by category
- Manual sensor/camera placement (persisted in localStorage)
- Zone group management with aggregated analytics popups
- Import/export of placement data as JSON

---

## Inputs the user may provide

| Input | Required | Notes |
|---|---|---|
| IMDF zip file | Required | Apple IMDF format — contains `*.geojson` files |
| VA / analytics data | Optional | Excel (.xlsx), CSV, or JSON with detection counts per camera |
| Venue title & emoji | Optional | Default: "Venue Map Navigator" / 🏢 |
| Sensor color map | Optional | Dict of sensor_id → hex color |
| Age group labels | Optional | Ordered list for age bar chart |

If VA data is missing, the map still works — sensors show "No data linked".

---

## Step 1 — Install dependencies

```bash
python3 -m pip install --user openpyxl  # only if VA data is .xlsx
npm install leaflet                    # provides leaflet.js + leaflet.css
```

Verify Leaflet was installed:
```bash
ls node_modules/leaflet/dist/leaflet.js && echo "OK"
```

---

## Step 2 — Process IMDF + VA data

Use the bundled script: `scripts/process_imdf.py`

```bash
# With Excel VA data
python3 {baseDir}/scripts/process_imdf.py \
  --imdf-zip "path/to/IMDF.zip" \
  --va-xlsx  "path/to/va_data.xlsx" \
  --out-dir  ./outputs

# Without VA data (map only)
python3 {baseDir}/scripts/process_imdf.py \
  --imdf-zip "path/to/IMDF.zip" \
  --out-dir  ./outputs
```

**Outputs:**
- `outputs/imdf_b64.txt` — gzip+base64 IMDF for embedding
- `outputs/dash_data.json` — processed sensor analytics data
- `outputs/imdf_compact.json` — intermediate (for inspection)

**Column auto-detection**: The script recognises common column names
(`camera_id`, `date`, `hour`, `gender`, `age_group`, `eyewear`).
If the user's Excel has different column names, read the file first and
pass the correct field names or patch the `col()` calls in the script.

---

## Step 3 — Generate the HTML

Use Python's string `.replace()` injection — **not f-strings** — because the
template contains JavaScript ternary operators (`?`) that Python would try to
evaluate as f-string expressions.

```python
SKILL_DIR = "{baseDir}"

with open(f'{SKILL_DIR}/references/html_template.html') as f:
    html = f.read()
with open('node_modules/leaflet/dist/leaflet.js') as f:  leaflet_js  = f.read()
with open('node_modules/leaflet/dist/leaflet.css') as f: leaflet_css = f.read()
with open('outputs/imdf_b64.txt') as f:    imdf_b64 = f.read().strip()
with open('outputs/dash_data.json') as f:  va_data  = f.read()

# Customize these for the venue
VENUE_TITLE    = "One Bangkok Retail Data Navigator"
VENUE_SUBTITLE = "IMDF Indoor Map · Camera Groups · VA Analytics Overlay"
VENUE_EMOJI    = "🏢"
LS_KEY         = "oneBangkok_v1"   # localStorage key prefix — change per project

# Sensor color map: sensor_id -> hex color
# Generate automatically from VA data if not provided
import json
va = json.loads(va_data)
PALETTE = ['#1565C0','#2E7D32','#E65100','#C62828','#6A1B9A','#00838F',
           '#AD1457','#F57F17','#0277BD','#558B2F','#BF360C','#4527A0']
sensor_colors = {cid: PALETTE[i % len(PALETTE)] for i, cid in enumerate(va['cameras'])}

# Age group order (must match what's in the data)
age_order = ['Under 18','18-25','26-35','36-45','46-55','56-65','65+']

html = html.replace('__LEAFLET_CSS__',    leaflet_css)
html = html.replace('__LEAFLET_JS__',     leaflet_js)
html = html.replace('__IMDF_B64__',       imdf_b64)
html = html.replace('__VA_DATA__',        va_data)
html = html.replace('__VENUE_TITLE__',    VENUE_TITLE)
html = html.replace('__VENUE_SUBTITLE__', VENUE_SUBTITLE)
html = html.replace('"__VENUE_EMOJI__"',  f'"{VENUE_EMOJI}"')   # in JS
html = html.replace('__VENUE_EMOJI__',    VENUE_EMOJI)           # in HTML
html = html.replace('__LS_KEY__',         LS_KEY)
html = html.replace('__SENSOR_COLORS__',  json.dumps(sensor_colors))
html = html.replace('__AGE_ORDER__',      json.dumps(age_order))

with open('venue_map.html', 'w') as f:
    f.write(html)
print(f"Done — {len(html)//1024}KB")
```

Save the output HTML to the workspace folder so the user can open it.

---

## Key technical patterns (know these to avoid bugs)

### Per-floor marker visibility
Markers are NOT added to the `map` object directly on creation.
They are added/removed in `syncMarkerVisibility()` when the floor changes.
The rule is: `if p.levelId === currentLevel → addTo(map)`.
`L.layerGroup()` does **not** have `.bringToBack()` — do not call it.

### Straight lines on GeoJSON
Set `smoothFactor: 0` on every `L.geoJSON()` call.
The template already does this inside `CAT_STYLE` and `buildLevelLayer()`.

### Unit category colors (CAT_STYLE)
The template uses a light/white color scheme with distinctive fill colors.
Categories: `room`, `walkway`, `restroom`, `escalator`, `elevator`,
`stairs`, `nonpublic`, `opentobelow`, `default`.
Override in `CAT_STYLE` if the venue uses different category names.

### Group data model
Groups use `sensorIds` (not `cameraIds`) as the array key in the JSON.
Old v1 files used `cameraIds` — if importing old data add a migration shim.

### localStorage keys
Use a unique `LS_KEY` per project so different venues don't share state.
Format: `<LS_KEY>_placements` and `<LS_KEY>_groups`.

### VA data structure expected by template
```json
{
  "cameras": ["113034", "113042"],
  "cam_data": {
    "113034": {
      "total": 12500,
      "gender": {"MALE": 7000, "FEMALE": 5500},
      "age": {"Under 18": 200, "18-25": 3000, ...},
      "footfall_hour": {"0": 10, "1": 5, ..., "23": 400},
      "footfall_date": {"2026-06-17": 1800, ...},
      "footfall_dh": {"2026-06-17": {"8": 200, "9": 350, ...}}
    }
  }
}
```

---

## Customisation checklist

- [ ] `VENUE_TITLE` — name shown in header and browser tab
- [ ] `VENUE_SUBTITLE` — subtitle line in header
- [ ] `VENUE_EMOJI` — emoji logo (e.g. 🏢 🛫 🛒 🏥)
- [ ] `LS_KEY` — unique localStorage prefix for this deployment
- [ ] `sensor_colors` — per-sensor colour palette (auto-generated if omitted)
- [ ] `age_order` — match the age labels in the actual data
- [ ] `CAT_STYLE` — adjust colours if venue uses non-standard unit categories
- [ ] `EXCLUDE_UNIT_CATEGORIES` in `process_imdf.py` — filter unwanted unit types

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| Map shows blank / loading forever | IMDF decompression failed | Check browser console; ensure IMDF b64 file is valid |
| All markers show on every floor | Old addMarker code | Ensure `addMarker()` does NOT call `.addTo(map)` unconditionally |
| Lines are curvy | smoothFactor not 0 | Add `smoothFactor:0` to all `L.geoJSON` calls |
| Python SyntaxError in HTML gen | f-string with `?` operator | Use `.replace()` — never f-strings for JS injection |
| Unit outlines missing | Wrong `level_id` field name | Check actual geojson; try `levelId`, `level`, `level_id` |
| VA data shows 0 totals | Column name mismatch | Read Excel headers first; update `col()` calls |
| `bringToBack is not a function` | Called on layerGroup | Remove `.bringToBack()` — only L.Path subclasses support it |

---

## File size expectations

| Component | Approx size |
|---|---|
| Leaflet JS | ~147 KB |
| Leaflet CSS | ~14 KB |
| IMDF b64 (typical mall, parking filtered) | 400–600 KB |
| VA data JSON | 20–60 KB |
| **Total HTML** | **~700 KB** |

For very large venues (>1000 units), consider more aggressive unit filtering
in `process_imdf.py` (e.g. filter `nonpublic` units too).
