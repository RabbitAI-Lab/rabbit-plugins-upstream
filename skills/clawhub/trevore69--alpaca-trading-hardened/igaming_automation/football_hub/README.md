# Football hub prototype (igamingreviews.org)

Open `index.html` in a browser. All data is baked into `data.js`, no server needed.
Regenerate data: `python3 fetch_league.py epl` (rewrites `data.js`).
API responses are cached in `.api_cache/` so re-runs only fetch missing bits. Delete that folder to force a full refresh.
Add a league: add an entry to `LEAGUES` at the top of `fetch_league.py` (league_id, name, full_name, team_names), then run `python3 fetch_league.py <key>`.
Demo key limits: list and search endpoints truncate hard (squads about 10 players, league events 1 or 2 at a time), so teams are discovered by name. Full squad data unlocks with the premium API key.
The demo key is also rate limited. The script retries with backoff; if data looks thin, just run it again and the cache fills the gaps.
Data source: TheSportsDB free API. Crest and badge images load from their CDN.
