---
name: open-meteo-weather
description: "Current conditions and a short forecast for any city from the free Open-Meteo API (no API key, no account). Uses web_fetch only."
homepage: https://open-meteo.com
metadata: { "openclaw": { "emoji": "🌤️" } }
---

# Open-Meteo weather

Free, keyless weather. Needs only the `web_fetch` tool; no shell, no credentials.

## 1. Find coordinates (skip if you already know them)
Fetch:
`https://geocoding-api.open-meteo.com/v1/search?name=<city>&count=1&language=en&format=json`
Use `results[0].latitude`, `results[0].longitude` and `results[0].timezone`.
Example: Los Angeles is about latitude 34.05, longitude -118.24, timezone America/Los_Angeles.

## 2. Fetch the forecast
`https://api.open-meteo.com/v1/forecast?latitude=<lat>&longitude=<lon>&current=temperature_2m,apparent_temperature,weather_code,wind_speed_10m&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max&temperature_unit=fahrenheit&wind_speed_unit=mph&timezone=<tz>&forecast_days=2`

Use `celsius`/`kmh` instead if the user prefers metric.

## 3. Report
- One line for now: temperature, feels-like, conditions, wind.
- One line per day: high / low, conditions, rain chance (`precipitation_probability_max`).
- Add one practical tip only if it matters (umbrella if rain chance ≥ 40%, heat over 90°F).

## Weather codes (WMO)
0 clear · 1-3 mainly clear / partly cloudy / overcast · 45, 48 fog · 51-57 drizzle ·
61-67 rain · 71-77 snow · 80-82 rain showers · 85-86 snow showers · 95-99 thunderstorm.

## 4. Fallback if Open-Meteo doesn't answer
Some networks can't reach `api.open-meteo.com`. Try once more, then use wttr.in (also keyless):
`https://wttr.in/<City>?format=j1` → `current_condition[0].temp_F`, `weatherDesc[0].value`,
and `weather[0].maxtempF` / `mintempF`, `weather[0].hourly[*].chanceofrain` (take the max).
Say which source you used.

## Notes
- Data: Open-Meteo (CC BY 4.0) or wttr.in. Free for non-commercial use; don't poll more than needed.
- If every source fails, say weather is unavailable rather than guessing.
