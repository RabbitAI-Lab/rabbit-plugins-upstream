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
  GET) ;;
  *)
    echo "only GET are supported by the entertainment-discovery-research skill" >&2
    exit 2
    ;;
esac

# Reject path syntax that could smuggle a route through a shell glob check.
case "$path" in
  ""|*[?#%]*|*..*|*//* )
    echo "invalid path for the entertainment-discovery-research skill" >&2
    exit 2
    ;;
esac

# Static routes use escaped case patterns. Parameterized routes use anchored
# extended regular expressions so every {param} is exactly one non-empty path
# segment; unlike a case '*', [^/]+ cannot consume another slash.
route_allowed=false
case "$path" in
  /imdb/charts) route_allowed=true ;;
  /imdb/name) route_allowed=true ;;
  /imdb/name/awards) route_allowed=true ;;
  /imdb/name/credits) route_allowed=true ;;
  /imdb/search) route_allowed=true ;;
  /imdb/search/title) route_allowed=true ;;
  /imdb/title) route_allowed=true ;;
  /imdb/title/awards) route_allowed=true ;;
  /imdb/title/company-credits) route_allowed=true ;;
  /imdb/title/credits) route_allowed=true ;;
  /imdb/title/episodes) route_allowed=true ;;
  /imdb/title/filming-locations) route_allowed=true ;;
  /imdb/title/goofs) route_allowed=true ;;
  /imdb/title/keywords) route_allowed=true ;;
  /imdb/title/parental-guide) route_allowed=true ;;
  /imdb/title/public-facts-analysis) route_allowed=true ;;
  /imdb/title/quotes) route_allowed=true ;;
  /imdb/title/ratings) route_allowed=true ;;
  /imdb/title/release-info) route_allowed=true ;;
  /imdb/title/reviews) route_allowed=true ;;
  /imdb/title/similar) route_allowed=true ;;
  /imdb/title/technical-specs) route_allowed=true ;;
  /imdb/title/trivia) route_allowed=true ;;
  /justwatch/age-certifications) route_allowed=true ;;
  /justwatch/discover) route_allowed=true ;;
  /justwatch/episode/by-id) route_allowed=true ;;
  /justwatch/episode/offers) route_allowed=true ;;
  /justwatch/genre/titles) route_allowed=true ;;
  /justwatch/genres) route_allowed=true ;;
  /justwatch/monetization/titles) route_allowed=true ;;
  /justwatch/new) route_allowed=true ;;
  /justwatch/popular) route_allowed=true ;;
  /justwatch/provider/titles) route_allowed=true ;;
  /justwatch/providers) route_allowed=true ;;
  /justwatch/search) route_allowed=true ;;
  /justwatch/season/by-id) route_allowed=true ;;
  /justwatch/season/episodes) route_allowed=true ;;
  /justwatch/show/seasons) route_allowed=true ;;
  /justwatch/title) route_allowed=true ;;
  /justwatch/title/analysis) route_allowed=true ;;
  /justwatch/title/by-id) route_allowed=true ;;
  /justwatch/title/media) route_allowed=true ;;
  /justwatch/title/offers) route_allowed=true ;;
  /justwatch/title/similar) route_allowed=true ;;
  /metacritic/browse) route_allowed=true ;;
  /rottentomatoes/browse/movies) route_allowed=true ;;
  /rottentomatoes/browse/tv) route_allowed=true ;;
  /rottentomatoes/episode) route_allowed=true ;;
  /rottentomatoes/movie) route_allowed=true ;;
  /rottentomatoes/movie/reviews) route_allowed=true ;;
  /rottentomatoes/person) route_allowed=true ;;
  /rottentomatoes/search) route_allowed=true ;;
  /rottentomatoes/season) route_allowed=true ;;
  /rottentomatoes/series) route_allowed=true ;;
  /tmdb/movie/list) route_allowed=true ;;
  /tmdb/person/list) route_allowed=true ;;
  /tmdb/search) route_allowed=true ;;
  /tmdb/tv/list) route_allowed=true ;;
esac
if [ "$route_allowed" = false ]; then
  route_regexes=(
  '^/metacritic/game/[^/]+$'
  '^/metacritic/game/[^/]+/critic-reviews$'
  '^/metacritic/game/[^/]+/user-reviews$'
  '^/metacritic/movie/[^/]+$'
  '^/metacritic/movie/[^/]+/critic-reviews$'
  '^/metacritic/movie/[^/]+/user-reviews$'
  '^/metacritic/tv/[^/]+$'
  '^/metacritic/tv/[^/]+/critic-reviews$'
  '^/metacritic/tv/[^/]+/user-reviews$'
  '^/tmdb/movie/[^/]+$'
  '^/tmdb/person/[^/]+$'
  '^/tmdb/tv/[^/]+$'
  )
  for route_regex in ${route_regexes[@]+"${route_regexes[@]}"}; do
    if [[ "$path" =~ $route_regex ]]; then
      route_allowed=true
      break
    fi
  done
fi
if [ "$route_allowed" = false ]; then
  echo "path is not in the entertainment-discovery-research skill catalog" >&2
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
  curl -q -fsS -G "${auth[@]}" ${qs[@]+"${qs[@]}"} "${base}${path}"
else
  [ -n "$body" ] || body="${rest[0]:-}"
  [ -n "$body" ] || body='{}'
  # Stream the body on stdin so curl never interprets a user value as its
  # @file shorthand (and cannot read local files supplied in a request body).
  printf '%s' "$body" | curl -q -fsS -X "$method" "${auth[@]}" \
    -H "Content-Type: application/json" --data-binary @- "${base}${path}"
fi
