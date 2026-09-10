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
    echo "only GET and POST are supported by the movie-tv-research skill" >&2
    exit 2
    ;;
esac

# Reject path syntax that could smuggle a route through a shell glob check.
case "$path" in
  ""|*[?#%]*|*..*|*//* )
    echo "invalid path for the movie-tv-research skill" >&2
    exit 2
    ;;
esac
case "$path" in
  /boxofficemojo/brand) ;;
  /boxofficemojo/brands) ;;
  /boxofficemojo/calendar) ;;
  /boxofficemojo/calendar/changes) ;;
  /boxofficemojo/calendar/date) ;;
  /boxofficemojo/date/domestic) ;;
  /boxofficemojo/franchise) ;;
  /boxofficemojo/franchises) ;;
  /boxofficemojo/genre) ;;
  /boxofficemojo/genres) ;;
  /boxofficemojo/lifetime-grosses) ;;
  /boxofficemojo/release) ;;
  /boxofficemojo/release-group) ;;
  /boxofficemojo/showdown) ;;
  /boxofficemojo/showdowns) ;;
  /boxofficemojo/title) ;;
  /boxofficemojo/weekend/domestic) ;;
  /boxofficemojo/weekend/domestic/by-distributor) ;;
  /boxofficemojo/weekend/domestic/estimates) ;;
  /boxofficemojo/year/domestic) ;;
  /boxofficemojo/year/worldwide) ;;
  /imdb/charts) ;;
  /imdb/name) ;;
  /imdb/name/awards) ;;
  /imdb/name/credits) ;;
  /imdb/search) ;;
  /imdb/search/title) ;;
  /imdb/title) ;;
  /imdb/title/awards) ;;
  /imdb/title/company-credits) ;;
  /imdb/title/credits) ;;
  /imdb/title/episodes) ;;
  /imdb/title/filming-locations) ;;
  /imdb/title/goofs) ;;
  /imdb/title/keywords) ;;
  /imdb/title/parental-guide) ;;
  /imdb/title/public-facts-analysis) ;;
  /imdb/title/quotes) ;;
  /imdb/title/ratings) ;;
  /imdb/title/release-info) ;;
  /imdb/title/reviews) ;;
  /imdb/title/similar) ;;
  /imdb/title/technical-specs) ;;
  /imdb/title/trivia) ;;
  /justwatch/age-certifications) ;;
  /justwatch/discover) ;;
  /justwatch/episode/by-id) ;;
  /justwatch/episode/offers) ;;
  /justwatch/genre/titles) ;;
  /justwatch/genres) ;;
  /justwatch/monetization/titles) ;;
  /justwatch/new) ;;
  /justwatch/popular) ;;
  /justwatch/provider/titles) ;;
  /justwatch/providers) ;;
  /justwatch/search) ;;
  /justwatch/season/by-id) ;;
  /justwatch/season/episodes) ;;
  /justwatch/show/seasons) ;;
  /justwatch/title) ;;
  /justwatch/title/analysis) ;;
  /justwatch/title/by-id) ;;
  /justwatch/title/media) ;;
  /justwatch/title/offers) ;;
  /justwatch/title/similar) ;;
  /letterboxd/film/*) ;;
  /letterboxd/film/*/rating-histogram) ;;
  /letterboxd/film/*/reviews) ;;
  /letterboxd/film/*/similar) ;;
  /letterboxd/member/*) ;;
  /letterboxd/person/*) ;;
  /letterboxd/popular) ;;
  /letterboxd/search) ;;
  /metacritic/browse) ;;
  /metacritic/game/*) ;;
  /metacritic/game/*/critic-reviews) ;;
  /metacritic/game/*/user-reviews) ;;
  /metacritic/movie/*) ;;
  /metacritic/movie/*/critic-reviews) ;;
  /metacritic/movie/*/user-reviews) ;;
  /metacritic/tv/*) ;;
  /metacritic/tv/*/critic-reviews) ;;
  /metacritic/tv/*/user-reviews) ;;
  /rottentomatoes/browse/movies) ;;
  /rottentomatoes/browse/tv) ;;
  /rottentomatoes/episode) ;;
  /rottentomatoes/movie) ;;
  /rottentomatoes/movie/reviews) ;;
  /rottentomatoes/person) ;;
  /rottentomatoes/search) ;;
  /rottentomatoes/season) ;;
  /rottentomatoes/series) ;;
  /tmdb/movie/*) ;;
  /tmdb/movie/list) ;;
  /tmdb/person/*) ;;
  /tmdb/person/list) ;;
  /tmdb/search) ;;
  /tmdb/tv/*) ;;
  /tmdb/tv/list) ;;
  *)
    echo "path is not in the movie-tv-research skill catalog" >&2
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
