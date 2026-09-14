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
    echo "only GET and POST are supported by the product-price-research skill" >&2
    exit 2
    ;;
esac

# Reject path syntax that could smuggle a route through a shell glob check.
case "$path" in
  ""|*[?#%]*|*..*|*//* )
    echo "invalid path for the product-price-research skill" >&2
    exit 2
    ;;
esac

# Static routes use escaped case patterns. Parameterized routes use anchored
# extended regular expressions so every {param} is exactly one non-empty path
# segment; unlike a case '*', [^/]+ cannot consume another slash.
route_allowed=false
case "$path" in
  /adidas/product) route_allowed=true ;;
  /adidas/product/review-topics) route_allowed=true ;;
  /adidas/product/reviews) route_allowed=true ;;
  /adidas/search) route_allowed=true ;;
  /adidas/store) route_allowed=true ;;
  /adidas/stores) route_allowed=true ;;
  /adidas/suggest) route_allowed=true ;;
  /amazon/search) route_allowed=true ;;
  /bestbuy/brands) route_allowed=true ;;
  /bestbuy/categories) route_allowed=true ;;
  /bestbuy/categories/trending) route_allowed=true ;;
  /bestbuy/category) route_allowed=true ;;
  /bestbuy/category/subcategories) route_allowed=true ;;
  /bestbuy/product) route_allowed=true ;;
  /bestbuy/product/questions) route_allowed=true ;;
  /bestbuy/product/related) route_allowed=true ;;
  /bestbuy/product/reviews) route_allowed=true ;;
  /bestbuy/search) route_allowed=true ;;
  /bestbuy/stores) route_allowed=true ;;
  /bigcommerce/category) route_allowed=true ;;
  /bigcommerce/product) route_allowed=true ;;
  /bigcommerce/search) route_allowed=true ;;
  /boots/search) route_allowed=true ;;
  /boots/suggest) route_allowed=true ;;
  /chewy/brands) route_allowed=true ;;
  /chewy/categories) route_allowed=true ;;
  /chewy/category) route_allowed=true ;;
  /chewy/facets) route_allowed=true ;;
  /chewy/gtin-lookup) route_allowed=true ;;
  /chewy/inventory) route_allowed=true ;;
  /chewy/item-attributes) route_allowed=true ;;
  /chewy/product) route_allowed=true ;;
  /chewy/product-questions) route_allowed=true ;;
  /chewy/product-reviews) route_allowed=true ;;
  /chewy/products) route_allowed=true ;;
  /chewy/search) route_allowed=true ;;
  /chewy/suggest) route_allowed=true ;;
  /chewy/variants) route_allowed=true ;;
  /costco/categories) route_allowed=true ;;
  /costco/search) route_allowed=true ;;
  /costco/warehouses) route_allowed=true ;;
  /cvs/brands) route_allowed=true ;;
  /cvs/categories) route_allowed=true ;;
  /cvs/category) route_allowed=true ;;
  /cvs/search) route_allowed=true ;;
  /cvs/store-locator) route_allowed=true ;;
  /ebay/live/streams) route_allowed=true ;;
  /ebay/live/streams/batch) route_allowed=true ;;
  /ebay/search) route_allowed=true ;;
  /hm/categories) route_allowed=true ;;
  /hm/listing) route_allowed=true ;;
  /hm/search) route_allowed=true ;;
  /hm/search/suggestions) route_allowed=true ;;
  /hm/stores) route_allowed=true ;;
  /homedepot/categories) route_allowed=true ;;
  /homedepot/category) route_allowed=true ;;
  /homedepot/search) route_allowed=true ;;
  /homedepot/suggest) route_allowed=true ;;
  /ikea/availability) route_allowed=true ;;
  /ikea/category) route_allowed=true ;;
  /ikea/product) route_allowed=true ;;
  /ikea/reviews) route_allowed=true ;;
  /ikea/search) route_allowed=true ;;
  /ikea/store) route_allowed=true ;;
  /ikea/stores) route_allowed=true ;;
  /ikea/suggest) route_allowed=true ;;
  /kohls/category) route_allowed=true ;;
  /kohls/product/reviews) route_allowed=true ;;
  /kohls/stores) route_allowed=true ;;
  /kohls/suggest) route_allowed=true ;;
  /lazada/categories) route_allowed=true ;;
  /lazada/category-products) route_allowed=true ;;
  /lazada/home) route_allowed=true ;;
  /lazada/product) route_allowed=true ;;
  /lazada/search) route_allowed=true ;;
  /lululemon/categories) route_allowed=true ;;
  /lululemon/category) route_allowed=true ;;
  /lululemon/outfit) route_allowed=true ;;
  /lululemon/stores) route_allowed=true ;;
  /macys/product/reviews) route_allowed=true ;;
  /macys/suggest) route_allowed=true ;;
  /nike/categories) route_allowed=true ;;
  /nike/product) route_allowed=true ;;
  /nike/product/availability) route_allowed=true ;;
  /nike/product/details) route_allowed=true ;;
  /nike/product/recommendations) route_allowed=true ;;
  /nike/product/reviews) route_allowed=true ;;
  /nike/search) route_allowed=true ;;
  /nike/stores) route_allowed=true ;;
  /nike/suggest) route_allowed=true ;;
  /oldnavy/categories) route_allowed=true ;;
  /oldnavy/category) route_allowed=true ;;
  /oldnavy/product) route_allowed=true ;;
  /oldnavy/product/availability) route_allowed=true ;;
  /oldnavy/product/reviews) route_allowed=true ;;
  /oldnavy/search) route_allowed=true ;;
  /oldnavy/stores) route_allowed=true ;;
  /otto/categories) route_allowed=true ;;
  /otto/product) route_allowed=true ;;
  /otto/search) route_allowed=true ;;
  /samsclub/category) route_allowed=true ;;
  /samsclub/departments) route_allowed=true ;;
  /sephora/category) route_allowed=true ;;
  /sephora/product) route_allowed=true ;;
  /sephora/product/questions) route_allowed=true ;;
  /sephora/product/reviews) route_allowed=true ;;
  /sephora/search) route_allowed=true ;;
  /sephora/stores) route_allowed=true ;;
  /sephora/suggest) route_allowed=true ;;
  /shein/category/filters) route_allowed=true ;;
  /shein/category/goods) route_allowed=true ;;
  /shein/category/nav) route_allowed=true ;;
  /shein/products/aggregation-filters) route_allowed=true ;;
  /shein/products/detail) route_allowed=true ;;
  /shein/products/search) route_allowed=true ;;
  /shein/search/autocomplete) route_allowed=true ;;
  /shein/search/keywords) route_allowed=true ;;
  /shop-app/analysis) route_allowed=true ;;
  /shop-app/categories) route_allowed=true ;;
  /shop-app/search) route_allowed=true ;;
  /shop-app/suggestions) route_allowed=true ;;
  /shopify/collections) route_allowed=true ;;
  /shopify/pages) route_allowed=true ;;
  /shopify/products) route_allowed=true ;;
  /shopify/search/suggest) route_allowed=true ;;
  /shopify/sitemap/urls) route_allowed=true ;;
  /shopify/sitemaps) route_allowed=true ;;
  /shopify/store) route_allowed=true ;;
  /sparkfun/categories) route_allowed=true ;;
  /sparkfun/category) route_allowed=true ;;
  /sparkfun/product) route_allowed=true ;;
  /sparkfun/search) route_allowed=true ;;
  /target/categories) route_allowed=true ;;
  /target/category-products) route_allowed=true ;;
  /target/filter-options) route_allowed=true ;;
  /target/product) route_allowed=true ;;
  /target/questions) route_allowed=true ;;
  /target/reviews) route_allowed=true ;;
  /target/search) route_allowed=true ;;
  /tokopedia/autocomplete) route_allowed=true ;;
  /tokopedia/category) route_allowed=true ;;
  /tokopedia/home) route_allowed=true ;;
  /tokopedia/home/tabs) route_allowed=true ;;
  /tokopedia/product) route_allowed=true ;;
  /tokopedia/product/review-filters) route_allowed=true ;;
  /tokopedia/search) route_allowed=true ;;
  /tokopedia/search/filters) route_allowed=true ;;
  /ulta/categories) route_allowed=true ;;
  /ulta/category) route_allowed=true ;;
  /ulta/product/questions) route_allowed=true ;;
  /ulta/product/reviews) route_allowed=true ;;
  /ulta/search) route_allowed=true ;;
  /ulta/stores) route_allowed=true ;;
  /ulta/suggest) route_allowed=true ;;
  /walgreens/stores) route_allowed=true ;;
  /walmart/search) route_allowed=true ;;
  /wayfair/categories) route_allowed=true ;;
  /wayfair/category) route_allowed=true ;;
  /wish/categories) route_allowed=true ;;
  /wish/search) route_allowed=true ;;
  /wish/suggest) route_allowed=true ;;
  /zalando/category) route_allowed=true ;;
  /zalando/markets) route_allowed=true ;;
  /zalando/product) route_allowed=true ;;
  /zalando/search) route_allowed=true ;;
  /zalando/suggest) route_allowed=true ;;
  /zappos/brand) route_allowed=true ;;
  /zappos/brands) route_allowed=true ;;
  /zappos/search) route_allowed=true ;;
  /zappos/suggest) route_allowed=true ;;
  /zara/categories) route_allowed=true ;;
  /zara/search) route_allowed=true ;;
  /zara/stores) route_allowed=true ;;
  /zara/suggest) route_allowed=true ;;
