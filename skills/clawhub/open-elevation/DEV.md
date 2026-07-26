# Open-Elevation Skill - Development Doc

## Purpose
Batch query elevation data from the Open-Elevation public API by lat/lon coordinates.

## API Reference
- Endpoint: `https://api.open-elevation.com/api/v1/lookup`
- Method: POST
- Request body: `{"locations": [{"latitude": Y, "longitude": X}, ...]}`
- Response: `{"results": [{"latitude": Y, "longitude": X, "elevation": Z}, ...]}`
- No API key required
- Rate limit: keep batches to ~100 points per request

## CLI Design
```
open-elevation lookup --lat 39.9042 --lon 116.4074
open-elevation lookup --lat 39.9042 --lon 116.4074 --json
open-elevation batch --input coords.csv --output results.csv
open-elevation batch --input coords.csv --output results.json --json
```

### Subcommands
- `lookup`: single point query
  - `--lat`: latitude (-90 to 90)
  - `--lon`: longitude (-180 to 180)
  - `--json`: output as JSON
- `batch`: batch query from CSV
  - `--input`: input CSV file (must have lat/lon columns)
  - `--output`: output file path
  - `--json`: output as JSON instead of CSV
  - `--chunk`: points per API call (default 100)

## Privacy
- Only lat/lon coordinates are sent to api.open-elevation.com
- No personal data, cookies, or identifiers sent

## Error Handling
- Validate lat/lon ranges
- Handle network errors gracefully
- Handle empty results
- Validate CSV columns
