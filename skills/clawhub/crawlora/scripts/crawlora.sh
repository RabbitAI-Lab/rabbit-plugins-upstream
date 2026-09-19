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
    -X)
      [ $# -ge 2 ] || { echo "-X requires an HTTP method" >&2; exit 2; }
      method="$2"; shift 2 ;;
    -d)
      [ $# -ge 2 ] || { echo "-d requires a request body" >&2; exit 2; }
      body="$2"; shift 2 ;;
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
    echo "only GET and POST are supported by the crawlora skill" >&2
    exit 2
    ;;
esac

# Reject path syntax that could smuggle a route through a shell glob check.
case "$path" in
  ""|*[?#%]*|*..*|*//* )
    echo "invalid path for the crawlora skill" >&2
    exit 2
    ;;
esac

# Static routes use escaped case patterns. Parameterized routes use anchored
# extended regular expressions so every {param} is exactly one non-empty path
# segment; unlike a case '*', [^/]+ cannot consume another slash.
route_allowed=false
case "$path" in
  /7now/catalog) route_allowed=true ;;
  /7now/categories) route_allowed=true ;;
  /7now/category) route_allowed=true ;;
  /7now/combo) route_allowed=true ;;
  /7now/combos) route_allowed=true ;;
  /7now/deals) route_allowed=true ;;
  /7now/offers) route_allowed=true ;;
  /7now/popular) route_allowed=true ;;
  /7now/product) route_allowed=true ;;
  /7now/promotion) route_allowed=true ;;
  /7now/search) route_allowed=true ;;
  /7now/stores) route_allowed=true ;;
  /7now/suggest) route_allowed=true ;;
  /accor/amenities) route_allowed=true ;;
  /accor/brands) route_allowed=true ;;
  /accor/catalog/hotels) route_allowed=true ;;
  /accor/destination/hotels) route_allowed=true ;;
  /accor/property) route_allowed=true ;;
  /accor/search) route_allowed=true ;;
  /accor/search/details) route_allowed=true ;;
  /accor/search/suggest) route_allowed=true ;;
  /adidas/product) route_allowed=true ;;
  /adidas/product/review-topics) route_allowed=true ;;
  /adidas/product/reviews) route_allowed=true ;;
  /adidas/search) route_allowed=true ;;
  /adidas/store) route_allowed=true ;;
  /adidas/stores) route_allowed=true ;;
  /adidas/suggest) route_allowed=true ;;
  /agoda/activities/search) route_allowed=true ;;
  /agoda/flights/itinerary-amenities) route_allowed=true ;;
  /agoda/flights/search) route_allowed=true ;;
  /agoda/flights/search-locations) route_allowed=true ;;
  /agoda/homes/search) route_allowed=true ;;
  /agoda/hotels/search) route_allowed=true ;;
  /airbnb/search) route_allowed=true ;;
  /allbirds/collections) route_allowed=true ;;
  /allbirds/pages) route_allowed=true ;;
  /allbirds/products) route_allowed=true ;;
  /allbirds/search/suggest) route_allowed=true ;;
  /allbirds/sitemap/urls) route_allowed=true ;;
  /allbirds/sitemaps) route_allowed=true ;;
  /allbirds/store) route_allowed=true ;;
  /amazon-jobs/job) route_allowed=true ;;
  /amazon-jobs/search) route_allowed=true ;;
  /amazon/search) route_allowed=true ;;
  /anime/airing-schedule) route_allowed=true ;;
  /anime/character/search) route_allowed=true ;;
  /anime/rankings) route_allowed=true ;;
  /anime/search) route_allowed=true ;;
  /apple-books/audiobook/search) route_allowed=true ;;
  /apple-books/charts) route_allowed=true ;;
  /apple-books/search) route_allowed=true ;;
  /apple-jobs/job) route_allowed=true ;;
  /apple-jobs/search) route_allowed=true ;;
  /apple-maps/autocomplete) route_allowed=true ;;
  /apple-maps/categories) route_allowed=true ;;
  /apple-maps/category-search) route_allowed=true ;;
  /apple-maps/directions) route_allowed=true ;;
  /apple-maps/eta) route_allowed=true ;;
  /apple-maps/guides) route_allowed=true ;;
  /apple-maps/guides/cities) route_allowed=true ;;
  /apple-maps/guides/guide) route_allowed=true ;;
  /apple-maps/guides/lookup) route_allowed=true ;;
  /apple-maps/guides/nearby) route_allowed=true ;;
  /apple-maps/guides/publisher) route_allowed=true ;;
  /apple-maps/guides/publishers) route_allowed=true ;;
  /apple-maps/place) route_allowed=true ;;
  /apple-maps/place/photos) route_allowed=true ;;
  /apple-maps/places) route_allowed=true ;;
  /apple-maps/reverse-geocode) route_allowed=true ;;
  /apple-maps/search) route_allowed=true ;;
  /apple-maps/transit-departures) route_allowed=true ;;
  /apple-maps/venue/browse) route_allowed=true ;;
  /apple-podcasts/charts) route_allowed=true ;;
  /apple-podcasts/charts/rankings) route_allowed=true ;;
  /apple-podcasts/episodes/search) route_allowed=true ;;
  /apple-podcasts/new) route_allowed=true ;;
  /apple-podcasts/search) route_allowed=true ;;
  /appstore/app) route_allowed=true ;;
  /appstore/editorial) route_allowed=true ;;
  /appstore/editorial/category) route_allowed=true ;;
  /appstore/list) route_allowed=true ;;
  /appstore/ratings) route_allowed=true ;;
  /appstore/reviews) route_allowed=true ;;
  /appstore/search) route_allowed=true ;;
  /appstore/similar) route_allowed=true ;;
  /arbys/categories) route_allowed=true ;;
  /arbys/directory) route_allowed=true ;;
  /arbys/location) route_allowed=true ;;
  /arbys/locations) route_allowed=true ;;
  /arbys/menu) route_allowed=true ;;
  /audible/categories) route_allowed=true ;;
  /audible/charts) route_allowed=true ;;
  /audible/products) route_allowed=true ;;
  /audible/search) route_allowed=true ;;
  /autotrader/search) route_allowed=true ;;
  /bbb/business) route_allowed=true ;;
  /bbb/business/complaints) route_allowed=true ;;
  /bbb/business/more-info) route_allowed=true ;;
  /bbb/business/reviews) route_allowed=true ;;
  /bbb/category) route_allowed=true ;;
  /bbb/scamtracker/search) route_allowed=true ;;
  /bbb/scamtracker/state-stats) route_allowed=true ;;
  /bbb/search) route_allowed=true ;;
  /bbc/article) route_allowed=true ;;
  /bbc/headlines) route_allowed=true ;;
  /bbc/live) route_allowed=true ;;
  /bbc/search) route_allowed=true ;;
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
  /bilibili/anime-home) route_allowed=true ;;
  /bilibili/autocomplete) route_allowed=true ;;
  /bilibili/guochuang-home) route_allowed=true ;;
  /bilibili/must-watch) route_allowed=true ;;
  /bilibili/popular) route_allowed=true ;;
  /bilibili/ranking) route_allowed=true ;;
  /bilibili/vertical-home) route_allowed=true ;;
  /bilibili/weekly) route_allowed=true ;;
  /bing/images) route_allowed=true ;;
  /bing/news) route_allowed=true ;;
  /bing/search) route_allowed=true ;;
  /bing/suggest) route_allowed=true ;;
  /bing/videos) route_allowed=true ;;
  /bluesky/author-feed) route_allowed=true ;;
  /bluesky/followers) route_allowed=true ;;
  /bluesky/follows) route_allowed=true ;;
  /bluesky/post-thread) route_allowed=true ;;
  /bluesky/profile) route_allowed=true ;;
  /bluesky/search-actors) route_allowed=true ;;
  /bluesky/trending-topics) route_allowed=true ;;
  /bonhams/auctions/search) route_allowed=true ;;
  /bonhams/lots/search) route_allowed=true ;;
  /booking-attractions/detail) route_allowed=true ;;
  /booking-attractions/reviews) route_allowed=true ;;
  /booking-attractions/search) route_allowed=true ;;
  /booking-flights/autocomplete) route_allowed=true ;;
  /booking-flights/search) route_allowed=true ;;
  /booking/hotel-detail) route_allowed=true ;;
  /booking/reviews) route_allowed=true ;;
  /booking/search) route_allowed=true ;;
  /boots/search) route_allowed=true ;;
  /boots/suggest) route_allowed=true ;;
  /boxofficemojo/brand) route_allowed=true ;;
  /boxofficemojo/brands) route_allowed=true ;;
  /boxofficemojo/calendar) route_allowed=true ;;
  /boxofficemojo/calendar/changes) route_allowed=true ;;
  /boxofficemojo/calendar/date) route_allowed=true ;;
  /boxofficemojo/date/domestic) route_allowed=true ;;
  /boxofficemojo/franchise) route_allowed=true ;;
  /boxofficemojo/franchises) route_allowed=true ;;
  /boxofficemojo/genre) route_allowed=true ;;
  /boxofficemojo/genres) route_allowed=true ;;
  /boxofficemojo/lifetime-grosses) route_allowed=true ;;
  /boxofficemojo/release) route_allowed=true ;;
  /boxofficemojo/release-group) route_allowed=true ;;
  /boxofficemojo/showdown) route_allowed=true ;;
  /boxofficemojo/showdowns) route_allowed=true ;;
  /boxofficemojo/title) route_allowed=true ;;
  /boxofficemojo/weekend/domestic) route_allowed=true ;;
  /boxofficemojo/weekend/domestic/by-distributor) route_allowed=true ;;
  /boxofficemojo/weekend/domestic/estimates) route_allowed=true ;;
  /boxofficemojo/year/domestic) route_allowed=true ;;
  /boxofficemojo/year/worldwide) route_allowed=true ;;
  /brand/retrieve) route_allowed=true ;;
  /brave/images) route_allowed=true ;;
  /brave/news) route_allowed=true ;;
  /brave/search) route_allowed=true ;;
  /brave/suggest) route_allowed=true ;;
  /brave/videos) route_allowed=true ;;
  /brooklinen/collections) route_allowed=true ;;
  /brooklinen/pages) route_allowed=true ;;
  /brooklinen/products) route_allowed=true ;;
  /brooklinen/search/suggest) route_allowed=true ;;
  /brooklinen/sitemap/urls) route_allowed=true ;;
  /brooklinen/sitemaps) route_allowed=true ;;
  /brooklinen/store) route_allowed=true ;;
  /burgerking/availability) route_allowed=true ;;
  /burgerking/locations) route_allowed=true ;;
  /burgerking/menu) route_allowed=true ;;
  /burgerking/product) route_allowed=true ;;
  /capterra/product) route_allowed=true ;;
  /capterra/product/reviews) route_allowed=true ;;
  /capterra/search) route_allowed=true ;;
  /carmax/search) route_allowed=true ;;
  /carmax/search/suggestions) route_allowed=true ;;
  /carmax/shop-by-brand) route_allowed=true ;;
  /carmax/stores) route_allowed=true ;;
  /carsdotcom/search) route_allowed=true ;;
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
  /chick-fil-a/content) route_allowed=true ;;
  /chick-fil-a/content-taxonomy) route_allowed=true ;;
  /chick-fil-a/faq) route_allowed=true ;;
  /chick-fil-a/location) route_allowed=true ;;
  /chick-fil-a/locations) route_allowed=true ;;
  /chick-fil-a/menu) route_allowed=true ;;
  /chick-fil-a/menu-item) route_allowed=true ;;
  /chick-fil-a/menu-taxonomy) route_allowed=true ;;
  /chipotle/ingredients) route_allowed=true ;;
  /chipotle/meals) route_allowed=true ;;
  /chipotle/menu) route_allowed=true ;;
  /chipotle/menu/metadata) route_allowed=true ;;
  /chipotle/restaurant) route_allowed=true ;;
  /chipotle/restaurant/meals) route_allowed=true ;;
  /chipotle/restaurant/menu) route_allowed=true ;;
  /chipotle/restaurants) route_allowed=true ;;
  /chromewebstore/categories) route_allowed=true ;;
  /chromewebstore/category) route_allowed=true ;;
  /chromewebstore/charts) route_allowed=true ;;
  /chromewebstore/collection) route_allowed=true ;;
  /chromewebstore/developer) route_allowed=true ;;
  /chromewebstore/item) route_allowed=true ;;
  /chromewebstore/permissions) route_allowed=true ;;
  /chromewebstore/privacy) route_allowed=true ;;
  /chromewebstore/reviews) route_allowed=true ;;
  /chromewebstore/search) route_allowed=true ;;
  /chromewebstore/similar) route_allowed=true ;;
  /chromewebstore/suggest) route_allowed=true ;;
  /cnn/article) route_allowed=true ;;
  /cnn/headlines) route_allowed=true ;;
  /cnn/live-story) route_allowed=true ;;
  /coingecko/categories) route_allowed=true ;;
  /coingecko/chains) route_allowed=true ;;
  /coingecko/exchanges) route_allowed=true ;;
  /coingecko/gainers-losers) route_allowed=true ;;
  /coingecko/global) route_allowed=true ;;
  /coingecko/global/charts) route_allowed=true ;;
  /coingecko/learn/articles) route_allowed=true ;;
  /coingecko/markets) route_allowed=true ;;
  /coingecko/new-coins) route_allowed=true ;;
  /coingecko/news) route_allowed=true ;;
  /coingecko/nfts) route_allowed=true ;;
  /coingecko/search) route_allowed=true ;;
  /coingecko/token-unlocks) route_allowed=true ;;
  /coingecko/treasuries) route_allowed=true ;;
  /coingecko/trending) route_allowed=true ;;
  /colehaan/collections) route_allowed=true ;;
  /colehaan/pages) route_allowed=true ;;
  /colehaan/products) route_allowed=true ;;
  /colehaan/search/suggest) route_allowed=true ;;
  /colehaan/sitemap/urls) route_allowed=true ;;
  /colehaan/sitemaps) route_allowed=true ;;
  /colehaan/store) route_allowed=true ;;
  /congress/report) route_allowed=true ;;
  /congress/stock-disclosures) route_allowed=true ;;
  /costco/categories) route_allowed=true ;;
  /costco/search) route_allowed=true ;;
  /costco/warehouses) route_allowed=true ;;
  /courtlistener/courts) route_allowed=true ;;
  /courtlistener/people) route_allowed=true ;;
  /courtlistener/search) route_allowed=true ;;
  /cricinfo/calendar) route_allowed=true ;;
  /cricinfo/commentary) route_allowed=true ;;
  /cricinfo/grounds) route_allowed=true ;;
  /cricinfo/live) route_allowed=true ;;
  /cricinfo/match) route_allowed=true ;;
  /cricinfo/news) route_allowed=true ;;
  /cricinfo/photos) route_allowed=true ;;
  /cricinfo/rankings) route_allowed=true ;;
  /cricinfo/records) route_allowed=true ;;
  /cricinfo/records/index) route_allowed=true ;;
  /cricinfo/rss) route_allowed=true ;;
  /cricinfo/scores) route_allowed=true ;;
  /cricinfo/series) route_allowed=true ;;
  /cricinfo/squads) route_allowed=true ;;
  /cricinfo/stats) route_allowed=true ;;
  /cricinfo/story) route_allowed=true ;;
  /cricinfo/team) route_allowed=true ;;
  /cricinfo/team/schedule) route_allowed=true ;;
  /cricinfo/teams) route_allowed=true ;;
  /cricinfo/venue) route_allowed=true ;;
  /cricinfo/venue/matches) route_allowed=true ;;
  /cricinfo/videos) route_allowed=true ;;
  /culvers/calendar) route_allowed=true ;;
  /culvers/categories) route_allowed=true ;;
  /culvers/directory) route_allowed=true ;;
  /culvers/flavor) route_allowed=true ;;
  /culvers/item) route_allowed=true ;;
  /culvers/menu) route_allowed=true ;;
  /culvers/store) route_allowed=true ;;
  /cvs/brands) route_allowed=true ;;
  /cvs/categories) route_allowed=true ;;
  /cvs/category) route_allowed=true ;;
  /cvs/search) route_allowed=true ;;
  /cvs/store-locator) route_allowed=true ;;
  /deliveroo/fulfillment-times) route_allowed=true ;;
  /deliveroo/restaurant) route_allowed=true ;;
  /deliveroo/restaurant/menu) route_allowed=true ;;
  /deliveroo/search) route_allowed=true ;;
  /deliveroo/search/filters) route_allowed=true ;;
  /depop/brands) route_allowed=true ;;
  /depop/categories) route_allowed=true ;;
  /depop/search) route_allowed=true ;;
  /depop/search-sellers) route_allowed=true ;;
  /depop/search/facets) route_allowed=true ;;
  /depop/sizes) route_allowed=true ;;
  /depop/suggest) route_allowed=true ;;
  /discogs/search) route_allowed=true ;;
  /dominos/coupons) route_allowed=true ;;
  /dominos/customization) route_allowed=true ;;
  /dominos/menu) route_allowed=true ;;
  /dominos/nutrition) route_allowed=true ;;
  /dominos/store) route_allowed=true ;;
  /dominos/store-locator) route_allowed=true ;;
  /doordash/explore) route_allowed=true ;;
  /doordash/feed) route_allowed=true ;;
  /doordash/search) route_allowed=true ;;
  /doordash/search/autocomplete) route_allowed=true ;;
  /doordash/search/filters) route_allowed=true ;;
  /doordash/search/items) route_allowed=true ;;
  /draftkings/sportsbook/event) route_allowed=true ;;
  /draftkings/sportsbook/event-context) route_allowed=true ;;
  /draftkings/sportsbook/event-markets) route_allowed=true ;;
  /draftkings/sportsbook/featured-leagues) route_allowed=true ;;
  /draftkings/sportsbook/futures) route_allowed=true ;;
  /draftkings/sportsbook/league-events) route_allowed=true ;;
  /draftkings/sportsbook/leagues) route_allowed=true ;;
  /draftkings/sportsbook/live) route_allowed=true ;;
  /draftkings/sportsbook/odds) route_allowed=true ;;
  /draftkings/sportsbook/quick-links) route_allowed=true ;;
  /draftkings/sportsbook/team) route_allowed=true ;;
  /draftkings/sportsbook/teams) route_allowed=true ;;
  /duckduckgo/image) route_allowed=true ;;
  /duckduckgo/news) route_allowed=true ;;
  /duckduckgo/search) route_allowed=true ;;
  /duckduckgo/shopping) route_allowed=true ;;
  /duckduckgo/video) route_allowed=true ;;
  /dunkin/directory) route_allowed=true ;;
  /dunkin/menu) route_allowed=true ;;
  /dunkin/nearby) route_allowed=true ;;
  /dunkin/store) route_allowed=true ;;
  /ebay/live/streams) route_allowed=true ;;
  /ebay/live/streams/batch) route_allowed=true ;;
  /ebay/search) route_allowed=true ;;
  /espn/athlete) route_allowed=true ;;
  /espn/game-summary) route_allowed=true ;;
  /espn/news) route_allowed=true ;;
  /espn/rankings) route_allowed=true ;;
  /espn/scoreboard) route_allowed=true ;;
  /espn/standings) route_allowed=true ;;
  /espn/team) route_allowed=true ;;
  /espn/team-roster) route_allowed=true ;;
  /espn/teams) route_allowed=true ;;
  /etsy/search) route_allowed=true ;;
  /etsy/shop/search) route_allowed=true ;;
  /everlane/collections) route_allowed=true ;;
  /everlane/pages) route_allowed=true ;;
  /everlane/products) route_allowed=true ;;
  /everlane/search/suggest) route_allowed=true ;;
  /everlane/sitemap/urls) route_allowed=true ;;
  /everlane/sitemaps) route_allowed=true ;;
  /everlane/store) route_allowed=true ;;
  /expedia/activities/search) route_allowed=true ;;
  /expedia/flights/search) route_allowed=true ;;
  /expedia/locations/search) route_allowed=true ;;
  /expedia/properties/detail) route_allowed=true ;;
  /expedia/properties/filters) route_allowed=true ;;
  /expedia/properties/reviews) route_allowed=true ;;
  /expedia/properties/search) route_allowed=true ;;
  /facebook/marketplace/search) route_allowed=true ;;
  /fashionnova/collections) route_allowed=true ;;
  /fashionnova/pages) route_allowed=true ;;
  /fashionnova/products) route_allowed=true ;;
  /fashionnova/search/suggest) route_allowed=true ;;
  /fashionnova/sitemap/urls) route_allowed=true ;;
  /fashionnova/sitemaps) route_allowed=true ;;
  /fashionnova/store) route_allowed=true ;;
  /fiveguys/directory) route_allowed=true ;;
  /fiveguys/faq) route_allowed=true ;;
  /fiveguys/faq-categories) route_allowed=true ;;
  /fiveguys/menu) route_allowed=true ;;
  /fiveguys/nearby) route_allowed=true ;;
  /fiveguys/nutrition) route_allowed=true ;;
  /fiveguys/ordering-locations) route_allowed=true ;;
  /fiveguys/ordering-menu) route_allowed=true ;;
  /fiveguys/search) route_allowed=true ;;
  /fiveguys/store) route_allowed=true ;;
  /fiverr/search) route_allowed=true ;;
  /foodpanda/restaurant) route_allowed=true ;;
  /foodpanda/restaurant/menu) route_allowed=true ;;
  /foodpanda/restaurant/reviews) route_allowed=true ;;
  /foodpanda/search) route_allowed=true ;;
  /gdelt/context) route_allowed=true ;;
  /gdelt/search) route_allowed=true ;;
  /gdelt/timeline) route_allowed=true ;;
  /gdelt/tonechart) route_allowed=true ;;
  /gdelt/tv-concept-entities) route_allowed=true ;;
  /gdelt/tv-search) route_allowed=true ;;
  /gdelt/tv-showchart) route_allowed=true ;;
  /gdelt/tv-stationchart) route_allowed=true ;;
  /gdelt/tv-stationdetails) route_allowed=true ;;
  /gdelt/tv-timeline) route_allowed=true ;;
  /gdelt/tv-visual-entities) route_allowed=true ;;
  /gdelt/tv-wordcloud) route_allowed=true ;;
  /geocoding/lookup) route_allowed=true ;;
  /geocoding/reverse) route_allowed=true ;;
  /geocoding/search) route_allowed=true ;;
  /github/search/repositories) route_allowed=true ;;
  /github/search/users) route_allowed=true ;;
  /github/trending) route_allowed=true ;;
  /github/trending/developers) route_allowed=true ;;
  /goat/collection) route_allowed=true ;;
  /goat/countries) route_allowed=true ;;
  /goat/curated) route_allowed=true ;;
  /goat/listings/count) route_allowed=true ;;
  /goat/search) route_allowed=true ;;
  /goat/search/facets) route_allowed=true ;;
  /goat/searches/trending) route_allowed=true ;;
  /goat/suggest) route_allowed=true ;;
  /goodreads/lists) route_allowed=true ;;
  /goodreads/search) route_allowed=true ;;
  /google-jobs/job) route_allowed=true ;;
  /google-jobs/search) route_allowed=true ;;
  /google/finance/context) route_allowed=true ;;
  /google/finance/markets/earnings) route_allowed=true ;;
  /google/finance/markets/featured) route_allowed=true ;;
  /google/finance/markets/headline) route_allowed=true ;;
  /google/finance/markets/indices) route_allowed=true ;;
  /google/finance/markets/movers) route_allowed=true ;;
  /google/finance/markets/top) route_allowed=true ;;
  /google/finance/markets/trending) route_allowed=true ;;
  /google/finance/search) route_allowed=true ;;
  /google/jobs) route_allowed=true ;;
  /google/map/search) route_allowed=true ;;
  /google/news) route_allowed=true ;;
  /google/search) route_allowed=true ;;
  /google/suggest) route_allowed=true ;;
  /google/trends/categories) route_allowed=true ;;
  /google/trends/enums) route_allowed=true ;;
  /google/trends/explore) route_allowed=true ;;
  /google/trends/explore/interest-by-region) route_allowed=true ;;
  /google/trends/explore/interest-over-time) route_allowed=true ;;
  /google/trends/explore/related-topics) route_allowed=true ;;
  /google/trends/explore/rising-queries) route_allowed=true ;;
  /google/trends/explore/top-queries) route_allowed=true ;;
  /google/trends/locations) route_allowed=true ;;
  /google/trends/trending) route_allowed=true ;;
  /google/trends/trending/detail) route_allowed=true ;;
  /google/videos) route_allowed=true ;;
  /googlepatents/classification) route_allowed=true ;;
  /googlepatents/coverage) route_allowed=true ;;
  /googlepatents/detail) route_allowed=true ;;
  /googlepatents/recent) route_allowed=true ;;
  /googlepatents/search) route_allowed=true ;;
  /googlepatents/suggest) route_allowed=true ;;
  /googleplay/app) route_allowed=true ;;
  /googleplay/categories) route_allowed=true ;;
  /googleplay/datasafety) route_allowed=true ;;
  /googleplay/list) route_allowed=true ;;
  /googleplay/permissions) route_allowed=true ;;
  /googleplay/ratings) route_allowed=true ;;
  /googleplay/reviews) route_allowed=true ;;
  /googleplay/search) route_allowed=true ;;
  /googleplay/similar) route_allowed=true ;;
  /grubhub/availability) route_allowed=true ;;
  /grubhub/offers) route_allowed=true ;;
  /grubhub/restaurant) route_allowed=true ;;
  /grubhub/restaurant/menu) route_allowed=true ;;
  /grubhub/restaurant/reviews) route_allowed=true ;;
  /grubhub/search) route_allowed=true ;;
  /grubhub/timepicker) route_allowed=true ;;
  /guardian/article) route_allowed=true ;;
  /guardian/headlines) route_allowed=true ;;
  /guardian/topic) route_allowed=true ;;
  /gymshark/collections) route_allowed=true ;;
  /gymshark/pages) route_allowed=true ;;
  /gymshark/products) route_allowed=true ;;
  /gymshark/sitemap/urls) route_allowed=true ;;
  /gymshark/sitemaps) route_allowed=true ;;
  /gymshark/store) route_allowed=true ;;
  /hm/categories) route_allowed=true ;;
  /hm/listing) route_allowed=true ;;
  /hm/search) route_allowed=true ;;
  /hm/search/suggestions) route_allowed=true ;;
  /hm/stores) route_allowed=true ;;
  /homedepot/categories) route_allowed=true ;;
  /homedepot/category) route_allowed=true ;;
  /homedepot/search) route_allowed=true ;;
  /homedepot/suggest) route_allowed=true ;;
  /hotels/autocomplete) route_allowed=true ;;
  /hotels/offers) route_allowed=true ;;
  /hotels/property) route_allowed=true ;;
  /hotels/rates) route_allowed=true ;;
  /hotels/reviews) route_allowed=true ;;
  /hotels/reviews/archive) route_allowed=true ;;
  /hotels/search) route_allowed=true ;;
  /ikea/availability) route_allowed=true ;;
  /ikea/category) route_allowed=true ;;
  /ikea/product) route_allowed=true ;;
  /ikea/reviews) route_allowed=true ;;
  /ikea/search) route_allowed=true ;;
  /ikea/store) route_allowed=true ;;
  /ikea/stores) route_allowed=true ;;
  /ikea/suggest) route_allowed=true ;;
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
  /importyeti/company) route_allowed=true ;;
  /importyeti/search) route_allowed=true ;;
  /indeed/job) route_allowed=true ;;
  /indeed/locations/suggest) route_allowed=true ;;
  /indeed/search) route_allowed=true ;;
  /instacart/departments) route_allowed=true ;;
  /instacart/item) route_allowed=true ;;
  /instacart/search) route_allowed=true ;;
  /instacart/search-nearby) route_allowed=true ;;
  /instacart/stores) route_allowed=true ;;
  /instacart/trending) route_allowed=true ;;
  /jcrew/categories) route_allowed=true ;;
  /jcrew/category) route_allowed=true ;;
  /jcrew/product) route_allowed=true ;;
  /jcrew/product/reviews) route_allowed=true ;;
  /jcrew/search) route_allowed=true ;;
  /jcrew/size-chart) route_allowed=true ;;
  /jcrew/stores) route_allowed=true ;;
  /jcrew/suggest) route_allowed=true ;;
  /jimmy-johns/menu) route_allowed=true ;;
  /jimmy-johns/modifiers) route_allowed=true ;;
  /jimmy-johns/nearby) route_allowed=true ;;
  /jimmy-johns/sitemap) route_allowed=true ;;
  /jimmy-johns/store) route_allowed=true ;;
  /jobs/ashby/board) route_allowed=true ;;
  /jobs/company-search) route_allowed=true ;;
  /jobs/eightfold/board) route_allowed=true ;;
  /jobs/eightfold/job) route_allowed=true ;;
  /jobs/gem/board) route_allowed=true ;;
  /jobs/greenhouse/board) route_allowed=true ;;
  /jobs/greenhouse/job) route_allowed=true ;;
  /jobs/hiring-signals) route_allowed=true ;;
  /jobs/icims/board) route_allowed=true ;;
  /jobs/icims/job) route_allowed=true ;;
  /jobs/lever/posting) route_allowed=true ;;
  /jobs/lever/postings) route_allowed=true ;;
  /jobs/oracle/board) route_allowed=true ;;
  /jobs/oracle/job) route_allowed=true ;;
  /jobs/personio/feed) route_allowed=true ;;
  /jobs/phenom/board) route_allowed=true ;;
  /jobs/phenom/job) route_allowed=true ;;
  /jobs/pinpoint/board) route_allowed=true ;;
  /jobs/recruitee/offer) route_allowed=true ;;
  /jobs/recruitee/offers) route_allowed=true ;;
  /jobs/rippling/board) route_allowed=true ;;
  /jobs/rippling/job) route_allowed=true ;;
  /jobs/smartrecruiters/posting) route_allowed=true ;;
  /jobs/smartrecruiters/postings) route_allowed=true ;;
  /jobs/teamtailor/jobs) route_allowed=true ;;
  /jobs/ukg/board) route_allowed=true ;;
  /jobs/workable/posting) route_allowed=true ;;
  /jobs/workable/postings) route_allowed=true ;;
  /jobs/workday/board) route_allowed=true ;;
  /jobs/workday/job) route_allowed=true ;;
  /justeat/restaurant) route_allowed=true ;;
  /justeat/restaurant/menu) route_allowed=true ;;
  /justeat/search) route_allowed=true ;;
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
  /kalshi/events) route_allowed=true ;;
  /kalshi/events/multivariate) route_allowed=true ;;
  /kalshi/exchange/schedule) route_allowed=true ;;
  /kalshi/exchange/status) route_allowed=true ;;
  /kalshi/historical/cutoff) route_allowed=true ;;
  /kalshi/historical/markets) route_allowed=true ;;
  /kalshi/historical/trades) route_allowed=true ;;
  /kalshi/markets) route_allowed=true ;;
  /kalshi/markets/history) route_allowed=true ;;
  /kalshi/markets/orderbooks) route_allowed=true ;;
  /kalshi/series) route_allowed=true ;;
  /kalshi/trades) route_allowed=true ;;
  /kfc/delivery-estimate) route_allowed=true ;;
  /kfc/menu) route_allowed=true ;;
  /kfc/nearby) route_allowed=true ;;
  /kfc/promotion) route_allowed=true ;;
  /kfc/promotions) route_allowed=true ;;
  /kfc/store) route_allowed=true ;;
  /kfc/stores) route_allowed=true ;;
  /kickstarter/comments) route_allowed=true ;;
  /kickstarter/discover) route_allowed=true ;;
  /kickstarter/project) route_allowed=true ;;
  /kickstarter/updates) route_allowed=true ;;
  /kohls/category) route_allowed=true ;;
  /kohls/product/reviews) route_allowed=true ;;
  /kohls/stores) route_allowed=true ;;
  /kohls/suggest) route_allowed=true ;;
  /kroger/category) route_allowed=true ;;
  /kroger/coupons) route_allowed=true ;;
  /kroger/product) route_allowed=true ;;
  /kroger/product/reviews) route_allowed=true ;;
  /kroger/products) route_allowed=true ;;
  /kroger/related-tags) route_allowed=true ;;
  /kroger/search) route_allowed=true ;;
  /kroger/store) route_allowed=true ;;
  /kroger/suggest) route_allowed=true ;;
  /kyliecosmetics/collections) route_allowed=true ;;
  /kyliecosmetics/pages) route_allowed=true ;;
  /kyliecosmetics/products) route_allowed=true ;;
  /kyliecosmetics/search/suggest) route_allowed=true ;;
  /kyliecosmetics/sitemap/urls) route_allowed=true ;;
  /kyliecosmetics/sitemaps) route_allowed=true ;;
  /kyliecosmetics/store) route_allowed=true ;;
  /lazada/categories) route_allowed=true ;;
  /lazada/category-products) route_allowed=true ;;
  /lazada/home) route_allowed=true ;;
  /lazada/product) route_allowed=true ;;
  /lazada/search) route_allowed=true ;;
  /leboncoin/listing) route_allowed=true ;;
  /leboncoin/search) route_allowed=true ;;
  /letterboxd/popular) route_allowed=true ;;
  /letterboxd/search) route_allowed=true ;;
  /lululemon/categories) route_allowed=true ;;
  /lululemon/category) route_allowed=true ;;
  /lululemon/outfit) route_allowed=true ;;
  /lululemon/stores) route_allowed=true ;;
  /macys/product/reviews) route_allowed=true ;;
  /macys/suggest) route_allowed=true ;;
  /manga/rankings) route_allowed=true ;;
  /manga/search) route_allowed=true ;;
  /mcdonalds/categories) route_allowed=true ;;
  /mcdonalds/item) route_allowed=true ;;
  /mcdonalds/item-list) route_allowed=true ;;
  /mcdonalds/menu) route_allowed=true ;;
  /mcdonalds/restaurant-menu) route_allowed=true ;;
  /mcdonalds/restaurants) route_allowed=true ;;
  /mercari/autocomplete) route_allowed=true ;;
  /mercari/home) route_allowed=true ;;
  /mercari/master) route_allowed=true ;;
  /mercari/search) route_allowed=true ;;
  /meta-jobs/job) route_allowed=true ;;
  /meta-jobs/list) route_allowed=true ;;
  /meta-jobs/search) route_allowed=true ;;
  /metacritic/browse) route_allowed=true ;;
  /metaculus/comments-feed) route_allowed=true ;;
  /metaculus/questions) route_allowed=true ;;
  /metaculus/top-comments) route_allowed=true ;;
  /mlb/game) route_allowed=true ;;
  /mlb/game-boxscore) route_allowed=true ;;
  /mlb/game-play-by-play) route_allowed=true ;;
  /mlb/league-stats) route_allowed=true ;;
  /mlb/player) route_allowed=true ;;
  /mlb/player-stats) route_allowed=true ;;
  /mlb/schedule) route_allowed=true ;;
  /mlb/standings) route_allowed=true ;;
  /mlb/team-roster) route_allowed=true ;;
  /mlb/team-stats) route_allowed=true ;;
  /mlb/teams) route_allowed=true ;;
  /mlb/transactions) route_allowed=true ;;
  /nike/categories) route_allowed=true ;;
  /nike/product) route_allowed=true ;;
  /nike/product/availability) route_allowed=true ;;
  /nike/product/details) route_allowed=true ;;
  /nike/product/recommendations) route_allowed=true ;;
  /nike/product/reviews) route_allowed=true ;;
  /nike/search) route_allowed=true ;;
  /nike/stores) route_allowed=true ;;
  /nike/suggest) route_allowed=true ;;
  /numbeo/cost-of-living/country) route_allowed=true ;;
  /numbeo/cost-of-living/rankings) route_allowed=true ;;
  /numbeo/cost-of-living/rankings-by-country) route_allowed=true ;;
  /numbeo/indices/country) route_allowed=true ;;
  /numbeo/indices/rankings) route_allowed=true ;;
  /numbeo/indices/rankings-by-country) route_allowed=true ;;
  /ohpolly/collections) route_allowed=true ;;
  /ohpolly/pages) route_allowed=true ;;
  /ohpolly/products) route_allowed=true ;;
  /ohpolly/search/suggest) route_allowed=true ;;
  /ohpolly/sitemap/urls) route_allowed=true ;;
  /ohpolly/sitemaps) route_allowed=true ;;
  /ohpolly/store) route_allowed=true ;;
  /oldnavy/categories) route_allowed=true ;;
  /oldnavy/category) route_allowed=true ;;
  /oldnavy/product) route_allowed=true ;;
  /oldnavy/product/availability) route_allowed=true ;;
  /oldnavy/product/reviews) route_allowed=true ;;
  /oldnavy/search) route_allowed=true ;;
  /oldnavy/stores) route_allowed=true ;;
  /opensea/activity) route_allowed=true ;;
  /opensea/categories) route_allowed=true ;;
  /opensea/chains) route_allowed=true ;;
  /opensea/collections) route_allowed=true ;;
  /opensea/drops) route_allowed=true ;;
  /opensea/most-watched) route_allowed=true ;;
  /opensea/rankings) route_allowed=true ;;
  /opensea/search/collections) route_allowed=true ;;
  /opensea/top-movers) route_allowed=true ;;
  /opentable/restaurant) route_allowed=true ;;
  /opentable/restaurant/menus) route_allowed=true ;;
  /opentable/restaurant/reviews) route_allowed=true ;;
  /opentable/search) route_allowed=true ;;
  /otto/categories) route_allowed=true ;;
  /otto/product) route_allowed=true ;;
  /otto/search) route_allowed=true ;;
  /pandamart/search) route_allowed=true ;;
  /pandamart/store) route_allowed=true ;;
  /pandamart/store/categories) route_allowed=true ;;
  /pandamart/store/product) route_allowed=true ;;
  /pandamart/store/products) route_allowed=true ;;
  /pandamart/store/search) route_allowed=true ;;
  /panera/at-work-locations) route_allowed=true ;;
  /panera/cafe) route_allowed=true ;;
  /panera/catering-delivery-info) route_allowed=true ;;
  /panera/catering-menu) route_allowed=true ;;
  /panera/geocode) route_allowed=true ;;
  /panera/item-detail) route_allowed=true ;;
  /panera/item-options) route_allowed=true ;;
  /panera/locations) route_allowed=true ;;
  /panera/menu) route_allowed=true ;;
  /panera/quantity-rules) route_allowed=true ;;
  /panera/retired-products) route_allowed=true ;;
  /panera/time-slots) route_allowed=true ;;
  /panera/upsell-suggestions) route_allowed=true ;;
  /papajohns/allergens) route_allowed=true ;;
  /papajohns/colombia/menu) route_allowed=true ;;
  /papajohns/deals) route_allowed=true ;;
  /papajohns/directory) route_allowed=true ;;
  /papajohns/elsalvador/menu) route_allowed=true ;;
  /papajohns/india/deal) route_allowed=true ;;
  /papajohns/india/menu) route_allowed=true ;;
  /papajohns/india/menu/item) route_allowed=true ;;
  /papajohns/india/stores) route_allowed=true ;;
  /papajohns/intl/deals) route_allowed=true ;;
  /papajohns/intl/ingredients) route_allowed=true ;;
  /papajohns/intl/menu) route_allowed=true ;;
  /papajohns/intl/offer) route_allowed=true ;;
  /papajohns/intl/product) route_allowed=true ;;
  /papajohns/intl/stores) route_allowed=true ;;
  /papajohns/menu) route_allowed=true ;;
  /papajohns/menu/item) route_allowed=true ;;
  /papajohns/nearby) route_allowed=true ;;
  /papajohns/nutrition) route_allowed=true ;;
  /papajohns/peru/menu) route_allowed=true ;;
  /papajohns/poland/menu) route_allowed=true ;;
  /papajohns/russia/menu) route_allowed=true ;;
  /papajohns/store) route_allowed=true ;;
  /patreon/creator) route_allowed=true ;;
  /patreon/creator/tiers) route_allowed=true ;;
  /patreon/explore) route_allowed=true ;;
  /patreon/rss) route_allowed=true ;;
  /pinterest/categories) route_allowed=true ;;
  /pinterest/search) route_allowed=true ;;
  /pitchbook/advisor) route_allowed=true ;;
  /pitchbook/company) route_allowed=true ;;
  /pitchbook/fund) route_allowed=true ;;
  /pitchbook/investor) route_allowed=true ;;
  /pitchbook/limited-partner) route_allowed=true ;;
  /pizzahut/bundle-choices) route_allowed=true ;;
  /pizzahut/delivery-estimate) route_allowed=true ;;
  /pizzahut/menu) route_allowed=true ;;
  /pizzahut/modifiers) route_allowed=true ;;
  /pizzahut/store) route_allowed=true ;;
  /pizzahut/stores) route_allowed=true ;;
  /playstation/browse) route_allowed=true ;;
  /playstation/category) route_allowed=true ;;
  /playstation/concept) route_allowed=true ;;
  /playstation/deals) route_allowed=true ;;
  /playstation/latest) route_allowed=true ;;
  /playstation/page) route_allowed=true ;;
  /playstation/product) route_allowed=true ;;
  /playstation/search) route_allowed=true ;;
  /polymarket/activity/trades) route_allowed=true ;;
  /polymarket/dashboards/macro) route_allowed=true ;;
  /polymarket/events) route_allowed=true ;;
  /polymarket/events/similar) route_allowed=true ;;
  /polymarket/fee-types) route_allowed=true ;;
  /polymarket/homepage/feed) route_allowed=true ;;
  /polymarket/leaderboard) route_allowed=true ;;
  /polymarket/markets) route_allowed=true ;;
  /polymarket/predictions) route_allowed=true ;;
  /polymarket/rewards/markets) route_allowed=true ;;
  /polymarket/search) route_allowed=true ;;
  /polymarket/tags) route_allowed=true ;;
  /polymarket/tokens/midpoints) route_allowed=true ;;
  /polymarket/tokens/orderbooks) route_allowed=true ;;
  /polymarket/tokens/prices) route_allowed=true ;;
  /polymarket/tokens/spreads) route_allowed=true ;;
  /popeyes/faq) route_allowed=true ;;
  /popeyes/location) route_allowed=true ;;
  /popeyes/locations) route_allowed=true ;;
  /popeyes/menu) route_allowed=true ;;
  /popeyes/offers) route_allowed=true ;;
  /popeyes/promotions) route_allowed=true ;;
  /popeyes/quests) route_allowed=true ;;
  /popeyes/rewards) route_allowed=true ;;
  /poshmark/brands) route_allowed=true ;;
  /poshmark/categories) route_allowed=true ;;
  /poshmark/search) route_allowed=true ;;
  /producthunt/leaderboard) route_allowed=true ;;
  /producthunt/search) route_allowed=true ;;
  /quince/categories) route_allowed=true ;;
  /quince/navigation) route_allowed=true ;;
  /quince/product) route_allowed=true ;;
  /quince/product/faq) route_allowed=true ;;
  /quince/product/reviews) route_allowed=true ;;
  /quince/search) route_allowed=true ;;
  /quince/sitemap/urls) route_allowed=true ;;
  /quince/sitemaps) route_allowed=true ;;
  /quince/suggest) route_allowed=true ;;
  /raisingcanes/directory) route_allowed=true ;;
  /raisingcanes/menu) route_allowed=true ;;
  /raisingcanes/nearby) route_allowed=true ;;
  /raisingcanes/promotion) route_allowed=true ;;
  /raisingcanes/promotions) route_allowed=true ;;
  /raisingcanes/store) route_allowed=true ;;
  /reddit/leads) route_allowed=true ;;
  /reddit/search) route_allowed=true ;;
  /reddit/subreddits/posts) route_allowed=true ;;
  /reddit/trends) route_allowed=true ;;
  /redfin/estimate) route_allowed=true ;;
  /redfin/property) route_allowed=true ;;
  /redfin/region-trends) route_allowed=true ;;
  /redfin/search) route_allowed=true ;;
  /redfin/similar) route_allowed=true ;;
  /rightmove/agents) route_allowed=true ;;
  /rightmove/autocomplete) route_allowed=true ;;
  /rightmove/commercial/search) route_allowed=true ;;
  /rightmove/new-homes/search) route_allowed=true ;;
  /rightmove/search) route_allowed=true ;;
  /rightmove/student/search) route_allowed=true ;;
  /roblox/badges) route_allowed=true ;;
  /roblox/game) route_allowed=true ;;
  /roblox/rankings) route_allowed=true ;;
  /roblox/search) route_allowed=true ;;
  /rothys/collections) route_allowed=true ;;
  /rothys/pages) route_allowed=true ;;
  /rothys/products) route_allowed=true ;;
  /rothys/search/suggest) route_allowed=true ;;
  /rothys/sitemap/urls) route_allowed=true ;;
  /rothys/sitemaps) route_allowed=true ;;
  /rothys/store) route_allowed=true ;;
  /rottentomatoes/browse/movies) route_allowed=true ;;
  /rottentomatoes/browse/tv) route_allowed=true ;;
  /rottentomatoes/episode) route_allowed=true ;;
  /rottentomatoes/movie) route_allowed=true ;;
  /rottentomatoes/movie/reviews) route_allowed=true ;;
  /rottentomatoes/person) route_allowed=true ;;
  /rottentomatoes/search) route_allowed=true ;;
  /rottentomatoes/season) route_allowed=true ;;
  /rottentomatoes/series) route_allowed=true ;;
  /rover/search) route_allowed=true ;;
  /rover/trainer-search) route_allowed=true ;;
  /samsclub/category) route_allowed=true ;;
  /samsclub/departments) route_allowed=true ;;
  /sec/company/intelligence) route_allowed=true ;;
  /sec/company/search) route_allowed=true ;;
  /sec/company/submissions) route_allowed=true ;;
  /sec/filing) route_allowed=true ;;
  /sec/filing/sections) route_allowed=true ;;
  /sec/financials) route_allowed=true ;;
  /sec/frames) route_allowed=true ;;
  /sec/full-text-search) route_allowed=true ;;
  /sec/insider) route_allowed=true ;;
  /sec/institutional-holdings) route_allowed=true ;;
  /sephora/category) route_allowed=true ;;
  /sephora/product) route_allowed=true ;;
  /sephora/product/questions) route_allowed=true ;;
  /sephora/product/reviews) route_allowed=true ;;
  /sephora/search) route_allowed=true ;;
  /sephora/stores) route_allowed=true ;;
  /sephora/suggest) route_allowed=true ;;
  /shakeshack/locations) route_allowed=true ;;
  /shakeshack/menu) route_allowed=true ;;
  /shakeshack/nearby) route_allowed=true ;;
  /shakeshack/store) route_allowed=true ;;
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
  /similarweb/search) route_allowed=true ;;
  /skims/collections) route_allowed=true ;;
  /skims/pages) route_allowed=true ;;
  /skims/products) route_allowed=true ;;
  /skims/search/suggest) route_allowed=true ;;
  /skims/sitemap/urls) route_allowed=true ;;
  /skims/sitemaps) route_allowed=true ;;
  /skims/store) route_allowed=true ;;
  /sofascore/event) route_allowed=true ;;
  /sofascore/event-h2h) route_allowed=true ;;
  /sofascore/event-incidents) route_allowed=true ;;
  /sofascore/event-lineups) route_allowed=true ;;
  /sofascore/event-odds) route_allowed=true ;;
  /sofascore/event-statistics) route_allowed=true ;;
  /sofascore/live-events) route_allowed=true ;;
  /sofascore/player) route_allowed=true ;;
  /sofascore/round-events) route_allowed=true ;;
  /sofascore/search) route_allowed=true ;;
  /sofascore/standings) route_allowed=true ;;
  /sofascore/team) route_allowed=true ;;
  /sofascore/team-events) route_allowed=true ;;
  /sofascore/team-players) route_allowed=true ;;
  /sofascore/tournament-seasons) route_allowed=true ;;
  /sonic/availability) route_allowed=true ;;
  /sonic/categories) route_allowed=true ;;
  /sonic/deals) route_allowed=true ;;
  /sonic/directory) route_allowed=true ;;
  /sonic/item) route_allowed=true ;;
  /sonic/location-suggest) route_allowed=true ;;
  /sonic/locations) route_allowed=true ;;
  /sonic/menu) route_allowed=true ;;
  /sonic/nearby) route_allowed=true ;;
  /sonic/nutrition-documents) route_allowed=true ;;
  /sonic/sitemap) route_allowed=true ;;
  /sonic/store) route_allowed=true ;;
  /soundcloud/playlist) route_allowed=true ;;
  /soundcloud/profile) route_allowed=true ;;
  /soundcloud/search) route_allowed=true ;;
  /soundcloud/track) route_allowed=true ;;
  /soundcloud/user-tracks) route_allowed=true ;;
  /sparkfun/categories) route_allowed=true ;;
  /sparkfun/category) route_allowed=true ;;
  /sparkfun/product) route_allowed=true ;;
  /sparkfun/search) route_allowed=true ;;
  /spotify-podcasts/categories) route_allowed=true ;;
  /spotify-podcasts/charts) route_allowed=true ;;
  /spotify-podcasts/episode) route_allowed=true ;;
  /spotify-podcasts/home) route_allowed=true ;;
  /spotify-podcasts/search) route_allowed=true ;;
  /spotify-podcasts/show) route_allowed=true ;;
  /spotify-podcasts/show/episodes) route_allowed=true ;;
  /spotify-podcasts/show/recommendations) route_allowed=true ;;
  /spotify/album) route_allowed=true ;;
  /spotify/album/tracks) route_allowed=true ;;
  /spotify/albums/search) route_allowed=true ;;
  /spotify/artist) route_allowed=true ;;
  /spotify/artist/albums) route_allowed=true ;;
  /spotify/artist/playlists) route_allowed=true ;;
  /spotify/artist/related) route_allowed=true ;;
  /spotify/artists/search) route_allowed=true ;;
  /spotify/audiobook) route_allowed=true ;;
  /spotify/audiobook/chapters) route_allowed=true ;;
  /spotify/audiobooks/search) route_allowed=true ;;
  /spotify/chapter) route_allowed=true ;;
  /spotify/episodes/search) route_allowed=true ;;
  /spotify/featured-charts-by-country) route_allowed=true ;;
  /spotify/genre) route_allowed=true ;;
  /spotify/home) route_allowed=true ;;
  /spotify/playlist) route_allowed=true ;;
  /spotify/playlists/search) route_allowed=true ;;
  /spotify/popular-by-country) route_allowed=true ;;
  /spotify/profile) route_allowed=true ;;
  /spotify/profile/followers) route_allowed=true ;;
  /spotify/profile/playlists) route_allowed=true ;;
  /spotify/profiles/search) route_allowed=true ;;
  /spotify/search) route_allowed=true ;;
  /spotify/section) route_allowed=true ;;
  /spotify/shows/search) route_allowed=true ;;
  /spotify/track) route_allowed=true ;;
  /spotify/track/recommended) route_allowed=true ;;
  /spotify/track/similar-albums) route_allowed=true ;;
  /spotify/tracks/search) route_allowed=true ;;
  /starbucks/menu) route_allowed=true ;;
  /starbucks/nearest-store) route_allowed=true ;;
  /starbucks/stores) route_allowed=true ;;
  /steam/achievements) route_allowed=true ;;
  /steam/app) route_allowed=true ;;
  /steam/charts/concurrent) route_allowed=true ;;
  /steam/charts/most-played) route_allowed=true ;;
  /steam/charts/top-releases) route_allowed=true ;;
  /steam/community-recommendations) route_allowed=true ;;
  /steam/featured) route_allowed=true ;;
  /steam/featured-categories) route_allowed=true ;;
  /steam/items) route_allowed=true ;;
  /steam/news) route_allowed=true ;;
  /steam/package) route_allowed=true ;;
  /steam/players) route_allowed=true ;;
  /steam/reviews) route_allowed=true ;;
  /steam/reviews/histogram) route_allowed=true ;;
  /steam/search) route_allowed=true ;;
  /steam/search/results) route_allowed=true ;;
  /steam/steamspy) route_allowed=true ;;
  /steam/tags) route_allowed=true ;;
  /steam/tags/list) route_allowed=true ;;
  /steam/top-sellers) route_allowed=true ;;
  /stevemadden/collections) route_allowed=true ;;
  /stevemadden/pages) route_allowed=true ;;
  /stevemadden/products) route_allowed=true ;;
  /stevemadden/search/suggest) route_allowed=true ;;
  /stevemadden/sitemap/urls) route_allowed=true ;;
  /stevemadden/sitemaps) route_allowed=true ;;
  /stevemadden/store) route_allowed=true ;;
  /stockx/brands) route_allowed=true ;;
  /stockx/categories) route_allowed=true ;;
  /stockx/releases) route_allowed=true ;;
  /stockx/search) route_allowed=true ;;
  /strava/challenges) route_allowed=true ;;
  /strava/routes) route_allowed=true ;;
  /strava/routes/detail) route_allowed=true ;;
  /subway/available-times) route_allowed=true ;;
  /subway/combos) route_allowed=true ;;
  /subway/menu) route_allowed=true ;;
  /subway/nearby) route_allowed=true ;;
  /subway/sitemap) route_allowed=true ;;
  /subway/store) route_allowed=true ;;
  /swiggy/collections) route_allowed=true ;;
  /swiggy/restaurant) route_allowed=true ;;
  /swiggy/restaurant/menu) route_allowed=true ;;
  /swiggy/search) route_allowed=true ;;
  /taco-bell/app-menu) route_allowed=true ;;
  /taco-bell/categories) route_allowed=true ;;
  /taco-bell/menu) route_allowed=true ;;
  /taco-bell/nutrition) route_allowed=true ;;
  /taco-bell/product) route_allowed=true ;;
  /taco-bell/store) route_allowed=true ;;
  /taco-bell/store-menu) route_allowed=true ;;
  /taco-bell/stores) route_allowed=true ;;
  /target/categories) route_allowed=true ;;
  /target/category-products) route_allowed=true ;;
  /target/filter-options) route_allowed=true ;;
  /target/product) route_allowed=true ;;
  /target/questions) route_allowed=true ;;
  /target/reviews) route_allowed=true ;;
  /target/search) route_allowed=true ;;
  /tes/jobs/detail) route_allowed=true ;;
  /tes/jobs/employer) route_allowed=true ;;
  /tes/jobs/search) route_allowed=true ;;
  /tes/resources/detail) route_allowed=true ;;
  /tes/resources/search) route_allowed=true ;;
  /tes/resources/shop) route_allowed=true ;;
  /tes/schools/search) route_allowed=true ;;
  /tesla-jobs/job) route_allowed=true ;;
  /tesla-jobs/list) route_allowed=true ;;
  /thebodyshop/collections) route_allowed=true ;;
  /thebodyshop/pages) route_allowed=true ;;
  /thebodyshop/products) route_allowed=true ;;
  /thebodyshop/search/suggest) route_allowed=true ;;
  /thebodyshop/sitemap/urls) route_allowed=true ;;
  /thebodyshop/sitemaps) route_allowed=true ;;
  /thebodyshop/store) route_allowed=true ;;
  /threads/search) route_allowed=true ;;
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
  /tiktok/category) route_allowed=true ;;
  /tiktok/comments) route_allowed=true ;;
  /tiktok/creative-center/hashtags) route_allowed=true ;;
  /tiktok/creative-center/videos) route_allowed=true ;;
  /tiktok/hashtags) route_allowed=true ;;
  /tiktok/popular-trend/country-industry-meta) route_allowed=true ;;
  /tiktok/posts) route_allowed=true ;;
  /tiktok/search) route_allowed=true ;;
  /tiktok/search/hashtag) route_allowed=true ;;
  /tiktok/search/user) route_allowed=true ;;
  /tiktok/top-ads/analysis) route_allowed=true ;;
  /tiktok/top-ads/detail) route_allowed=true ;;
  /tiktok/top-ads/filters) route_allowed=true ;;
  /tiktok/top-ads/list) route_allowed=true ;;
  /tiktok/top-ads/location-info) route_allowed=true ;;
  /tiktok/top-ads/locations) route_allowed=true ;;
  /tiktok/top-ads/recommend) route_allowed=true ;;
  /tiktok/top-ads/safety) route_allowed=true ;;
  /tiktok/top-ads/spotlight) route_allowed=true ;;
  /tiktok/top-ads/suggestions) route_allowed=true ;;
  /tiktok/trending) route_allowed=true ;;
  /tmdb/movie/list) route_allowed=true ;;
  /tmdb/person/list) route_allowed=true ;;
  /tmdb/search) route_allowed=true ;;
  /tmdb/tv/list) route_allowed=true ;;
  /tokopedia/autocomplete) route_allowed=true ;;
  /tokopedia/category) route_allowed=true ;;
  /tokopedia/home) route_allowed=true ;;
  /tokopedia/home/tabs) route_allowed=true ;;
  /tokopedia/product) route_allowed=true ;;
  /tokopedia/product/review-filters) route_allowed=true ;;
  /tokopedia/search) route_allowed=true ;;
  /tokopedia/search/filters) route_allowed=true ;;
  /tripadvisor/autocomplete) route_allowed=true ;;
  /tripadvisor/enums) route_allowed=true ;;
  /tripadvisor/hotels) route_allowed=true ;;
  /tripadvisor/place) route_allowed=true ;;
  /tripadvisor/reviews) route_allowed=true ;;
  /tripadvisor/search) route_allowed=true ;;
  /tripcom/hotels/search) route_allowed=true ;;
  /trustmrr/acquire) route_allowed=true ;;
  /trustmrr/categories) route_allowed=true ;;
  /trustmrr/leaderboard) route_allowed=true ;;
  /trustmrr/marketplace) route_allowed=true ;;
  /trustmrr/startups) route_allowed=true ;;
  /trustpilot/business-units/search) route_allowed=true ;;
  /trustpilot/categories) route_allowed=true ;;
  /trustpilot/categories/search) route_allowed=true ;;
  /twitch/channel) route_allowed=true ;;
  /twitch/clips) route_allowed=true ;;
  /twitch/schedule) route_allowed=true ;;
  /twitch/search) route_allowed=true ;;
  /twitch/streams) route_allowed=true ;;
  /twitch/team) route_allowed=true ;;
  /twitch/top-games) route_allowed=true ;;
  /twitch/videos) route_allowed=true ;;
  /twitch/vod-comments) route_allowed=true ;;
  /ubereats/feed) route_allowed=true ;;
  /ubereats/search) route_allowed=true ;;
  /ulta/categories) route_allowed=true ;;
  /ulta/category) route_allowed=true ;;
  /ulta/product/questions) route_allowed=true ;;
  /ulta/product/reviews) route_allowed=true ;;
  /ulta/search) route_allowed=true ;;
  /ulta/stores) route_allowed=true ;;
  /ulta/suggest) route_allowed=true ;;
  /upwork/search) route_allowed=true ;;
  /usptoppubs/detail) route_allowed=true ;;
  /usptoppubs/search) route_allowed=true ;;
  /vinted/brand) route_allowed=true ;;
  /vinted/brands) route_allowed=true ;;
  /vinted/catalog) route_allowed=true ;;
  /vinted/categories) route_allowed=true ;;
  /vinted/category) route_allowed=true ;;
  /vinted/item) route_allowed=true ;;
  /vinted/member) route_allowed=true ;;
  /walgreens/stores) route_allowed=true ;;
  /walmart/search) route_allowed=true ;;
  /wayfair/categories) route_allowed=true ;;
  /wayfair/category) route_allowed=true ;;
  /wendys/categories) route_allowed=true ;;
  /wendys/directory) route_allowed=true ;;
  /wendys/item) route_allowed=true ;;
  /wendys/menu) route_allowed=true ;;
  /wendys/nearby) route_allowed=true ;;
  /wendys/nutrition) route_allowed=true ;;
  /wendys/restaurant) route_allowed=true ;;
  /wendys/store) route_allowed=true ;;
  /wendys/store-menu) route_allowed=true ;;
  /wendys/time-slots) route_allowed=true ;;
  /whataburger/sitemap) route_allowed=true ;;
  /whataburger/store) route_allowed=true ;;
  /whatnot/browse) route_allowed=true ;;
  /whatnot/categories) route_allowed=true ;;
  /wingstop/delivery-store) route_allowed=true ;;
  /wingstop/directory) route_allowed=true ;;
  /wingstop/flavors) route_allowed=true ;;
  /wingstop/menu) route_allowed=true ;;
  /wingstop/nearby) route_allowed=true ;;
  /wingstop/store) route_allowed=true ;;
  /wish/categories) route_allowed=true ;;
  /wish/search) route_allowed=true ;;
  /wish/suggest) route_allowed=true ;;
  /wolt/cities) route_allowed=true ;;
  /wolt/collections) route_allowed=true ;;
  /wolt/restaurant) route_allowed=true ;;
  /wolt/restaurant/availability) route_allowed=true ;;
  /wolt/restaurant/menu) route_allowed=true ;;
  /wolt/restaurant/menu/search) route_allowed=true ;;
  /wolt/search) route_allowed=true ;;
  /wolt/search/filters) route_allowed=true ;;
  /yahoo-autos/article) route_allowed=true ;;
  /yahoo-autos/category) route_allowed=true ;;
  /yahoo-autos/home) route_allowed=true ;;
  /yahoo-entertainment/article) route_allowed=true ;;
  /yahoo-entertainment/category) route_allowed=true ;;
  /yahoo-entertainment/home) route_allowed=true ;;
  /yahoo-finance/calendars) route_allowed=true ;;
  /yahoo-finance/download) route_allowed=true ;;
  /yahoo-finance/industries) route_allowed=true ;;
  /yahoo-finance/lookup) route_allowed=true ;;
  /yahoo-finance/screener) route_allowed=true ;;
  /yahoo-finance/screeners) route_allowed=true ;;
  /yahoo-finance/search) route_allowed=true ;;
  /yahoo-finance/sectors) route_allowed=true ;;
  /yahoo-health/article) route_allowed=true ;;
  /yahoo-health/category) route_allowed=true ;;
  /yahoo-health/home) route_allowed=true ;;
  /yahoo-life/article) route_allowed=true ;;
  /yahoo-life/home) route_allowed=true ;;
  /yahoo-news/article) route_allowed=true ;;
  /yahoo-news/category) route_allowed=true ;;
  /yahoo-news/comments) route_allowed=true ;;
  /yahoo-news/comments/replies) route_allowed=true ;;
  /yahoo-news/home) route_allowed=true ;;
  /yahoo-news/suggest) route_allowed=true ;;
  /yahoo-search/images) route_allowed=true ;;
  /yahoo-search/local) route_allowed=true ;;
  /yahoo-search/news) route_allowed=true ;;
  /yahoo-search/search) route_allowed=true ;;
  /yahoo-search/suggest) route_allowed=true ;;
  /yahoo-search/videos) route_allowed=true ;;
  /yahoo-shopping/article) route_allowed=true ;;
  /yahoo-shopping/category) route_allowed=true ;;
  /yahoo-shopping/home) route_allowed=true ;;
  /yahoo-shopping/shopping-list) route_allowed=true ;;
  /yahoo-shopping/shopping-lists) route_allowed=true ;;
  /yahoo-shopping/store) route_allowed=true ;;
  /yahoo-shopping/stores) route_allowed=true ;;
  /yahoo-sports/game) route_allowed=true ;;
  /yahoo-sports/golf-leaderboard) route_allowed=true ;;
  /yahoo-sports/golf-schedule) route_allowed=true ;;
  /yahoo-sports/mma-fight-card) route_allowed=true ;;
  /yahoo-sports/mma-schedule) route_allowed=true ;;
  /yahoo-sports/motorsports-race) route_allowed=true ;;
  /yahoo-sports/motorsports-schedule) route_allowed=true ;;
  /yahoo-sports/news) route_allowed=true ;;
  /yahoo-sports/olympics-medals) route_allowed=true ;;
  /yahoo-sports/player) route_allowed=true ;;
  /yahoo-sports/scoreboard) route_allowed=true ;;
  /yahoo-sports/standings) route_allowed=true ;;
  /yahoo-sports/team) route_allowed=true ;;
  /yahoo-sports/team-roster) route_allowed=true ;;
  /yahoo-sports/team-schedule) route_allowed=true ;;
  /yahoo-sports/tennis-rankings) route_allowed=true ;;
  /yahoo-sports/tennis-schedule) route_allowed=true ;;
  /yahoo-sports/tennis-scoreboard) route_allowed=true ;;
  /yahoo-tech/article) route_allowed=true ;;
  /yahoo-tech/category) route_allowed=true ;;
  /yahoo-tech/home) route_allowed=true ;;
  /yelp/geocode) route_allowed=true ;;
  /yelp/search) route_allowed=true ;;
  /youtube/search) route_allowed=true ;;
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
  /zaxbys/menu) route_allowed=true ;;
  /zaxbys/nearby) route_allowed=true ;;
  /zaxbys/store) route_allowed=true ;;
  /zillow/autocomplete) route_allowed=true ;;
  /zillow/search) route_allowed=true ;;
  /zomato/collection) route_allowed=true ;;
  /zomato/collections) route_allowed=true ;;
  /zomato/restaurant) route_allowed=true ;;
  /zomato/restaurant/menu) route_allowed=true ;;
  /zomato/search) route_allowed=true ;;
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
  '^/allbirds/collections/[^/]+/products$'
  '^/allbirds/pages/[^/]+$'
  '^/allbirds/products/[^/]+$'
  '^/allbirds/products/[^/]+/recommendations$'
  '^/amazon/product/[^/]+$'
  '^/amazon/suggest/[^/]+$'
  '^/anime/character/[^/]+$'
  '^/anime/title/[^/]+$'
  '^/anime/title/[^/]+/characters$'
  '^/anime/title/[^/]+/recommendations$'
  '^/anime/title/[^/]+/staff$'
  '^/apple-books/audiobook-series/[^/]+$'
  '^/apple-books/audiobook/[^/]+$'
  '^/apple-books/audiobook/[^/]+/reviews$'
  '^/apple-books/audiobook/[^/]+/similar$'
  '^/apple-books/author/[^/]+$'
  '^/apple-books/book/[^/]+$'
  '^/apple-books/book/[^/]+/reviews$'
  '^/apple-books/book/[^/]+/similar$'
  '^/apple-books/series/[^/]+$'
  '^/apple-podcasts/show/[^/]+$'
  '^/apple-podcasts/show/[^/]+/episodes$'
  '^/apple-podcasts/show/[^/]+/related$'
  '^/appstore/developer/[^/]+$'
  '^/appstore/privacy/[^/]+$'
  '^/appstore/suggest/[^/]+$'
  '^/appstore/version-history/[^/]+$'
  '^/audible/category/[^/]+$'
  '^/audible/list/[^/]+$'
  '^/audible/product/[^/]+$'
  '^/audible/product/[^/]+/related$'
  '^/audible/product/[^/]+/reviews$'
  '^/audible/series/[^/]+$'
  '^/autotrader/dealer/[^/]+$'
  '^/autotrader/vehicle/[^/]+$'
  '^/bbb/scamtracker/[^/]+$'
  '^/bonhams/auctions/[^/]+$'
  '^/bonhams/auctions/[^/]+/lots$'
  '^/bonhams/lots/[^/]+/[^/]+$'
  '^/brooklinen/collections/[^/]+/products$'
  '^/brooklinen/pages/[^/]+$'
  '^/brooklinen/products/[^/]+$'
  '^/brooklinen/products/[^/]+/recommendations$'
  '^/carmax/store/[^/]+$'
  '^/carmax/vehicle/[^/]+$'
  '^/carmax/vehicle/[^/]+/recommendations$'
  '^/carsdotcom/vehicle/[^/]+$'
  '^/coingecko/category/[^/]+/coins$'
  '^/coingecko/chains/[^/]+$'
  '^/coingecko/coin/[^/]+$'
  '^/coingecko/coin/[^/]+/analysis$'
  '^/coingecko/exchange/[^/]+$'
  '^/coingecko/nft/category/[^/]+$'
  '^/colehaan/collections/[^/]+/products$'
  '^/colehaan/pages/[^/]+$'
  '^/colehaan/products/[^/]+$'
  '^/colehaan/products/[^/]+/recommendations$'
  '^/costco/product/[^/]+$'
  '^/costco/product/[^/]+/availability$'
  '^/costco/product/[^/]+/reviews$'
  '^/cvs/product-ingredients/[^/]+$'
  '^/cvs/product/[^/]+$'
  '^/depop/item/[^/]+$'
  '^/depop/item/[^/]+/similar$'
  '^/depop/shop/[^/]+$'
  '^/discogs/artist/[^/]+$'
  '^/discogs/artist/[^/]+/releases$'
  '^/discogs/label/[^/]+$'
  '^/discogs/label/[^/]+/releases$'
  '^/discogs/master/[^/]+$'
  '^/discogs/release/[^/]+$'
  '^/doordash/store/[^/]+$'
  '^/doordash/store/[^/]+/fulfillment$'
  '^/doordash/store/[^/]+/info$'
  '^/doordash/store/[^/]+/item/[^/]+$'
  '^/doordash/store/[^/]+/menu$'
  '^/doordash/store/[^/]+/reviews$'
  '^/ebay/item/[^/]+$'
  '^/ebay/live/streams/[^/]+$'
  '^/ebay/live/streams/[^/]+/items$'
  '^/ebay/seller/[^/]+$'
  '^/ebay/seller/[^/]+/about$'
  '^/ebay/seller/[^/]+/feedback$'
  '^/ebay/seller/[^/]+/shop$'
  '^/etsy/listing/[^/]+$'
  '^/etsy/listing/[^/]+/reviews$'
  '^/etsy/shop/[^/]+$'
  '^/etsy/shop/[^/]+/listings$'
  '^/etsy/shop/[^/]+/reviews$'
  '^/everlane/collections/[^/]+/products$'
  '^/everlane/pages/[^/]+$'
  '^/everlane/products/[^/]+$'
  '^/everlane/products/[^/]+/recommendations$'
  '^/facebook/[^/]+$'
  '^/fashionnova/collections/[^/]+/products$'
  '^/fashionnova/pages/[^/]+$'
  '^/fashionnova/products/[^/]+$'
  '^/fashionnova/products/[^/]+/recommendations$'
  '^/fiverr/gig/[^/]+/[^/]+$'
  '^/fiverr/seller/[^/]+$'
  '^/github/org/[^/]+$'
  '^/github/org/[^/]+/repos$'
  '^/github/repo/[^/]+/[^/]+$'
  '^/github/repo/[^/]+/[^/]+/contributors$'
  '^/github/repo/[^/]+/[^/]+/forks$'
  '^/github/repo/[^/]+/[^/]+/languages$'
  '^/github/repo/[^/]+/[^/]+/releases$'
  '^/github/user/[^/]+$'
  '^/github/user/[^/]+/events$'
  '^/github/user/[^/]+/followers$'
  '^/github/user/[^/]+/following$'
  '^/github/user/[^/]+/pinned$'
  '^/github/user/[^/]+/repos$'
  '^/goat/product/[^/]+$'
  '^/goat/product/[^/]+/recommended$'
  '^/goodreads/author/[^/]+$'
  '^/goodreads/author/[^/]+/books$'
  '^/goodreads/author/[^/]+/quotes$'
  '^/goodreads/book/[^/]+$'
  '^/goodreads/book/[^/]+/editions$'
  '^/goodreads/book/[^/]+/reviews$'
  '^/goodreads/genre/[^/]+$'
  '^/goodreads/list/[^/]+$'
  '^/google/finance/analyst-articles/[^/]+$'
  '^/google/finance/chart/[^/]+$'
  '^/google/finance/classification/[^/]+$'
  '^/google/finance/company/[^/]+$'
  '^/google/finance/financials/[^/]+$'
  '^/google/finance/markets/categories/[^/]+/news$'
  '^/google/finance/markets/categories/[^/]+/stocks$'
  '^/google/finance/news/[^/]+$'
  '^/google/finance/quote/[^/]+$'
  '^/google/finance/related/[^/]+$'
  '^/google/finance/ticker/[^/]+$'
  '^/google/map/place/[^/]+$'
  '^/google/map/place/[^/]+/photos$'
  '^/google/map/place/[^/]+/reviews$'
  '^/googleplay/developer/[^/]+$'
  '^/googleplay/suggest/[^/]+$'
  '^/gymshark/collections/[^/]+/products$'
  '^/gymshark/pages/[^/]+$'
  '^/gymshark/products/[^/]+$'
  '^/gymshark/products/[^/]+/recommendations$'
  '^/hm/product/[^/]+$'
  '^/hm/product/[^/]+/related$'
  '^/homedepot/product/[^/]+$'
  '^/homedepot/product/[^/]+/questions$'
  '^/instagram/post/[^/]+/[^/]+$'
  '^/instagram/profile/[^/]+$'
  '^/instagram/reels/[^/]+$'
  '^/kalshi/event/[^/]+$'
  '^/kalshi/event/[^/]+/history$'
  '^/kalshi/event/[^/]+/metadata$'
  '^/kalshi/historical/market/[^/]+$'
  '^/kalshi/historical/market/[^/]+/history$'
  '^/kalshi/market/[^/]+$'
  '^/kalshi/market/[^/]+/history$'
  '^/kalshi/market/[^/]+/orderbook$'
  '^/kalshi/series/[^/]+$'
  '^/kyliecosmetics/collections/[^/]+/products$'
  '^/kyliecosmetics/pages/[^/]+$'
  '^/kyliecosmetics/products/[^/]+$'
  '^/kyliecosmetics/products/[^/]+/recommendations$'
  '^/letterboxd/film/[^/]+$'
  '^/letterboxd/film/[^/]+/rating-histogram$'
  '^/letterboxd/film/[^/]+/reviews$'
  '^/letterboxd/film/[^/]+/similar$'
  '^/letterboxd/member/[^/]+$'
  '^/letterboxd/person/[^/]+$'
  '^/linkedin/company/[^/]+$'
  '^/linkedin/product/[^/]+$'
  '^/linkedin/showcase/[^/]+$'
  '^/lululemon/product/[^/]+$'
  '^/macys/product/[^/]+$'
  '^/manga/title/[^/]+$'
  '^/manga/title/[^/]+/characters$'
  '^/manga/title/[^/]+/recommendations$'
  '^/manga/title/[^/]+/staff$'
  '^/mercari/item/[^/]+$'
  '^/metacritic/game/[^/]+$'
  '^/metacritic/game/[^/]+/critic-reviews$'
  '^/metacritic/game/[^/]+/user-reviews$'
  '^/metacritic/movie/[^/]+$'
  '^/metacritic/movie/[^/]+/critic-reviews$'
  '^/metacritic/movie/[^/]+/user-reviews$'
  '^/metacritic/tv/[^/]+$'
  '^/metacritic/tv/[^/]+/critic-reviews$'
  '^/metacritic/tv/[^/]+/user-reviews$'
  '^/metaculus/category/[^/]+/questions$'
  '^/metaculus/project/[^/]+/questions$'
  '^/metaculus/question/[^/]+$'
  '^/metaculus/question/[^/]+/forecast-history$'
  '^/metaculus/question/[^/]+/forecasts$'
  '^/metaculus/question/[^/]+/metadata$'
  '^/metaculus/question/[^/]+/options$'
  '^/metaculus/tournament/[^/]+/questions$'
  '^/numbeo/cost-of-living/city/[^/]+$'
  '^/numbeo/indices/city/[^/]+$'
  '^/ohpolly/collections/[^/]+/products$'
  '^/ohpolly/pages/[^/]+$'
  '^/ohpolly/products/[^/]+$'
  '^/ohpolly/products/[^/]+/recommendations$'
  '^/opensea/collection/[^/]+$'
  '^/opensea/collection/[^/]+/activity$'
  '^/opensea/collection/[^/]+/best-deals$'
  '^/opensea/collection/[^/]+/chart$'
  '^/opensea/collection/[^/]+/depth$'
  '^/opensea/collection/[^/]+/holders$'
  '^/opensea/collection/[^/]+/items$'
  '^/opensea/collection/[^/]+/offers$'
  '^/opensea/collection/[^/]+/rarest-items$'
  '^/opensea/collection/[^/]+/search-items$'
  '^/opensea/collection/[^/]+/social-proof$'
  '^/opensea/collection/[^/]+/top-sales$'
  '^/opensea/collection/[^/]+/trait-offers$'
  '^/opensea/collection/[^/]+/traits$'
  '^/opensea/item/[^/]+/[^/]+/[^/]+$'
  '^/opensea/item/[^/]+/[^/]+/[^/]+/activity$'
  '^/opensea/item/[^/]+/[^/]+/[^/]+/chart$'
  '^/opensea/item/[^/]+/[^/]+/[^/]+/depth$'
  '^/opensea/item/[^/]+/[^/]+/[^/]+/listings$'
  '^/opensea/item/[^/]+/[^/]+/[^/]+/offers$'
  '^/opensea/item/[^/]+/[^/]+/[^/]+/owners$'
  '^/opensea/profile/[^/]+$'
  '^/opensea/profile/[^/]+/activity$'
  '^/opensea/profile/[^/]+/collections$'
  '^/opensea/profile/[^/]+/created$'
  '^/opensea/profile/[^/]+/items$'
  '^/opensea/profile/[^/]+/search-items$'
  '^/pinterest/board/[^/]+/[^/]+$'
  '^/pinterest/ideas/[^/]+$'
  '^/pinterest/pin/[^/]+$'
  '^/pinterest/user/[^/]+$'
  '^/pinterest/user/[^/]+/boards$'
  '^/pinterest/user/[^/]+/pins$'
  '^/polymarket/clob/market/[^/]+$'
  '^/polymarket/event/[^/]+$'
  '^/polymarket/events/[^/]+/tags$'
  '^/polymarket/market/[^/]+$'
  '^/polymarket/market/[^/]+/liquidity$'
  '^/polymarket/market/[^/]+/tags$'
  '^/polymarket/rewards/market/[^/]+$'
  '^/polymarket/tag/[^/]+$'
  '^/polymarket/tag/[^/]+/related-tags$'
  '^/polymarket/token/[^/]+/midpoint$'
  '^/polymarket/token/[^/]+/orderbook$'
  '^/polymarket/token/[^/]+/price$'
  '^/polymarket/token/[^/]+/price-history$'
  '^/polymarket/token/[^/]+/spread$'
  '^/poshmark/brand/[^/]+$'
  '^/poshmark/category/[^/]+$'
  '^/poshmark/closet/[^/]+$'
  '^/poshmark/listing/[^/]+$'
  '^/poshmark/trend/[^/]+$'
  '^/producthunt/category/[^/]+$'
  '^/producthunt/category/[^/]+/products$'
  '^/producthunt/product/[^/]+$'
  '^/producthunt/product/[^/]+/about$'
  '^/producthunt/product/[^/]+/alternatives$'
  '^/producthunt/product/[^/]+/customers$'
  '^/producthunt/product/[^/]+/launches$'
  '^/producthunt/product/[^/]+/makers$'
  '^/producthunt/product/[^/]+/reviews$'
  '^/reddit/comments/[^/]+$'
  '^/reddit/domain/[^/]+/posts$'
  '^/reddit/post/[^/]+$'
  '^/reddit/subreddit/[^/]+/about$'
  '^/reddit/subreddit/[^/]+/comments$'
  '^/reddit/subreddit/[^/]+/posts$'
  '^/reddit/user/[^/]+/comments$'
  '^/reddit/user/[^/]+/posts$'
  '^/rightmove/agents/[^/]+$'
  '^/rightmove/properties/[^/]+$'
  '^/rothys/collections/[^/]+/products$'
  '^/rothys/pages/[^/]+$'
  '^/rothys/products/[^/]+$'
  '^/rothys/products/[^/]+/recommendations$'
  '^/rover/sitter/[^/]+$'
  '^/rover/trainer/[^/]+$'
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
  '^/similarweb/web/[^/]+$'
  '^/skims/collections/[^/]+/products$'
  '^/skims/pages/[^/]+$'
  '^/skims/products/[^/]+$'
  '^/skims/products/[^/]+/recommendations$'
  '^/starbucks/product/[^/]+/[^/]+$'
  '^/starbucks/product/[^/]+/[^/]+/nutrition$'
  '^/steam/category/[^/]+$'
  '^/stevemadden/collections/[^/]+/products$'
  '^/stevemadden/pages/[^/]+$'
  '^/stevemadden/products/[^/]+$'
  '^/stevemadden/products/[^/]+/recommendations$'
  '^/stockx/product/[^/]+$'
  '^/strava/clubs/[^/]+$'
  '^/thebodyshop/collections/[^/]+/products$'
  '^/thebodyshop/pages/[^/]+$'
  '^/thebodyshop/products/[^/]+$'
  '^/thebodyshop/products/[^/]+/recommendations$'
  '^/threads/post/[^/]+/[^/]+$'
  '^/threads/post/[^/]+/[^/]+/replies$'
  '^/threads/profile/[^/]+$'
  '^/threads/profile/[^/]+/posts$'
  '^/tiktok/explore/[^/]+$'
  '^/tiktok/hashtag/[^/]+$'
  '^/tiktok/post/[^/]+$'
  '^/tiktok/profile/[^/]+$'
  '^/tmdb/movie/[^/]+$'
  '^/tmdb/person/[^/]+$'
  '^/tmdb/tv/[^/]+$'
  '^/tripcom/hotels/[^/]+$'
  '^/trustmrr/category/[^/]+$'
  '^/trustmrr/startup/[^/]+$'
  '^/trustpilot/business/[^/]+$'
  '^/trustpilot/business/[^/]+/related$'
  '^/trustpilot/business/[^/]+/reviews$'
  '^/trustpilot/category/[^/]+$'
  '^/ubereats/store/[^/]+$'
  '^/ubereats/store/[^/]+/menu$'
  '^/ubereats/store/[^/]+/reviews$'
  '^/ulta/product/[^/]+$'
  '^/upwork/freelancer/[^/]+$'
  '^/upwork/job/[^/]+$'
  '^/walmart/product/[^/]+$'
  '^/walmart/product/[^/]+/reviews$'
  '^/wayfair/product/[^/]+$'
  '^/whatnot/live/[^/]+$'
  '^/wish/product/[^/]+$'
  '^/wish/product/[^/]+/related$'
  '^/wish/product/[^/]+/reviews$'
  '^/x/post/[^/]+$'
  '^/x/profile/[^/]+$'
  '^/x/profile/[^/]+/posts$'
  '^/yahoo-finance/calendars/[^/]+$'
  '^/yahoo-finance/industries/[^/]+$'
  '^/yahoo-finance/market/[^/]+/status$'
  '^/yahoo-finance/market/[^/]+/summary$'
  '^/yahoo-finance/screener/[^/]+$'
  '^/yahoo-finance/sectors/[^/]+$'
  '^/yahoo-finance/ticker/[^/]+/actions$'
  '^/yahoo-finance/ticker/[^/]+/analysts$'
  '^/yahoo-finance/ticker/[^/]+/calendar$'
  '^/yahoo-finance/ticker/[^/]+/capital-gains$'
  '^/yahoo-finance/ticker/[^/]+/dividends$'
  '^/yahoo-finance/ticker/[^/]+/earnings$'
  '^/yahoo-finance/ticker/[^/]+/earnings-dates$'
  '^/yahoo-finance/ticker/[^/]+/financials$'
  '^/yahoo-finance/ticker/[^/]+/funds$'
  '^/yahoo-finance/ticker/[^/]+/history$'
  '^/yahoo-finance/ticker/[^/]+/history-metadata$'
  '^/yahoo-finance/ticker/[^/]+/holders$'
  '^/yahoo-finance/ticker/[^/]+/info$'
  '^/yahoo-finance/ticker/[^/]+/isin$'
  '^/yahoo-finance/ticker/[^/]+/news$'
  '^/yahoo-finance/ticker/[^/]+/options$'
  '^/yahoo-finance/ticker/[^/]+/options/[^/]+$'
  '^/yahoo-finance/ticker/[^/]+/quote$'
  '^/yahoo-finance/ticker/[^/]+/sec-filings$'
  '^/yahoo-finance/ticker/[^/]+/shares$'
  '^/yahoo-finance/ticker/[^/]+/shares-full$'
  '^/yahoo-finance/ticker/[^/]+/splits$'
  '^/yahoo-finance/ticker/[^/]+/sustainability$'
  '^/yahoo-finance/ticker/[^/]+/valuation$'
  '^/yahoo-finance/trending/[^/]+$'
  '^/yelp/business/[^/]+$'
  '^/yelp/business/[^/]+/menu$'
  '^/yelp/business/[^/]+/photos$'
  '^/yelp/business/[^/]+/reviews$'
  '^/yelp/business/[^/]+/reviews/highlights$'
  '^/yelp/business/[^/]+/reviews/search$'
  '^/youtube/captions/[^/]+$'
  '^/youtube/channel/[^/]+/playlists$'
  '^/youtube/channel/[^/]+/search$'
  '^/youtube/channel/[^/]+/shorts$'
  '^/youtube/channel/[^/]+/videos$'
  '^/youtube/comments/[^/]+$'
  '^/youtube/playlist/[^/]+$'
  '^/youtube/profile/[^/]+$'
  '^/youtube/tag/[^/]+$'
  '^/youtube/transcript/[^/]+$'
  '^/youtube/transcript/[^/]+/languages$'
  '^/youtube/video/[^/]+$'
  '^/zappos/product/[^/]+$'
  '^/zara/category/[^/]+/products$'
  '^/zara/product/[^/]+$'
  '^/zillow/property/[^/]+$'
  )
  for route_regex in ${route_regexes[@]+"${route_regexes[@]}"}; do
    if [[ "$path" =~ $route_regex ]]; then
      route_allowed=true
      break
    fi
  done
