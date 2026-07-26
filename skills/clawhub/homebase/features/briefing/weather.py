#!/usr/bin/env python3
"""
Weather Module for Homebase
Fetches weather from Open-Meteo (free, no API key) using configured coordinates.
"""

import json
import os
from datetime import datetime
from typing import Optional, Dict

def _get_coords():
    try:
        from core.config_loader import config
        return config.latitude, config.longitude
    except Exception:
        return 0.0, 0.0  # Set coordinates in config.json
LATITUDE, LONGITUDE = _get_coords()


def _geocode_location(location: str) -> Optional[tuple]:
    """
    Geocode a location name to (lat, lon) using the free Open-Meteo geocoding API.
    Returns None on failure.
    """
    import urllib.parse
    import urllib.request as _req

    try:
        encoded = urllib.parse.quote(location)
        url = (
            f"https://geocoding-api.open-meteo.com/v1/search"
            f"?name={encoded}&count=1&language=en&format=json"
        )
        with _req.urlopen(url, timeout=8) as resp:
            data = json.loads(resp.read().decode())
        results = data.get("results", [])
        if results:
            return results[0]["latitude"], results[0]["longitude"]
    except Exception as e:
        print(f"Geocode failed for '{location}': {e}")
    return None


def fetch_weather(location: Optional[str] = None) -> Optional[Dict]:
    """
    Fetch today's weather from Open-Meteo API.

    Args:
        location: Optional location name (e.g. "Big Bear Lake, CA"). If None,
                  falls back to the configured home coordinates (Irvine, CA).

    Returns structured weather data or None on failure.
    Retries up to 3 times with short back-off (network can be flaky at 7 AM).
    """
    import time as _time
    import urllib.request

    # Resolve coordinates: named location takes priority over home coords
    lat, lon = LATITUDE, LONGITUDE
    if location:
        coords = _geocode_location(location)
        if coords:
            lat, lon = coords
        else:
            print(f"Could not geocode '{location}', falling back to home coords.")

    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,apparent_temperature,weather_code,"
        f"wind_speed_10m,relative_humidity_2m"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_probability_max"
        f"&hourly=precipitation_probability"
        f"&temperature_unit=fahrenheit"
        f"&wind_speed_unit=mph"
        f"&timezone=America/Los_Angeles"
        f"&forecast_days=1"
    )

    last_err = None
    for attempt, delay in enumerate([0, 2, 4]):
        if delay:
            _time.sleep(delay)
        try:
            with urllib.request.urlopen(url, timeout=8) as response:
                data = json.loads(response.read().decode())

            current = data.get("current", {})
            daily   = data.get("daily", {})
            hourly  = data.get("hourly", {})
            code    = current.get("weather_code", 0)

            hourly_probs = hourly.get("precipitation_probability") or []
            rain_windows = _extract_rain_windows(hourly_probs)

            return {
                "temp_current":    round(current.get("temperature_2m", 0)),
                "temp_feels_like": round(current.get("apparent_temperature", 0)),
                "temp_high":       round((daily.get("temperature_2m_max") or [0])[0]),
                "temp_low":        round((daily.get("temperature_2m_min") or [0])[0]),
                "condition":       weather_code_to_description(code),
                "wind_speed":      round(current.get("wind_speed_10m", 0)),
                "humidity":        round(current.get("relative_humidity_2m", 0)),
                "rain_chance":     (daily.get("precipitation_probability_max") or [0])[0],
                "rain_windows":    _format_rain_timing(rain_windows),
            }
        except Exception as e:
            last_err = e
            print(f"Weather fetch attempt {attempt + 1} failed: {e}")

    print(f"Weather fetch gave up after 3 attempts: {last_err}")
    return None


def _extract_rain_windows(hourly_probs: list, threshold: int = 30) -> list:
    """Group consecutive hours with precipitation probability >= threshold."""
    windows = []
    start = None
    for hour, prob in enumerate(hourly_probs):
        if prob >= threshold:
            if start is None:
                start = hour
        else:
            if start is not None:
                windows.append((start, hour - 1))
                start = None
    if start is not None:
        windows.append((start, len(hourly_probs) - 1))
    return windows


def _format_hour(h: int) -> str:
    """Format 0-23 hour as '12 AM', '3 PM', etc."""
    if h == 0:
        return "12 AM"
    elif h < 12:
        return f"{h} AM"
    elif h == 12:
        return "12 PM"
    else:
        return f"{h - 12} PM"


def _format_rain_timing(windows: list) -> str:
    """Format rain windows into a readable string like '2 – 5 PM' or '8 – 10 AM, 3 – 6 PM'."""
    if not windows:
        return ""
    parts = []
    for start, end in windows:
        if start == end:
            parts.append(f"around {_format_hour(start)}")
        else:
            start_suffix = "AM" if start < 12 else "PM"
            end_suffix = "AM" if end < 12 else "PM"
            start_num = start if start <= 12 else start - 12
            end_num = end if end <= 12 else end - 12
            if start_num == 0:
                start_num = 12
            if end_num == 0:
                end_num = 12
            if start_suffix == end_suffix:
                parts.append(f"{start_num}\u2009–\u2009{end_num} {end_suffix}")
            else:
                parts.append(f"{start_num} {start_suffix}\u2009–\u2009{end_num} {end_suffix}")
    return ", ".join(parts)


def weather_code_to_description(code: int) -> str:
    """Convert WMO weather code to human-readable description."""
    codes = {
        0:  "Clear sky",
        1:  "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
        45: "Foggy", 48: "Freezing fog",
        51: "Light drizzle", 53: "Drizzle", 55: "Heavy drizzle",
        61: "Light rain", 63: "Moderate rain", 65: "Heavy rain",
        71: "Light snow", 73: "Moderate snow", 75: "Heavy snow",
        80: "Rain showers", 81: "Moderate showers", 82: "Heavy showers",
        95: "Thunderstorm", 96: "Thunderstorm with hail",
    }
    return codes.get(code, "Mixed conditions")


def generate_weather_suggestion(weather: Dict) -> str:
    """
    Return structured weather facts as a compact string.
    The agent composes the human-readable summary at dispatch time.
    """
    return (
        f"{weather['condition']}, {weather['temp_current']}°F "
        f"(High {weather['temp_high']}°F / Low {weather['temp_low']}°F) · "
        f"Humidity {weather['humidity']}% · Wind {weather['wind_speed']}mph · "
        f"Rain {weather['rain_chance']}%"
    )


def get_weather_briefing() -> Optional[str]:
    """
    Main entry point — fetch weather and generate suggestion.
    Returns formatted string for morning briefing or None on failure.
    """
    weather = fetch_weather()
    if not weather:
        return None

    suggestion = generate_weather_suggestion(weather)

    rain_warning = ""
    if weather["rain_chance"] >= 40:
        timing = weather.get("rain_windows", "")
        if timing:
            rain_warning = f"\n  ☂️ {weather['rain_chance']}% chance of rain (expected {timing}) — pack an umbrella"
        else:
            rain_warning = f"\n  ☂️ {weather['rain_chance']}% chance of rain — pack an umbrella"

    return f"🌤️ *Weather*\n  {suggestion}{rain_warning}"


if __name__ == "__main__":
    print("Fetching Irvine weather...")
    result = get_weather_briefing()
    print(result or "Failed to fetch weather")
