---
name: china-weather
description: Query current conditions and 1-10 day weather forecasts for cities, counties, districts, or coordinates in China, including temperature, apparent temperature, humidity, precipitation, wind, UV, sunrise, and sunset. Use when users ask in Chinese or English about today's weather, tomorrow's weather, rain, temperature, travel conditions, or multi-day forecasts for locations in mainland China, Hong Kong, Macao, or Taiwan. No API key is required.
metadata:
  openclaw:
    requires:
      anyBins:
        - python3
        - python
    emoji: "⛅"
---

# China Weather

Use the bundled script to resolve Chinese place names and retrieve current conditions plus forecasts from Open-Meteo. Do not invent or interpolate missing weather data.

## Query

Run one of these commands from the skill directory:

```bash
python3 scripts/china_weather.py "杭州"
python3 scripts/china_weather.py "深圳南山区" --days 3
python3 scripts/china_weather.py "北京" --days 1 --format json
```

If `python3` is unavailable, use `python`.

For coordinates supplied by the user, bypass place-name resolution:

```bash
python3 scripts/china_weather.py --latitude 31.2304 --longitude 121.4737 --days 5
```

## Respond

1. State the resolved location, including the province or administrative area, so the user can spot an ambiguous match.
2. Give current conditions first when available.
3. Summarize only the requested forecast period. Preserve the units printed by the script.
4. Highlight practical signals such as heavy precipitation, large temperature swings, strong winds, or high UV without exaggerating them.
5. Include the data source and retrieval time shown by the script.
6. If the resolved location is not what the user intended, ask for a province, district, or coordinates and rerun the query.

## Safety and limits

- Treat results as model forecasts, not official warnings or guarantees.
- For typhoons, rainstorms, floods, extreme heat, or other safety-critical conditions, advise the user to verify active alerts with the China Meteorological Administration or the relevant local authority.
- Do not claim that this skill retrieves official Chinese weather warnings.
- Do not send credentials, personal data, or unrelated content to the weather endpoints. This skill requires no API key.
- If the API is unavailable or returns incomplete data, report the failure plainly and suggest retrying; do not substitute fabricated values.

## Data access

The script sends HTTPS GET requests only to:

- `geocoding-api.open-meteo.com` for place-name resolution
- `api.open-meteo.com` for current and forecast data

It uses the Python standard library, writes no files, executes no downloaded code, and reads no environment variables.
