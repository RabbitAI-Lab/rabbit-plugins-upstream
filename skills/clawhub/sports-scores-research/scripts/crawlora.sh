#!/usr/bin/env bash
# Crawlora REST helper — minimal, dependency-free (curl only).
# Calls https://api.crawlora.net/api/v1 with your Crawlora API key.
# Get a free key (2,000 credits/mo, no card) at https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills.
#
# Usage:
#   GET  :  crawlora.sh /path
#
# GET key=value args become the query string. Prints raw JSON to stdout — pipe into `jq`.
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
args=()
while [ $# -gt 0 ]; do
  case "$1" in
    -X|-d) echo "only GET are supported by the sports-scores-research skill" >&2; exit 2 ;;
    *) args+=("$1"); shift ;;
  esac
done

[ "${#args[@]}" -ge 1 ] || { echo "usage: crawlora.sh /<route> [k=v ...]" >&2; exit 2; }
path="${args[0]}"
rest=("${args[@]:1}")

# This skill's helper is limited to its documented Crawlora route set. Keep
# caller-account surfaces and unrelated API routes out of the helper even if
# someone supplies an undocumented path directly.
case "$method" in
  GET) ;;
  *)
    echo "only GET are supported by the sports-scores-research skill" >&2
    exit 2
    ;;
esac

# Reject path syntax that could smuggle a route through a shell glob check.
case "$path" in
  ""|*[?#%]*|*..*|*//* )
    echo "invalid path for the sports-scores-research skill" >&2
    exit 2
    ;;
esac

# Static routes use escaped case patterns. Parameterized routes use anchored
# extended regular expressions so every {param} is exactly one non-empty path
# segment; unlike a case '*', [^/]+ cannot consume another slash.
route_allowed=false
case "$path" in
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
  /espn/athlete) route_allowed=true ;;
  /espn/game-summary) route_allowed=true ;;
  /espn/news) route_allowed=true ;;
  /espn/rankings) route_allowed=true ;;
  /espn/scoreboard) route_allowed=true ;;
  /espn/standings) route_allowed=true ;;
  /espn/team) route_allowed=true ;;
  /espn/team-roster) route_allowed=true ;;
  /espn/teams) route_allowed=true ;;
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
  /strava/challenges) route_allowed=true ;;
  /strava/routes) route_allowed=true ;;
  /strava/routes/detail) route_allowed=true ;;
esac
if [ "$route_allowed" = false ]; then
  route_regexes=(
  '^/strava/clubs/[^/]+$'
  )
  for route_regex in ${route_regexes[@]+"${route_regexes[@]}"}; do
    if [[ "$path" =~ $route_regex ]]; then
      route_allowed=true
      break
    fi
  done
fi
if [ "$route_allowed" = false ]; then
  echo "path is not in the sports-scores-research skill catalog" >&2
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

# GET-only skill: no request body or alternate method is accepted.
# -G + --data-urlencode URL-encodes each value (so spaces etc. are safe).
qs=()
for kv in ${rest[@]+"${rest[@]}"}; do
  [ -n "$kv" ] || continue
  case "$kv" in
    *@*) echo "@ is not allowed in query arguments" >&2; exit 2 ;;
  esac
  qs+=(--data-urlencode "$kv")
done
curl -q -fsS -G "${auth[@]}" ${qs[@]+"${qs[@]}"} "${base}${path}"