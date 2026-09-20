# music-podcast-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**58 endpoints across 5 platform group(s).**

## Spotify (30)

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

### `spotify_artist_playlists`

- **HTTP:** `GET /spotify/artist/playlists`
- **What:** Retrieve Spotify artist playlists. Returns artist playlists from Spotify Web Player private Pathfinder responses.
- **Params:** `id` (string, optional) — Spotify artist ID; `uri` (string, optional) — Spotify artist URI or open.spotify.com artist URL

### `spotify_artist_related`

- **HTTP:** `GET /spotify/artist/related`
- **What:** Retrieve Spotify related artists. Returns related artists from Spotify Web Player private Pathfinder responses.
- **Params:** `id` (string, optional) — Spotify artist ID; `uri` (string, optional) — Spotify artist URI or open.spotify.com artist URL

### `spotify_artists_search`

- **HTTP:** `GET /spotify/artists/search`
- **What:** Search Spotify artists. Returns normalized Spotify Web Player artist search results for a search term.
- **Params:** `limit` (integer, optional) — Result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Search term

### `spotify_audiobook`

- **HTTP:** `GET /spotify/audiobook`
- **What:** Retrieve Spotify audiobook details. Returns Spotify Web Player audiobook metadata from private Pathfinder responses. Spotify exposes audiobooks through show URIs.
- **Params:** `id` (string, optional) — Spotify show ID; `uri` (string, optional) — Spotify audiobook/show URI or open.spotify.com show URL

### `spotify_audiobook_chapters`

- **HTTP:** `GET /spotify/audiobook/chapters`
- **What:** Retrieve Spotify audiobook chapters. Returns audiobook chapters from Spotify Web Player private Pathfinder responses.
- **Params:** `id` (string, optional) — Spotify show ID; `limit` (integer, optional) — Chapter limit, clamped to 1-50; `offset` (integer, optional) — Chapter offset; `uri` (string, optional) — Spotify audiobook/show URI or open.spotify.com show URL

### `spotify_audiobooks_search`

- **HTTP:** `GET /spotify/audiobooks/search`
- **What:** Search Spotify audiobooks. Returns normalized Spotify Web Player audiobook search results for a search term. The endpoint fetches anonymous Spotify credentials at request time; caller-supplied Spotify bearer or client tokens are not required.
- **Params:** `include_album_pre_releases` (boolean, optional) — Include album pre-release results; `include_audiobooks` (boolean, optional) — Include audiobook results; `include_authors` (boolean, optional) — Include authors; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `include_pre_releases` (boolean, optional) — Include pre-release results; `limit` (integer, optional) — Audiobook result limit, clamped to 1-50; `number_of_top_results` (integer, optional) — Top result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Search term

### `spotify_chapter`

- **HTTP:** `GET /spotify/chapter`
- **What:** Retrieve Spotify audiobook chapter details. Returns a Spotify chapter from the same private Pathfinder operation used for episodes and chapters.
- **Params:** `id` (string, optional) — Spotify chapter/episode ID; `uri` (string, optional) — Spotify chapter or episode URI/URL

### `spotify_episodes_search`

- **HTTP:** `GET /spotify/episodes/search`
- **What:** Search Spotify episodes. Returns normalized Spotify Web Player episode search results for a search term.
- **Params:** `limit` (integer, optional) — Result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Search term

### `spotify_featured_charts_by_country`

- **HTTP:** `GET /spotify/featured-charts-by-country`
- **What:** Retrieve Spotify featured charts by country. Returns normalized Spotify country hub content from Spotify's countryHubContent Pathfinder response. Defaults to the CHARTS content shelf for the requested country.
- **Params:** `content_id` (string, optional) — Country hub content ID. Allowed: CHARTS, POPULAR_ALBUMS, POPULAR_ARTISTS, TRENDING_SONGS; `country_code` (string, optional) — Two-letter Spotify popular-in country code

### `spotify_genre`

