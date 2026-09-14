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

# Static routes use escaped case patterns. Parameterized routes use anchored
# extended regular expressions so every {param} is exactly one non-empty path
# segment; unlike a case '*', [^/]+ cannot consume another slash.
route_allowed=false
case "$path" in
  /7now|/7now/*) route_allowed=true ;;
  /accor|/accor/*) route_allowed=true ;;
  /adidas|/adidas/*) route_allowed=true ;;
  /agoda|/agoda/*) route_allowed=true ;;
  /airbnb|/airbnb/*) route_allowed=true ;;
  /allbirds|/allbirds/*) route_allowed=true ;;
  /amazon|/amazon/*) route_allowed=true ;;
  /amazon-jobs|/amazon-jobs/*) route_allowed=true ;;
  /anime|/anime/*) route_allowed=true ;;
  /apple-books|/apple-books/*) route_allowed=true ;;
  /apple-jobs|/apple-jobs/*) route_allowed=true ;;
  /apple-maps|/apple-maps/*) route_allowed=true ;;
  /apple-podcasts|/apple-podcasts/*) route_allowed=true ;;
  /appstore|/appstore/*) route_allowed=true ;;
  /arbys|/arbys/*) route_allowed=true ;;
  /audible|/audible/*) route_allowed=true ;;
  /autotrader|/autotrader/*) route_allowed=true ;;
  /bbb|/bbb/*) route_allowed=true ;;
  /bbc|/bbc/*) route_allowed=true ;;
  /bestbuy|/bestbuy/*) route_allowed=true ;;
  /bigcommerce|/bigcommerce/*) route_allowed=true ;;
  /bilibili|/bilibili/*) route_allowed=true ;;
  /bing|/bing/*) route_allowed=true ;;
  /bluesky|/bluesky/*) route_allowed=true ;;
  /bonhams|/bonhams/*) route_allowed=true ;;
  /booking|/booking/*) route_allowed=true ;;
  /booking-attractions|/booking-attractions/*) route_allowed=true ;;
  /booking-flights|/booking-flights/*) route_allowed=true ;;
  /boots|/boots/*) route_allowed=true ;;
  /boxofficemojo|/boxofficemojo/*) route_allowed=true ;;
  /brand|/brand/*) route_allowed=true ;;
  /brave|/brave/*) route_allowed=true ;;
  /brooklinen|/brooklinen/*) route_allowed=true ;;
  /burgerking|/burgerking/*) route_allowed=true ;;
  /capterra|/capterra/*) route_allowed=true ;;
  /carmax|/carmax/*) route_allowed=true ;;
  /carsdotcom|/carsdotcom/*) route_allowed=true ;;
  /chewy|/chewy/*) route_allowed=true ;;
  /chick-fil-a|/chick-fil-a/*) route_allowed=true ;;
  /chipotle|/chipotle/*) route_allowed=true ;;
  /chromewebstore|/chromewebstore/*) route_allowed=true ;;
  /cnn|/cnn/*) route_allowed=true ;;
  /coingecko|/coingecko/*) route_allowed=true ;;
  /colehaan|/colehaan/*) route_allowed=true ;;
  /congress|/congress/*) route_allowed=true ;;
  /costco|/costco/*) route_allowed=true ;;
  /courtlistener|/courtlistener/*) route_allowed=true ;;
  /cricinfo|/cricinfo/*) route_allowed=true ;;
  /culvers|/culvers/*) route_allowed=true ;;
  /cvs|/cvs/*) route_allowed=true ;;
  /deliveroo|/deliveroo/*) route_allowed=true ;;
  /depop|/depop/*) route_allowed=true ;;
  /discogs|/discogs/*) route_allowed=true ;;
  /dominos|/dominos/*) route_allowed=true ;;
  /doordash|/doordash/*) route_allowed=true ;;
  /draftkings|/draftkings/*) route_allowed=true ;;
  /duckduckgo|/duckduckgo/*) route_allowed=true ;;
  /dunkin|/dunkin/*) route_allowed=true ;;
  /ebay|/ebay/*) route_allowed=true ;;
  /espn|/espn/*) route_allowed=true ;;
  /etsy|/etsy/*) route_allowed=true ;;
  /everlane|/everlane/*) route_allowed=true ;;
  /expedia|/expedia/*) route_allowed=true ;;
  /facebook|/facebook/*) route_allowed=true ;;
  /fashionnova|/fashionnova/*) route_allowed=true ;;
  /fiveguys|/fiveguys/*) route_allowed=true ;;
  /fiverr|/fiverr/*) route_allowed=true ;;
  /foodpanda|/foodpanda/*) route_allowed=true ;;
  /gdelt|/gdelt/*) route_allowed=true ;;
  /geocoding|/geocoding/*) route_allowed=true ;;
  /github|/github/*) route_allowed=true ;;
  /goat|/goat/*) route_allowed=true ;;
  /goodreads|/goodreads/*) route_allowed=true ;;
  /google|/google/*) route_allowed=true ;;
  /google-jobs|/google-jobs/*) route_allowed=true ;;
  /googlepatents|/googlepatents/*) route_allowed=true ;;
  /googleplay|/googleplay/*) route_allowed=true ;;
  /grubhub|/grubhub/*) route_allowed=true ;;
  /guardian|/guardian/*) route_allowed=true ;;
  /gymshark|/gymshark/*) route_allowed=true ;;
  /hm|/hm/*) route_allowed=true ;;
  /homedepot|/homedepot/*) route_allowed=true ;;
  /hotels|/hotels/*) route_allowed=true ;;
  /ikea|/ikea/*) route_allowed=true ;;
  /imdb|/imdb/*) route_allowed=true ;;
  /importyeti|/importyeti/*) route_allowed=true ;;
  /indeed|/indeed/*) route_allowed=true ;;
  /instacart|/instacart/*) route_allowed=true ;;
  /instagram|/instagram/*) route_allowed=true ;;
  /jcrew|/jcrew/*) route_allowed=true ;;
  /jimmy-johns|/jimmy-johns/*) route_allowed=true ;;
  /jobs|/jobs/*) route_allowed=true ;;
  /justeat|/justeat/*) route_allowed=true ;;
  /justwatch|/justwatch/*) route_allowed=true ;;
  /kalshi|/kalshi/*) route_allowed=true ;;
  /kfc|/kfc/*) route_allowed=true ;;
  /kickstarter|/kickstarter/*) route_allowed=true ;;
  /kohls|/kohls/*) route_allowed=true ;;
  /kroger|/kroger/*) route_allowed=true ;;
  /kyliecosmetics|/kyliecosmetics/*) route_allowed=true ;;
  /lazada|/lazada/*) route_allowed=true ;;
  /leboncoin|/leboncoin/*) route_allowed=true ;;
  /letterboxd|/letterboxd/*) route_allowed=true ;;
  /linkedin|/linkedin/*) route_allowed=true ;;
  /lululemon|/lululemon/*) route_allowed=true ;;
  /macys|/macys/*) route_allowed=true ;;
  /manga|/manga/*) route_allowed=true ;;
  /mcdonalds|/mcdonalds/*) route_allowed=true ;;
  /mercari|/mercari/*) route_allowed=true ;;
  /meta-jobs|/meta-jobs/*) route_allowed=true ;;
  /metacritic|/metacritic/*) route_allowed=true ;;
  /metaculus|/metaculus/*) route_allowed=true ;;
  /mlb|/mlb/*) route_allowed=true ;;
  /nike|/nike/*) route_allowed=true ;;
  /numbeo|/numbeo/*) route_allowed=true ;;
  /ohpolly|/ohpolly/*) route_allowed=true ;;
  /oldnavy|/oldnavy/*) route_allowed=true ;;
  /opensea|/opensea/*) route_allowed=true ;;
  /opentable|/opentable/*) route_allowed=true ;;
  /otto|/otto/*) route_allowed=true ;;
  /pandamart|/pandamart/*) route_allowed=true ;;
  /panera|/panera/*) route_allowed=true ;;
  /papajohns|/papajohns/*) route_allowed=true ;;
  /patreon|/patreon/*) route_allowed=true ;;
  /pinterest|/pinterest/*) route_allowed=true ;;
  /pitchbook|/pitchbook/*) route_allowed=true ;;
  /pizzahut|/pizzahut/*) route_allowed=true ;;
  /playstation|/playstation/*) route_allowed=true ;;
  /polymarket|/polymarket/*) route_allowed=true ;;
  /popeyes|/popeyes/*) route_allowed=true ;;
  /poshmark|/poshmark/*) route_allowed=true ;;
  /producthunt|/producthunt/*) route_allowed=true ;;
  /quince|/quince/*) route_allowed=true ;;
  /raisingcanes|/raisingcanes/*) route_allowed=true ;;
  /reddit|/reddit/*) route_allowed=true ;;
  /redfin|/redfin/*) route_allowed=true ;;
  /rightmove|/rightmove/*) route_allowed=true ;;
  /roblox|/roblox/*) route_allowed=true ;;
  /rothys|/rothys/*) route_allowed=true ;;
  /rottentomatoes|/rottentomatoes/*) route_allowed=true ;;
  /rover|/rover/*) route_allowed=true ;;
  /samsclub|/samsclub/*) route_allowed=true ;;
  /sec|/sec/*) route_allowed=true ;;
  /sephora|/sephora/*) route_allowed=true ;;
  /shakeshack|/shakeshack/*) route_allowed=true ;;
  /shein|/shein/*) route_allowed=true ;;
  /shop-app|/shop-app/*) route_allowed=true ;;
  /shopify|/shopify/*) route_allowed=true ;;
  /similarweb|/similarweb/*) route_allowed=true ;;
  /skims|/skims/*) route_allowed=true ;;
  /sofascore|/sofascore/*) route_allowed=true ;;
  /sonic|/sonic/*) route_allowed=true ;;
  /soundcloud|/soundcloud/*) route_allowed=true ;;
  /sparkfun|/sparkfun/*) route_allowed=true ;;
  /spotify|/spotify/*) route_allowed=true ;;
  /spotify-podcasts|/spotify-podcasts/*) route_allowed=true ;;
  /starbucks|/starbucks/*) route_allowed=true ;;
  /steam|/steam/*) route_allowed=true ;;
  /stevemadden|/stevemadden/*) route_allowed=true ;;
  /stockx|/stockx/*) route_allowed=true ;;
  /strava|/strava/*) route_allowed=true ;;
  /subway|/subway/*) route_allowed=true ;;
  /swiggy|/swiggy/*) route_allowed=true ;;
  /taco-bell|/taco-bell/*) route_allowed=true ;;
  /target|/target/*) route_allowed=true ;;
  /tes|/tes/*) route_allowed=true ;;
  /tesla-jobs|/tesla-jobs/*) route_allowed=true ;;
  /thebodyshop|/thebodyshop/*) route_allowed=true ;;
  /threads|/threads/*) route_allowed=true ;;
  /ticketmaster|/ticketmaster/*) route_allowed=true ;;
  /ticketweb|/ticketweb/*) route_allowed=true ;;
  /tiktok|/tiktok/*) route_allowed=true ;;
  /tmdb|/tmdb/*) route_allowed=true ;;
  /tokopedia|/tokopedia/*) route_allowed=true ;;
  /tripadvisor|/tripadvisor/*) route_allowed=true ;;
  /tripcom|/tripcom/*) route_allowed=true ;;
  /trustmrr|/trustmrr/*) route_allowed=true ;;
  /trustpilot|/trustpilot/*) route_allowed=true ;;
  /twitch|/twitch/*) route_allowed=true ;;
  /ubereats|/ubereats/*) route_allowed=true ;;
  /ulta|/ulta/*) route_allowed=true ;;
  /upwork|/upwork/*) route_allowed=true ;;
  /usptoppubs|/usptoppubs/*) route_allowed=true ;;
  /vinted|/vinted/*) route_allowed=true ;;
  /walgreens|/walgreens/*) route_allowed=true ;;
  /walmart|/walmart/*) route_allowed=true ;;
  /wayfair|/wayfair/*) route_allowed=true ;;
  /wendys|/wendys/*) route_allowed=true ;;
  /whataburger|/whataburger/*) route_allowed=true ;;
  /whatnot|/whatnot/*) route_allowed=true ;;
  /wingstop|/wingstop/*) route_allowed=true ;;
  /wish|/wish/*) route_allowed=true ;;
  /wolt|/wolt/*) route_allowed=true ;;
  /x|/x/*) route_allowed=true ;;
  /yahoo-autos|/yahoo-autos/*) route_allowed=true ;;
  /yahoo-entertainment|/yahoo-entertainment/*) route_allowed=true ;;
  /yahoo-finance|/yahoo-finance/*) route_allowed=true ;;
  /yahoo-health|/yahoo-health/*) route_allowed=true ;;
  /yahoo-life|/yahoo-life/*) route_allowed=true ;;
  /yahoo-news|/yahoo-news/*) route_allowed=true ;;
  /yahoo-search|/yahoo-search/*) route_allowed=true ;;
  /yahoo-shopping|/yahoo-shopping/*) route_allowed=true ;;
  /yahoo-sports|/yahoo-sports/*) route_allowed=true ;;
  /yahoo-tech|/yahoo-tech/*) route_allowed=true ;;
  /yelp|/yelp/*) route_allowed=true ;;
  /youtube|/youtube/*) route_allowed=true ;;
  /zalando|/zalando/*) route_allowed=true ;;
  /zappos|/zappos/*) route_allowed=true ;;
  /zara|/zara/*) route_allowed=true ;;
  /zaxbys|/zaxbys/*) route_allowed=true ;;
  /zillow|/zillow/*) route_allowed=true ;;
  /zomato|/zomato/*) route_allowed=true ;;
esac
if [ "$route_allowed" = false ]; then
  route_regexes=(

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
