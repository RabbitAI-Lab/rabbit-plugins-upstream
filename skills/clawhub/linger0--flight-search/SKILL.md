---
name: flight-search
version: 1.0.0
description: Search one-way flight options by departure city, destination city, and date using Ctrip mobile results, then sort by price ascending. Use when the user wants a quick flight lookup like "查一下上海到北京 2026-04-01 的机票", or asks for results that include flight number, departure/arrival time, price, and whether the itinerary has a transfer.
---

# Flight Search

Use the bundled CLI to fetch and normalize Ctrip mobile flight results.

## Workflow

1. Normalize the user's departure city, destination city, and date.
2. Run `scripts/search_ctrip_flights.py`.
3. Return the cheapest options first.
4. For each result, include at minimum:
   - flight number
   - departure time
   - arrival time
   - price
   - whether it is direct or has a transfer

## Command

```bash
python3 skills/flight-search/scripts/search_ctrip_flights.py 上海 北京 2026-04-01
```

Useful flags:

```bash
python3 skills/flight-search/scripts/search_ctrip_flights.py SHA BJS 2026-04-01 --format json
python3 skills/flight-search/scripts/search_ctrip_flights.py 上海 北京 2026-04-01 --limit 10
```

## Input Rules

- Accept either Chinese city names or 3-letter city/airport codes.
- Expect dates in `YYYY-MM-DD` format.
- Treat this as one-way search only unless the skill is explicitly extended.
- If the requested date is in the past, stop and tell the user.

## Output Rules

- Sort results by price from low to high.
- Prefer concise Chinese output that reads cleanly in Telegram.
- Format each option as two short lines: flight number, then time + price + transfer status.
- Show at least 5 options when available.
- After the first 5, stop when the fare exceeds 1.5x of the cheapest shown fare, or exceeds 1000 yuan.
- Mark transfer status as `直飞` or `转机N次`.
- If the script returns zero results, say that no flights were found for that route and date.
- Never invent missing prices or schedules.

## Resources

- `scripts/search_ctrip_flights.py`: fetch and format flight results.
- `references/city_codes.json`: Chinese city-name to airport/city-code mapping.
