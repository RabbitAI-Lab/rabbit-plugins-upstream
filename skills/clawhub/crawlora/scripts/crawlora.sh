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
case "$path" in
  /7now|/7now/*) ;;
  /accor|/accor/*) ;;
  /adidas|/adidas/*) ;;
  /agoda|/agoda/*) ;;
  /airbnb|/airbnb/*) ;;
  /allbirds|/allbirds/*) ;;
  /amazon|/amazon/*) ;;
  /amazon-jobs|/amazon-jobs/*) ;;
  /anime|/anime/*) ;;
  /apple-books|/apple-books/*) ;;
  /apple-jobs|/apple-jobs/*) ;;
  /apple-maps|/apple-maps/*) ;;
  /apple-podcasts|/apple-podcasts/*) ;;
  /appstore|/appstore/*) ;;
  /arbys|/arbys/*) ;;
  /audible|/audible/*) ;;
  /autotrader|/autotrader/*) ;;
  /bbb|/bbb/*) ;;
  /bbc|/bbc/*) ;;
  /bestbuy|/bestbuy/*) ;;
  /bigcommerce|/bigcommerce/*) ;;
  /bilibili|/bilibili/*) ;;
  /bing|/bing/*) ;;
  /bluesky|/bluesky/*) ;;
  /bonhams|/bonhams/*) ;;
  /booking|/booking/*) ;;
  /booking-attractions|/booking-attractions/*) ;;
  /booking-flights|/booking-flights/*) ;;
  /boots|/boots/*) ;;
  /boxofficemojo|/boxofficemojo/*) ;;
  /brand|/brand/*) ;;
  /brave|/brave/*) ;;
  /brooklinen|/brooklinen/*) ;;
  /burgerking|/burgerking/*) ;;
  /capterra|/capterra/*) ;;
  /carmax|/carmax/*) ;;
  /carsdotcom|/carsdotcom/*) ;;
  /chewy|/chewy/*) ;;
  /chick-fil-a|/chick-fil-a/*) ;;
  /chipotle|/chipotle/*) ;;
  /chromewebstore|/chromewebstore/*) ;;
  /cnn|/cnn/*) ;;
  /coingecko|/coingecko/*) ;;
  /colehaan|/colehaan/*) ;;
  /congress|/congress/*) ;;
  /costco|/costco/*) ;;
  /courtlistener|/courtlistener/*) ;;
  /cricinfo|/cricinfo/*) ;;
  /culvers|/culvers/*) ;;
  /cvs|/cvs/*) ;;
  /deliveroo|/deliveroo/*) ;;
  /depop|/depop/*) ;;
  /discogs|/discogs/*) ;;
  /dominos|/dominos/*) ;;
  /doordash|/doordash/*) ;;
  /draftkings|/draftkings/*) ;;
  /duckduckgo|/duckduckgo/*) ;;
  /dunkin|/dunkin/*) ;;
  /ebay|/ebay/*) ;;
  /espn|/espn/*) ;;
  /etsy|/etsy/*) ;;
  /everlane|/everlane/*) ;;
  /expedia|/expedia/*) ;;
  /facebook|/facebook/*) ;;
  /fashionnova|/fashionnova/*) ;;
  /fiveguys|/fiveguys/*) ;;
  /fiverr|/fiverr/*) ;;
  /foodpanda|/foodpanda/*) ;;
  /gdelt|/gdelt/*) ;;
  /geocoding|/geocoding/*) ;;
  /github|/github/*) ;;
  /goat|/goat/*) ;;
  /goodreads|/goodreads/*) ;;
  /google|/google/*) ;;
  /google-jobs|/google-jobs/*) ;;
  /googlepatents|/googlepatents/*) ;;
  /googleplay|/googleplay/*) ;;
  /grubhub|/grubhub/*) ;;
  /guardian|/guardian/*) ;;
  /gymshark|/gymshark/*) ;;
  /hm|/hm/*) ;;
  /homedepot|/homedepot/*) ;;
  /hotels|/hotels/*) ;;
  /ikea|/ikea/*) ;;
  /imdb|/imdb/*) ;;
  /importyeti|/importyeti/*) ;;
  /indeed|/indeed/*) ;;
  /instacart|/instacart/*) ;;
  /instagram|/instagram/*) ;;
  /jcrew|/jcrew/*) ;;
  /jimmy-johns|/jimmy-johns/*) ;;
  /jobs|/jobs/*) ;;
  /justeat|/justeat/*) ;;
  /justwatch|/justwatch/*) ;;
  /kalshi|/kalshi/*) ;;
  /kfc|/kfc/*) ;;
  /kickstarter|/kickstarter/*) ;;
  /kohls|/kohls/*) ;;
  /kroger|/kroger/*) ;;
  /kyliecosmetics|/kyliecosmetics/*) ;;
  /lazada|/lazada/*) ;;
  /leboncoin|/leboncoin/*) ;;
  /letterboxd|/letterboxd/*) ;;
  /linkedin|/linkedin/*) ;;
  /lululemon|/lululemon/*) ;;
  /macys|/macys/*) ;;
  /manga|/manga/*) ;;
  /mcdonalds|/mcdonalds/*) ;;
  /mercari|/mercari/*) ;;
  /meta-jobs|/meta-jobs/*) ;;
  /metacritic|/metacritic/*) ;;
  /metaculus|/metaculus/*) ;;
  /mlb|/mlb/*) ;;
  /nike|/nike/*) ;;
  /numbeo|/numbeo/*) ;;
  /ohpolly|/ohpolly/*) ;;
  /oldnavy|/oldnavy/*) ;;
  /opensea|/opensea/*) ;;
  /opentable|/opentable/*) ;;
  /otto|/otto/*) ;;
  /pandamart|/pandamart/*) ;;
  /panera|/panera/*) ;;
  /papajohns|/papajohns/*) ;;
  /patreon|/patreon/*) ;;
  /pinterest|/pinterest/*) ;;
  /pitchbook|/pitchbook/*) ;;
  /pizzahut|/pizzahut/*) ;;
  /playstation|/playstation/*) ;;
  /polymarket|/polymarket/*) ;;
  /popeyes|/popeyes/*) ;;
  /poshmark|/poshmark/*) ;;
  /producthunt|/producthunt/*) ;;
  /quince|/quince/*) ;;
  /raisingcanes|/raisingcanes/*) ;;
  /reddit|/reddit/*) ;;
  /redfin|/redfin/*) ;;
  /rightmove|/rightmove/*) ;;
  /roblox|/roblox/*) ;;
  /rothys|/rothys/*) ;;
  /rottentomatoes|/rottentomatoes/*) ;;
  /rover|/rover/*) ;;
  /samsclub|/samsclub/*) ;;
  /sec|/sec/*) ;;
  /sephora|/sephora/*) ;;
  /shakeshack|/shakeshack/*) ;;
  /shein|/shein/*) ;;
  /shop-app|/shop-app/*) ;;
  /shopify|/shopify/*) ;;
  /similarweb|/similarweb/*) ;;
  /skims|/skims/*) ;;
  /sofascore|/sofascore/*) ;;
  /sonic|/sonic/*) ;;
  /soundcloud|/soundcloud/*) ;;
  /sparkfun|/sparkfun/*) ;;
  /spotify|/spotify/*) ;;
  /spotify-podcasts|/spotify-podcasts/*) ;;
  /starbucks|/starbucks/*) ;;
  /steam|/steam/*) ;;
  /stevemadden|/stevemadden/*) ;;
  /stockx|/stockx/*) ;;
  /strava|/strava/*) ;;
  /subway|/subway/*) ;;
  /swiggy|/swiggy/*) ;;
  /taco-bell|/taco-bell/*) ;;
  /target|/target/*) ;;
  /tes|/tes/*) ;;
  /tesla-jobs|/tesla-jobs/*) ;;
  /thebodyshop|/thebodyshop/*) ;;
  /threads|/threads/*) ;;
  /ticketmaster|/ticketmaster/*) ;;
  /ticketweb|/ticketweb/*) ;;
  /tiktok|/tiktok/*) ;;
  /tmdb|/tmdb/*) ;;
  /tokopedia|/tokopedia/*) ;;
  /tripadvisor|/tripadvisor/*) ;;
  /tripcom|/tripcom/*) ;;
  /trustmrr|/trustmrr/*) ;;
  /trustpilot|/trustpilot/*) ;;
  /twitch|/twitch/*) ;;
  /ubereats|/ubereats/*) ;;
  /ulta|/ulta/*) ;;
  /upwork|/upwork/*) ;;
  /usptoppubs|/usptoppubs/*) ;;
  /vinted|/vinted/*) ;;
  /walgreens|/walgreens/*) ;;
  /walmart|/walmart/*) ;;
  /wayfair|/wayfair/*) ;;
  /wendys|/wendys/*) ;;
  /whataburger|/whataburger/*) ;;
  /whatnot|/whatnot/*) ;;
  /wingstop|/wingstop/*) ;;
  /wish|/wish/*) ;;
  /wolt|/wolt/*) ;;
  /x|/x/*) ;;
  /yahoo-autos|/yahoo-autos/*) ;;
  /yahoo-entertainment|/yahoo-entertainment/*) ;;
  /yahoo-finance|/yahoo-finance/*) ;;
  /yahoo-health|/yahoo-health/*) ;;
  /yahoo-life|/yahoo-life/*) ;;
  /yahoo-news|/yahoo-news/*) ;;
  /yahoo-search|/yahoo-search/*) ;;
  /yahoo-shopping|/yahoo-shopping/*) ;;
  /yahoo-sports|/yahoo-sports/*) ;;
  /yahoo-tech|/yahoo-tech/*) ;;
  /yelp|/yelp/*) ;;
  /youtube|/youtube/*) ;;
  /zalando|/zalando/*) ;;
  /zappos|/zappos/*) ;;
  /zara|/zara/*) ;;
  /zaxbys|/zaxbys/*) ;;
  /zillow|/zillow/*) ;;
  /zomato|/zomato/*) ;;
  *)
    echo "path is not in the crawlora skill catalog" >&2
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