- **HTTP:** `GET /spotify/genre`
- **What:** Retrieve Spotify genre page. Returns normalized sections and items from Spotify's browsePage Pathfinder response for a Spotify genre or page URI.
- **Params:** `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `page_limit` (integer, optional) — Page pagination limit, clamped to 1-50; `page_offset` (integer, optional) — Page pagination offset; `section_limit` (integer, optional) — Section pagination limit, clamped to 1-50; `section_offset` (integer, optional) — Section pagination offset; `uri` (string, optional) — Spotify genre or page URI

### `spotify_home`

- **HTTP:** `GET /spotify/home`
- **What:** Retrieve Spotify home sections. Returns normalized shelves and items from Spotify's Web Player home Pathfinder response. The endpoint fetches anonymous Spotify credentials at request time; caller-supplied Spotify bearer or client tokens are not required.
- **Params:** `facet` (string, optional) — Optional Spotify home facet; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `section_items_limit` (integer, optional) — Per-section item limit, clamped to 1-50; `sp_t` (string, optional) — Optional Spotify session token. A random UUID is generated when omitted; `time_zone` (string, optional) — IANA time zone used by Spotify home personalization

### `spotify_playlist`

- **HTTP:** `GET /spotify/playlist`
- **What:** Retrieve Spotify playlist details. Returns normalized Spotify Web Player playlist metadata and items from Spotify's fetchPlaylist Pathfinder response. Provide either uri or id; defaults to a known public playlist when omitted.
- **Params:** `enable_watch_feed_entrypoint` (boolean, optional) — Enable watch feed entrypoint; `id` (string, optional) — Spotify playlist ID. Used when uri is omitted; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `limit` (integer, optional) — Playlist item limit, clamped to 1-50; `offset` (integer, optional) — Playlist item offset; `uri` (string, optional) — Spotify playlist URI or open.spotify.com playlist URL

### `spotify_playlists_search`

- **HTTP:** `GET /spotify/playlists/search`
- **What:** Search Spotify playlists. Returns normalized Spotify Web Player playlist search results for a search term. The endpoint fetches anonymous Spotify credentials at request time; caller-supplied Spotify bearer or client tokens are not required.
- **Params:** `include_album_pre_releases` (boolean, optional) — Include album pre-release results; `include_audiobooks` (boolean, optional) — Include audiobook context where available; `include_authors` (boolean, optional) — Include authors; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `include_pre_releases` (boolean, optional) — Include pre-release results; `limit` (integer, optional) — Playlist result limit, clamped to 1-50; `number_of_top_results` (integer, optional) — Top result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Search term

### `spotify_popular_by_country`

- **HTTP:** `GET /spotify/popular-by-country`
- **What:** Retrieve Spotify popular by country. Returns normalized Spotify country hub shelves from Spotify's countryHubsPage Pathfinder response. The country_code parameter accepts Spotify popular-in country codes from open.spotify.com/popular-in/us.
- **Params:** `country_code` (string, optional) — Two-letter Spotify popular-in country code

### `spotify_profile`

- **HTTP:** `GET /spotify/profile`
- **What:** Retrieve Spotify public profile. Returns normalized public profile metadata and preview playlists from Spotify's Web Player user-profile service. Provide username, uri, or url; defaults to Spotify's official profile.
- **Params:** `artist_limit` (integer, optional) — Recently played artist limit, clamped to 0-50; `episode_limit` (integer, optional) — Embedded episode limit, clamped to 0-50; `playlist_limit` (integer, optional) — Embedded public playlist limit, clamped to 0-50; `uri` (string, optional) — Spotify user URI; `url` (string, optional) — open.spotify.com user URL; `username` (string, optional) — Spotify username

### `spotify_profile_followers`

- **HTTP:** `GET /spotify/profile/followers`
- **What:** Retrieve Spotify public profile followers. Returns normalized public follower profiles from Spotify's Web Player user-profile service. Spotify exposes this as a public anonymous response for some profiles; private or restricted profiles may return an upstream error.
- **Params:** `limit` (integer, optional) — Follower limit, clamped to 1-200; `offset` (integer, optional) — Follower offset applied locally; `uri` (string, optional) — Spotify user URI; `url` (string, optional) — open.spotify.com user URL; `username` (string, optional) — Spotify username

### `spotify_profile_playlists`

- **HTTP:** `GET /spotify/profile/playlists`
- **What:** Retrieve Spotify public profile playlists. Returns normalized public playlists from Spotify's Web Player user-profile service. Provide username, uri, or url; defaults to Spotify's official profile.
- **Params:** `limit` (integer, optional) — Playlist limit, clamped to 1-50; `offset` (integer, optional) — Playlist offset; `uri` (string, optional) — Spotify user URI; `url` (string, optional) — open.spotify.com user URL; `username` (string, optional) — Spotify username

### `spotify_profiles_search`

- **HTTP:** `GET /spotify/profiles/search`
- **What:** Search Spotify profiles. Returns normalized Spotify Web Player profile search results for a search term. The endpoint fetches anonymous Spotify credentials at request time; caller-supplied Spotify bearer or client tokens are not required.
- **Params:** `include_album_pre_releases` (boolean, optional) — Include album pre-release results; `include_audiobooks` (boolean, optional) — Include audiobook context where available; `include_authors` (boolean, optional) — Include authors; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `include_pre_releases` (boolean, optional) — Include pre-release results; `limit` (integer, optional) — Profile result limit, clamped to 1-50; `number_of_top_results` (integer, optional) — Top result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Search term

### `spotify_search`

- **HTTP:** `GET /spotify/search`
- **What:** Search Spotify catalog. Returns normalized Spotify Web Player catalog search results across tracks, artists, albums, playlists, shows, episodes, audiobooks, and top results. The endpoint fetches anonymous Spotify credentials at request time; caller-supplied Spotify bearer or client tokens are not required.
- **Params:** `include_album_pre_releases` (boolean, optional) — Include album pre-release results; `include_artist_has_concerts_field` (boolean, optional) — Include artist concert availability fields; `include_audiobooks` (boolean, optional) — Include audiobook results; `include_authors` (boolean, optional) — Include authors; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `include_pre_releases` (boolean, optional) — Include pre-release results; `is_prefix` (boolean, optional) — Treat the search term as a prefix; `limit` (integer, optional) — Result limit per section, clamped to 1-50; `number_of_top_results` (integer, optional) — Top result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Search term

### `spotify_section`

- **HTTP:** `GET /spotify/section`
- **What:** Retrieve Spotify browse section. Returns normalized items from Spotify's browseSection Pathfinder response for a Spotify section URI.
- **Params:** `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `limit` (integer, optional) — Section item limit, clamped to 1-50; `offset` (integer, optional) — Section item offset; `uri` (string, optional) — Spotify section URI

