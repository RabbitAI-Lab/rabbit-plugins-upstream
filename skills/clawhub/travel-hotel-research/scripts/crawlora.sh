#!/usr/bin/env bash
# Crawlora REST helper — minimal, dependency-free (curl only).
# Calls https://api.crawlora.net/api/v1 with your Crawlora API key.
# Get a free key (2,000 credits/mo, no card) at https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills.
#
# Usage:
#   GET  :  crawlora.sh /amazon/search k=laptop s=relevanceblender
#   GET  :  crawlora.sh /youtube/transcript/dQw4w9WgXcQ
#   POST :  crawlora.sh -X POST /google/search '{"keyword":"web scraping api","language":"en","country":"us"}'
#   POST :  crawlora.sh -X POST /google/trends/explore/interest-over-time '{"keywords":["bitcoin"]}'
#
# GET key=value args become the query string. POST takes one JSON body argument
# (or pass it with -d '<json>'). Prints raw JSON to stdout — pipe into `jq`.
set -euo pipefail

: "${CRAWLORA_API_KEY:?Set CRAWLORA_API_KEY first — get a free key at https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills}"
# The key is written to a curl config file below. Restrict it to the key
# alphabet so a newline, quote, or config directive cannot alter that file.
case "$CRAWLORA_API_KEY" in
  *[!A-Za-z0-9._-]*) echo "invalid CRAWLORA_API_KEY format" >&2; exit 2 ;;
esac
# Fixed, non-overridable: an env-configurable base URL would let anything that
# can set CRAWLORA_API_BASE redirect this key to an attacker-controlled host.
base="https://api.crawlora.net/api/v1"

method="GET"
body=""
args=()
while [ $# -gt 0 ]; do
  case "$1" in
    -X) method="$2"; shift 2 ;;
    -d) body="$2"; shift 2 ;;
    *)  args+=("$1"); shift ;;
  esac
done

[ "${#args[@]}" -ge 1 ] || { echo "usage: crawlora.sh [-X METHOD] /path [k=v ... | json-body]" >&2; exit 2; }
path="${args[0]}"
rest=("${args[@]:1}")

# This skill's helper is limited to its documented Crawlora route set. Keep
# caller-account surfaces and unrelated API routes out of the helper even if
# someone supplies an undocumented path directly.
case "$method" in
  GET|POST) ;;
  *)
    echo "only GET and POST are supported by the travel-hotel-research skill" >&2
    exit 2
    ;;
esac

