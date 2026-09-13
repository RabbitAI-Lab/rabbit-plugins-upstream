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
    echo "only GET and POST are supported by the crawlora-datasets skill" >&2
    exit 2
    ;;
esac

# Reject path syntax that could smuggle a route through a shell glob check.
case "$path" in
  ""|*[?#%]*|*..*|*//* )
    echo "invalid path for the crawlora-datasets skill" >&2
    exit 2
    ;;
esac
case "$path" in
  /datasets) ;;
  /datasets/airbnb-markets/facets) ;;
  /datasets/airbnb-markets/items/*) ;;
  /datasets/airbnb-markets/nearby) ;;
  /datasets/airbnb-markets/search) ;;
  /datasets/apple-podcasts-shows/facets) ;;
  /datasets/apple-podcasts-shows/items/*) ;;
  /datasets/apple-podcasts-shows/search) ;;
  /datasets/apps-charts/search) ;;
  /datasets/apps-reviews/search) ;;
  /datasets/apps/search) ;;
  /datasets/bbb-businesses/facets) ;;
  /datasets/bbb-businesses/items/*) ;;
  /datasets/bbb-businesses/search) ;;
  /datasets/boxofficemojo/facets) ;;
  /datasets/boxofficemojo/items/*) ;;
  /datasets/boxofficemojo/search) ;;
  /datasets/chrome-extensions/changes) ;;
  /datasets/chrome-extensions/facets) ;;
  /datasets/chrome-extensions/history/*) ;;
  /datasets/chrome-extensions/items/*) ;;
  /datasets/chrome-extensions/metrics) ;;
  /datasets/chrome-extensions/search) ;;
  /datasets/chrome-extensions/trending) ;;
  /datasets/creators/search) ;;
  /datasets/facebook-pages/facets) ;;
  /datasets/facebook-pages/items/*) ;;
  /datasets/facebook-pages/search) ;;
  /datasets/github-users/facets) ;;
  /datasets/github-users/items/*) ;;
  /datasets/github-users/nearby) ;;
  /datasets/github-users/search) ;;
  /datasets/goodreads-authors/facets) ;;
  /datasets/goodreads-authors/items/*) ;;
  /datasets/goodreads-authors/search) ;;
  /datasets/goodreads-books/facets) ;;
  /datasets/goodreads-books/items/*) ;;
  /datasets/goodreads-books/search) ;;
  /datasets/google-map-businesses/facets) ;;
  /datasets/google-map-businesses/items/*) ;;
  /datasets/google-map-businesses/nearby) ;;
  /datasets/google-map-businesses/search) ;;
  /datasets/housing-markets/facets) ;;
  /datasets/housing-markets/items/*/*) ;;
  /datasets/housing-markets/search) ;;
  /datasets/instagram-users/facets) ;;
  /datasets/instagram-users/items/*) ;;
  /datasets/instagram-users/search) ;;
  /datasets/jobs/companies) ;;
  /datasets/jobs/companies/*) ;;
  /datasets/jobs/facets) ;;
  /datasets/jobs/items/*) ;;
  /datasets/jobs/nearby) ;;
  /datasets/jobs/search) ;;
  /datasets/journalists/facets) ;;
  /datasets/journalists/items/*/*) ;;
  /datasets/journalists/search) ;;
  /datasets/numbeo-cities/facets) ;;
  /datasets/numbeo-cities/items/*) ;;
  /datasets/numbeo-cities/search) ;;
  /datasets/numbeo-countries/items/*) ;;
  /datasets/numbeo-countries/search) ;;
  /datasets/pitchbook-advisors/facets) ;;
  /datasets/pitchbook-advisors/items/*) ;;
  /datasets/pitchbook-advisors/search) ;;
  /datasets/pitchbook-companies/facets) ;;
  /datasets/pitchbook-companies/items/*) ;;
  /datasets/pitchbook-companies/search) ;;
  /datasets/pitchbook-funds/facets) ;;
  /datasets/pitchbook-funds/items/*) ;;
  /datasets/pitchbook-funds/search) ;;
  /datasets/pitchbook-investors/facets) ;;
  /datasets/pitchbook-investors/items/*) ;;
  /datasets/pitchbook-investors/search) ;;
  /datasets/pitchbook-limited-partners/facets) ;;
  /datasets/pitchbook-limited-partners/items/*) ;;
  /datasets/pitchbook-limited-partners/search) ;;
  /datasets/playstation-games/facets) ;;
  /datasets/playstation-games/items/*) ;;
  /datasets/playstation-games/search) ;;
  /datasets/producthunt-makers/facets) ;;
  /datasets/producthunt-makers/items/*) ;;
  /datasets/producthunt-makers/search) ;;
  /datasets/producthunt-products/facets) ;;
  /datasets/producthunt-products/items/*) ;;
  /datasets/producthunt-products/search) ;;
  /datasets/producthunt-trends/facets) ;;
  /datasets/producthunt-trends/search) ;;
  /datasets/reddit-trending/search) ;;
  /datasets/sec-companies/facets) ;;
  /datasets/sec-companies/financials/*) ;;
  /datasets/sec-companies/insider/*) ;;
  /datasets/sec-companies/items/*) ;;
  /datasets/sec-companies/search) ;;
  /datasets/sec-institutional-positions/facets) ;;
  /datasets/sec-institutional-positions/search) ;;
  /datasets/starbucks-stores/facets) ;;
  /datasets/starbucks-stores/items/*) ;;
  /datasets/starbucks-stores/nearby) ;;
  /datasets/starbucks-stores/search) ;;
  /datasets/steam-achievements/search) ;;
  /datasets/steam-charts/search) ;;
  /datasets/steam-games/facets) ;;
  /datasets/steam-games/items/*) ;;
  /datasets/steam-games/search) ;;
  /datasets/steam-news/search) ;;
  /datasets/steam-playercounts/search) ;;
  /datasets/steam-prices/search) ;;
  /datasets/steam-reviews/search) ;;
  /datasets/techstack/facets) ;;
  /datasets/techstack/items/*) ;;
  /datasets/techstack/search) ;;
  /datasets/trustmrr/facets) ;;
  /datasets/trustmrr/history/*) ;;
  /datasets/trustmrr/items/*) ;;
  /datasets/trustmrr/search) ;;
  /datasets/vehicle-listings/facets) ;;
  /datasets/vehicle-listings/items/*) ;;
  /datasets/vehicle-listings/price-history/*) ;;
  /datasets/vehicle-listings/search) ;;
  /datasets/x-users/facets) ;;
  /datasets/x-users/items/*) ;;
  /datasets/x-users/search) ;;
  /datasets/youtube-creators/facets) ;;
  /datasets/youtube-creators/items/*) ;;
  /datasets/youtube-creators/search) ;;
  *)
    echo "path is not in the crawlora-datasets skill catalog" >&2
    exit 2
    ;;
esac



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
