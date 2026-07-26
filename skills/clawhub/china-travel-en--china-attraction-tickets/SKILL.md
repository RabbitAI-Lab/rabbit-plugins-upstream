---
display_name: China Attraction Tickets
description: Discover top attractions in China with ticket prices, opening hours and Trip.com booking links. Also supports hotels, flights, itinerary planning and travel tips for inbound tourists.
tools:
  - bash
env:
  - PROXY_URL
  - PROXY_TOKEN
---

# China Attraction Tickets

## Description

Your all-in-one travel companion for visiting China. This skill provides 5 powerful features for international tourists:

1. **Attraction Tickets** — Discover attractions with ticket prices, opening hours and booking links
2. **Hotel Search** — Find hotels with real-time pricing, ratings and booking links
3. **Flight Search** — Search flights to/from/within China with live prices
4. **Itinerary Planner** — Generate personalized multi-day travel plans
5. **Travel Tips** — Get answers about visa, payment, transport, food and more

## Data Flow & Privacy

User queries are sent to a secure proxy server (SCF) which injects authentication tokens and forwards requests to TripGenie API. The proxy handles affiliate link generation automatically. No user personal data is stored or logged. All communication is HTTPS encrypted.

## When to Use

- Find attractions and things to do in a Chinese city
- Get ticket prices and opening hours for specific attractions
- Discover activities based on interests (history, nature, food, etc.)

Keywords: China attractions, things to do in Beijing, Shanghai sightseeing, Great Wall tickets, Forbidden City, Terracotta Warriors, attractions, tickets, sightseeing

## Execution

### Step 1: Identify parameters from user request

| Parameter | Description | Example |
|-----------|-------------|---------|
| city | City name in English (required) | "Xi'an" |
| days | Number of days to spend (optional, default: 1) | 2 |
| interests | Interest keywords (optional) | "history and culture" |

### Step 2: Run the script

```bash
python scripts/china_travel.py attraction "<city>" [days] "[interests]" [--locale=xx]
```

Optional: Add `--locale=ja/ko/ru/zh` at the end for localized results (default: en).

### Step 3: Present results

The API returns structured Markdown with attraction names, ticket prices, opening hours, and direct booking links. Present the content directly to the user.

## Examples

**User:** "What can I visit in Xi'an?"
```bash
python scripts/china_travel.py attraction "Xi'an"
```

**User:** "2 days of history attractions in Beijing"
```bash
python scripts/china_travel.py attraction "Beijing" 2 "history"
```

## Other Features Available

This skill also supports:
- `hotel` — Search and book hotels across China
- `flight` — Search flights to/from/within China
- `itinerary` — Generate multi-day travel plans
- `tips` — Travel advice, visa, payment, transport tips

## Notes

- City names should be in English for best results
- Booking links go directly to Trip.com (international version)
