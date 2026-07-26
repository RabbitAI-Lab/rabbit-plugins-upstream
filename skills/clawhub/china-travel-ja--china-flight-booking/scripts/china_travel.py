#!/usr/bin/env python3
"""China Travel - All-in-one TripGenie API Client for inbound tourists.

Supports 5 modes: hotel, flight, attraction, itinerary, tips.
Usage: python china_travel.py <mode> [args...] [--locale=xx]

Modes:
  hotel <city> [check_in] [check_out] [guests] [budget] [preferences]
  flight <origin> <destination> <date> [trip_type] [cabin]
  attraction <city> [days] [interests]
  itinerary <city> <days> [travelers] [interests] [budget]
  tips <question>

All modes support optional --locale=xx parameter (default: en)
Supported locales: en, zh, ja, ko, ru, es, fr, de, ar, th, vi
"""

import sys
import json
import urllib.request
import urllib.error

PROXY_URL = "https://1439498936-eu423jdjnd.ap-guangzhou.tencentscf.com"
PROXY_TOKEN = "tp_8k2mX9vQ4z"


def query_tripgenie(query, locale="en", command_type="hotel"):
    """Query via SCF proxy (token injected server-side, affiliate links auto-injected)."""
    payload = {"query": query, "locale": locale, "command_type": command_type}
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        PROXY_URL, data=data,
        headers={
            "Content-Type": "application/json",
            "X-Proxy-Token": PROXY_TOKEN,
            "User-Agent": "ChinaTravel/2.0",
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode("utf-8"))
            if isinstance(result, dict) and "data" in result:
                response = result["data"]
            elif isinstance(result, str):
                response = result
            else:
                response = str(result)
            return {"success": True, "response": response}
    except urllib.error.HTTPError as e:
        return {"success": False, "error": f"HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}"}
    except Exception as e:
        return {"success": False, "error": f"Error: {str(e)}"}


def build_hotel_query(city, check_in="", check_out="", guests=2, budget="", preferences=""):
    parts = [f"Find hotels in {city}"]
    if check_in and check_out:
        parts.append(f"from {check_in} to {check_out}")
    parts.append(f"for {guests} guest{'s' if guests > 1 else ''}")
    if budget:
        parts.append(f"budget: {budget}")
    if preferences:
        parts.append(f"preferences: {preferences}")
    parts.append("Include hotel names, prices per night, ratings, key features.")
    return ", ".join(parts)


def build_flight_query(origin, destination, date, trip_type="one way", cabin="economy"):
    return f"Find {cabin} class flights from {origin} to {destination} on {date}, {trip_type}"


def build_attraction_query(city, days=1, interests=""):
    parts = [f"What are the top attractions and things to do in {city}"]
    if int(days) > 1:
        parts.append(f"for {days} days")
    if interests:
        parts.append(f"interested in: {interests}")
    parts.append("Include ticket prices, opening hours, and practical tips if available.")
    return ", ".join(parts)


def build_itinerary_query(city, days, travelers=2, interests="", budget=""):
    parts = [f"Plan a {days}-day itinerary for {city}"]
    parts.append(f"for {travelers} traveler{'s' if travelers > 1 else ''}")
    if interests:
        parts.append(f"interests: {interests}")
    if budget:
        parts.append(f"budget level: {budget}")
    parts.append("Include hotel recommendations, must-see attractions, dining suggestions, and practical tips.")
    return ", ".join(parts)


def build_tips_query(question, locale="en"):
    return f"{question}"


def parse_locale(args):
    """Extract --locale=xx from args, return (locale, remaining_args)."""
    locale = "en"
    remaining = []
    for arg in args:
        if arg.startswith("--locale="):
            locale = arg.split("=", 1)[1]
        else:
            remaining.append(arg)
    return locale, remaining


