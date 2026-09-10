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
case "$path" in
  /adidas/product) ;;
  /adidas/product/review-topics) ;;
  /adidas/product/reviews) ;;
  /adidas/search) ;;
  /adidas/store) ;;
  /adidas/stores) ;;
  /adidas/suggest) ;;
  /amazon/product/*) ;;
  /amazon/search) ;;
  /amazon/suggest/*) ;;
  /bestbuy/brands) ;;
  /bestbuy/categories) ;;
  /bestbuy/categories/trending) ;;
  /bestbuy/category) ;;
  /bestbuy/category/subcategories) ;;
  /bestbuy/product) ;;
  /bestbuy/product/questions) ;;
  /bestbuy/product/related) ;;
  /bestbuy/product/reviews) ;;
  /bestbuy/search) ;;
  /bestbuy/stores) ;;
  /bigcommerce/category) ;;
  /bigcommerce/product) ;;
  /bigcommerce/search) ;;
  /boots/search) ;;
  /boots/suggest) ;;
  /chewy/brands) ;;
  /chewy/categories) ;;
  /chewy/category) ;;
  /chewy/facets) ;;
  /chewy/gtin-lookup) ;;
  /chewy/inventory) ;;
  /chewy/item-attributes) ;;
  /chewy/product) ;;
  /chewy/product-questions) ;;
  /chewy/product-reviews) ;;
  /chewy/products) ;;
  /chewy/search) ;;
  /chewy/suggest) ;;
  /chewy/variants) ;;
  /costco/categories) ;;
  /costco/product/*) ;;
  /costco/product/*/availability) ;;
  /costco/product/*/reviews) ;;
  /costco/search) ;;
  /costco/warehouses) ;;
  /cvs/brands) ;;
  /cvs/categories) ;;
  /cvs/category) ;;
  /cvs/product-ingredients/*) ;;
  /cvs/product/*) ;;
  /cvs/search) ;;
  /cvs/store-locator) ;;
  /ebay/item/*) ;;
  /ebay/live/streams) ;;
  /ebay/live/streams/*) ;;
  /ebay/live/streams/*/items) ;;
  /ebay/live/streams/batch) ;;
  /ebay/search) ;;
  /ebay/seller/*) ;;
  /ebay/seller/*/about) ;;
  /ebay/seller/*/feedback) ;;
  /ebay/seller/*/shop) ;;
  /hm/categories) ;;
  /hm/listing) ;;
  /hm/product/*) ;;
  /hm/product/*/related) ;;
  /hm/search) ;;
  /hm/search/suggestions) ;;
  /hm/stores) ;;
  /homedepot/categories) ;;
  /homedepot/category) ;;
  /homedepot/product/*) ;;
  /homedepot/product/*/questions) ;;
  /homedepot/search) ;;
  /homedepot/suggest) ;;
  /ikea/availability) ;;
  /ikea/category) ;;
  /ikea/product) ;;
  /ikea/reviews) ;;
  /ikea/search) ;;
  /ikea/store) ;;
  /ikea/stores) ;;
  /ikea/suggest) ;;
  /kohls/category) ;;
  /kohls/product/reviews) ;;
  /kohls/stores) ;;
  /kohls/suggest) ;;
  /lazada/categories) ;;
  /lazada/category-products) ;;
  /lazada/home) ;;
  /lazada/product) ;;
  /lazada/search) ;;
  /lululemon/categories) ;;
  /lululemon/category) ;;
  /lululemon/outfit) ;;
  /lululemon/product/*) ;;
  /lululemon/stores) ;;
  /macys/product/*) ;;
  /macys/product/reviews) ;;
  /macys/suggest) ;;
  /nike/categories) ;;
  /nike/product) ;;
  /nike/product/availability) ;;
  /nike/product/details) ;;
  /nike/product/recommendations) ;;
  /nike/product/reviews) ;;
  /nike/search) ;;
  /nike/stores) ;;
  /nike/suggest) ;;
  /oldnavy/categories) ;;
  /oldnavy/category) ;;
  /oldnavy/product) ;;
  /oldnavy/product/availability) ;;
  /oldnavy/product/reviews) ;;
  /oldnavy/search) ;;
  /oldnavy/stores) ;;
  /otto/categories) ;;
  /otto/product) ;;
  /otto/search) ;;
  /samsclub/category) ;;
  /samsclub/content/*) ;;
  /samsclub/departments) ;;
  /samsclub/product/*) ;;
  /samsclub/product/*/related) ;;
  /sephora/category) ;;
  /sephora/product) ;;
  /sephora/product/questions) ;;
  /sephora/product/reviews) ;;
  /sephora/search) ;;
  /sephora/stores) ;;
  /sephora/suggest) ;;
  /shein/category/filters) ;;
  /shein/category/goods) ;;
  /shein/category/nav) ;;
  /shein/products/aggregation-filters) ;;
  /shein/products/detail) ;;
  /shein/products/search) ;;
  /shein/search/autocomplete) ;;
  /shein/search/keywords) ;;
  /shop-app/analysis) ;;
  /shop-app/categories) ;;
  /shop-app/products/*) ;;
  /shop-app/products/*/related) ;;
  /shop-app/products/*/reviews) ;;
  /shop-app/products/*/shop) ;;
  /shop-app/products/*/variant) ;;
  /shop-app/products/*/variants) ;;
  /shop-app/search) ;;
  /shop-app/shops/*) ;;
  /shop-app/shops/*/collections/*/products) ;;
  /shop-app/shops/*/locations) ;;
  /shop-app/shops/*/products) ;;
  /shop-app/shops/*/reviews) ;;
  /shop-app/shops/*/typeahead) ;;
  /shop-app/suggestions) ;;
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
  /sparkfun/categories) ;;
  /sparkfun/category) ;;
  /sparkfun/product) ;;
  /sparkfun/search) ;;
  /target/categories) ;;
  /target/category-products) ;;
  /target/filter-options) ;;
  /target/product) ;;
  /target/questions) ;;
  /target/reviews) ;;
  /target/search) ;;
  /tokopedia/autocomplete) ;;
  /tokopedia/category) ;;
  /tokopedia/home) ;;
  /tokopedia/home/tabs) ;;
  /tokopedia/product) ;;
  /tokopedia/product/review-filters) ;;
  /tokopedia/search) ;;
  /tokopedia/search/filters) ;;
  /ulta/categories) ;;
  /ulta/category) ;;
  /ulta/product/*) ;;
  /ulta/product/questions) ;;
  /ulta/product/reviews) ;;
  /ulta/search) ;;
  /ulta/stores) ;;
  /ulta/suggest) ;;
  /walgreens/stores) ;;
  /walmart/product/*) ;;
  /walmart/product/*/reviews) ;;
  /walmart/search) ;;
  /wayfair/categories) ;;
  /wayfair/category) ;;
  /wayfair/product/*) ;;
  /wish/categories) ;;
  /wish/product/*) ;;
  /wish/product/*/related) ;;
  /wish/product/*/reviews) ;;
  /wish/search) ;;
  /wish/suggest) ;;
  /zalando/category) ;;
  /zalando/markets) ;;
  /zalando/product) ;;
  /zalando/search) ;;
  /zalando/suggest) ;;
  /zappos/brand) ;;
  /zappos/brands) ;;
  /zappos/product/*) ;;
  /zappos/search) ;;
  /zappos/suggest) ;;
  /zara/categories) ;;
  /zara/category/*/products) ;;
  /zara/product/*) ;;
  /zara/search) ;;
  /zara/stores) ;;
  /zara/suggest) ;;
  *)
    echo "path is not in the product-price-research skill catalog" >&2
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
