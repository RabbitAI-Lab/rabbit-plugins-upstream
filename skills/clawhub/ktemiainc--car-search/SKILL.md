---
name: car-search
description: Search and compare rental cars with the Ktemia car search API and return each seller's price with a booking link. Use when the user asks to hire, rent, or compare a car at a city or airport on specific dates, including narrowing to one rental agency or booking site. Asks for missing details instead of guessing.
version: 1.0.1
allowed-tools: Bash(python3 scripts/ktemia.py:*)
metadata:
  openclaw:
    emoji: "🚗"
    homepage: https://www.ktemia.com/docs/api/cars/search/
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

# Car search with the Ktemia API

Ktemia compares rental cars and returns each seller's booking link. It does not reserve the car: the traveller books on the seller's site.

API reference: https://www.ktemia.com/docs/api/cars/search/

## Before you call anything

1. You need `KTEMIA_API_KEY` in the environment. If it is missing, tell the user to create a key (https://www.ktemia.com/docs/api/#authentication) and export it. Never print the key or put it in code you write for a browser.
2. You need a pickup place, a pickup date, and a drop-off date. Drop-off defaults to the same place. Times default to 12:00.
3. **Do not guess.** If a place, date, or time is missing or vague ("next week", "somewhere"), ask. Every API call counts against the user's monthly quota, so a guessed search wastes it.
4. Dates are `YYYY-MM-DD` and must be today or later. Times are `HH:MM`. Resolve "next Friday" into a date and confirm it with the user if there is any doubt.

## Workflow

Use the bundled script `scripts/ktemia.py` in this skill's directory. It needs only Python 3, no packages. Every command prints JSON.

### 1. Turn a place name into a location id

`pickupLocation` is a `locationId`, not a city name or an airport code.

```bash
python3 scripts/ktemia.py locations "Lisbon"
python3 scripts/ktemia.py locations "LIS" --type airport
```

`--type` is `city` (default), `airport`, or `all`.

- Send `locationId` as `--pickup`. Use a second id as `--dropoff` only when the traveller returns the car somewhere else.
- If several places match, **ask which one**. Do not take the first match.

### 2. Start the search

```bash
python3 scripts/ktemia.py search --pickup 29230 --pickup-date 2027-03-10 --dropoff-date 2027-03-17
python3 scripts/ktemia.py search --pickup 29230 --dropoff 174457 --pickup-date 2027-03-10 --dropoff-date 2027-03-17 --pickup-time 09:00 --dropoff-time 18:00 --transmission automatic --sort price --sort-order asc
```

Other options: `--driver-age 30` (18–99; send it only when the user gave an age), `--class small|medium|large|suv|van|pickup|luxury|convertible`, `--max-price N` (whole number in the country's currency), `--price-mode total|perDay` (default `total`, the price for the whole hire), `--country GB`.

`--providers` and `--agencies` narrow a search to named sellers. Both need ids from a previous results page, so they belong on a **second** search — see "Filter by seller or agency" below. Do not guess the ids.

`country` picks the market. Prices come back in that country's native currency: GB is GBP, DE is EUR, US is USD. Omit it for the US. Do not send a currency field.

`sort` is `bestValue` (default), `price`, `rating`, or `distance`. `--sort-order` changes `price` only: `asc` is cheapest first, `desc` is dearest first. Rating is always highest first. Distance is always nearest first.

The search returns a `searchToken`, valid for 60 minutes. It does not return cars. A search usually answers in several seconds.

### 3. Read results

```bash
python3 scripts/ktemia.py results <searchToken>
```

Up to 20 cars per page. Show the user a short list: car, class, passengers, agency, and price. `price` is the hire total. `perDay` is the daily price. If `nextToken` is present and the user wants more, call `results <nextToken>`.

The summary also lists `bookingSites` and `agencies`: the sellers and rental companies in this search, each with a count. Those ids are what `--providers` and `--agencies` take.

### 4. Filter by seller or agency

When the user wants one company ("only Avis", "book through Expedia, not the agency"), read the ids off a results page and start a **new** search with them. A filter cannot be applied to an existing token.

```bash
python3 scripts/ktemia.py search --pickup 22863 --pickup-date 2027-03-10 --dropoff-date 2027-03-17 --agencies avis,hertz
python3 scripts/ktemia.py search --pickup 22863 --pickup-date 2027-03-10 --dropoff-date 2027-03-17 --providers "Booking.com,Expedia"
```

- `--agencies` is the company whose car it is. Ids are lowercase: `avis`, `hertz`, `enterprise`, `budget`, `alamo`, `dollar`, `europcar`, `fox`.
- `--providers` is the site selling it. Ids are display names with capitals and dots: `Booking.com`, `Expedia`, `Avis`, `Auto Europe`, `DiscoverCars.com`.
- Take both from `bookingSites` and `agencies` on a results page, exactly as written — matching is case-sensitive. Separate with commas only, so an id containing a space is fine: `--providers "Auto Europe,Car Rental 8"`.
- Up to 10 each. An id with `,`, `;`, or `=` in it is rejected.
- Which sellers appear changes by city and date, so **read the ids rather than hard-coding them**. Tell the user this is a second search against their quota, and ask first.

Both filters can be sent together. Narrowing can return nothing, which is a real `NO_RESULTS` — report it instead of retrying.

### 5. Booking links for one car

```bash
python3 scripts/ktemia.py details <searchToken> <car id>
```

Each option includes `providerUrl`, the seller's booking page. Give the user the link as returned; do not edit the query string. A null URL means that seller did not resolve. Make clear they book on the seller's site, and that prices can change after the search.

## Errors

The script prints the API error and exits non-zero. Common codes:

- `MISSING_FIELD` / `INVALID_REQUEST`: ask the user for the field in `param`, or fix the value.
- `DATE_IN_PAST`: ask for a future date.
- `NO_RESULTS` (404): nothing published for that place and those dates. Suggest nearby dates or a different desk, and ask before searching again.
- `SEARCH_EXPIRED` (410): the 60-minute token is gone. Start a new search.
- `MISSING_API_KEY` / `INVALID_API_KEY` (401): the key is missing or wrong.
- `QUOTA_EXCEEDED` / `RATE_LIMIT_EXCEEDED` (429): stop and tell the user. Do not retry in a loop.
- `LOCATIONS_UNAVAILABLE` / `SEARCH_FAILED` / `DETAILS_FAILED` (502): temporary. Retry the same request once.

Full list: https://www.ktemia.com/docs/api/#errors

## Without Python

```bash
curl "https://api.ktemia.com/cars/locations?query=Lisbon" -H "X-API-Key: $KTEMIA_API_KEY"

curl https://api.ktemia.com/cars/search \
  -H "X-API-Key: $KTEMIA_API_KEY" -H "Content-Type: application/json" \
  -d '{"pickupLocation": "29230", "pickupDate": "2027-03-10", "dropoffDate": "2027-03-17"}'

curl https://api.ktemia.com/cars/search \
  -H "X-API-Key: $KTEMIA_API_KEY" -H "Content-Type: application/json" \
  -d '{"pickupLocation": "29230", "pickupDate": "2027-03-10", "dropoffDate": "2027-03-17", "agencies": ["avis"], "providers": ["Booking.com"]}'

curl "https://api.ktemia.com/cars/results?token=$TOKEN" -H "X-API-Key: $KTEMIA_API_KEY"
curl "https://api.ktemia.com/cars/details?token=$TOKEN&resultId=$ID" -H "X-API-Key: $KTEMIA_API_KEY"
```

## Security

- The API key is read from `KTEMIA_API_KEY` and sent only as the `X-API-Key` header, over HTTPS, to `https://api.ktemia.com`.
- `scripts/ktemia.py` refuses any `KTEMIA_API_URL` that is not `https://` on `ktemia.com`, and never follows redirects, so the key cannot reach another host.
- The script uses the Python standard library only. It reads no files and writes nothing to disk.

## Further reading

Background for the user. You do not need these to run a search, so don't open them unless the user asks.

- [Car rental API: compare vehicles and prices for a pickup](https://www.ktemia.com/blog/car-rental-api/)
- [Car rental aggregator API: search multiple providers in one call](https://www.ktemia.com/blog/car-rental-aggregator-api/)
- [How to compare car rental deals across providers and locations](https://www.ktemia.com/blog/compare-car-rental-deals/)
