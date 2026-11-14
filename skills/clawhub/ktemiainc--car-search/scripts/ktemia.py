#!/usr/bin/env python3
"""Minimal client for the Ktemia car search API. Standard library only.

    ktemia.py locations QUERY [--type city|airport|all] [--country CC]
    ktemia.py search --pickup LOCATION_ID --pickup-date YYYY-MM-DD --dropoff-date YYYY-MM-DD
                     [--providers "Booking.com,Expedia"] [--agencies avis,hertz]
    ktemia.py results TOKEN
    ktemia.py details TOKEN RESULT_ID

Reads the API key from KTEMIA_API_KEY. Prints JSON. Exits 1 on an API error.
Reference: https://www.ktemia.com/docs/api/cars/search/
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


def money(block):
    if not isinstance(block, dict):
        return None
    return block.get("formatted") or block.get("amount")


def filter_ids(items, limit=12):
    """Compact `id (count)` view of one availableFilters facet.

    Both facets arrive as a list of objects on cars. Only the ids are kept:
    they are what a follow-up search sends back as --providers / --agencies.
    """
    if not isinstance(items, list):
        return None
    out = []
    for item in items:
        if isinstance(item, dict) and item.get("id"):
            out.append({"id": item["id"], "count": item.get("count")})
    return out[:limit] or None


def summarize_results(page):
    cars = []
    for car in page.get("cars", []):
        vehicle = car.get("car") or {}
        best = car.get("bestOption") or {}
        cars.append({
            "id": car.get("id"),
            "name": vehicle.get("name"),
            "class": vehicle.get("class"),
            "passengers": vehicle.get("passengers"),
            "bags": vehicle.get("bags"),
            "transmission": vehicle.get("transmission"),
            "agency": (car.get("agency") or {}).get("name"),
            "price": money(best.get("price") or car.get("price")),
            "perDay": money(best.get("perDay")),
            "sellers": car.get("optionCount"),
        })
    filters = page.get("availableFilters") or {}
    summary = {
        "page": page.get("page"),
        "totalResults": page.get("totalResults"),
        "nextToken": page.get("nextToken"),
        "cars": cars,
    }
    # Surfaced so a follow-up search can filter by seller or agency without
    # re-reading the whole page with --raw.
    sites = filter_ids(filters.get("bookingSites"))
    agencies = filter_ids(filters.get("agency"))
    if sites:
        summary["bookingSites"] = sites
    if agencies:
        summary["agencies"] = agencies
    return summary


def summarize_details(details):
    options = []
    for option in details.get("bookingOptions", []):
        provider = option.get("provider") or {}
        options.append({
            "seller": provider.get("name") or provider.get("code"),
            "price": money(option.get("totalPrice") or option.get("price")),
            "perDay": money(option.get("perDay")),
            "providerUrl": option.get("providerUrl"),
        })
    return {"resultId": details.get("resultId"), "bookingOptions": options}


def id_list(value):
    """Split a comma-separated filter-id option into the list the API wants.

    Ids are display names taken straight from `availableFilters`, so they can
    contain spaces and dots ("Auto Europe", "Booking.com"). Only the comma is a
    separator, and case is preserved: the API matches these ids exactly.
    """
    if not value:
        return None
    ids = [part.strip() for part in value.split(",") if part.strip()]
    return ids or None


def search_body(args):
    body = {
        "pickupLocation": args.pickup,
        "pickupDate": args.pickup_date,
        "dropoffDate": args.dropoff_date,
    }
    optional = {
        "dropoffLocation": args.dropoff,
        "pickupTime": args.pickup_time,
        "dropoffTime": args.dropoff_time,
        "driverAge": args.driver_age,
        "carClass": args.car_class,
        "transmission": args.transmission,
        "maxPrice": args.max_price,
        "providers": id_list(args.providers),
        "agencies": id_list(args.agencies),
        "sortBy": args.sort,
        "sortOrder": args.sort_order,
        "priceMode": args.price_mode,
        "country": args.country,
    }
    body.update({k: v for k, v in optional.items() if v is not None})
    return body


def main():
    parser = argparse.ArgumentParser(description="Ktemia car search API client")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("locations", help="look up pickup and drop-off location ids")
    p.add_argument("query")
    p.add_argument("--type", choices=["city", "airport", "all"], dest="location_type")
    p.add_argument("--country")

    p = sub.add_parser("search", help="start a car search; returns a searchToken")
    p.add_argument("--pickup", required=True, help="locationId from locations")
    p.add_argument("--dropoff", help="locationId; omit to return the car where it was picked up")
    p.add_argument("--pickup-date", required=True, help="YYYY-MM-DD")
    p.add_argument("--dropoff-date", required=True, help="YYYY-MM-DD")
    p.add_argument("--pickup-time", help="HH:MM, default 12:00")
    p.add_argument("--dropoff-time", help="HH:MM, default 12:00")
    p.add_argument("--driver-age", type=int)
    p.add_argument("--class", dest="car_class", choices=["small", "medium", "large", "suv", "van", "pickup", "luxury", "convertible"])
    p.add_argument("--transmission", choices=["automatic", "manual"])
    p.add_argument("--max-price", type=int, help="whole number in the country's native currency")
    p.add_argument("--providers", help="comma-separated booking-site ids from availableFilters.bookingSites, for example 'Booking.com,Expedia'. Up to 10")
    p.add_argument("--agencies", help="comma-separated agency ids from availableFilters.agency, for example 'avis,hertz'. Up to 10")
    p.add_argument("--sort", choices=["bestValue", "price", "rating", "distance"])
    p.add_argument("--sort-order", choices=["asc", "desc"])
    p.add_argument("--price-mode", choices=["total", "perDay"])
    p.add_argument("--country", help="market country code such as GB; prices come back in that country's native currency")

    p = sub.add_parser("results", help="read a page of results")
    p.add_argument("token")
    p.add_argument("--raw", action="store_true", help="print the full response")

    p = sub.add_parser("details", help="sellers and booking links for one car")
    p.add_argument("token")
    p.add_argument("result_id")
    p.add_argument("--raw", action="store_true", help="print the full response")

    args = parser.parse_args()
    if args.command == "locations":
        out = call("GET", "/cars/locations", {
            "query": args.query,
            "type": args.location_type,
            "country": args.country,
        })
    elif args.command == "search":
        out = call("POST", "/cars/search", body=search_body(args))
    elif args.command == "results":
        page = call("GET", "/cars/results", {"token": args.token})
        out = page if args.raw else summarize_results(page)
    else:
        details = call("GET", "/cars/details", {"token": args.token, "resultId": args.result_id})
        out = details if args.raw else summarize_details(details)
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
