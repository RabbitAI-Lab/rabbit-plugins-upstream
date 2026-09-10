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
    echo "only GET and POST are supported by the social-media-research skill" >&2
    exit 2
    ;;
esac

# Reject path syntax that could smuggle a route through a shell glob check.
case "$path" in
  ""|*[?#%]*|*..*|*//* )
    echo "invalid path for the social-media-research skill" >&2
    exit 2
    ;;
esac
case "$path" in
  /bilibili/anime-home) ;;
  /bilibili/autocomplete) ;;
  /bilibili/guochuang-home) ;;
  /bilibili/must-watch) ;;
  /bilibili/popular) ;;
  /bilibili/ranking) ;;
  /bilibili/vertical-home) ;;
  /bilibili/weekly) ;;
  /bluesky/author-feed) ;;
  /bluesky/followers) ;;
  /bluesky/follows) ;;
  /bluesky/post-thread) ;;
  /bluesky/profile) ;;
  /bluesky/search-actors) ;;
  /bluesky/trending-topics) ;;
  /facebook/*) ;;
  /facebook/marketplace/search) ;;
  /instagram/post/*/*) ;;
  /instagram/profile/*) ;;
  /instagram/reels/*) ;;
  /linkedin/company/*) ;;
  /linkedin/product/*) ;;
  /linkedin/showcase/*) ;;
  /patreon/creator) ;;
  /patreon/creator/tiers) ;;
  /patreon/explore) ;;
  /patreon/rss) ;;
  /pinterest/board/*/*) ;;
  /pinterest/categories) ;;
  /pinterest/ideas/*) ;;
  /pinterest/pin/*) ;;
  /pinterest/search) ;;
  /pinterest/user/*) ;;
  /pinterest/user/*/boards) ;;
  /pinterest/user/*/pins) ;;
  /reddit/comments/*) ;;
  /reddit/domain/*/posts) ;;
  /reddit/leads) ;;
  /reddit/post/*) ;;
  /reddit/search) ;;
  /reddit/subreddit/*/about) ;;
  /reddit/subreddit/*/comments) ;;
  /reddit/subreddit/*/posts) ;;
  /reddit/subreddits/posts) ;;
  /reddit/trends) ;;
  /reddit/user/*/comments) ;;
  /reddit/user/*/posts) ;;
  /threads/post/*/*) ;;
  /threads/post/*/*/replies) ;;
  /threads/profile/*) ;;
  /threads/profile/*/posts) ;;
  /threads/search) ;;
  /tiktok/category) ;;
  /tiktok/comments) ;;
  /tiktok/creative-center/hashtags) ;;
  /tiktok/creative-center/videos) ;;
  /tiktok/explore/*) ;;
  /tiktok/hashtag/*) ;;
  /tiktok/hashtags) ;;
  /tiktok/popular-trend/country-industry-meta) ;;
  /tiktok/post/*) ;;
  /tiktok/posts) ;;
  /tiktok/profile/*) ;;
  /tiktok/search) ;;
  /tiktok/search/hashtag) ;;
  /tiktok/search/user) ;;
  /tiktok/top-ads/analysis) ;;
  /tiktok/top-ads/detail) ;;
  /tiktok/top-ads/filters) ;;
  /tiktok/top-ads/list) ;;
  /tiktok/top-ads/location-info) ;;
  /tiktok/top-ads/locations) ;;
  /tiktok/top-ads/recommend) ;;
  /tiktok/top-ads/safety) ;;
  /tiktok/top-ads/spotlight) ;;
  /tiktok/top-ads/suggestions) ;;
  /tiktok/trending) ;;
  /x/post/*) ;;
  /x/profile/*) ;;
  /x/profile/*/posts) ;;
  *)
    echo "path is not in the social-media-research skill catalog" >&2
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
