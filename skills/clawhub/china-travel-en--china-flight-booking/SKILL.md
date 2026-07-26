---
display_name: China Flight Booking
description: Search flights to China and domestic routes with real-time prices, schedules and Trip.com booking links. Also supports hotels, attractions, itinerary planning and travel tips for inbound tourists.
tools:
  - bash
env:
  - PROXY_URL
  - PROXY_TOKEN
---

# China Flight Booking

## Description

Your all-in-one travel companion for visiting China. This skill provides 5 powerful features for international tourists:

1. **Flight Search** — Search flights to/from/within China with live prices and schedules
2. **Hotel Search** — Find hotels with real-time pricing, ratings and booking links
3. **Attraction Tickets** — Discover attractions with ticket prices and opening hours
4. **Itinerary Planner** — Generate personalized multi-day travel plans
5. **Travel Tips** — Get answers about visa, payment, transport, food and more

## Data Flow & Privacy

User queries are sent to a secure proxy server (SCF) which injects authentication tokens and forwards requests to TripGenie API. The proxy handles affiliate link generation automatically. No user personal data is stored or logged. All communication is HTTPS encrypted.

## When to Use

- Find flights to a Chinese city from your home country
- Search domestic flights between Chinese cities
- Compare flight options by date, cabin class, or trip type

Keywords: flight to China, fly to Beijing, Shanghai flight, domestic flight China, China airfare, business class, economy

## Execution

### Step 1: Identify parameters from user request

| Parameter | Description | Example |
|-----------|-------------|---------|
| origin | Departure city/airport (required) | "London" |
| destination | Arrival city/airport (required) | "Beijing" |
| date | Travel date YYYY-MM-DD (required) | "2026-08-15" |
| trip_type | "one way" or "round trip" (optional) | "round trip" |
| cabin | Cabin class (optional, default: economy) | "business" |

### Step 2: Run the script

```bash
python scripts/china_travel.py flight "<origin>" "<destination>" "<date>" "[trip_type]" "[cabin]" [--locale=xx]
```

Optional: Add `--locale=ja/ko/ru/zh` at the end for localized results (default: en).

### Step 3: Present results

The API returns structured Markdown with airline names, flight numbers, departure/arrival times, prices, and direct booking links. Present the content directly to the user.

## Examples

**User:** "Find a flight from London to Beijing on August 15"
```bash
python scripts/china_travel.py flight "London" "Beijing" "2026-08-15"
```

**User:** "Round trip business class from New York to Shanghai"
```bash
python scripts/china_travel.py flight "New York" "Shanghai" "2026-09-01" "round trip" "business"
```

## Other Features Available

This skill also supports:
- `hotel` — Search and book hotels across China
- `attraction` — Find attractions and ticket prices
- `itinerary` — Generate multi-day travel plans
- `tips` — Travel advice, visa, payment, transport tips

## Notes

- City names and airport codes are both supported
- Booking links go directly to Trip.com (international version)
