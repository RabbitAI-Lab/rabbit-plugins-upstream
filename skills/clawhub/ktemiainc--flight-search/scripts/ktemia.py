#!/usr/bin/env python3
"""Minimal client for the Ktemia flight search API. Standard library only.

    ktemia.py airports QUERY [--country CC]
    ktemia.py airlines QUERY [--country CC]
    ktemia.py search --origin LIS --destination LHR --date 2027-03-15 [options]
    ktemia.py search --leg LIS:BCN:2027-04-02 --leg BCN:FCO:2027-04-06
    ktemia.py results TOKEN
    ktemia.py details TOKEN RESULT_ID

Reads the API key from KTEMIA_API_KEY. Prints JSON. Exits 1 on an API error.
Reference: https://www.ktemia.com/docs/api/
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

DEFAULT_API = "https://api.ktemia.com"


def api_base():
    """Return the API base URL. The key is only ever sent over HTTPS to ktemia.com."""
    url = (os.environ.get("KTEMIA_API_URL") or DEFAULT_API).strip().rstrip("/")
    parts = urllib.parse.urlsplit(url)
    host = (parts.hostname or "").lower()
    trusted = host == "ktemia.com" or host.endswith(".ktemia.com")
    if parts.scheme != "https" or not trusted or parts.username or parts.password or parts.query or parts.fragment:
        sys.exit("KTEMIA_API_URL must be an https:// URL on ktemia.com. Unset it to use " + DEFAULT_API + ".")
    return url


class NoRedirect(urllib.request.HTTPRedirectHandler):
    """Never follow a redirect, so the X-API-Key header cannot be forwarded to another host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise urllib.error.HTTPError(req.full_url, code, "Redirect refused (the API key is only sent to the API host)", headers, fp)


API = api_base()
OPENER = urllib.request.build_opener(NoRedirect)


def call(method, path, params=None, body=None):
    key = os.environ.get("KTEMIA_API_KEY")
    if not key:
        sys.exit("KTEMIA_API_KEY is not set. Create a key: https://www.ktemia.com/docs/api/#authentication")
    url = API + path
    if params:
        url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={"X-API-Key": key})
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with OPENER.open(req, timeout=120) as res:
            return json.load(res)
    except urllib.error.HTTPError as err:
        try:
            error = json.load(err).get("error") or {}
        except (ValueError, AttributeError):
            error = {}
        print(json.dumps({"status": err.code, **error}, indent=2), file=sys.stderr)
        sys.exit(1)


def summarize_results(page):
    providers = page.get("providers") or {}
    flights = []
    for flight in page.get("flights", []):
        fare = (flight.get("bookingOptions") or [{}])[0]
        code = fare.get("providerCode")
        flights.append({
            "id": flight.get("id"),
            "legs": [
                {k: leg.get(k) for k in ("departure", "arrival", "duration", "stops")}
                for leg in flight.get("legs", [])
            ],
            "seller": (providers.get(code) or {}).get("name", code),
            "price": fare.get("formattedPrice"),
            "totalPrice": fare.get("formattedTotalPrice"),
            "sellers": flight.get("totalProviders"),
        })
    return {
        "page": page.get("page"),
        "totalResults": page.get("totalResults"),
        "nextToken": page.get("nextToken"),
        "flights": flights,
    }


def summarize_details(details):
    providers = details.get("providers") or {}
    return {
        "resultId": details.get("resultId"),
        "bookingOptions": [
            {
                "seller": (providers.get(o.get("providerCode")) or {}).get("name", o.get("providerCode")),
                "price": o.get("formattedPrice"),
                "totalPrice": o.get("formattedTotalPrice"),
                "providerUrl": o.get("providerUrl"),
            }
            for o in details.get("bookingOptions", [])
        ],
    }


def search_body(args):
    body = {}
    if args.leg:
        legs = []
        for leg in args.leg:
            origin, destination, date = leg.split(":", 2)
            legs.append({"origin": origin, "destination": destination, "date": date})
        body["legs"] = legs
    else:
        body.update(origin=args.origin, destination=args.destination, departureDate=args.date)
        if args.return_date:
            body["returnDate"] = args.return_date
    passengers = {k: v for k, v in (("adults", args.adults), ("children", args.children)) if v is not None}
    if passengers:
        body["passengers"] = passengers
    optional = {
        "cabin": args.cabin,
        "maxStops": args.max_stops,
        "maxPrice": args.max_price,
        "sortBy": args.sort,
        "country": args.country,
        "airlines": args.airlines.split(",") if args.airlines else None,
    }
    body.update({k: v for k, v in optional.items() if v is not None})
    return body


def main():
    parser = argparse.ArgumentParser(description="Ktemia flight search API client")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("airports", help="look up airport and city codes")
    p.add_argument("query")
    p.add_argument("--country")

    p = sub.add_parser("airlines", help="look up 2-character airline codes")
    p.add_argument("query")
    p.add_argument("--country")

    p = sub.add_parser("search", help="start a flight search; returns a searchToken")
    p.add_argument("--origin")
    p.add_argument("--destination")
    p.add_argument("--date", help="departure date, YYYY-MM-DD")
    p.add_argument("--return", dest="return_date", help="return date, YYYY-MM-DD")
    p.add_argument("--leg", action="append", help="multi-city leg ORIGIN:DESTINATION:YYYY-MM-DD, repeat in travel order")
    p.add_argument("--adults", type=int)
    p.add_argument("--children", type=int)
    p.add_argument("--cabin", choices=["economy", "premiumEconomy", "business", "first"])
    p.add_argument("--max-stops", type=int, choices=[0, 1, 2])
    p.add_argument("--max-price", type=int, help="per person")
    p.add_argument("--airlines", help="comma-separated airline codes")
    p.add_argument("--sort", choices=["bestValue", "price", "duration", "departure", "arrival"])
    p.add_argument("--country", help="market country code such as GB; prices come back in that country's native currency")

    p = sub.add_parser("results", help="read a page of results")
    p.add_argument("token")
    p.add_argument("--raw", action="store_true", help="print the full response")

    p = sub.add_parser("details", help="fares and booking links for one itinerary")
    p.add_argument("token")
    p.add_argument("result_id")
    p.add_argument("--raw", action="store_true", help="print the full response")

    args = parser.parse_args()
    if args.command == "airports":
        out = call("GET", "/flights/airports", {"query": args.query, "country": args.country})
    elif args.command == "airlines":
        out = call("GET", "/flights/airlines", {"query": args.query, "country": args.country})
    elif args.command == "search":
        if not args.leg and not (args.origin and args.destination and args.date):
            parser.error("search needs --origin, --destination and --date, or two or more --leg")
        out = call("POST", "/flights/search", body=search_body(args))
    elif args.command == "results":
        page = call("GET", "/flights/results", {"token": args.token})
        out = page if args.raw else summarize_results(page)
    else:
        details = call("GET", "/flights/details", {"token": args.token, "resultId": args.result_id})
        out = details if args.raw else summarize_details(details)
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