def get_cross_guide(mode, locale="en"):
    """Return cross-feature guidance based on current mode."""
    guides = {
        "en": {
            "hotel": "\n\n---\n💡 You can also search flights, find attractions, plan itineraries, or ask travel tips.",
            "flight": "\n\n---\n💡 You can also search hotels, find attractions, plan itineraries, or ask travel tips.",
            "attraction": "\n\n---\n💡 You can also search hotels, book flights, plan itineraries, or ask travel tips.",
            "itinerary": "\n\n---\n💡 You can also search hotels, book flights, find attractions, or ask travel tips.",
            "tips": "\n\n---\n💡 You can also search hotels, book flights, find attractions, or plan itineraries.",
        },
        "zh": {
            "hotel": "\n\n---\n💡 您还可以查询航班、景点、规划行程或咨询旅行贴士。",
            "flight": "\n\n---\n💡 您还可以查询酒店、景点、规划行程或咨询旅行贴士。",
            "attraction": "\n\n---\n💡 您还可以查询酒店、航班、规划行程或咨询旅行贴士。",
            "itinerary": "\n\n---\n💡 您还可以查询酒店、航班、景点或咨询旅行贴士。",
            "tips": "\n\n---\n💡 您还可以查询酒店、航班、景点或规划行程。",
        },
        "ja": {
            "hotel": "\n\n---\n💡 航空券検索、観光地検索、旅程プラン、旅行アドバイスもご利用いただけます。",
            "flight": "\n\n---\n💡 ホテル検索、観光地検索、旅程プラン、旅行アドバイスもご利用いただけます。",
            "attraction": "\n\n---\n💡 ホテル検索、航空券検索、旅程プラン、旅行アドバイスもご利用いただけます。",
            "itinerary": "\n\n---\n💡 ホテル検索、航空券検索、観光地検索、旅行アドバイスもご利用いただけます。",
            "tips": "\n\n---\n💡 ホテル検索、航空券検索、観光地検索、旅程プランもご利用いただけます。",
        },
        "ko": {
            "hotel": "\n\n---\n💡 항공권 검색, 관광지 검색, 일정 계획, 여행 팁도 이용하실 수 있습니다.",
            "flight": "\n\n---\n💡 호텔 검색, 관광지 검색, 일정 계획, 여행 팁도 이용하실 수 있습니다.",
            "attraction": "\n\n---\n💡 호텔 검색, 항공권 검색, 일정 계획, 여행 팁도 이용하실 수 있습니다.",
            "itinerary": "\n\n---\n💡 호텔 검색, 항공권 검색, 관광지 검색, 여행 팁도 이용하실 수 있습니다.",
            "tips": "\n\n---\n💡 호텔 검색, 항공권 검색, 관광지 검색, 일정 계획도 이용하실 수 있습니다.",
        },
        "ru": {
            "hotel": "\n\n---\n💡 Вы также можете искать авиабилеты, достопримечательности, планировать маршруты или задавать вопросы.",
            "flight": "\n\n---\n💡 Вы также можете искать отели, достопримечательности, планировать маршруты или задавать вопросы.",
            "attraction": "\n\n---\n💡 Вы также можете искать отели, авиабилеты, планировать маршруты или задавать вопросы.",
            "itinerary": "\n\n---\n💡 Вы также можете искать отели, авиабилеты, достопримечательности или задавать вопросы.",
            "tips": "\n\n---\n💡 Вы также можете искать отели, авиабилеты, достопримечательности или планировать маршруты.",
        },
    }
    locale_guides = guides.get(locale, guides["en"])
    return locale_guides.get(mode, "")


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "success": False,
            "error": "Usage: china_travel.py <mode> [args...] [--locale=xx]\n"
                     "Modes: hotel, flight, attraction, itinerary, tips\n"
                     "Supported locales: en, zh, ja, ko, ru, es, fr, de, ar, th, vi"
        }, ensure_ascii=False))
        sys.exit(1)

    mode = sys.argv[1].lower()
    raw_args = sys.argv[2:]
    
    # Parse locale from args
    locale, args = parse_locale(raw_args)

    if mode == "hotel":
        if len(args) < 1:
            print(json.dumps({"success": False, "error": "hotel mode requires: <city>"}, ensure_ascii=False))
            sys.exit(1)
        city = args[0]
        check_in = args[1] if len(args) > 1 else ""
        check_out = args[2] if len(args) > 2 else ""
        guests = int(args[3]) if len(args) > 3 else 2
        budget = args[4] if len(args) > 4 else ""
        preferences = args[5] if len(args) > 5 else ""
        query = build_hotel_query(city, check_in, check_out, guests, budget, preferences)
        result = query_tripgenie(query, locale=locale, command_type="hotel")

    elif mode == "flight":
        if len(args) < 3:
            print(json.dumps({"success": False, "error": "flight mode requires: <origin> <destination> <date>"}, ensure_ascii=False))
            sys.exit(1)
        origin, destination, date = args[0], args[1], args[2]
        trip_type = args[3] if len(args) > 3 else "one way"
        cabin = args[4] if len(args) > 4 else "economy"
        query = build_flight_query(origin, destination, date, trip_type, cabin)
        result = query_tripgenie(query, locale=locale, command_type="flight")

    elif mode == "attraction":
        if len(args) < 1:
            print(json.dumps({"success": False, "error": "attraction mode requires: <city>"}, ensure_ascii=False))
            sys.exit(1)
        city = args[0]
        days = args[1] if len(args) > 1 else "1"
        interests = args[2] if len(args) > 2 else ""
        query = build_attraction_query(city, days, interests)
        result = query_tripgenie(query, locale=locale, command_type="attraction")

    elif mode == "itinerary":
        if len(args) < 2:
            print(json.dumps({"success": False, "error": "itinerary mode requires: <city> <days>"}, ensure_ascii=False))
            sys.exit(1)
        city = args[0]
        days = int(args[1])
        travelers = int(args[2]) if len(args) > 2 else 2
        interests = args[3] if len(args) > 3 else ""
        budget = args[4] if len(args) > 4 else ""
        query = build_itinerary_query(city, days, travelers, interests, budget)
        result = query_tripgenie(query, locale=locale, command_type="itinerary")

    elif mode == "tips":
        if len(args) < 1:
            print(json.dumps({"success": False, "error": "tips mode requires: <question>"}, ensure_ascii=False))
            sys.exit(1)
        question = " ".join(args)
        query = build_tips_query(question)
        result = query_tripgenie(query, locale=locale, command_type="query")

    else:
        print(json.dumps({
            "success": False,
            "error": f"Unknown mode: {mode}. Use: hotel, flight, attraction, itinerary, tips"
        }, ensure_ascii=False))
        sys.exit(1)

    # Add cross-feature guidance
    if result.get("success") and isinstance(result.get("response"), str):
        result["response"] += get_cross_guide(mode, locale)

    print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0 if result.get("success") else 1)


if __name__ == "__main__":
    main()
