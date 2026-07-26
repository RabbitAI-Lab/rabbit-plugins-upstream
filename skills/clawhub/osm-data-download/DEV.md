# DEV.md — osm-data-download

## Goal
Download OpenStreetMap features via Overpass API by bbox and tag filter.

## Data Source
OpenStreetMap via Overpass API (https://overpass-api.de/api/interpreter)

## Core Functions
1. **download** — Download OSM features by bbox + tag filter
2. **query** — Run custom Overpass QL query
3. **list-tags** — List common OSM feature tags

## Key Feature Types
- Roads: highway=*
- Buildings: building=*
- POIs: amenity=*, shop=*, tourism=*
- Landuse: landuse=*
- Natural: natural=*, waterway=*

## API Details
- POST to https://overpass-api.de/api/interpreter
- Data format: [out:json][timeout:60]; ...
- Rate limits: be respectful, add delays

## Dependencies
- requests>=2.28.0, tqdm

## Verification
1. `python scripts/osm-data-download.py --help` works
2. `list-tags` subcommand works