fi
if [ "$route_allowed" = false ]; then
  echo "path is not in the crawlora skill catalog" >&2
  exit 2
fi

# Enforce the documented HTTP method for each route, not just the global method set.
route_method_allowed=false
route_method_regexes=(
  '^GET:/7now/catalog$'
  '^GET:/7now/categories$'
  '^GET:/7now/category$'
  '^GET:/7now/combo$'
  '^GET:/7now/combos$'
  '^GET:/7now/deals$'
  '^GET:/7now/offers$'
  '^GET:/7now/popular$'
  '^GET:/7now/product$'
  '^GET:/7now/promotion$'
  '^GET:/7now/search$'
  '^GET:/7now/stores$'
  '^GET:/7now/suggest$'
  '^GET:/accor/amenities$'
  '^GET:/accor/brands$'
  '^GET:/accor/catalog/hotels$'
  '^GET:/accor/destination/hotels$'
  '^GET:/accor/property$'
  '^GET:/accor/search$'
  '^GET:/accor/search/details$'
  '^GET:/accor/search/suggest$'
  '^GET:/adidas/product$'
  '^GET:/adidas/product/review-topics$'
  '^GET:/adidas/product/reviews$'
  '^GET:/adidas/search$'
  '^GET:/adidas/store$'
  '^GET:/adidas/stores$'
  '^GET:/adidas/suggest$'
  '^GET:/agoda/activities/[^/]+$'
  '^GET:/agoda/activities/search$'
  '^GET:/agoda/flights/search$'
  '^GET:/agoda/flights/search-locations$'
  '^GET:/agoda/homes/search$'
  '^GET:/agoda/hotels/[^/]+$'
  '^GET:/agoda/hotels/search$'
  '^GET:/airbnb/host/[^/]+$'
  '^GET:/airbnb/host/[^/]+/listings$'
  '^GET:/airbnb/host/[^/]+/reviews$'
  '^GET:/airbnb/room/[^/]+$'
  '^GET:/airbnb/room/[^/]+/calendar$'
  '^GET:/airbnb/room/[^/]+/reviews$'
  '^GET:/airbnb/search$'
  '^GET:/allbirds/collections$'
  '^GET:/allbirds/collections/[^/]+/products$'
  '^GET:/allbirds/pages$'
  '^GET:/allbirds/pages/[^/]+$'
  '^GET:/allbirds/products$'
  '^GET:/allbirds/products/[^/]+$'
  '^GET:/allbirds/products/[^/]+/recommendations$'
  '^GET:/allbirds/search/suggest$'
  '^GET:/allbirds/sitemap/urls$'
  '^GET:/allbirds/sitemaps$'
  '^GET:/allbirds/store$'
  '^GET:/amazon-jobs/job$'
  '^GET:/amazon-jobs/search$'
  '^GET:/amazon/product/[^/]+$'
  '^GET:/amazon/search$'
  '^GET:/amazon/suggest/[^/]+$'
  '^GET:/anime/airing-schedule$'
  '^GET:/anime/character/[^/]+$'
  '^GET:/anime/character/search$'
  '^GET:/anime/rankings$'
  '^GET:/anime/search$'
  '^GET:/anime/title/[^/]+$'
  '^GET:/anime/title/[^/]+/characters$'
  '^GET:/anime/title/[^/]+/recommendations$'
  '^GET:/anime/title/[^/]+/staff$'
  '^GET:/apple-books/audiobook-series/[^/]+$'
  '^GET:/apple-books/audiobook/[^/]+$'
  '^GET:/apple-books/audiobook/[^/]+/reviews$'
  '^GET:/apple-books/audiobook/[^/]+/similar$'
  '^GET:/apple-books/audiobook/search$'
  '^GET:/apple-books/author/[^/]+$'
  '^GET:/apple-books/book/[^/]+$'
  '^GET:/apple-books/book/[^/]+/reviews$'
  '^GET:/apple-books/book/[^/]+/similar$'
  '^GET:/apple-books/charts$'
  '^GET:/apple-books/search$'
  '^GET:/apple-books/series/[^/]+$'
  '^GET:/apple-jobs/job$'
  '^GET:/apple-jobs/search$'
  '^GET:/apple-maps/autocomplete$'
  '^GET:/apple-maps/categories$'
  '^GET:/apple-maps/category-search$'
  '^GET:/apple-maps/directions$'
  '^GET:/apple-maps/eta$'
  '^GET:/apple-maps/guides$'
  '^GET:/apple-maps/guides/cities$'
  '^GET:/apple-maps/guides/guide$'
  '^GET:/apple-maps/guides/lookup$'
  '^GET:/apple-maps/guides/nearby$'
  '^GET:/apple-maps/guides/publisher$'
  '^GET:/apple-maps/guides/publishers$'
  '^GET:/apple-maps/place$'
  '^GET:/apple-maps/place/photos$'
  '^GET:/apple-maps/places$'
  '^GET:/apple-maps/reverse-geocode$'
  '^GET:/apple-maps/search$'
  '^GET:/apple-maps/transit-departures$'
  '^GET:/apple-maps/venue/browse$'
  '^GET:/apple-podcasts/charts$'
  '^GET:/apple-podcasts/charts/rankings$'
  '^GET:/apple-podcasts/episodes/search$'
  '^GET:/apple-podcasts/new$'
  '^GET:/apple-podcasts/search$'
  '^GET:/apple-podcasts/show/[^/]+$'
  '^GET:/apple-podcasts/show/[^/]+/episodes$'
  '^GET:/apple-podcasts/show/[^/]+/related$'
  '^GET:/appstore/app$'
  '^GET:/appstore/developer/[^/]+$'
  '^GET:/appstore/editorial$'
  '^GET:/appstore/editorial/category$'
  '^GET:/appstore/list$'
  '^GET:/appstore/privacy/[^/]+$'
  '^GET:/appstore/ratings$'
  '^GET:/appstore/reviews$'
  '^GET:/appstore/search$'
  '^GET:/appstore/similar$'
  '^GET:/appstore/suggest/[^/]+$'
  '^GET:/appstore/version-history/[^/]+$'
  '^GET:/arbys/categories$'
  '^GET:/arbys/directory$'
  '^GET:/arbys/location$'
  '^GET:/arbys/locations$'
  '^GET:/arbys/menu$'
  '^GET:/audible/categories$'
  '^GET:/audible/category/[^/]+$'
  '^GET:/audible/charts$'
  '^GET:/audible/list/[^/]+$'
  '^GET:/audible/product/[^/]+$'
  '^GET:/audible/product/[^/]+/related$'
  '^GET:/audible/product/[^/]+/reviews$'
  '^GET:/audible/products$'
  '^GET:/audible/search$'
  '^GET:/audible/series/[^/]+$'
  '^GET:/autotrader/dealer/[^/]+$'
  '^GET:/autotrader/search$'
  '^GET:/autotrader/vehicle/[^/]+$'
  '^GET:/bbb/business$'
  '^GET:/bbb/business/complaints$'
  '^GET:/bbb/business/more-info$'
  '^GET:/bbb/business/reviews$'
  '^GET:/bbb/category$'
  '^GET:/bbb/scamtracker/[^/]+$'
  '^GET:/bbb/scamtracker/search$'
  '^GET:/bbb/scamtracker/state-stats$'
  '^GET:/bbb/search$'
  '^GET:/bbc/article$'
  '^GET:/bbc/headlines$'
  '^GET:/bbc/live$'
  '^GET:/bbc/search$'
  '^GET:/bestbuy/brands$'
  '^GET:/bestbuy/categories$'
  '^GET:/bestbuy/categories/trending$'
  '^GET:/bestbuy/category$'
  '^GET:/bestbuy/category/subcategories$'
  '^GET:/bestbuy/product$'
  '^GET:/bestbuy/product/questions$'
  '^GET:/bestbuy/product/related$'
  '^GET:/bestbuy/product/reviews$'
  '^GET:/bestbuy/search$'
  '^GET:/bestbuy/stores$'
  '^GET:/bigcommerce/category$'
  '^GET:/bigcommerce/product$'
  '^GET:/bigcommerce/search$'
  '^GET:/bilibili/anime-home$'
  '^GET:/bilibili/autocomplete$'
  '^GET:/bilibili/guochuang-home$'
  '^GET:/bilibili/must-watch$'
  '^GET:/bilibili/popular$'
  '^GET:/bilibili/ranking$'
  '^GET:/bilibili/vertical-home$'
  '^GET:/bilibili/weekly$'
  '^GET:/bing/images$'
  '^GET:/bing/news$'
  '^GET:/bing/search$'
  '^GET:/bing/suggest$'
  '^GET:/bing/videos$'
  '^GET:/bluesky/author-feed$'
  '^GET:/bluesky/followers$'
  '^GET:/bluesky/follows$'
  '^GET:/bluesky/post-thread$'
  '^GET:/bluesky/profile$'
  '^GET:/bluesky/search-actors$'
  '^GET:/bluesky/trending-topics$'
  '^GET:/bonhams/auctions/[^/]+$'
  '^GET:/bonhams/auctions/[^/]+/lots$'
  '^GET:/bonhams/auctions/search$'
  '^GET:/bonhams/lots/[^/]+/[^/]+$'
  '^GET:/bonhams/lots/search$'
  '^GET:/booking-attractions/detail$'
  '^GET:/booking-attractions/reviews$'
  '^GET:/booking-attractions/search$'
  '^GET:/booking-flights/autocomplete$'
  '^GET:/booking-flights/search$'
  '^GET:/booking/hotel-detail$'
  '^GET:/booking/reviews$'
  '^GET:/booking/search$'
  '^GET:/boots/search$'
  '^GET:/boots/suggest$'
  '^GET:/boxofficemojo/brand$'
  '^GET:/boxofficemojo/brands$'
  '^GET:/boxofficemojo/calendar$'
  '^GET:/boxofficemojo/calendar/changes$'
  '^GET:/boxofficemojo/calendar/date$'
  '^GET:/boxofficemojo/date/domestic$'
  '^GET:/boxofficemojo/franchise$'
  '^GET:/boxofficemojo/franchises$'
  '^GET:/boxofficemojo/genre$'
  '^GET:/boxofficemojo/genres$'
  '^GET:/boxofficemojo/lifetime-grosses$'
  '^GET:/boxofficemojo/release$'
  '^GET:/boxofficemojo/release-group$'
  '^GET:/boxofficemojo/showdown$'
  '^GET:/boxofficemojo/showdowns$'
  '^GET:/boxofficemojo/title$'
  '^GET:/boxofficemojo/weekend/domestic$'
  '^GET:/boxofficemojo/weekend/domestic/by-distributor$'
  '^GET:/boxofficemojo/weekend/domestic/estimates$'
  '^GET:/boxofficemojo/year/domestic$'
  '^GET:/boxofficemojo/year/worldwide$'
  '^GET:/brand/retrieve$'
  '^GET:/brave/images$'
  '^GET:/brave/news$'
  '^GET:/brave/search$'
  '^GET:/brave/suggest$'
  '^GET:/brave/videos$'
  '^GET:/brooklinen/collections$'
  '^GET:/brooklinen/collections/[^/]+/products$'
  '^GET:/brooklinen/pages$'
  '^GET:/brooklinen/pages/[^/]+$'
  '^GET:/brooklinen/products$'
  '^GET:/brooklinen/products/[^/]+$'
  '^GET:/brooklinen/products/[^/]+/recommendations$'
  '^GET:/brooklinen/search/suggest$'
  '^GET:/brooklinen/sitemap/urls$'
  '^GET:/brooklinen/sitemaps$'
  '^GET:/brooklinen/store$'
  '^GET:/burgerking/availability$'
  '^GET:/burgerking/locations$'
  '^GET:/burgerking/menu$'
  '^GET:/burgerking/product$'
  '^GET:/capterra/product$'
  '^GET:/capterra/product/reviews$'
  '^GET:/capterra/search$'
  '^GET:/carmax/search$'
  '^GET:/carmax/search/suggestions$'
  '^GET:/carmax/shop-by-brand$'
  '^GET:/carmax/store/[^/]+$'
  '^GET:/carmax/stores$'
  '^GET:/carmax/vehicle/[^/]+$'
  '^GET:/carmax/vehicle/[^/]+/recommendations$'
  '^GET:/carsdotcom/search$'
  '^GET:/carsdotcom/vehicle/[^/]+$'
  '^GET:/chewy/brands$'
  '^GET:/chewy/categories$'
  '^GET:/chewy/category$'
  '^GET:/chewy/facets$'
  '^GET:/chewy/gtin-lookup$'
  '^GET:/chewy/inventory$'
  '^GET:/chewy/item-attributes$'
  '^GET:/chewy/product$'
  '^GET:/chewy/product-questions$'
  '^GET:/chewy/product-reviews$'
  '^GET:/chewy/products$'
  '^GET:/chewy/search$'
  '^GET:/chewy/suggest$'
  '^GET:/chewy/variants$'
  '^GET:/chick-fil-a/content$'
  '^GET:/chick-fil-a/content-taxonomy$'
  '^GET:/chick-fil-a/faq$'
  '^GET:/chick-fil-a/location$'
  '^GET:/chick-fil-a/locations$'
  '^GET:/chick-fil-a/menu$'
  '^GET:/chick-fil-a/menu-item$'
  '^GET:/chick-fil-a/menu-taxonomy$'
  '^GET:/chipotle/ingredients$'
  '^GET:/chipotle/meals$'
  '^GET:/chipotle/menu$'
  '^GET:/chipotle/menu/metadata$'
  '^GET:/chipotle/restaurant$'
  '^GET:/chipotle/restaurant/meals$'
  '^GET:/chipotle/restaurant/menu$'
  '^GET:/chipotle/restaurants$'
  '^GET:/chromewebstore/categories$'
  '^GET:/chromewebstore/category$'
  '^GET:/chromewebstore/charts$'
  '^GET:/chromewebstore/collection$'
  '^GET:/chromewebstore/developer$'
  '^GET:/chromewebstore/item$'
  '^GET:/chromewebstore/permissions$'
  '^GET:/chromewebstore/privacy$'
  '^GET:/chromewebstore/reviews$'
  '^GET:/chromewebstore/search$'
  '^GET:/chromewebstore/similar$'
  '^GET:/chromewebstore/suggest$'
  '^GET:/cnn/article$'
  '^GET:/cnn/headlines$'
  '^GET:/cnn/live-story$'
  '^GET:/coingecko/categories$'
  '^GET:/coingecko/category/[^/]+/coins$'
  '^GET:/coingecko/chains$'
  '^GET:/coingecko/chains/[^/]+$'
  '^GET:/coingecko/coin/[^/]+$'
  '^GET:/coingecko/coin/[^/]+/analysis$'
  '^GET:/coingecko/exchange/[^/]+$'
  '^GET:/coingecko/exchanges$'
  '^GET:/coingecko/gainers-losers$'
  '^GET:/coingecko/global$'
  '^GET:/coingecko/global/charts$'
  '^GET:/coingecko/learn/articles$'
  '^GET:/coingecko/markets$'
  '^GET:/coingecko/new-coins$'
  '^GET:/coingecko/news$'
  '^GET:/coingecko/nft/category/[^/]+$'
  '^GET:/coingecko/nfts$'
  '^GET:/coingecko/search$'
  '^GET:/coingecko/token-unlocks$'
  '^GET:/coingecko/treasuries$'
  '^GET:/coingecko/trending$'
  '^GET:/colehaan/collections$'
  '^GET:/colehaan/collections/[^/]+/products$'
  '^GET:/colehaan/pages$'
  '^GET:/colehaan/pages/[^/]+$'
  '^GET:/colehaan/products$'
  '^GET:/colehaan/products/[^/]+$'
  '^GET:/colehaan/products/[^/]+/recommendations$'
  '^GET:/colehaan/search/suggest$'
  '^GET:/colehaan/sitemap/urls$'
  '^GET:/colehaan/sitemaps$'
  '^GET:/colehaan/store$'
  '^GET:/congress/report$'
  '^GET:/congress/stock-disclosures$'
  '^GET:/costco/categories$'
  '^GET:/costco/product/[^/]+$'
  '^GET:/costco/product/[^/]+/availability$'
  '^GET:/costco/product/[^/]+/reviews$'
  '^GET:/costco/search$'
  '^GET:/costco/warehouses$'
  '^GET:/courtlistener/courts$'
  '^GET:/courtlistener/people$'
  '^GET:/courtlistener/search$'
  '^GET:/cricinfo/calendar$'
  '^GET:/cricinfo/commentary$'
  '^GET:/cricinfo/grounds$'
  '^GET:/cricinfo/live$'
  '^GET:/cricinfo/match$'
  '^GET:/cricinfo/news$'
  '^GET:/cricinfo/photos$'
  '^GET:/cricinfo/rankings$'
  '^GET:/cricinfo/records$'
  '^GET:/cricinfo/records/index$'
  '^GET:/cricinfo/rss$'
  '^GET:/cricinfo/scores$'
  '^GET:/cricinfo/series$'
  '^GET:/cricinfo/squads$'
  '^GET:/cricinfo/stats$'
  '^GET:/cricinfo/story$'
  '^GET:/cricinfo/team$'
  '^GET:/cricinfo/team/schedule$'
  '^GET:/cricinfo/teams$'
  '^GET:/cricinfo/venue$'
  '^GET:/cricinfo/venue/matches$'
  '^GET:/cricinfo/videos$'
  '^GET:/culvers/calendar$'
  '^GET:/culvers/categories$'
  '^GET:/culvers/directory$'
  '^GET:/culvers/flavor$'
  '^GET:/culvers/item$'
  '^GET:/culvers/menu$'
  '^GET:/culvers/store$'
  '^GET:/cvs/brands$'
  '^GET:/cvs/categories$'
  '^GET:/cvs/category$'
  '^GET:/cvs/product-ingredients/[^/]+$'
  '^GET:/cvs/product/[^/]+$'
  '^GET:/cvs/search$'
  '^GET:/cvs/store-locator$'
  '^GET:/deliveroo/fulfillment-times$'
  '^GET:/deliveroo/restaurant$'
  '^GET:/deliveroo/restaurant/menu$'
  '^GET:/deliveroo/search$'
  '^GET:/deliveroo/search/filters$'
  '^GET:/depop/brands$'
  '^GET:/depop/categories$'
  '^GET:/depop/item/[^/]+$'
  '^GET:/depop/item/[^/]+/similar$'
  '^GET:/depop/search$'
  '^GET:/depop/search-sellers$'
  '^GET:/depop/search/facets$'
  '^GET:/depop/shop/[^/]+$'
  '^GET:/depop/sizes$'
  '^GET:/depop/suggest$'
  '^GET:/discogs/artist/[^/]+$'
  '^GET:/discogs/artist/[^/]+/releases$'
  '^GET:/discogs/label/[^/]+$'
  '^GET:/discogs/label/[^/]+/releases$'
  '^GET:/discogs/master/[^/]+$'
  '^GET:/discogs/release/[^/]+$'
  '^GET:/discogs/search$'
  '^GET:/dominos/coupons$'
  '^GET:/dominos/customization$'
  '^GET:/dominos/menu$'
  '^GET:/dominos/nutrition$'
  '^GET:/dominos/store$'
  '^GET:/dominos/store-locator$'
  '^GET:/doordash/explore$'
  '^GET:/doordash/feed$'
  '^GET:/doordash/search$'
  '^GET:/doordash/search/autocomplete$'
  '^GET:/doordash/search/filters$'
  '^GET:/doordash/search/items$'
  '^GET:/doordash/store/[^/]+$'
  '^GET:/doordash/store/[^/]+/fulfillment$'
  '^GET:/doordash/store/[^/]+/info$'
  '^GET:/doordash/store/[^/]+/item/[^/]+$'
  '^GET:/doordash/store/[^/]+/menu$'
  '^GET:/doordash/store/[^/]+/reviews$'
  '^GET:/draftkings/sportsbook/event$'
  '^GET:/draftkings/sportsbook/event-context$'
  '^GET:/draftkings/sportsbook/event-markets$'
  '^GET:/draftkings/sportsbook/featured-leagues$'
  '^GET:/draftkings/sportsbook/futures$'
  '^GET:/draftkings/sportsbook/league-events$'
  '^GET:/draftkings/sportsbook/leagues$'
  '^GET:/draftkings/sportsbook/live$'
  '^GET:/draftkings/sportsbook/odds$'
  '^GET:/draftkings/sportsbook/quick-links$'
  '^GET:/draftkings/sportsbook/team$'
  '^GET:/draftkings/sportsbook/teams$'
  '^GET:/duckduckgo/image$'
  '^GET:/duckduckgo/news$'
  '^GET:/duckduckgo/search$'
  '^GET:/duckduckgo/shopping$'
  '^GET:/duckduckgo/video$'
  '^GET:/dunkin/directory$'
  '^GET:/dunkin/menu$'
  '^GET:/dunkin/nearby$'
  '^GET:/dunkin/store$'
  '^GET:/ebay/item/[^/]+$'
  '^GET:/ebay/live/streams$'
  '^GET:/ebay/live/streams/[^/]+$'
  '^GET:/ebay/live/streams/[^/]+/items$'
  '^GET:/ebay/live/streams/batch$'
  '^GET:/ebay/seller/[^/]+$'
  '^GET:/ebay/seller/[^/]+/about$'
  '^GET:/ebay/seller/[^/]+/feedback$'
  '^GET:/ebay/seller/[^/]+/shop$'
  '^GET:/espn/athlete$'
  '^GET:/espn/game-summary$'
  '^GET:/espn/news$'
  '^GET:/espn/rankings$'
  '^GET:/espn/scoreboard$'
  '^GET:/espn/standings$'
  '^GET:/espn/team$'
  '^GET:/espn/team-roster$'
  '^GET:/espn/teams$'
  '^GET:/etsy/listing/[^/]+$'
  '^GET:/etsy/listing/[^/]+/reviews$'
  '^GET:/etsy/search$'
  '^GET:/etsy/shop/[^/]+$'
  '^GET:/etsy/shop/[^/]+/listings$'
  '^GET:/etsy/shop/[^/]+/reviews$'
  '^GET:/etsy/shop/search$'
  '^GET:/everlane/collections$'
  '^GET:/everlane/collections/[^/]+/products$'
  '^GET:/everlane/pages$'
  '^GET:/everlane/pages/[^/]+$'
  '^GET:/everlane/products$'
  '^GET:/everlane/products/[^/]+$'
  '^GET:/everlane/products/[^/]+/recommendations$'
  '^GET:/everlane/search/suggest$'
  '^GET:/everlane/sitemap/urls$'
  '^GET:/everlane/sitemaps$'
  '^GET:/everlane/store$'
  '^GET:/facebook/[^/]+$'
  '^GET:/facebook/marketplace/search$'
  '^GET:/fashionnova/collections$'
  '^GET:/fashionnova/collections/[^/]+/products$'
  '^GET:/fashionnova/pages$'
  '^GET:/fashionnova/pages/[^/]+$'
  '^GET:/fashionnova/products$'
  '^GET:/fashionnova/products/[^/]+$'
  '^GET:/fashionnova/products/[^/]+/recommendations$'
  '^GET:/fashionnova/search/suggest$'
  '^GET:/fashionnova/sitemap/urls$'
  '^GET:/fashionnova/sitemaps$'
  '^GET:/fashionnova/store$'
  '^GET:/fiveguys/directory$'
  '^GET:/fiveguys/faq$'
  '^GET:/fiveguys/faq-categories$'
  '^GET:/fiveguys/menu$'
  '^GET:/fiveguys/nearby$'
  '^GET:/fiveguys/nutrition$'
  '^GET:/fiveguys/ordering-locations$'
  '^GET:/fiveguys/ordering-menu$'
  '^GET:/fiveguys/search$'
  '^GET:/fiveguys/store$'
  '^GET:/fiverr/gig/[^/]+/[^/]+$'
  '^GET:/fiverr/search$'
  '^GET:/fiverr/seller/[^/]+$'
  '^GET:/foodpanda/restaurant$'
  '^GET:/foodpanda/restaurant/menu$'
  '^GET:/foodpanda/restaurant/reviews$'
  '^GET:/foodpanda/search$'
  '^GET:/gdelt/context$'
  '^GET:/gdelt/search$'
  '^GET:/gdelt/timeline$'
  '^GET:/gdelt/tonechart$'
  '^GET:/gdelt/tv-concept-entities$'
  '^GET:/gdelt/tv-search$'
  '^GET:/gdelt/tv-showchart$'
  '^GET:/gdelt/tv-stationchart$'
  '^GET:/gdelt/tv-stationdetails$'
  '^GET:/gdelt/tv-timeline$'
  '^GET:/gdelt/tv-visual-entities$'
  '^GET:/gdelt/tv-wordcloud$'
  '^GET:/geocoding/lookup$'
  '^GET:/geocoding/reverse$'
  '^GET:/geocoding/search$'
  '^GET:/github/org/[^/]+$'
  '^GET:/github/org/[^/]+/repos$'
  '^GET:/github/repo/[^/]+/[^/]+$'
  '^GET:/github/repo/[^/]+/[^/]+/contributors$'
  '^GET:/github/repo/[^/]+/[^/]+/forks$'
  '^GET:/github/repo/[^/]+/[^/]+/languages$'
  '^GET:/github/repo/[^/]+/[^/]+/releases$'
  '^GET:/github/search/repositories$'
  '^GET:/github/search/users$'
  '^GET:/github/trending$'
  '^GET:/github/trending/developers$'
  '^GET:/github/user/[^/]+$'
  '^GET:/github/user/[^/]+/events$'
  '^GET:/github/user/[^/]+/followers$'
  '^GET:/github/user/[^/]+/following$'
  '^GET:/github/user/[^/]+/pinned$'
  '^GET:/github/user/[^/]+/repos$'
  '^GET:/goat/collection$'
  '^GET:/goat/countries$'
  '^GET:/goat/curated$'
  '^GET:/goat/listings/count$'
  '^GET:/goat/product/[^/]+$'
  '^GET:/goat/product/[^/]+/recommended$'
  '^GET:/goat/search$'
  '^GET:/goat/search/facets$'
  '^GET:/goat/searches/trending$'
  '^GET:/goat/suggest$'
  '^GET:/goodreads/author/[^/]+$'
  '^GET:/goodreads/author/[^/]+/books$'
  '^GET:/goodreads/author/[^/]+/quotes$'
  '^GET:/goodreads/book/[^/]+$'
  '^GET:/goodreads/book/[^/]+/editions$'
  '^GET:/goodreads/book/[^/]+/reviews$'
  '^GET:/goodreads/genre/[^/]+$'
  '^GET:/goodreads/list/[^/]+$'
  '^GET:/goodreads/lists$'
  '^GET:/goodreads/search$'
  '^GET:/google-jobs/job$'
  '^GET:/google-jobs/search$'
  '^GET:/google/finance/analyst-articles/[^/]+$'
  '^GET:/google/finance/chart/[^/]+$'
  '^GET:/google/finance/classification/[^/]+$'
  '^GET:/google/finance/company/[^/]+$'
  '^GET:/google/finance/context$'
  '^GET:/google/finance/financials/[^/]+$'
  '^GET:/google/finance/markets/categories/[^/]+/news$'
  '^GET:/google/finance/markets/categories/[^/]+/stocks$'
  '^GET:/google/finance/markets/earnings$'
  '^GET:/google/finance/markets/featured$'
  '^GET:/google/finance/markets/headline$'
  '^GET:/google/finance/markets/indices$'
  '^GET:/google/finance/markets/movers$'
  '^GET:/google/finance/markets/top$'
  '^GET:/google/finance/markets/trending$'
  '^GET:/google/finance/news/[^/]+$'
  '^GET:/google/finance/quote/[^/]+$'
  '^GET:/google/finance/related/[^/]+$'
  '^GET:/google/finance/search$'
  '^GET:/google/finance/ticker/[^/]+$'
  '^GET:/google/map/place/[^/]+$'
  '^GET:/google/map/place/[^/]+/photos$'
  '^GET:/google/map/place/[^/]+/reviews$'
  '^GET:/google/news$'
  '^GET:/google/suggest$'
  '^GET:/google/trends/categories$'
  '^GET:/google/trends/enums$'
  '^GET:/google/trends/locations$'
  '^GET:/google/trends/trending$'
  '^GET:/google/videos$'
  '^GET:/googlepatents/classification$'
  '^GET:/googlepatents/coverage$'
  '^GET:/googlepatents/detail$'
  '^GET:/googlepatents/recent$'
  '^GET:/googlepatents/search$'
  '^GET:/googlepatents/suggest$'
  '^GET:/googleplay/app$'
  '^GET:/googleplay/categories$'
  '^GET:/googleplay/datasafety$'
  '^GET:/googleplay/developer/[^/]+$'
  '^GET:/googleplay/list$'
  '^GET:/googleplay/permissions$'
  '^GET:/googleplay/ratings$'
  '^GET:/googleplay/reviews$'
  '^GET:/googleplay/search$'
  '^GET:/googleplay/similar$'
  '^GET:/googleplay/suggest/[^/]+$'
  '^GET:/grubhub/availability$'
  '^GET:/grubhub/offers$'
  '^GET:/grubhub/restaurant$'
  '^GET:/grubhub/restaurant/menu$'
  '^GET:/grubhub/restaurant/reviews$'
  '^GET:/grubhub/search$'
  '^GET:/grubhub/timepicker$'
  '^GET:/guardian/article$'
  '^GET:/guardian/headlines$'
  '^GET:/guardian/topic$'
  '^GET:/gymshark/collections$'
  '^GET:/gymshark/collections/[^/]+/products$'
  '^GET:/gymshark/pages$'
  '^GET:/gymshark/pages/[^/]+$'
  '^GET:/gymshark/products$'
  '^GET:/gymshark/products/[^/]+$'
  '^GET:/gymshark/products/[^/]+/recommendations$'
  '^GET:/gymshark/sitemap/urls$'
  '^GET:/gymshark/sitemaps$'
  '^GET:/gymshark/store$'
  '^GET:/hm/categories$'
  '^GET:/hm/listing$'
  '^GET:/hm/product/[^/]+$'
  '^GET:/hm/product/[^/]+/related$'
  '^GET:/hm/search$'
  '^GET:/hm/search/suggestions$'
  '^GET:/hm/stores$'
  '^GET:/homedepot/categories$'
  '^GET:/homedepot/category$'
  '^GET:/homedepot/product/[^/]+$'
  '^GET:/homedepot/product/[^/]+/questions$'
  '^GET:/homedepot/search$'
  '^GET:/homedepot/suggest$'
  '^GET:/hotels/autocomplete$'
  '^GET:/ikea/availability$'
  '^GET:/ikea/category$'
  '^GET:/ikea/product$'
  '^GET:/ikea/reviews$'
  '^GET:/ikea/search$'
  '^GET:/ikea/store$'
  '^GET:/ikea/stores$'
  '^GET:/ikea/suggest$'
  '^GET:/imdb/charts$'
  '^GET:/imdb/name$'
  '^GET:/imdb/name/awards$'
  '^GET:/imdb/name/credits$'
  '^GET:/imdb/search$'
  '^GET:/imdb/search/title$'
  '^GET:/imdb/title$'
  '^GET:/imdb/title/awards$'
  '^GET:/imdb/title/company-credits$'
  '^GET:/imdb/title/credits$'
  '^GET:/imdb/title/episodes$'
  '^GET:/imdb/title/filming-locations$'
  '^GET:/imdb/title/goofs$'
  '^GET:/imdb/title/keywords$'
  '^GET:/imdb/title/parental-guide$'
  '^GET:/imdb/title/public-facts-analysis$'
  '^GET:/imdb/title/quotes$'
  '^GET:/imdb/title/ratings$'
  '^GET:/imdb/title/release-info$'
  '^GET:/imdb/title/reviews$'
  '^GET:/imdb/title/similar$'
  '^GET:/imdb/title/technical-specs$'
  '^GET:/imdb/title/trivia$'
  '^GET:/importyeti/company$'
  '^GET:/importyeti/search$'
  '^GET:/indeed/job$'
  '^GET:/indeed/locations/suggest$'
  '^GET:/indeed/search$'
  '^GET:/instacart/departments$'
  '^GET:/instacart/item$'
  '^GET:/instacart/search$'
  '^GET:/instacart/search-nearby$'
  '^GET:/instacart/stores$'
  '^GET:/instacart/trending$'
  '^GET:/instagram/post/[^/]+/[^/]+$'
  '^GET:/instagram/profile/[^/]+$'
  '^GET:/instagram/reels/[^/]+$'
  '^GET:/jcrew/categories$'
  '^GET:/jcrew/category$'
  '^GET:/jcrew/product$'
  '^GET:/jcrew/product/reviews$'
  '^GET:/jcrew/search$'
  '^GET:/jcrew/size-chart$'
  '^GET:/jcrew/stores$'
  '^GET:/jcrew/suggest$'
  '^GET:/jimmy-johns/menu$'
  '^GET:/jimmy-johns/modifiers$'
  '^GET:/jimmy-johns/nearby$'
  '^GET:/jimmy-johns/sitemap$'
  '^GET:/jimmy-johns/store$'
  '^GET:/jobs/ashby/board$'
  '^GET:/jobs/company-search$'
  '^GET:/jobs/eightfold/board$'
  '^GET:/jobs/eightfold/job$'
  '^GET:/jobs/gem/board$'
  '^GET:/jobs/greenhouse/board$'
  '^GET:/jobs/greenhouse/job$'
  '^GET:/jobs/hiring-signals$'
  '^GET:/jobs/icims/board$'
  '^GET:/jobs/icims/job$'
  '^GET:/jobs/lever/posting$'
  '^GET:/jobs/lever/postings$'
  '^GET:/jobs/oracle/board$'
  '^GET:/jobs/oracle/job$'
  '^GET:/jobs/personio/feed$'
  '^GET:/jobs/phenom/board$'
  '^GET:/jobs/phenom/job$'
  '^GET:/jobs/pinpoint/board$'
  '^GET:/jobs/recruitee/offer$'
  '^GET:/jobs/recruitee/offers$'
  '^GET:/jobs/rippling/board$'
  '^GET:/jobs/rippling/job$'
  '^GET:/jobs/smartrecruiters/posting$'
  '^GET:/jobs/smartrecruiters/postings$'
  '^GET:/jobs/teamtailor/jobs$'
  '^GET:/jobs/ukg/board$'
  '^GET:/jobs/workable/posting$'
  '^GET:/jobs/workable/postings$'
  '^GET:/jobs/workday/board$'
  '^GET:/jobs/workday/job$'
  '^GET:/justeat/restaurant$'
  '^GET:/justeat/restaurant/menu$'
  '^GET:/justeat/search$'
  '^GET:/justwatch/age-certifications$'
  '^GET:/justwatch/discover$'
  '^GET:/justwatch/episode/by-id$'
  '^GET:/justwatch/episode/offers$'
  '^GET:/justwatch/genre/titles$'
  '^GET:/justwatch/genres$'
  '^GET:/justwatch/monetization/titles$'
  '^GET:/justwatch/new$'
  '^GET:/justwatch/popular$'
  '^GET:/justwatch/provider/titles$'
  '^GET:/justwatch/providers$'
  '^GET:/justwatch/search$'
  '^GET:/justwatch/season/by-id$'
  '^GET:/justwatch/season/episodes$'
  '^GET:/justwatch/show/seasons$'
  '^GET:/justwatch/title$'
  '^GET:/justwatch/title/analysis$'
  '^GET:/justwatch/title/by-id$'
  '^GET:/justwatch/title/media$'
  '^GET:/justwatch/title/offers$'
  '^GET:/justwatch/title/similar$'
  '^GET:/kalshi/event/[^/]+$'
  '^GET:/kalshi/event/[^/]+/history$'
  '^GET:/kalshi/event/[^/]+/metadata$'
  '^GET:/kalshi/events$'
  '^GET:/kalshi/events/multivariate$'
  '^GET:/kalshi/exchange/schedule$'
  '^GET:/kalshi/exchange/status$'
  '^GET:/kalshi/historical/cutoff$'
  '^GET:/kalshi/historical/market/[^/]+$'
  '^GET:/kalshi/historical/market/[^/]+/history$'
  '^GET:/kalshi/historical/markets$'
  '^GET:/kalshi/historical/trades$'
  '^GET:/kalshi/market/[^/]+$'
  '^GET:/kalshi/market/[^/]+/history$'
  '^GET:/kalshi/market/[^/]+/orderbook$'
  '^GET:/kalshi/markets$'
  '^GET:/kalshi/markets/history$'
  '^GET:/kalshi/markets/orderbooks$'
  '^GET:/kalshi/series$'
  '^GET:/kalshi/series/[^/]+$'
  '^GET:/kalshi/trades$'
  '^GET:/kfc/delivery-estimate$'
  '^GET:/kfc/menu$'
  '^GET:/kfc/nearby$'
  '^GET:/kfc/promotion$'
  '^GET:/kfc/promotions$'
  '^GET:/kfc/store$'
  '^GET:/kfc/stores$'
  '^GET:/kickstarter/comments$'
  '^GET:/kickstarter/discover$'
  '^GET:/kickstarter/project$'
  '^GET:/kickstarter/updates$'
  '^GET:/kohls/category$'
  '^GET:/kohls/product/reviews$'
  '^GET:/kohls/stores$'
  '^GET:/kohls/suggest$'
  '^GET:/kroger/category$'
  '^GET:/kroger/coupons$'
  '^GET:/kroger/product$'
  '^GET:/kroger/product/reviews$'
  '^GET:/kroger/products$'
  '^GET:/kroger/related-tags$'
  '^GET:/kroger/search$'
  '^GET:/kroger/store$'
  '^GET:/kroger/suggest$'
  '^GET:/kyliecosmetics/collections$'
  '^GET:/kyliecosmetics/collections/[^/]+/products$'
  '^GET:/kyliecosmetics/pages$'
  '^GET:/kyliecosmetics/pages/[^/]+$'
  '^GET:/kyliecosmetics/products$'
  '^GET:/kyliecosmetics/products/[^/]+$'
  '^GET:/kyliecosmetics/products/[^/]+/recommendations$'
  '^GET:/kyliecosmetics/search/suggest$'
  '^GET:/kyliecosmetics/sitemap/urls$'
  '^GET:/kyliecosmetics/sitemaps$'
  '^GET:/kyliecosmetics/store$'
  '^GET:/lazada/categories$'
  '^GET:/lazada/category-products$'
  '^GET:/lazada/home$'
  '^GET:/lazada/product$'
  '^GET:/lazada/search$'
  '^GET:/leboncoin/listing$'
  '^GET:/leboncoin/search$'
  '^GET:/letterboxd/film/[^/]+$'
  '^GET:/letterboxd/film/[^/]+/rating-histogram$'
  '^GET:/letterboxd/film/[^/]+/reviews$'
  '^GET:/letterboxd/film/[^/]+/similar$'
  '^GET:/letterboxd/member/[^/]+$'
  '^GET:/letterboxd/person/[^/]+$'
  '^GET:/letterboxd/popular$'
  '^GET:/letterboxd/search$'
  '^GET:/linkedin/company/[^/]+$'
  '^GET:/linkedin/product/[^/]+$'
  '^GET:/linkedin/showcase/[^/]+$'
  '^GET:/lululemon/categories$'
  '^GET:/lululemon/category$'
  '^GET:/lululemon/outfit$'
  '^GET:/lululemon/product/[^/]+$'
  '^GET:/lululemon/stores$'
  '^GET:/macys/product/[^/]+$'
  '^GET:/macys/product/reviews$'
  '^GET:/macys/suggest$'
  '^GET:/manga/rankings$'
  '^GET:/manga/search$'
  '^GET:/manga/title/[^/]+$'
  '^GET:/manga/title/[^/]+/characters$'
  '^GET:/manga/title/[^/]+/recommendations$'
  '^GET:/manga/title/[^/]+/staff$'
  '^GET:/mcdonalds/categories$'
  '^GET:/mcdonalds/item$'
  '^GET:/mcdonalds/item-list$'
  '^GET:/mcdonalds/menu$'
  '^GET:/mcdonalds/restaurant-menu$'
  '^GET:/mcdonalds/restaurants$'
  '^GET:/mercari/autocomplete$'
  '^GET:/mercari/home$'
  '^GET:/mercari/item/[^/]+$'
  '^GET:/mercari/master$'
  '^GET:/mercari/search$'
  '^GET:/meta-jobs/job$'
  '^GET:/meta-jobs/list$'
  '^GET:/meta-jobs/search$'
  '^GET:/metacritic/browse$'
  '^GET:/metacritic/game/[^/]+$'
  '^GET:/metacritic/game/[^/]+/critic-reviews$'
  '^GET:/metacritic/game/[^/]+/user-reviews$'
  '^GET:/metacritic/movie/[^/]+$'
  '^GET:/metacritic/movie/[^/]+/critic-reviews$'
  '^GET:/metacritic/movie/[^/]+/user-reviews$'
  '^GET:/metacritic/tv/[^/]+$'
  '^GET:/metacritic/tv/[^/]+/critic-reviews$'
  '^GET:/metacritic/tv/[^/]+/user-reviews$'
  '^GET:/metaculus/category/[^/]+/questions$'
  '^GET:/metaculus/comments-feed$'
  '^GET:/metaculus/project/[^/]+/questions$'
  '^GET:/metaculus/question/[^/]+$'
  '^GET:/metaculus/question/[^/]+/forecast-history$'
  '^GET:/metaculus/question/[^/]+/forecasts$'
  '^GET:/metaculus/question/[^/]+/metadata$'
  '^GET:/metaculus/question/[^/]+/options$'
  '^GET:/metaculus/questions$'
  '^GET:/metaculus/top-comments$'
  '^GET:/metaculus/tournament/[^/]+/questions$'
  '^GET:/mlb/game$'
  '^GET:/mlb/game-boxscore$'
  '^GET:/mlb/game-play-by-play$'
  '^GET:/mlb/league-stats$'
  '^GET:/mlb/player$'
  '^GET:/mlb/player-stats$'
  '^GET:/mlb/schedule$'
  '^GET:/mlb/standings$'
  '^GET:/mlb/team-roster$'
  '^GET:/mlb/team-stats$'
  '^GET:/mlb/teams$'
  '^GET:/mlb/transactions$'
  '^GET:/nike/categories$'
  '^GET:/nike/product$'
  '^GET:/nike/product/availability$'
  '^GET:/nike/product/details$'
  '^GET:/nike/product/recommendations$'
  '^GET:/nike/product/reviews$'
  '^GET:/nike/search$'
  '^GET:/nike/stores$'
  '^GET:/nike/suggest$'
  '^GET:/numbeo/cost-of-living/city/[^/]+$'
  '^GET:/numbeo/cost-of-living/country$'
  '^GET:/numbeo/cost-of-living/rankings$'
  '^GET:/numbeo/cost-of-living/rankings-by-country$'
  '^GET:/numbeo/indices/city/[^/]+$'
  '^GET:/numbeo/indices/country$'
  '^GET:/numbeo/indices/rankings$'
  '^GET:/numbeo/indices/rankings-by-country$'
  '^GET:/ohpolly/collections$'
  '^GET:/ohpolly/collections/[^/]+/products$'
  '^GET:/ohpolly/pages$'
  '^GET:/ohpolly/pages/[^/]+$'
  '^GET:/ohpolly/products$'
  '^GET:/ohpolly/products/[^/]+$'
  '^GET:/ohpolly/products/[^/]+/recommendations$'
  '^GET:/ohpolly/search/suggest$'
  '^GET:/ohpolly/sitemap/urls$'
  '^GET:/ohpolly/sitemaps$'
  '^GET:/ohpolly/store$'
  '^GET:/oldnavy/categories$'
  '^GET:/oldnavy/category$'
  '^GET:/oldnavy/product$'
  '^GET:/oldnavy/product/availability$'
  '^GET:/oldnavy/product/reviews$'
  '^GET:/oldnavy/search$'
  '^GET:/oldnavy/stores$'
  '^GET:/opensea/activity$'
  '^GET:/opensea/categories$'
  '^GET:/opensea/chains$'
  '^GET:/opensea/collection/[^/]+$'
  '^GET:/opensea/collection/[^/]+/activity$'
  '^GET:/opensea/collection/[^/]+/best-deals$'
  '^GET:/opensea/collection/[^/]+/chart$'
  '^GET:/opensea/collection/[^/]+/depth$'
  '^GET:/opensea/collection/[^/]+/holders$'
  '^GET:/opensea/collection/[^/]+/items$'
  '^GET:/opensea/collection/[^/]+/offers$'
  '^GET:/opensea/collection/[^/]+/rarest-items$'
  '^GET:/opensea/collection/[^/]+/search-items$'
  '^GET:/opensea/collection/[^/]+/social-proof$'
  '^GET:/opensea/collection/[^/]+/top-sales$'
  '^GET:/opensea/collection/[^/]+/trait-offers$'
  '^GET:/opensea/collection/[^/]+/traits$'
  '^GET:/opensea/collections$'
  '^GET:/opensea/drops$'
  '^GET:/opensea/item/[^/]+/[^/]+/[^/]+$'
  '^GET:/opensea/item/[^/]+/[^/]+/[^/]+/activity$'
  '^GET:/opensea/item/[^/]+/[^/]+/[^/]+/chart$'
  '^GET:/opensea/item/[^/]+/[^/]+/[^/]+/depth$'
  '^GET:/opensea/item/[^/]+/[^/]+/[^/]+/listings$'
  '^GET:/opensea/item/[^/]+/[^/]+/[^/]+/offers$'
  '^GET:/opensea/item/[^/]+/[^/]+/[^/]+/owners$'
  '^GET:/opensea/most-watched$'
  '^GET:/opensea/profile/[^/]+$'
  '^GET:/opensea/profile/[^/]+/activity$'
  '^GET:/opensea/profile/[^/]+/collections$'
  '^GET:/opensea/profile/[^/]+/created$'
  '^GET:/opensea/profile/[^/]+/items$'
  '^GET:/opensea/profile/[^/]+/search-items$'
  '^GET:/opensea/rankings$'
  '^GET:/opensea/search/collections$'
  '^GET:/opensea/top-movers$'
  '^GET:/opentable/restaurant$'
  '^GET:/opentable/restaurant/menus$'
  '^GET:/opentable/restaurant/reviews$'
  '^GET:/opentable/search$'
  '^GET:/otto/categories$'
  '^GET:/otto/product$'
  '^GET:/otto/search$'
  '^GET:/pandamart/search$'
  '^GET:/pandamart/store$'
  '^GET:/pandamart/store/categories$'
  '^GET:/pandamart/store/product$'
  '^GET:/pandamart/store/products$'
  '^GET:/pandamart/store/search$'
  '^GET:/panera/at-work-locations$'
  '^GET:/panera/cafe$'
  '^GET:/panera/catering-delivery-info$'
  '^GET:/panera/catering-menu$'
  '^GET:/panera/geocode$'
  '^GET:/panera/item-detail$'
  '^GET:/panera/item-options$'
  '^GET:/panera/locations$'
  '^GET:/panera/menu$'
  '^GET:/panera/quantity-rules$'
  '^GET:/panera/retired-products$'
  '^GET:/panera/time-slots$'
  '^GET:/panera/upsell-suggestions$'
  '^GET:/papajohns/allergens$'
  '^GET:/papajohns/colombia/menu$'
  '^GET:/papajohns/deals$'
  '^GET:/papajohns/directory$'
  '^GET:/papajohns/elsalvador/menu$'
  '^GET:/papajohns/india/deal$'
  '^GET:/papajohns/india/menu$'
  '^GET:/papajohns/india/menu/item$'
  '^GET:/papajohns/india/stores$'
  '^GET:/papajohns/intl/deals$'
  '^GET:/papajohns/intl/ingredients$'
  '^GET:/papajohns/intl/menu$'
  '^GET:/papajohns/intl/offer$'
  '^GET:/papajohns/intl/product$'
  '^GET:/papajohns/intl/stores$'
  '^GET:/papajohns/menu$'
  '^GET:/papajohns/menu/item$'
  '^GET:/papajohns/nearby$'
  '^GET:/papajohns/nutrition$'
  '^GET:/papajohns/peru/menu$'
  '^GET:/papajohns/poland/menu$'
  '^GET:/papajohns/russia/menu$'
  '^GET:/papajohns/store$'
  '^GET:/patreon/creator$'
  '^GET:/patreon/creator/tiers$'
  '^GET:/patreon/explore$'
  '^GET:/patreon/rss$'
  '^GET:/pinterest/board/[^/]+/[^/]+$'
  '^GET:/pinterest/categories$'
  '^GET:/pinterest/ideas/[^/]+$'
  '^GET:/pinterest/pin/[^/]+$'
  '^GET:/pinterest/search$'
  '^GET:/pinterest/user/[^/]+$'
  '^GET:/pinterest/user/[^/]+/boards$'
  '^GET:/pinterest/user/[^/]+/pins$'
  '^GET:/pitchbook/advisor$'
  '^GET:/pitchbook/company$'
  '^GET:/pitchbook/fund$'
  '^GET:/pitchbook/investor$'
  '^GET:/pitchbook/limited-partner$'
  '^GET:/pizzahut/bundle-choices$'
  '^GET:/pizzahut/delivery-estimate$'
  '^GET:/pizzahut/menu$'
  '^GET:/pizzahut/modifiers$'
  '^GET:/pizzahut/store$'
  '^GET:/pizzahut/stores$'
  '^GET:/playstation/browse$'
  '^GET:/playstation/category$'
  '^GET:/playstation/concept$'
  '^GET:/playstation/deals$'
  '^GET:/playstation/latest$'
  '^GET:/playstation/page$'
  '^GET:/playstation/product$'
  '^GET:/playstation/search$'
  '^GET:/polymarket/activity/trades$'
  '^GET:/polymarket/clob/market/[^/]+$'
  '^GET:/polymarket/dashboards/macro$'
  '^GET:/polymarket/event/[^/]+$'
  '^GET:/polymarket/events$'
  '^GET:/polymarket/events/[^/]+/tags$'
  '^GET:/polymarket/events/similar$'
  '^GET:/polymarket/fee-types$'
  '^GET:/polymarket/homepage/feed$'
  '^GET:/polymarket/leaderboard$'
  '^GET:/polymarket/market/[^/]+$'
  '^GET:/polymarket/market/[^/]+/liquidity$'
  '^GET:/polymarket/market/[^/]+/tags$'
  '^GET:/polymarket/markets$'
  '^GET:/polymarket/predictions$'
  '^GET:/polymarket/rewards/market/[^/]+$'
  '^GET:/polymarket/rewards/markets$'
  '^GET:/polymarket/search$'
  '^GET:/polymarket/tag/[^/]+$'
  '^GET:/polymarket/tag/[^/]+/related-tags$'
  '^GET:/polymarket/tags$'
  '^GET:/polymarket/token/[^/]+/midpoint$'
  '^GET:/polymarket/token/[^/]+/orderbook$'
  '^GET:/polymarket/token/[^/]+/price$'
  '^GET:/polymarket/token/[^/]+/price-history$'
  '^GET:/polymarket/token/[^/]+/spread$'
  '^GET:/popeyes/faq$'
  '^GET:/popeyes/location$'
  '^GET:/popeyes/locations$'
  '^GET:/popeyes/menu$'
  '^GET:/popeyes/offers$'
  '^GET:/popeyes/promotions$'
  '^GET:/popeyes/quests$'
  '^GET:/popeyes/rewards$'
  '^GET:/poshmark/brand/[^/]+$'
  '^GET:/poshmark/brands$'
  '^GET:/poshmark/categories$'
  '^GET:/poshmark/category/[^/]+$'
  '^GET:/poshmark/closet/[^/]+$'
  '^GET:/poshmark/listing/[^/]+$'
  '^GET:/poshmark/search$'
  '^GET:/poshmark/trend/[^/]+$'
  '^GET:/producthunt/category/[^/]+$'
  '^GET:/producthunt/category/[^/]+/products$'
  '^GET:/producthunt/leaderboard$'
  '^GET:/producthunt/product/[^/]+$'
  '^GET:/producthunt/product/[^/]+/about$'
  '^GET:/producthunt/product/[^/]+/alternatives$'
  '^GET:/producthunt/product/[^/]+/customers$'
  '^GET:/producthunt/product/[^/]+/launches$'
  '^GET:/producthunt/product/[^/]+/makers$'
  '^GET:/producthunt/product/[^/]+/reviews$'
  '^GET:/producthunt/search$'
  '^GET:/quince/categories$'
  '^GET:/quince/navigation$'
  '^GET:/quince/product$'
  '^GET:/quince/product/faq$'
  '^GET:/quince/product/reviews$'
  '^GET:/quince/search$'
  '^GET:/quince/sitemap/urls$'
  '^GET:/quince/sitemaps$'
  '^GET:/quince/suggest$'
  '^GET:/raisingcanes/directory$'
  '^GET:/raisingcanes/menu$'
  '^GET:/raisingcanes/nearby$'
  '^GET:/raisingcanes/promotion$'
  '^GET:/raisingcanes/promotions$'
  '^GET:/raisingcanes/store$'
  '^GET:/reddit/comments/[^/]+$'
  '^GET:/reddit/domain/[^/]+/posts$'
  '^GET:/reddit/leads$'
  '^GET:/reddit/post/[^/]+$'
  '^GET:/reddit/search$'
  '^GET:/reddit/subreddit/[^/]+/about$'
  '^GET:/reddit/subreddit/[^/]+/comments$'
  '^GET:/reddit/subreddit/[^/]+/posts$'
  '^GET:/reddit/subreddits/posts$'
  '^GET:/reddit/trends$'
  '^GET:/reddit/user/[^/]+/comments$'
  '^GET:/reddit/user/[^/]+/posts$'
  '^GET:/redfin/estimate$'
  '^GET:/redfin/property$'
  '^GET:/redfin/region-trends$'
  '^GET:/redfin/search$'
  '^GET:/redfin/similar$'
  '^GET:/rightmove/agents$'
  '^GET:/rightmove/agents/[^/]+$'
  '^GET:/rightmove/autocomplete$'
  '^GET:/rightmove/commercial/search$'
  '^GET:/rightmove/new-homes/search$'
  '^GET:/rightmove/properties/[^/]+$'
  '^GET:/rightmove/search$'
  '^GET:/rightmove/student/search$'
  '^GET:/roblox/badges$'
  '^GET:/roblox/game$'
  '^GET:/roblox/rankings$'
  '^GET:/roblox/search$'
  '^GET:/rothys/collections$'
  '^GET:/rothys/collections/[^/]+/products$'
  '^GET:/rothys/pages$'
  '^GET:/rothys/pages/[^/]+$'
  '^GET:/rothys/products$'
  '^GET:/rothys/products/[^/]+$'
  '^GET:/rothys/products/[^/]+/recommendations$'
  '^GET:/rothys/search/suggest$'
  '^GET:/rothys/sitemap/urls$'
  '^GET:/rothys/sitemaps$'
  '^GET:/rothys/store$'
  '^GET:/rottentomatoes/browse/movies$'
  '^GET:/rottentomatoes/browse/tv$'
  '^GET:/rottentomatoes/episode$'
  '^GET:/rottentomatoes/movie$'
  '^GET:/rottentomatoes/movie/reviews$'
  '^GET:/rottentomatoes/person$'
  '^GET:/rottentomatoes/search$'
  '^GET:/rottentomatoes/season$'
  '^GET:/rottentomatoes/series$'
  '^GET:/rover/search$'
  '^GET:/rover/sitter/[^/]+$'
  '^GET:/rover/trainer-search$'
  '^GET:/rover/trainer/[^/]+$'
  '^GET:/samsclub/category$'
  '^GET:/samsclub/content/[^/]+$'
  '^GET:/samsclub/departments$'
  '^GET:/samsclub/product/[^/]+$'
  '^GET:/samsclub/product/[^/]+/related$'
  '^GET:/sec/company/intelligence$'
  '^GET:/sec/company/search$'
  '^GET:/sec/company/submissions$'
  '^GET:/sec/filing$'
  '^GET:/sec/filing/sections$'
  '^GET:/sec/financials$'
  '^GET:/sec/frames$'
  '^GET:/sec/full-text-search$'
  '^GET:/sec/insider$'
  '^GET:/sec/institutional-holdings$'
  '^GET:/sephora/category$'
  '^GET:/sephora/product$'
  '^GET:/sephora/product/questions$'
  '^GET:/sephora/product/reviews$'
  '^GET:/sephora/search$'
  '^GET:/sephora/stores$'
  '^GET:/sephora/suggest$'
  '^GET:/shakeshack/locations$'
  '^GET:/shakeshack/menu$'
  '^GET:/shakeshack/nearby$'
  '^GET:/shakeshack/store$'
  '^GET:/shein/category/filters$'
  '^GET:/shein/category/goods$'
  '^GET:/shein/category/nav$'
  '^GET:/shein/products/detail$'
  '^GET:/shop-app/analysis$'
  '^GET:/shop-app/categories$'
  '^GET:/shop-app/products/[^/]+$'
  '^GET:/shop-app/products/[^/]+/related$'
  '^GET:/shop-app/products/[^/]+/reviews$'
  '^GET:/shop-app/products/[^/]+/shop$'
  '^GET:/shop-app/products/[^/]+/variant$'
  '^GET:/shop-app/products/[^/]+/variants$'
  '^GET:/shop-app/search$'
  '^GET:/shop-app/shops/[^/]+$'
  '^GET:/shop-app/shops/[^/]+/collections/[^/]+/products$'
  '^GET:/shop-app/shops/[^/]+/locations$'
  '^GET:/shop-app/shops/[^/]+/products$'
  '^GET:/shop-app/shops/[^/]+/reviews$'
  '^GET:/shop-app/shops/[^/]+/typeahead$'
  '^GET:/shop-app/suggestions$'
  '^GET:/shopify/collections$'
  '^GET:/shopify/collections/[^/]+/products$'
  '^GET:/shopify/pages$'
  '^GET:/shopify/pages/[^/]+$'
  '^GET:/shopify/products$'
  '^GET:/shopify/products/[^/]+$'
  '^GET:/shopify/products/[^/]+/recommendations$'
  '^GET:/shopify/search/suggest$'
  '^GET:/shopify/sitemap/urls$'
  '^GET:/shopify/sitemaps$'
  '^GET:/shopify/store$'
  '^GET:/similarweb/search$'
  '^GET:/similarweb/web/[^/]+$'
  '^GET:/skims/collections$'
  '^GET:/skims/collections/[^/]+/products$'
  '^GET:/skims/pages$'
  '^GET:/skims/pages/[^/]+$'
  '^GET:/skims/products$'
  '^GET:/skims/products/[^/]+$'
  '^GET:/skims/products/[^/]+/recommendations$'
  '^GET:/skims/search/suggest$'
  '^GET:/skims/sitemap/urls$'
  '^GET:/skims/sitemaps$'
  '^GET:/skims/store$'
  '^GET:/sofascore/event$'
  '^GET:/sofascore/event-h2h$'
  '^GET:/sofascore/event-incidents$'
  '^GET:/sofascore/event-lineups$'
  '^GET:/sofascore/event-odds$'
  '^GET:/sofascore/event-statistics$'
  '^GET:/sofascore/live-events$'
  '^GET:/sofascore/player$'
  '^GET:/sofascore/round-events$'
  '^GET:/sofascore/search$'
  '^GET:/sofascore/standings$'
  '^GET:/sofascore/team$'
  '^GET:/sofascore/team-events$'
  '^GET:/sofascore/team-players$'
  '^GET:/sofascore/tournament-seasons$'
  '^GET:/sonic/availability$'
  '^GET:/sonic/categories$'
  '^GET:/sonic/deals$'
  '^GET:/sonic/directory$'
  '^GET:/sonic/item$'
  '^GET:/sonic/location-suggest$'
  '^GET:/sonic/locations$'
  '^GET:/sonic/menu$'
  '^GET:/sonic/nearby$'
  '^GET:/sonic/nutrition-documents$'
  '^GET:/sonic/sitemap$'
  '^GET:/sonic/store$'
  '^GET:/soundcloud/playlist$'
  '^GET:/soundcloud/profile$'
  '^GET:/soundcloud/search$'
  '^GET:/soundcloud/track$'
  '^GET:/soundcloud/user-tracks$'
  '^GET:/sparkfun/categories$'
  '^GET:/sparkfun/category$'
  '^GET:/sparkfun/product$'
  '^GET:/sparkfun/search$'
  '^GET:/spotify-podcasts/categories$'
  '^GET:/spotify-podcasts/charts$'
  '^GET:/spotify-podcasts/episode$'
  '^GET:/spotify-podcasts/home$'
  '^GET:/spotify-podcasts/search$'
  '^GET:/spotify-podcasts/show$'
  '^GET:/spotify-podcasts/show/episodes$'
  '^GET:/spotify-podcasts/show/recommendations$'
  '^GET:/spotify/album$'
  '^GET:/spotify/album/tracks$'
  '^GET:/spotify/albums/search$'
  '^GET:/spotify/artist$'
  '^GET:/spotify/artist/albums$'
  '^GET:/spotify/artist/playlists$'
  '^GET:/spotify/artist/related$'
  '^GET:/spotify/artists/search$'
  '^GET:/spotify/audiobook$'
  '^GET:/spotify/audiobook/chapters$'
  '^GET:/spotify/audiobooks/search$'
  '^GET:/spotify/chapter$'
  '^GET:/spotify/episodes/search$'
  '^GET:/spotify/featured-charts-by-country$'
  '^GET:/spotify/genre$'
  '^GET:/spotify/home$'
  '^GET:/spotify/playlist$'
  '^GET:/spotify/playlists/search$'
  '^GET:/spotify/popular-by-country$'
  '^GET:/spotify/profile$'
  '^GET:/spotify/profile/followers$'
  '^GET:/spotify/profile/playlists$'
  '^GET:/spotify/profiles/search$'
  '^GET:/spotify/search$'
  '^GET:/spotify/section$'
  '^GET:/spotify/shows/search$'
  '^GET:/spotify/track$'
  '^GET:/spotify/track/recommended$'
  '^GET:/spotify/track/similar-albums$'
  '^GET:/spotify/tracks/search$'
  '^GET:/starbucks/menu$'
  '^GET:/starbucks/nearest-store$'
  '^GET:/starbucks/product/[^/]+/[^/]+$'
  '^GET:/starbucks/stores$'
  '^GET:/steam/achievements$'
  '^GET:/steam/app$'
  '^GET:/steam/category/[^/]+$'
  '^GET:/steam/charts/concurrent$'
  '^GET:/steam/charts/most-played$'
  '^GET:/steam/charts/top-releases$'
  '^GET:/steam/community-recommendations$'
  '^GET:/steam/featured$'
  '^GET:/steam/featured-categories$'
  '^GET:/steam/items$'
  '^GET:/steam/news$'
  '^GET:/steam/package$'
  '^GET:/steam/players$'
  '^GET:/steam/reviews$'
  '^GET:/steam/reviews/histogram$'
  '^GET:/steam/search$'
  '^GET:/steam/search/results$'
  '^GET:/steam/steamspy$'
  '^GET:/steam/tags$'
  '^GET:/steam/tags/list$'
  '^GET:/steam/top-sellers$'
  '^GET:/stevemadden/collections$'
  '^GET:/stevemadden/collections/[^/]+/products$'
  '^GET:/stevemadden/pages$'
  '^GET:/stevemadden/pages/[^/]+$'
  '^GET:/stevemadden/products$'
  '^GET:/stevemadden/products/[^/]+$'
  '^GET:/stevemadden/products/[^/]+/recommendations$'
  '^GET:/stevemadden/search/suggest$'
  '^GET:/stevemadden/sitemap/urls$'
  '^GET:/stevemadden/sitemaps$'
  '^GET:/stevemadden/store$'
  '^GET:/stockx/brands$'
  '^GET:/stockx/categories$'
  '^GET:/stockx/product/[^/]+$'
  '^GET:/stockx/releases$'
  '^GET:/stockx/search$'
  '^GET:/strava/challenges$'
  '^GET:/strava/clubs/[^/]+$'
  '^GET:/strava/routes$'
  '^GET:/strava/routes/detail$'
  '^GET:/subway/available-times$'
  '^GET:/subway/combos$'
  '^GET:/subway/menu$'
  '^GET:/subway/nearby$'
  '^GET:/subway/sitemap$'
  '^GET:/subway/store$'
  '^GET:/swiggy/collections$'
  '^GET:/swiggy/restaurant$'
  '^GET:/swiggy/restaurant/menu$'
  '^GET:/swiggy/search$'
  '^GET:/taco-bell/app-menu$'
  '^GET:/taco-bell/categories$'
  '^GET:/taco-bell/menu$'
  '^GET:/taco-bell/nutrition$'
  '^GET:/taco-bell/product$'
  '^GET:/taco-bell/store$'
  '^GET:/taco-bell/store-menu$'
  '^GET:/taco-bell/stores$'
  '^GET:/target/categories$'
  '^GET:/target/category-products$'
  '^GET:/target/filter-options$'
  '^GET:/target/product$'
  '^GET:/target/questions$'
  '^GET:/target/reviews$'
  '^GET:/target/search$'
  '^GET:/tes/jobs/detail$'
  '^GET:/tes/jobs/employer$'
  '^GET:/tes/jobs/search$'
  '^GET:/tes/resources/detail$'
  '^GET:/tes/resources/search$'
  '^GET:/tes/resources/shop$'
  '^GET:/tes/schools/search$'
  '^GET:/tesla-jobs/job$'
  '^GET:/tesla-jobs/list$'
  '^GET:/thebodyshop/collections$'
  '^GET:/thebodyshop/collections/[^/]+/products$'
  '^GET:/thebodyshop/pages$'
  '^GET:/thebodyshop/pages/[^/]+$'
  '^GET:/thebodyshop/products$'
  '^GET:/thebodyshop/products/[^/]+$'
  '^GET:/thebodyshop/products/[^/]+/recommendations$'
  '^GET:/thebodyshop/search/suggest$'
  '^GET:/thebodyshop/sitemap/urls$'
  '^GET:/thebodyshop/sitemaps$'
  '^GET:/thebodyshop/store$'
  '^GET:/threads/post/[^/]+/[^/]+$'
  '^GET:/threads/post/[^/]+/[^/]+/replies$'
  '^GET:/threads/profile/[^/]+$'
  '^GET:/threads/profile/[^/]+/posts$'
  '^GET:/threads/search$'
  '^GET:/ticketmaster/attraction$'
  '^GET:/ticketmaster/attraction-events$'
  '^GET:/ticketmaster/attraction-related$'
  '^GET:/ticketmaster/attraction-reviews$'
  '^GET:/ticketmaster/discover-categories$'
  '^GET:/ticketmaster/discover-category-events$'
  '^GET:/ticketmaster/discover-cities$'
  '^GET:/ticketmaster/discover-city-events$'
  '^GET:/ticketmaster/event$'
  '^GET:/ticketmaster/search-events$'
  '^GET:/ticketmaster/suggest$'
  '^GET:/ticketmaster/trending-attractions$'
  '^GET:/ticketmaster/venue$'
  '^GET:/ticketmaster/venue-enhanced-details$'
  '^GET:/ticketmaster/venue-events$'
  '^GET:/ticketweb/event$'
  '^GET:/ticketweb/search$'
  '^GET:/ticketweb/venue$'
  '^GET:/tiktok/category$'
  '^GET:/tiktok/comments$'
  '^GET:/tiktok/creative-center/hashtags$'
  '^GET:/tiktok/creative-center/videos$'
  '^GET:/tiktok/explore/[^/]+$'
  '^GET:/tiktok/hashtag/[^/]+$'
  '^GET:/tiktok/hashtags$'
  '^GET:/tiktok/popular-trend/country-industry-meta$'
  '^GET:/tiktok/post/[^/]+$'
  '^GET:/tiktok/posts$'
  '^GET:/tiktok/profile/[^/]+$'
  '^GET:/tiktok/search$'
  '^GET:/tiktok/search/hashtag$'
  '^GET:/tiktok/search/user$'
  '^GET:/tiktok/top-ads/analysis$'
  '^GET:/tiktok/top-ads/detail$'
  '^GET:/tiktok/top-ads/filters$'
  '^GET:/tiktok/top-ads/list$'
  '^GET:/tiktok/top-ads/location-info$'
  '^GET:/tiktok/top-ads/locations$'
  '^GET:/tiktok/top-ads/recommend$'
  '^GET:/tiktok/top-ads/safety$'
  '^GET:/tiktok/top-ads/spotlight$'
  '^GET:/tiktok/top-ads/suggestions$'
  '^GET:/tiktok/trending$'
  '^GET:/tmdb/movie/[^/]+$'
  '^GET:/tmdb/movie/list$'
  '^GET:/tmdb/person/[^/]+$'
  '^GET:/tmdb/person/list$'
  '^GET:/tmdb/search$'
  '^GET:/tmdb/tv/[^/]+$'
  '^GET:/tmdb/tv/list$'
  '^GET:/tokopedia/autocomplete$'
  '^GET:/tokopedia/category$'
  '^GET:/tokopedia/home$'
  '^GET:/tokopedia/home/tabs$'
  '^GET:/tokopedia/product$'
  '^GET:/tokopedia/product/review-filters$'
  '^GET:/tokopedia/search$'
  '^GET:/tokopedia/search/filters$'
  '^GET:/tripadvisor/autocomplete$'
  '^GET:/tripadvisor/enums$'
  '^GET:/tripadvisor/hotels$'
  '^GET:/tripadvisor/place$'
  '^GET:/tripadvisor/reviews$'
  '^GET:/tripadvisor/search$'
  '^GET:/tripcom/hotels/[^/]+$'
  '^GET:/tripcom/hotels/search$'
  '^GET:/trustmrr/acquire$'
  '^GET:/trustmrr/categories$'
  '^GET:/trustmrr/category/[^/]+$'
  '^GET:/trustmrr/leaderboard$'
  '^GET:/trustmrr/marketplace$'
  '^GET:/trustmrr/startup/[^/]+$'
  '^GET:/trustmrr/startups$'
  '^GET:/trustpilot/business-units/search$'
  '^GET:/trustpilot/business/[^/]+$'
  '^GET:/trustpilot/business/[^/]+/related$'
  '^GET:/trustpilot/business/[^/]+/reviews$'
  '^GET:/trustpilot/categories$'
  '^GET:/trustpilot/categories/search$'
  '^GET:/trustpilot/category/[^/]+$'
  '^GET:/twitch/channel$'
  '^GET:/twitch/clips$'
  '^GET:/twitch/schedule$'
  '^GET:/twitch/search$'
  '^GET:/twitch/streams$'
  '^GET:/twitch/team$'
  '^GET:/twitch/top-games$'
  '^GET:/twitch/videos$'
  '^GET:/twitch/vod-comments$'
  '^GET:/ubereats/feed$'
  '^GET:/ubereats/search$'
  '^GET:/ubereats/store/[^/]+$'
  '^GET:/ubereats/store/[^/]+/menu$'
  '^GET:/ubereats/store/[^/]+/reviews$'
  '^GET:/ulta/categories$'
  '^GET:/ulta/category$'
  '^GET:/ulta/product/[^/]+$'
  '^GET:/ulta/product/questions$'
  '^GET:/ulta/product/reviews$'
  '^GET:/ulta/search$'
  '^GET:/ulta/stores$'
  '^GET:/ulta/suggest$'
  '^GET:/upwork/freelancer/[^/]+$'
  '^GET:/upwork/job/[^/]+$'
  '^GET:/upwork/search$'
  '^GET:/usptoppubs/detail$'
  '^GET:/usptoppubs/search$'
  '^GET:/vinted/brand$'
  '^GET:/vinted/brands$'
  '^GET:/vinted/catalog$'
  '^GET:/vinted/categories$'
  '^GET:/vinted/category$'
  '^GET:/vinted/item$'
  '^GET:/vinted/member$'
  '^GET:/walgreens/stores$'
  '^GET:/walmart/product/[^/]+$'
  '^GET:/walmart/product/[^/]+/reviews$'
  '^GET:/walmart/search$'
  '^GET:/wayfair/categories$'
  '^GET:/wayfair/category$'
  '^GET:/wayfair/product/[^/]+$'
  '^GET:/wendys/categories$'
  '^GET:/wendys/directory$'
  '^GET:/wendys/item$'
  '^GET:/wendys/menu$'
  '^GET:/wendys/nearby$'
  '^GET:/wendys/nutrition$'
  '^GET:/wendys/restaurant$'
  '^GET:/wendys/store$'
  '^GET:/wendys/store-menu$'
  '^GET:/wendys/time-slots$'
  '^GET:/whataburger/sitemap$'
  '^GET:/whataburger/store$'
  '^GET:/whatnot/browse$'
  '^GET:/whatnot/categories$'
  '^GET:/whatnot/live/[^/]+$'
  '^GET:/wingstop/delivery-store$'
  '^GET:/wingstop/directory$'
  '^GET:/wingstop/flavors$'
  '^GET:/wingstop/menu$'
  '^GET:/wingstop/nearby$'
  '^GET:/wingstop/store$'
  '^GET:/wish/categories$'
  '^GET:/wish/product/[^/]+$'
  '^GET:/wish/product/[^/]+/related$'
  '^GET:/wish/product/[^/]+/reviews$'
  '^GET:/wish/search$'
  '^GET:/wish/suggest$'
  '^GET:/wolt/cities$'
  '^GET:/wolt/collections$'
  '^GET:/wolt/restaurant$'
  '^GET:/wolt/restaurant/availability$'
  '^GET:/wolt/restaurant/menu$'
  '^GET:/wolt/restaurant/menu/search$'
  '^GET:/wolt/search$'
  '^GET:/wolt/search/filters$'
  '^GET:/x/post/[^/]+$'
  '^GET:/x/profile/[^/]+$'
  '^GET:/x/profile/[^/]+/posts$'
  '^GET:/yahoo-autos/article$'
  '^GET:/yahoo-autos/category$'
  '^GET:/yahoo-autos/home$'
  '^GET:/yahoo-entertainment/article$'
  '^GET:/yahoo-entertainment/category$'
  '^GET:/yahoo-entertainment/home$'
  '^GET:/yahoo-finance/calendars$'
  '^GET:/yahoo-finance/calendars/[^/]+$'
  '^GET:/yahoo-finance/industries$'
  '^GET:/yahoo-finance/industries/[^/]+$'
  '^GET:/yahoo-finance/lookup$'
  '^GET:/yahoo-finance/market/[^/]+/status$'
  '^GET:/yahoo-finance/market/[^/]+/summary$'
  '^GET:/yahoo-finance/screener/[^/]+$'
  '^GET:/yahoo-finance/screeners$'
  '^GET:/yahoo-finance/search$'
  '^GET:/yahoo-finance/sectors$'
  '^GET:/yahoo-finance/sectors/[^/]+$'
  '^GET:/yahoo-finance/ticker/[^/]+/actions$'
  '^GET:/yahoo-finance/ticker/[^/]+/analysts$'
  '^GET:/yahoo-finance/ticker/[^/]+/calendar$'
  '^GET:/yahoo-finance/ticker/[^/]+/capital-gains$'
  '^GET:/yahoo-finance/ticker/[^/]+/dividends$'
  '^GET:/yahoo-finance/ticker/[^/]+/earnings$'
  '^GET:/yahoo-finance/ticker/[^/]+/earnings-dates$'
  '^GET:/yahoo-finance/ticker/[^/]+/financials$'
  '^GET:/yahoo-finance/ticker/[^/]+/funds$'
  '^GET:/yahoo-finance/ticker/[^/]+/history$'
  '^GET:/yahoo-finance/ticker/[^/]+/history-metadata$'
  '^GET:/yahoo-finance/ticker/[^/]+/holders$'
  '^GET:/yahoo-finance/ticker/[^/]+/info$'
  '^GET:/yahoo-finance/ticker/[^/]+/isin$'
  '^GET:/yahoo-finance/ticker/[^/]+/news$'
  '^GET:/yahoo-finance/ticker/[^/]+/options$'
  '^GET:/yahoo-finance/ticker/[^/]+/options/[^/]+$'
  '^GET:/yahoo-finance/ticker/[^/]+/quote$'
  '^GET:/yahoo-finance/ticker/[^/]+/sec-filings$'
  '^GET:/yahoo-finance/ticker/[^/]+/shares$'
  '^GET:/yahoo-finance/ticker/[^/]+/shares-full$'
  '^GET:/yahoo-finance/ticker/[^/]+/splits$'
  '^GET:/yahoo-finance/ticker/[^/]+/sustainability$'
  '^GET:/yahoo-finance/ticker/[^/]+/valuation$'
  '^GET:/yahoo-finance/trending/[^/]+$'
  '^GET:/yahoo-health/article$'
  '^GET:/yahoo-health/category$'
  '^GET:/yahoo-health/home$'
  '^GET:/yahoo-life/article$'
  '^GET:/yahoo-life/home$'
  '^GET:/yahoo-news/article$'
  '^GET:/yahoo-news/category$'
  '^GET:/yahoo-news/comments$'
  '^GET:/yahoo-news/comments/replies$'
  '^GET:/yahoo-news/home$'
  '^GET:/yahoo-news/suggest$'
  '^GET:/yahoo-search/images$'
  '^GET:/yahoo-search/local$'
  '^GET:/yahoo-search/news$'
  '^GET:/yahoo-search/search$'
  '^GET:/yahoo-search/suggest$'
  '^GET:/yahoo-search/videos$'
  '^GET:/yahoo-shopping/article$'
  '^GET:/yahoo-shopping/category$'
  '^GET:/yahoo-shopping/home$'
  '^GET:/yahoo-shopping/shopping-list$'
  '^GET:/yahoo-shopping/shopping-lists$'
  '^GET:/yahoo-shopping/store$'
  '^GET:/yahoo-shopping/stores$'
  '^GET:/yahoo-sports/game$'
  '^GET:/yahoo-sports/golf-leaderboard$'
  '^GET:/yahoo-sports/golf-schedule$'
  '^GET:/yahoo-sports/mma-fight-card$'
  '^GET:/yahoo-sports/mma-schedule$'
  '^GET:/yahoo-sports/motorsports-race$'
  '^GET:/yahoo-sports/motorsports-schedule$'
  '^GET:/yahoo-sports/news$'
  '^GET:/yahoo-sports/olympics-medals$'
  '^GET:/yahoo-sports/player$'
  '^GET:/yahoo-sports/scoreboard$'
  '^GET:/yahoo-sports/standings$'
  '^GET:/yahoo-sports/team$'
  '^GET:/yahoo-sports/team-roster$'
  '^GET:/yahoo-sports/team-schedule$'
  '^GET:/yahoo-sports/tennis-rankings$'
  '^GET:/yahoo-sports/tennis-schedule$'
  '^GET:/yahoo-sports/tennis-scoreboard$'
  '^GET:/yahoo-tech/article$'
  '^GET:/yahoo-tech/category$'
  '^GET:/yahoo-tech/home$'
  '^GET:/yelp/business/[^/]+$'
  '^GET:/yelp/business/[^/]+/menu$'
  '^GET:/yelp/business/[^/]+/photos$'
  '^GET:/yelp/business/[^/]+/reviews$'
  '^GET:/yelp/business/[^/]+/reviews/highlights$'
  '^GET:/yelp/business/[^/]+/reviews/search$'
  '^GET:/yelp/geocode$'
  '^GET:/yelp/search$'
  '^GET:/youtube/captions/[^/]+$'
  '^GET:/youtube/channel/[^/]+/playlists$'
  '^GET:/youtube/channel/[^/]+/search$'
  '^GET:/youtube/channel/[^/]+/shorts$'
  '^GET:/youtube/channel/[^/]+/videos$'
  '^GET:/youtube/comments/[^/]+$'
  '^GET:/youtube/playlist/[^/]+$'
  '^GET:/youtube/profile/[^/]+$'
  '^GET:/youtube/search$'
  '^GET:/youtube/tag/[^/]+$'
  '^GET:/youtube/transcript/[^/]+$'
  '^GET:/youtube/transcript/[^/]+/languages$'
  '^GET:/youtube/video/[^/]+$'
  '^GET:/zalando/category$'
  '^GET:/zalando/markets$'
  '^GET:/zalando/product$'
  '^GET:/zalando/search$'
  '^GET:/zalando/suggest$'
  '^GET:/zappos/brand$'
  '^GET:/zappos/brands$'
  '^GET:/zappos/product/[^/]+$'
  '^GET:/zappos/search$'
  '^GET:/zappos/suggest$'
  '^GET:/zara/categories$'
  '^GET:/zara/category/[^/]+/products$'
  '^GET:/zara/product/[^/]+$'
  '^GET:/zara/search$'
  '^GET:/zara/stores$'
  '^GET:/zara/suggest$'
  '^GET:/zaxbys/menu$'
  '^GET:/zaxbys/nearby$'
  '^GET:/zaxbys/store$'
  '^GET:/zillow/autocomplete$'
  '^GET:/zillow/property/[^/]+$'
  '^GET:/zillow/search$'
  '^GET:/zomato/collection$'
  '^GET:/zomato/collections$'
  '^GET:/zomato/restaurant$'
  '^GET:/zomato/restaurant/menu$'
  '^GET:/zomato/search$'
  '^POST:/agoda/flights/itinerary-amenities$'
  '^POST:/ebay/search$'
  '^POST:/expedia/activities/search$'
  '^POST:/expedia/flights/search$'
  '^POST:/expedia/locations/search$'
  '^POST:/expedia/properties/detail$'
  '^POST:/expedia/properties/filters$'
  '^POST:/expedia/properties/reviews$'
  '^POST:/expedia/properties/search$'
  '^POST:/google/jobs$'
  '^POST:/google/map/search$'
  '^POST:/google/search$'
  '^POST:/google/trends/explore$'
  '^POST:/google/trends/explore/interest-by-region$'
  '^POST:/google/trends/explore/interest-over-time$'
  '^POST:/google/trends/explore/related-topics$'
  '^POST:/google/trends/explore/rising-queries$'
  '^POST:/google/trends/explore/top-queries$'
  '^POST:/google/trends/trending/detail$'
  '^POST:/hotels/offers$'
  '^POST:/hotels/property$'
  '^POST:/hotels/rates$'
  '^POST:/hotels/reviews$'
  '^POST:/hotels/reviews/archive$'
  '^POST:/hotels/search$'
  '^POST:/polymarket/tokens/midpoints$'
  '^POST:/polymarket/tokens/orderbooks$'
  '^POST:/polymarket/tokens/prices$'
  '^POST:/polymarket/tokens/spreads$'
  '^POST:/shein/products/aggregation-filters$'
  '^POST:/shein/products/search$'
  '^POST:/shein/search/autocomplete$'
  '^POST:/shein/search/keywords$'
  '^POST:/starbucks/product/[^/]+/[^/]+/nutrition$'
  '^POST:/yahoo-finance/download$'
  '^POST:/yahoo-finance/screener$'
)
for route_method_regex in ${route_method_regexes[@]+"${route_method_regexes[@]}"}; do
  if [[ "$method:$path" =~ $route_method_regex ]]; then
    route_method_allowed=true
    break
  fi
done
if [ "$route_method_allowed" = false ]; then
  echo "method is not allowed for this crawlora route" >&2
  exit 2
fi



# Keep the API key out of the curl process command line. A private temporary
# config supplies the header and is removed automatically on exit.
umask 077
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
  # -q must be the first curl option: ignore any user ~/.curlrc so inherited
  # config cannot redirect the request, add uploads, or alter credential use.
  curl -q -fsS -G "${auth[@]}" ${qs[@]+"${qs[@]}"} "${base}${path}"
else
  [ -n "$body" ] || body="${rest[0]:-}"
  [ -n "$body" ] || body='{}'
  # Stream the body on stdin so curl never interprets a user value as its
  # @file shorthand (and cannot read local files supplied in a request body).
  printf '%s' "$body" | curl -q -fsS -X "$method" "${auth[@]}" \
    -H "Content-Type: application/json" --data-binary @- "${base}${path}"
fi