esac
if [ "$route_allowed" = false ]; then
  route_regexes=(
  '^/amazon/product/[^/]+$'
  '^/amazon/suggest/[^/]+$'
  '^/costco/product/[^/]+$'
  '^/costco/product/[^/]+/availability$'
  '^/costco/product/[^/]+/reviews$'
  '^/cvs/product-ingredients/[^/]+$'
  '^/cvs/product/[^/]+$'
  '^/ebay/item/[^/]+$'
  '^/ebay/live/streams/[^/]+$'
  '^/ebay/live/streams/[^/]+/items$'
  '^/ebay/seller/[^/]+$'
  '^/ebay/seller/[^/]+/about$'
  '^/ebay/seller/[^/]+/feedback$'
  '^/ebay/seller/[^/]+/shop$'
  '^/hm/product/[^/]+$'
  '^/hm/product/[^/]+/related$'
  '^/homedepot/product/[^/]+$'
  '^/homedepot/product/[^/]+/questions$'
  '^/lululemon/product/[^/]+$'
  '^/macys/product/[^/]+$'
  '^/samsclub/content/[^/]+$'
  '^/samsclub/product/[^/]+$'
  '^/samsclub/product/[^/]+/related$'
  '^/shop-app/products/[^/]+$'
  '^/shop-app/products/[^/]+/related$'
  '^/shop-app/products/[^/]+/reviews$'
  '^/shop-app/products/[^/]+/shop$'
  '^/shop-app/products/[^/]+/variant$'
  '^/shop-app/products/[^/]+/variants$'
  '^/shop-app/shops/[^/]+$'
  '^/shop-app/shops/[^/]+/collections/[^/]+/products$'
  '^/shop-app/shops/[^/]+/locations$'
  '^/shop-app/shops/[^/]+/products$'
  '^/shop-app/shops/[^/]+/reviews$'
  '^/shop-app/shops/[^/]+/typeahead$'
  '^/shopify/collections/[^/]+/products$'
  '^/shopify/pages/[^/]+$'
  '^/shopify/products/[^/]+$'
  '^/shopify/products/[^/]+/recommendations$'
  '^/ulta/product/[^/]+$'
  '^/walmart/product/[^/]+$'
  '^/walmart/product/[^/]+/reviews$'
  '^/wayfair/product/[^/]+$'
  '^/wish/product/[^/]+$'
  '^/wish/product/[^/]+/related$'
  '^/wish/product/[^/]+/reviews$'
  '^/zappos/product/[^/]+$'
  '^/zara/category/[^/]+/products$'
  '^/zara/product/[^/]+$'
  )
  for route_regex in ${route_regexes[@]+"${route_regexes[@]}"}; do
    if [[ "$path" =~ $route_regex ]]; then
      route_allowed=true
      break
    fi
  done
fi
if [ "$route_allowed" = false ]; then
  echo "path is not in the product-price-research skill catalog" >&2
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
