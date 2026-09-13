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
    echo "only GET and POST are supported by the restaurant-food-delivery-research skill" >&2
    exit 2
    ;;
esac

# Reject path syntax that could smuggle a route through a shell glob check.
case "$path" in
  ""|*[?#%]*|*..*|*//* )
    echo "invalid path for the restaurant-food-delivery-research skill" >&2
    exit 2
    ;;
esac
case "$path" in
  /7now/catalog) ;;
  /7now/categories) ;;
  /7now/category) ;;
  /7now/combo) ;;
  /7now/combos) ;;
  /7now/deals) ;;
  /7now/offers) ;;
  /7now/popular) ;;
  /7now/product) ;;
  /7now/promotion) ;;
  /7now/search) ;;
  /7now/stores) ;;
  /7now/suggest) ;;
  /arbys/categories) ;;
  /arbys/directory) ;;
  /arbys/location) ;;
  /arbys/locations) ;;
  /arbys/menu) ;;
  /burgerking/availability) ;;
  /burgerking/locations) ;;
  /burgerking/menu) ;;
  /burgerking/product) ;;
  /chick-fil-a/content) ;;
  /chick-fil-a/content-taxonomy) ;;
  /chick-fil-a/faq) ;;
  /chick-fil-a/location) ;;
  /chick-fil-a/locations) ;;
  /chick-fil-a/menu) ;;
  /chick-fil-a/menu-item) ;;
  /chick-fil-a/menu-taxonomy) ;;
  /chipotle/ingredients) ;;
  /chipotle/meals) ;;
  /chipotle/menu) ;;
  /chipotle/menu/metadata) ;;
  /chipotle/restaurant) ;;
  /chipotle/restaurant/meals) ;;
  /chipotle/restaurant/menu) ;;
  /chipotle/restaurants) ;;
  /culvers/calendar) ;;
  /culvers/categories) ;;
  /culvers/directory) ;;
  /culvers/flavor) ;;
  /culvers/item) ;;
  /culvers/menu) ;;
  /culvers/store) ;;
  /deliveroo/fulfillment-times) ;;
  /deliveroo/restaurant) ;;
  /deliveroo/restaurant/menu) ;;
  /deliveroo/search) ;;
  /deliveroo/search/filters) ;;
  /dominos/coupons) ;;
  /dominos/customization) ;;
  /dominos/menu) ;;
  /dominos/nutrition) ;;
  /dominos/store) ;;
  /dominos/store-locator) ;;
  /doordash/explore) ;;
  /doordash/feed) ;;
  /doordash/search) ;;
  /doordash/search/autocomplete) ;;
  /doordash/search/filters) ;;
  /doordash/search/items) ;;
  /doordash/store/*) ;;
  /doordash/store/*/fulfillment) ;;
  /doordash/store/*/info) ;;
  /doordash/store/*/item/*) ;;
  /doordash/store/*/menu) ;;
  /doordash/store/*/reviews) ;;
  /dunkin/directory) ;;
  /dunkin/menu) ;;
  /dunkin/nearby) ;;
  /dunkin/store) ;;
  /fiveguys/directory) ;;
  /fiveguys/faq) ;;
  /fiveguys/faq-categories) ;;
  /fiveguys/menu) ;;
  /fiveguys/nearby) ;;
  /fiveguys/nutrition) ;;
  /fiveguys/ordering-locations) ;;
  /fiveguys/ordering-menu) ;;
  /fiveguys/search) ;;
  /fiveguys/store) ;;
  /foodpanda/restaurant) ;;
  /foodpanda/restaurant/menu) ;;
  /foodpanda/restaurant/reviews) ;;
  /foodpanda/search) ;;
  /grubhub/availability) ;;
  /grubhub/offers) ;;
  /grubhub/restaurant) ;;
  /grubhub/restaurant/menu) ;;
  /grubhub/restaurant/reviews) ;;
  /grubhub/search) ;;
  /grubhub/timepicker) ;;
  /instacart/departments) ;;
  /instacart/item) ;;
  /instacart/search) ;;
  /instacart/search-nearby) ;;
  /instacart/stores) ;;
  /instacart/trending) ;;
  /jimmy-johns/menu) ;;
  /jimmy-johns/modifiers) ;;
  /jimmy-johns/nearby) ;;
  /jimmy-johns/sitemap) ;;
  /jimmy-johns/store) ;;
  /justeat/restaurant) ;;
  /justeat/restaurant/menu) ;;
  /justeat/search) ;;
  /kfc/delivery-estimate) ;;
  /kfc/menu) ;;
  /kfc/nearby) ;;
  /kfc/promotion) ;;
  /kfc/promotions) ;;
  /kfc/store) ;;
  /kfc/stores) ;;
  /kroger/category) ;;
  /kroger/coupons) ;;
  /kroger/product) ;;
  /kroger/product/reviews) ;;
  /kroger/products) ;;
  /kroger/related-tags) ;;
  /kroger/search) ;;
  /kroger/store) ;;
  /kroger/suggest) ;;
  /mcdonalds/categories) ;;
  /mcdonalds/item) ;;
  /mcdonalds/item-list) ;;
  /mcdonalds/menu) ;;
  /mcdonalds/restaurant-menu) ;;
  /mcdonalds/restaurants) ;;
  /opentable/restaurant) ;;
  /opentable/restaurant/menus) ;;
  /opentable/restaurant/reviews) ;;
  /opentable/search) ;;
  /pandamart/search) ;;
  /pandamart/store) ;;
  /pandamart/store/categories) ;;
  /pandamart/store/product) ;;
  /pandamart/store/products) ;;
  /pandamart/store/search) ;;
  /panera/at-work-locations) ;;
  /panera/cafe) ;;
  /panera/catering-delivery-info) ;;
  /panera/catering-menu) ;;
  /panera/geocode) ;;
  /panera/item-detail) ;;
  /panera/item-options) ;;
  /panera/locations) ;;
  /panera/menu) ;;
  /panera/quantity-rules) ;;
  /panera/retired-products) ;;
  /panera/time-slots) ;;
  /panera/upsell-suggestions) ;;
  /papajohns/allergens) ;;
  /papajohns/colombia/menu) ;;
  /papajohns/deals) ;;
  /papajohns/directory) ;;
  /papajohns/elsalvador/menu) ;;
  /papajohns/india/deal) ;;
  /papajohns/india/menu) ;;
  /papajohns/india/menu/item) ;;
  /papajohns/india/stores) ;;
  /papajohns/intl/deals) ;;
  /papajohns/intl/ingredients) ;;
  /papajohns/intl/menu) ;;
  /papajohns/intl/offer) ;;
  /papajohns/intl/product) ;;
  /papajohns/intl/stores) ;;
  /papajohns/menu) ;;
  /papajohns/menu/item) ;;
  /papajohns/nearby) ;;
  /papajohns/nutrition) ;;
  /papajohns/peru/menu) ;;
  /papajohns/poland/menu) ;;
  /papajohns/russia/menu) ;;
  /papajohns/store) ;;
  /pizzahut/bundle-choices) ;;
  /pizzahut/delivery-estimate) ;;
  /pizzahut/menu) ;;
  /pizzahut/modifiers) ;;
  /pizzahut/store) ;;
  /pizzahut/stores) ;;
  /popeyes/faq) ;;
  /popeyes/location) ;;
  /popeyes/locations) ;;
  /popeyes/menu) ;;
  /popeyes/offers) ;;
  /popeyes/promotions) ;;
  /popeyes/quests) ;;
  /popeyes/rewards) ;;
  /raisingcanes/directory) ;;
  /raisingcanes/menu) ;;
  /raisingcanes/nearby) ;;
  /raisingcanes/promotion) ;;
  /raisingcanes/promotions) ;;
  /raisingcanes/store) ;;
  /shakeshack/locations) ;;
  /shakeshack/menu) ;;
  /shakeshack/nearby) ;;
  /shakeshack/store) ;;
  /sonic/availability) ;;
  /sonic/categories) ;;
  /sonic/deals) ;;
  /sonic/directory) ;;
  /sonic/item) ;;
  /sonic/location-suggest) ;;
  /sonic/locations) ;;
  /sonic/menu) ;;
  /sonic/nearby) ;;
  /sonic/nutrition-documents) ;;
  /sonic/sitemap) ;;
  /sonic/store) ;;
  /starbucks/menu) ;;
  /starbucks/nearest-store) ;;
  /starbucks/product/*/*) ;;
  /starbucks/product/*/*/nutrition) ;;
  /starbucks/stores) ;;
  /subway/available-times) ;;
  /subway/combos) ;;
  /subway/menu) ;;
  /subway/nearby) ;;
  /subway/sitemap) ;;
  /subway/store) ;;
  /swiggy/collections) ;;
  /swiggy/restaurant) ;;
  /swiggy/restaurant/menu) ;;
  /swiggy/search) ;;
  /taco-bell/app-menu) ;;
  /taco-bell/categories) ;;
  /taco-bell/menu) ;;
  /taco-bell/nutrition) ;;
  /taco-bell/product) ;;
  /taco-bell/store) ;;
  /taco-bell/store-menu) ;;
  /taco-bell/stores) ;;
  /ubereats/feed) ;;
  /ubereats/search) ;;
  /ubereats/store/*) ;;
  /ubereats/store/*/menu) ;;
  /ubereats/store/*/reviews) ;;
  /wendys/categories) ;;
  /wendys/directory) ;;
  /wendys/item) ;;
  /wendys/menu) ;;
  /wendys/nearby) ;;
  /wendys/nutrition) ;;
  /wendys/restaurant) ;;
  /wendys/store) ;;
  /wendys/store-menu) ;;
  /wendys/time-slots) ;;
  /whataburger/sitemap) ;;
  /whataburger/store) ;;
  /wingstop/delivery-store) ;;
  /wingstop/directory) ;;
  /wingstop/flavors) ;;
  /wingstop/menu) ;;
  /wingstop/nearby) ;;
  /wingstop/store) ;;
  /wolt/cities) ;;
  /wolt/collections) ;;
  /wolt/restaurant) ;;
  /wolt/restaurant/availability) ;;
  /wolt/restaurant/menu) ;;
  /wolt/restaurant/menu/search) ;;
  /wolt/search) ;;
  /wolt/search/filters) ;;
  /yelp/business/*) ;;
  /yelp/business/*/menu) ;;
  /yelp/business/*/photos) ;;
  /yelp/business/*/reviews) ;;
  /yelp/business/*/reviews/highlights) ;;
  /yelp/business/*/reviews/search) ;;
  /yelp/geocode) ;;
  /yelp/search) ;;
  /zaxbys/menu) ;;
  /zaxbys/nearby) ;;
  /zaxbys/store) ;;
  /zomato/collection) ;;
  /zomato/collections) ;;
  /zomato/restaurant) ;;
  /zomato/restaurant/menu) ;;
  /zomato/search) ;;
  *)
    echo "path is not in the restaurant-food-delivery-research skill catalog" >&2
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