### `spotify_shows_search`

- **HTTP:** `GET /spotify/shows/search`
- **What:** Search Spotify shows. Returns normalized Spotify Web Player show search results for a search term.
- **Params:** `limit` (integer, optional) — Result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Search term

### `spotify_track`

- **HTTP:** `GET /spotify/track`
- **What:** Retrieve Spotify track details. Returns normalized Spotify Web Player track metadata from Spotify's getTrack Pathfinder response. Provide either uri or id; defaults to a known public track when omitted.
- **Params:** `id` (string, optional) — Spotify track ID. Used when uri is omitted; `uri` (string, optional) — Spotify track URI or open.spotify.com track URL

### `spotify_track_recommended`

- **HTTP:** `GET /spotify/track/recommended`
- **What:** Retrieve Spotify recommended tracks. Returns normalized recommended Spotify entities from the internalLinkRecommenderTrack Pathfinder response.
- **Params:** `id` (string, optional) — Spotify track ID. Used when uri is omitted; `limit` (integer, optional) — Recommendation limit, clamped to 1-50; `uri` (string, optional) — Spotify track URI or open.spotify.com track URL

### `spotify_track_similar_albums`

- **HTTP:** `GET /spotify/track/similar-albums`
- **What:** Retrieve Spotify track similar albums. Returns normalized albums from the similarAlbumsBasedOnThisTrack Pathfinder response.
- **Params:** `albums_only` (boolean, optional) — Request albums-only recommendations; `id` (string, optional) — Spotify track ID. Used when uri is omitted; `limit` (integer, optional) — Album limit, clamped to 1-50; `uri` (string, optional) — Spotify track URI or open.spotify.com track URL

### `spotify_tracks_search`

- **HTTP:** `GET /spotify/tracks/search`
- **What:** Search Spotify tracks. Returns normalized Spotify Web Player track search results for a search term. The endpoint fetches anonymous Spotify credentials at request time; caller-supplied Spotify bearer or client tokens are not required.
- **Params:** `include_album_pre_releases` (boolean, optional) — Include album pre-release results; `include_audiobooks` (boolean, optional) — Include audiobook context where available; `include_authors` (boolean, optional) — Include authors; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `include_pre_releases` (boolean, optional) — Include pre-release results; `limit` (integer, optional) — Track result limit, clamped to 1-50; `number_of_top_results` (integer, optional) — Top result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Search term

