---
display_name: China Travel Planner
description: Generate personalized multi-day itineraries for China with hotels, attractions, dining and tips. Also supports hotel search, flights, attraction tickets and travel Q&A for inbound tourists.
tools:
  - bash
env:
  - PROXY_URL
  - PROXY_TOKEN
---

# China Travel Planner

## Description

Your all-in-one travel companion for visiting China. This skill provides 5 powerful features for international tourists:

1. **Itinerary Planner** — Generate personalized multi-day travel plans with AI
2. **Hotel Search** — Find hotels with real-time pricing, ratings and booking links
3. **Flight Search** — Search flights to/from/within China with live prices
4. **Attraction Tickets** — Discover attractions with ticket prices and opening hours
5. **Travel Tips** — Get answers about visa, payment, transport, food and more

## Data Flow & Privacy

User queries are sent to a secure proxy server (SCF) which injects authentication tokens and forwards requests to TripGenie API. The proxy handles affiliate link generation automatically. No user personal data is stored or logged. All communication is HTTPS encrypted.

## When to Use

- Plan a multi-day trip to a Chinese city
- Get a complete itinerary with hotels, attractions, and dining
- Customize a trip plan based on interests or budget

Keywords: China itinerary, plan trip to China, 3 days in Beijing, Shanghai travel plan, Chengdu trip, travel planner, day by day

## Execution

### Step 1: Identify parameters from user request

| Parameter | Description | Example |
|-----------|-------------|---------|
| city | City name in English (required) | "Chengdu" |
| days | Number of days (required) | 3 |
| travelers | Number of travelers (optional, default: 2) | 2 |
| interests | Travel interests (optional) | "pandas and food" |
| budget | Budget level (optional) | "mid-range" |

### Step 2: Run the script

```bash
python scripts/china_travel.py itinerary "<city>" <days> [travelers] "[interests]" "[budget]" [--locale=xx]
```

Optional: Add `--locale=ja/ko/ru/zh` at the end for localized results (default: en).

### Step 3: Present results

The API returns a structured day-by-day itinerary in Markdown with time slots, activity descriptions, hotel recommendations, restaurant suggestions, and direct booking links. Present the content directly to the user.

## Examples

**User:** "Plan a 3-day trip to Beijing for 2 people"
```bash
python scripts/china_travel.py itinerary "Beijing" 3
```

**User:** "5-day Chengdu itinerary focused on pandas and spicy food, mid-range budget"
```bash
python scripts/china_travel.py itinerary "Chengdu" 5 2 "pandas and spicy food" "mid-range"
```

## Other Features Available

This skill also supports:
- `hotel` — Search and book hotels across China
- `flight` — Search flights to/from/within China
- `attraction` — Find attractions and ticket prices
- `tips` — Travel advice, visa, payment, transport tips

## Notes

- City names should be in English for best results
- Budget levels: "budget", "mid-range", "luxury"
- Booking links go directly to Trip.com (international version)