# Reject path syntax that could smuggle a route through a shell glob check.
case "$path" in
  ""|*[?#%]*|*..*|*//* )
    echo "invalid path for the travel-hotel-research skill" >&2
    exit 2
    ;;
esac

# Static routes use escaped case patterns. Parameterized routes use anchored
# extended regular expressions so every {param} is exactly one non-empty path
# segment; unlike a case '*', [^/]+ cannot consume another slash.
route_allowed=false
case "$path" in
  /accor/amenities) route_allowed=true ;;
  /accor/brands) route_allowed=true ;;
  /accor/catalog/hotels) route_allowed=true ;;
  /accor/destination/hotels) route_allowed=true ;;
  /accor/property) route_allowed=true ;;
  /accor/search) route_allowed=true ;;
  /accor/search/details) route_allowed=true ;;
  /accor/search/suggest) route_allowed=true ;;
  /agoda/activities/search) route_allowed=true ;;
  /agoda/flights/itinerary-amenities) route_allowed=true ;;
  /agoda/flights/search) route_allowed=true ;;
  /agoda/flights/search-locations) route_allowed=true ;;
  /agoda/homes/search) route_allowed=true ;;
  /agoda/hotels/search) route_allowed=true ;;
  /airbnb/search) route_allowed=true ;;
  /booking-attractions/detail) route_allowed=true ;;
  /booking-attractions/reviews) route_allowed=true ;;
  /booking-attractions/search) route_allowed=true ;;
  /booking-flights/autocomplete) route_allowed=true ;;
  /booking-flights/search) route_allowed=true ;;
  /booking/hotel-detail) route_allowed=true ;;
  /booking/reviews) route_allowed=true ;;
  /booking/search) route_allowed=true ;;
  /expedia/activities/search) route_allowed=true ;;
  /expedia/flights/search) route_allowed=true ;;
  /expedia/locations/search) route_allowed=true ;;
  /expedia/properties/detail) route_allowed=true ;;
  /expedia/properties/filters) route_allowed=true ;;
  /expedia/properties/reviews) route_allowed=true ;;
  /expedia/properties/search) route_allowed=true ;;
  /hotels/autocomplete) route_allowed=true ;;
  /hotels/offers) route_allowed=true ;;
  /hotels/property) route_allowed=true ;;
  /hotels/rates) route_allowed=true ;;
  /hotels/reviews) route_allowed=true ;;
  /hotels/reviews/archive) route_allowed=true ;;
  /hotels/search) route_allowed=true ;;
  /ticketmaster/attraction) route_allowed=true ;;
  /ticketmaster/attraction-events) route_allowed=true ;;
  /ticketmaster/attraction-related) route_allowed=true ;;
  /ticketmaster/attraction-reviews) route_allowed=true ;;
  /ticketmaster/discover-categories) route_allowed=true ;;
  /ticketmaster/discover-category-events) route_allowed=true ;;
  /ticketmaster/discover-cities) route_allowed=true ;;
  /ticketmaster/discover-city-events) route_allowed=true ;;
  /ticketmaster/event) route_allowed=true ;;
  /ticketmaster/search-events) route_allowed=true ;;
  /ticketmaster/suggest) route_allowed=true ;;
  /ticketmaster/trending-attractions) route_allowed=true ;;
  /ticketmaster/venue) route_allowed=true ;;
  /ticketmaster/venue-enhanced-details) route_allowed=true ;;
  /ticketmaster/venue-events) route_allowed=true ;;
  /ticketweb/event) route_allowed=true ;;
  /ticketweb/search) route_allowed=true ;;
  /ticketweb/venue) route_allowed=true ;;
  /tripadvisor/autocomplete) route_allowed=true ;;
  /tripadvisor/enums) route_allowed=true ;;
  /tripadvisor/hotels) route_allowed=true ;;
  /tripadvisor/place) route_allowed=true ;;
  /tripadvisor/reviews) route_allowed=true ;;
  /tripadvisor/search) route_allowed=true ;;
  /tripcom/hotels/search) route_allowed=true ;;
esac
if [ "$route_allowed" = false ]; then
  route_regexes=(
  '^/agoda/activities/[^/]+$'
  '^/agoda/hotels/[^/]+$'
  '^/airbnb/host/[^/]+$'
  '^/airbnb/host/[^/]+/listings$'
  '^/airbnb/host/[^/]+/reviews$'
  '^/airbnb/room/[^/]+$'
  '^/airbnb/room/[^/]+/calendar$'
  '^/airbnb/room/[^/]+/reviews$'
  '^/tripcom/hotels/[^/]+$'
  )
  for route_regex in ${route_regexes[@]+"${route_regexes[@]}"}; do
    if [[ "$path" =~ $route_regex ]]; then
      route_allowed=true
      break
    fi
  done
fi
if [ "$route_allowed" = false ]; then
  echo "path is not in the travel-hotel-research skill catalog" >&2
  exit 2
fi



# Keep the API key out of the curl process command line. A private temporary
# config supplies the header and is removed automatically on exit.
curl_config="$(mktemp "${TMPDIR:-/tmp}/crawlora-curl.XXXXXX")"
chmod 600 "$curl_config"
trap 'rm -f "$curl_config"' EXIT
printf 'header = "x-api-key: %s"\n' "$CRAWLORA_API_KEY" >"$curl_config"
auth=(--config "$curl_config")

if [ "$method" = "GET" ]; then
  # -G + --data-urlencode URL-encodes each value (so spaces etc. are safe).
  qs=()
  for kv in ${rest[@]+"${rest[@]}"}; do
    [ -n "$kv" ] || continue
    # curl treats both @file and name@file forms as local-file input for
    # --data-urlencode. Reject @ outright so query arguments cannot disclose
    # local files to the Crawlora API.
    case "$kv" in
      *@*) echo "@ is not allowed in query arguments" >&2; exit 2 ;;
    esac
    qs+=(--data-urlencode "$kv")
  done
  curl -fsS -G "${auth[@]}" ${qs[@]+"${qs[@]}"} "${base}${path}"
else
  [ -n "$body" ] || body="${rest[0]:-}"
  [ -n "$body" ] || body='{}'
  # Stream the body on stdin so curl never interprets a user value as its
  # @file shorthand (and cannot read local files supplied in a request body).
  printf '%s' "$body" | curl -fsS -X "$method" "${auth[@]}" \
    -H "Content-Type: application/json" --data-binary @- "${base}${path}"
fi