## SpotifyPodcasts (8)

### `spotify_podcasts_categories`

- **HTTP:** `GET /spotify-podcasts/categories`
- **What:** Retrieve Spotify Podcasts categories. Returns normalized Spotify podcast category sections and items from Spotify's all-categories browsePage Pathfinder response.
- **Params:** `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `page_limit` (integer, optional) — Page pagination limit, clamped to 1-50; `page_offset` (integer, optional) — Page pagination offset; `section_limit` (integer, optional) — Section pagination limit, clamped to 1-50; `section_offset` (integer, optional) — Section pagination offset; `uri` (string, optional) — Spotify podcast categories page URI

### `spotify_podcasts_charts`

- **HTTP:** `GET /spotify-podcasts/charts`
- **What:** Retrieve Spotify podcast charts. Returns normalized Spotify podcast chart rankings from podcastcharts.byspotify.com. The chart and region parameters are validated against Spotify's supported podcast chart slugs and countries. Category charts are available only in au, br, de, gb, mx, se, and us.
- **Params:** `chart` (string, optional) — Chart slug. Allowed: top-podcasts, top-episodes, trending, arts, business, comedy, education, fiction, health-fitness, history, leisure, music, news, religion-spirituality, science, society-culture, sports, technology, true-crime, tv-film; `limit` (integer, optional) — Result limit, clamped to 1-100; `region` (string, optional) — Two-letter region code. Allowed: ar, au, at, br, ca, cl, co, dk, fi, fr, de, in, id, ie, it, jp, mx, nz, no, ph, pl, es, se, nl, gb, us

### `spotify_podcasts_episode`

- **HTTP:** `GET /spotify-podcasts/episode`
- **What:** Retrieve Spotify podcast episode details. Returns normalized public episode metadata from Spotify's getEpisodeOrChapter Pathfinder response, with episode page, embed page, and anonymous oEmbed fallbacks when Pathfinder is unavailable. Provide either uri or id; defaults to a known public episode when omitted.
- **Params:** `id` (string, optional) — Spotify episode ID. Used when uri is omitted; `uri` (string, optional) — Spotify episode URI or open.spotify.com episode URL

### `spotify_podcasts_home`

- **HTTP:** `GET /spotify-podcasts/home`
- **What:** Retrieve Spotify Podcasts home. Returns normalized sections and items from Spotify's podcast home browsePage Pathfinder response.
- **Params:** `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `page_limit` (integer, optional) — Page pagination limit, clamped to 1-50; `page_offset` (integer, optional) — Page pagination offset; `section_limit` (integer, optional) — Section pagination limit, clamped to 1-50; `section_offset` (integer, optional) — Section pagination offset; `uri` (string, optional) — Spotify page or genre URI

### `spotify_podcasts_search`

- **HTTP:** `GET /spotify-podcasts/search`
- **What:** Search Spotify Podcasts. Returns normalized Spotify podcast shows, episodes, and top results for a search term.
- **Params:** `include_album_pre_releases` (boolean, optional) — Include album pre-release results; `include_audiobooks` (boolean, optional) — Include audiobooks; `include_authors` (boolean, optional) — Include authors; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `include_pre_releases` (boolean, optional) — Include pre-release results; `limit` (integer, optional) — Result limit, clamped to 1-50; `number_of_top_results` (integer, optional) — Top result limit, clamped to 1-50; `offset` (integer, optional) — Search offset; `q` (string, **required**) — Podcast search term

### `spotify_podcasts_show`

