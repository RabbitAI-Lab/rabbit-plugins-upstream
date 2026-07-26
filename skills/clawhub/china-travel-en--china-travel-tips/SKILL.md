---
display_name: China Travel Tips
description: Essential travel guide for visiting China — visa, mobile payment, transport, food, safety and more. Also supports hotel search, flights, attractions and itinerary planning for inbound tourists.
tools:
  - bash
env:
  - PROXY_URL
  - PROXY_TOKEN
---

# China Travel Tips

## Description

Your all-in-one travel companion for visiting China. This skill provides 5 powerful features for international tourists:

1. **Travel Tips** — Get answers about visa, payment, transport, food, safety and culture
2. **Hotel Search** — Find hotels with real-time pricing, ratings and booking links
3. **Flight Search** — Search flights to/from/within China with live prices
4. **Attraction Tickets** — Discover attractions with ticket prices and opening hours
5. **Itinerary Planner** — Generate personalized multi-day travel plans

## Data Flow & Privacy

User queries are sent to a secure proxy server (SCF) which injects authentication tokens and forwards requests to TripGenie API. The proxy handles affiliate link generation automatically. No user personal data is stored or logged. All communication is HTTPS encrypted.

## When to Use

- General questions about traveling in China
- How to set up payment apps (Alipay, WeChat Pay)
- Visa requirements and entry policies
- Transportation tips (trains, metro, taxis)
- Language and communication advice
- Food and dining culture
- Weather and packing tips
- Safety and emergency information
- Cultural etiquette and customs

Keywords: China travel tips, visiting China, China visa, Alipay setup, China transportation, Chinese food, travel advice, China safety, China customs

## Execution

### Step 1: Identify the user's question

Extract the travel question from the user's query.

### Step 2: Run the script

```bash
python scripts/china_travel.py tips "<question>" [--locale=xx]
```

Optional: Add `--locale=ja/ko/ru/zh` at the end for localized results (default: en).

### Step 3: Present results

The API returns detailed, practical answers in English tailored to the needs of foreign visitors to China. Present the content directly to the user.

## Examples

**User:** "How do I set up Alipay in China?"
```bash
python scripts/china_travel.py tips "How do I set up Alipay in China as a foreign tourist?"
```

**User:** "Do I need a visa to visit China?"
```bash
python scripts/china_travel.py tips "What are the visa requirements for visiting China?"
```

**User:** "Can I use credit cards in China?"
```bash
python scripts/china_travel.py tips "Can foreign tourists use credit cards in China? What payment methods are available?"
```

## Other Features Available

This skill also supports:
- `hotel` — Search and book hotels across China
- `flight` — Search flights to/from/within China
- `attraction` — Find attractions and ticket prices
- `itinerary` — Generate multi-day travel plans

## Notes

- All answers are in English and tailored to international tourists
- Information covers practical, up-to-date advice for visiting China
- Booking links go directly to Trip.com (international version)
