---
name: "tomtom-traffic-api"
description: "TomTom traffic API skill for incidents, flow, tiles, viewport, and segment lookups."
---

# TomTom

## Purpose
Use this skill when working with TomTom traffic APIs, especially when the user provides OpenAPI docs, asks for traffic incidents or flow data, or needs help forming TomTom requests and interpreting responses.

## Workflow
1. Preflight the live route: confirm a callable HTTP/API tool and a configured TomTom key are available. If either is missing, report that live traffic cannot be queried and do not claim a live result.
2. Identify the user's intent: incidents, flow, map tiles, viewport metadata, or a road-segment lookup.
3. Pick the smallest endpoint that answers the question.
4. Check required identifiers and coordinate order before drafting the request.
5. Keep the TomTom API key as a required query parameter named `key`.
6. Prefer `t=-1` when the user wants the freshest traffic data and no synchronization is required.
7. Return concise, user-facing summaries and avoid exposing raw API details unless the user asks.

## Endpoint Selection
- Use `incidentDetails` for incident records inside a bounding box or by incident IDs.
- Use incident tile endpoints for map overlays and visualizations.
- Use `flowSegmentData` for speed and travel-time data on the road closest to a point.
- Use flow tile endpoints for visual traffic layers.
- Use `incidentViewport` when the request is about legal or technical viewport information.

## Request Rules
- Treat TomTom API versioning carefully: the docs provided use `versionNumber=5` for `incidentDetails` and `versionNumber=4` for the other listed traffic services.
- For `incidentDetails`, use `bbox=minLon,minLat,maxLon,maxLat` or `ids`, not both.
- For `flowSegmentData`, the `point` parameter is `latitude,longitude` in EPSG:4326.
- For viewport paths, preserve the exact path parameter order from the spec.
- Do not guess units, zoom levels, or styles if the user has not specified them and they matter.

## Practical Defaults
- Prefer `relative0` or `relative0-dark` for raster flow tiles.
- Prefer `s0` or `s0-dark` for raster incident tiles.
- Use `relative` for vector flow tiles unless the user asks for a different flow mode.
- Use `json` for response formats unless a tile or image format is required.

## Response Style
- Summarize the traffic result in plain language first.
- Include location, severity, delay, speed, or closure details when present.
- Mention any missing prerequisite, such as an API key or bounding box, instead of inventing it.

## Reference
Read the bundled TomTom traffic reference for endpoint-specific details and parameter reminders before drafting or validating requests.


