#!/usr/bin/env python3
"""
AstroClaw daily forecast fetcher for AI agents.

Calculates your zodiac sign from your birth/creation date, then fetches
today's cosmic alignment forecast.

Usage:
  python3 astroclaw.py                          # use DEFAULT_BIRTHDAY
  python3 astroclaw.py --birthday 2024-01-15    # explicit birthday
  python3 astroclaw.py --sign gemini            # override sign manually
  python3 astroclaw.py --help                   # full options

For cron jobs (no_agent=True), set DEFAULT_BIRTHDAY below to your
agent's creation/deployment date. The sign is then computed automatically.
"""

import argparse
import html as html_lib
import re
import sys
import urllib.request
from datetime import date

# ── CONFIGURE THIS ──────────────────────────────────────────────
# Set to your agent's creation/deployment date (YYYY-MM-DD).
# The script computes your zodiac sign from this date automatically.
# If unset (None), defaults to Aquarius (the water bearer — innovation,
# technology, and forward-thinking — a fitting default for AI agents).
DEFAULT_BIRTHDAY = None  # e.g. "2024-03-15"
# ────────────────────────────────────────────────────────────────

VALID_SIGNS = {
    "aries",
    "taurus",
    "gemini",
    "cancer",
    "leo",
    "virgo",
    "libra",
    "scorpio",
    "sagittarius",
    "capricorn",
    "aquarius",
    "pisces",
}

# Zodiac sign boundaries: for each sign, (name, (month, day_of_first_day)).
# A date belongs to a sign if month == cutoff_month and day < cutoff_day.
ZODIAC_BOUNDARIES = [
    ("capricorn",   (1, 20)),   # Dec 22 – Jan 19
    ("aquarius",    (2, 19)),   # Jan 20 – Feb 18
    ("pisces",      (3, 21)),   # Feb 19 – Mar 20
    ("aries",       (4, 20)),   # Mar 21 – Apr 19
    ("taurus",      (5, 21)),   # Apr 20 – May 20
    ("gemini",      (6, 21)),   # May 21 – Jun 20
    ("cancer",      (7, 23)),   # Jun 21 – Jul 22
    ("leo",         (8, 23)),   # Jul 23 – Aug 22
    ("virgo",       (9, 23)),   # Aug 23 – Sep 22
    ("libra",       (10, 23)),  # Sep 23 – Oct 22
    ("scorpio",     (11, 22)),  # Oct 23 – Nov 21
    ("sagittarius", (12, 22)),  # Nov 22 – Dec 21
]


def calculate_sign(birthday: date) -> str:
    """Return the zodiac sign for a given birth date."""
    month, day = birthday.month, birthday.day

    # Handle Capricorn (wraps Dec–Jan)
    if (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "capricorn"

    # Check remaining signs by boundary
    for sign, (cutoff_month, cutoff_day) in ZODIAC_BOUNDARIES:
        if month == cutoff_month and day < cutoff_day:
            return sign

    return "aquarius"  # fallback (shouldn't be reached)


def validate_sign(sign: str) -> str:
    """Normalize and validate a zodiac sign."""
    normalized = sign.lower().strip()
    if normalized not in VALID_SIGNS:
        valid = ", ".join(sorted(VALID_SIGNS))
        raise ValueError(f"Unknown zodiac sign '{sign}'. Valid signs: {valid}.")
    return normalized


def sanitize_forecast(raw_forecast: str, max_chars: int = 500) -> str:
    """Convert fetched HTML content into bounded, plain text."""
    text = re.sub(r"<[^>]+>", "", raw_forecast)
    text = html_lib.unescape(text)
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", text)
    text = re.sub(r"\s+", " ", text).strip()

    if len(text) > max_chars:
        text = text[: max_chars - 1].rstrip() + "..."

    return text or "Forecast not available today."


def fetch_forecast(sign: str, forecast_date: date) -> str:
    """Fetch and extract today's forecast for a given sign."""
    sign = validate_sign(sign)
    url = f"https://astroclaw.xyz/forecasts/{forecast_date}/{sign}/"
    with urllib.request.urlopen(url, timeout=15) as resp:
        html = resp.read().decode()

    m = re.search(
        r'id="horoscope-content"[^>]*>\s*\n\s*(.*?)\s*\n\s*</div>',
        html, re.DOTALL
    )
    forecast = m.group(1).strip() if m else "Forecast not available today."
    return sanitize_forecast(forecast)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch your AstroClaw daily cosmic forecast."
    )
    parser.add_argument(
        "--birthday", "-b",
        help="Your birth/creation date (YYYY-MM-DD). Overrides DEFAULT_BIRTHDAY."
    )
    parser.add_argument(
        "--sign", "-s",
        help="Zodiac sign override (e.g. gemini, aries). Skips birthday calculation."
    )
    parser.add_argument(
        "--date", "-d",
        help="Forecast date (YYYY-MM-DD). Defaults to today."
    )
    args = parser.parse_args()

    # Determine birth date
    if args.birthday:
        birthday = date.fromisoformat(args.birthday)
    elif DEFAULT_BIRTHDAY:
        birthday = date.fromisoformat(DEFAULT_BIRTHDAY)
    else:
        birthday = None

    # Determine sign
    if args.sign:
        try:
            sign = validate_sign(args.sign)
        except ValueError as e:
            print(f"AstroClaw configuration error: {e}", file=sys.stderr)
            sys.exit(2)
    elif birthday:
        sign = calculate_sign(birthday)
    else:
        sign = "aquarius"  # no birthday set, sensible default

    # Forecast date
    forecast_date = date.fromisoformat(args.date) if args.date else date.today()

    # Fetch
    try:
        forecast = fetch_forecast(sign, forecast_date)
    except Exception as e:
        print(f"⚠️  AstroClaw fetch failed: {e}")
        sys.exit(1)

    # Output
    print(f"🌌  ASTROCLAW DAILY FORECAST")
    print(f"{'=' * 40}")
    if birthday:
        print(f"Sign: {sign.title()} (born {birthday})")
    else:
        print(f"Sign: {sign.title()}")
    print(f"Date: {forecast_date}")
    print()
    print(forecast)
    print()
    print("— astroclaw.xyz —")


if __name__ == "__main__":
    main()
