#!/usr/bin/env python3
"""Minimal client for the Ktemia hotel search API. Standard library only.

    ktemia.py locations QUERY [--country CC]
    ktemia.py search --location LOCATION_ID --checkin YYYY-MM-DD --checkout YYYY-MM-DD
                     [--providers "Booking.com,Expedia"]
    ktemia.py results TOKEN
    ktemia.py details TOKEN RESULT_ID
    ktemia.py reviews HOTEL_ID [--page N]

Reads the API key from KTEMIA_API_KEY. Prints JSON. Exits 1 on an API error.
Reference: https://www.ktemia.com/docs/api/hotels/search/
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


def clip(text, limit=180):
    if not isinstance(text, str) or len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def summarize_results(page):
    hotels = []
    for hotel in page.get("hotels", []):
        rating = hotel.get("rating") or {}
        place = hotel.get("location") or {}
        best = hotel.get("bestOption") or {}
        hotels.append({
            "id": hotel.get("id"),
            "name": hotel.get("name"),
            "stars": hotel.get("stars"),
            "score": rating.get("score"),
            "reviews": rating.get("reviewCount"),
            "neighborhood": place.get("neighborhood"),
            "price": money(best.get("price")),
            "total": money(best.get("totalPrice")),
            "seller": best.get("provider"),
        })
    summary = {
        "page": page.get("page"),
        "totalResults": page.get("totalResults"),
        "hasMore": page.get("hasMore"),
        "nextToken": page.get("nextToken"),
        "destination": (page.get("destination") or {}).get("name"),
        "hotels": hotels,
    }
    # Surfaced so a follow-up search can filter by seller without re-reading
    # the whole page with --raw.
    sites = filter_ids((page.get("availableFilters") or {}).get("bookingSites"))
    if sites:
        summary["bookingSites"] = sites
    return summary

def summarize_details(details):
    reviews = details.get("reviews") or {}
    options = []
    for option in details.get("bookingOptions", []):
        options.append({
            "seller": option.get("provider"),
            "price": money(option.get("price")),
            "total": money(option.get("totalPrice")),
            "providerUrl": option.get("providerUrl"),
        })
    recent = []
    for review in (reviews.get("recent") or [])[:5]:
        recent.append({
            "score": review.get("score"),
            "date": review.get("date"),
            "author": review.get("author"),
            "source": review.get("source"),
            "positive": clip(review.get("positive")),
            "negative": clip(review.get("negative")),
            "comment": clip(review.get("comment")),
        })
    return {
        "resultId": details.get("resultId"),
        "bookingOptions": options,
        "reviews": {
            "score": reviews.get("score"),
            "count": reviews.get("count"),
            "recent": recent,
        },
    }


def summarize_reviews(page):
    reviews = []
    for review in page.get("reviews", []):
        reviews.append({
            "id": review.get("id"),
            "score": review.get("score"),
            "date": review.get("date"),
            "author": review.get("author"),
            "source": review.get("source"),
            "positive": clip(review.get("positive")),
            "negative": clip(review.get("negative")),
            "comment": clip(review.get("comment")),
            "url": review.get("url"),
        })
    return {
        "hotelId": page.get("hotelId"),
        "totalReviews": page.get("totalReviews"),
        "page": page.get("page"),
        "hasMore": page.get("hasMore"),
        "reviews": reviews,
    }


def ints(value):
    if not value:
        return None
    return [int(part) for part in value.split(",") if part.strip()]


def id_list(value):
    """Split a comma-separated filter-id option into the list the API wants.

    Booking-site ids are display names taken straight from `availableFilters`,
    so they can contain spaces and dots ("Booking.com", "Trip.com"). Only the
    comma is a separator, and case is preserved: the API matches these ids
    exactly, unlike amenity ids which are lowercased.
    """
    if not value:
        return None
    ids = [part.strip() for part in value.split(",") if part.strip()]
    return ids or None


def filter_ids(section, limit=12):
    """Compact `id (count)` view of one availableFilters facet.

    Hotel facets are objects wrapping an ``options`` list, unlike the cars API
    where the facet is the list itself.
    """
    if not isinstance(section, dict):
        return None
    out = []
    for item in section.get("options") or []:
        if isinstance(item, dict) and item.get("id"):
            out.append({"id": item["id"], "count": item.get("count")})
    return out[:limit] or None


def search_body(args):
    body = {
        "location": args.location,
        "checkin": args.checkin,
        "checkout": args.checkout,
    }
    optional = {
        "adults": args.adults,
        "rooms": args.rooms,
        "childAges": ints(args.child_ages),
        "minStars": args.min_stars,
        "minRating": args.min_rating,
        "maxPrice": args.max_price,
        "freeCancellation": True if args.free_cancellation else None,
        "amenities": [part.strip().lower() for part in args.amenities.split(",")] if args.amenities else None,
        "providers": id_list(args.providers),
        "sortBy": args.sort,
        "sortOrder": args.sort_order,
        "country": args.country,
    }
    body.update({k: v for k, v in optional.items() if v is not None})
    return body


def main():
    parser = argparse.ArgumentParser(description="Ktemia hotel search API client")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("locations", help="look up location ids")
    p.add_argument("query")
    p.add_argument("--country")

    p = sub.add_parser("search", help="start a hotel search; returns a searchToken")
    p.add_argument("--location", required=True, help="locationId from locations")
    p.add_argument("--checkin", required=True, help="YYYY-MM-DD")
    p.add_argument("--checkout", required=True, help="YYYY-MM-DD")
    p.add_argument("--adults", type=int)
    p.add_argument("--rooms", type=int)
    p.add_argument("--child-ages", help="comma-separated ages, for example 4,7")
    p.add_argument("--min-stars", type=int, choices=[2, 3, 4, 5])
    p.add_argument("--min-rating", type=int, choices=[6, 7, 8, 9])
    p.add_argument("--max-price", type=int, help="before-tax stay price, whole number")
    p.add_argument("--free-cancellation", action="store_true")
    p.add_argument("--amenities", help="comma-separated amenity ids, for example pool")
    p.add_argument("--providers", help="comma-separated booking-site ids from availableFilters.bookingSites, for example 'Booking.com,Expedia'. Up to 10")
    p.add_argument("--sort", choices=["bestValue", "price", "rating", "stars", "distance"])
    p.add_argument("--sort-order", choices=["asc", "desc"])
    p.add_argument("--country", help="market country code such as GB; prices come back in that country's native currency")

    p = sub.add_parser("results", help="read a page of results")
    p.add_argument("token")
    p.add_argument("--raw", action="store_true", help="print the full response")

    p = sub.add_parser("details", help="sellers, booking links, and recent reviews for one hotel")
    p.add_argument("token")
    p.add_argument("result_id")
    p.add_argument("--raw", action="store_true", help="print the full response")

    p = sub.add_parser("reviews", help="one page of guest reviews; no search token")
    p.add_argument("hotel_id")
    p.add_argument("--sort", choices=["recent", "oldest", "highestScore", "lowestScore"])
    p.add_argument("--travelers", help="comma-separated: families,couples,solo,friends,business")
    p.add_argument("--months", help="comma-separated months 1-12")
    p.add_argument("--sources", help="comma-separated: booking,agoda,priceline")
    p.add_argument("--search", help="only reviews that mention this text")
    p.add_argument("--page", type=int)
    p.add_argument("--raw", action="store_true", help="print the full response")

    args = parser.parse_args()
    if args.command == "locations":
        out = call("GET", "/hotels/locations", {"query": args.query, "country": args.country})
    elif args.command == "search":
        out = call("POST", "/hotels/search", body=search_body(args))
    elif args.command == "results":
        page = call("GET", "/hotels/results", {"token": args.token})
        out = page if args.raw else summarize_results(page)
    elif args.command == "details":
        details = call("GET", "/hotels/details", {"token": args.token, "resultId": args.result_id})
        out = details if args.raw else summarize_details(details)
    else:
        page = call("GET", "/hotels/reviews", {
            "hotelId": args.hotel_id,
            "sortBy": args.sort,
            "travelerTypes": args.travelers,
            "months": args.months,
            "sources": args.sources,
            "search": args.search,
            "page": args.page,
        })
        out = page if args.raw else summarize_reviews(page)
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