- **HTTP:** `GET /spotify-podcasts/show`
- **What:** Retrieve Spotify podcast show metadata. Returns normalized podcast show metadata from Spotify Pathfinder.
- **Params:** `include_content_capability_trait` (boolean, optional) — Include content capability trait; `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `uri` (string, optional) — Spotify show URI

### `spotify_podcasts_show_episodes`

- **HTTP:** `GET /spotify-podcasts/show/episodes`
- **What:** Retrieve Spotify podcast show episodes. Returns normalized podcast episodes for a Spotify show URI.
- **Params:** `include_episode_content_ratings_v2` (boolean, optional) — Include Spotify episode content ratings v2; `limit` (integer, optional) — Episode limit, clamped to 1-50; `offset` (integer, optional) — Episode offset; `uri` (string, optional) — Spotify show URI

### `spotify_podcasts_show_recommendations`

- **HTTP:** `GET /spotify-podcasts/show/recommendations`
- **What:** Retrieve Spotify podcast recommendations. Returns normalized related Spotify shows and episodes from Spotify's show recommendations response.
- **Params:** `uri` (string, optional) — Spotify show URI

## ApplePodcasts (8)

### `apple_podcasts_charts`

- **HTTP:** `GET /apple-podcasts/charts`
- **What:** Retrieve Apple Podcasts chart rankings. Returns Apple Podcasts show chart rankings from public iTunes RSS JSON feeds. Supported collections are `toppodcasts` and `topaudiopodcasts`.
- **Params:** `category` (integer, optional) — Numeric Apple podcast genre ID; `collection` (string, optional) — Chart collection; `country` (string, optional) — Two-letter storefront country code; `limit` (integer, optional) — Number of chart items to return

### `apple_podcasts_charts_rankings`

- **HTTP:** `GET /apple-podcasts/charts/rankings`
- **What:** Retrieve Apple Podcasts chart rankings by algorithm, type, and genre. Returns Apple Podcasts chart rankings from the modern podcasts.apple.com charts page, covering chart algorithms (`top`, `top-subscriber`, `top-series`) crossed with entity types (`podcasts`, `podcast-episodes`, `podcast-channels`) and an optional genre filter. A richer, differently-sourced capability than the legacy RSS-based `/apple-podcasts/charts` endpoint.
- **Params:** `chart` (string, optional) — Chart algorithm. Allowed values: `top`, `top-subscriber`, `top-series`. Default `top`.; `country` (string, optional) — Two-letter storefront country code; `genre` (integer, optional) — Optional Apple Podcasts genre ID to filter the chart, e.g. 1303 for Comedy; `limit` (integer, optional) — Number of chart entries to return, default 24, max 200; `type` (string, optional) — Entity type. Allowed values: `podcasts`, `podcast-episodes`, `podcast-channels`. Default `podcasts`.

### `apple_podcasts_episodes_search`

- **HTTP:** `GET /apple-podcasts/episodes/search`
- **What:** Search Apple Podcasts episodes. Returns normalized Apple Podcasts episodes from Apple's public iTunes Search API.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Result language tag; `limit` (integer, optional) — Number of episodes per page; `page` (integer, optional) — Search page number (1-based); `term` (string, **required**) — Search term

### `apple_podcasts_new`

- **HTTP:** `GET /apple-podcasts/new`
- **What:** Retrieve Apple Podcasts curated "New" editorial shelves. Returns the curated editorial shelves from podcasts.apple.com/{country}/new (New Shows, New Seasons, New Trailers, Essentials, and other seasonal spotlights). Shelves that merely mirror a Charts Rankings query are omitted here since `/apple-podcasts/charts/rankings` already covers that data.
- **Params:** `country` (string, optional) — Two-letter storefront country code

### `apple_podcasts_search`

- **HTTP:** `GET /apple-podcasts/search`
- **What:** Search Apple Podcasts shows. Returns normalized Apple Podcasts shows from Apple's public iTunes Search API.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Result language tag; `limit` (integer, optional) — Number of shows per page; `page` (integer, optional) — Search page number (1-based); `term` (string, **required**) — Search term

### `apple_podcasts_show`

- **HTTP:** `GET /apple-podcasts/show/{id}`
- **What:** Retrieve Apple Podcasts show details. Returns normalized show metadata from Apple's public iTunes Lookup API.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Podcasts show ID; `lang` (string, optional) — Result language tag

### `apple_podcasts_show_episodes`

- **HTTP:** `GET /apple-podcasts/show/{id}/episodes`
- **What:** Retrieve Apple Podcasts show episodes. Returns a show and its public Apple Podcasts episodes from Apple's iTunes Lookup API.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Podcasts show ID; `lang` (string, optional) — Result language tag; `limit` (integer, optional) — Number of episodes to return

### `apple_podcasts_show_related`

- **HTTP:** `GET /apple-podcasts/show/{id}/related`
- **What:** Retrieve Apple Podcasts "You Might Also Like" related shows. Returns the "You Might Also Like" rail for a single show, sourced from the modern podcasts.apple.com show page's listener-cohort recommendation data.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Podcasts show ID; `limit` (integer, optional) — Number of related shows to return, default 20, max 50

## Discogs (7)

### `discogs_artist`

- **HTTP:** `GET /discogs/artist/{id}`
- **What:** Get a Discogs artist profile. Returns a normalized Discogs artist profile: real name, bio, links, name variations, aliases, and group memberships. Credential-free official Discogs database data.
- **Params:** `id` (string, **required**) — Discogs artist id

### `discogs_artist_releases`

- **HTTP:** `GET /discogs/artist/{id}/releases`
- **What:** List a Discogs artist's releases. Returns an artist's paginated release/master credits (role, format, label, year, want/collection counts). Credential-free official Discogs database data.
- **Params:** `id` (string, **required**) — Discogs artist id; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 50, max 100

### `discogs_label`

- **HTTP:** `GET /discogs/label/{id}`
- **What:** Get a Discogs label profile. Returns a normalized Discogs label profile: profile text, contact info, parent label, and sub-labels. Credential-free official Discogs database data.
- **Params:** `id` (string, **required**) — Discogs label id

### `discogs_label_releases`

- **HTTP:** `GET /discogs/label/{id}/releases`
- **What:** List a Discogs label's releases. Returns a label's paginated release catalog (title, artist, format, catalog number, year). Credential-free official Discogs database data.
- **Params:** `id` (string, **required**) — Discogs label id; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 50, max 100

### `discogs_master`

- **HTTP:** `GET /discogs/master/{id}`
- **What:** Get a Discogs master release. Returns a normalized Discogs master release: the version-agnostic grouping of a release across pressings/reissues (artists, tracklist, genres/styles, videos, images, marketplace stats). Credential-free official Discogs database data.
- **Params:** `id` (string, **required**) — Discogs master release id

### `discogs_release`

- **HTTP:** `GET /discogs/release/{id}`
- **What:** Get a Discogs release. Returns a normalized Discogs release: artists, labels, formats, tracklist, credits, identifiers, videos, images, and community want/have/rating. Credential-free official Discogs database data (api.discogs.com).
- **Params:** `id` (string, **required**) — Discogs release id

### `discogs_search`

- **HTTP:** `GET /discogs/search`
- **What:** Search the Discogs database. Searches Discogs releases, masters, artists, and labels. Credential-free official Discogs database data.
- **Params:** `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 50, max 100; `q` (string, **required**) — Search query; `type` (string, optional) — Result type filter

