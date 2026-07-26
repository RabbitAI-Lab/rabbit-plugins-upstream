---
display_name: China Hotel Booking
description: Search hotels across China with real-time pricing, ratings and Trip.com booking links. Also supports flights, attractions, itinerary planning and travel tips for inbound tourists.
tools:
  - bash
env:
  - PROXY_URL
  - PROXY_TOKEN
---

# China Hotel Booking

## Description

Your all-in-one travel companion for visiting China. This skill provides 5 powerful features for international tourists:

1. **Hotel Search** — Find hotels with real-time pricing, ratings and booking links
2. **Flight Search** — Search flights to/from/within China with live prices
3. **Attraction Tickets** — Discover attractions with ticket prices and opening hours
4. **Itinerary Planner** — Generate personalized multi-day travel plans
5. **Travel Tips** — Get answers about visa, payment, transport, food and more

## Data Flow & Privacy

User queries are sent to a secure proxy server (SCF) which injects authentication tokens and forwards requests to TripGenie API. The proxy handles affiliate link generation automatically. No user personal data is stored or logged. All communication is HTTPS encrypted.

## When to Use

- Find and book hotels in any Chinese city
- Search hotels by budget, location, dates or preferences

Keywords: China hotel, hotel in Beijing, Shanghai accommodation, stay in China, book hotel, budget hotel, luxury hotel

## Execution

### Step 1: Identify parameters from user request

| Parameter | Description | Example |
|-----------|-------------|---------|
| city | City name in English (required) | "Beijing" |
| check_in | Check-in date YYYY-MM-DD (optional) | "2026-08-01" |
| check_out | Check-out date YYYY-MM-DD (optional) | "2026-08-05" |
| guests | Number of guests (optional, default: 2) | 2 |
| budget | Budget level or amount (optional) | "under $100/night" |
| preferences | Additional preferences (optional) | "near Forbidden City" |

### Step 2: Run the script

```bash
python scripts/china_travel.py hotel "<city>" "[check_in]" "[check_out]" [guests] "[budget]" "[preferences]" [--locale=xx]
```

Optional: Add `--locale=ja/ko/ru/zh` at the end for localized results (default: en).

### Step 3: Present results

The API returns structured Markdown with hotel names, prices, ratings, key features, and direct booking links. Present the content directly to the user.

## Examples

**User:** "Find hotels in Shanghai near the Bund for 2 adults"
```bash
python scripts/china_travel.py hotel "Shanghai" "" "" 2 "" "near the Bund"
```

**User:** "Budget hotels in Beijing from July 10-12"
```bash
python scripts/china_travel.py hotel "Beijing" "2026-07-10" "2026-07-12" 2 "under $80/night"
```

## Other Features Available

This skill also supports:
- `flight` — Search flights to/from/within China
- `attraction` — Find attractions and ticket prices
- `itinerary` — Generate multi-day travel plans
- `tips` — Travel advice, visa, payment, transport tips

## Notes

- City names should be in English for best results
- Dates are optional but help narrow down availability and pricing
- Booking links go directly to Trip.com (international version)
