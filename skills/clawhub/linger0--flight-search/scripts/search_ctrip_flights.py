#!/usr/bin/env python3
import argparse
import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
)
MOBILE_URL = "https://m.ctrip.com/html5/flight/{origin}-{destination}-day-{offset}.html"
CTRIP_TZ = timezone(timedelta(hours=8))

# Fallback aliases for common Chinese city names and airport groups.
FALLBACK_CITY_CODES = {
    "北京": "BJS",
    "上海": "SHA",
    "广州": "CAN",
    "深圳": "SZX",
    "成都": "CTU",
    "杭州": "HGH",
    "武汉": "WUH",
    "西安": "SIA",
    "重庆": "CKG",
    "青岛": "TAO",
    "长沙": "CSX",
    "南京": "NKG",
    "厦门": "XMN",
    "昆明": "KMG",
    "大连": "DLC",
    "天津": "TSN",
    "郑州": "CGO",
    "三亚": "SYX",
    "济南": "TNA",
    "福州": "FOC",
    "香港": "HKG",
    "中国香港": "HKG",
    "台北": "TPE",
    "中国台北": "TPE",
    "澳门": "MFM",
    "中国澳门": "MFM",
}


def load_city_codes() -> dict:
    codes = dict(FALLBACK_CITY_CODES)
    json_path = Path(__file__).resolve().parent.parent / "references" / "city_codes.json"
    if json_path.exists():
        with json_path.open("r", encoding="utf-8") as fh:
            file_codes = json.load(fh)
        for name, code in file_codes.items():
            codes[name] = code
    return codes


def normalize_city(value: str, codes: dict) -> str:
    value = value.strip()
    if not value:
        raise ValueError("city cannot be empty")
    upper = value.upper()
    if len(upper) == 3 and upper.isalpha():
        return upper
    if value in codes:
        return codes[value]
    raise ValueError(f"unknown city or airport code: {value}")


def parse_date(value: str) -> date:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ValueError("date must be in YYYY-MM-DD format") from exc


def fetch_html(origin: str, destination: str, flight_date: date) -> str:
    today_in_ctrip_tz = datetime.now(CTRIP_TZ).date()
    offset = (flight_date - today_in_ctrip_tz).days
    if offset < 0:
        raise ValueError("date must not be in the past")

    url = MOBILE_URL.format(origin=quote(origin), destination=quote(destination), offset=offset)
    req = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(req, timeout=30) as resp:
            return resp.read().decode("utf-8", "ignore")
    except HTTPError as exc:
        raise RuntimeError(f"ctrip returned HTTP {exc.code}") from exc
    except URLError as exc:
        raise RuntimeError(f"failed to reach ctrip: {exc.reason}") from exc


def extract_list_data(html: str) -> dict:
    marker = '"listData":'
    start = html.find(marker)
    if start == -1:
        raise RuntimeError("could not find embedded flight data in the Ctrip page")

    decoder = json.JSONDecoder()
    payload_start = html.find("{", start)
    if payload_start == -1:
        raise RuntimeError("could not find listData payload start")

    try:
        data, _ = decoder.raw_decode(html[payload_start:])
    except json.JSONDecodeError as exc:
        raise RuntimeError("failed to parse embedded flight data") from exc
    return data


def format_hhmm(timestamp: str) -> str:
    try:
        return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").strftime("%H:%M")
    except ValueError:
        return timestamp


def summarize_route(entry: dict) -> dict:
    flight_item = entry.get("flightItem", {})
    segments = flight_item.get("flights", [])
    policy = entry.get("policy") or (flight_item.get("pl") or [{}])[0]

    flight_numbers = [segment.get("flightNo", "") for segment in segments if segment.get("flightNo")]
    depart = format_hhmm(segments[0].get("dtime", "")) if segments else ""
    arrive = format_hhmm(segments[-1].get("atime", "")) if segments else ""
    transit_count = entry.get("transitCount")
    if transit_count is None:
        transit_count = max(len(segments) - 1, 0)
    has_transit = bool(entry.get("isTransit") or transit_count > 0 or len(segments) > 1)

    return {
        "flightNumbers": "/".join(flight_numbers) or "N/A",
        "departureTime": depart,
        "arrivalTime": arrive,
        "price": policy.get("price"),
        "currency": policy.get("currency", "CNY"),
        "hasTransit": has_transit,
        "transitCount": transit_count,
        "from": flight_item.get("departCity", {}).get("name", ""),
        "to": flight_item.get("arriveCity", {}).get("name", ""),
        "routeType": flight_item.get("routeType"),
    }


def search_flights(origin: str, destination: str, flight_date: date) -> dict:
    html = fetch_html(origin, destination, flight_date)
    list_data = extract_list_data(html)
    flights = [summarize_route(entry) for entry in list_data.get("flights", [])]
    flights = [item for item in flights if item.get("price") is not None]
    flights.sort(key=lambda item: (item["price"], item["departureTime"], item["flightNumbers"]))
    return {
        "query": {
            "origin": list_data.get("dcityName", origin),
            "destination": list_data.get("acityName", destination),
            "date": list_data.get("ddate", flight_date.isoformat()),
        },
        "count": len(flights),
        "results": flights,
    }


def select_display_results(results: list, limit: int) -> list:
    if not results:
        return []

    minimum = min(max(limit, 5), len(results))
    cheapest_price = results[0]["price"]
    cutoff_price = min(int(cheapest_price * 1.5), 1000)
    selected = results[:minimum]

    for item in results[minimum:]:
        if item["price"] > cutoff_price:
            break
        selected.append(item)

    return selected


def print_text(result: dict, limit: int) -> None:
    query = result["query"]
    top_results = select_display_results(result["results"], limit)
    print(f"{query['origin']}→{query['destination']}  {query['date']}")
    print(f"共 {result['count']} 班，以下显示 {len(top_results)} 班：")
    print()
    for idx, item in enumerate(top_results, start=1):
        transit = "直飞" if not item["hasTransit"] else f"转机{item['transitCount']}次"
        print(
            f"{idx}. {item['flightNumbers']}\n"
            f"{item['departureTime']}-{item['arrivalTime']}  {item['price']}元  {transit}"
        )
        if idx != len(top_results):
            print()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Search Ctrip mobile flight results and sort them by price ascending."
    )
    parser.add_argument("origin", help="Departure city name or 3-letter city/airport code")
    parser.add_argument("destination", help="Arrival city name or 3-letter city/airport code")
    parser.add_argument("date", help="Flight date in YYYY-MM-DD format")
    parser.add_argument("--limit", type=int, default=20, help="Number of results to print in text mode")
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    city_codes = load_city_codes()

    try:
        origin = normalize_city(args.origin, city_codes)
        destination = normalize_city(args.destination, city_codes)
        flight_date = parse_date(args.date)
        result = search_flights(origin, destination, flight_date)
    except Exception as exc:  # Keep CLI failures human-readable.
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print_text(result, max(args.limit, 1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
