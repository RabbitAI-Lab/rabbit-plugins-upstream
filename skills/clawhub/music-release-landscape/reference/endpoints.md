# music-release-landscape — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**9 endpoints across 1 platform group(s).**

## Spotify (9)

### `spotify_album`

- **HTTP:** `GET /spotify/album`
- **What:** Retrieve Spotify album details. Returns normalized Spotify Web Player album metadata and tracks from private Pathfinder responses.
- **Params:** `id` (string, optional) — Spotify album ID; `limit` (integer, optional) — Track limit, clamped to 1-50; `offset` (integer, optional) — Track offset; `uri` (string, optional) — Spotify album URI or open.spotify.com album URL

### `spotify_album_tracks`

- **HTTP:** `GET /spotify/album/tracks`
- **What:** Retrieve Spotify album tracks. Returns normalized Spotify Web Player album tracks from private Pathfinder responses.
- **Params:** `id` (string, optional) — Spotify album ID; `limit` (integer, optional) — Track limit, clamped to 1-50; `offset` (integer, optional) — Track offset; `uri` (string, optional) — Spotify album URI or open.spotify.com album URL

### `spotify_albums_search`

- **HTTP:** `GET /spotify/albums/search`
- **What:** Search Spotify albums. Returns normalized Spotify Web Player album search results for a search term. The endpoint fetches anonymous Spotify credentials at request time; caller-supplied Spotify bearer or client tokens are not required.
- **Params:** `include_album_pre_releases` (boolean, optional) — Include album pre-release results; `include_audiobooks` (boolean, optional) — Include audiobook context where available; `include_authors` (boolean, optional) — Include authors; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `include_pre_releases` (boolean, optional) — Include pre-release results; `limit` (integer, optional) — Album result limit, clamped to 1-50; `number_of_top_results` (integer, optional) — Top result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Search term

### `spotify_artist`

- **HTTP:** `GET /spotify/artist`
- **What:** Retrieve Spotify artist details. Returns normalized Spotify Web Player artist overview data from private Pathfinder responses.
- **Params:** `id` (string, optional) — Spotify artist ID; `uri` (string, optional) — Spotify artist URI or open.spotify.com artist URL

### `spotify_artist_albums`

- **HTTP:** `GET /spotify/artist/albums`
- **What:** Retrieve Spotify artist albums. Returns artist discography items from Spotify Web Player private Pathfinder responses.
- **Params:** `id` (string, optional) — Spotify artist ID; `limit` (integer, optional) — Limit, clamped to 1-50; `offset` (integer, optional) — Offset; `order` (string, optional) — date_desc, date_asc, name_asc, or name_desc; `type` (string, optional) — album, single, compilation, appears_on, or all; `uri` (string, optional) — Spotify artist URI or open.spotify.com artist URL

### `spotify_artist_related`

- **HTTP:** `GET /spotify/artist/related`
- **What:** Retrieve Spotify related artists. Returns related artists from Spotify Web Player private Pathfinder responses.
- **Params:** `id` (string, optional) — Spotify artist ID; `uri` (string, optional) — Spotify artist URI or open.spotify.com artist URL

### `spotify_artists_search`

- **HTTP:** `GET /spotify/artists/search`
- **What:** Search Spotify artists. Returns normalized Spotify Web Player artist search results for a search term.
- **Params:** `limit` (integer, optional) — Result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Search term

### `spotify_track`

- **HTTP:** `GET /spotify/track`
- **What:** Retrieve Spotify track details. Returns normalized Spotify Web Player track metadata from Spotify's getTrack Pathfinder response. Provide either uri or id; defaults to a known public track when omitted.
- **Params:** `id` (string, optional) — Spotify track ID. Used when uri is omitted; `uri` (string, optional) — Spotify track URI or open.spotify.com track URL

### `spotify_tracks_search`

- **HTTP:** `GET /spotify/tracks/search`
- **What:** Search Spotify tracks. Returns normalized Spotify Web Player track search results for a search term. The endpoint fetches anonymous Spotify credentials at request time; caller-supplied Spotify bearer or client tokens are not required.
- **Params:** `include_album_pre_releases` (boolean, optional) — Include album pre-release results; `include_audiobooks` (boolean, optional) — Include audiobook context where available; `include_authors` (boolean, optional) — Include authors; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `include_pre_releases` (boolean, optional) — Include pre-release results; `limit` (integer, optional) — Track result limit, clamped to 1-50; `number_of_top_results` (integer, optional) — Top result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Search term