## SoundCloud (5)

### `soundcloud_playlist`

- **HTTP:** `GET /soundcloud/playlist`
- **What:** Get a SoundCloud playlist or album's detail. Returns one playlist or album's metadata plus its full track list: owner, likes/reposts counts, and every track's title, artwork, and playback/likes counts. Public data sourced from SoundCloud's own JSON API.
- **Params:** `url` (string, **required**) — Full soundcloud.com playlist/album URL (a playlist's permalink_url)

### `soundcloud_profile`

- **HTTP:** `GET /soundcloud/profile`
- **What:** Get a SoundCloud user/artist profile. Returns one user/artist's profile: bio, avatar, followers/followings/track/playlist/likes counts, and verified status. Public data sourced from SoundCloud's own JSON API.
- **Params:** `url` (string, **required**) — Full soundcloud.com user/artist profile URL

### `soundcloud_search`

- **HTTP:** `GET /soundcloud/search`
- **What:** Search SoundCloud tracks. Returns tracks matching a query: title, artwork, playback/likes/comment/repost counts, and uploader. Public data sourced from SoundCloud's own JSON API.
- **Params:** `limit` (integer, optional) — Number of tracks to return (default 20, max 50); `query` (string, **required**) — Search text

### `soundcloud_track`

- **HTTP:** `GET /soundcloud/track`
- **What:** Get a SoundCloud track's detail. Returns one track's full metadata: title, artwork, description, genre, tags, playback/likes/comment/repost counts, and uploader. Public data sourced from SoundCloud's own JSON API.
- **Params:** `url` (string, **required**) — Full soundcloud.com track URL (a track's permalink_url)

### `soundcloud_user_tracks`

- **HTTP:** `GET /soundcloud/user-tracks`
- **What:** Get a SoundCloud user's own uploaded tracks. Returns a user/artist's own uploaded tracks, most recent first: title, artwork, playback/likes/comment/repost counts. Public data sourced from SoundCloud's own JSON API.
- **Params:** `limit` (integer, optional) — Number of tracks to return (default 20, max 50); `url` (string, **required**) — Full soundcloud.com user/artist profile URL
