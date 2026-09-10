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
    echo "only GET and POST are supported by the finance-markets-research skill" >&2
    exit 2
    ;;
esac

# Reject path syntax that could smuggle a route through a shell glob check.
case "$path" in
  ""|*[?#%]*|*..*|*//* )
    echo "invalid path for the finance-markets-research skill" >&2
    exit 2
    ;;
esac
case "$path" in
  /coingecko/categories) ;;
  /coingecko/category/*/coins) ;;
  /coingecko/chains) ;;
  /coingecko/chains/*) ;;
  /coingecko/coin/*) ;;
  /coingecko/coin/*/analysis) ;;
  /coingecko/exchange/*) ;;
  /coingecko/exchanges) ;;
  /coingecko/gainers-losers) ;;
  /coingecko/global) ;;
  /coingecko/global/charts) ;;
  /coingecko/learn/articles) ;;
  /coingecko/markets) ;;
  /coingecko/new-coins) ;;
  /coingecko/news) ;;
  /coingecko/nft/category/*) ;;
  /coingecko/nfts) ;;
  /coingecko/search) ;;
  /coingecko/token-unlocks) ;;
  /coingecko/treasuries) ;;
  /coingecko/trending) ;;
  /congress/report) ;;
  /congress/stock-disclosures) ;;
  /pitchbook/advisor) ;;
  /pitchbook/company) ;;
  /pitchbook/fund) ;;
  /pitchbook/investor) ;;
  /pitchbook/limited-partner) ;;
  /sec/company/intelligence) ;;
  /sec/company/search) ;;
  /sec/company/submissions) ;;
  /sec/filing) ;;
  /sec/filing/sections) ;;
  /sec/financials) ;;
  /sec/frames) ;;
  /sec/full-text-search) ;;
  /sec/insider) ;;
  /sec/institutional-holdings) ;;
  /yahoo-finance/calendars) ;;
  /yahoo-finance/calendars/*) ;;
  /yahoo-finance/download) ;;
  /yahoo-finance/industries) ;;
  /yahoo-finance/industries/*) ;;
  /yahoo-finance/lookup) ;;
  /yahoo-finance/market/*/status) ;;
  /yahoo-finance/market/*/summary) ;;
  /yahoo-finance/screener) ;;
  /yahoo-finance/screener/*) ;;
  /yahoo-finance/screeners) ;;
  /yahoo-finance/search) ;;
  /yahoo-finance/sectors) ;;
  /yahoo-finance/sectors/*) ;;
  /yahoo-finance/ticker/*/actions) ;;
  /yahoo-finance/ticker/*/analysts) ;;
  /yahoo-finance/ticker/*/calendar) ;;
  /yahoo-finance/ticker/*/capital-gains) ;;
  /yahoo-finance/ticker/*/dividends) ;;
  /yahoo-finance/ticker/*/earnings) ;;
  /yahoo-finance/ticker/*/earnings-dates) ;;
  /yahoo-finance/ticker/*/financials) ;;
  /yahoo-finance/ticker/*/funds) ;;
  /yahoo-finance/ticker/*/history) ;;
  /yahoo-finance/ticker/*/history-metadata) ;;
  /yahoo-finance/ticker/*/holders) ;;
  /yahoo-finance/ticker/*/info) ;;
  /yahoo-finance/ticker/*/isin) ;;
  /yahoo-finance/ticker/*/news) ;;
  /yahoo-finance/ticker/*/options) ;;
  /yahoo-finance/ticker/*/options/*) ;;
  /yahoo-finance/ticker/*/quote) ;;
  /yahoo-finance/ticker/*/sec-filings) ;;
  /yahoo-finance/ticker/*/shares) ;;
  /yahoo-finance/ticker/*/shares-full) ;;
  /yahoo-finance/ticker/*/splits) ;;
  /yahoo-finance/ticker/*/sustainability) ;;
  /yahoo-finance/ticker/*/valuation) ;;
  /yahoo-finance/trending/*) ;;
  *)
    echo "path is not in the finance-markets-research skill catalog" >&2
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
