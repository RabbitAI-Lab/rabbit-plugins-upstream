# TomTom Traffic API Reference

## Base
- Base URL: `https://api.tomtom.com`
- Auth: query parameter `key` is required

## Main Services

### Incident Details v5
- `GET /traffic/services/{versionNumber}/incidentDetails`
- `POST /traffic/services/{versionNumber}/incidentDetails`
- `versionNumber = 5`
- Use either `bbox` or `ids`
- `bbox` order: `minLon,minLat,maxLon,maxLat`
- Traffic freshness uses `t` (Traffic Model ID)
- Useful query params: `fields`, `language`, `t`, `categoryFilter`, `timeValidityFilter`

### Raster Incident Tiles
- `GET /traffic/map/{versionNumber}/tile/incidents/{style}/{zoom}/{x}/{y}.{format}`
- `versionNumber = 4`
- Recommended styles: `s0`, `s0-dark`
- Formats: `png`, `gif`
- Useful query params: `t`, `tileSize`

### Vector Incident Tiles
- `GET /traffic/map/{versionNumber}/tile/incidents/{zoom}/{x}/{y}.{format}`
- `versionNumber = 4`
- Format: `pbf`
- Optional `tags` query filter

### Incident Viewport
- `GET /traffic/services/{versionNumber}/incidentViewport/{boundingBox}/{boundingZoom}/{overviewBox}/{overviewZoom}/{copyright}/{contentType}`
- `versionNumber = 4`
- Path params must stay in exact order
- `boundingBox` / `overviewBox` are in EPSG:900913 and use `minY,minX,maxY,maxX`

### Flow Segment Data
- `GET /traffic/services/{versionNumber}/flowSegmentData/{style}/{zoom}/{format}`
- `versionNumber = 4`
- `point` is `latitude,longitude`
- Styles: `relative0`, `relative0-dark`, `absolute`, `relative`, `relative-delay`
- Formats: `xml`, `json`, `jsonp`
- Optional params: `unit`, `thickness`, `openLr`

### Raster Flow Tiles
- `GET /traffic/map/{versionNumber}/tile/flow/{style}/{zoom}/{x}/{y}.{format}`
- `versionNumber = 4`
- Recommended styles: `relative0`, `relative0-dark`
- Format: `png`
- Useful query params: `t`, `tileSize`

### Vector Flow Tiles
- `GET /traffic/map/{versionNumber}/tile/flow/{type}/{zoom}/{x}/{y}.{format}`
- `versionNumber = 4`
- Types: `absolute`, `relative`, `relative-delay`
- Format: `pbf`
- Optional `tags` query filter

## Reminders
- Prefer `t=-1` for newest traffic data when synchronization is not needed.
- Keep coordinate order straight: bbox uses lon/lat pairs, flow segment points use lat/lon.
- Use the least complex endpoint that answers the question.