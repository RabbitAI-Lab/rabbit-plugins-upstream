---
name: hotel-search
description: Search and compare hotels with the Ktemia hotel API and return each seller's price, a booking link, and guest reviews. Use when the user asks to find, compare, or price a stay in a city on specific dates, to narrow prices to one booking site, or to read reviews of a hotel. Asks for missing details instead of guessing.
version: 0.3.1
allowed-tools: Bash(python3 scripts/ktemia.py:*)
metadata:
  openclaw:
    emoji: "🏨"
    homepage: https://www.ktemia.com/docs/api/hotels/search/
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

# Hotel search with the Ktemia API

Ktemia compares stays and returns each seller's booking link, plus guest reviews. It does not reserve the room: the traveller books on the seller's site.

API reference: https://www.ktemia.com/docs/api/hotels/search/

## Before you call anything

1. You need `KTEMIA_API_KEY` in the environment. If it is missing, tell the user to create a key (https://www.ktemia.com/docs/api/#authentication) and export it. Never print the key or put it in code you write for a browser.
2. You need a place, a check-in date, and a check-out date. Adults default to 2 and rooms default to 1.
3. **Do not guess.** If the place or either date is missing or vague ("sometime in spring", "a nice hotel"), ask. Every API call counts against the user's monthly quota, so a guessed search wastes it.
4. Dates are `YYYY-MM-DD`, check-in is today or later, and the stay is 1 to 30 nights. Resolve "next Friday" into a date and confirm it with the user if there is any doubt.

## Workflow

Use the bundled script `scripts/ktemia.py` in this skill's directory. It needs only Python 3, no packages. Every command prints JSON.

### 1. Turn a place name into a location id

`location` on a search is a `locationId`, not a city name.

```bash
python3 scripts/ktemia.py locations "London"
```

- Send `locations[].locationId` as `--location`. A neighbourhood and an airport in the same city have their own ids.
- A row with `locationType: hotel` is one property. Its `locationId` is still the city, so a search for that id returns the city. Its `hotelId` is only for reviews.
- If several places match (London, England and London, Ontario), **ask which one**. Do not take the first match.

### 2. Start the search

```bash
python3 scripts/ktemia.py search --location 29230 --checkin 2027-03-10 --checkout 2027-03-12
python3 scripts/ktemia.py search --location 29230 --checkin 2027-03-10 --checkout 2027-03-12 --adults 2 --rooms 1 --min-stars 4 --sort price --sort-order asc
```

Other options: `--child-ages 4,7` (one age per child, 0–17, at most 8; send it only when the user named children), `--min-rating 6|7|8|9`, `--max-price N` (before-tax stay price, whole number), `--free-cancellation`, `--amenities pool` (ids from `availableFilters` on a previous results page), `--country GB`.

`--providers` narrows a search to named booking sites. It needs ids from a previous results page, so it belongs on a **second** search — see "Filter by booking site" below. Do not guess the ids.

`country` picks the market. Prices come back in that country's native currency: GB is GBP, DE is EUR, US is USD. Omit it for the US. Do not send a currency field.

`sort` is `bestValue` (default), `price`, `rating`, `stars`, or `distance`. `--sort-order` changes `price` and `stars` only. `asc` is cheapest, or fewest stars, first. Rating is always highest first. Distance is always nearest first.

The search returns a `searchToken`, valid for 60 minutes. It does not return hotels. A city search usually answers in 8–16 seconds while it settles.

### 3. Read results

```bash
python3 scripts/ktemia.py results <searchToken>
```

Up to 30 hotels per page. The first page is often a few short of 30. Show a short list: name, stars, guest score, neighbourhood, and price. `price` is the stay before taxes, which is what a price sort uses. `total` includes taxes. If `nextToken` is present and the user wants more, call `results <nextToken>`.

`availableFilters` on the full response (`--raw`) lists amenity ids you can send on a new search. Ask the user before starting that second search.

The summary also lists `bookingSites`: the sites selling stays in this search, each with a count. Those ids are what `--providers` takes.

### 4. Filter by booking site

When the user wants one site ("only Booking.com", "compare Expedia and Agoda"), read the ids off a results page and start a **new** search with them. A filter cannot be applied to an existing token.

```bash
python3 scripts/ktemia.py search --location 29230 --checkin 2027-03-10 --checkout 2027-03-12 --providers "Booking.com"
python3 scripts/ktemia.py search --location 29230 --checkin 2027-03-10 --checkout 2027-03-12 --providers "Booking.com,Expedia"
```

- Ids are display names with capitals and dots: `Booking.com`, `Expedia`, `Hotels.com`, `Priceline`, `Agoda.com`, `Trip.com`, `Super.com`, `HomeToGo`.
- Take them from `bookingSites` on a results page, exactly as written — matching is case-sensitive, unlike `--amenities` which is lowercased. Separate with commas only, so an id containing a space is fine.
- Up to 10. An id with `,`, `;`, or `=` in it is rejected.
- Which sites appear changes by city and date, so **read the ids rather than hard-coding them**. Tell the user this is a second search against their quota, and ask first.

With two or more sites, `bestOption` on each hotel is the cheapest among them, and `details` lists only those sites. `availableFilters.bookingSites` still lists every site in the search, so the user can switch with another search. Narrowing can return nothing, which is a real `NO_RESULTS` — report it instead of retrying.

### 5. Booking links for one hotel

```bash
python3 scripts/ktemia.py details <searchToken> <hotel id>
```

Each option includes `providerUrl`, the seller's booking page. Give the user the link as returned; do not edit the query string. A null URL means that seller did not resolve. `reviews` on this call is up to five recent guest reviews. Make clear they book on the seller's site, and that prices can change after the search.

### 6. More reviews

Reviews need the hotel id and no search token. The id is `id` from results, or `hotelId` from a location whose type is `hotel`.

```bash
python3 scripts/ktemia.py reviews 1072956080
python3 scripts/ktemia.py reviews 1072956080 --sort highestScore --travelers couples --months 10,11 --sources booking --page 2
```

Ten reviews per page. `sort` is `recent` (default), `oldest`, `highestScore`, or `lowestScore`. `--travelers` is a comma-separated list of `families`, `couples`, `solo`, `friends`, `business`. `--months` is month numbers, `1` through `12`. `--sources` is `booking`, `agoda`, `priceline`, or a mix. Scores are 0–10.

## Errors

The script prints the API error and exits non-zero. Common codes:

- `MISSING_FIELD` / `INVALID_REQUEST`: ask the user for the field in `param`, or fix the value. Sending `currency` is rejected.
- `DATE_IN_PAST`: ask for a future check-in. The error names `checkin` or `checkout`.
- `STAY_TOO_LONG`: the stay is over 30 nights. Ask for a shorter stay.
- `NO_RESULTS` (404): nothing published for that place and those dates. No token is returned.
- `NO_MORE_RESULTS` (404): that results page is past the end.
- `SEARCH_EXPIRED` (410): the 60-minute token is gone. Start a new search. Reviews do not use the token and keep working.
- `INVALID_HOTEL_ID`: the reviews id must be digits.
- `MISSING_API_KEY` / `INVALID_API_KEY` (401): the key is missing or wrong.
- `QUOTA_EXCEEDED` / `RATE_LIMIT_EXCEEDED` (429): stop and tell the user. Do not retry in a loop.
- `LOCATIONS_UNAVAILABLE` / `SEARCH_FAILED` / `DETAILS_FAILED` / `REVIEWS_UNAVAILABLE` (502): temporary. Retry the same request once.

An unknown hotel id on reviews returns 200 with `totalReviews: 0`. Full list: https://www.ktemia.com/docs/api/#errors

## Without Python

```bash
curl "https://api.ktemia.com/hotels/locations?query=London" -H "X-API-Key: $KTEMIA_API_KEY"

curl https://api.ktemia.com/hotels/search \
  -H "X-API-Key: $KTEMIA_API_KEY" -H "Content-Type: application/json" \
  -d '{"location": "29230", "checkin": "2027-03-10", "checkout": "2027-03-12"}'

curl https://api.ktemia.com/hotels/search \
  -H "X-API-Key: $KTEMIA_API_KEY" -H "Content-Type: application/json" \
  -d '{"location": "29230", "checkin": "2027-03-10", "checkout": "2027-03-12", "providers": ["Booking.com"]}'

curl "https://api.ktemia.com/hotels/results?token=$TOKEN" -H "X-API-Key: $KTEMIA_API_KEY"
curl "https://api.ktemia.com/hotels/details?token=$TOKEN&resultId=$ID" -H "X-API-Key: $KTEMIA_API_KEY"
curl "https://api.ktemia.com/hotels/reviews?hotelId=$ID" -H "X-API-Key: $KTEMIA_API_KEY"
```

## Security

- The API key is read from `KTEMIA_API_KEY` and sent only as the `X-API-Key` header, over HTTPS, to `https://api.ktemia.com`.
- `scripts/ktemia.py` refuses any `KTEMIA_API_URL` that is not `https://` on `ktemia.com`, and never follows redirects, so the key cannot reach another host.
- The script uses the Python standard library only. It reads no files and writes nothing to disk.

## Further reading

Background for the user. You do not need these to run a search, so don't open them unless the user asks.

- [Booking.com API: search is not the reservation](https://www.ktemia.com/blog/booking-com-api/)
- [Expedia API alternative: compare without the partner gate](https://www.ktemia.com/blog/expedia-api-alternative/)
- [Hotel price API: every booking site in one call](https://www.ktemia.com/blog/hotel-price-api/)
