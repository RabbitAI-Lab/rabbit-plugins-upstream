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
    echo "only GET and POST are supported by the shopify-research skill" >&2
    exit 2
    ;;
esac

# Reject path syntax that could smuggle a route through a shell glob check.
case "$path" in
  ""|*[?#%]*|*..*|*//* )
    echo "invalid path for the shopify-research skill" >&2
    exit 2
    ;;
esac
case "$path" in
  /allbirds/collections) ;;
  /allbirds/collections/*/products) ;;
  /allbirds/pages) ;;
  /allbirds/pages/*) ;;
  /allbirds/products) ;;
  /allbirds/products/*) ;;
  /allbirds/products/*/recommendations) ;;
  /allbirds/search/suggest) ;;
  /allbirds/sitemap/urls) ;;
  /allbirds/sitemaps) ;;
  /allbirds/store) ;;
  /brooklinen/collections) ;;
  /brooklinen/collections/*/products) ;;
  /brooklinen/pages) ;;
  /brooklinen/pages/*) ;;
  /brooklinen/products) ;;
  /brooklinen/products/*) ;;
  /brooklinen/products/*/recommendations) ;;
  /brooklinen/search/suggest) ;;
  /brooklinen/sitemap/urls) ;;
  /brooklinen/sitemaps) ;;
  /brooklinen/store) ;;
  /colehaan/collections) ;;
  /colehaan/collections/*/products) ;;
  /colehaan/pages) ;;
  /colehaan/pages/*) ;;
  /colehaan/products) ;;
  /colehaan/products/*) ;;
  /colehaan/products/*/recommendations) ;;
  /colehaan/search/suggest) ;;
  /colehaan/sitemap/urls) ;;
  /colehaan/sitemaps) ;;
  /colehaan/store) ;;
  /everlane/collections) ;;
  /everlane/collections/*/products) ;;
  /everlane/pages) ;;
  /everlane/pages/*) ;;
  /everlane/products) ;;
  /everlane/products/*) ;;
  /everlane/products/*/recommendations) ;;
  /everlane/search/suggest) ;;
  /everlane/sitemap/urls) ;;
  /everlane/sitemaps) ;;
  /everlane/store) ;;
  /fashionnova/collections) ;;
  /fashionnova/collections/*/products) ;;
  /fashionnova/pages) ;;
  /fashionnova/pages/*) ;;
  /fashionnova/products) ;;
  /fashionnova/products/*) ;;
  /fashionnova/products/*/recommendations) ;;
  /fashionnova/search/suggest) ;;
  /fashionnova/sitemap/urls) ;;
  /fashionnova/sitemaps) ;;
  /fashionnova/store) ;;
  /gymshark/collections) ;;
  /gymshark/collections/*/products) ;;
  /gymshark/pages) ;;
  /gymshark/pages/*) ;;
  /gymshark/products) ;;
  /gymshark/products/*) ;;
  /gymshark/products/*/recommendations) ;;
  /gymshark/sitemap/urls) ;;
  /gymshark/sitemaps) ;;
  /gymshark/store) ;;
  /jcrew/categories) ;;
  /jcrew/category) ;;
  /jcrew/product) ;;
  /jcrew/product/reviews) ;;
  /jcrew/search) ;;
  /jcrew/size-chart) ;;
  /jcrew/stores) ;;
  /jcrew/suggest) ;;
  /kyliecosmetics/collections) ;;
  /kyliecosmetics/collections/*/products) ;;
  /kyliecosmetics/pages) ;;
  /kyliecosmetics/pages/*) ;;
  /kyliecosmetics/products) ;;
  /kyliecosmetics/products/*) ;;
  /kyliecosmetics/products/*/recommendations) ;;
  /kyliecosmetics/search/suggest) ;;
  /kyliecosmetics/sitemap/urls) ;;
  /kyliecosmetics/sitemaps) ;;
  /kyliecosmetics/store) ;;
  /ohpolly/collections) ;;
  /ohpolly/collections/*/products) ;;
  /ohpolly/pages) ;;
  /ohpolly/pages/*) ;;
  /ohpolly/products) ;;
  /ohpolly/products/*) ;;
  /ohpolly/products/*/recommendations) ;;
  /ohpolly/search/suggest) ;;
  /ohpolly/sitemap/urls) ;;
  /ohpolly/sitemaps) ;;
  /ohpolly/store) ;;
  /quince/categories) ;;
  /quince/navigation) ;;
  /quince/product) ;;
  /quince/product/faq) ;;
  /quince/product/reviews) ;;
  /quince/search) ;;
  /quince/sitemap/urls) ;;
  /quince/sitemaps) ;;
  /quince/suggest) ;;
  /rothys/collections) ;;
  /rothys/collections/*/products) ;;
  /rothys/pages) ;;
  /rothys/pages/*) ;;
  /rothys/products) ;;
  /rothys/products/*) ;;
  /rothys/products/*/recommendations) ;;
  /rothys/search/suggest) ;;
  /rothys/sitemap/urls) ;;
  /rothys/sitemaps) ;;
  /rothys/store) ;;
  /shopify/collections) ;;
  /shopify/collections/*/products) ;;
  /shopify/pages) ;;
  /shopify/pages/*) ;;
  /shopify/products) ;;
  /shopify/products/*) ;;
  /shopify/products/*/recommendations) ;;
  /shopify/search/suggest) ;;
  /shopify/sitemap/urls) ;;
  /shopify/sitemaps) ;;
  /shopify/store) ;;
  /skims/collections) ;;
  /skims/collections/*/products) ;;
  /skims/pages) ;;
  /skims/pages/*) ;;
  /skims/products) ;;
  /skims/products/*) ;;
  /skims/products/*/recommendations) ;;
  /skims/search/suggest) ;;
  /skims/sitemap/urls) ;;
  /skims/sitemaps) ;;
  /skims/store) ;;
  /stevemadden/collections) ;;
  /stevemadden/collections/*/products) ;;
  /stevemadden/pages) ;;
  /stevemadden/pages/*) ;;
  /stevemadden/products) ;;
  /stevemadden/products/*) ;;
  /stevemadden/products/*/recommendations) ;;
  /stevemadden/search/suggest) ;;
  /stevemadden/sitemap/urls) ;;
  /stevemadden/sitemaps) ;;
  /stevemadden/store) ;;
  /thebodyshop/collections) ;;
  /thebodyshop/collections/*/products) ;;
  /thebodyshop/pages) ;;
  /thebodyshop/pages/*) ;;
  /thebodyshop/products) ;;
  /thebodyshop/products/*) ;;
  /thebodyshop/products/*/recommendations) ;;
  /thebodyshop/search/suggest) ;;
  /thebodyshop/sitemap/urls) ;;
  /thebodyshop/sitemaps) ;;
  /thebodyshop/store) ;;
  *)
    echo "path is not in the shopify-research skill catalog" >&2
    exit 2
    ;;
esac



auth=(-H "x-api-key: ${CRAWLORA_API_KEY}")

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
