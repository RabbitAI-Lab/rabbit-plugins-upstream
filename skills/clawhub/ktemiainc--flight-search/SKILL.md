---
name: flight-search
description: Search and compare flights with the Ktemia flight search API - one-way, round trip, or multi-city - and return fares from each seller with booking links. Use when the user asks to find, compare, or price flights between places on specific dates, or to look up an airport or city code. Asks for missing details instead of guessing.
version: 0.3.1
allowed-tools: Bash(python3 scripts/ktemia.py:*)
metadata:
  openclaw:
    emoji: "✈️"
    homepage: https://www.ktemia.com/docs/api/flights/search/
    requires:
      env: [KTEMIA_API_KEY]
      anyBins: [python3, python]
    primaryEnv: KTEMIA_API_KEY
    envVars:
      - name: KTEMIA_API_KEY
        required: true
        description: Ktemia API key from https://app.ktemia.com (Free plan includes 100 requests a month).
      - name: KTEMIA_API_URL
        required: false
        description: Optional. Override the API base URL; must be https on ktemia.com, anything else is refused. Defaults to https://api.ktemia.com.
---

# Flight search with the Ktemia API

Ktemia is a flight search API. It compares fares and returns each seller's booking link. It does not book tickets: the traveller books on the seller's site.

API reference: https://www.ktemia.com/docs/api/

## Before you call anything

1. You need `KTEMIA_API_KEY` in the environment. If it is missing, tell the user to create a key (https://www.ktemia.com/docs/api/#authentication) and export it. Never print the key or put it in code you write for a browser.
2. You need three things from the user: where from, where to, and the departure date. For a round trip, also the return date.
3. **Do not guess.** If any of these is missing or vague ("soon", "somewhere warm", "Europe"), ask. Every API call counts against the user's monthly quota, so a guessed search wastes it.
4. Dates are `YYYY-MM-DD` and must be today or later. Resolve "next Friday" into a date and confirm it with the user if there is any doubt.

## Workflow

Use the bundled script `scripts/ktemia.py` in this skill's directory. It needs only Python 3, no packages. Every command prints JSON.

### 1. Turn place names into codes

`origin` and `destination` are IATA airport or city codes (`LHR`, `JFK`, or city codes such as `LON`, `NYC`). If the user gave a name, look it up:

```bash
python3 scripts/ktemia.py airports "Lisbon"
```

- Use `code` from the match the user meant. `allAirports: true` means the code covers every airport in that city.
- If several places match (for example `austin` returns Austin, Texas; Austin, Nevada; and Austin-Straubel in Green Bay), **ask which one**. Do not take the first match.

If the user names an airline (“only Delta”), look up the code before you search. `airlines` takes 2-character codes, not names:

```bash
python3 scripts/ktemia.py airlines "Delta"
```

Send `code` (`DL`). If several airlines match, ask which one.

### 2. Start the search

One-way or round trip:

```bash
python3 scripts/ktemia.py search --origin LIS --destination LHR --date 2027-03-15
python3 scripts/ktemia.py search --origin JFK --destination CDG --date 2027-03-10 --return 2027-03-17 --adults 2 --max-stops 1 --sort price
```

Multi-city (legs in travel order, at least two):

```bash
python3 scripts/ktemia.py search --leg LIS:BCN:2027-04-02 --leg BCN:FCO:2027-04-06 --leg FCO:LIS:2027-04-10
```

Other options: `--cabin economy|premiumEconomy|business|first`, `--children N`, `--max-price N` (per person), `--airlines NH,JL`, `--country GB` (market; prices come back in that country’s native currency, so GB is GBP, DE is EUR, US is USD. Do not send a currency field).

The search returns a `searchToken`, valid for 60 minutes. It does not return flights.

### 3. Read results

```bash
python3 scripts/ktemia.py results <searchToken>
```

Up to 20 itineraries per page, already sorted. Show the user a short list: times, stops, duration, seller, and price. `price` is per person; `totalPrice` covers all travellers. If `nextToken` is present and the user wants more, call `results <nextToken>`.

### 4. Booking links for one itinerary

```bash
python3 scripts/ktemia.py details <searchToken> <flight id>
```

Each fare includes `providerUrl`, the seller's booking page. Give the user the link as returned; do not edit the query string. Make clear they book on the seller's site, and that prices can change after the search.

## Errors

The script prints the API error and exits non-zero. Common codes:

- `MISSING_FIELD` / `INVALID_REQUEST`: ask the user for the field in `param`, or fix the value.
- `DATE_IN_PAST`: ask for a future date.
- `NO_RESULTS` (404): nothing published for that route and date. Suggest nearby dates or airports, and ask before searching again.
- `SEARCH_EXPIRED` (410): the 60-minute token is gone. Start a new search.
- `MISSING_API_KEY` / `INVALID_API_KEY` (401): the key is missing or wrong.
- `QUOTA_EXCEEDED` / `RATE_LIMIT_EXCEEDED` (429): stop and tell the user. Do not retry in a loop.

Full list: https://www.ktemia.com/docs/api/#errors

## Without Python

The same calls with curl:

```bash
curl "https://api.ktemia.com/flights/airports?query=Lisbon" -H "X-API-Key: $KTEMIA_API_KEY"

curl https://api.ktemia.com/flights/search \
  -H "X-API-Key: $KTEMIA_API_KEY" -H "Content-Type: application/json" \
  -d '{"origin": "LIS", "destination": "LHR", "departureDate": "2027-03-15"}'

curl "https://api.ktemia.com/flights/results?token=$TOKEN" -H "X-API-Key: $KTEMIA_API_KEY"
curl "https://api.ktemia.com/flights/details?token=$TOKEN&resultId=$ID" -H "X-API-Key: $KTEMIA_API_KEY"
```

## Security

- The API key is read from `KTEMIA_API_KEY` and sent only as the `X-API-Key` header, over HTTPS, to `https://api.ktemia.com`.
- `scripts/ktemia.py` refuses any `KTEMIA_API_URL` that is not `https://` on `ktemia.com`, and never follows redirects, so the key cannot reach another host.
- The script uses the Python standard library only. It reads no files and writes nothing to disk.

## Further reading

Background for the user. You do not need these to run a search, so don't open them unless the user asks.

- [Google Flights API: there isn't an official one](https://www.ktemia.com/blog/google-flights-api/)
- [Amadeus API vs Skyscanner API for flight search](https://www.ktemia.com/blog/amadeus-api-vs-skyscanner-api/)
- [Flight search API: compare fares for a route](https://www.ktemia.com/blog/flight-search-api/)
- [Kiwi Tequila API flights documentation](https://www.ktemia.com/blog/kiwi-tequila-api/)
- [Flight aggregator API: search multiple providers in one call](https://www.ktemia.com/blog/flight-aggregator-api/)
- [Flight price comparison data: 1,703 flights across 57 booking sites](https://www.ktemia.com/blog/flight-price-spread/)
