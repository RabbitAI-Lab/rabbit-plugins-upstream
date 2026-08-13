# Crawlora endpoint catalog

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

The complete Crawlora public-web-data API surface, grouped by platform. Use this to pick the right endpoint for any job, then call it via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**987 endpoints across 101 platform group(s).**

## Agoda (8)

### `agoda_activities_search`

- **HTTP:** `GET /agoda/activities/search`
- **What:** Search Agoda activities. Returns Agoda activities (tours, attractions, experiences) matching a free-text keyword and/or a city. When keyword is omitted, the resolved city's name is used instead to return a general listing of activities in that city. Callers may supply a known Agoda city id or a free-text city name for the city filter; when both are supplied city_id takes precedence. Credential-free public data from Agoda's own destination search.
- **Params:** `city` (string, optional) — Free-text city name, used directly as the search text when keyword is omitted, and to resolve a city id filter.; `city_id` (integer, optional) — Numeric Agoda city id to filter results to. Optional if keyword is supplied; city_id takes precedence over city when both are supplied.; `keyword` (string, optional) — Free-text activity search keyword. When omitted, the resolved city's name is used instead.

### `agoda_activity_detail`

- **HTTP:** `GET /agoda/activities/{activity_id}`
- **What:** Get Agoda activity detail. Returns full activity detail from Agoda: title, description, stated duration, categories, and content images. Credential-free public data from Agoda's own activity content source.
- **Params:** `activity_id` (string, **required**) — Numeric Agoda activity id, from a prior activities search call's activity_id field

### `agoda_flights_itinerary_amenities`

- **HTTP:** `POST /agoda/flights/itinerary-amenities`
- **What:** Get Agoda flight segment amenities. Returns real-content amenities (aircraft type, seat layout, meals, entertainment, wifi) for one or more flight segments. Copy the segments straight from a flight search response's own segment fields. Credential-free public data from Agoda's own flight content service.
- **Params:** `body` (object, **required**) — One or more flight segments to fetch amenities for

### `agoda_flights_search`

- **HTTP:** `GET /agoda/flights/search`
- **What:** Search Agoda one-way flights. Returns bookable one-way flight itineraries between two IATA airport codes for a departure date, including per-segment flight number, airline, times, layovers, aircraft type, and price. Resolve free-text city/airport names to codes first via the flight destination search endpoint. Credential-free public data from Agoda's own flight search.
- **Params:** `adults` (integer, optional) — Adult passengers (age 12+), defaults to 1; `cabin_class` (string, optional) — Cabin class, defaults to Economy; `children` (integer, optional) — Child passengers (age 2-11), defaults to 0; `departure_date` (string, **required**) — Departure date, YYYY-MM-DD; `destination` (string, **required**) — Destination IATA airport code; `infants` (integer, optional) — Infant passengers (under age 2), defaults to 0; `origin` (string, **required**) — Origin IATA airport code; `page` (integer, optional) — 1-indexed result page, defaults to 1

### `agoda_flights_search_locations`

- **HTTP:** `GET /agoda/flights/search-locations`
- **What:** Search Agoda flight destinations/airports. Resolves a free-text city or airport name into IATA airport codes for flight search, with each city's direct and nearby airports. Credential-free public data from Agoda's own flight destination search.
- **Params:** `keyword` (string, **required**) — Free-text city or airport name

### `agoda_homes_search`

- **HTTP:** `GET /agoda/homes/search`
- **What:** Search Agoda Homes & Apartments by city. Returns Homes & Apartments results for an Agoda city: full listing detail for every matching property whose accommodation type is Apartment, drawn from the same city search as hotel search and filtered to non-hotel accommodation types. Callers may supply a known Agoda city id or a free-text city name; when both are supplied city_id takes precedence. Credential-free public data from Agoda's own hotel/home search.
- **Params:** `city` (string, optional) — Free-text city name, resolved to a numeric city id via Agoda's own destination search. Ignored when city_id is also supplied.; `city_id` (integer, optional) — Numeric Agoda city id, e.g. 9395 for Bangkok. Either city_id or city is required; city_id takes precedence when both are supplied.; `limit` (integer, optional) — Candidate listings fetched per page before filtering to homes/apartments, defaults to 10, maximum 50; `page` (integer, optional) — 1-indexed result page over the underlying city search, defaults to 1

### `agoda_hotel_detail`

- **HTTP:** `GET /agoda/hotels/{property_id}`
- **What:** Get Agoda hotel detail. Returns full hotel detail from Agoda: identity (name, any former name), an accommodation type code, address (street address, postal code, city, country), guest rating, a main photo, room count, hotel chain id, a long and short description, and short-form policy statements (minimum age, adult/child definitions, extra-bed and additional-room booking policy). Credential-free public data from Agoda's own hotel content source.
- **Params:** `property_id` (string, **required**) — Numeric Agoda property id, from a prior search call's property_id field or the id embedded in an Agoda hotel URL

### `agoda_hotels_search`

- **HTTP:** `GET /agoda/hotels/search`
- **What:** Search Agoda hotels by city. Returns hotel search results for an Agoda city: the matching property ids for that city plus a direct link to each property's listing page. Callers may supply a known Agoda city id or a free-text city name; when both are supplied city_id takes precedence. Credential-free public data from Agoda's own hotel search.
- **Params:** `city` (string, optional) — Free-text city name, resolved to a numeric city id via Agoda's own destination search. Ignored when city_id is also supplied.; `city_id` (integer, optional) — Numeric Agoda city id, e.g. 9395 for Bangkok. Either city_id or city is required; city_id takes precedence when both are supplied.; `limit` (integer, optional) — Results per page, defaults to 10, maximum 50; `page` (integer, optional) — 1-indexed result page, defaults to 1

## Airbnb (7)

### `airbnb_host`

- **HTTP:** `GET /airbnb/host/{id}`
- **What:** Get Airbnb host profile. Returns a normalized Airbnb public host profile — display name, Superhost and identity-verification status, location, bio, hosting tenure, total guest-review count, and total listing count.
- **Params:** `id` (string, **required**) — Host id (numeric)

### `airbnb_host_listings`

- **HTTP:** `GET /airbnb/host/{id}/listings`
- **What:** Get Airbnb host listings. Returns the listings an Airbnb host manages, paginated. Page 1 comes from the host profile; deeper pages page through the host's full portfolio.
- **Params:** `id` (string, **required**) — Host id (numeric); `page` (integer, optional) — 1-based page

### `airbnb_host_reviews`

- **HTTP:** `GET /airbnb/host/{id}/reviews`
- **What:** Get Airbnb host reviews. Returns reviews guests left for an Airbnb host, paginated, including the reviewer name and location.
- **Params:** `id` (string, **required**) — Host id (numeric); `page` (integer, optional) — 1-based page

### `airbnb_room`

- **HTTP:** `GET /airbnb/room/{id}`
- **What:** Get Airbnb room. Returns normalized Airbnb public room details.
- **Params:** `id` (string, **required**) — Room id

### `airbnb_room_calendar`

- **HTTP:** `GET /airbnb/room/{id}/calendar`
- **What:** Get Airbnb room calendar. Returns public calendar month hints parsed from Airbnb room bootstrap data.
- **Params:** `id` (string, **required**) — Room id

### `airbnb_room_reviews`

- **HTTP:** `GET /airbnb/room/{id}/reviews`
- **What:** Get Airbnb room reviews. Returns normalized Airbnb public review snippets.
- **Params:** `id` (string, **required**) — Room id; `page` (integer, optional) — 1-based page

### `airbnb_search`

- **HTTP:** `GET /airbnb/search`
- **What:** Search Airbnb stays. Returns normalized Airbnb public web search results.
- **Params:** `adults` (integer, optional) — Adult guests; `check_in` (string, optional) — Check-in date; `check_out` (string, optional) — Check-out date; `currency` (string, optional) — Currency for bounded map search; `location` (string, **required**) — Location; `ne_lat` (number, optional) — Northeast latitude for bounded map search; `ne_lng` (number, optional) — Northeast longitude for bounded map search; `page` (integer, optional) — 1-based page; `sw_lat` (number, optional) — Southwest latitude for bounded map search; `sw_lng` (number, optional) — Southwest longitude for bounded map search; `zoom` (integer, optional) — Map zoom for bounded map search

## Amazon (3)

### `amazon_product`

- **HTTP:** `GET /amazon/product/{asin}`
- **What:** Retrieve Amazon product details. Returns normalized product details for an Amazon ASIN on `amazon.com`, including pricing, availability, overview data, inline review samples, and descriptive content.
- **Params:** `asin` (string, **required**) — Amazon ASIN; `currency` (string, optional) — Amazon currency; `language` (string, optional) — Amazon language

### `amazon_search`

- **HTTP:** `GET /amazon/search`
- **What:** Search Amazon products. Returns normalized Amazon search result cards for `amazon.com`.
- **Params:** `k` (string, **required**) — Search keyword; `page` (integer, optional) — 1-based page number; `s` (string, optional) — Sort order

### `amazon_suggest`

- **HTTP:** `GET /amazon/suggest/{keyword}`
- **What:** Retrieve Amazon search suggestions. Returns typeahead keyword suggestions from Amazon's public suggestion API for `amazon.com`.
- **Params:** `keyword` (string, **required**) — Suggestion prefix

## Amazon Jobs (2)

### `amazon_jobs_job`

- **HTTP:** `GET /amazon-jobs/job`
- **What:** Amazon Jobs single posting. Returns one Amazon.jobs posting by its numeric job id (the `id` field returned by search). Parsed from amazon.jobs's stable server-rendered job detail page — there is no separate JSON detail endpoint upstream.
- **Params:** `id` (string, **required**) — Numeric Amazon job id

### `amazon_jobs_search`

- **HTTP:** `GET /amazon-jobs/search`
- **What:** Amazon Jobs search. Searches Amazon's public careers site (amazon.jobs) via its credential-free search JSON. Each result includes the full description and qualifications inline. `sort` accepts `relevant` (default, upstream relevance ranking) or `recent` (newest posted first). Either `q` or `category` (or both) must be given -- `category` filters by Amazon's own job-category taxonomy and works with no text query at all.
- **Params:** `category` (string, optional) — Amazon's own job-category taxonomy slug. Either q or category is required; `country` (string, optional) — ISO 3166-1 alpha-3 country code filter; `limit` (integer, optional) — Results per page, max 100 (default 20); `page` (integer, optional) — Page number, 1-based; `q` (string, optional) — Search query. Either q or category is required; `sort` (string, optional) — Sort order

## Anime (9)

### `anime_airing_schedule`

- **HTTP:** `GET /anime/airing-schedule`
- **What:** Upcoming anime airing schedule. Returns upcoming anime episode broadcasts (episode number, air time, countdown, and the normalized title), soonest first, paginated. Credential-free public AniList data.
- **Params:** `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 20, max 50

### `anime_character`

- **HTTP:** `GET /anime/character/{id}`
- **What:** Get an anime/manga character. Returns a normalized character profile by AniList id: names, image, description, gender, age, blood type, birthday, favourites, and the titles the character appears in with their billed role. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList character id

### `anime_character_search`

- **HTTP:** `GET /anime/character/search`
- **What:** Search anime & manga characters. Searches anime and manga characters by name. Returns character summaries (name, native name, image, favourites), paginated. Credential-free public AniList data.
- **Params:** `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50; `query` (string, **required**) — Search text

### `anime_rankings`

- **HTTP:** `GET /anime/rankings`
- **What:** Rank anime. Returns a filterable, sorted anime ranking. Credential-free public AniList data. Filter by season, year, format, genre, and status.
- **Params:** `format` (string, optional) — Format filter: TV, TV_SHORT, MOVIE, SPECIAL, OVA, ONA, MUSIC.; `genre` (string, optional) — Genre filter, e.g. Fantasy.; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 20, max 50; `season` (string, optional) — Airing season filter: WINTER, SPRING, SUMMER, FALL.; `season_year` (integer, optional) — Airing year filter, 1940-2100.; `sort` (string, optional) — Order: TRENDING_DESC, POPULARITY_DESC, SCORE_DESC, FAVOURITES_DESC, START_DATE_DESC, UPDATED_AT_DESC. Default TRENDING_DESC.; `status` (string, optional) — Status filter: FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED, HIATUS.

### `anime_search`

- **HTTP:** `GET /anime/search`
- **What:** Search anime. Searches anime by free-text query. Credential-free public anime data from AniList. Returns normalized entries: titles, scores, popularity, format, status, season, genres, tags, and studios.
- **Params:** `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50; `query` (string, **required**) — Search text; `sort` (string, optional) — Ordering: SEARCH_MATCH, POPULARITY_DESC, SCORE_DESC, TRENDING_DESC, FAVOURITES_DESC, START_DATE_DESC. Default SEARCH_MATCH.

### `anime_title`

- **HTTP:** `GET /anime/title/{id}`
- **What:** Get an anime. Returns a normalized anime by AniList id: titles (romaji/english/native), MyAnimeList id, scores, popularity, favourites, format, status, season, episodes, duration, genres, ranked tags, studios, dates, description, images, and next-airing countdown. Pass mal=true to additionally enrich the response with the MyAnimeList community score (mal block: score on a 0-10 scale, plus scored-by count), scraped credential-free from the public MAL page. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList anime id; `mal` (boolean, optional) — Enrich with the MyAnimeList community score (adds one fetch; omitted when the title has no MAL id)

### `anime_title_characters`

- **HTTP:** `GET /anime/title/{id}/characters`
- **What:** List an anime's characters. Returns an anime's cast (character name, native name, billed role, image, favourites), paginated. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList anime id; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50

### `anime_title_recommendations`

- **HTTP:** `GET /anime/title/{id}/recommendations`
- **What:** List an anime's recommendations. Returns community-recommended titles for an anime, each with a recommendation rating and the full normalized media entry, paginated. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList anime id; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50

### `anime_title_staff`

- **HTTP:** `GET /anime/title/{id}/staff`
- **What:** List an anime's staff. Returns the people credited on an anime (name, production role, occupations, image), paginated. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList anime id; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50

## Apple Jobs (2)

### `apple_jobs_job`

- **HTTP:** `GET /apple-jobs/job`
- **What:** Apple Jobs single posting. Returns one Apple Careers posting by its job id (the `id` field returned by search, e.g. `200674676-0836` for a specific requisition or `PIPE-200314122` for an evergreen/pipeline retail role). Parsed from jobs.apple.com's server-rendered job detail page.
- **Params:** `id` (string, **required**) — Apple job id

### `apple_jobs_search`

- **HTTP:** `GET /apple-jobs/search`
- **What:** Apple Jobs search. Searches Apple's public careers site (jobs.apple.com) via its server-rendered search page's embedded job data. Page size is fixed by Apple at 20 results. Search results carry identity/location/team metadata only — call the job endpoint for the full description and qualifications.
- **Params:** `location` (string, optional) — Location filter in Apple's own slug format, e.g. united-states-USA or singapore-SGP; `page` (integer, optional) — Page number, 1-based; `q` (string, **required**) — Search query

## AppleBooks (12)

### `apple_books_audiobook`

- **HTTP:** `GET /apple-books/audiobook/{id}`
- **What:** Retrieve Apple Books audiobook details. Returns normalized audiobook metadata from Apple Books' public catalog page, including narrator, duration, audio preview, and a cross-link to the ebook edition (when one exists).
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Books numeric audiobook ID; `lang` (string, optional) — Result language tag

### `apple_books_audiobook_reviews`

- **HTTP:** `GET /apple-books/audiobook/{id}/reviews`
- **What:** Retrieve Apple Books audiobook customer reviews. Returns a page of an audiobook's customer reviews. The default first page is served from the audiobook's own catalog page; deeper pages (page>1 or a larger limit) page through Apple's review API directly, up to 20 per page.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Books numeric audiobook ID; `lang` (string, optional) — Result language tag; `limit` (integer, optional) — Reviews per page, default 10, max 20; `page` (integer, optional) — Review page number, default 1

### `apple_books_audiobook_search`

- **HTTP:** `GET /apple-books/audiobook/search`
- **What:** Search Apple Books audiobooks. Returns normalized Apple Books audiobooks from Apple's public iTunes Search API.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Result language tag; `limit` (integer, optional) — Number of audiobooks per page; `page` (integer, optional) — Search page number (1-based); `term` (string, **required**) — Search term

### `apple_books_audiobook_series`

- **HTTP:** `GET /apple-books/audiobook-series/{id}`
- **What:** Retrieve an Apple Books audiobook series and its full audiobook list. Returns series metadata and the full ordered list of audiobooks in the series from Apple Books' public catalog page. An audio-book-series is a catalog resource distinct from a book-series, even for the same conceptual series.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Books numeric audiobook series ID; `lang` (string, optional) — Result language tag

### `apple_books_audiobook_similar`

- **HTTP:** `GET /apple-books/audiobook/{id}/similar`
- **What:** Retrieve "Customers Also Bought" audiobooks. Returns the related audiobooks shown on the Apple Books catalog page.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Books numeric audiobook ID; `lang` (string, optional) — Result language tag

### `apple_books_author`

- **HTTP:** `GET /apple-books/author/{id}`
- **What:** Retrieve an Apple Books author's bibliography. Returns author metadata and their full ebook (and audiobook, where available) bibliography from Apple Books' public catalog page.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Books numeric author ID; `lang` (string, optional) — Result language tag

### `apple_books_book`

- **HTTP:** `GET /apple-books/book/{id}`
- **What:** Retrieve Apple Books book details. Returns normalized book metadata from Apple Books' public catalog page, including ISBN, page count, publisher, audience, rating histogram, and series linkage.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Books numeric book ID; `lang` (string, optional) — Result language tag

### `apple_books_book_reviews`

- **HTTP:** `GET /apple-books/book/{id}/reviews`
- **What:** Retrieve Apple Books customer reviews. Returns a page of a book's customer reviews. The default first page is served from the book's own catalog page; deeper pages (page>1 or a larger limit) page through Apple's review API directly, up to 20 per page.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Books numeric book ID; `lang` (string, optional) — Result language tag; `limit` (integer, optional) — Reviews per page, default 10, max 20; `page` (integer, optional) — Review page number, default 1

### `apple_books_book_similar`

- **HTTP:** `GET /apple-books/book/{id}/similar`
- **What:** Retrieve "Customers Also Bought" books. Returns the related books shown on the Apple Books catalog page.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Books numeric book ID; `lang` (string, optional) — Result language tag

### `apple_books_charts`

- **HTTP:** `GET /apple-books/charts`
- **What:** Retrieve Apple Books chart rankings. Returns Apple Books chart rankings from Apple's public marketing-tools RSS JSON feed. Supported collections are `top-free` and `top-paid`.
- **Params:** `collection` (string, optional) — Chart collection. Allowed values: top-free, top-paid; `country` (string, optional) — Two-letter storefront country code; `genre` (integer, optional) — Optional Apple Books genre ID to filter the chart; `limit` (integer, optional) — Number of chart items to return

### `apple_books_search`

- **HTTP:** `GET /apple-books/search`
- **What:** Search Apple Books titles. Returns normalized Apple Books ebooks from Apple's public iTunes Search API.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Result language tag; `limit` (integer, optional) — Number of books per page; `page` (integer, optional) — Search page number (1-based); `term` (string, **required**) — Search term

### `apple_books_series`

- **HTTP:** `GET /apple-books/series/{id}`
- **What:** Retrieve an Apple Books series and its full book list. Returns series metadata and the full ordered list of books in the series from Apple Books' public catalog page.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Apple Books numeric series ID; `lang` (string, optional) — Result language tag

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

## AppStore (12)

### `appstore_app`

- **HTTP:** `GET /appstore/app`
- **What:** Retrieve full App Store app details. Returns normalized app metadata from the App Store lookup API. Provide either `id` (numeric track ID) or `app_id` (bundle ID). `id`/`app_id` can identify an iPhone, iPad, or Mac App Store listing.
- **Params:** `app_id` (string, optional) — App Store bundle ID; `country` (string, optional) — Two-letter storefront country code; `id` (string, optional) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag; `platforms` (boolean, optional) — Include the full device-platform compatibility list (adds one extra upstream fetch); `ratings` (boolean, optional) — Include ratings histogram

### `appstore_developer`

- **HTTP:** `GET /appstore/developer/{dev_id}`
- **What:** Retrieve apps by developer ID. Returns App Store apps associated with a specific developer artist ID.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `dev_id` (string, **required**) — Developer artist ID; `lang` (string, optional) — Result language tag

### `appstore_editorial`

- **HTTP:** `GET /appstore/editorial`
- **What:** Retrieve an App Store device or Arcade editorial landing page. Returns the curated editorial shelves from one of Apple's per-device App Store landing pages (the same content shown by apps.apple.com's device switcher). `device` enum: `iphone`, `ipad`, `mac`, `vision`, `watch`, `tv`. `section` enum: `main` (the device's Today/Discover/Apps & Games landing page), `arcade` (the device's Apple Arcade landing page). Watch has no Arcade page — `device=watch` with `section=arcade` returns `400`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `device` (string, **required**) — Apple device catalog; `lang` (string, optional) — Result language tag; `section` (string, optional) — Editorial section within the device

### `appstore_editorial_category`

- **HTTP:** `GET /appstore/editorial/category`
- **What:** Retrieve an App Store category-scoped editorial page. Returns the curated editorial shelves for one device category page (e.g. "Entertainment Apps for Vision"). `category_id` is a numeric, device-specific editorial page ID — not a static enum — discovered from an `appstore_editorial` response for the SAME `device`, in its "Browse by Category" shelf items' `destination_id` field. `device` enum: `iphone`, `ipad`, `mac`, `vision`, `watch`, `tv`.
- **Params:** `category_id` (string, **required**) — Numeric App Store editorial page ID, discovered from appstore_editorial (same device); `country` (string, optional) — Two-letter storefront country code; `device` (string, **required**) — Apple device catalog; `lang` (string, optional) — Result language tag

### `appstore_list`

- **HTTP:** `GET /appstore/list`
- **What:** Retrieve App Store collection rankings. Returns ranked App Store apps from an iTunes RSS collection, optionally expanded to full lookup details. `collection` enum: `topfreeapplications`, `toppaidapplications`, `topgrossingapplications`, `topfreeipadapplications`, `toppaidipadapplications`, `topgrossingipadapplications`, `topmacapps`, `topfreemacapps`, `topgrossingmacapps`, `toppaidmacapps`, `newapplications`, `newfreeapplications`, `newpaidapplications`. Of the Mac collections, only `topfreemacapps` currently returns ranked apps — `topmacapps`, `topgrossingmacapps`, and `toppaidmacapps` are accepted but Apple's feed for them is currently empty. There is no separate Games `collection` — combine any collection with `category=6014` (or a Games subgenre ID, e.g. `7012` for Puzzle) to get its Games-only equivalent, e.g. Top Free Games. See the endpoint markdown for the full category ID table.
- **Params:** `category` (integer, optional) — Numeric App Store category ID, see description for the full enum; e.g. 6014 = Games, 7012 = Games/Puzzle; `collection` (string, optional) — Chart collection slug, see description for the full enum; `country` (string, optional) — Two-letter storefront country code; `full_detail` (boolean, optional) — Expand each app via lookup API; `lang` (string, optional) — Result language tag; `num` (integer, optional) — Number of apps to return

### `appstore_privacy`

- **HTTP:** `GET /appstore/privacy/{id}`
- **What:** Retrieve App Store privacy disclosures. Returns the app privacy cards shown on the App Store page, including data categories and purposes.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag

### `appstore_ratings`

- **HTTP:** `GET /appstore/ratings`
- **What:** Retrieve App Store ratings histogram. Returns total ratings count and the 1-5 star histogram shown on the App Store product page.
- **Params:** `app_id` (string, optional) — App Store bundle ID; `country` (string, optional) — Two-letter storefront country code; `id` (string, optional) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag

### `appstore_reviews`

- **HTTP:** `GET /appstore/reviews`
- **What:** Retrieve App Store reviews. Returns one page of customer reviews for an app. Provide either `id` (numeric track ID) or `app_id` (bundle ID).
- **Params:** `app_id` (string, optional) — App Store bundle ID; `country` (string, optional) — Two-letter storefront country code; `id` (string, optional) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag; `page` (integer, optional) — Review page number (1-10); `sort` (string, optional) — Sort order

### `appstore_search`

- **HTTP:** `GET /appstore/search`
- **What:** Search the App Store. Returns App Store search results for a term. Set `ids_only=true` to return only app IDs. `platform` enum: `phone`, `pad`, `mac`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `ids_only` (boolean, optional) — Return only app IDs; `lang` (string, optional) — Result language tag; `num` (integer, optional) — Number of apps per page; `page` (integer, optional) — Search page number (1-based); `platform` (string, optional) — App Store catalog to search: phone, pad, mac; `term` (string, **required**) — Search term

### `appstore_similar`

- **HTTP:** `GET /appstore/similar`
- **What:** Retrieve "You Might Also Like" apps. Returns the related apps shown on the App Store product page. Provide either `id` (numeric track ID) or `app_id` (bundle ID).
- **Params:** `app_id` (string, optional) — App Store bundle ID; `country` (string, optional) — Two-letter storefront country code; `id` (string, optional) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag

### `appstore_suggest`

- **HTTP:** `GET /appstore/suggest/{term}`
- **What:** Retrieve App Store search suggestions. Returns suggested search terms for the given partial keyword.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `term` (string, **required**) — Partial search term

### `appstore_version_history`

- **HTTP:** `GET /appstore/version-history/{id}`
- **What:** Retrieve App Store version history. Returns the version history entries shown in the App Store "What's New" section.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — App Store numeric track ID (digits only); `lang` (string, optional) — Result language tag

## Autotrader (3)

### `autotrader_dealer`

- **HTTP:** `GET /autotrader/dealer/{id}`
- **What:** Get Autotrader dealer profile. Returns a normalized Autotrader dealer profile (name, phone, address, rating, website) plus a first page of the dealer's own current inventory as normalized vehicle summaries and the dealer's total listing count. Credential-free public data sourced from Autotrader's own server-rendered dealer profile page.
- **Params:** `id` (string, **required**) — Autotrader dealer/owner id, the numeric path segment of a /car-dealers/{id} URL

### `autotrader_search`

- **HTTP:** `GET /autotrader/search`
- **What:** Search Autotrader vehicle listings. Searches Autotrader for new and used car listings, returning normalized vehicle summaries (make, model, trim, year, mileage, pricing, images) plus the total matching count. Credential-free public data sourced from Autotrader's own server-rendered search page.
- **Params:** `body_style` (string, optional) — Body style. Allowed values: convertible, coupe, hatchback, sedan, suv, truck, van, wagon; `condition` (string, optional) — Listing condition. Allowed values: new, used, certified, 3p_cert; `make` (string, optional) — Autotrader make code, e.g. TOYOTA, HONDA, BMW; `max_mileage` (integer, optional) — Maximum odometer mileage; `max_price` (integer, optional) — Maximum price in US dollars; `max_year` (integer, optional) — Maximum model year; `min_price` (integer, optional) — Minimum price in US dollars; `min_year` (integer, optional) — Minimum model year; `model` (string, optional) — Autotrader model code, e.g. CAMRY. Requires make; `page` (integer, optional) — 1-indexed result page, defaults to 1. Autotrader returns 24 results per page; `query` (string, optional) — Free-text keyword search; `radius` (integer, optional) — Search radius in miles around zip; `seller_type` (string, optional) — Seller type. Allowed values: dealer, private; `trim` (string, optional) — Autotrader trim code. Requires make and model; `zip` (string, optional) — 5-digit US ZIP code to search around

### `autotrader_vehicle`

- **HTTP:** `GET /autotrader/vehicle/{id}`
- **What:** Get Autotrader vehicle listing detail. Returns a normalized Autotrader vehicle listing: full vehicle spec (make, model, trim, mileage, colors, transmission, fuel type, engine, images, pricing), the full listing description, and seller detail (dealership or private seller). Credential-free public data sourced from Autotrader's own server-rendered vehicle detail page.
- **Params:** `id` (string, **required**) — Autotrader listing id, the numeric path segment of a /cars-for-sale/vehicle/{id} URL

## Bing (5)

### `bing_images`

- **HTTP:** `GET /bing/images`
- **What:** Search Bing image results. Returns normalized Bing image search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Bing image HTML/async pages and return 503 when Bing serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

### `bing_news`

- **HTTP:** `GET /bing/news`
- **What:** Search Bing news results. Returns normalized Bing news search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Bing news HTML/async pages and return 503 when Bing serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

### `bing_search`

- **HTTP:** `GET /bing/search`
- **What:** Search Bing web results. Returns normalized Bing web search results for a query string, including organic results, optional context panel data, related queries, people-also-ask questions, news modules, video modules, and page-based pagination. Empty optional blocks are omitted from the JSON response. Locale defaults to country=us and lang=en-us. Results are fetched with a Chrome-impersonated request client and return 503 when Bing serves a challenge page, unusable HTML, or a response whose results are unrelated to the query. Queries that use the site: operator (for example site:gov.hu) are not supported: Bing serves a bot-verification challenge for them, so they are rejected with 400 before any request is made. Use the Google search endpoint (/api/v1/google/search) for domain-restricted searches.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

### `bing_suggest`

- **HTTP:** `GET /bing/suggest`
- **What:** Suggest Bing search queries. Returns Bing autosuggest query completions for a query prefix. Locale defaults to country=us and lang=en-us. Suggestions are fetched from public Bing suggest endpoints and trimmed to the requested count.
- **Params:** `count` (integer, optional) — Suggestions to return; defaults to 10, clamped to 1..12; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `q` (string, **required**) — Search query prefix

### `bing_videos`

- **HTTP:** `GET /bing/videos`
- **What:** Search Bing video results. Returns normalized Bing video search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Bing video HTML/async pages and return 503 when Bing serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Bing UI language; defaults to en-us; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

## Bluesky (7)

### `bluesky_author_feed`

- **HTTP:** `GET /bluesky/author-feed`
- **What:** A Bluesky account's posts. Returns a page of a Bluesky account's posts, newest first, including text, engagement counts, and any attached images/link card/quoted post. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `actor` (string, **required**) — A handle (e.g. bsky.app) or DID; `cursor` (string, optional) — Pagination cursor from a previous response's cursor field; `limit` (integer, optional) — Page size, 1-100

### `bluesky_followers`

- **HTTP:** `GET /bluesky/followers`
- **What:** A Bluesky account's followers. Returns a page of a Bluesky account's followers. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `actor` (string, **required**) — A handle (e.g. bsky.app) or DID; `cursor` (string, optional) — Pagination cursor from a previous response's cursor field; `limit` (integer, optional) — Page size, 1-100

### `bluesky_follows`

- **HTTP:** `GET /bluesky/follows`
- **What:** Accounts a Bluesky account follows. Returns a page of the accounts a Bluesky account follows. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `actor` (string, **required**) — A handle (e.g. bsky.app) or DID; `cursor` (string, optional) — Pagination cursor from a previous response's cursor field; `limit` (integer, optional) — Page size, 1-100

### `bluesky_post_thread`

- **HTTP:** `GET /bluesky/post-thread`
- **What:** A Bluesky post and its reply tree. Returns a Bluesky post along with its nested replies (and, when the post is itself a reply, its parent chain), up to `depth` levels deep. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `depth` (integer, optional) — Reply-tree depth, 1-10; `uri` (string, **required**) — The post's at:// URI, e.g. from an author-feed or search-actors result's post uri field

### `bluesky_profile`

- **HTTP:** `GET /bluesky/profile`
- **What:** A Bluesky account's full public profile. Returns a Bluesky account's public profile: display name, description, avatar/banner images, and follower/follows/posts counts. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `actor` (string, **required**) — A handle (e.g. bsky.app) or DID (e.g. did:plc:z72i7hdynmk6r22z27h6tvur)

### `bluesky_search_actors`

- **HTTP:** `GET /bluesky/search-actors`
- **What:** Search Bluesky accounts. Returns Bluesky accounts matching a query against display name, handle, and profile description. Public data, sourced from the AT Protocol's public, credential-free AppView API.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous response's cursor field; `limit` (integer, optional) — Page size, 1-100; `q` (string, **required**) — Search text

### `bluesky_trending_topics`

- **HTTP:** `GET /bluesky/trending-topics`
- **What:** Bluesky's current trending topics. Returns Bluesky's current trending topics and suggested feeds, each with a link to its feed. Public data, sourced from the AT Protocol's public, credential-free AppView API. This surface is less stable than the rest of this family -- Bluesky may change its shape without notice.
- **Params:** _none_

## Booking (8)

### `booking_attractions_detail`

- **HTTP:** `GET /booking-attractions/detail`
- **What:** Booking.com attraction detail. Returns a Booking.com attraction's detail page.
- **Params:** `slug` (string, **required**) — Attraction slug, from a prior attraction search result

### `booking_attractions_reviews`

- **HTTP:** `GET /booking-attractions/reviews`
- **What:** Booking.com attraction reviews. Returns normalized guest reviews for a Booking.com attraction.
- **Params:** `limit` (integer, optional) — Reviews per page, 1-50, default 10; `page` (integer, optional) — 1-based result page, default 1; `product_id` (string, **required**) — Attraction product id, from a prior attraction search result

### `booking_attractions_search`

- **HTTP:** `GET /booking-attractions/search`
- **What:** Search Booking.com attractions. Returns normalized Booking.com attractions/things-to-do search results for a destination and date range, with an optional category/subcategory filter and a discoverable category taxonomy.
- **Params:** `category` (string, optional) — Optional top-level category tagname filter, from a prior response's categories; `end_date` (string, optional) — Availability end date, YYYY-MM-DD, defaults to start_date; `limit` (integer, optional) — Results per page, 1-30, default 15; `page` (integer, optional) — 1-based result page, default 1; `query` (string, **required**) — Destination name or city; `start_date` (string, **required**) — Availability start date, YYYY-MM-DD; `subcategory` (string, optional) — Optional subcategory tagname filter, from a prior response's categories

### `booking_flights_autocomplete`

- **HTTP:** `GET /booking-flights/autocomplete`
- **What:** Booking.com flight autocomplete. Returns Booking.com flight-search location suggestions (airports/cities) for a query string.
- **Params:** `origin` (string, optional) — Optional origin location code, biases results by proximity; `origin_type` (string, optional) — Origin location type; `query` (string, **required**) — City or airport name/code to search; `type` (string, optional) — Location role, default to

### `booking_flights_search`

- **HTTP:** `GET /booking-flights/search`
- **What:** Search Booking.com flights. Returns normalized round-trip or one-way flight offers between two Booking.com flight-search locations.
- **Params:** `adults` (integer, optional) — Number of adults, 1-9, default 1; `cabin_class` (string, optional) — Cabin class, default ECONOMY; `children` (integer, optional) — Number of children, 0-9; `depart` (string, **required**) — Departure date, YYYY-MM-DD; `from` (string, **required**) — Origin location id, e.g. SGN.AIRPORT, from a prior autocomplete result; `from_country` (string, optional) — Origin country code; `return` (string, optional) — Return date, YYYY-MM-DD, required when type is ROUNDTRIP; `sort` (string, optional) — Result sort order, default BEST; `to` (string, **required**) — Destination location id, same composite format as from; `to_country` (string, optional) — Destination country code; `type` (string, optional) — Trip type, default ROUNDTRIP

### `booking_hotel_detail`

- **HTTP:** `GET /booking/hotel-detail`
- **What:** Booking.com hotel detail. Returns a Booking.com hotel's core detail page: rating, facilities, highlights, house rules, cover photos, and rooms with their own photos.
- **Params:** `hotel_id` (integer, **required**) — Booking.com hotel id, from a prior search's property id

### `booking_reviews`

- **HTTP:** `GET /booking/reviews`
- **What:** Booking.com hotel reviews. Returns normalized guest reviews for a Booking.com hotel, with an optional free-text search over review content.
- **Params:** `destination_id` (integer, optional) — Destination id (ufi), from a prior search response; `hotel_country_code` (string, **required**) — Hotel's country code, from a prior search response; `hotel_id` (integer, **required**) — Booking.com hotel id, from a prior search's property id; `hotel_score` (number, optional) — Hotel's overall review score; `limit` (integer, optional) — Reviews per page, 1-25, default 10; `page` (integer, optional) — 1-based result page, default 1; `search_text` (string, optional) — Optional free-text search over review content

### `booking_search`

- **HTTP:** `GET /booking/search`
- **What:** Search Booking.com hotels. Returns normalized Booking.com hotel search results for a destination and date range.
- **Params:** `adults` (integer, optional) — Number of adults, 1-9, default 2; `checkin` (string, **required**) — Check-in date, YYYY-MM-DD; `checkout` (string, **required**) — Check-out date, YYYY-MM-DD; `children` (integer, optional) — Number of children, 0-9; `page` (integer, optional) — 1-based result page, default 1; `query` (string, **required**) — Destination name or city; `rooms` (integer, optional) — Number of rooms, 1-8, default 1

## Box Office Mojo (21)

### `boxofficemojo_brand`

- **HTTP:** `GET /boxofficemojo/brand`
- **What:** Box Office Mojo brand detail. Returns normalized release rows from a public Box Office Mojo brand page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo brand id; `offset` (integer, optional) — Row offset for pagination (page size 100); `path` (string, optional) — Box Office Mojo brand path; `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction; `url` (string, optional) — Absolute https://www.boxofficemojo.com brand URL

### `boxofficemojo_brands`

- **HTTP:** `GET /boxofficemojo/brands`
- **What:** Box Office Mojo brand chart. Returns normalized rows from Box Office Mojo's public brand chart.
- **Params:** `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction

### `boxofficemojo_calendar`

- **HTTP:** `GET /boxofficemojo/calendar`
- **What:** Box Office Mojo domestic release schedule. Returns normalized grouped rows from Box Office Mojo's public domestic release schedule. Provide `year` and `month`.
- **Params:** `month` (integer, **required**) — Calendar month, 1 through 12; `year` (integer, **required**) — Calendar year, from 1921 through 2100

### `boxofficemojo_calendar_changes`

- **HTTP:** `GET /boxofficemojo/calendar/changes`
- **What:** Box Office Mojo domestic release schedule changes. Returns normalized grouped rows from Box Office Mojo's public domestic release-schedule changes page.
- **Params:** `offset` (integer, optional) — Changes page offset. Allowed values: 0, 30, 60, ... 780

### `boxofficemojo_calendar_date`

- **HTTP:** `GET /boxofficemojo/calendar/date`
- **What:** Box Office Mojo domestic release schedule date. Returns normalized release rows for one public Box Office Mojo domestic release-schedule date.
- **Params:** `date` (string, **required**) — Calendar date in YYYY-MM-DD format

### `boxofficemojo_date_domestic`

- **HTTP:** `GET /boxofficemojo/date/domestic`
- **What:** Box Office Mojo domestic daily box office. Returns normalized rows from Box Office Mojo's public domestic daily chart. Empty upstream daily pages return a typed not-found error rather than an empty success.
- **Params:** `date` (string, **required**) — Domestic box office date in YYYY-MM-DD format

### `boxofficemojo_franchise`

- **HTTP:** `GET /boxofficemojo/franchise`
- **What:** Box Office Mojo franchise detail. Returns normalized release rows from a public Box Office Mojo franchise page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo franchise id; `offset` (integer, optional) — Row offset for pagination (page size 100); `path` (string, optional) — Box Office Mojo franchise path; `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction; `url` (string, optional) — Absolute https://www.boxofficemojo.com franchise URL

### `boxofficemojo_franchises`

- **HTTP:** `GET /boxofficemojo/franchises`
- **What:** Box Office Mojo franchise chart. Returns normalized rows from Box Office Mojo's public franchise chart.
- **Params:** `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction

### `boxofficemojo_genre`

- **HTTP:** `GET /boxofficemojo/genre`
- **What:** Box Office Mojo genre detail. Returns normalized release rows from a public Box Office Mojo genre page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo genre id; `offset` (integer, optional) — Row offset for pagination (page size 100); `path` (string, optional) — Box Office Mojo genre path; `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction; `url` (string, optional) — Absolute https://www.boxofficemojo.com genre URL

### `boxofficemojo_genres`

- **HTTP:** `GET /boxofficemojo/genres`
- **What:** Box Office Mojo genre chart. Returns normalized rows from Box Office Mojo's public genre chart.
- **Params:** `sort` (string, optional) — Sort field; `sortDir` (string, optional) — Sort direction

### `boxofficemojo_lifetime_grosses`

- **HTTP:** `GET /boxofficemojo/lifetime-grosses`
- **What:** Box Office Mojo lifetime gross chart. Returns normalized rows from Box Office Mojo's credential-free lifetime gross chart. `area` values: `worldwide`, `domestic`.
- **Params:** `area` (string, optional) — Chart area. Allowed values: worldwide, domestic; `offset` (integer, optional) — Chart page offset. Allowed values: 0, 200, 400, 600, 800

### `boxofficemojo_release`

- **HTTP:** `GET /boxofficemojo/release`
- **What:** Box Office Mojo release detail. Returns normalized Box Office Mojo release summary fields and domestic daily rows from a public release page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo release id; `path` (string, optional) — Box Office Mojo release path; `url` (string, optional) — Absolute https://www.boxofficemojo.com release URL

### `boxofficemojo_release_group`

- **HTTP:** `GET /boxofficemojo/release-group`
- **What:** Box Office Mojo release group detail. Returns normalized market release rows grouped by region from a public Box Office Mojo release-group page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo release-group id; `path` (string, optional) — Box Office Mojo release-group path; `url` (string, optional) — Absolute https://www.boxofficemojo.com release-group URL

### `boxofficemojo_showdown`

- **HTTP:** `GET /boxofficemojo/showdown`
- **What:** Box Office Mojo showdown detail. Returns normalized release comparison metrics from a public Box Office Mojo showdown page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo showdown id; `path` (string, optional) — Box Office Mojo showdown path; `url` (string, optional) — Absolute https://www.boxofficemojo.com showdown URL

### `boxofficemojo_showdowns`

- **HTTP:** `GET /boxofficemojo/showdowns`
- **What:** Box Office Mojo showdowns. Returns normalized comparison rows from Box Office Mojo's public showdowns page.
- **Params:** _none_

### `boxofficemojo_title`

- **HTTP:** `GET /boxofficemojo/title`
- **What:** Box Office Mojo title detail. Returns normalized Box Office Mojo title release-group and market-gross tables from a public title page. Pass exactly one of `id`, `path`, or `url`.
- **Params:** `id` (string, optional) — Box Office Mojo title id; `path` (string, optional) — Box Office Mojo title path; `url` (string, optional) — Absolute https://www.boxofficemojo.com title URL

### `boxofficemojo_weekend_domestic`

- **HTTP:** `GET /boxofficemojo/weekend/domestic`
- **What:** Box Office Mojo domestic weekend box office. Returns normalized rows from Box Office Mojo's public domestic weekend chart. Empty upstream weekend pages return a typed not-found error rather than an empty success.
- **Params:** `week` (integer, **required**) — Weekend number, 1 through 53; `year` (integer, **required**) — Domestic weekend year, from 1982 through 2100

### `boxofficemojo_weekend_domestic_by_distributor`

- **HTTP:** `GET /boxofficemojo/weekend/domestic/by-distributor`
- **What:** Box Office Mojo domestic weekend by distributor. Returns normalized distributor rows from Box Office Mojo's public domestic weekend by-distributor chart. Empty upstream weekend pages return a typed not-found error rather than an empty success.
- **Params:** `week` (integer, **required**) — Weekend number, 1 through 53; `year` (integer, **required**) — Domestic weekend year, from 1982 through 2100

### `boxofficemojo_weekend_domestic_estimates`

- **HTTP:** `GET /boxofficemojo/weekend/domestic/estimates`
- **What:** Box Office Mojo domestic weekend estimates. Returns normalized estimate-vs-actual rows from Box Office Mojo's public domestic weekend estimates chart. Empty upstream weekend pages return a typed not-found error rather than an empty success.
- **Params:** `week` (integer, **required**) — Weekend number, 1 through 53; `year` (integer, **required**) — Domestic weekend year, from 1982 through 2100

### `boxofficemojo_year_domestic`

- **HTTP:** `GET /boxofficemojo/year/domestic`
- **What:** Box Office Mojo domestic yearly box office. Returns normalized release rows from Box Office Mojo's public domestic yearly calendar-grosses chart.
- **Params:** `year` (integer, **required**) — Domestic box office year, from 1977 through 2100

### `boxofficemojo_year_worldwide`

- **HTTP:** `GET /boxofficemojo/year/worldwide`
- **What:** Box Office Mojo worldwide yearly box office. Returns normalized release-group rows from Box Office Mojo's public worldwide yearly chart.
- **Params:** `year` (integer, **required**) — Box office year, from 1977 through 2100

## Brand (1)

### `brand_retrieve`

- **HTTP:** `GET /brand/retrieve`
- **What:** Retrieve brand data by domain. Fetches a domain's homepage and Web App Manifest and extracts a normalized brand profile (title, description, brand colors normalized to hex, logos and icons ranked best-first, backdrops, socials, links, and any schema.org organization data). Enrichment-only fields that are not present in the page markup are returned as null.
- **Params:** `domain` (string, **required**) — Domain to retrieve brand data for, e.g. context.dev; `force_language` (string, optional) — Accepted for compatibility; not applied in HTML-only mode; `maxAgeMs` (integer, optional) — Cache freshness window in milliseconds, clamps to 1 day..1 year; `maxSpeed` (boolean, optional) — Optimize for speed by skipping schema.org and footer-link extraction; `timeoutMS` (integer, optional) — Upstream fetch timeout in milliseconds, clamps to 1000..300000

## Brave (5)

### `brave_images`

- **HTTP:** `GET /brave/images`
- **What:** Search Brave image results. Returns normalized Brave image search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Brave Search image HTML and return 503 when Brave serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results to return; defaults to 10, clamped to 1..50; `country` (string, optional) — Brave result country; defaults to us; `lang` (string, optional) — Brave UI language; defaults to en-us; `offset` (integer, optional) — Zero-based Brave result page; defaults to 0; `q` (string, **required**) — Search query

### `brave_news`

- **HTTP:** `GET /brave/news`
- **What:** Search Brave news results. Returns normalized Brave news search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Brave Search news HTML and return 503 when Brave serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results to return; defaults to 10, clamped to 1..50; `country` (string, optional) — Brave result country; defaults to us; `date_from` (string, optional) — Custom start date in YYYY-MM-DD; requires date_to; `date_to` (string, optional) — Custom end date in YYYY-MM-DD; requires date_from; `lang` (string, optional) — Brave UI language; defaults to en-us; `offset` (integer, optional) — Zero-based Brave result page; defaults to 0; `q` (string, **required**) — Search query; `time_range` (string, optional) — Preset time filter: any, day, week, month, year, or custom

### `brave_search`

- **HTTP:** `GET /brave/search`
- **What:** Search Brave. Returns normalized web search results from Brave Search for a query string, along with offset-based pagination, related queries, discussions, videos, and the right-side knowledge card when Brave includes one. Use time_range for preset ranges or date_from/date_to for a custom YYYY-MM-DD range. Locale defaults to country=us and lang=en-us.
- **Params:** `country` (string, optional) — Brave result country; defaults to us; `date_from` (string, optional) — Custom start date in YYYY-MM-DD; requires date_to; `date_to` (string, optional) — Custom end date in YYYY-MM-DD; requires date_from; `lang` (string, optional) — Brave UI language; defaults to en-us; `offset` (integer, optional) — Zero-based Brave result page; `q` (string, **required**) — Search query; `time_range` (string, optional) — Preset time filter: any, day, week, month, year, or custom

### `brave_suggest`

- **HTTP:** `GET /brave/suggest`
- **What:** Suggest Brave search queries. Returns Brave autosuggest query completions for a query prefix. Locale defaults to country=us and lang=en-us. Suggestions are fetched from public Brave Search suggest JSON and trimmed to the requested count.
- **Params:** `count` (integer, optional) — Suggestions to return; defaults to 10, clamped to 1..12; `country` (string, optional) — Brave result country; defaults to us; `lang` (string, optional) — Brave UI language; defaults to en-us; `q` (string, **required**) — Search query prefix

### `brave_videos`

- **HTTP:** `GET /brave/videos`
- **What:** Search Brave video results. Returns normalized Brave video search results for a query string. Locale defaults to country=us and lang=en-us. Results are fetched from public Brave Search video HTML and return 503 when Brave serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results to return; defaults to 10, clamped to 1..50; `country` (string, optional) — Brave result country; defaults to us; `date_from` (string, optional) — Custom start date in YYYY-MM-DD; requires date_to; `date_to` (string, optional) — Custom end date in YYYY-MM-DD; requires date_from; `lang` (string, optional) — Brave UI language; defaults to en-us; `offset` (integer, optional) — Zero-based Brave result page; defaults to 0; `q` (string, **required**) — Search query; `time_range` (string, optional) — Preset time filter: any, day, week, month, year, or custom

## Capterra (3)

### `capterra_product`

- **HTTP:** `GET /capterra/product`
- **What:** Get a Capterra product. Returns a normalized Capterra product profile: name, description, category, and aggregate rating. Credential-free public Capterra data, rendered from the product page through proxied browser renderers.
- **Params:** `product_id` (string, **required**) — Capterra product id (the numeric id in a /p/{id}/{slug}/ URL)

### `capterra_reviews`

- **HTTP:** `GET /capterra/product/reviews`
- **What:** Get Capterra product reviews. Returns a page of normalized Capterra reviews (author, headline, rating) plus the product's aggregate rating. Credential-free public Capterra data, rendered from the reviews page through proxied browser renderers.
- **Params:** `page` (integer, optional) — Page number (default 1); `product_id` (string, **required**) — Capterra product id (the numeric id in a /p/{id}/{slug}/ URL)

### `capterra_search`

- **HTTP:** `GET /capterra/search`
- **What:** Search Capterra products. Returns Capterra search-result products (id, name, url, description, rating). Credential-free public Capterra data, rendered from the search page through proxied browser renderers. Note: Capterra renders a fallback product list even for queries with no genuine match, rather than a distinct empty-results page, so callers should treat low-relevance results as an upstream characteristic, not a bug.
- **Params:** `q` (string, **required**) — Search query

## CarMax (7)

### `carmax_search`

- **HTTP:** `GET /carmax/search`
- **What:** Search CarMax vehicle listings. Searches CarMax for used car listings, returning normalized vehicle summaries (make, model, trim, year, mileage, colors, engine, fuel economy, pricing, store, images), available search facets with live counts, and the total matching count. Credential-free public data sourced from CarMax's own mobile-app search API.
- **Params:** `make` (string, optional) — CarMax make, e.g. honda, Toyota, BMW (case-insensitive); `max_mileage` (integer, optional) — Maximum odometer mileage; `max_price` (integer, optional) — Maximum price in US dollars; `max_year` (integer, optional) — Maximum model year; `min_price` (integer, optional) — Minimum price in US dollars; `min_year` (integer, optional) — Minimum model year; `model` (string, optional) — CarMax model, e.g. civic (case-insensitive). Does not require make; `page` (integer, optional) — 1-indexed result page, defaults to 1. CarMax returns 48 results per page; `sort` (string, optional) — Sort order: bestmatch, distance-asc, price-asc, price-desc, mileage-asc, mileage-desc, year-desc, year-asc, newarrival. Defaults to bestmatch; `zip` (string, optional) — 5-digit US ZIP code to bias results toward CarMax's nearest store

### `carmax_search_suggestions`

- **HTTP:** `GET /carmax/search/suggestions`
- **What:** Get CarMax search autocomplete suggestions. Returns autocomplete suggestions for a partial search term (make/model/trim), typo-tolerant by default. Credential-free public data sourced from CarMax's own mobile-app API.
- **Params:** `exact_match` (boolean, optional) — Disable fuzzy/typo-tolerant matching -- require an exact prefix match. Defaults to false; `search` (string, **required**) — Free-text partial search term to get autocomplete suggestions for

### `carmax_shop_by_brand`

- **HTTP:** `GET /carmax/shop-by-brand`
- **What:** Get CarMax's "shop by brand" make taxonomy. Returns CarMax's full make taxonomy for browsing by brand: every make, a display image, and CarMax's own display order. Credential-free public data sourced from CarMax's own mobile-app API.
- **Params:** _none_

### `carmax_store`

- **HTTP:** `GET /carmax/store/{id}`
- **What:** Get CarMax store (physical location) detail. Returns a normalized CarMax store: name, full address, phone numbers, coordinates, opening hours, and store-type flags (car buying center, microstore). Credential-free public data sourced from CarMax's own server-rendered store page.
- **Params:** `id` (string, **required**) — CarMax store id, the numeric path segment of a /stores/{id} URL

### `carmax_stores`

- **HTTP:** `GET /carmax/stores`
- **What:** Search CarMax store (physical location) locations. Searches CarMax's physical store locations by ZIP code or free-text keyword, returning normalized stores with full address, every published phone number, opening hours, and (for a ZIP-based search) live driving distance in miles. Credential-free public data sourced from CarMax's own mobile-app store-locator API.
- **Params:** `keyword` (string, optional) — Free-text match against store name or city; `take` (integer, optional) — Maximum number of stores to return, defaults to 10, capped at 300; `zip` (string, optional) — 5-digit US ZIP code to search near. Triggers a live geo-distance sort. Provide this or keyword; zip takes precedence if both are given

### `carmax_vehicle`

- **HTTP:** `GET /carmax/vehicle/{stock_number}`
- **What:** Get CarMax vehicle listing detail. Returns a normalized CarMax vehicle listing: full vehicle spec (make, model, trim, mileage, colors, engine, transmission, fuel economy, pricing), equipment features, labeled specifications, warranty coverage, accident/owner history, and CarMax's return guarantee terms. Credential-free public data sourced primarily from CarMax's own mobile-app API, backfilled with the website's server-rendered page for accident/owner history and warranty terms the mobile API doesn't expose.
- **Params:** `stock_number` (string, **required**) — CarMax stock number, the numeric path segment of a /car/{stock_number} URL; `store_id` (string, optional) — Optional CarMax store id for pricing/transfer-fee display context. Defaults to a fixed CarMax store when omitted

### `carmax_vehicle_recommendations`

- **HTTP:** `GET /carmax/vehicle/{stock_number}/recommendations`
- **What:** Get CarMax "similar vehicles" recommendations for a listing. Returns CarMax's own similar-vehicle recommendations for a listing: stock number, description, display mileage/price, store location, and image, for vehicles CarMax considers comparable. An empty list is a normal result, not an error. Credential-free public data sourced from CarMax's own mobile-app API.
- **Params:** `stock_number` (string, **required**) — CarMax stock number to find similar vehicles for, the numeric path segment of a /car/{stock_number} URL; `store_id` (string, **required**) — CarMax store id used as the recommendation's location context. See any search/vehicle/store response's store id field

## Cars.com (2)

### `carsdotcom_search`

- **HTTP:** `GET /carsdotcom/search`
- **What:** Search Cars.com vehicle listings. Searches Cars.com for new and used car listings, returning normalized vehicle summaries (make, model, trim, year, mileage, exterior color, drivetrain, fuel type, pricing, seller, images) plus the total matching count. Credential-free public data sourced directly from Cars.com's own public search API.
- **Params:** `page` (integer, optional) — 1-indexed result page, defaults to 1. Cars.com returns 24 results per page; `radius` (integer, optional) — Search radius in miles around zip; `stock_type` (string, optional) — Listing condition. Allowed values: new, used, cpo, all; `zip` (string, optional) — 5-digit US ZIP code to search around

### `carsdotcom_vehicle`

- **HTTP:** `GET /carsdotcom/vehicle/{listing_id}`
- **What:** Get Cars.com vehicle listing detail. Returns a normalized Cars.com vehicle listing: full vehicle spec (make, model, trim, mileage, colors, engine, transmission, fuel economy, a key-specs table), Cars.com's own deal-fairness rating and predicted fair price, categorized equipment features, an AutoCheck-derived vehicle history report, Cars.com's own price-change history, the seller's notes, dealer detail (name, rating, address, website, phones, hours) or private-seller detail for a for-sale-by-owner listing, and certified-pre-owned/manufacturer-program detail when applicable. Credential-free public data sourced directly from Cars.com's own public GraphQL API.
- **Params:** `listing_id` (string, **required**) — Cars.com listing id (a UUID), the path segment of a /vehicledetail/{listing_id}/ URL

## ChromeWebStore (12)

### `chromewebstore_categories`

- **HTTP:** `GET /chromewebstore/categories`
- **What:** List Chrome Web Store categories and collections. Returns the reference taxonomy for the list endpoints: extension category groups and their subcategory slugs, the top-chart identifiers, and known curated collection slugs.
- **Params:** _none_

### `chromewebstore_category`

- **HTTP:** `GET /chromewebstore/category`
- **What:** List items in a Chrome Web Store category. Returns the item cards listed under an extensions category slug (e.g. `productivity/tools`, `lifestyle/shopping`, `make_chrome_yours/privacy`). Use /chromewebstore/categories for the reference taxonomy. Defaults: `num=50`, `country=us`, `lang=en`.
- **Params:** `category` (string, **required**) — Category slug under extensions; `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of items

### `chromewebstore_charts`

- **HTTP:** `GET /chromewebstore/charts`
- **What:** List a Chrome Web Store top chart. Returns the item cards in a store top chart. `chart` accepts `trending`, `popular`, or `notable`. Defaults: `chart=popular`, `num=50`, `country=us`, `lang=en`.
- **Params:** `chart` (string, optional) — Top chart to list; `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of items

### `chromewebstore_collection`

- **HTTP:** `GET /chromewebstore/collection`
- **What:** List items in a curated Chrome Web Store collection. Returns the item cards in a curated store collection slug (e.g. `editors_picks_extensions`, `dark_mode`, `ai_productivity`). Use /chromewebstore/categories for known collection slugs. Defaults: `num=50`, `country=us`, `lang=en`.
- **Params:** `collection` (string, **required**) — Curated collection slug; `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of items

### `chromewebstore_developer`

- **HTTP:** `GET /chromewebstore/developer`
- **What:** Retrieve a Chrome Web Store publisher and their items. Returns a Chrome Web Store publisher (developer) by publisher id, including the disclosed trader details — legal name, email, phone, address, website, and D-U-N-S number — plus the publisher's listed items ("More from ..."). Trader fields are only present for publishers that identify as EU traders. Defaults: `num=50`, `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store publisher id (u + 32 hex chars); `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of items

### `chromewebstore_item`

- **HTTP:** `GET /chromewebstore/item`
- **What:** Retrieve Chrome Web Store item details. Returns normalized detail for a Chrome Web Store extension or theme, including name, rating, rating count, user count, version, last-updated date, size, supported languages, developer, category, screenshots, and privacy links. Defaults: `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store item id (32-character extension/theme id); `lang` (string, optional) — Two-letter language code

### `chromewebstore_permissions`

- **HTTP:** `GET /chromewebstore/permissions`
- **What:** Retrieve a Chrome Web Store item's declared permissions. Returns the permissions a Chrome Web Store extension declares in its manifest: `permissions`, `optional_permissions`, `host_permissions`, `optional_host_permissions`, plus `manifest_version` and `min_browser_version`. Useful for security and supply-chain review. Defaults: `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store item id (32-character extension id); `lang` (string, optional) — Two-letter language code

### `chromewebstore_privacy`

- **HTTP:** `GET /chromewebstore/privacy`
- **What:** Retrieve a Chrome Web Store item's privacy disclosures. Returns an extension's privacy disclosures as the store renders them: the developer's data-use statement, whether it collects data, the standard data-handling declarations, and the privacy-policy link. Defaults: `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store item id (32-character extension/theme id); `lang` (string, optional) — Two-letter language code

### `chromewebstore_reviews`

- **HTTP:** `GET /chromewebstore/reviews`
- **What:** Retrieve Chrome Web Store item reviews. Returns the reviews the store renders on an item's reviews page, each with author, star rating, text, posted/edited dates and reviewed version. Defaults: `num=20`, `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store item id (32-character extension/theme id); `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of reviews; `sort` (string, optional) — Review sort order

### `chromewebstore_search`

- **HTTP:** `GET /chromewebstore/search`
- **What:** Search Chrome Web Store items. Returns Chrome Web Store search result cards for a keyword, each with id, name, rating, user count, publisher and detail URL. Defaults: `num=30`, `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of results; `term` (string, **required**) — Search keyword

### `chromewebstore_similar`

- **HTTP:** `GET /chromewebstore/similar`
- **What:** Retrieve related Chrome Web Store items. Returns the related-items shelf the store renders on an item's detail page. Defaults: `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `id` (string, **required**) — Chrome Web Store item id (32-character extension/theme id); `lang` (string, optional) — Two-letter language code

### `chromewebstore_suggest`

- **HTTP:** `GET /chromewebstore/suggest`
- **What:** Suggest Chrome Web Store search terms. Returns item-name suggestions for a search prefix, drawn from the top store-search results. Defaults: `num=8`, `country=us`, `lang=en`.
- **Params:** `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Maximum number of suggestions; `term` (string, **required**) — Search prefix to autocomplete

## CoinGecko (21)

### `coingecko_categories`

- **HTTP:** `GET /coingecko/categories`
- **What:** CoinGecko categories. Returns normalized CoinGecko category rows from the public categories page. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_category_coins`

- **HTTP:** `GET /coingecko/category/{slug}/coins`
- **What:** CoinGecko category coins. Returns normalized coin rows from a CoinGecko public category page. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `slug` (string, **required**) — CoinGecko category slug such as stablecoins; `vs_currency` (string, optional) — Quote currency

### `coingecko_chain`

- **HTTP:** `GET /coingecko/chains/{id}`
- **What:** CoinGecko chain detail. Returns normalized sections from a CoinGecko public chain detail page. Sections are omitted when not present. This endpoint supports the documented `vs_currency` enum.
- **Params:** `id` (string, **required**) — CoinGecko chain id such as ethereum; `limit` (integer, optional) — Rows per section to return, default 20, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_chains`

- **HTTP:** `GET /coingecko/chains`
- **What:** CoinGecko chains. Returns normalized chain rows from the CoinGecko public website chains table. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_coin`

- **HTTP:** `GET /coingecko/coin/{id}`
- **What:** CoinGecko coin profile. Returns normalized CoinGecko profile, market stats, links, and categories for one coin id. This endpoint supports the documented `vs_currency` enum and is not intended for real-time trading.
- **Params:** `id` (string, **required**) — CoinGecko coin id such as bitcoin; `vs_currency` (string, optional) — Quote currency

### `coingecko_coin_analysis`

- **HTTP:** `GET /coingecko/coin/{id}/analysis`
- **What:** CoinGecko coin chart analysis. Returns derived price-chart metrics from CoinGecko public chart JSON. This endpoint supports the documented `vs_currency` enum and is not investment advice or real-time trading data.
- **Params:** `id` (string, **required**) — CoinGecko coin id such as bitcoin; `include_annotations` (boolean, optional) — Fetch optional CoinGecko chart annotations; `range` (string, optional) — Chart range; `vs_currency` (string, optional) — Quote currency

### `coingecko_exchange`

- **HTTP:** `GET /coingecko/exchange/{id}`
- **What:** CoinGecko exchange detail. Returns normalized profile stats and market rows from a CoinGecko public exchange page. This endpoint supports the documented `vs_currency` enum.
- **Params:** `id` (string, **required**) — CoinGecko exchange id such as binance; `limit` (integer, optional) — Rows to return, default 100, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_exchanges`

- **HTTP:** `GET /coingecko/exchanges`
- **What:** CoinGecko exchanges. Returns normalized exchange rows from CoinGecko public website exchange tables. This endpoint supports the documented `vs_currency` enum.
- **Params:** `kind` (string, optional) — Exchange table kind, default spot; `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `vs_currency` (string, optional) — Quote currency

### `coingecko_gainers_losers`

- **HTTP:** `GET /coingecko/gainers-losers`
- **What:** CoinGecko crypto gainers and losers. Returns normalized rows from CoinGecko's public crypto gainers and losers table. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows per section to return, default 20, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_global`

- **HTTP:** `GET /coingecko/global`
- **What:** CoinGecko global market snapshot. Returns normalized global market metrics from CoinGecko's public charts page.
- **Params:** _none_

### `coingecko_global_charts`

- **HTTP:** `GET /coingecko/global/charts`
- **What:** CoinGecko global chart series. Returns normalized global chart series from public CoinGecko website JSON endpoints.
- **Params:** `kind` (string, optional) — Chart kind, default total_market_cap; `limit` (integer, optional) — Rows per series to return, default 120, max 500; `range` (string, optional) — Chart range, default 90d

### `coingecko_learn_articles`

- **HTTP:** `GET /coingecko/learn/articles`
- **What:** CoinGecko Learn articles. Returns normalized article cards from CoinGecko Learn public pages.
- **Params:** `category` (string, optional) — Learn category, default all; `limit` (integer, optional) — Rows to return, default 20, max 50

### `coingecko_markets`

- **HTTP:** `GET /coingecko/markets`
- **What:** CoinGecko markets. Returns normalized cryptocurrency market rows from CoinGecko public pages. This endpoint supports the documented `vs_currency` enum and is not intended for real-time trading.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `vs_currency` (string, optional) — Quote currency

### `coingecko_new_coins`

- **HTTP:** `GET /coingecko/new-coins`
- **What:** CoinGecko new cryptocurrencies. Returns normalized rows from CoinGecko's public new cryptocurrencies table. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `vs_currency` (string, optional) — Quote currency

### `coingecko_news`

- **HTTP:** `GET /coingecko/news`
- **What:** CoinGecko news cards. Returns normalized article cards from CoinGecko's public news page.
- **Params:** `limit` (integer, optional) — Rows to return, default 20, max 50

### `coingecko_nft_category`

- **HTTP:** `GET /coingecko/nft/category/{slug}`
- **What:** CoinGecko NFT category. Returns normalized NFT collection rows from a CoinGecko public NFT category page. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `slug` (string, **required**) — CoinGecko NFT category slug such as metaverse; `vs_currency` (string, optional) — Quote currency

### `coingecko_nfts`

- **HTTP:** `GET /coingecko/nfts`
- **What:** CoinGecko NFT collections. Returns normalized NFT collection rows from the CoinGecko public website NFT table. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100; `page` (integer, optional) — Page number, default 1; `vs_currency` (string, optional) — Quote currency

### `coingecko_search`

- **HTTP:** `GET /coingecko/search`
- **What:** CoinGecko discovery search. Returns normalized CoinGecko search sections from the public website search JSON. Empty valid searches return empty arrays.
- **Params:** `limit` (integer, optional) — Rows per section to return, default 10, max 50; `q` (string, **required**) — Search query

### `coingecko_token_unlocks`

- **HTTP:** `GET /coingecko/token-unlocks`
- **What:** CoinGecko incoming token unlocks. Returns normalized rows from CoinGecko's public incoming token unlocks page.
- **Params:** `limit` (integer, optional) — Rows to return, default 100, max 100

### `coingecko_treasuries`

- **HTTP:** `GET /coingecko/treasuries`
- **What:** CoinGecko crypto treasuries. Returns normalized entity rows from CoinGecko's public crypto treasuries tables. This endpoint supports the documented `vs_currency` enum.
- **Params:** `asset` (string, optional) — Treasury asset filter, default all; `holder_type` (string, optional) — Treasury holder type filter, default all; `limit` (integer, optional) — Rows to return, default 100, max 100; `vs_currency` (string, optional) — Quote currency

### `coingecko_trending`

- **HTTP:** `GET /coingecko/trending`
- **What:** CoinGecko trending highlights. Returns deduped trending coins and categories from the public CoinGecko highlights page. This endpoint supports the documented `vs_currency` enum.
- **Params:** `limit` (integer, optional) — Rows per section to return, default 20, max 50; `vs_currency` (string, optional) — Quote currency

## Congress (2)

### `congress_report`

- **HTTP:** `GET /congress/report`
- **What:** Fetch and parse a congressional disclosure report. Fetch a single disclosure report by its filing_url (as returned by.
- **Params:** `url` (string, **required**) — Filing URL, as returned by congress-stock-disclosures' filing_url field. Must be an efdsearch.senate.gov /search/view/annual/..., /search/view/ptr/..., or /search/view/extension-notice/regular/... URL.

### `congress_stock_disclosures`

- **HTTP:** `GET /congress/stock-disclosures`
- **What:** Search congressional stock-disclosure filings. Search public congressional stock disclosure filings (House or Senate).
- **Params:** `chamber` (string, optional) — Chamber filter. Allowed values: house, senate.; `district` (string, optional) — House district filter (House only).; `election_year` (string, optional) — House candidate-search election year filter (requires filer_type=candidate).; `filer_type` (string, optional) — Filer-type filter, meaning differs by chamber. House: single value selecting between the site's two separate search forms -- member (default, Search Members) or candidate (Search Candidates; results[].filing_year holds election year instead of a filing year). Senate: comma-separated multi-select -- senator, candidate, former_senator. Defaults to senator when omitted.; `from` (string, optional) — Minimum filing year (YYYY).; `limit` (integer, optional) — Max results (1-500).; `member` (string, optional) — Chamber member name (required when ticker is omitted).; `report_type` (string, optional) — Comma-separated Senate report-type filter (Senate only). Allowed values: annual, periodic_transaction, due_date_extension, blind_trust, other. Defaults to all types when omitted.; `sort` (string, optional) — Sort key. Allowed values: name_asc, name_desc, office_asc, office_desc, filing_year_asc, filing_year_desc.; `state` (string, optional) — Member state filter (2-letter code).; `ticker` (string, optional) — Ticker symbol filter. Not supported by House or Senate sources.; `to` (string, optional) — Maximum filing year (YYYY).

## Costco (6)

### `costco_categories`

- **HTTP:** `GET /costco/categories`
- **What:** Get Costco category facets. Returns Costco category slugs and product counts relevant to an optional search term, each slug usable directly with GET /costco/search's category filter. Public data sourced from Costco's own search backend.
- **Params:** `query` (string, optional) — Search text to scope the returned categories to, e.g. \

### `costco_product`

- **HTTP:** `GET /costco/product/{id}`
- **What:** Get a Costco product's detail. Returns a Costco product's detail: title, description, manufacturer, image, price, stock status, and rating. Public data sourced from Costco's own product backend.
- **Params:** `id` (string, **required**) — Costco product id, e.g. from a search result's id field or a product page URL's \

### `costco_product_availability`

- **HTTP:** `GET /costco/product/{id}/availability`
- **What:** Get a Costco product's delivery estimate. Returns a Costco product's stock and estimated-delivery status for a delivery destination. Public data sourced from Costco's own fulfillment backend.
- **Params:** `id` (string, **required**) — Costco product id; `postal_code` (string, **required**) — US destination ZIP code; `state` (string, **required**) — US destination two-letter state code

### `costco_product_reviews`

- **HTTP:** `GET /costco/product/{id}/reviews`
- **What:** Get a Costco product's reviews. Returns a page of a Costco product's reviews: title, text, rating, author, and recommendation for each. Public data sourced from Costco's own review platform.
- **Params:** `id` (string, **required**) — Costco product id, e.g. from a search result's id field

### `costco_search`

- **HTTP:** `GET /costco/search`
- **What:** Search Costco products. Returns public Costco products matching a text query and/or a category slug: title, brand, model, image, and rating for each result. Public data sourced from Costco's own search backend.
- **Params:** `category` (string, optional) — Costco category slug, e.g. the last path segment of a category page URL; `query` (string, optional) — Search text

### `costco_warehouses`

- **HTTP:** `GET /costco/warehouses`
- **What:** Find nearby Costco warehouses. Returns Costco warehouses near a latitude/longitude, sorted by distance: name, address, and distance for each. Public data sourced from Costco's own warehouse locator backend.
- **Params:** `latitude` (number, **required**) — Latitude; `longitude` (number, **required**) — Longitude

## Datasets (109)

### `datasets_airbnb_facets`

- **HTTP:** `GET /datasets/airbnb-markets/facets`
- **What:** Facet the Airbnb markets dataset. Returns suppressed distribution counts over the Airbnb markets dataset, honoring the same filters as search. Facet enum: `country`, `market`, `currency`, `superhost`, `guest_favorite`, `rating_band`, `review_band`, `admin1` (top subdivision), `locality` (settlement), `room_type` (`entire_place`/`private_room`/`hotel`/`shared_room`), `property_type` (Airbnb's canonical listing type from the detail page), `amenities` (each amenity with the count of listings offering it). The `admin1`, `locality`, `room_type`, `property_type` and `amenities` facets stay empty until their enrichment coverage is high enough to be reliable. group_by enum: `country`, `market`, `admin1`, `locality`, `room_type`, `property_type`.
- **Params:** `active_since` (string, optional) — Freshness filter, an ISO-8601 date (YYYY-MM-DD); `country` (string, optional) — Exact ISO-3166-1 alpha-2 country filter, e.g. FR; `facet` (string, **required**) — Facet enum: country, market, currency, superhost, guest_favorite, rating_band, review_band, admin1, locality, room_type, property_type, amenities; `group_by` (string, optional) — Aggregate cell dimension enum: country, market, admin1, locality, room_type, property_type. Defaults to country; `guest_favorite` (boolean, optional) — Count only Guest Favorite listings (an observed lower bound; the badge under-counts); `market` (string, optional) — Exact metro-market filter, max 128 characters; `min_listings` (integer, optional) — Minimum listings per bucket; raises the small-cell suppression floor; `min_rating` (number, optional) — Minimum listing rating, from 0 through 5; `min_review_count` (integer, optional) — Minimum listing review count, 0 or greater; `superhost` (boolean, optional) — Count only Superhost listings

### `datasets_airbnb_item`

- **HTTP:** `GET /datasets/airbnb-markets/items/{country}`
- **What:** Get an Airbnb market from the dataset. Returns one country's full aggregate Airbnb market profile from dataset id enum value `airbnb-markets` — headline supply, Superhost share, Guest Favorite share (`guest_favorite_pct`, an observed lower bound), `avg_person_capacity` (average guests a listing sleeps over the detail-page-enriched sample), ratings, its top metros, bounding box, per-currency nightly-price percentiles, and a USD-normalized `price_usd` percentile block (converted via an approximate dated FX snapshot) for cross-country comparison. Aggregate-only. Returns 404 for a country below the suppression floor.
- **Params:** `country` (string, **required**) — ISO-3166-1 alpha-2 country code, e.g. FR

### `datasets_airbnb_nearby`

- **HTTP:** `GET /datasets/airbnb-markets/nearby`
- **What:** Airbnb market density near a coordinate. Returns an aggregate geohash-grid density map of Airbnb listings within a radius of a coordinate, from dataset id enum value `airbnb-markets`. Each cell reports a centroid, listing count and Superhost share; thin cells are suppressed. Aggregate-only.
- **Params:** `active_since` (string, optional) — Freshness filter, an ISO-8601 date (YYYY-MM-DD); `country` (string, optional) — Exact ISO-3166-1 alpha-2 country filter, e.g. US; `lat` (number, **required**) — Center latitude, from -90 through 90; `lon` (number, **required**) — Center longitude, from -180 through 180; `min_listings` (integer, optional) — Minimum listings per cell; raises the small-cell suppression floor; `min_rating` (number, optional) — Minimum listing rating, from 0 through 5; `precision` (integer, optional) — Geohash precision, from 1 through 12; defaults to a value derived from the radius; `radius_m` (integer, **required**) — Search radius in meters, from 1 through 50000; `superhost` (boolean, optional) — Count only Superhost listings

### `datasets_airbnb_search`

- **HTTP:** `GET /datasets/airbnb-markets/search`
- **What:** Search the Airbnb markets dataset. Returns aggregate Airbnb short-term-rental market rollups from the dataset id enum value `airbnb-markets`. Aggregate-only: each row is a market cell, never an individual listing. Thin cells are suppressed. group_by enum: `country`, `market`, `admin1` (top subdivision), `locality` (settlement), `room_type` (`entire_place`/`private_room`/`hotel`/`shared_room`), `property_type` (Airbnb's canonical listing type from the detail page). `admin1`, `locality`, `room_type` and `property_type` are enrichment-derived and stay empty until their coverage is high enough to be reliable. Each cell also carries `median_price_usd`, the median nightly price converted to USD via an approximate dated FX snapshot, for cross-country comparison (combine with `group_by=room_type` for median price by room type); `guest_favorite_pct`, the share of listings carrying the Guest Favorite badge (an observed lower bound, like `superhost_pct`); and `avg_person_capacity`, the average guests a listing sleeps over the detail-page-enriched sample. Sort enum: `listings_desc`, `superhost_pct_desc`, `rating_desc`, `key_asc`.
- **Params:** `active_since` (string, optional) — Freshness filter, an ISO-8601 date (YYYY-MM-DD); only listings last seen on or after it are counted; `country` (string, optional) — Exact ISO-3166-1 alpha-2 country filter, e.g. FR; `group_by` (string, optional) — Aggregate cell dimension enum: country, market, admin1, locality, room_type, property_type. Defaults to country; `guest_favorite` (boolean, optional) — Count only Guest Favorite listings (an observed lower bound; the badge under-counts); `market` (string, optional) — Exact metro-market filter, e.g. Paris, max 128 characters; `min_listings` (integer, optional) — Minimum listings per cell; raises the small-cell suppression floor (never lowered below the built-in minimum); `min_rating` (number, optional) — Minimum listing rating, from 0 through 5; `min_review_count` (integer, optional) — Minimum listing review count, 0 or greater; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `sort` (string, optional) — Sort enum: listings_desc, superhost_pct_desc, rating_desc, key_asc; `superhost` (boolean, optional) — Count only Superhost listings

### `datasets_apple_podcasts_shows_facets`

- **HTTP:** `GET /datasets/apple-podcasts-shows/facets`
- **What:** Facet Apple Podcasts shows dataset. Returns terms aggregation counts for the Apple Podcasts shows dataset. Facet enum: `genre`, `genre_id`, `country`, `content_advisory_rating`, `run_id`.
- **Params:** `country` (string, optional) — Exact storefront country filter, max 128 characters; `explicitness` (string, optional) — Exact explicitness filter, max 128 characters; `facet` (string, **required**) — Facet enum: genre, genre_id, country, content_advisory_rating, run_id; `genre` (string, optional) — Exact primary-genre filter, max 128 characters; `genre_id` (string, optional) — Exact Apple Podcasts genre id filter, max 128 characters; `min_track_count` (integer, optional) — Minimum episode count (track_count), 0 or greater; `q` (string, optional) — Full-text query over show title and artist name, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters

### `datasets_apple_podcasts_shows_item`

- **HTTP:** `GET /datasets/apple-podcasts-shows/items/{id}`
- **What:** Get an Apple Podcasts show from dataset. Returns one crawled Apple Podcasts show record by id from dataset id enum value `apple-podcasts-shows`.
- **Params:** `id` (string, **required**) — Apple Podcasts numeric show id (e.g. 173001861)

### `datasets_apple_podcasts_shows_search`

- **HTTP:** `GET /datasets/apple-podcasts-shows/search`
- **What:** Search Apple Podcasts shows dataset. Searches the crawled public Apple Podcasts show catalog stored in a search index. One row per show. Discovered from a country x genre x collection chart grid and a search-term sweep — not a full catalog of every Apple Podcasts show. Sort enum: `relevance`, `popularity`, `track_count_desc`, `release_desc`, `title_asc`.
- **Params:** `country` (string, optional) — Exact storefront country filter (the crawl's discovery storefront, e.g. us, gb), max 128 characters; `explicitness` (string, optional) — Exact explicitness filter as reported by Apple (e.g. explicit, cleaned), max 128 characters; `genre` (string, optional) — Exact primary-genre filter (e.g. Comedy, True Crime), max 128 characters; `genre_id` (string, optional) — Exact Apple Podcasts genre id filter (e.g. 1303 for Comedy), max 128 characters; `min_track_count` (integer, optional) — Minimum episode count (track_count), 0 or greater; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over show title and artist name, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `sort` (string, optional) — Sort enum: relevance, popularity, track_count_desc, release_desc, title_asc

### `datasets_apps_charts_search`

- **HTTP:** `GET /datasets/apps-charts/search`
- **What:** Search the app-charts dataset. Searches daily top-chart snapshots scraped from the iOS App Store and Google Play, stored in a search index (one document per chart × snapshot × rank). With no `date` the latest snapshot is returned (today's chart); pair `app_id` with `sort=date_desc` for an app's rank over time. Store enum: `ios`, `android`. Chart type enum: `top_free`, `top_paid`, `top_grossing`, `new`. Platform enum (Apple device platforms, ios charts only): `phone`, `pad`, `mac`. Sort enum: `rank`, `rank_desc`, `date_desc`.
- **Params:** `app_id` (string, optional) — Exact app filter — iOS numeric track id or Android package; pair with sort=date_desc for rank history; `category` (string, optional) — Store category/genre filter, max 128 characters; empty for the overall charts; `chart_type` (string, optional) — Chart enum: top_free, top_paid, top_grossing, new; `collection` (string, optional) — Raw store collection id filter (e.g. topgrossingapplications, GROSSING), max 128 characters; `country` (string, optional) — Exact storefront country filter, max 128 characters; `date` (string, optional) — Snapshot date filter yyyy-MM-dd; defaults to the latest snapshot; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `platform` (string, optional) — Apple device-platform filter, iOS charts only; see platform enum above; `q` (string, optional) — Full-text query over chart-entry title and developer, max 256 characters; `sort` (string, optional) — Sort enum: rank, rank_desc, date_desc; `store` (string, optional) — Store enum: ios, android

### `datasets_apps_reviews_search`

- **HTTP:** `GET /datasets/apps-reviews/search`
- **What:** Search the app-reviews dataset. Searches user reviews scraped from the iOS App Store and Google Play, stored in a search index (one document per review). Store enum: `ios`, `android`. Sort enum: `recent`, `score_desc`, `score_asc`, `helpful_desc`.
- **Params:** `app_id` (string, optional) — Exact app filter — iOS numeric track id or Android package, max 128 characters; `country` (string, optional) — Exact storefront country filter, max 128 characters; `min_score` (integer, optional) — Minimum star rating, 1 through 5; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over review text, title and author, max 256 characters; `sort` (string, optional) — Sort enum: recent, score_desc, score_asc, helpful_desc; `store` (string, optional) — Store enum: ios, android

### `datasets_apps_search`

- **HTTP:** `GET /datasets/apps/search`
- **What:** Search the apps-intelligence dataset. Searches resolved iOS App Store and Google Play apps stored in a search index. Store enum: `ios`, `android`, `both`. Platform enum (Apple device platforms, ios records only): `phone`, `pad`, `mac`, `tv`, `watch`, `vision`. Sort enum: `relevance`, `rating_desc`, `reviews_desc`, `installs_desc`, `updated_at_desc`, `popularity_desc`.
- **Params:** `category` (string, optional) — Exact app-store category filter, max 128 characters; `country` (string, optional) — Exact storefront country filter, max 128 characters; `developer` (string, optional) — Exact developer/publisher name filter, max 128 characters; `free` (boolean, optional) — Filter by price; true keeps only free apps, false only paid; `min_rating` (number, optional) — Minimum store rating, 0 through 5; `min_reviews` (integer, optional) — Minimum ratings/review count; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `platforms` (array, optional) — Repeatable Apple device-platform filter (OR); see platform enum above; `q` (string, optional) — Full-text query over title, developer and category, max 256 characters; `sort` (string, optional) — Sort enum: relevance, rating_desc, reviews_desc, installs_desc, updated_at_desc, popularity_desc; `store` (string, optional) — Store enum: ios, android, both

### `datasets_boxofficemojo_facets`

- **HTTP:** `GET /datasets/boxofficemojo/facets`
- **What:** Facet the Box Office Mojo dataset. Returns terms-aggregation counts for one facet of the Box Office Mojo dataset, scoped to the same filters as search. Facet enum: `gross_band`, `years_active`, `lifetime_year`, `franchise_names`, `brand_names`, `genre_names`, `hydrated`, `is_billion_dollar`, `in_lifetime_top_1000_ww`. gross_band enum: `under_50m`, `50_100m`, `100_250m`, `250_500m`, `500m_1b`, `over_1b`.
- **Params:** `brand` (string, optional) — Brand name filter, max 128 characters; `facet` (string, **required**) — Facet enum: gross_band, years_active, lifetime_year, franchise_names, brand_names, genre_names, hydrated, is_billion_dollar, in_lifetime_top_1000_ww; `franchise` (string, optional) — Franchise name filter, max 128 characters; `genre` (string, optional) — Genre name filter, max 128 characters; `gross_band` (string, optional) — Gross band filter; `hydrated` (boolean, optional) — Hydrated filter; `in_lifetime_top_1000` (boolean, optional) — Only titles in the lifetime worldwide top 1000 chart; `is_billion_dollar` (boolean, optional) — Only titles with worldwide gross of at least $1B; `lifetime_year` (integer, optional) — Primary lifetime chart year; `max_domestic_share` (number, optional) — Maximum domestic share of worldwide gross, 0 through 1; `max_worldwide` (integer, optional) — Maximum lifetime worldwide gross; `min_domestic` (integer, optional) — Minimum lifetime domestic gross; `min_foreign_share` (number, optional) — Minimum foreign share of worldwide gross, 0 through 1; `min_worldwide` (integer, optional) — Minimum lifetime worldwide gross; `q` (string, optional) — Full-text query, max 256 characters; `title_id` (string, optional) — Exact title id (IMDb tt… id used by Box Office Mojo), max 32 characters; `year` (integer, optional) — Year in years_active

### `datasets_boxofficemojo_item`

- **HTTP:** `GET /datasets/boxofficemojo/items/{title_id}`
- **What:** Get a Box Office Mojo title from the dataset. Returns one Box Office Mojo dataset record by title id (IMDb `tt…` id used on Box Office Mojo title pages), including lifetime grosses, year history, release groups and market grosses when hydrated.
- **Params:** `title_id` (string, **required**) — Title id (IMDb tt… id), e.g. tt0499549

### `datasets_boxofficemojo_search`

- **HTTP:** `GET /datasets/boxofficemojo/search`
- **What:** Search the Box Office Mojo dataset. Searches theatrical box-office records from public Box Office Mojo charts and title pages, stored in a search index. Filter by title id, year, franchise/brand/genre, gross band, lifetime top-1000 membership, hydration status, and worldwide/domestic gross ranges. Sort enum: `relevance`, `worldwide_desc`, `domestic_desc`, `peak_worldwide_desc`, `lifetime_rank_asc`, `year_desc`, `year_asc`. gross_band enum: `under_50m`, `50_100m`, `100_250m`, `250_500m`, `500m_1b`, `over_1b`.
- **Params:** `brand` (string, optional) — Brand name filter, max 128 characters; `franchise` (string, optional) — Franchise name filter, max 128 characters; `genre` (string, optional) — Genre name filter, max 128 characters; `gross_band` (string, optional) — Gross band enum: under_50m, 50_100m, 100_250m, 250_500m, 500m_1b, over_1b; `hydrated` (boolean, optional) — Only titles with hydrated release groups and market grosses; `in_lifetime_top_1000` (boolean, optional) — Only titles in the lifetime worldwide top 1000 chart; `is_billion_dollar` (boolean, optional) — Only titles with worldwide gross of at least $1B; `lifetime_year` (integer, optional) — Primary lifetime chart year; `max_domestic_share` (number, optional) — Maximum domestic share of worldwide gross, 0 through 1; `max_worldwide` (integer, optional) — Maximum lifetime worldwide gross in whole USD dollars; `min_domestic` (integer, optional) — Minimum lifetime domestic gross in whole USD dollars; `min_foreign_share` (number, optional) — Minimum foreign share of worldwide gross, 0 through 1; `min_worldwide` (integer, optional) — Minimum lifetime worldwide gross in whole USD dollars; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over title and taxonomy names, max 256 characters; `sort` (string, optional) — Sort enum: relevance, worldwide_desc, domestic_desc, peak_worldwide_desc, lifetime_rank_asc, year_desc, year_asc; `title_id` (string, optional) — Exact title id (IMDb tt… id used by Box Office Mojo), max 32 characters; `year` (integer, optional) — Year that must appear in years_active

### `datasets_chrome_extensions_changes`

- **HTTP:** `GET /datasets/chrome-extensions/changes`
- **What:** Get recent Chrome Web Store item changes. Returns recent change observations. Change type enum: `users`, `rating`, `rating_count`, `version`, `developer`, `permissions`, `privacy`, `status`.
- **Params:** `change_type` (string, optional) — Change type enum: users, rating, rating_count, version, developer, permissions, privacy, status; `limit` (integer, optional) — Maximum observations, default 100, max 500

### `datasets_chrome_extensions_facets`

- **HTTP:** `GET /datasets/chrome-extensions/facets`
- **What:** Facet the Chrome Web Store dataset. Returns aggregation buckets. Facet enum: `item_type`, `category`, `developer`, `developer_email`, `manifest_version`, `permission`, `status`, `collects_data`, `has_broad_host_access`. Item type enum: `extension`, `theme`, `app`, `unknown`. Search sort, status and manifest-version enums match the search endpoint.
- **Params:** `category` (string, optional) — Exact category; `collects_data` (boolean, optional) — Data-collection filter; `developer` (string, optional) — Exact developer; `developer_email` (string, optional) — Exact developer email; `facet` (string, **required**) — Facet enum: item_type, category, developer, developer_email, manifest_version, permission, status, collects_data, has_broad_host_access; `has_broad_host_access` (boolean, optional) — Broad-host-access filter; `item_type` (string, optional) — Item type enum: extension, theme, app, unknown; `manifest_version` (integer, optional) — Manifest version enum: 2, 3; `min_rating` (number, optional) — Minimum rating; `min_rating_count` (integer, optional) — Minimum rating count; `min_users` (integer, optional) — Minimum users; `permission` (string, optional) — Exact permission; `q` (string, optional) — Full-text query; `sort` (string, optional) — Sort enum: relevance, users_desc, rating_desc, reviews_desc, updated_desc, trending_desc; `status` (string, optional) — Status enum: active, removed

### `datasets_chrome_extensions_history`

- **HTTP:** `GET /datasets/chrome-extensions/history/{id}`
- **What:** Get Chrome Web Store item history. Returns chronological change-only observations for a Chrome Web Store item.
- **Params:** `from` (string, optional) — Inclusive start date, YYYY-MM-DD; `id` (string, **required**) — Chrome Web Store item id; `limit` (integer, optional) — Maximum points, default 365, max 1000; `to` (string, optional) — Inclusive end date, YYYY-MM-DD

### `datasets_chrome_extensions_item`

- **HTTP:** `GET /datasets/chrome-extensions/items/{id}`
- **What:** Get a Chrome Web Store dataset item. Returns one stored extension, theme or legacy app snapshot by its 32-character Chrome Web Store id.
- **Params:** `id` (string, **required**) — Chrome Web Store item id

### `datasets_chrome_extensions_metrics`

- **HTTP:** `GET /datasets/chrome-extensions/metrics`
- **What:** Get Chrome Web Store dataset metrics. Returns chart-ready coverage, adoption, rating, permission, privacy and recent-change aggregates for the stored Chrome Web Store dataset. Days enum: `7`, `30`, `90`.
- **Params:** `days` (integer, optional) — Recent-change window enum: 7, 30, 90; default 30; `limit` (integer, optional) — Top category and permission buckets, default 10, min 5, max 25

### `datasets_chrome_extensions_search`

- **HTTP:** `GET /datasets/chrome-extensions/search`
- **What:** Search the Chrome Web Store dataset. Searches stored Chrome Web Store item snapshots. Item type enum: `extension`, `theme`, `app`, `unknown`. Sort enum: `relevance`, `users_desc`, `rating_desc`, `reviews_desc`, `updated_desc`, `trending_desc`. Status enum: `active`, `removed`. Manifest version enum: `2`, `3`.
- **Params:** `category` (string, optional) — Exact Chrome Web Store category; `collects_data` (boolean, optional) — Filter by public data-collection disclosure; `developer` (string, optional) — Exact displayed developer name; `developer_email` (string, optional) — Exact disclosed developer email; `has_broad_host_access` (boolean, optional) — Filter by broad host access; `item_type` (string, optional) — Item type enum: extension, theme, app, unknown; `manifest_version` (integer, optional) — Manifest version enum: 2, 3; `min_rating` (number, optional) — Minimum rating, 0 through 5; `min_rating_count` (integer, optional) — Minimum rating count; `min_users` (integer, optional) — Minimum displayed user count; `page` (integer, optional) — Page number, default 1; `page_size` (integer, optional) — Page size, default 20, max 100; `permission` (string, optional) — Exact declared permission; `q` (string, optional) — Full-text query, max 256 characters; `sort` (string, optional) — Sort enum: relevance, users_desc, rating_desc, reviews_desc, updated_desc, trending_desc; `status` (string, optional) — Status enum: active, removed

### `datasets_chrome_extensions_trending`

- **HTTP:** `GET /datasets/chrome-extensions/trending`
- **What:** Get trending Chrome Web Store items. Returns stored Chrome Web Store items ranked by the latest observed user and rating-count movement. Filters match the search endpoint; sort is fixed to `trending_desc`.
- **Params:** `category` (string, optional) — Exact category; `collects_data` (boolean, optional) — Data-collection filter; `developer` (string, optional) — Exact developer; `developer_email` (string, optional) — Exact developer email; `has_broad_host_access` (boolean, optional) — Broad-host-access filter; `item_type` (string, optional) — Item type enum: extension, theme, app, unknown; `manifest_version` (integer, optional) — Manifest version enum: 2, 3; `min_rating` (number, optional) — Minimum rating; `min_rating_count` (integer, optional) — Minimum rating count; `min_users` (integer, optional) — Minimum users; `page` (integer, optional) — Page number; `page_size` (integer, optional) — Page size, max 100; `permission` (string, optional) — Exact permission; `q` (string, optional) — Full-text query; `status` (string, optional) — Status enum: active, removed

### `datasets_creators_search`

- **HTTP:** `GET /datasets/creators/search`
- **What:** Search the TikTok creators dataset. Searches TikTok creators stored in a search index (one document per creator), with follower counts, verified status, niche, and engagement. Deleted and private accounts are excluded by default; set `include_inactive=true` to include them for historical lookups. Sort enum: `followers_desc`, `engagement_desc`, `likes_desc`, `relevance`. Coverage note: `followers_desc`, `likes_desc`, and `relevance` are backed by profile fields present across the full dataset; the post-level engagement metrics (`engagement_rate`, `avg_views`, and the nested `post_stats` object) and the `engagement_desc` sort are currently populated for a growing subset of creators, prioritizing the highest-reach accounts. Creators without these metrics are still returned but sort last under `engagement_desc` and omit those fields.
- **Params:** `country` (string, optional) — Exact creator country/region filter, max 128 characters; `handle` (string, optional) — Exact handle lookup (case-insensitive), e.g. khaby.lame; returns the single creator with that exact @handle; `has_email` (boolean, optional) — Filter by contact-email presence; true keeps only creators with an email; `include_inactive` (boolean, optional) — Include deleted/private accounts; defaults to false (only live accounts returned); `min_followers` (integer, optional) — Minimum follower count; `niche` (string, optional) — Exact content-niche filter, max 128 characters; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over handle, nickname and bio, max 256 characters; `sort` (string, optional) — Sort enum: followers_desc, engagement_desc, likes_desc, relevance. engagement_desc ranks by post-level engagement rate, currently populated for a subset of creators (highest-reach first); creators without it sort last; `verified` (boolean, optional) — Filter by verified badge; true keeps only verified creators

### `datasets_github_users_facets`

- **HTTP:** `GET /datasets/github-users/facets`
- **What:** Facet the GitHub users dataset. Returns terms aggregation counts for the GitHub users dataset. Facet enum: `influence_tier`, `type`, `country`, `country_code`, `state`, `city`, `domains`, `company`, `reachable`, `has_email`, `has_twitter`, `has_blog`, `active_90d`, `hireable`, `is_org`, `is_bot`, `is_suspected_automation`. influence_tier enum: `nano`, `micro`, `mid`, `macro`, `mega`. Suspected-automation records are excluded by default unless is_suspected_automation is set.
- **Params:** `active_90d` (boolean, optional) — Filter by activity within the last 90 days; `city` (string, optional) — Exact geocoded city filter, max 128 characters; `company` (string, optional) — Exact normalized-company filter, max 128 characters; `country` (string, optional) — Exact geocoded country filter, max 128 characters; `country_code` (string, optional) — Exact ISO country-code filter, max 128 characters; `domain` (string, optional) — Interest-domain tag filter, max 128 characters; `facet` (string, **required**) — Facet enum: influence_tier, type, country, country_code, state, city, domains, company, reachable, has_email, has_twitter, has_blog, active_90d, hireable, is_org, is_bot, is_suspected_automation; `has_blog` (boolean, optional) — Filter by public blog/website presence; `has_email` (boolean, optional) — Filter by public email presence; `has_twitter` (boolean, optional) — Filter by public Twitter/X handle presence; `hireable` (boolean, optional) — Filter by the GitHub available-for-hire flag; `influence_tier` (string, optional) — Follower-tier enum: nano, micro, mid, macro, mega; `is_bot` (boolean, optional) — Bot filter; `is_org` (boolean, optional) — Organization filter; `is_suspected_automation` (boolean, optional) — Suspected automation filter; omitted these are hidden by default; `lat` (number, optional) — Latitude for radius filtering; `login` (string, optional) — Exact login filter, max 128 characters; `lon` (number, optional) — Longitude for radius filtering; `max_account_age_years` (number, optional) — Maximum account age in years; `max_followers` (integer, optional) — Maximum follower count; `min_account_age_years` (number, optional) — Minimum account age in years; `min_followers` (integer, optional) — Minimum follower count; `min_rank_score` (integer, optional) — Minimum composite rank score; `min_repos` (integer, optional) — Minimum public repository count; `q` (string, optional) — Full-text query over login, name, company, bio and location, max 256 characters; `radius_m` (integer, optional) — Radius in meters, 1 through 50000; requires lat and lon when supplied; `reachable` (boolean, optional) — Filter by any public contact channel; `sort` (string, optional) — Sort enum: relevance, rank_score_desc, followers_desc, account_age_desc, account_age_asc, distance_asc; `state` (string, optional) — Exact geocoded state filter, max 128 characters

### `datasets_github_users_item`

- **HTTP:** `GET /datasets/github-users/items/{login}`
- **What:** Get a GitHub user from the dataset. Returns one enriched GitHub user record by login from dataset id enum value `github-users`.
- **Params:** `login` (string, **required**) — GitHub login, max 128 characters

### `datasets_github_users_nearby`

- **HTTP:** `GET /datasets/github-users/nearby`
- **What:** Search nearby GitHub users. Searches enriched GitHub users near a coordinate, sorted by distance, in dataset id enum value `github-users`. influence_tier enum: `nano`, `micro`, `mid`, `macro`, `mega`.
- **Params:** `influence_tier` (string, optional) — Follower-tier enum: nano, micro, mid, macro, mega; `lat` (number, **required**) — Latitude; `lon` (number, **required**) — Longitude; `min_followers` (integer, optional) — Minimum follower count; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `radius_m` (integer, **required**) — Radius in meters, max 50000; `reachable` (boolean, optional) — Filter by any public contact channel

### `datasets_github_users_search`

- **HTTP:** `GET /datasets/github-users/search`
- **What:** Search the GitHub users dataset. Searches enriched public GitHub user profiles stored in a search index. influence_tier enum: `nano`, `micro`, `mid`, `macro`, `mega`. Sort enum: `relevance`, `rank_score_desc`, `followers_desc`, `account_age_desc`, `account_age_asc`, `distance_asc`.
- **Params:** `active_90d` (boolean, optional) — Filter by activity within the last 90 days; `city` (string, optional) — Exact geocoded city filter, max 128 characters; `company` (string, optional) — Exact normalized-company filter, max 128 characters; `country` (string, optional) — Exact geocoded country filter, max 128 characters; `country_code` (string, optional) — Exact ISO country-code filter, max 128 characters; `domain` (string, optional) — Interest-domain tag filter (e.g. ml-ai, web, devops), max 128 characters; `has_blog` (boolean, optional) — Filter by public blog/website presence; `has_email` (boolean, optional) — Filter by public email presence; `has_twitter` (boolean, optional) — Filter by public Twitter/X handle presence; `hireable` (boolean, optional) — Filter by the GitHub available-for-hire flag; `influence_tier` (string, optional) — Follower-tier enum: nano, micro, mid, macro, mega; `is_bot` (boolean, optional) — Bot filter (normally false; the crawl skips bots); `is_org` (boolean, optional) — Organization filter (normally false; the crawl indexes individuals); `is_suspected_automation` (boolean, optional) — Suspected automation (commit-farm/mass-repo bots); omitted these are hidden by default, pass true to isolate them; `lat` (number, optional) — Latitude for radius filtering or distance sort; `login` (string, optional) — Exact login filter, max 128 characters; `lon` (number, optional) — Longitude for radius filtering or distance sort; `max_account_age_years` (number, optional) — Maximum account age in years; `max_followers` (integer, optional) — Maximum follower count; `min_account_age_years` (number, optional) — Minimum account age in years; `min_followers` (integer, optional) — Minimum follower count; `min_rank_score` (integer, optional) — Minimum composite rank score; `min_repos` (integer, optional) — Minimum public repository count; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over login, name, company, bio and location, max 256 characters; `radius_m` (integer, optional) — Radius in meters, 1 through 50000; requires lat and lon when supplied; `reachable` (boolean, optional) — Filter by any public contact channel; `sort` (string, optional) — Sort enum: relevance, rank_score_desc, followers_desc, account_age_desc, account_age_asc, distance_asc; `state` (string, optional) — Exact geocoded state filter, max 128 characters

### `datasets_goodreads_authors_facets`

- **HTTP:** `GET /datasets/goodreads-authors/facets`
- **What:** Facet Goodreads authors dataset. Returns terms aggregation counts for the Goodreads authors dataset. Facet enum: `genres`, `run_id`.
- **Params:** `facet` (string, **required**) — Facet enum: genres, run_id; `genre` (string, optional) — Exact genre filter, max 128 characters; `min_rating` (number, optional) — Minimum average rating, 0 through 5; `min_ratings_count` (integer, optional) — Minimum number of ratings; `name` (string, optional) — Exact author name filter, max 128 characters; `q` (string, optional) — Full-text query over name, about and genres, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters

### `datasets_goodreads_authors_item`

- **HTTP:** `GET /datasets/goodreads-authors/items/{id}`
- **What:** Get a Goodreads author from dataset. Returns one crawled Goodreads author profile record by id from dataset id enum value `goodreads-authors`.
- **Params:** `id` (string, **required**) — Goodreads author id, e.g. 153394

### `datasets_goodreads_authors_search`

- **HTTP:** `GET /datasets/goodreads-authors/search`
- **What:** Search Goodreads authors dataset. Searches the crawled public Goodreads author profile index. Authors are discovered as a byproduct of the books crawl (every credited book contributor, plus the genre/search/list seed sources) — not a full catalog. Sort enum: `relevance`, `rating_desc`, `reviews_desc`, `name_asc`.
- **Params:** `genre` (string, optional) — Exact genre filter (e.g. Fantasy, Romance, Nonfiction), max 128 characters; `min_rating` (number, optional) — Minimum average rating, 0 through 5; `min_ratings_count` (integer, optional) — Minimum number of ratings; `name` (string, optional) — Exact author name filter, max 128 characters; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over name, about and genres, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `sort` (string, optional) — Sort enum: relevance, rating_desc, reviews_desc, name_asc

### `datasets_goodreads_books_facets`

- **HTTP:** `GET /datasets/goodreads-books/facets`
- **What:** Facet Goodreads books dataset. Returns terms aggregation counts for the Goodreads books dataset. Facet enum: `genres`, `format`, `language`, `publisher`, `primary_author`, `primary_author_id`, `series_name`, `publication_year`, `run_id`.
- **Params:** `author` (string, optional) — Exact author name filter, max 128 characters; `author_id` (string, optional) — Exact Goodreads author id filter, max 128 characters; `facet` (string, **required**) — Facet enum: genres, format, language, publisher, primary_author, primary_author_id, series_name, publication_year, run_id; `format` (string, optional) — Exact format filter, max 128 characters; `genre` (string, optional) — Exact genre filter, max 128 characters; `isbn` (string, optional) — Exact ISBN-10 filter, max 128 characters; `isbn13` (string, optional) — Exact ISBN-13 filter, max 128 characters; `language` (string, optional) — Exact language filter, max 128 characters; `max_pages` (integer, optional) — Maximum page count; `max_publication_year` (integer, optional) — Maximum publication year; `min_pages` (integer, optional) — Minimum page count; `min_publication_year` (integer, optional) — Minimum publication year; `min_rating` (number, optional) — Minimum average rating, 0 through 5; `min_ratings_count` (integer, optional) — Minimum number of ratings; `publisher` (string, optional) — Exact publisher filter, max 128 characters; `q` (string, optional) — Full-text query over title, author and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `series` (string, optional) — Exact series name filter, max 128 characters

### `datasets_goodreads_books_item`

- **HTTP:** `GET /datasets/goodreads-books/items/{id}`
- **What:** Get a Goodreads book from dataset. Returns one crawled Goodreads book record by id from dataset id enum value `goodreads-books`.
- **Params:** `id` (string, **required**) — Goodreads book id, e.g. 2767052

### `datasets_goodreads_books_search`

- **HTTP:** `GET /datasets/goodreads-books/search`
- **What:** Search Goodreads books dataset. Searches the crawled public Goodreads book catalog stored in a search index. Discovered from curated Listopia "best of" lists, a search-term sweep, and author bibliography expansion — not a full catalog. Sort enum: `relevance`, `rating_desc`, `reviews_desc`, `publication_desc`, `publication_asc`, `pages_desc`, `pages_asc`, `title_asc`.
- **Params:** `author` (string, optional) — Exact author name filter (matches any credited contributor), max 128 characters; `author_id` (string, optional) — Exact Goodreads author id filter, max 128 characters; `format` (string, optional) — Exact format filter (e.g. Hardcover, Paperback, Kindle Edition), max 128 characters; `genre` (string, optional) — Exact genre filter (e.g. Fantasy, Romance, Nonfiction), max 128 characters; `isbn` (string, optional) — Exact ISBN-10 filter, max 128 characters; `isbn13` (string, optional) — Exact ISBN-13 filter, max 128 characters; `language` (string, optional) — Exact language filter (e.g. English, Spanish), max 128 characters; `max_pages` (integer, optional) — Maximum page count; `max_publication_year` (integer, optional) — Maximum publication year; `min_pages` (integer, optional) — Minimum page count; `min_publication_year` (integer, optional) — Minimum publication year; `min_rating` (number, optional) — Minimum average rating, 0 through 5; `min_ratings_count` (integer, optional) — Minimum number of ratings; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `publisher` (string, optional) — Exact publisher filter, max 128 characters; `q` (string, optional) — Full-text query over title, author and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `series` (string, optional) — Exact series name filter, max 128 characters; `sort` (string, optional) — Sort enum: relevance, rating_desc, reviews_desc, publication_desc, publication_asc, pages_desc, pages_asc, title_asc

### `datasets_google_map_facets`

- **HTTP:** `GET /datasets/google-map-businesses/facets`
- **What:** Facet stored Google Maps businesses. Returns terms aggregation counts for Google Maps businesses. Facet enum: `category`, `country`, `state`, `county`, `city`, `town`, `website_status`. Category facet values are exact locale-specific Google Maps labels and can be localized, non-ASCII, or contain punctuation; pass a returned value unchanged to the category filter.
- **Params:** `category` (string, optional) — Exact locale-specific Google Maps category label; use the category facet to discover values, max 128 characters; `city` (string, optional) — Exact city filter, max 128 characters; `country` (string, optional) — Exact country filter, max 128 characters; `county` (string, optional) — Exact county filter, max 128 characters; `facet` (string, **required**) — Facet enum: category, country, state, county, city, town, website_status; `has_geo` (boolean, optional) — Filter by location presence: true keeps only mappable businesses with coordinates; false isolates locationless service-area businesses that have no map location; `has_phone` (boolean, optional) — Filter by phone presence; `has_website` (boolean, optional) — Filter by website presence; `lat` (number, optional) — Latitude for radius filtering; `lon` (number, optional) — Longitude for radius filtering; `min_rating` (number, optional) — Minimum rating, 0 through 5. Businesses with no aggregate Google rating are returned with rating null, so any min_rating above 0 excludes them.; `min_review_count` (integer, optional) — Minimum review count; `q` (string, optional) — Full-text business search query, max 256 characters; `radius_m` (integer, optional) — Radius in meters, 1 through 50000; requires lat and lon when supplied; `sort` (string, optional) — Sort enum: relevance, updated_at_desc, rating_desc, review_count_desc, distance_asc; `state` (string, optional) — Exact state filter, max 128 characters; `town` (string, optional) — Exact town filter, max 128 characters

### `datasets_google_map_item`

- **HTTP:** `GET /datasets/google-map-businesses/items/{place_id}`
- **What:** Get a stored Google Maps business. Returns one stored Google Maps business by Google place_id from dataset id enum value `google-map-businesses`. The `category` field contains the exact Google Maps category label returned for the business locale and can be localized, non-ASCII, or contain punctuation. A `rating` of `null` means no aggregate rating is available. A `review_count` of `null` means Google did not return a count; numeric `0` means Google confirmed zero reviews. Locationless service-area businesses (online/mobile/home-based) have a `null` `geo`.
- **Params:** `place_id` (string, **required**) — Google Place ID, max 256 characters

### `datasets_google_map_nearby`

- **HTTP:** `GET /datasets/google-map-businesses/nearby`
- **What:** Search nearby stored Google Maps businesses. Searches stored Google Maps businesses near a coordinate in dataset id enum value `google-map-businesses`. `category` is the exact Google Maps category label returned for the business locale; it can be localized, non-ASCII, or contain punctuation, so use the category facet to discover exact filter values. A `rating` of `null` means no aggregate rating is available. A `review_count` of `null` means Google did not return a count; numeric `0` means Google confirmed zero reviews. `min_rating` above 0 excludes unrated businesses.
- **Params:** `category` (string, optional) — Exact locale-specific Google Maps category label; use the category facet to discover values, max 128 characters; `lat` (number, **required**) — Latitude; `lon` (number, **required**) — Longitude; `min_rating` (number, optional) — Minimum rating, 0 through 5. Businesses with no aggregate Google rating are returned with rating null, so any min_rating above 0 excludes them.; `min_review_count` (integer, optional) — Minimum review count; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `radius_m` (integer, **required**) — Radius in meters, max 50000

### `datasets_google_map_search`

- **HTTP:** `GET /datasets/google-map-businesses/search`
- **What:** Search stored Google Maps businesses. Searches Google Maps business records stored in a search index. Sort enum: `relevance`, `updated_at_desc`, `rating_desc`, `review_count_desc`, `distance_asc`. `category` is the exact Google Maps category label returned for the business locale; it can be localized, non-ASCII, or contain punctuation, so use the category facet to discover exact filter values. A `rating` of `null` means no aggregate rating is available. A `review_count` of `null` means Google did not return a count; numeric `0` means Google confirmed zero reviews. `rating_desc` sorts unrated businesses last, and `min_rating` above 0 excludes them. Use `has_geo=false` to isolate locationless service-area businesses (which have a `null` `geo`).
- **Params:** `category` (string, optional) — Exact locale-specific Google Maps category label; use the category facet to discover values, max 128 characters; `city` (string, optional) — Exact city filter, max 128 characters; `country` (string, optional) — Exact country filter, max 128 characters; `county` (string, optional) — Exact county filter, max 128 characters; `has_geo` (boolean, optional) — Filter by location presence: true keeps only mappable businesses with coordinates; false isolates locationless service-area businesses that have no map location; `has_phone` (boolean, optional) — Filter by phone presence; `has_website` (boolean, optional) — Filter by website presence; `lat` (number, optional) — Latitude for radius filtering or distance sort; `lon` (number, optional) — Longitude for radius filtering or distance sort; `min_rating` (number, optional) — Minimum rating, 0 through 5. Businesses with no aggregate Google rating are returned with rating null, so any min_rating above 0 excludes them.; `min_review_count` (integer, optional) — Minimum review count; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text business search query, max 256 characters; `radius_m` (integer, optional) — Radius in meters, 1 through 50000; requires lat and lon when supplied; `sort` (string, optional) — Sort enum: relevance, updated_at_desc, rating_desc, review_count_desc, distance_asc; `state` (string, optional) — Exact state filter, max 128 characters; `town` (string, optional) — Exact town filter, max 128 characters

### `datasets_housing_markets_facets`

- **HTTP:** `GET /datasets/housing-markets/facets`
- **What:** Facet the US housing markets dataset. Returns terms aggregation counts for the housing markets dataset. Facet enum: `region_type`, `state_code`, `property_type`, `parent_metro`, `parent_metro_code`, `income_vintage`, `is_latest`, `period_begin`. region_type enum: `national`, `metro`, `county`, `city`, `zip`. property_type enum: `All Residential`, `Single Family Residential`, `Condo/Co-op`, `Townhouse`, `Multi-Family (2-4 Unit)`, `Single Units Only`.
- **Params:** `facet` (string, **required**) — Facet enum: region_type, state_code, property_type, parent_metro, parent_metro_code, income_vintage, is_latest, period_begin; `latest` (boolean, optional) — Filter for the most recent period per region and property type; `max_inventory` (integer, optional) — Maximum active inventory; `max_median_dom` (number, optional) — Maximum median days on market; `max_median_list_price` (number, optional) — Maximum median list price in USD; `max_median_sale_price` (number, optional) — Maximum median sale price in USD; `max_price_to_income` (number, optional) — Maximum price-to-income ratio; `max_salary_to_buy` (integer, optional) — Maximum salary needed to buy in USD per year; `min_homes_sold` (integer, optional) — Minimum homes sold in the period; `min_inventory` (integer, optional) — Minimum active inventory; `min_median_dom` (number, optional) — Minimum median days on market; `min_median_list_price` (number, optional) — Minimum median list price in USD; `min_median_sale_price` (number, optional) — Minimum median sale price in USD; `min_price_to_income` (number, optional) — Minimum price-to-income ratio; `min_salary_to_buy` (integer, optional) — Minimum salary needed to buy in USD per year; `parent_metro_code` (string, optional) — Exact parent metro (CBSA) code filter, e.g. 16980; `period` (string, optional) — Exact period start date filter, YYYY-MM-DD; `property_type` (string, optional) — Property type enum: All Residential, Single Family Residential, Condo/Co-op, Townhouse, Multi-Family (2-4 Unit), Single Units Only; `q` (string, optional) — Full-text query over region name and city, max 256 characters; `region_type` (string, optional) — Region level enum: national, metro, county, city, zip; `state_code` (string, optional) — Exact two-letter state code filter, e.g. CA; `zip_code` (string, optional) — Exact zip code filter (zip-level rows only), e.g. 60616

### `datasets_housing_markets_item`

- **HTTP:** `GET /datasets/housing-markets/items/{region_type}/{table_id}`
- **What:** Get a US housing market record from the dataset. Returns one housing-market record by region_type and Redfin table_id from dataset id enum value `housing-markets`. region_type enum: `national`, `metro`, `county`, `city`, `zip`. property_type enum: `All Residential`, `Single Family Residential`, `Condo/Co-op`, `Townhouse`, `Multi-Family (2-4 Unit)`, `Single Units Only` (defaults to `All Residential`). `period` defaults to the most recent period on record. Pass `history=true` to get the full monthly series (a `{dataset, region_type, table_id, property_type, items}` envelope, sorted by period ascending) instead of a single record.
- **Params:** `history` (boolean, optional) — Return the full monthly series instead of a single period; `period` (string, optional) — Exact period start date, YYYY-MM-DD; defaults to the latest period; `property_type` (string, optional) — Property type enum: All Residential, Single Family Residential, Condo/Co-op, Townhouse, Multi-Family (2-4 Unit), Single Units Only; defaults to All Residential; `region_type` (string, **required**) — Region level enum: national, metro, county, city, zip; `table_id` (integer, **required**) — Redfin table id (the region's stable numeric id)

### `datasets_housing_markets_search`

- **HTTP:** `GET /datasets/housing-markets/search`
- **What:** Search the US housing markets dataset. Searches monthly Redfin housing-market statistics per region and property type since 2012, joined to Census ACS income for affordability metrics. region_type enum: `national`, `metro`, `county`, `city`, `zip`. property_type enum: `All Residential`, `Single Family Residential`, `Condo/Co-op`, `Townhouse`, `Multi-Family (2-4 Unit)`, `Single Units Only`. Sort enum: `relevance`, `price_desc`, `price_asc`, `list_price_desc`, `list_price_asc`, `price_to_income_desc`, `price_to_income_asc`, `salary_to_buy_desc`, `salary_to_buy_asc`, `dom_asc`, `dom_desc`, `inventory_desc`, `homes_sold_desc`, `period_desc`. Use `latest=true` for the most recent period per region series.
- **Params:** `latest` (boolean, optional) — Filter for the most recent period per region and property type; `max_inventory` (integer, optional) — Maximum active inventory; `max_median_dom` (number, optional) — Maximum median days on market; `max_median_list_price` (number, optional) — Maximum median list price in USD; `max_median_sale_price` (number, optional) — Maximum median sale price in USD; `max_price_to_income` (number, optional) — Maximum price-to-income ratio; `max_salary_to_buy` (integer, optional) — Maximum salary needed to buy in USD per year; `min_homes_sold` (integer, optional) — Minimum homes sold in the period; `min_inventory` (integer, optional) — Minimum active inventory; `min_median_dom` (number, optional) — Minimum median days on market; `min_median_list_price` (number, optional) — Minimum median list price in USD; `min_median_sale_price` (number, optional) — Minimum median sale price in USD; `min_price_to_income` (number, optional) — Minimum price-to-income ratio; `min_salary_to_buy` (integer, optional) — Minimum salary needed to buy in USD per year; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `parent_metro_code` (string, optional) — Exact parent metro (CBSA) code filter, e.g. 16980; `period` (string, optional) — Exact period start date filter, YYYY-MM-DD; `property_type` (string, optional) — Property type enum: All Residential, Single Family Residential, Condo/Co-op, Townhouse, Multi-Family (2-4 Unit), Single Units Only; `q` (string, optional) — Full-text query over region name and city, max 256 characters; `region_type` (string, optional) — Region level enum: national, metro, county, city, zip; `sort` (string, optional) — Sort enum: relevance, price_desc, price_asc, list_price_desc, list_price_asc, price_to_income_desc, price_to_income_asc, salary_to_buy_desc, salary_to_buy_asc, dom_asc, dom_desc, inventory_desc, homes_sold_desc, period_desc; `state_code` (string, optional) — Exact two-letter state code filter, e.g. CA; `zip_code` (string, optional) — Exact zip code filter (zip-level rows only), e.g. 60616

### `datasets_instagram_users_facets`

- **HTTP:** `GET /datasets/instagram-users/facets`
- **What:** Facet the Instagram users dataset. Returns terms aggregation counts for the Instagram users dataset. Facet enum: `is_verified`, `is_business_account`, `has_bio`, `has_external_url`, `category_name`, `source_tier`.
- **Params:** `category_name` (string, optional) — Exact category filter (case-insensitive, e.g. Digital Creator), max 128 characters; `crawled_after` (string, optional) — Records last refreshed on or after this date (RFC3339 or YYYY-MM-DD); `crawled_before` (string, optional) — Records last refreshed on or before this date (RFC3339 or YYYY-MM-DD); `created_after` (string, optional) — Accounts created on or after this date (RFC3339 or YYYY-MM-DD); `created_before` (string, optional) — Accounts created on or before this date (RFC3339 or YYYY-MM-DD); `facet` (string, **required**) — Facet enum: is_verified, is_business_account, has_bio, has_external_url, category_name, source_tier; `has_bio` (boolean, optional) — Filter by a non-empty profile biography; `has_external_url` (boolean, optional) — Filter by a linked external URL; `is_business_account` (boolean, optional) — Filter by business or creator accounts; `is_verified` (boolean, optional) — Filter by the Instagram verification checkmark; `max_followers` (integer, optional) — Maximum follower count; `max_ratio` (number, optional) — Maximum follower-to-following ratio; `min_followers` (integer, optional) — Minimum follower count; `min_ratio` (number, optional) — Minimum follower-to-following ratio; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over username, full_name and biography, max 256 characters; `sort` (string, optional) — Sort enum: relevance, followers_desc, followers_asc, crawled_at_desc, crawled_at_asc, created_at_desc, created_at_asc; `source_tier` (string, optional) — Exact filter for seed tier (e.g. crossref, vertical-hashtags, mention-graph, head-directory); `username` (string, optional) — Exact username filter (case-insensitive), max 128 characters

### `datasets_instagram_users_item`

- **HTTP:** `GET /datasets/instagram-users/items/{username}`
- **What:** Get an Instagram user from the dataset. Returns one Instagram user record by username from dataset id enum value `instagram-users`.
- **Params:** `username` (string, **required**) — Instagram username, with or without a leading @, max 128 characters

### `datasets_instagram_users_search`

- **HTTP:** `GET /datasets/instagram-users/search`
- **What:** Search the Instagram users dataset. Searches public Instagram user profiles stored in a search index. Sort enum: `relevance`, `followers_desc`, `followers_asc`, `crawled_at_desc`, `crawled_at_asc`, `created_at_desc`, `created_at_asc`.
- **Params:** `category_name` (string, optional) — Exact category filter (case-insensitive, e.g. Digital Creator), max 128 characters; `crawled_after` (string, optional) — Records last refreshed on or after this date (RFC3339 or YYYY-MM-DD); `crawled_before` (string, optional) — Records last refreshed on or before this date (RFC3339 or YYYY-MM-DD); `created_after` (string, optional) — Accounts created on or after this date (RFC3339 or YYYY-MM-DD); `created_before` (string, optional) — Accounts created on or before this date (RFC3339 or YYYY-MM-DD); `has_bio` (boolean, optional) — Filter by a non-empty profile biography; `has_external_url` (boolean, optional) — Filter by a linked external URL; `is_business_account` (boolean, optional) — Filter by business or creator accounts; `is_verified` (boolean, optional) — Filter by the Instagram verification checkmark; `max_followers` (integer, optional) — Maximum follower count; `max_ratio` (number, optional) — Maximum follower-to-following ratio; `min_followers` (integer, optional) — Minimum follower count; `min_ratio` (number, optional) — Minimum follower-to-following ratio; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over username, full_name and biography, max 256 characters; `sort` (string, optional) — Sort enum: relevance, followers_desc, followers_asc, crawled_at_desc, crawled_at_asc, created_at_desc, created_at_asc; `source_tier` (string, optional) — Exact filter for seed tier (e.g. crossref, vertical-hashtags, mention-graph, head-directory), max 128 characters; `username` (string, optional) — Exact username filter (case-insensitive), max 128 characters

### `datasets_jobs_companies`

- **HTTP:** `GET /datasets/jobs/companies`
- **What:** Find which companies are hiring. Searches the discovered company board registry — which companies are hiring, on which ATS (or, for the 5 single-company big-tech providers, which platform), with how many open roles. Set sponsors_visa=true to keep companies with certified employer filings in recent public U.S. Department of Labor LCA disclosure data. This is company-level historical evidence, not a guarantee for a specific role or candidate. provider enum: `greenhouse`, `lever`, `ashby`, `workday`, `smartrecruiters`, `workable`, `recruitee`, `rippling`, `personio`, `teamtailor`, `oracle`, `ukg`, `icims`, `eightfold`, `gem`, `pinpoint`, `amazon-jobs`, `apple-jobs`, `google-jobs`, `meta-jobs`, `tesla-jobs`. status enum: `active`, `empty`, `gone`, `blocked`, `pending`, `invalid`. sort enum: `open_desc`, `company_asc`, `crawled_desc`.
- **Params:** `min_open_roles` (integer, optional) — Minimum open roles; `page` (integer, optional) — Page number, default 1; `page_size` (integer, optional) — Page size, default 20, max 100; `provider` (string, optional) — Provider filter; `q` (string, optional) — Match on company name / domain; `sort` (string, optional) — Sort enum: open_desc, company_asc, crawled_desc; `sponsors_visa` (boolean, optional) — Keep companies with recent certified DOL LCA filings (default false); `status` (string, optional) — Board status. Enum: active, empty, gone, blocked, pending, invalid

### `datasets_jobs_company_item`

- **HTTP:** `GET /datasets/jobs/companies/{id}`
- **What:** Get a single company by board id. Returns one discovered company board by its dataset board id. When the company name matches recent public U.S. Department of Labor LCA disclosure data, the response includes `lca_sponsorship` with filing counts and observed fiscal-quarter range; this is company-level historical evidence, not a guarantee for a specific role or candidate. When the board carries a known domain, the response also includes a `tech_stack` firmographic hint. Returns 404 when the board id is not in the registry.
- **Params:** `id` (string, **required**) — Dataset board id

### `datasets_jobs_facets`

- **HTTP:** `GET /datasets/jobs/facets`
- **What:** Facet the jobs dataset (hiring market aggregates). Aggregations over all open postings: top companies hiring, breakdown by provider (every provider filterable via /datasets/jobs/search's `provider` param), department, location, employment type, skill, benefit, education, security clearance, seniority, and ESCO/ISCO job family, plus the remote share — a live hiring-market snapshot. Seniority uses one mutually exclusive value: `entry`, `mid`, or `senior`; ambiguous occupations are omitted from job-family buckets.
- **Params:** `size` (integer, optional) — Buckets per facet, default 20, max 100

### `datasets_jobs_item`

- **HTTP:** `GET /datasets/jobs/items/{id}`
- **What:** Get a single posting from the jobs dataset. Returns one crawled job posting by its dataset posting id. Returns 404 when absent.
- **Params:** `id` (string, **required**) — Dataset posting id

### `datasets_jobs_nearby`

- **HTTP:** `GET /datasets/jobs/nearby`
- **What:** Find postings near a coordinate. Finds crawled job postings within `radius_km` of a `lat`/`lon`, nearest first. Only geocoded postings participate (the geo-enrich worker back-fills coordinates from each posting's location). Open roles only by default. provider enum: `greenhouse`, `lever`, `ashby`, `workday`, `smartrecruiters`, `workable`, `recruitee`, `rippling`, `personio`, `teamtailor`, `oracle`, `ukg`, `icims`, `eightfold`, `gem`, `pinpoint`, `amazon-jobs`, `apple-jobs`, `google-jobs`, `meta-jobs`, `tesla-jobs`.
- **Params:** `include_closed` (boolean, optional) — Include closed/filled roles (default false); `lat` (number, **required**) — Latitude, -90..90; `lon` (number, **required**) — Longitude, -180..180; `page` (integer, optional) — Page number, default 1; `page_size` (integer, optional) — Page size, default 20, max 100; `provider` (string, optional) — Provider filter; `radius_km` (number, optional) — Search radius in km, default 50, max 500

### `datasets_jobs_search`

- **HTTP:** `GET /datasets/jobs/search`
- **What:** Search the jobs dataset (all companies' live postings). Full-text + faceted search over every job posting crawled from every discovered company ATS board (Greenhouse, Lever, Ashby, Workday, SmartRecruiters, Workable, Recruitee, Rippling, Personio, Teamtailor, Oracle, UKG, iCIMS, Eightfold, Gem, Pinpoint) plus 5 single-company big-tech careers platforms (Amazon, Apple, Google, Meta, Tesla). Open roles only by default (set include_closed=true for historical/filled roles). Salary is parsed from a structured field when the provider has one, or from an explicit pay figure stated in the description otherwise, so coverage varies by posting rather than by provider; min_salary/max_salary filter on it and require salary_currency, since comparing raw compensation numbers across currencies is meaningless. Location is also exposed as structured city/state/country fields alongside the free-text location string, so city/state/country filter on an exact match of those parsed components rather than substring-matching the display string. job_family is an exact level-2 ISCO family label assigned from ESCO occupation evidence; ambiguous postings remain unclassified and do not match that filter. employment_type is never populated for google-jobs/meta-jobs, and posted_at (so sort=posted_desc) is never populated for meta-jobs/tesla-jobs -- their upstream APIs expose no such field. provider enum: `greenhouse`, `lever`, `ashby`, `workday`, `smartrecruiters`, `workable`, `recruitee`, `rippling`, `personio`, `teamtailor`, `oracle`, `ukg`, `icims`, `eightfold`, `gem`, `pinpoint`, `amazon-jobs`, `apple-jobs`, `google-jobs`, `meta-jobs`, `tesla-jobs`. workplace_type enum: `onsite`, `hybrid`, `remote`. sort enum: `relevance`, `posted_desc`, `company_asc`.
- **Params:** `city` (string, optional) — Exact city filter (parsed location component); `company` (string, optional) — Company name match; `country` (string, optional) — Exact country filter (parsed location component); ISO country code or name, matched case-insensitively; `department` (string, optional) — Exact department filter; `employment_type` (string, optional) — Exact employment-type filter; `include_closed` (boolean, optional) — Include closed/filled roles (default false = open only); `job_family` (string, optional) — Exact ESCO/ISCO job-family label filter; `location` (string, optional) — Location match; `max_salary` (number, optional) — Maximum salary (matches postings whose range starts at or below this); requires salary_currency; `min_salary` (number, optional) — Minimum salary (matches postings whose range reaches at least this); requires salary_currency; `page` (integer, optional) — Page number, default 1; `page_size` (integer, optional) — Page size, default 20, max 100; page*page_size must be <= 10000; `provider` (string, optional) — Provider filter; `q` (string, optional) — Full-text over title, company, description; `remote` (boolean, optional) — Filter by remote (true or false); `salary_currency` (string, optional) — 3-letter ISO currency code (e.g. USD) the min_salary/max_salary bounds are in; required when either bound is set; `sort` (string, optional) — Sort enum: relevance, posted_desc, company_asc; `state` (string, optional) — Exact state/region filter (parsed location component); `workplace_type` (string, optional) — Workplace type filter

### `datasets_journalists_facets`

- **HTTP:** `GET /datasets/journalists/facets`
- **What:** Facet the journalists dataset. Returns distribution counts over the journalists index (dataset id enum value `journalists`), honoring the same filters as search. Facet enum: `outlet`, `vertical`, `topic`, `contact_type`.
- **Params:** `contact_type` (string, optional) — Contact-availability filter. Enum: email, social, none; `facet` (string, **required**) — Facet enum: outlet, vertical, topic, contact_type; `outlet` (string, optional) — Exact outlet id filter; `q` (string, optional) — Full-text match on the journalist's name, title, and bio, max 256 characters; `topic` (string, optional) — Exact topic filter; `vertical` (string, optional) — Exact beat-vertical filter. Enum: tech, crypto, marketing, consumer_tech, consumer_policy, cybersecurity, health, gaming, climate, business, entertainment, sports, legal, science, politics, real_estate, automotive, travel, food, education, design, film_tv, fashion, music, personal_finance, tech_independent, culture_independent, local_news, construction, banking, retail, aerospace_defense, energy, agriculture, local_business

### `datasets_journalists_item`

- **HTTP:** `GET /datasets/journalists/items/{outlet}/{slug}`
- **What:** Get a journalist from the journalists dataset. Returns one journalist by outlet id and slug from dataset id enum value `journalists`. Returns 404 when the outlet is not supported or the journalist is not in the index.
- **Params:** `outlet` (string, **required**) — Outlet id, e.g. techcrunch. Use the ids returned by facets?facet=outlet; `slug` (string, **required**) — Journalist slug within the outlet, e.g. zack-whittaker

### `datasets_journalists_search`

- **HTTP:** `GET /datasets/journalists/search`
- **What:** Search the journalists dataset. Searches the journalists index (dataset id enum value `journalists`) — public journalist and reporter contact records crawled from news outlets' own staff/author pages, for PR outreach. Each record carries the outlet, title, best-effort beat topics, and any public contact info (a work email or a social handle) found on that outlet's own page. There is no cross-outlet upstream search; this dataset is built by crawling a curated roster of outlets ourselves. vertical enum: `tech`, `crypto`, `marketing`, `consumer_tech`, `consumer_policy`, `cybersecurity`, `health`, `gaming`, `climate`, `business`, `entertainment`, `sports`, `legal`, `science`, `politics`, `real_estate`, `automotive`, `travel`, `food`, `education`, `design`, `film_tv`, `fashion`, `music`, `personal_finance`, `tech_independent`, `culture_independent`, `local_news`, `construction`, `banking`, `retail`, `aerospace_defense`, `energy`, `agriculture`, `local_business`. contact_type enum: `email`, `social`, `none`. sort enum: `relevance`, `name_asc`, `outlet_asc`, `crawled_desc`.
- **Params:** `contact_type` (string, optional) — Contact-availability filter. Enum: email, social, none; `outlet` (string, optional) — Exact outlet id filter, e.g. techcrunch, coindesk. Use the ids returned by facets?facet=outlet; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text match on the journalist's name, title, and bio, max 256 characters; `sort` (string, optional) — Sort enum: relevance, name_asc, outlet_asc, crawled_desc; `topic` (string, optional) — Exact topic filter, e.g. security, stablecoins. Use the values returned by facets?facet=topic; `vertical` (string, optional) — Exact beat-vertical filter. Enum: tech, crypto, marketing, consumer_tech, consumer_policy, cybersecurity, health, gaming, climate, business, entertainment, sports, legal, science, politics, real_estate, automotive, travel, food, education, design, film_tv, fashion, music, personal_finance, tech_independent, culture_independent, local_news, construction, banking, retail, aerospace_defense, energy, agriculture, local_business

### `datasets_list`

- **HTTP:** `GET /datasets`
- **What:** List stored scraped datasets. Lists available read-only scraped datasets and the capabilities supported by each dataset.
- **Params:** _none_

### `datasets_numbeo_cities_facets`

- **HTTP:** `GET /datasets/numbeo-cities/facets`
- **What:** Facet the Numbeo cities dataset. Returns terms aggregation counts for the Numbeo cities dataset. Facet enum: `country`.
- **Params:** `country` (string, optional) — Exact country filter, max 128 characters; `facet` (string, **required**) — Facet enum: country; `max_cost_of_living_index` (number, optional) — Maximum Cost of Living Index (New York = 100); `max_crime_index` (number, optional) — Maximum Crime Index; `max_pollution_index` (number, optional) — Maximum Pollution Index; `max_traffic_index` (number, optional) — Maximum Traffic Index; `min_cost_of_living_index` (number, optional) — Minimum Cost of Living Index (New York = 100); `min_crime_index` (number, optional) — Minimum Crime Index; `min_health_care_index` (number, optional) — Minimum Health Care Index; `min_quality_of_life_index` (number, optional) — Minimum Quality of Life Index; `min_safety_index` (number, optional) — Minimum Safety Index; `q` (string, optional) — Full-text query over the city name, max 256 characters

### `datasets_numbeo_cities_item`

- **HTTP:** `GET /datasets/numbeo-cities/items/{slug}`
- **What:** Get a Numbeo city from the dataset. Returns one composite Numbeo city record by city slug from dataset id enum value `numbeo-cities`.
- **Params:** `slug` (string, **required**) — Numbeo city slug

### `datasets_numbeo_cities_search`

- **HTTP:** `GET /datasets/numbeo-cities/search`
- **What:** Search the Numbeo cities dataset. Searches the composite Numbeo cities dataset, merged from the current global rankings of all seven index families (cost of living, quality of life, crime, health care, pollution, traffic, property investment). A city appears once it is ranked by at least one family; coverage varies per city. Sort enum: `name_asc`, `cost_of_living_asc`, `cost_of_living_desc`, `quality_of_life_desc`, `safety_desc`, `crime_asc`, `health_care_desc`, `pollution_asc`, `traffic_asc`.
- **Params:** `country` (string, optional) — Exact country filter, max 128 characters; `max_cost_of_living_index` (number, optional) — Maximum Cost of Living Index (New York = 100); `max_crime_index` (number, optional) — Maximum Crime Index; `max_pollution_index` (number, optional) — Maximum Pollution Index; `max_traffic_index` (number, optional) — Maximum Traffic Index; `min_cost_of_living_index` (number, optional) — Minimum Cost of Living Index (New York = 100); `min_crime_index` (number, optional) — Minimum Crime Index; `min_health_care_index` (number, optional) — Minimum Health Care Index; `min_quality_of_life_index` (number, optional) — Minimum Quality of Life Index; `min_safety_index` (number, optional) — Minimum Safety Index; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over the city name, max 256 characters; `sort` (string, optional) — Sort enum: name_asc, cost_of_living_asc, cost_of_living_desc, quality_of_life_desc, safety_desc, crime_asc, health_care_desc, pollution_asc, traffic_asc

### `datasets_numbeo_countries_item`

- **HTTP:** `GET /datasets/numbeo-countries/items/{country}`
- **What:** Get a Numbeo country from the dataset. Returns one composite Numbeo country record by country name from dataset id enum value `numbeo-countries`.
- **Params:** `country` (string, **required**) — Country name as Numbeo spells it

### `datasets_numbeo_countries_search`

- **HTTP:** `GET /datasets/numbeo-countries/search`
- **What:** Search the Numbeo countries dataset. Searches the composite Numbeo countries dataset, merged from the current global by-country rankings of all seven index families. Sort enum: `name_asc`, `cost_of_living_asc`, `cost_of_living_desc`, `quality_of_life_desc`, `safety_desc`, `crime_asc`, `health_care_desc`, `pollution_asc`, `traffic_asc`.
- **Params:** `max_cost_of_living_index` (number, optional) — Maximum Cost of Living Index (New York = 100); `max_crime_index` (number, optional) — Maximum Crime Index; `max_pollution_index` (number, optional) — Maximum Pollution Index; `max_traffic_index` (number, optional) — Maximum Traffic Index; `min_cost_of_living_index` (number, optional) — Minimum Cost of Living Index (New York = 100); `min_crime_index` (number, optional) — Minimum Crime Index; `min_health_care_index` (number, optional) — Minimum Health Care Index; `min_quality_of_life_index` (number, optional) — Minimum Quality of Life Index; `min_safety_index` (number, optional) — Minimum Safety Index; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over the country name, max 256 characters; `sort` (string, optional) — Sort enum: name_asc, cost_of_living_asc, cost_of_living_desc, quality_of_life_desc, safety_desc, crime_asc, health_care_desc, pollution_asc, traffic_asc

### `datasets_pitchbook_advisors_facets`

- **HTTP:** `GET /datasets/pitchbook-advisors/facets`
- **What:** Facet PitchBook advisors dataset. Returns terms aggregation counts for the PitchBook advisors dataset. Facet enum: `service_type`, `hq_country`, `hq_state`, `run_id`.
- **Params:** `facet` (string, **required**) — Facet enum: service_type, hq_country, hq_state, run_id; `hq_country` (string, optional) — Exact headquarters country filter, max 128 characters; `hq_state` (string, optional) — Exact headquarters state/region filter, max 128 characters; `max_year_founded` (integer, optional) — Maximum founding year; `min_year_founded` (integer, optional) — Minimum founding year; `q` (string, optional) — Full-text query over name and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `service_type` (string, optional) — Exact service provider type filter, max 128 characters

### `datasets_pitchbook_advisors_item`

- **HTTP:** `GET /datasets/pitchbook-advisors/items/{id}`
- **What:** Get a PitchBook advisor from dataset. Returns one crawled PitchBook advisor record by id from dataset id enum value `pitchbook-advisors`.
- **Params:** `id` (string, **required**) — PitchBook advisor id, e.g. 676215-64

### `datasets_pitchbook_advisors_search`

- **HTTP:** `GET /datasets/pitchbook-advisors/search`
- **What:** Search PitchBook advisors dataset. Searches the crawled public PitchBook advisor (service provider — e.g. investment bank, lender, financing advisory firm) profile catalog stored in a search index. Discovered from PitchBook's public sitemap. Sort enum: `relevance`, `name_asc`, `year_founded_desc`, `recently_crawled_desc`.
- **Params:** `hq_country` (string, optional) — Exact headquarters country filter, max 128 characters; `hq_state` (string, optional) — Exact headquarters state/region filter, max 128 characters; `max_year_founded` (integer, optional) — Maximum founding year; `min_year_founded` (integer, optional) — Minimum founding year; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over name and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `service_type` (string, optional) — Exact service provider type filter (e.g. Commercial Bank, Investment Bank, Financing Advisory), max 128 characters; `sort` (string, optional) — Sort enum: relevance, name_asc, year_founded_desc, recently_crawled_desc

### `datasets_pitchbook_companies_facets`

- **HTTP:** `GET /datasets/pitchbook-companies/facets`
- **What:** Facet PitchBook companies dataset. Returns terms aggregation counts for the PitchBook companies dataset. Facet enum: `status`, `primary_industry`, `financing_status`, `ownership_status`, `hq_country`, `hq_state`, `run_id`.
- **Params:** `facet` (string, **required**) — Facet enum: status, primary_industry, financing_status, ownership_status, hq_country, hq_state, run_id; `financing_status` (string, optional) — Exact financing status filter, max 128 characters; `hq_country` (string, optional) — Exact headquarters country filter, max 128 characters; `hq_state` (string, optional) — Exact headquarters state/region filter, max 128 characters; `max_year_founded` (integer, optional) — Maximum founding year; `min_investor_count` (integer, optional) — Minimum number of investors; `min_year_founded` (integer, optional) — Minimum founding year; `ownership_status` (string, optional) — Exact ownership status filter, max 128 characters; `primary_industry` (string, optional) — Exact primary industry filter, max 128 characters; `q` (string, optional) — Full-text query over name and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `status` (string, optional) — Exact status filter, max 128 characters

### `datasets_pitchbook_companies_item`

- **HTTP:** `GET /datasets/pitchbook-companies/items/{id}`
- **What:** Get a PitchBook company from dataset. Returns one crawled PitchBook company record by id from dataset id enum value `pitchbook-companies`.
- **Params:** `id` (string, **required**) — PitchBook company id, e.g. 752821-12

### `datasets_pitchbook_companies_search`

- **HTTP:** `GET /datasets/pitchbook-companies/search`
- **What:** Search PitchBook companies dataset. Searches the crawled public PitchBook company profile catalog stored in a search index. Discovered from PitchBook's public sitemap. Sort enum: `relevance`, `name_asc`, `year_founded_desc`, `investor_count_desc`, `recently_crawled_desc`.
- **Params:** `financing_status` (string, optional) — Exact financing status filter, max 128 characters; `hq_country` (string, optional) — Exact headquarters country filter, max 128 characters; `hq_state` (string, optional) — Exact headquarters state/region filter, max 128 characters; `max_year_founded` (integer, optional) — Maximum founding year; `min_investor_count` (integer, optional) — Minimum number of investors; `min_year_founded` (integer, optional) — Minimum founding year; `ownership_status` (string, optional) — Exact ownership status filter, max 128 characters; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `primary_industry` (string, optional) — Exact primary industry filter, max 128 characters; `q` (string, optional) — Full-text query over name and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `sort` (string, optional) — Sort enum: relevance, name_asc, year_founded_desc, investor_count_desc, recently_crawled_desc; `status` (string, optional) — Exact status filter (e.g. Private, Public, Acquired, Out of Business), max 128 characters

### `datasets_pitchbook_funds_facets`

- **HTTP:** `GET /datasets/pitchbook-funds/facets`
- **What:** Facet PitchBook funds dataset. Returns terms aggregation counts for the PitchBook funds dataset. Facet enum: `fund_strategy`, `fund_status`, `run_id`.
- **Params:** `facet` (string, **required**) — Facet enum: fund_strategy, fund_status, run_id; `fund_status` (string, optional) — Exact fund status filter, max 128 characters; `fund_strategy` (string, optional) — Exact fund strategy filter, max 128 characters; `max_vintage_year` (integer, optional) — Maximum vintage year; `min_vintage_year` (integer, optional) — Minimum vintage year; `q` (string, optional) — Full-text query over name and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters

### `datasets_pitchbook_funds_item`

- **HTTP:** `GET /datasets/pitchbook-funds/items/{id}`
- **What:** Get a PitchBook fund from dataset. Returns one crawled PitchBook fund record by id from dataset id enum value `pitchbook-funds`.
- **Params:** `id` (string, **required**) — PitchBook fund id, e.g. 19719-91F

### `datasets_pitchbook_funds_search`

- **HTTP:** `GET /datasets/pitchbook-funds/search`
- **What:** Search PitchBook funds dataset. Searches the crawled public PitchBook fund profile catalog stored in a search index. Discovered from PitchBook's public sitemap. Sort enum: `relevance`, `name_asc`, `vintage_desc`, `recently_crawled_desc`.
- **Params:** `fund_status` (string, optional) — Exact fund status filter (e.g. Closed, Raising), max 128 characters; `fund_strategy` (string, optional) — Exact fund strategy filter (e.g. Early Stage VC, Buyout), max 128 characters; `max_vintage_year` (integer, optional) — Maximum vintage year; `min_vintage_year` (integer, optional) — Minimum vintage year; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over name and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `sort` (string, optional) — Sort enum: relevance, name_asc, vintage_desc, recently_crawled_desc

### `datasets_pitchbook_investors_facets`

- **HTTP:** `GET /datasets/pitchbook-investors/facets`
- **What:** Facet PitchBook investors dataset. Returns terms aggregation counts for the PitchBook investors dataset. Facet enum: `status`, `investor_type`, `hq_country`, `hq_state`, `run_id`.
- **Params:** `facet` (string, **required**) — Facet enum: status, investor_type, hq_country, hq_state, run_id; `hq_country` (string, optional) — Exact headquarters country filter, max 128 characters; `hq_state` (string, optional) — Exact headquarters state/region filter, max 128 characters; `investor_type` (string, optional) — Exact investor type filter, max 128 characters; `min_exits_count` (integer, optional) — Minimum number of exits; `min_portfolio_count` (integer, optional) — Minimum current portfolio size; `q` (string, optional) — Full-text query over name and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `status` (string, optional) — Exact status filter, max 128 characters

### `datasets_pitchbook_investors_item`

- **HTTP:** `GET /datasets/pitchbook-investors/items/{id}`
- **What:** Get a PitchBook investor from dataset. Returns one crawled PitchBook investor record by id from dataset id enum value `pitchbook-investors`.
- **Params:** `id` (string, **required**) — PitchBook investor id, e.g. 294471-37

### `datasets_pitchbook_investors_search`

- **HTTP:** `GET /datasets/pitchbook-investors/search`
- **What:** Search PitchBook investors dataset. Searches the crawled public PitchBook investor (fund manager/firm) profile catalog stored in a search index. Discovered from PitchBook's public sitemap. Sort enum: `relevance`, `name_asc`, `portfolio_count_desc`, `recently_crawled_desc`.
- **Params:** `hq_country` (string, optional) — Exact headquarters country filter, max 128 characters; `hq_state` (string, optional) — Exact headquarters state/region filter, max 128 characters; `investor_type` (string, optional) — Exact investor type filter (e.g. Venture Capital, Private Equity, Angel), max 128 characters; `min_exits_count` (integer, optional) — Minimum number of exits; `min_portfolio_count` (integer, optional) — Minimum current portfolio size; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over name and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `sort` (string, optional) — Sort enum: relevance, name_asc, portfolio_count_desc, recently_crawled_desc; `status` (string, optional) — Exact status filter (e.g. Active, Inactive), max 128 characters

### `datasets_pitchbook_limited_partners_facets`

- **HTTP:** `GET /datasets/pitchbook-limited-partners/facets`
- **What:** Facet PitchBook limited partners dataset. Returns terms aggregation counts for the PitchBook limited partners dataset. Facet enum: `institution_type`, `hq_country`, `hq_state`, `run_id`.
- **Params:** `facet` (string, **required**) — Facet enum: institution_type, hq_country, hq_state, run_id; `hq_country` (string, optional) — Exact headquarters country filter, max 128 characters; `hq_state` (string, optional) — Exact headquarters state/region filter, max 128 characters; `institution_type` (string, optional) — Exact institution type filter, max 128 characters; `max_year_founded` (integer, optional) — Maximum founding year; `min_year_founded` (integer, optional) — Minimum founding year; `q` (string, optional) — Full-text query over name and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters

### `datasets_pitchbook_limited_partners_item`

- **HTTP:** `GET /datasets/pitchbook-limited-partners/items/{id}`
- **What:** Get a PitchBook limited partner from dataset. Returns one crawled PitchBook limited partner record by id from dataset id enum value `pitchbook-limited-partners`.
- **Params:** `id` (string, **required**) — PitchBook limited partner id, e.g. 864326-44

### `datasets_pitchbook_limited_partners_search`

- **HTTP:** `GET /datasets/pitchbook-limited-partners/search`
- **What:** Search PitchBook limited partners dataset. Searches the crawled public PitchBook limited partner (institutional investor — e.g. pension fund, endowment, insurance company) profile catalog stored in a search index. Discovered from PitchBook's public sitemap. Some limited partner profiles have no FAQ section -- this is normal, not a sign of missing data. Sort enum: `relevance`, `name_asc`, `year_founded_desc`, `recently_crawled_desc`.
- **Params:** `hq_country` (string, optional) — Exact headquarters country filter, max 128 characters; `hq_state` (string, optional) — Exact headquarters state/region filter, max 128 characters; `institution_type` (string, optional) — Exact institution type filter (e.g. Corporate Pension, Private Investment Fund, Endowment), max 128 characters; `max_year_founded` (integer, optional) — Maximum founding year; `min_year_founded` (integer, optional) — Minimum founding year; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over name and description, max 256 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `sort` (string, optional) — Sort enum: relevance, name_asc, year_founded_desc, recently_crawled_desc

### `datasets_playstation_games_facets`

- **HTTP:** `GET /datasets/playstation-games/facets`
- **What:** Facet PlayStation games dataset. Returns terms aggregation counts for the PlayStation games dataset. Facet enum: `publisher`, `classification`, `genres`, `platforms`, `content_rating_authority`, `content_descriptors`, `price_tier`, `service_branding`, `region`, `release_year`, `run_id`, `is_free`, `is_addon`, `is_tied_to_subscription`, `coming_soon`. price_tier enum: `free`, `under_5`, `5_to_10`, `10_to_20`, `20_to_40`, `40_to_60`, `60_plus`.
- **Params:** `branding` (string, optional) — Exact subscription/service-branding filter, max 128 characters; `classification` (string, optional) — Exact classification filter, max 128 characters; `coming_soon` (boolean, optional) — Filter for pre-release titles; `concept_id` (string, optional) — Exact concept id filter, max 128 characters; `content_descriptor` (string, optional) — Exact content-descriptor filter, max 128 characters; `content_rating` (string, optional) — Exact content-rating authority filter, max 128 characters; `facet` (string, **required**) — Facet enum: publisher, classification, genres, platforms, content_rating_authority, content_descriptors, price_tier, service_branding, region, release_year, run_id, is_free, is_addon, is_tied_to_subscription, coming_soon; `genre` (string, optional) — Exact genre filter, max 128 characters; `is_addon` (boolean, optional) — Filter add-ons vs games; `is_free` (boolean, optional) — Filter by free flag; `is_tied_to_subscription` (boolean, optional) — Filter subscription-included titles; `max_price_value` (integer, optional) — Maximum current price in minor units; `max_release_year` (integer, optional) — Maximum release year; `min_discount_pct` (integer, optional) — Minimum discount percent, 0 through 100; `min_price_value` (integer, optional) — Minimum current price in minor units; `min_release_year` (integer, optional) — Minimum release year; `min_star_count` (integer, optional) — Minimum number of star ratings; `min_star_rating` (number, optional) — Minimum average star rating, 0 through 5; `np_title_id` (string, optional) — Exact np_title_id filter, max 128 characters; `on_sale` (boolean, optional) — Filter by titles currently discounted (discount_pct > 0); `platform` (string, optional) — Exact platform filter: PS4 or PS5; `price_tier` (string, optional) — Price-tier enum: free, under_5, 5_to_10, 10_to_20, 20_to_40, 40_to_60, 60_plus; `publisher` (string, optional) — Exact publisher filter, max 128 characters; `q` (string, optional) — Full-text query over name and publisher, max 256 characters; `region` (string, optional) — Exact store region (country code) filter, max 128 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters

### `datasets_playstation_games_item`

- **HTTP:** `GET /datasets/playstation-games/items/{product_id}`
- **What:** Get a PlayStation game from dataset. Returns one crawled PlayStation Store record by product_id from dataset id enum value `playstation-games`.
- **Params:** `product_id` (string, **required**) — PlayStation product id (e.g. UP0001-PPSA01491_00-GAME000000000000)

### `datasets_playstation_games_search`

- **HTTP:** `GET /datasets/playstation-games/search`
- **What:** Search PlayStation games dataset. Searches the crawled public PlayStation Store catalog stored in a search index. One row per product SKU (game, edition or add-on); concept_id / np_title_id group a title's SKUs. price_tier enum: `free`, `under_5`, `5_to_10`, `10_to_20`, `20_to_40`, `40_to_60`, `60_plus`. Sort enum: `relevance`, `rating_desc`, `reviews_desc`, `price_asc`, `price_desc`, `discount_desc`, `release_desc`, `release_asc`.
- **Params:** `branding` (string, optional) — Exact subscription/service-branding filter (e.g. PS_PLUS, EA_PLAY, UBISOFT_PLUS), max 128 characters; `classification` (string, optional) — Exact classification filter: FULL_GAME, PREMIUM_EDITION, GAME_BUNDLE, ADD_ON_PACK, VIRTUAL_CURRENCY, LEVEL, OTHER; `coming_soon` (boolean, optional) — Filter for pre-release / not-yet-purchasable titles; `concept_id` (string, optional) — Exact concept id filter (groups all SKUs of a title), max 128 characters; `content_descriptor` (string, optional) — Exact content-descriptor filter (e.g. Blood, Violence, In-Game Purchases, Users Interact), max 128 characters; `content_rating` (string, optional) — Exact content-rating authority filter (e.g. ESRB, PEGI), max 128 characters; `genre` (string, optional) — Exact genre filter (e.g. Action, Role Playing Games), max 128 characters; `is_addon` (boolean, optional) — Filter: true returns add-ons/DLC/currency, false returns games and editions; `is_free` (boolean, optional) — Filter by free flag; `is_tied_to_subscription` (boolean, optional) — Filter for titles included with a subscription (e.g. free with PS Plus); `max_price_value` (integer, optional) — Maximum current price in minor units (e.g. cents); `max_release_year` (integer, optional) — Maximum release year; `min_discount_pct` (integer, optional) — Minimum discount percent, 0 through 100; `min_price_value` (integer, optional) — Minimum current price in minor units (e.g. cents); `min_release_year` (integer, optional) — Minimum release year; `min_star_count` (integer, optional) — Minimum number of star ratings; `min_star_rating` (number, optional) — Minimum average star rating, 0 through 5; `np_title_id` (string, optional) — Exact np_title_id filter, max 128 characters; `on_sale` (boolean, optional) — Filter by titles currently discounted (discount_pct > 0); `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `platform` (string, optional) — Exact platform filter: PS4 or PS5; `price_tier` (string, optional) — Price-tier enum: free, under_5, 5_to_10, 10_to_20, 20_to_40, 40_to_60, 60_plus; `publisher` (string, optional) — Exact publisher filter, max 128 characters; `q` (string, optional) — Full-text query over name and publisher, max 256 characters; `region` (string, optional) — Exact store region (country code) filter, max 128 characters; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `sort` (string, optional) — Sort enum: relevance, rating_desc, reviews_desc, price_asc, price_desc, discount_desc, release_desc, release_asc

### `datasets_producthunt_makers_facets`

- **HTTP:** `GET /datasets/producthunt-makers/facets`
- **What:** Facet the Product Hunt makers dataset. Returns distribution counts over the Product Hunt makers dataset (dataset id enum value `producthunt-makers`), honoring the same filters as search. Facet enum: `topic`, `product_count_band`.
- **Params:** `facet` (string, **required**) — Facet enum: topic, product_count_band; `min_products` (integer, optional) — Minimum number of products made, 0 or greater; `min_total_votes` (integer, optional) — Minimum total upvotes across the maker's products, 0 or greater; `q` (string, optional) — Full-text query over maker name and headline, max 256 characters; `topic` (string, optional) — Exact topic-slug the maker builds in, max 128 characters

### `datasets_producthunt_makers_item`

- **HTTP:** `GET /datasets/producthunt-makers/items/{username}`
- **What:** Get a Product Hunt maker from the dataset. Returns one maker by Product Hunt username from dataset id enum value `producthunt-makers`, including the products they made and their aggregate footprint. Returns 404 when the username is not in the dataset.
- **Params:** `username` (string, **required**) — Product Hunt maker username, e.g. rrhoover

### `datasets_producthunt_makers_search`

- **HTTP:** `GET /datasets/producthunt-makers/search`
- **What:** Search the Product Hunt makers dataset. Searches Product Hunt makers from the dataset id enum value `producthunt-makers` — public-profile records of the people who made products, with their footprint (products made, total upvotes, topics) for maker leaderboards. Public fields only. Sort enum: `total_votes_desc`, `product_count_desc`, `followers_desc`, `relevance`.
- **Params:** `min_products` (integer, optional) — Minimum number of products made, 0 or greater; `min_total_votes` (integer, optional) — Minimum total upvotes across the maker's products, 0 or greater; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over maker name and headline, max 256 characters; `sort` (string, optional) — Sort enum: total_votes_desc, product_count_desc, followers_desc, relevance; `topic` (string, optional) — Exact topic-slug the maker builds in, e.g. artificial-intelligence, max 128 characters

### `datasets_producthunt_products_facets`

- **HTTP:** `GET /datasets/producthunt-products/facets`
- **What:** Facet the Product Hunt products dataset. Returns distribution counts over the Product Hunt products dataset (dataset id enum value `producthunt-products`), honoring the same filters as search. Facet enum: `topic`, `launch_year`, `pricing_type`, `product_state`.
- **Params:** `facet` (string, **required**) — Facet enum: topic, launch_year, pricing_type, product_state; `has_website` (boolean, optional) — Website presence filter; `is_online` (boolean, optional) — true keeps only products still online, false only retired products; `launched_after` (string, optional) — Lower bound on first-launch date, an ISO-8601 date (YYYY-MM-DD); `launched_before` (string, optional) — Upper bound on first-launch date, an ISO-8601 date (YYYY-MM-DD); `maker` (string, optional) — Exact maker-username filter (populated by hydration), max 128 characters; `min_rating` (number, optional) — Minimum review rating, from 0 through 5; `min_votes` (integer, optional) — Minimum upvotes, 0 or greater; `pricing_type` (string, optional) — Exact pricing-type filter, e.g. free, paid, freemium; `q` (string, optional) — Full-text query over product name and tagline, max 256 characters; `topic` (string, optional) — Exact topic-slug filter, e.g. artificial-intelligence, max 128 characters

### `datasets_producthunt_products_item`

- **HTTP:** `GET /datasets/producthunt-products/items/{slug}`
- **What:** Get a Product Hunt product from the dataset. Returns one product by its Product Hunt slug from dataset id enum value `producthunt-products`, including its full launch history and (once hydrated) description, website, twitter_url, pricing and makers. Returns 404 when the slug is not in the archive.
- **Params:** `slug` (string, **required**) — Product Hunt product slug, e.g. chatgpt

### `datasets_producthunt_products_search`

- **HTTP:** `GET /datasets/producthunt-products/search`
- **What:** Search the Product Hunt products dataset. Searches individual Product Hunt launches from the dataset id enum value `producthunt-products` — the searchable launch archive. Each result is one product with its topics, upvotes, ranks and launch history; description/website/twitter_url/pricing/makers are filled in as hydration runs. Sort enum: `relevance`, `votes_desc`, `launched_desc`, `launched_asc`, `rating_desc`, `best_rank_asc`.
- **Params:** `has_website` (boolean, optional) — Website presence filter (populated by hydration); `is_online` (boolean, optional) — true keeps only products still online, false only retired products; `launched_after` (string, optional) — Lower bound on first-launch date, an ISO-8601 date (YYYY-MM-DD); `launched_before` (string, optional) — Upper bound on first-launch date, an ISO-8601 date (YYYY-MM-DD); `maker` (string, optional) — Exact maker-username filter (populated by hydration), max 128 characters; `min_rating` (number, optional) — Minimum review rating, from 0 through 5 (populated by hydration); `min_votes` (integer, optional) — Minimum upvotes, 0 or greater; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `pricing_type` (string, optional) — Exact pricing-type filter (populated by hydration), e.g. free, paid, freemium; `q` (string, optional) — Full-text query over product name and tagline, max 256 characters; `sort` (string, optional) — Sort enum: relevance, votes_desc, launched_desc, launched_asc, rating_desc, best_rank_asc; `topic` (string, optional) — Exact topic-slug filter, e.g. artificial-intelligence, max 128 characters

### `datasets_producthunt_trends_facets`

- **HTTP:** `GET /datasets/producthunt-trends/facets`
- **What:** Facet the Product Hunt trends dataset. Returns suppressed distribution counts over the Product Hunt trends dataset (dataset id enum value `producthunt-trends`), honoring the same filters as search. Facet enum: `topic`, `launch_year`.
- **Params:** `facet` (string, **required**) — Facet enum: topic, launch_year; `group_by` (string, optional) — Aggregate cell dimension enum: topic_month, topic_year, topic. Defaults to topic_month; `launched_after` (string, optional) — Lower bound on first-launch date, an ISO-8601 date (YYYY-MM-DD); `launched_before` (string, optional) — Upper bound on first-launch date, an ISO-8601 date (YYYY-MM-DD); `min_launches` (integer, optional) — Minimum launches per bucket; raises the small-cell suppression floor; `min_votes` (integer, optional) — Minimum product upvotes, 0 or greater; `topic` (string, optional) — Exact topic-slug filter, e.g. artificial-intelligence, max 128 characters

### `datasets_producthunt_trends_search`

- **HTTP:** `GET /datasets/producthunt-trends/search`
- **What:** Search the Product Hunt trends dataset. Returns aggregate Product Hunt launch trends from the dataset id enum value `producthunt-trends`. Aggregate-only: each row is a category-over-time cell (a topic, optionally within a calendar period), reporting launch count, total and average upvotes, average rating and the top product — never an individual product record. Thin cells are suppressed. group_by enum: `topic_month`, `topic_year`, `topic`. Sort enum: `period_desc`, `period_asc`, `launch_count_desc`, `sum_votes_desc`.
- **Params:** `group_by` (string, optional) — Aggregate cell dimension enum: topic_month, topic_year, topic. Defaults to topic_month; `launched_after` (string, optional) — Lower bound on first-launch date, an ISO-8601 date (YYYY-MM-DD); `launched_before` (string, optional) — Upper bound on first-launch date, an ISO-8601 date (YYYY-MM-DD); `min_launches` (integer, optional) — Minimum launches per cell; raises the small-cell suppression floor (never lowered below the built-in minimum); `min_votes` (integer, optional) — Minimum product upvotes, 0 or greater; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `sort` (string, optional) — Sort enum: period_desc, period_asc, launch_count_desc, sum_votes_desc; `topic` (string, optional) — Exact topic-slug filter, e.g. artificial-intelligence, max 128 characters

### `datasets_reddit_trending_search`

- **HTTP:** `GET /datasets/reddit-trending/search`
- **What:** Search the reddit-trending dataset. Searches daily snapshots of each tracked subreddit's hot-feed post order, stored in a search index (one document per subreddit × snapshot × rank) so history accumulates. With no `date` the latest snapshot is returned (today's trending); pair `subreddit` with `sort=date_desc` for a subreddit's trending history over time. There is no score or comment-count field — the underlying credential-free scraper does not expose vote counts, so `rank` reflects Reddit's own hot-feed order rather than a locally computed score.
- **Params:** `date` (string, optional) — Snapshot date filter yyyy-MM-dd; defaults to the latest snapshot; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over the post title, max 256 characters; `sort` (string, optional) — Sort enum: rank, date_desc; `subreddit` (string, optional) — Exact subreddit-name filter, max 128 characters

### `datasets_sec_companies_facets`

- **HTTP:** `GET /datasets/sec-companies/facets`
- **What:** Facet the SEC companies dataset. Returns terms-aggregation counts for one facet of the SEC companies dataset, scoped to the same filters as search. Facet enum: `sic`, `sic_description`, `exchange`, `state_of_incorporation`, `entity_type`, `reporting_currency`, `revenue_band`, `forms_filed`. `revenue_band` buckets latest-annual revenue into: `unknown`, `under_1m`, `1m_10m`, `10m_100m`, `100m_1b`, `1b_10b`, `over_10b`.
- **Params:** `entity_type` (string, optional) — Exact entity-type filter, max 64 characters; `exchange` (string, optional) — Exact exchange filter as reported by EDGAR, max 64 characters; `facet` (string, **required**) — Facet enum: sic, sic_description, exchange, state_of_incorporation, entity_type, reporting_currency, revenue_band, forms_filed; `form_filed` (string, optional) — Exact form-type filter, e.g. 10-K, 8-K; `has_financials` (boolean, optional) — When true, keep only companies that have XBRL financial statements; `min_revenue` (number, optional) — Minimum latest-annual revenue in USD (normalized at reference rates), 0 or greater; `q` (string, optional) — Full-text query over the company name, or an exact ticker match, max 256 characters; `reporting_currency` (string, optional) — Exact reporting-currency filter, ISO-4217 code, e.g. USD, JPY, EUR; `sic` (string, optional) — Exact SIC industry-code filter, max 32 characters; `state_of_incorporation` (string, optional) — Exact state/country-of-incorporation filter, max 32 characters; `ticker` (string, optional) — Exact ticker filter (case-insensitive), max 32 characters

### `datasets_sec_companies_financials`

- **HTTP:** `GET /datasets/sec-companies/financials/{cik}`
- **What:** Get a SEC company's financial-statement history. Returns a company's normalized financial-statement history (income statement, balance sheet, cash flow) from the SEC companies dataset, newest fiscal year first. An unknown CIK or a company with no XBRL data returns an empty series rather than a 404 — most filers without a current ticker have no financial-statement history at all. `lines` keys are the same normalized concept names the live `/sec/financials` endpoint uses (e.g. `revenue`, `net_income`, `total_assets`); `ratios` keys include `gross_margin`, `operating_margin`, `net_margin`, `revenue_growth_yoy`, `current_ratio`, `debt_to_equity`, `free_cash_flow` where derivable. statement enum: `income`, `balance`, `cash_flow`. period enum: `annual`, `quarterly`.
- **Params:** `cik` (string, **required**) — SEC CIK, numeric or zero-padded; `from` (integer, optional) — Inclusive lower bound on fiscal_year; `limit` (integer, optional) — Maximum points returned (most recent fiscal years first), default 100, max 400; `period` (string, optional) — Period-type enum: annual, quarterly. Omit to return both.; `statement` (string, optional) — Statement enum: income, balance, cash_flow. Omit to return all three.; `to` (integer, optional) — Inclusive upper bound on fiscal_year

### `datasets_sec_companies_insider`

- **HTTP:** `GET /datasets/sec-companies/insider/{cik}`
- **What:** Get a SEC company's insider-transaction history. Returns a company's insider (Form 3/4/5) transaction history from the SEC companies dataset, most recent transaction first. An unknown CIK or a company with no reported transactions returns an empty series rather than a 404.
- **Params:** `cik` (string, **required**) — SEC CIK, numeric or zero-padded; `code` (string, optional) — Exact transaction code filter, e.g. P (open-market purchase), S (sale); `from` (string, optional) — Inclusive start date (YYYY-MM-DD, UTC) filtering transaction date; `limit` (integer, optional) — Maximum transactions returned (most recent first), default 50, max 200; `to` (string, optional) — Inclusive end date (YYYY-MM-DD, UTC) filtering transaction date

### `datasets_sec_companies_item`

- **HTTP:** `GET /datasets/sec-companies/items/{cik}`
- **What:** Get a company from the SEC companies dataset. Returns one SEC-reporting company by CIK from dataset id `sec-companies`, including its filing-history summary, financial-statement rollups, and trailing-90-day insider-activity summary. Returns 404 when the CIK is not in the dataset.
- **Params:** `cik` (string, **required**) — SEC CIK, numeric or zero-padded, e.g. 320193 or 0000320193

### `datasets_sec_companies_search`

- **HTTP:** `GET /datasets/sec-companies/search`
- **What:** Search the SEC companies dataset. Searches SEC-reporting companies stored in a search index — normalized filing history, financial-statement rollups (latest annual/quarterly revenue, net income, total assets) and trailing-90-day insider (Form 3/4/5) activity. Sort enum: `relevance`, `name_asc`, `revenue_desc`, `net_income_desc`, `filing_recent_desc`, `insider_activity_desc`. `entity_type`, `sic`, `sic_description`, `exchange`, and `state_of_incorporation` are open filters over the exact values EDGAR reports for each filer (not a fixed enum) — discover real values via the matching facet.
- **Params:** `cik` (string, optional) — Exact CIK filter, numeric or zero-padded, e.g. 320193 or 0000320193; `entity_type` (string, optional) — Exact entity-type filter as reported by EDGAR (e.g. operating), max 64 characters; `exchange` (string, optional) — Exact exchange filter as reported by EDGAR, e.g. Nasdaq, NYSE, max 64 characters; `form_filed` (string, optional) — Exact form-type filter; keeps only companies that have ever filed this form, e.g. 10-K, 8-K; `has_financials` (boolean, optional) — When true, keep only companies that have XBRL financial statements; `max_revenue` (number, optional) — Maximum latest-annual revenue in USD (normalized), 0 or greater; `min_insider_txn_count_90d` (integer, optional) — Minimum insider (Form 3/4/5) transaction count in the trailing 90 days, 0 or greater; `min_net_income` (number, optional) — Minimum latest-annual net income in USD (normalized; negative allowed); `min_revenue` (number, optional) — Minimum latest-annual revenue in USD (normalized from the filer's reporting currency at reference rates), 0 or greater; `min_total_assets` (number, optional) — Minimum latest-annual total assets in USD (normalized), 0 or greater; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over the company name, or an exact ticker match, max 256 characters; `reporting_currency` (string, optional) — Exact reporting-currency filter, ISO-4217 code, e.g. USD, JPY, EUR; `sic` (string, optional) — Exact SIC industry-code filter, e.g. 3571, max 32 characters; `sic_description` (string, optional) — Exact SIC description filter, e.g. Electronic Computers, max 128 characters; `sort` (string, optional) — Sort enum: relevance, name_asc, revenue_desc, net_income_desc, filing_recent_desc, insider_activity_desc; `state_of_incorporation` (string, optional) — Exact state/country-of-incorporation filter as reported by EDGAR, e.g. DE, CA, max 32 characters; `ticker` (string, optional) — Exact ticker filter (case-insensitive), e.g. AAPL, max 32 characters

### `datasets_sec_institutional_positions_facets`

- **HTTP:** `GET /datasets/sec-institutional-positions/facets`
- **What:** Facet the SEC institutional positions dataset. Returns terms-aggregation counts for one facet of the SEC institutional positions dataset, scoped to the same filters as search. Facet enum: `manager`, `issuer`.
- **Params:** `cusip` (string, optional) — Exact CUSIP filter, max 16 characters; `facet` (string, **required**) — Facet enum: manager, issuer; `issuer_name` (string, optional) — Issuer-name text filter (best-effort match), max 256 characters; `manager_cik` (string, optional) — Exact institutional-manager CIK filter, numeric or zero-padded

### `datasets_sec_institutional_positions_search`

- **HTTP:** `GET /datasets/sec-institutional-positions/search`
- **What:** Search the SEC institutional positions dataset. Searches institutional investment managers' quarterly 13F portfolio holdings stored in a search index. Filter by manager_cik for a manager's full reported portfolio (an exact, reliable filter), or by issuer_name/cusip for a best-effort view of which managers reported a position in an issuer — SEC publishes no authoritative CUSIP-to-CIK mapping, so the issuer side is never a guaranteed-resolved join. Sort enum: `value_desc`, `value_asc`, `shares_desc`.
- **Params:** `cusip` (string, optional) — Exact CUSIP filter, max 16 characters; `issuer_name` (string, optional) — Issuer-name text filter (best-effort match, not a resolved CIK join), max 256 characters; `manager_cik` (string, optional) — Exact institutional-manager CIK filter, numeric or zero-padded; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `sort` (string, optional) — Sort enum: value_desc, value_asc, shares_desc

### `datasets_steam_achievements_search`

- **HTTP:** `GET /datasets/steam-achievements/search`
- **What:** Search steam-achievements dataset. Searches per-game global achievement unlock percentages (one document per appid × achievement). Pass `app_id` to list a game's achievements. Sort enum: `percent_desc` (most-unlocked first, default), `percent_asc` (rarest first), `rank_asc`.
- **Params:** `app_id` (string, optional) — Exact Steam app id filter; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `sort` (string, optional) — Sort enum: percent_desc, percent_asc, rank_asc

### `datasets_steam_charts_search`

- **HTTP:** `GET /datasets/steam-charts/search`
- **What:** Search the steam-charts dataset. Searches daily snapshots of Steam's player-count and sales charts, stored in a search index (one document per chart × country × snapshot × rank) so history accumulates. Charts: `most_played` (weekly peak concurrent), `concurrent` (live concurrent players), `top_sellers` (weekly sales; country-specific). With no `date` the latest snapshot is returned (today's chart); pair `app_id` with `sort=date_desc` for an app's rank/players over time. Country is `global` for the player-count charts or an ISO code (e.g. `us`) for `top_sellers`. Sort enum: `rank`, `rank_desc`, `date_desc`.
- **Params:** `app_id` (string, optional) — Exact Steam app id filter; pair with sort=date_desc for rank/players history; `chart` (string, optional) — Chart enum: most_played, concurrent, top_sellers; `country` (string, optional) — Market filter: global (player-count charts) or an ISO country code (top_sellers), max 128 characters; `date` (string, optional) — Snapshot date filter yyyy-MM-dd; defaults to the latest snapshot; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over the game name, max 256 characters; `sort` (string, optional) — Sort enum: rank, rank_desc, date_desc

### `datasets_steam_games_facets`

- **HTTP:** `GET /datasets/steam-games/facets`
- **What:** Facet the Steam games dataset. Returns terms aggregation counts for the Steam games dataset. Facet enum: `type`, `developer`, `publisher`, `genres`, `categories`, `tags`, `primary_tag`, `price_tier`, `review_tier`, `owners_bucket`, `release_year`, `run_id`, `is_free`, `coming_soon`, `platform_windows`, `platform_mac`, `platform_linux`. price_tier enum: `free`, `under5`, `5to15`, `15to30`, `30to60`, `over60`. review_tier enum: `overwhelmingly_positive`, `very_positive`, `positive`, `mostly_positive`, `mixed`, `mostly_negative`, `negative`, `very_negative`, `overwhelmingly_negative`, `insufficient`.
- **Params:** `category` (string, optional) — Exact store category filter, max 128 characters; `developer` (string, optional) — Exact developer filter, max 128 characters; `facet` (string, **required**) — Facet enum: type, developer, publisher, genres, categories, tags, primary_tag, price_tier, review_tier, owners_bucket, release_year, run_id, is_free, coming_soon, platform_windows, platform_mac, platform_linux; `genre` (string, optional) — Exact genre filter, max 128 characters; `is_free` (boolean, optional) — Filter by free-to-play flag; `linux` (boolean, optional) — Filter by Linux support; `mac` (boolean, optional) — Filter by macOS support; `max_price_cents` (integer, optional) — Maximum current price in cents; `max_release_year` (integer, optional) — Maximum release year; `min_ccu` (integer, optional) — Minimum peak concurrent users yesterday; `min_metacritic` (integer, optional) — Minimum Metacritic score, 0 through 100; `min_owners` (integer, optional) — Minimum estimated owners (SteamSpy owners midpoint); `min_positive` (integer, optional) — Minimum positive review count; `min_price_cents` (integer, optional) — Minimum current price in cents; `min_release_year` (integer, optional) — Minimum release year; `min_review_score` (number, optional) — Minimum positive-review ratio, 0 through 1; `min_total_reviews` (integer, optional) — Minimum total review count; `on_sale` (boolean, optional) — Filter by titles currently discounted (discount_pct > 0); `owners_bucket` (string, optional) — Exact SteamSpy owners-range bucket filter, max 128 characters; `price_tier` (string, optional) — Price-tier enum: free, under5, 5to15, 15to30, 30to60, over60; `publisher` (string, optional) — Exact publisher filter, max 128 characters; `q` (string, optional) — Full-text query over name, developer and publisher, max 256 characters; `review_tier` (string, optional) — Review-tier enum: overwhelmingly_positive, very_positive, positive, mostly_positive, mixed, mostly_negative, negative, very_negative, overwhelmingly_negative, insufficient; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `tag` (string, optional) — Exact community-tag filter (e.g. Roguelike, Cozy), max 128 characters; `type` (string, optional) — Exact storefront type filter, max 128 characters; `windows` (boolean, optional) — Filter by Windows support

### `datasets_steam_games_item`

- **HTTP:** `GET /datasets/steam-games/items/{appid}`
- **What:** Get a Steam game from the dataset. Returns one enriched Steam catalog record by appid from dataset id enum value `steam-games`.
- **Params:** `appid` (integer, **required**) — Steam app id

### `datasets_steam_games_search`

- **HTTP:** `GET /datasets/steam-games/search`
- **What:** Search the Steam games dataset. Searches enriched public Steam catalog records stored in a search index. price_tier enum: `free`, `under5`, `5to15`, `15to30`, `30to60`, `over60`. review_tier enum: `overwhelmingly_positive`, `very_positive`, `positive`, `mostly_positive`, `mixed`, `mostly_negative`, `negative`, `very_negative`, `overwhelmingly_negative`, `insufficient`. Sort enum: `relevance`, `owners_desc`, `reviews_desc`, `review_score_desc`, `ccu_desc`, `metacritic_desc`, `price_asc`, `price_desc`, `release_desc`, `release_asc`.
- **Params:** `category` (string, optional) — Exact store category filter (e.g. Single-player), max 128 characters; `developer` (string, optional) — Exact developer filter, max 128 characters; `genre` (string, optional) — Exact genre filter (e.g. Action, Indie), max 128 characters; `is_free` (boolean, optional) — Filter by free-to-play flag; `linux` (boolean, optional) — Filter by Linux support; `mac` (boolean, optional) — Filter by macOS support; `max_price_cents` (integer, optional) — Maximum current price in cents; `max_release_year` (integer, optional) — Maximum release year; `min_ccu` (integer, optional) — Minimum peak concurrent users yesterday; `min_metacritic` (integer, optional) — Minimum Metacritic score, 0 through 100; `min_owners` (integer, optional) — Minimum estimated owners (SteamSpy owners midpoint); `min_positive` (integer, optional) — Minimum positive review count; `min_price_cents` (integer, optional) — Minimum current price in cents; `min_release_year` (integer, optional) — Minimum release year; `min_review_score` (number, optional) — Minimum positive-review ratio, 0 through 1; `min_total_reviews` (integer, optional) — Minimum total review count; `on_sale` (boolean, optional) — Filter by titles currently discounted (discount_pct > 0); `owners_bucket` (string, optional) — Exact SteamSpy owners-range bucket filter, max 128 characters; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `price_tier` (string, optional) — Price-tier enum: free, under5, 5to15, 15to30, 30to60, over60; `publisher` (string, optional) — Exact publisher filter, max 128 characters; `q` (string, optional) — Full-text query over name, developer and publisher, max 256 characters; `review_tier` (string, optional) — Review-tier enum: overwhelmingly_positive, very_positive, positive, mostly_positive, mixed, mostly_negative, negative, very_negative, overwhelmingly_negative, insufficient; `run_id` (string, optional) — Exact crawl run-id filter, max 128 characters; `sort` (string, optional) — Sort enum: relevance, owners_desc, reviews_desc, review_score_desc, ccu_desc, metacritic_desc, price_asc, price_desc, release_desc, release_asc; `tag` (string, optional) — Exact community-tag filter (e.g. Roguelike, Metroidvania, Cozy), max 128 characters; `type` (string, optional) — Exact storefront type filter (e.g. game, dlc, demo), max 128 characters; `windows` (boolean, optional) — Filter by Windows support

### `datasets_steam_news_search`

- **HTTP:** `GET /datasets/steam-news/search`
- **What:** Search the steam-news dataset. Searches Steam news + announcements for tracked apps (one document per appid × gid; the latest items per app are kept). Filter by `app_id` for a single game's news, or full-text `q` over the title + contents. Sort enum: `date_desc` (newest first, default), `date_asc`.
- **Params:** `app_id` (string, optional) — Exact Steam app id filter; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over the news title + contents, max 256 characters; `sort` (string, optional) — Sort enum: date_desc, date_asc

### `datasets_steam_playercounts_search`

- **HTTP:** `GET /datasets/steam-playercounts/search`
- **What:** Search steam-playercounts dataset. Searches the daily concurrent-player time series for tracked games (one document per appid × day). Pair `app_id` with `sort=date_desc` for a game's player-count history, or pass `date` for one day's snapshot. Sort enum: `date_desc` (default), `date_asc`, `players_desc`.
- **Params:** `app_id` (string, optional) — Exact Steam app id filter; `date` (string, optional) — Snapshot date filter yyyy-MM-dd; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `sort` (string, optional) — Sort enum: date_desc, date_asc, players_desc

### `datasets_steam_prices_search`

- **HTTP:** `GET /datasets/steam-prices/search`
- **What:** Search the steam-prices dataset. Searches the daily price time series for priced games (one document per appid × day; integer cents). Pair `app_id` with `sort=date_desc` for a game's price history, or pass `date` for one day's snapshot. Sort enum: `date_desc` (default), `date_asc`, `price_asc`, `price_desc`, `discount_desc`.
- **Params:** `app_id` (string, optional) — Exact Steam app id filter; `date` (string, optional) — Snapshot date filter yyyy-MM-dd; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `sort` (string, optional) — Sort enum: date_desc, date_asc, price_asc, price_desc, discount_desc

### `datasets_steam_reviews_search`

- **HTTP:** `GET /datasets/steam-reviews/search`
- **What:** Search the steam-reviews dataset. Searches the stored Steam review corpus (the most-helpful reviews per game; one document per appid × recommendation). Full-text `q` over the review body, filter by `app_id`, `language`, or `voted_up` (positive/negative). Sort enum: `votes_desc` (most-helpful first, default), `weighted_desc`, `date_desc`.
- **Params:** `app_id` (string, optional) — Exact Steam app id filter; `language` (string, optional) — Review language filter (e.g. english, schinese); `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over the review body, max 256 characters; `sort` (string, optional) — Sort enum: votes_desc, weighted_desc, date_desc; `voted_up` (string, optional) — Recommendation filter: true (positive) or false (negative)

### `datasets_techstack_facets`

- **HTTP:** `GET /datasets/techstack/facets`
- **What:** Facet the website tech-stack dataset. Returns distribution counts over the website tech-stack index (dataset id enum value `techstack`), honoring the same filters as search — the technology / category market-share view. Facet enum: `technology`, `category`, `cms`, `ecommerce`, `cdn`, `web_server`, `server_language`, `analytics`, `tld`, `render_tier`, `seed_source`.
- **Params:** `any_of` (array, optional) — Repeatable exact technology name; the site must use at least one (OR); `category` (string, optional) — Exact category filter, e.g. Ecommerce, CMS, Analytics; `cdn` (string, optional) — Exact CDN / hosting filter, e.g. Cloudflare, Fastly, Vercel; `cms` (string, optional) — Exact CMS filter, e.g. WordPress, Shopify, Webflow; `ecommerce` (string, optional) — Exact e-commerce platform filter, e.g. Shopify, WooCommerce, Magento; `facet` (string, **required**) — Facet enum: technology, category, cms, ecommerce, cdn, web_server, server_language, analytics, tld, render_tier, seed_source; `has_captcha` (boolean, optional) — true keeps only sites with a detected CAPTCHA; `min_tech_count` (integer, optional) — Minimum number of detected technologies, 0 or greater; `not` (array, optional) — Repeatable exact technology name the site must NOT use (excludes); `q` (string, optional) — Substring match on the site domain, max 256 characters; `reachable` (boolean, optional) — true keeps only sites whose homepage was fetched; `render_tier` (string, optional) — Fetch-tier filter. Enum: http, browser; `run_id` (string, optional) — Scan run id; defaults to the latest run; `seed_source` (string, optional) — Source filter for where the domain was discovered, e.g. tranco; `server_language` (string, optional) — Exact server language / framework filter, e.g. PHP, ASP.NET, Ruby on Rails; `technology` (array, optional) — Repeatable exact technology name the site MUST use (AND); `tld` (string, optional) — Exact top-level-domain filter, e.g. com, org, io; `web_server` (string, optional) — Exact web-server filter, e.g. nginx, Apache, IIS

### `datasets_techstack_item`

- **HTTP:** `GET /datasets/techstack/items/{domain}`
- **What:** Get a site from the website tech-stack dataset. Returns one site by its domain from dataset id enum value `techstack`, including every detected technology (name, categories, confidence, version, evidence) plus the CMS / e-commerce / CDN / web-server / server-language rollups. Returns 404 when the domain is not in the index.
- **Params:** `domain` (string, **required**) — Site domain, e.g. shopify.com (a scheme and www. are stripped)

### `datasets_techstack_search`

- **HTTP:** `GET /datasets/techstack/search`
- **What:** Search the website tech-stack dataset. Searches the website tech-stack index (dataset id enum value `techstack`) — one record per site listing the web technologies it is built with (frameworks, CMS, e-commerce, analytics, CDNs, servers, and more), BuiltWith / Wappalyzer-style. The reverse-index filters are the point: repeat `technology` to require several at once (AND), `any_of` to match at least one (OR), and `not` to exclude — e.g. sites on `Shopify` and `Klaviyo` but not `Recharge`. Sort enum: `relevance`, `rank_asc`, `tech_count_desc`, `domain_asc`, `crawled_desc`. render_tier enum: `http`, `browser`.
- **Params:** `any_of` (array, optional) — Repeatable exact technology name; the site must use at least one (OR); `category` (string, optional) — Exact category filter, e.g. Ecommerce, CMS, Analytics, Payment, CDN; `cdn` (string, optional) — Exact CDN / hosting filter, e.g. Cloudflare, Fastly, Vercel; `cms` (string, optional) — Exact CMS filter, e.g. WordPress, Shopify, Webflow; `ecommerce` (string, optional) — Exact e-commerce platform filter, e.g. Shopify, WooCommerce, Magento; `has_captcha` (boolean, optional) — true keeps only sites with a detected CAPTCHA; `min_tech_count` (integer, optional) — Minimum number of detected technologies, 0 or greater; `not` (array, optional) — Repeatable exact technology name the site must NOT use (excludes); `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Substring match on the site domain, max 256 characters; `reachable` (boolean, optional) — true keeps only sites whose homepage was fetched, false only sites that could not be fetched; `render_tier` (string, optional) — Fetch-tier filter. Enum: http, browser; `run_id` (string, optional) — Scan run id; defaults to the latest run; `seed_source` (string, optional) — Source filter for where the domain was discovered, e.g. tranco; `server_language` (string, optional) — Exact server language / framework filter, e.g. PHP, ASP.NET, Ruby on Rails; `sort` (string, optional) — Sort enum: relevance, rank_asc, tech_count_desc, domain_asc, crawled_desc; `technology` (array, optional) — Repeatable exact technology name the site MUST use (AND), e.g. technology=Shopify&technology=Klaviyo; `tld` (string, optional) — Exact top-level-domain filter, e.g. com, org, io; `web_server` (string, optional) — Exact web-server filter, e.g. nginx, Apache, IIS

### `datasets_trustmrr_facets`

- **HTTP:** `GET /datasets/trustmrr/facets`
- **What:** Facet the TrustMRR dataset. Returns terms-aggregation counts for one facet of the TrustMRR dataset, scoped to the same filters as search. Facet enum: `category`, `country`, `payment_provider`, `target_audience`, `business_type`, `tech`, `channels`, `listing_tier`, `status`, `on_sale`, `is_sponsored`, `tags`.
- **Params:** `category` (string, optional) — Exact category filter, max 128 characters; `country` (string, optional) — Exact ISO country-code filter, max 128 characters; `facet` (string, **required**) — Facet enum: category, country, payment_provider, target_audience, business_type, tech, channels, listing_tier, status, on_sale, is_sponsored, tags; `min_mrr` (number, optional) — Minimum verified MRR in USD; `on_sale` (boolean, optional) — Filter for startups currently listed for sale; `payment_provider` (string, optional) — Payment-provider filter, max 128 characters; `q` (string, optional) — Full-text query, max 256 characters

### `datasets_trustmrr_history`

- **HTTP:** `GET /datasets/trustmrr/history/{slug}`
- **What:** Get a TrustMRR startup's daily history. Returns a startup's daily time-series of payment-provider-verified metrics — MRR, all-time revenue, last-30-days revenue, 30-day and 12-month traffic, 30-day growth, for-sale flag, asking price, valuation multiple, deal score and offer count — one point per day in chronological order (oldest first). The series accrues one point per calendar day, so a recently discovered startup returns a short or empty series rather than a 404.
- **Params:** `from` (string, optional) — Inclusive start date, YYYY-MM-DD (UTC); `limit` (integer, optional) — Maximum points returned (the most recent within the range), default 365, max 1000; `slug` (string, **required**) — Startup slug, max 128 characters; `to` (string, optional) — Inclusive end date, YYYY-MM-DD (UTC)

### `datasets_trustmrr_item`

- **HTTP:** `GET /datasets/trustmrr/items/{slug}`
- **What:** Get a TrustMRR startup from the dataset. Returns one startup record by slug from the TrustMRR dataset (dataset id `trustmrr`), including verified revenue/MRR, traffic, growth, category, tech stack, marketing channels and acquisition-marketplace fields.
- **Params:** `slug` (string, **required**) — Startup slug, max 128 characters

### `datasets_trustmrr_search`

- **HTTP:** `GET /datasets/trustmrr/search`
- **What:** Search the TrustMRR dataset. Searches public startups with payment-provider-verified revenue and MRR, stored in a search index. Filter by category, country, payment provider, target audience, tech, marketing channel, listing tier and for-sale status, and by revenue/MRR/traffic/growth/multiple/asking-price ranges. Sort enum: `relevance`, `mrr_desc`, `revenue_desc`, `revenue_30d_desc`, `traffic_desc`, `growth_desc`, `deal_score_desc`, `price_asc`, `price_desc`, `multiple_asc`, `founded_desc`. status enum: `active`, `removed`.
- **Params:** `business_type` (string, optional) — Business-type filter (e.g. B2B, B2C), max 128 characters; `category` (string, optional) — Exact category filter (e.g. SaaS, Artificial Intelligence, Mobile Apps), max 128 characters; `channel` (string, optional) — Detected marketing-channel slug filter (e.g. meta-ads, seo), max 128 characters; `country` (string, optional) — Exact ISO country-code filter (e.g. US), max 128 characters; `is_sponsored` (boolean, optional) — Filter for sponsored (paid-placement) listings; `listing_tier` (string, optional) — For-sale listing-tier filter (e.g. pro), max 128 characters; `max_asking_price` (number, optional) — Maximum asking price in USD; `max_mrr` (number, optional) — Maximum verified MRR in USD; `max_multiple` (number, optional) — Maximum asking-price-to-revenue multiple; `min_ahrefs_dr` (integer, optional) — Minimum Ahrefs Domain Rating; `min_asking_price` (number, optional) — Minimum asking price in USD; `min_growth` (number, optional) — Minimum 30-day revenue growth percentage; `min_mrr` (number, optional) — Minimum verified MRR in USD; `min_revenue` (number, optional) — Minimum verified all-time revenue in USD; `min_revenue_30d` (number, optional) — Minimum verified last-30-days revenue in USD; `min_traffic` (number, optional) — Minimum last-30-days traffic (visits); `on_sale` (boolean, optional) — Filter for startups currently listed for sale; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `payment_provider` (string, optional) — Payment-provider filter (e.g. stripe, revenuecat, superwall, creem), max 128 characters; `q` (string, optional) — Full-text query over name, description, seller message and business summary, max 256 characters; `slug` (string, optional) — Exact startup slug filter, max 128 characters; `sort` (string, optional) — Sort enum: relevance, mrr_desc, revenue_desc, revenue_30d_desc, traffic_desc, growth_desc, deal_score_desc, price_asc, price_desc, multiple_asc, founded_desc; `status` (string, optional) — Lifecycle enum: active, removed; `target_audience` (string, optional) — Target-audience filter (e.g. B2B, B2C), max 128 characters; `tech` (string, optional) — Detected tech-stack slug filter (e.g. nextjs, reactnative), max 128 characters

### `datasets_x_users_facets`

- **HTTP:** `GET /datasets/x-users/facets`
- **What:** Facet the X users dataset. Returns terms aggregation counts for the X users dataset. Facet enum: `is_blue_verified`, `has_bio`, `has_external_url`, `source_tier`.
- **Params:** `crawled_after` (string, optional) — Records last refreshed on or after this date (RFC3339 or YYYY-MM-DD); `crawled_before` (string, optional) — Records last refreshed on or before this date (RFC3339 or YYYY-MM-DD); `created_after` (string, optional) — Accounts created on or after this date (RFC3339 or YYYY-MM-DD); `created_before` (string, optional) — Accounts created on or before this date (RFC3339 or YYYY-MM-DD); `facet` (string, **required**) — Facet enum: is_blue_verified, has_bio, has_external_url, source_tier; `has_bio` (boolean, optional) — Filter by a non-empty profile bio; `has_external_url` (boolean, optional) — Filter by a linked external URL; `is_blue_verified` (boolean, optional) — Filter by the X blue-check verification flag; `max_followers` (integer, optional) — Maximum follower count; `max_ratio` (number, optional) — Maximum follower-to-following ratio; `min_followers` (integer, optional) — Minimum follower count; `min_ratio` (number, optional) — Minimum follower-to-following ratio; `q` (string, optional) — Full-text query over username, name, bio and location, max 256 characters; `sort` (string, optional) — Sort enum: relevance, followers_desc, followers_asc, crawled_at_desc, crawled_at_asc, created_at_desc, created_at_asc; `source_tier` (string, optional) — Exact filter for which seed tier discovered this account; `username` (string, optional) — Exact username filter (case-insensitive), max 128 characters

### `datasets_x_users_item`

- **HTTP:** `GET /datasets/x-users/items/{username}`
- **What:** Get an X user from the dataset. Returns one X user record by username from dataset id enum value `x-users`.
- **Params:** `username` (string, **required**) — X username, with or without a leading @, max 128 characters

### `datasets_x_users_search`

- **HTTP:** `GET /datasets/x-users/search`
- **What:** Search the X users dataset. Searches public X (Twitter) user profiles stored in a search index. Sort enum: `relevance`, `followers_desc`, `followers_asc`, `crawled_at_desc`, `crawled_at_asc`, `created_at_desc`, `created_at_asc`.
- **Params:** `crawled_after` (string, optional) — Records last refreshed on or after this date (RFC3339 or YYYY-MM-DD); `crawled_before` (string, optional) — Records last refreshed on or before this date (RFC3339 or YYYY-MM-DD); `created_after` (string, optional) — Accounts created on or after this date (RFC3339 or YYYY-MM-DD); `created_before` (string, optional) — Accounts created on or before this date (RFC3339 or YYYY-MM-DD); `has_bio` (boolean, optional) — Filter by a non-empty profile bio; `has_external_url` (boolean, optional) — Filter by a linked external URL; `is_blue_verified` (boolean, optional) — Filter by the X blue-check verification flag; `max_followers` (integer, optional) — Maximum follower count; `max_ratio` (number, optional) — Maximum follower-to-following ratio; `min_followers` (integer, optional) — Minimum follower count; `min_ratio` (number, optional) — Minimum follower-to-following ratio (low values surface follow-spam / bot-like accounts); `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over username, name, bio and location, max 256 characters; `sort` (string, optional) — Sort enum: relevance, followers_desc, followers_asc, crawled_at_desc, crawled_at_asc, created_at_desc, created_at_asc; `source_tier` (string, optional) — Exact filter for which seed tier discovered this account, e.g. github-users, wikidata, tiktok-creators, journalists; `username` (string, optional) — Exact username filter (case-insensitive), max 128 characters

## Depop (4)

### `depop_categories`

- **HTTP:** `GET /depop/categories`
- **What:** Get Depop's category taxonomy. Returns Depop's full department, category, and subcategory taxonomy -- every value usable with /depop/search's and /depop/shop/{username}'s category/subcategory filters. Static data, no live request.
- **Params:** _none_

### `depop_item`

- **HTTP:** `GET /depop/item/{slug}`
- **What:** Get Depop item detail. Returns a normalized Depop item-detail page: description, all photos, price, condition, brand, size, seller info, and a "similar items" carousel when the page has one. Public data sourced from Depop's own item pages.
- **Params:** `slug` (string, **required**) — Depop item URL slug, e.g. from a search result's id field

### `depop_search`

- **HTTP:** `GET /depop/search`
- **What:** Search Depop listings. Searches Depop's resale-fashion marketplace by free-text keyword, with optional price, condition, colour, category, subcategory, gender, brand, discount, and sort filters, returning normalized listing summaries (title, price, brand, condition, photos, sizes), a pagination cursor, and the total matching count. Public data sourced from Depop's own search API.
- **Params:** `after` (string, optional) — Opaque pagination cursor from a previous response's next_cursor field. Omit for the first page.; `brand_ids` (string, optional) — Comma-separated Depop internal numeric brand ids. Not documented by Depop -- find a brand's id by browsing its depop.com/brands/<slug>/ page.; `category` (string, optional) — Depop category slug: tops, bottoms, dresses, coats-jackets, jumpsuit-and-playsuit, suits, footwear, accessories, nightwear, underwear, swim-beach-wear, fancy-dress, sleepsuits-and-bodysuits, bundles, beauty, face-masks, home, tech-accessories, film, art, books-and-magazine, music, party-supplies, sports-equipment-accesories, toys, umbrella. See GET /depop/categories for a machine-readable enumeration with names and subcategories.; `colours` (string, optional) — Comma-separated colour filter: black, grey, white, brown, tan, cream, yellow, red, burgundy, orange, pink, purple, blue, navy, green, khaki, multi; `condition` (string, optional) — Comma-separated condition filter: brand_new, used_like_new, used_excellent, used_good, used_fair; `gender` (string, optional) — Department filter: female, male; `on_sale` (boolean, optional) — Restrict results to discounted listings; `price_max` (number, optional) — Maximum listing price in USD; `price_min` (number, optional) — Minimum listing price in USD; `query` (string, **required**) — Free-text keyword search; `sort` (string, optional) — Sort order: relevance, price_low_to_high, price_high_to_low; `subcategory` (string, optional) — Comma-separated Depop subcategory slug(s), scoped within category. See GET /depop/categories for the full list per category.

### `depop_shop`

- **HTTP:** `GET /depop/shop/{username}`
- **What:** Get a Depop seller's shop. Returns a Depop seller's public shop: profile (rating, sold count, followers, bio) plus current listings, with optional price, condition, colour, category, subcategory, gender, discount, and sort filters. Public data sourced from Depop's own shop pages.
- **Params:** `category` (string, optional) — Depop category slug: tops, bottoms, dresses, coats-jackets, jumpsuit-and-playsuit, suits, footwear, accessories, nightwear, underwear, swim-beach-wear, fancy-dress, sleepsuits-and-bodysuits, bundles, beauty, face-masks, home, tech-accessories, film, art, books-and-magazine, music, party-supplies, sports-equipment-accesories, toys, umbrella. See GET /depop/categories for a machine-readable enumeration with names and subcategories.; `colours` (string, optional) — Comma-separated colour filter: black, grey, white, brown, tan, cream, yellow, red, burgundy, orange, pink, purple, blue, navy, green, khaki, multi; `condition` (string, optional) — Comma-separated condition filter: brand_new, used_like_new, used_excellent, used_good, used_fair; `gender` (string, optional) — Department filter: female, male; `on_sale` (boolean, optional) — Restrict results to discounted listings; `price_max` (number, optional) — Maximum listing price in USD; `price_min` (number, optional) — Minimum listing price in USD; `sort` (string, optional) — Sort order: relevance, price_low_to_high, price_high_to_low, recently_listed; `subcategory` (string, optional) — Comma-separated Depop subcategory slug(s), scoped within category. See GET /depop/categories for the full list per category.; `username` (string, **required**) — Depop seller username, e.g. from a shop page URL segment

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

## DoorDash (12)

### `doordash_explore`

- **HTTP:** `GET /doordash/explore`
- **What:** Get DoorDash nearby stores explore feed. Returns DoorDash's location-based "nearby stores" browse feed from the Android mobile guest experience. Unlike search or autocomplete, no search query is required. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Consumer latitude; `longitude` (number, **required**) — Consumer longitude

### `doordash_feed`

- **HTTP:** `GET /doordash/feed`
- **What:** Get DoorDash store discovery feed. Returns nearby trending restaurants, grocery stores, and promotional offers from the Android mobile guest experience for a location. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Consumer latitude; `limit` (integer, optional) — Max stores to return; `longitude` (number, **required**) — Consumer longitude; `offset` (integer, optional) — Feed offset

### `doordash_search`

- **HTTP:** `GET /doordash/search`
- **What:** Search DoorDash pickup restaurants. Searches the Android mobile guest catalog for pickup restaurants near a location and supports optional result filters. No DoorDash account or caller-supplied token is required.
- **Params:** `asapOnly` (boolean, optional) — Keep only stores currently available ASAP; `dashPassOnly` (boolean, optional) — Keep only DashPass-eligible stores; `latitude` (number, **required**) — Consumer latitude; `longitude` (number, **required**) — Consumer longitude; `maxDistanceMiles` (number, optional) — Maximum displayed distance in miles, from 0 to 100; `pickupOnly` (boolean, optional) — Keep only pickup-enabled stores; `query` (string, **required**) — Restaurant, cuisine, or dish query; `tag` (string, optional) — Exact cuisine or store tag, case-insensitive

### `doordash_search_autocomplete`

- **HTTP:** `GET /doordash/search/autocomplete`
- **What:** Get DoorDash pickup search suggestions. Returns pickup restaurant matches from the Android mobile guest search experience near a location. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Consumer latitude; `longitude` (number, **required**) — Consumer longitude; `query` (string, **required**) — Partial restaurant, cuisine, or dish query

### `doordash_search_filters`

- **HTTP:** `GET /doordash/search/filters`
- **What:** Get DoorDash search filter options. Returns the cuisines and filter values supported by the Android mobile guest search experience for a location. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Consumer latitude; `longitude` (number, **required**) — Consumer longitude

### `doordash_search_items`

- **HTTP:** `GET /doordash/search/items`
- **What:** Search DoorDash dishes and items. Search for specific dishes or items across nearby merchants from the Android mobile guest experience. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Consumer latitude; `longitude` (number, **required**) — Consumer longitude; `query` (string, **required**) — Search text

### `doordash_store`

- **HTTP:** `GET /doordash/store/{store_id}`
- **What:** Get a DoorDash store. Returns location-aware DoorDash store metadata through the Android mobile guest flow. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

### `doordash_store_fulfillment`

- **HTTP:** `GET /doordash/store/{store_id}/fulfillment`
- **What:** Get DoorDash store fulfillment details. Returns store fulfillment methods, delivery fee info, and scheduling details from the Android mobile guest experience. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

### `doordash_store_info`

- **HTTP:** `GET /doordash/store/{store_id}/info`
- **What:** Get DoorDash store contact info. Returns a lightweight store info card (map coordinates, address, phone number) from the Android mobile guest experience. This is a distinct upstream contract from the full store endpoint and reliably includes address and coordinates. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

### `doordash_store_item`

- **HTTP:** `GET /doordash/store/{store_id}/item/{item_id}`
- **What:** Get DoorDash menu item details. Returns details for a specific menu item from the Android mobile guest experience. No DoorDash account or caller-supplied token is required.
- **Params:** `item_id` (string, **required**) — Menu item ID or name; `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

### `doordash_store_menu`

- **HTTP:** `GET /doordash/store/{store_id}/menu`
- **What:** Get a DoorDash store menu. Returns the location-aware DoorDash mobile menu, grouped into sections with item names, descriptions, and displayed prices. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

### `doordash_store_reviews`

- **HTTP:** `GET /doordash/store/{store_id}/reviews`
- **What:** Get DoorDash store reviews. Returns store ratings and customer reviews from the Android mobile guest experience for a location. No DoorDash account or caller-supplied token is required.
- **Params:** `latitude` (number, **required**) — Delivery latitude; `longitude` (number, **required**) — Delivery longitude; `store_id` (string, **required**) — Numeric DoorDash store ID

## DuckDuckGo Search (5)

### `duckduckgo_image`

- **HTTP:** `GET /duckduckgo/image`
- **What:** Search DuckDuckGo image results. Returns normalized DuckDuckGo image results for a query string: title, source page URL, image URL, thumbnail, dimensions, and hostname, plus page-based pagination. Results are fetched from DuckDuckGo's own image JSON API.
- **Params:** `page` (integer, optional) — 1-based page number, defaults to 1; `q` (string, **required**) — Search query; `region` (string, optional) — DuckDuckGo region/locale code, e.g. us-en, uk-en, wt-wt (worldwide, the default)

### `duckduckgo_news`

- **HTTP:** `GET /duckduckgo/news`
- **What:** Search DuckDuckGo news results. Returns normalized DuckDuckGo news results for a query string: title, destination URL, source, excerpt, thumbnail, and relative/published time, plus page-based pagination. Results are fetched from DuckDuckGo's own news JSON API.
- **Params:** `page` (integer, optional) — 1-based page number, defaults to 1; `q` (string, **required**) — Search query; `region` (string, optional) — DuckDuckGo region/locale code, e.g. us-en, uk-en, wt-wt (worldwide, the default)

### `duckduckgo_search`

- **HTTP:** `GET /duckduckgo/search`
- **What:** Search DuckDuckGo web results. Returns normalized DuckDuckGo web search results for a query string: title, destination URL, description, and hostname, plus page-based pagination. DuckDuckGo wraps every result link in its own click-tracking redirect; this endpoint always returns the decoded destination URL, never the raw redirect link. Results are fetched from DuckDuckGo's own server-rendered search page.
- **Params:** `page` (integer, optional) — 1-based page number, defaults to 1; `q` (string, **required**) — Search query; `region` (string, optional) — DuckDuckGo region/locale code, e.g. us-en, uk-en, wt-wt (worldwide, the default); `safe_search` (string, optional) — Safe search level, defaults to DuckDuckGo's own moderate setting when omitted; `time_range` (string, optional) — Restrict results to a recency window

### `duckduckgo_shopping`

- **HTTP:** `GET /duckduckgo/shopping`
- **What:** Search DuckDuckGo shopping results. Returns normalized DuckDuckGo shopping results for a query string: title, brand, merchant, description, price, rating, and review count, plus total page count. DuckDuckGo's shopping vertical is ad-funded, syndicated product listings, not organic content; every product link is wrapped in an ad-click-tracking redirect with no clean destination to unwrap, so no destination URL is returned. DuckDuckGo's own pagination token for this vertical is an opaque per-response blob rather than a plain page offset, so only the first page is supported.
- **Params:** `q` (string, **required**) — Search query; `region` (string, optional) — DuckDuckGo market code, e.g. us-en, uk-en

### `duckduckgo_video`

- **HTTP:** `GET /duckduckgo/video`
- **What:** Search DuckDuckGo video results. Returns normalized DuckDuckGo video results for a query string: title, destination URL, description, duration, thumbnail, publisher/uploader, published time, and view count, plus page-based pagination. Results are fetched from DuckDuckGo's own video JSON API.
- **Params:** `page` (integer, optional) — 1-based page number, defaults to 1; `q` (string, **required**) — Search query; `region` (string, optional) — DuckDuckGo region/locale code, e.g. us-en, uk-en, wt-wt (worldwide, the default)

## eBay (6)

### `ebay_item`

- **HTTP:** `GET /ebay/item/{item_id}`
- **What:** Get eBay item details. Returns normalized details for a public eBay item listing.
- **Params:** `item_id` (string, **required**) — eBay item ID

### `ebay_search`

- **HTTP:** `POST /ebay/search`
- **What:** Search eBay listings. Returns normalized eBay search results.
- **Params:** `option` (object, **required**) — eBay search payload

### `ebay_seller`

- **HTTP:** `GET /ebay/seller/{seller}`
- **What:** Get eBay seller profile. Returns normalized details for a public eBay seller profile.
- **Params:** `seller` (string, **required**) — eBay seller username

### `ebay_seller_about`

- **HTTP:** `GET /ebay/seller/{seller}/about`
- **What:** Get eBay seller about details. Returns normalized seller about information from the public eBay store about tab, including seller stats, top-rated status, optional location/member-since fields, and cleaned store categories.
- **Params:** `seller` (string, **required**) — eBay seller username

### `ebay_seller_feedback`

- **HTTP:** `GET /ebay/seller/{seller}/feedback`
- **What:** Get eBay seller feedback. Returns normalized seller feedback summary, detailed ratings, and recent review cards from the public eBay seller feedback tab.
- **Params:** `page` (integer, optional) — Feedback page number; `per_page` (integer, optional) — Reviews per page; `seller` (string, **required**) — eBay seller username

### `ebay_seller_shop`

- **HTTP:** `GET /ebay/seller/{seller}/shop`
- **What:** Get eBay seller shop listings. Returns normalized listings from the public eBay seller shop tab, with pagination backed by the store odtRefresh response.
- **Params:** `page` (integer, optional) — Shop page number; `seller` (string, **required**) — eBay seller username

## ESPN (9)

### `espn_athlete`

- **HTTP:** `GET /espn/athlete`
- **What:** ESPN athlete. Returns one athlete's bio/overview (name, position, jersey, physicals, current team) from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `athlete` (string, **required**) — Numeric ESPN athlete (player) id; `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

### `espn_game_summary`

- **HTTP:** `GET /espn/game-summary`
- **What:** ESPN game summary. Returns one game's matchup, betting odds, and boxscore stat totals from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport. Get an `event` id from the scoreboard endpoint.
- **Params:** `event` (string, **required**) — Numeric ESPN event (game) id; `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

### `espn_news`

- **HTTP:** `GET /espn/news`
- **What:** ESPN league news. Returns recent news articles (headline, description, link) for a league from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

### `espn_rankings`

- **HTTP:** `GET /espn/rankings`
- **What:** ESPN poll rankings. Returns poll rankings (e.g. AP Top 25) for a college league from ESPN's credential-free public JSON. Rankings are only published for college leagues: the `sport` enum accepts `football` and `basketball`, and the `league` enum accepts `college-football`, `mens-college-basketball`, and `womens-college-basketball`.
- **Params:** `league` (string, **required**) — College league key; `sport` (string, **required**) — Sport key

### `espn_scoreboard`

- **HTTP:** `GET /espn/scoreboard`
- **What:** ESPN scoreboard. Returns games (scores, schedule, status, and odds when available) for a sport and league from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport. The `seasontype` enum accepts `1` (preseason), `2` (regular season), `3` (postseason), and `4` (offseason).
- **Params:** `dates` (string, optional) — Date or range as YYYYMMDD, YYYYMMDD-YYYYMMDD, or YYYY; defaults to the current scoreboard; `league` (string, **required**) — League key (must be valid for the sport); `seasontype` (integer, optional) — Season type; `sport` (string, **required**) — Sport key; `week` (integer, optional) — Week number (football leagues)

### `espn_standings`

- **HTTP:** `GET /espn/standings`
- **What:** ESPN standings. Returns league standings grouped by conference/division from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport. The `seasontype` enum accepts `1` (preseason), `2` (regular season), and `3` (postseason).
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `season` (integer, optional) — Four-digit season year; defaults to the current season; `seasontype` (integer, optional) — Season type; `sport` (string, **required**) — Sport key

### `espn_team`

- **HTTP:** `GET /espn/team`
- **What:** ESPN team detail. Returns one team's detail (identity, colors, record, standing summary) from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key; `team` (string, **required**) — Team id (numeric) or abbreviation

### `espn_team_roster`

- **HTTP:** `GET /espn/team-roster`
- **What:** ESPN team roster. Returns a team's roster (players with position, jersey, age, and experience) plus head coach from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key; `team` (string, **required**) — Team id (numeric) or abbreviation

### `espn_teams`

- **HTTP:** `GET /espn/teams`
- **What:** ESPN team list. Returns the full team list for a sport and league from ESPN's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, `baseball`, `hockey`, and `soccer`. The `league` enum accepts `nfl`, `college-football`, `nba`, `wnba`, `mens-college-basketball`, `womens-college-basketball`, `mlb`, `nhl`, `eng.1`, `esp.1`, `ita.1`, `ger.1`, `fra.1`, `usa.1`, and `uefa.champions`; it must be valid for the chosen sport.
- **Params:** `league` (string, **required**) — League key (must be valid for the sport); `sport` (string, **required**) — Sport key

## Etsy (7)

### `etsy_listing`

- **HTTP:** `GET /etsy/listing/{id}`
- **What:** Get Etsy listing detail. Returns Etsy listing detail: title, price, images, materials, tags, and shop.
- **Params:** `id` (string, **required**) — Numeric Etsy listing id

### `etsy_listing_reviews`

- **HTTP:** `GET /etsy/listing/{id}/reviews`
- **What:** Get Etsy listing reviews. Returns buyer reviews for an Etsy listing.
- **Params:** `id` (string, **required**) — Numeric Etsy listing id; `offset` (integer, optional) — 0-based review offset; `sort` (string, optional) — Review sort order

### `etsy_search`

- **HTTP:** `GET /etsy/search`
- **What:** Search Etsy listings. Returns Etsy product search results across shops for a keyword query.
- **Params:** `limit` (integer, optional) — Page size (default 36, max 100); `offset` (integer, optional) — 0-based result offset; `q` (string, **required**) — Search keywords

### `etsy_shop`

- **HTTP:** `GET /etsy/shop/{id}`
- **What:** Get Etsy shop profile. Returns an Etsy shop profile: seller, headline, rating, and sold count. Accepts a numeric shop id or a shop name.
- **Params:** `id` (string, **required**) — Numeric Etsy shop id or shop name

### `etsy_shop_listings`

- **HTTP:** `GET /etsy/shop/{id}/listings`
- **What:** Get an Etsy shop's listings. Returns a shop's listing catalog, optionally filtered by keyword. Accepts a numeric shop id or a shop name.
- **Params:** `id` (string, **required**) — Numeric Etsy shop id or shop name; `limit` (integer, optional) — Page size (default 24); `offset` (integer, optional) — 0-based listing offset; `q` (string, optional) — Keyword filter within the shop's own catalog

### `etsy_shop_reviews`

- **HTTP:** `GET /etsy/shop/{id}/reviews`
- **What:** Get Etsy shop reviews. Returns buyer reviews for an Etsy shop. Accepts a numeric shop id or a shop name.
- **Params:** `id` (string, **required**) — Numeric Etsy shop id or shop name; `limit` (integer, optional) — Page size (default 14); `offset` (integer, optional) — 0-based review offset

### `etsy_shop_search`

- **HTTP:** `GET /etsy/shop/search`
- **What:** Search Etsy shops. Returns Etsy shops matching a keyword.
- **Params:** `limit` (integer, optional) — Max shops to return (default 10); `q` (string, **required**) — Shop search keyword

## Expedia (7)

### `expedia_activities_search`

- **HTTP:** `POST /expedia/activities/search`
- **What:** Search Expedia activities. Returns normalized Expedia Things To Do (activities/tours) search results for a free-text destination and date range.
- **Params:** `option` (object, **required**) — Activity search payload

### `expedia_flights_search`

- **HTTP:** `POST /expedia/flights/search`
- **What:** Search Expedia flights. Returns normalized Expedia Flights search results (departing-leg offers) for an origin/destination IATA pair and date range.
- **Params:** `option` (object, **required**) — Flights search payload

### `expedia_locations_search`

- **HTTP:** `POST /expedia/locations/search`
- **What:** Search Expedia destinations. Returns normalized destination/property typeahead suggestions (cities, airports, neighborhoods, hotels) for a free-text term.
- **Params:** `option` (object, **required**) — Location search payload

### `expedia_properties_detail`

- **HTTP:** `POST /expedia/properties/detail`
- **What:** Expedia Stays property detail. Returns a hotel's detail summary (name, star rating, address/coordinates, top amenities) for a known property id.
- **Params:** `option` (object, **required**) — Property detail payload

### `expedia_properties_filters`

- **HTTP:** `POST /expedia/properties/filters`
- **What:** Expedia search filters. Returns the sort and filter facets (amenities, star rating, neighborhood, nightly price range, sort options) available for a Stays search.
- **Params:** `option` (object, **required**) — Property filters payload

### `expedia_properties_reviews`

- **HTTP:** `POST /expedia/properties/reviews`
- **What:** Expedia Stays property guest reviews. Returns a hotel's overall rating and highlighted/recent guest reviews (reviewer, date, rating, message) for a known property id.
- **Params:** `option` (object, **required**) — Property reviews payload

### `expedia_properties_search`

- **HTTP:** `POST /expedia/properties/search`
- **What:** Search Expedia Stays properties. Returns normalized Expedia Stays (hotel) search results for a free-text destination and date range.
- **Params:** `option` (object, **required**) — Property search payload

## Facebook (2)

### `facebook_marketplace_search`

- **HTTP:** `GET /facebook/marketplace/search`
- **What:** Search Facebook Marketplace. Fetches Facebook Marketplace search or browse results for a location: listing id, title, price, city/state, and a thumbnail image per result. Only the first page Facebook's own server-rendered results page returns is available — Facebook's own further pagination requires a logged-in session and is out of scope. Omit both query and category to get the location's browse feed instead of running a search. minPrice, maxPrice, sortBy, daysSinceListed, and condition only take effect alongside a query or category (Facebook itself ignores them on the plain browse feed), except for the property_rentals category, which has its own always-filtered listing page. This endpoint can take noticeably longer than other search endpoints (up to roughly a minute in the slowest case) as it retries to get past an intermittent upstream condition; priced accordingly.
- **Params:** `category` (string, optional) — Marketplace category; `condition` (string, optional) — Comma-separated listing conditions; requires query or category; `days_since_listed` (integer, optional) — Restrict to listings posted within this many days; requires query or category; `location` (string, **required**) — Facebook Marketplace location vanity slug; `max_price` (integer, optional) — Maximum price in whole currency units; requires query or category; `min_price` (integer, optional) — Minimum price in whole currency units; requires query or category; `query` (string, optional) — Free-text search terms; omit (with category) for the location's browse feed; `sort_by` (string, optional) — Result order; requires query or category

### `facebook_page`

- **HTTP:** `GET /facebook/{page}`
- **What:** Get Facebook page details. Fetches public data about a Facebook Page given its page ID, vanity name, or full page URL: name, follower/like counts, intro, category, business hours/price range, review count, and any public contact details (email, phone, address, website, WhatsApp number) exposed on the Page's About tab.
- **Params:** `page` (string, **required**) — Facebook Page reference: vanity name, handle, profile.php id, or full Facebook URL

## Fiverr (3)

### `fiverr_gig`

- **HTTP:** `GET /fiverr/gig/{username}/{slug}`
- **What:** Get Fiverr gig detail. Returns a normalized Fiverr gig detail page: title, description, category, pricing packages (basic/standard/premium tiers with price and delivery time), rating, review count, orders in queue, tags, gallery images, and a seller summary (level, rating, response time, languages). Public data sourced from Fiverr's own server-rendered gig pages via a real browser-rendering backend.
- **Params:** `slug` (string, **required**) — Fiverr gig URL slug, the trailing path segment after the username in a gig URL; `username` (string, **required**) — Fiverr seller username, e.g. from a search result's seller_username field

### `fiverr_search`

- **HTTP:** `GET /fiverr/search`
- **What:** Search Fiverr gigs. Searches Fiverr's public gig listings by free-text keyword, returning normalized gig summaries (title, seller username, seller level, rating, review count, starting price, category, thumbnail image). Public data sourced from Fiverr's own server-rendered search pages via a real browser-rendering backend.
- **Params:** `page` (integer, optional) — 1-based result page. Defaults to 1.; `q` (string, **required**) — Free-text gig search keyword

### `fiverr_seller`

- **HTTP:** `GET /fiverr/seller/{username}`
- **What:** Get Fiverr seller profile. Returns a normalized Fiverr seller profile: display name, one-liner title, description, country, seller level, verification status, hourly rate, spoken languages, join date, and the seller's gig ids. Public data sourced from Fiverr's own server-rendered seller profile pages via a real browser-rendering backend.
- **Params:** `username` (string, **required**) — Fiverr seller username, e.g. from a search result's seller_username field

## Geocoding (3)

### `geocoding_lookup`

- **HTTP:** `GET /geocoding/lookup`
- **What:** Lookup Nominatim OSM ids. Returns typed Nominatim JSONv2 places for comma-separated OSM ids such as W34633854,N123,R456.
- **Params:** `accept_language` (string, optional) — Preferred result language, forwarded to Nominatim; `addressdetails` (boolean, optional) — Include address details, defaults to true; `extratags` (boolean, optional) — Include OSM extra tags; `namedetails` (boolean, optional) — Include multilingual name details; `osm_ids` (string, **required**) — Comma-separated OSM ids such as W34633854,N123,R456

### `geocoding_reverse`

- **HTTP:** `GET /geocoding/reverse`
- **What:** Reverse geocode coordinates. Returns the nearest typed Nominatim JSONv2 place for latitude and longitude.
- **Params:** `accept_language` (string, optional) — Preferred result language, forwarded to Nominatim; `addressdetails` (boolean, optional) — Include address details, defaults to true; `extratags` (boolean, optional) — Include OSM extra tags; `lat` (number, **required**) — Latitude; `lon` (number, **required**) — Longitude; `namedetails` (boolean, optional) — Include multilingual name details; `zoom` (integer, optional) — Nominatim address zoom, defaults to 18

### `geocoding_search`

- **HTTP:** `GET /geocoding/search`
- **What:** Search Nominatim places. Returns typed Nominatim JSONv2 forward geocoding results. Use either q or structured fields, not both.
- **Params:** `accept_language` (string, optional) — Preferred result language, forwarded to Nominatim; `addressdetails` (boolean, optional) — Include address details, defaults to true; `city` (string, optional) — Structured city; `country` (string, optional) — Structured country; `countrycodes` (string, optional) — Comma-separated ISO 3166-1 alpha-2 country filters; `county` (string, optional) — Structured county; `extratags` (boolean, optional) — Include OSM extra tags; `limit` (integer, optional) — Maximum results, defaults to 10 and clamps to 20; `namedetails` (boolean, optional) — Include multilingual name details; `postalcode` (string, optional) — Structured postal code; `q` (string, optional) — Free-text search query; `state` (string, optional) — Structured state; `street` (string, optional) — Structured street or house number

## GitHub (17)

### `github_org`

- **HTTP:** `GET /github/org/{org}`
- **What:** Retrieve a GitHub organization profile. Returns a public GitHub organization profile (company-side enrichment).
- **Params:** `org` (string, **required**) — GitHub organization login

### `github_org_repos`

- **HTTP:** `GET /github/org/{org}/repos`
- **What:** List a GitHub organization's public repositories. Returns a page of an organization's public repositories (company tech stack).
- **Params:** `direction` (string, optional) — Sort direction; `org` (string, **required**) — GitHub organization login; `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `sort` (string, optional) — Sort field; `type` (string, optional) — Repository type

### `github_repo`

- **HTTP:** `GET /github/repo/{owner}/{repo}`
- **What:** Retrieve a GitHub repository. Returns public detail for a single repository (the core project object).
- **Params:** `owner` (string, **required**) — Repository owner (user or org login); `repo` (string, **required**) — Repository name

### `github_repo_contributors`

- **HTTP:** `GET /github/repo/{owner}/{repo}/contributors`
- **What:** List a repository's contributors. Returns a page of a repository's contributors (who builds a project).
- **Params:** `owner` (string, **required**) — Repository owner (user or org login); `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `repo` (string, **required**) — Repository name

### `github_repo_forks`

- **HTTP:** `GET /github/repo/{owner}/{repo}/forks`
- **What:** List a repository's public forks. Returns a page of a repository's public forks (adopter signal).
- **Params:** `owner` (string, **required**) — Repository owner (user or org login); `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `repo` (string, **required**) — Repository name; `sort` (string, optional) — Sort order

### `github_repo_languages`

- **HTTP:** `GET /github/repo/{owner}/{repo}/languages`
- **What:** Retrieve a repository's language breakdown. Returns the language byte breakdown for a repository, sorted by bytes descending (tech fingerprint).
- **Params:** `owner` (string, **required**) — Repository owner (user or org login); `repo` (string, **required**) — Repository name

### `github_repo_releases`

- **HTTP:** `GET /github/repo/{owner}/{repo}/releases`
- **What:** List a repository's releases. Returns a page of a repository's releases (momentum/health signal).
- **Params:** `owner` (string, **required**) — Repository owner (user or org login); `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `repo` (string, **required**) — Repository name

### `github_search_repositories`

- **HTTP:** `GET /github/search/repositories`
- **What:** Search public GitHub repositories. Searches public GitHub repositories (market/competitive discovery). Unauthenticated search is rate limited to roughly 10 requests per minute.
- **Params:** `order` (string, optional) — Sort order; `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `q` (string, **required**) — GitHub repository search query; `sort` (string, optional) — Sort field

### `github_search_users`

- **HTTP:** `GET /github/search/users`
- **What:** Search public GitHub users. Searches public GitHub users (developer discovery). Unauthenticated search is rate limited to roughly 10 requests per minute.
- **Params:** `order` (string, optional) — Sort order; `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `q` (string, **required**) — GitHub user search query; `sort` (string, optional) — Sort field

### `github_trending`

- **HTTP:** `GET /github/trending`
- **What:** List trending GitHub repositories. Returns the repositories on GitHub's trending page (market discovery).
- **Params:** `language` (string, optional) — Programming language filter (e.g. go, python); `since` (string, optional) — Time window

### `github_trending_developers`

- **HTTP:** `GET /github/trending/developers`
- **What:** List trending GitHub developers. Returns the developers on GitHub's trending developers page (market discovery).
- **Params:** `language` (string, optional) — Programming language filter (e.g. go, python); `since` (string, optional) — Time window

### `github_user`

- **HTTP:** `GET /github/user/{username}`
- **What:** Retrieve a GitHub user profile. Returns a public GitHub user's profile plus user-published social links. Email is included only when the user has made it public on their profile.
- **Params:** `username` (string, **required**) — GitHub username

### `github_user_events`

- **HTTP:** `GET /github/user/{username}/events`
- **What:** List a GitHub user's recent public activity. Returns a page of a user's recent public events, normalized to type, repository, and timestamp (freshness signal).
- **Params:** `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `username` (string, **required**) — GitHub username

### `github_user_followers`

- **HTTP:** `GET /github/user/{username}/followers`
- **What:** List a GitHub user's followers. Returns a page of the public accounts following a GitHub user.
- **Params:** `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `username` (string, **required**) — GitHub username

### `github_user_following`

- **HTTP:** `GET /github/user/{username}/following`
- **What:** List who a GitHub user follows. Returns a page of the public accounts a GitHub user follows.
- **Params:** `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `username` (string, **required**) — GitHub username

### `github_user_pinned`

- **HTTP:** `GET /github/user/{username}/pinned`
- **What:** List a GitHub user's pinned repositories. Returns the repositories a user pinned on their public profile (showcase signal). Empty when the user pinned nothing.
- **Params:** `username` (string, **required**) — GitHub username

### `github_user_repos`

- **HTTP:** `GET /github/user/{username}/repos`
- **What:** List a GitHub user's public repositories. Returns a page of a user's public repositories (tech-stack signal).
- **Params:** `direction` (string, optional) — Sort direction; `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `sort` (string, optional) — Sort field; `type` (string, optional) — Repository type; `username` (string, **required**) — GitHub username

## Goodreads (10)

### `goodreads_author`

- **HTTP:** `GET /goodreads/author/{id}`
- **What:** Get a Goodreads author. Returns a normalized Goodreads author profile: bio, birth/death dates, website, genres, photo, and aggregate rating stats. Credential-free public Goodreads data.
- **Params:** `id` (string, **required**) — Goodreads author id

### `goodreads_author_books`

- **HTTP:** `GET /goodreads/author/{id}/books`
- **What:** List a Goodreads author's books. Returns an author's paginated works list (title, author, average rating, ratings count). Credential-free public Goodreads data.
- **Params:** `id` (string, **required**) — Goodreads author id; `page` (integer, optional) — 1-based page number, default 1

### `goodreads_author_quotes`

- **HTTP:** `GET /goodreads/author/{id}/quotes`
- **What:** List a Goodreads author's attributed quotes. Returns an author's paginated attributed-quotes list (quote text, tags, like count, and — when the quote is credited to a specific book — that book's title, id, and work id). Credential-free public Goodreads data.
- **Params:** `id` (string, **required**) — Goodreads author id; `page` (integer, optional) — 1-based page number, default 1

### `goodreads_book`

- **HTTP:** `GET /goodreads/book/{id}`
- **What:** Get a Goodreads book. Returns a normalized Goodreads book: description, authors, series, genres, format, pages, publisher, publication date, ISBNs, and aggregate rating with the full 1-5 star distribution. Credential-free public Goodreads data (goodreads.com), parsed from the book page's embedded GraphQL cache.
- **Params:** `id` (string, **required**) — Goodreads book id

### `goodreads_book_editions`

- **HTTP:** `GET /goodreads/book/{id}/editions`
- **What:** List a Goodreads book's editions. Returns a work's paginated edition list (per-edition book id, format, page count, publication date, publisher, ISBN/ISBN13/ASIN, language, and rating) — every other translation, printing, and format of the requested book id. Goodreads keys editions by a separate "work id", not the book id in the path, so this makes one extra internal request to resolve it; requests against a book with no editions data return an upstream error.
- **Params:** `id` (string, **required**) — Goodreads book id; `page` (integer, optional) — 1-based page number, default 1

### `goodreads_book_reviews`

- **HTTP:** `GET /goodreads/book/{id}/reviews`
- **What:** Get a Goodreads book's featured reviews. Returns a book's featured reviews (reviewer, rating, text, date, like/comment counts, spoiler flag), sorted by like count. Credential-free public Goodreads data.
- **Params:** `id` (string, **required**) — Goodreads book id; `limit` (integer, optional) — Max reviews, default 10, max 50

### `goodreads_genre`

- **HTTP:** `GET /goodreads/genre/{name}`
- **What:** Get a Goodreads genre shelf. Returns up to 50 books on a Goodreads genre/shelf tag page (e.g. fantasy, romance, science-fiction), Goodreads' credential-free per-tag "top books" view: title, author, average rating, ratings count, publication year, and how many times the book was shelved under this specific tag. Goodreads' genre/shelf taxonomy is an open, user-generated folksonomy of thousands of tags, not a small fixed list, so there is no directory endpoint — pass any known tag slug, e.g. from a book's genres[] field or a value seen on goodreads.com. There is no pagination beyond the first 50.
- **Params:** `name` (string, **required**) — Goodreads genre/shelf tag

### `goodreads_list`

- **HTTP:** `GET /goodreads/list/{id}`
- **What:** Get a Goodreads Listopia list. Returns a Goodreads Listopia list (ranked book list) by id, paginated. Credential-free public Goodreads data.
- **Params:** `id` (string, **required**) — Goodreads list id; `page` (integer, optional) — 1-based page number, default 1

### `goodreads_lists`

- **HTTP:** `GET /goodreads/lists`
- **What:** List curated Goodreads Listopia lists. Returns a curated, non-exhaustive catalog of well-known Goodreads Listopia lists (id, name, category) — Goodreads has no directory or search endpoint for the tens of thousands of user-created lists, so this is hand-picked and verified live, not derived from an upstream index. Pass a returned id to GET /goodreads/list/{id} for that list's ranked book contents. Category enum: `general`, `genre`, `era`, `young_adult`, `children`, `holiday`.
- **Params:** _none_

### `goodreads_search`

- **HTTP:** `GET /goodreads/search`
- **What:** Search Goodreads books. Searches Goodreads books by title/author. Credential-free public Goodreads data via the autocomplete endpoint (book results only).
- **Params:** `limit` (integer, optional) — Max results, default 10, max 50; `q` (string, **required**) — Search query

## Google (40)

### `google_finance_analyst_articles`

- **HTTP:** `GET /google/finance/analyst-articles/{quote}`
- **What:** Google Finance analyst articles. Returns normalized analyst article results for a quote.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_chart`

- **HTTP:** `GET /google/finance/chart/{quote}`
- **What:** Google Finance chart data. Returns normalized chart points for a quote and window.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ; `window` (string, optional) — Window: 1d, 5d, 1m, 6m, ytd, 1y, 5y, max

### `google_finance_classification`

- **HTTP:** `GET /google/finance/classification/{quote}`
- **What:** Google Finance classification data. Returns normalized classification strings for a quote.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_company`

- **HTTP:** `GET /google/finance/company/{quote}`
- **What:** Google Finance company data. Returns normalized company information from Google Finance.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_context`

- **HTTP:** `GET /google/finance/context`
- **What:** Google Finance context search. Returns normalized Google Finance context search results.
- **Params:** `q` (string, **required**) — Search query

### `google_finance_financials`

- **HTTP:** `GET /google/finance/financials/{quote}`
- **What:** Google Finance financial statements. Returns normalized annual and quarterly financial rows when Google Finance has statement data for the quote.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_markets_category_news`

- **HTTP:** `GET /google/finance/markets/categories/{category}/news`
- **What:** Google Finance category news. Returns normalized news for a Google Finance category.
- **Params:** `category` (string, **required**) — Google Finance category id; `offset` (integer, optional) — Result offset

### `google_finance_markets_category_stocks`

- **HTTP:** `GET /google/finance/markets/categories/{category}/stocks`
- **What:** Google Finance category stocks. Returns normalized instruments for a Google Finance category.
- **Params:** `category` (string, **required**) — Google Finance category id; `offset` (integer, optional) — Result offset

### `google_finance_markets_earnings`

- **HTTP:** `GET /google/finance/markets/earnings`
- **What:** Google Finance earnings calendar. Returns normalized earnings calendar instruments.
- **Params:** _none_

### `google_finance_markets_featured`

- **HTTP:** `GET /google/finance/markets/featured`
- **What:** Google Finance featured stocks. Returns normalized featured instruments.
- **Params:** _none_

### `google_finance_markets_headline`

- **HTTP:** `GET /google/finance/markets/headline`
- **What:** Google Finance top headline. Returns the top Google Finance headline.
- **Params:** _none_

### `google_finance_markets_indices`

- **HTTP:** `GET /google/finance/markets/indices`
- **What:** Google Finance market indices. Returns normalized market index instruments.
- **Params:** _none_

### `google_finance_markets_movers`

- **HTTP:** `GET /google/finance/markets/movers`
- **What:** Google Finance market movers. Returns normalized market mover instruments.
- **Params:** `categories` (string, optional) — Comma-separated numeric categories; `count` (integer, optional) — Result count; `offset` (integer, optional) — Result offset

### `google_finance_markets_top`

- **HTTP:** `GET /google/finance/markets/top`
- **What:** Google Finance top stocks by metric. Returns normalized top instruments for a Google Finance metric.
- **Params:** `metric` (integer, optional) — Google Finance metric id; `page` (integer, optional) — Page number

### `google_finance_markets_trending`

- **HTTP:** `GET /google/finance/markets/trending`
- **What:** Google Finance trending stocks. Returns normalized trending instruments.
- **Params:** `limit` (integer, optional) — Result limit

### `google_finance_news`

- **HTTP:** `GET /google/finance/news/{quote}`
- **What:** Google Finance quote news. Returns normalized news articles for a quote.
- **Params:** `limit` (integer, optional) — Article limit; `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_quote`

- **HTTP:** `GET /google/finance/quote/{quote}`
- **What:** Google Finance Quote API. Fetches the latest quote data for a provided stock symbol from Google Finance https://www.google.com/finance/quote/AAPL:NASDAQ?hl=en.
- **Params:** `quote` (string, **required**) — Stock symbol to fetch the latest quote for (e.g., AAPL:NASDAQ, BTC-USD)

### `google_finance_related`

- **HTTP:** `GET /google/finance/related/{quote}`
- **What:** Google Finance related instruments. Returns normalized related instruments for a quote.
- **Params:** `quote` (string, **required**) — Quote identifier such as AAPL:NASDAQ

### `google_finance_search`

- **HTTP:** `GET /google/finance/search`
- **What:** Google Finance Search API. Fetches normalized search results for a provided keyword from Google Finance.
- **Params:** `q` (string, **required**) — Keyword to search for (e.g., Apple)

### `google_finance_ticker`

- **HTTP:** `GET /google/finance/ticker/{ticker}`
- **What:** Google Finance Ticker API. Fetches chart ticker data from Google Finance based on a provided ticker and window period.
- **Params:** `ticker` (string, **required**) — Ticker symbol to fetch data for example:AAPL:NASDAQ, BTC-USD; `window` (string, optional) — Time window for the ticker data (default: 1d), options: 1d, 5d, 1m, 6m, 1y, 5y, max

### `google_jobs`

- **HTTP:** `POST /google/jobs`
- **What:** Search Google Jobs. Returns normalized Google Jobs results parsed from public Google web responses.
- **Params:** `option` (object, **required**) — Google Jobs search payload

### `google_map_place`

- **HTTP:** `GET /google/map/place/{place_id}`
- **What:** Google Maps place details API. Returns detailed information for a specified place_id. Rate limit is enforced at 1 request per second.
- **Params:** `place_id` (string, **required**) — Google Place ID

### `google_map_place_photos`

- **HTTP:** `GET /google/map/place/{place_id}/photos`
- **What:** Google Maps place photos API. Returns the photos Google publishes for a specified place_id — the imagery shown on the place's Google Maps page, typically dozens of images for a well-covered business. Each entry carries the image URL as served plus its pixel dimensions when reported; swap the trailing size suffix on the URL (e.g. `=w203-h100-k-no`) to request other dimensions. Contributor avatars and review-attached photos are excluded. This is the place page's image set, not a paginated archive feed. Rate limit is enforced at 1 request per second.
- **Params:** `limit` (integer, optional) — Maximum number of photos to return. Omit or 0 for all captured.; `place_id` (string, **required**) — Google Place ID

### `google_map_place_reviews`

- **HTTP:** `GET /google/map/place/{place_id}/reviews`
- **What:** Google Maps place reviews API. Returns the reviews Google shows on a specified place_id's Google Maps page — typically the 8 most relevant, each with its rating, text, reviewer, timestamp, and any photos the reviewer attached. Photo-only reviews return an empty `text`. This is the place page's first page of reviews, not the full review archive. Rate limit is enforced at 1 request per second.
- **Params:** `limit` (integer, optional) — Maximum number of reviews to return. Omit or 0 for all captured.; `place_id` (string, **required**) — Google Place ID

### `google_map_search`

- **HTTP:** `POST /google/map/search`
- **What:** Google Maps search API. Returns results from Google Maps based on search options. Rate limit is enforced at 1 request per second.
- **Params:** `mapSearchOption` (object, **required**) — Search options

### `google_news`

- **HTTP:** `GET /google/news`
- **What:** Search Google News. Returns normalized Google News vertical results (title, source, link, age) parsed from the public Google News results page. Locale defaults to country=us and lang=en. Returns 503 when Google serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Google UI language; defaults to en; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

### `google_search`

- **HTTP:** `POST /google/search`
- **What:** Google search API. Returns normalized Google web search results. Results are fetched through proxied browser renderers that race several concurrent renders per request and return the first clean result, with stale-cache fallback when available. The endpoint returns 503 when Google serves a challenge page or unusable HTML. Rate limit is enforced at 1 request per second, and if the limit is exceeded a 429 status code is returned with rate limit headers.
- **Params:** `searchOption` (object, **required**) — Search options

### `google_suggest`

- **HTTP:** `GET /google/suggest`
- **What:** Suggest Google search queries. Returns Google autosuggest query completions from the public unauthenticated suggest JSON endpoint.
- **Params:** `count` (integer, optional) — Suggestions to return; defaults to 10, clamped to 1..12; `country` (string, optional) — Google result country; defaults to us; `lang` (string, optional) — Google UI language; defaults to en; `q` (string, **required**) — Search query prefix

### `google_trends_categories`

- **HTTP:** `GET /google/trends/categories`
- **What:** Google Trends categories. Returns supported top-level Google Trends category ids and labels for Trending Now category filters.
- **Params:** _none_

### `google_trends_enums`

- **HTTP:** `GET /google/trends/enums`
- **What:** Google Trends enum metadata. Returns supported Google Trends enum values for explore/trending filters, including locations, date ranges, search types, categories, statuses, and sort modes.
- **Params:** _none_

### `google_trends_explore`

- **HTTP:** `POST /google/trends/explore`
- **What:** Google Trends explore data. Returns normalized Google Trends keyword analytics from internal Trends widget requests: interest over time, interest by region, related queries, and related topics when available.
- **Params:** `request` (object, **required**) — Explore request

### `google_trends_explore_interest_by_region`

- **HTTP:** `POST /google/trends/explore/interest-by-region`
- **What:** Google Trends interest by region. Returns only the interest-by-region widget from the Google Trends Explore widget flow. Supports multiple comparison terms and returns an empty interest_by_region array when Google returns no rows.
- **Params:** `request` (object, **required**) — Explore request

### `google_trends_explore_interest_over_time`

- **HTTP:** `POST /google/trends/explore/interest-over-time`
- **What:** Google Trends interest over time. Returns only the interest-over-time timeline from the Google Trends Explore widget flow. Supports multiple comparison terms.
- **Params:** `request` (object, **required**) — Explore request

### `google_trends_explore_related_topics`

- **HTTP:** `POST /google/trends/explore/related-topics`
- **What:** Google Trends related topics. Returns only the related topics widget from the Google Trends Explore widget flow. Returns an empty related_topics array when Google returns no topic rows for the requested term/filter combination.
- **Params:** `request` (object, **required**) — Explore request

### `google_trends_explore_rising_queries`

- **HTTP:** `POST /google/trends/explore/rising-queries`
- **What:** Google Trends explore rising queries. Returns the Rising related queries widget for one or more Google Trends explore terms. Returns an empty queries array when Google returns no rows for the requested term/filter combination.
- **Params:** `request` (object, **required**) — Explore request

### `google_trends_explore_top_queries`

- **HTTP:** `POST /google/trends/explore/top-queries`
- **What:** Google Trends explore top queries. Returns the Top related queries widget for one or more Google Trends explore terms. Returns an empty queries array when Google returns no rows for the requested term/filter combination.
- **Params:** `request` (object, **required**) — Explore request

### `google_trends_locations`

- **HTTP:** `GET /google/trends/locations`
- **What:** Google Trends locations. Returns supported Google Trends location codes. Explore endpoints also accept WORLDWIDE.
- **Params:** _none_

### `google_trends_trending`

- **HTTP:** `GET /google/trends/trending`
- **What:** Google Trends trending now data. Returns normalized Google Trends Trending Now rows from the internal TrendsUi batch RPC replay.
- **Params:** `category` (integer, optional) — Trending category id; `geo` (string, optional) — Country/territory location code; `hl` (string, optional) — Google Trends UI locale; `limit` (integer, optional) — Maximum rows to return; `sort_by` (string, optional) — Sort mode; `status` (string, optional) — Trend status filter; `time_range` (string, optional) — Alias for window; `tz` (integer, optional) — Timezone offset minutes; `window` (string, optional) — Trend window

### `google_trends_trending_detail`

- **HTTP:** `POST /google/trends/trending/detail`
- **What:** Google Trends trending term detail. Returns the Explore detail widgets for a single trending term, including interest over time, regional interest, top/rising related queries, and related topics when Google returns them.
- **Params:** `request` (object, **required**) — Trending detail request

### `google_videos`

- **HTTP:** `GET /google/videos`
- **What:** Search Google video results. Returns normalized Google video vertical results (title, platform, link, duration, age) parsed from the public Google video results page. Locale defaults to country=us and lang=en. Returns 503 when Google serves a challenge page or unusable HTML.
- **Params:** `count` (integer, optional) — Results per page; defaults to 10, clamped to 1..50; `country` (string, optional) — Two-letter country code; defaults to us; `lang` (string, optional) — Google UI language; defaults to en; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, **required**) — Search query

## Google Jobs (2)

### `google_jobs_job`

- **HTTP:** `GET /google-jobs/job`
- **What:** Google Jobs single posting. Returns one Google Careers posting by its numeric job id (the `id` field returned by search). Parsed from careers.google.com's server-rendered job detail page.
- **Params:** `id` (string, **required**) — Numeric Google job id

### `google_jobs_search`

- **HTTP:** `GET /google-jobs/search`
- **What:** Google Jobs search. Searches Google's public careers site (careers.google.com) via its server-rendered search page's embedded job data. Each result includes the description, responsibilities, and qualifications inline. Page size is fixed by Google at 20 results.
- **Params:** `location` (string, optional) — Location filter (free text); `page` (integer, optional) — Page number, 1-based; `q` (string, **required**) — Search query

## GooglePlay (11)

### `googleplay_app`

- **HTTP:** `GET /googleplay/app`
- **What:** Retrieve full Google Play app details. Returns normalized app metadata from a Google Play details page, including installs, ratings, pricing, version info, developer metadata, media assets, release state, selected user comments, and "More by this developer" and "Similar apps" recommendation rails. For a per-device (phone/tablet/Chromebook) ratings-and-reviews breakdown, see `/googleplay/ratings`. Defaults: `country=us`, `lang=en`.
- **Params:** `app_id` (string, **required**) — Google Play package name; `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code

### `googleplay_categories`

- **HTTP:** `GET /googleplay/categories`
- **What:** Retrieve Google Play app categories. Returns category ids found in the Google Play apps navigation.
- **Params:** `country` (string, optional) — Two-letter country code; `lang` (string, optional) — Two-letter language code

### `googleplay_datasafety`

- **HTTP:** `GET /googleplay/datasafety`
- **What:** Retrieve Google Play data safety details. Returns the data safety information displayed on Google Play.
- **Params:** `app_id` (string, **required**) — Google Play app id; `lang` (string, optional) — Two-letter language code

### `googleplay_developer`

- **HTTP:** `GET /googleplay/developer/{dev_id}`
- **What:** Retrieve apps by Google Play developer. Returns apps published by a developer id or developer name.
- **Params:** `country` (string, optional) — Two-letter country code; `dev_id` (string, **required**) — Developer id or name; `full_detail` (boolean, optional) — Resolve each app to full detail; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Number of apps

### `googleplay_list`

- **HTTP:** `GET /googleplay/list`
- **What:** Retrieve apps from a Google Play top collection. Returns apps from a Google Play collection and category.
- **Params:** `age` (string, optional) — Family age range; `category` (string, optional) — Category id; `collection` (string, optional) — Collection: TOP_FREE, TOP_PAID, GROSSING, NEW_FREE, NEW_PAID; `country` (string, optional) — Two-letter country code; `device` (string, optional) — Google Play device tab: phone, tablet, tv, chromebook, watch, xr, car; `full_detail` (boolean, optional) — Resolve each app to full detail; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Number of apps

### `googleplay_permissions`

- **HTTP:** `GET /googleplay/permissions`
- **What:** Retrieve Google Play app permissions. Returns Google Play permission groups or a short permission name list.
- **Params:** `app_id` (string, **required**) — Google Play app id; `country` (string, optional) — Two-letter country code; `lang` (string, optional) — Two-letter language code; `short` (boolean, optional) — Return only permission names

### `googleplay_ratings`

- **HTTP:** `GET /googleplay/ratings`
- **What:** Get Google Play ratings by device. Returns the ratings-and-reviews breakdown Google Play shows under the details page's device tabs, one entry each for phone, tablet, and Chromebook. Defaults: `country=us`, `lang=en`.
- **Params:** `app_id` (string, **required**) — Google Play package name; `country` (string, optional) — Two-letter storefront country code; `lang` (string, optional) — Two-letter language code

### `googleplay_reviews`

- **HTTP:** `GET /googleplay/reviews`
- **What:** Retrieve Google Play reviews. Returns one or more pages of app reviews. Set `paginate=true` to fetch only the requested page.
- **Params:** `app_id` (string, **required**) — Google Play app id; `country` (string, optional) — Two-letter country code; `lang` (string, optional) — Two-letter language code; `next_pagination_token` (string, optional) — Token from a previous response; `num` (integer, optional) — Number of reviews; `paginate` (boolean, optional) — Only fetch the requested page; `sort` (string, optional) — Sort: helpfulness, newest, rating

### `googleplay_search`

- **HTTP:** `GET /googleplay/search`
- **What:** Search Google Play. Returns Google Play search results for a term.
- **Params:** `country` (string, optional) — Two-letter country code; `full_detail` (boolean, optional) — Resolve each app to full detail; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Number of apps; `price` (string, optional) — Price filter: all, free, paid; `term` (string, **required**) — Search term

### `googleplay_similar`

- **HTTP:** `GET /googleplay/similar`
- **What:** Retrieve similar Google Play apps. Returns apps from the "Similar apps" cluster on an app details page.
- **Params:** `app_id` (string, **required**) — Google Play app id; `country` (string, optional) — Two-letter country code; `full_detail` (boolean, optional) — Resolve each app to full detail; `lang` (string, optional) — Two-letter language code; `num` (integer, optional) — Number of apps

### `googleplay_suggest`

- **HTTP:** `GET /googleplay/suggest/{term}`
- **What:** Retrieve Google Play query suggestions. Returns up to 10 suggestions for a search term.
- **Params:** `country` (string, optional) — Two-letter country code; `lang` (string, optional) — Two-letter language code; `term` (string, **required**) — Search term prefix

## IMDb (20)

### `imdb_name`

- **HTTP:** `GET /imdb/name`
- **What:** IMDb name detail. Returns normalized public IMDb person metadata and known-for rows. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb name id; `url` (string, optional) — Absolute https://www.imdb.com/name/<id>/ URL

### `imdb_name_awards`

- **HTTP:** `GET /imdb/name/awards`
- **What:** IMDb name awards. Returns normalized public IMDb award rows for a person. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb name id; `url` (string, optional) — Absolute https://www.imdb.com/name/<id>/ URL

### `imdb_name_credits`

- **HTTP:** `GET /imdb/name/credits`
- **What:** IMDb name credits. Returns normalized public IMDb filmography sections for a person. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb name id; `url` (string, optional) — Absolute https://www.imdb.com/name/<id>/ URL

### `imdb_search`

- **HTTP:** `GET /imdb/search`
- **What:** IMDb title search. Returns normalized IMDb title search rows from credential-free public IMDb pages. Limit defaults to 10 and clamps to 20.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 20; `query` (string, **required**) — Search query

### `imdb_search_title`

- **HTTP:** `GET /imdb/search/title`
- **What:** IMDb advanced title search. Returns normalized IMDb advanced title-search results (imdb.com/search/title/) from a credential-free public IMDb page. At least one filter is required; sort/limit alone are not enough. Limit defaults to 25 and clamps to 50; only IMDb's first rendered page of results is returned (see `total`/`has_more`), there is no deeper cursor pagination. Genre/company/certificate/country/language/keyword/characters/role are include-only lists; there is no exclude support. Unsupported: genre exclude, three curated `groups` values (best-picture-nominee, best-director-nominee, national-film-registry), and the non-plot "page topic" search fields.
- **Params:** `certificates` (string, optional) — Comma-separated `COUNTRY:RATING` certificate pairs, e.g. `US:PG-13`; `characters` (string, optional) — Comma-separated character names; `colors` (string, optional) — Comma-separated color info: `color`, `black_and_white`, `colorized`, `aces`; `companies` (string, optional) — Comma-separated IMDb company ids, format `co########`; `countries` (string, optional) — Comma-separated ISO country codes; `genres` (string, optional) — Comma-separated genres (include-only): `Action`, `Adventure`, `Animation`, `Biography`, `Comedy`, `Crime`, `Documentary`, `Drama`, `Family`, `Fantasy`, `Film-Noir`, `Game-Show`, `History`, `Horror`, `Music`, `Musical`, `Mystery`, `News`, `Reality-TV`, `Romance`, `Sci-Fi`, `Short`, `Sport`, `Talk-Show`, `Thriller`, `War`, `Western`; `groups` (string, optional) — Comma-separated awards/curated-list groups: `oscar_winner`, `oscar_nominee`, `emmy_winner`, `emmy_nominee`, `golden_globe_winner`, `golden_globe_nominee`, `best_picture_winner`, `best_director_winner`, `razzie_winner`, `razzie_nominee`, `top_100`, `top_250`, `top_1000`, `bottom_100`, `bottom_250`, `bottom_1000`; `include_adult` (boolean, optional) — Include adult titles. Defaults to excluded; `keywords` (string, optional) — Comma-separated plot keywords; `languages` (string, optional) — Comma-separated ISO language codes; `limit` (integer, optional) — Rows to return, default 25, max 50; `max_popularity` (integer, optional) — Maximum IMDb popularity rank; `max_runtime` (integer, optional) — Maximum runtime in minutes; `max_user_rating` (number, optional) — Maximum IMDb user rating, 0-10; `max_votes` (integer, optional) — Maximum number of user rating votes; `min_popularity` (integer, optional) — Minimum IMDb popularity rank (1 is most popular); `min_runtime` (integer, optional) — Minimum runtime in minutes; `min_user_rating` (number, optional) — Minimum IMDb user rating, 0-10; `min_votes` (integer, optional) — Minimum number of user rating votes; `plot` (string, optional) — Plot text search term; `release_date_from` (string, optional) — Release date lower bound: YYYY, YYYY-MM, or YYYY-MM-DD; `release_date_to` (string, optional) — Release date upper bound: YYYY, YYYY-MM, or YYYY-MM-DD; `role` (string, optional) — Comma-separated cast/crew IMDb name ids, format `nm########`; `sort` (string, optional) — One of `moviemeter`, `alpha`, `user_rating`, `num_votes`, `boxoffice_gross_us`, `runtime`, `year`, `release_date`; `sort_order` (string, optional) — `asc` or `desc`. Defaults to `asc` when sort is set; `sound_mixes` (string, optional) — Comma-separated sound mix names: `12-Track Digital Sound`, `3 Channel Stereo`, `4-Track Stereo`, `6-Track Stereo`, `70 mm 6-Track`, `AGA Sound System`, `Auro 11.1`, `CDS`, `Chronophone`, `Cinematophone`, `Cinephone`, `Cinerama 7-Track`, `Cinesound`, `D-Cinema 48kHz 5.1`, `Datasat`, `De Forest Phonofilm`, `Digitrac Digital Audio System`, `Dolby`, `Dolby Atmos`, `Dolby Digital`, `Dolby Digital EX`, `Dolby SR`, `Dolby Stereo`, `Dolby Surround 7.1`, `DTS`, `DTS 70 mm`, `DTS Stereo`, `DTS-ES`, `IMAX 6-Track`, `Kinoplasticon`, `LC-Concept Digital Sound`, `Matrix Surround`, `Mono`, `Perspecta Stereo`, `Phono-Kinema`, `SDDS`, `Sensurround`, `Silent`, `Sonics-DDP`, `Sonix`, `Stereo`, `Ultra Stereo`, `Vitaphone`; `title` (string, optional) — Title-name substring match; `title_type` (string, optional) — Comma-separated title types: `feature`, `tvSeries`, `short`, `tvEpisode`, `tvMiniSeries`, `tvMovie`, `tvSpecial`, `tvShort`, `videoGame`, `video`, `musicVideo`, `podcastSeries`, `podcastEpisode`

### `imdb_title`

- **HTTP:** `GET /imdb/title`
- **What:** IMDb title detail. Returns normalized IMDb title metadata from a credential-free public IMDb title page. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_awards`

- **HTTP:** `GET /imdb/title/awards`
- **What:** IMDb title awards. Returns normalized public IMDb award rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_company_credits`

- **HTTP:** `GET /imdb/title/company-credits`
- **What:** IMDb title company credits. Returns normalized public IMDb company-credit sections for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_credits`

- **HTTP:** `GET /imdb/title/credits`
- **What:** IMDb title credits. Returns normalized public IMDb full cast and crew sections. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_episodes`

- **HTTP:** `GET /imdb/title/episodes`
- **What:** IMDb title episodes. Returns normalized public IMDb episode rows for a series title. Limit defaults to 10 and clamps to 20. Optional `season` filters the upstream episodes page. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `limit` (integer, optional) — Rows to return, default 10, max 20; `season` (integer, optional) — Season number to request; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_filming_locations`

- **HTTP:** `GET /imdb/title/filming-locations`
- **What:** IMDb title filming locations. Returns normalized public IMDb filming-location rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_goofs`

- **HTTP:** `GET /imdb/title/goofs`
- **What:** IMDb title goofs. Returns normalized public IMDb goof rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_keywords`

- **HTTP:** `GET /imdb/title/keywords`
- **What:** IMDb title keywords. Returns normalized public IMDb keyword rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_parental_guide`

- **HTTP:** `GET /imdb/title/parental-guide`
- **What:** IMDb title parental guide. Returns normalized public IMDb parental-guide categories and severity signals. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_public_facts_analysis`

- **HTTP:** `GET /imdb/title/public-facts-analysis`
- **What:** IMDb title public facts analysis. Returns derived public-page summary metrics for IMDb trivia, goofs, quotes, keywords, filming locations, and company credits. This endpoint is not viewing advice. Pass exactly one of `id` or `url`. The six sections are gathered from six independent sources, so a section that cannot be fetched is omitted and named in `missing_sections` with `partial` set to `true`, rather than failing the whole response; an error is returned only when no section could be fetched. Callers that require a complete analysis should check `partial`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_quotes`

- **HTTP:** `GET /imdb/title/quotes`
- **What:** IMDb title quotes. Returns normalized public IMDb quote rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_release_info`

- **HTTP:** `GET /imdb/title/release-info`
- **What:** IMDb title release info. Returns normalized public IMDb release date rows and alternate titles. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_reviews`

- **HTTP:** `GET /imdb/title/reviews`
- **What:** IMDb title user reviews. Returns normalized public IMDb user review rows. Limit defaults to 10 and clamps to 20. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `limit` (integer, optional) — Rows to return, default 10, max 20; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_technical_specs`

- **HTTP:** `GET /imdb/title/technical-specs`
- **What:** IMDb title technical specs. Returns normalized public IMDb technical specifications such as runtime, sound mix, color, and aspect ratio. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

### `imdb_title_trivia`

- **HTTP:** `GET /imdb/title/trivia`
- **What:** IMDb title trivia. Returns normalized public IMDb trivia rows for a title. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — IMDb title id; `url` (string, optional) — Absolute https://www.imdb.com/title/<id>/ URL

## ImportYeti (2)

### `importyeti_company`

- **HTTP:** `GET /importyeti/company`
- **What:** Get an ImportYeti company report. Returns a normalized ImportYeti company report: identity, headline US customs shipment-volume metrics (total shipments, average TEU, last shipment date, estimated shipping spend), its supplier list, and recent bill-of-lading shipment activity. Credential-free public data, rendered from the company report page through proxied browser renderers.
- **Params:** `slug` (string, **required**) — ImportYeti company slug, the last path segment of a /company/{slug} URL

### `importyeti_search`

- **HTTP:** `GET /importyeti/search`
- **What:** Search ImportYeti companies and suppliers by name. Searches ImportYeti for companies and suppliers matching a name, returning each match's kind (company or supplier), slug, country, address, and headline shipment stats. A "company" result's slug chains into GET /importyeti/company. Credential-free public data, sourced from ImportYeti's own JSON search API (distinct from its human-facing /search results page, which does not render due to a client-side bug in ImportYeti's own app).
- **Params:** `page` (integer, optional) — 1-indexed result page, defaults to 1; `q` (string, **required**) — Company or supplier name to search for

## Indeed (3)

### `indeed_job`

- **HTTP:** `GET /indeed/job`
- **What:** Indeed job detail. Returns one Indeed job posting by its job key (the `job_key` field returned by search). Primary transport is Indeed's own credential-free GraphQL API; falls back to the original web-page transport if that fails.
- **Params:** `jk` (string, **required**) — Indeed job key (16-character hex)

### `indeed_locations_suggest`

- **HTTP:** `GET /indeed/locations/suggest`
- **What:** Indeed location suggestions. Returns Indeed's own location-search autocomplete suggestions for a partial location string -- the same suggestions the app's search bar offers -- for building a valid `l` value for search. Credential-free GraphQL only; there is no page-based fallback for this endpoint.
- **Params:** `limit` (integer, optional) — Max suggestions to return, defaults to 10, maxes at 25; `q` (string, **required**) — Partial location text

### `indeed_search`

- **HTTP:** `GET /indeed/search`
- **What:** Indeed job search. Searches Indeed job postings by keyword and location. Primary transport is Indeed's own credential-free GraphQL API; a page 1, unfiltered-by-date request uses it directly. Requesting page 2+ or the `fromage` filter (not yet expressible over the primary transport) uses the original web-page transport instead, with the same normalized response shape either way. `sort` enum: `relevance` (default), `date`.
- **Params:** `fromage` (integer, optional) — Only jobs posted within this many days; `l` (string, optional) — Location (city, state, or zip); `page` (integer, optional) — Page number, 1-based, defaults to 1; `q` (string, **required**) — Search keywords; `radius` (integer, optional) — Search radius in miles; `sort` (string, optional) — Sort order: relevance, date

## Instacart (6)

### `instacart_departments`

- **HTTP:** `GET /instacart/departments`
- **What:** Get Instacart store department taxonomy. Returns a store's department/category taxonomy (Produce, Dairy & Eggs, Bakery, ...) two levels deep -- department and subcategory. Metadata only, does not return products. Public data sourced from Instacart's own storefront navigation.
- **Params:** `postal_code` (string, **required**) — Postal code to localize the taxonomy for; `shop_id` (string, **required**) — Store's opaque shop id, from GET /instacart/stores; `store_slug` (string, **required**) — Store's retailer slug, from GET /instacart/stores

### `instacart_item`

- **HTTP:** `GET /instacart/item`
- **What:** Get Instacart product detail at a store. Returns a single product's detail at a specific Instacart store: name, size, brand, image, current pricing (with any sale/offer badge), availability, stock level, dietary labels, and nutrition facts. Public data sourced from Instacart's own storefront pages.
- **Params:** `postal_code` (string, **required**) — Postal code to price/localize the lookup for; `product_id` (string, **required**) — Instacart's opaque product id; `retailer_location_id` (string, **required**) — Store's opaque retailer location id, from GET /instacart/stores; `shop_id` (string, **required**) — Store's opaque shop id, from GET /instacart/stores; `store_slug` (string, **required**) — Store's retailer slug, from GET /instacart/stores

### `instacart_search`

- **HTTP:** `GET /instacart/search`
- **What:** Search Instacart product terms at a store. Returns Instacart's own search-term autosuggestions for a keyword within one store -- the same suggestion list shown in the site's own search box dropdown. This is term-level (matching search phrases plus a representative thumbnail), not a paginated product-results list. Public data sourced from Instacart's own storefront search.
- **Params:** `q` (string, **required**) — Free-text search term; `shop_id` (string, **required**) — Store's opaque shop id, from GET /instacart/stores; `store_slug` (string, **required**) — Store's retailer slug, from GET /instacart/stores

### `instacart_search_nearby`

- **HTTP:** `GET /instacart/search-nearby`
- **What:** Search Instacart product terms near a postal code. Returns Instacart's own search-term autosuggestions for a keyword across every retailer serving a postal code at once, rather than one specific store. Public data sourced from Instacart's own cross-retailer search.
- **Params:** `postal_code` (string, **required**) — US postal/ZIP code to search near; `q` (string, **required**) — Free-text search term

### `instacart_stores`

- **HTTP:** `GET /instacart/stores`
- **What:** Find Instacart stores near a postal code. Finds Instacart retailer storefronts (grocery stores, warehouse clubs, and other partner retailers) serving a US postal code, each with the identifiers needed to look up its items and search suggestions. Public data sourced from Instacart's own store-discovery API.
- **Params:** `postal_code` (string, **required**) — US postal/ZIP code to search near

### `instacart_trending`

- **HTTP:** `GET /instacart/trending`
- **What:** Get Instacart trending search terms near a postal code. Returns Instacart's own popular/trending search terms across every retailer serving a postal code -- the same blank-state suggestions shown before a user types anything into the search box. Public data sourced from Instacart's own cross-retailer search.
- **Params:** `postal_code` (string, **required**) — US postal/ZIP code to search near

## Instagram (3)

### `instagram_post`

- **HTTP:** `GET /instagram/post/{id}/{post_id}`
- **What:** Retrieve a specific Instagram post by user ID and post ID. Returns the media details of a specific post from an Instagram user.
- **Params:** `id` (string, **required**) — Instagram user ID; `post_id` (string, **required**) — Instagram post ID

### `instagram_profile`

- **HTTP:** `GET /instagram/profile/{username}`
- **What:** Retrieve an Instagram user profile by username. Returns public profile details for a specified Instagram username.
- **Params:** `username` (string, **required**) — Instagram username

### `instagram_reels`

- **HTTP:** `GET /instagram/reels/{id}`
- **What:** Retrieve Instagram Reels for a user. Returns a feed of Instagram Reels for the specified user ID. Supports pagination via `max_id`.
- **Params:** `id` (string, **required**) — Instagram user ID; `max_id` (string, optional) — Pagination cursor for fetching the next page of Reels

## Jobs (28)

### `jobs_ashby_board`

- **HTTP:** `GET /jobs/ashby/board`
- **What:** List an organization's Ashby job board. Lists an organization's public Ashby board postings with inline detail (description, compensation when include_compensation=true). The org is the Ashby slug from its careers URL. An unknown org returns an empty board (Ashby does not 404). Credential-free public ATS JSON.
- **Params:** `include_compensation` (boolean, optional) — Include compensation summary; `org` (string, **required**) — Ashby org slug (careers URL)

### `jobs_company_search`

- **HTTP:** `GET /jobs/company-search`
- **What:** Find which ATS a company uses by slug. Probes Greenhouse, Lever, Ashby, SmartRecruiters, Workable, Recruitee, Rippling, Teamtailor, and Pinpoint in parallel for a slug and reports the providers where it resolves to a non-empty board (with the open-role count and board URL). Workday is excluded (its board needs tenant + datacenter + site). Credential-free public ATS JSON.
- **Params:** `slug` (string, **required**) — Company careers slug to probe

### `jobs_eightfold_board`

- **HTTP:** `GET /jobs/eightfold/board`
- **What:** List an Eightfold tenant's job board. Lists a company's public Eightfold AI job board, paged via limit/offset. tenant is the {tenant}.eightfold.ai subdomain from the careers URL; domain is the hiring organization's own domain (e.g. microsoft.com), also visible on the tenant's careers page. Tries the newer PCSX search first, falling back to the legacy SmartApply generation when PCSX is not enabled for the tenant. Credential-free public ATS JSON.
- **Params:** `domain` (string, **required**) — Hiring organization domain; `limit` (integer, optional) — Page size, default 10, max 10 (upstream caps results per page regardless of a larger value); `location` (string, optional) — Filter: location contains; `offset` (integer, optional) — Page offset, default 0; `query` (string, optional) — Free-text search; `tenant` (string, **required**) — Eightfold tenant subdomain (careers URL)

### `jobs_eightfold_job`

- **HTTP:** `GET /jobs/eightfold/job`
- **What:** Get a single Eightfold position. Returns a single Eightfold position with its full HTML/text description. id is the position id from a board listing; tenant/domain as in the board endpoint. Tries the newer PCSX detail first, falling back to the legacy SmartApply detail generation. Credential-free public ATS JSON.
- **Params:** `domain` (string, **required**) — Hiring organization domain; `id` (string, **required**) — Eightfold position id from a board listing; `tenant` (string, **required**) — Eightfold tenant subdomain

### `jobs_gem_board`

- **HTTP:** `GET /jobs/gem/board`
- **What:** List a company's Gem job board. Lists a company's public Gem (gem.com) board postings with inline detail (full HTML description, and compensation when the company publishes a pay range). The company is the Gem vanity URL slug from its careers URL. Credential-free public GraphQL.
- **Params:** `company` (string, **required**) — Gem vanity URL slug (careers URL)

### `jobs_greenhouse_board`

- **HTTP:** `GET /jobs/greenhouse/board`
- **What:** List a company's Greenhouse job board. Lists a company's public Greenhouse board postings, normalized to the shared Job shape. Set content=true to include each job's full HTML description in one call. The token is the company's Greenhouse board slug from its careers URL. Credential-free public ATS JSON.
- **Params:** `content` (boolean, optional) — Include full HTML description per job; `token` (string, **required**) — Greenhouse board token (careers URL slug)

### `jobs_greenhouse_job`

- **HTTP:** `GET /jobs/greenhouse/job`
- **What:** Get a single Greenhouse job. Returns a single Greenhouse job with its full HTML/text description, department, and offices. Credential-free public ATS JSON.
- **Params:** `id` (string, **required**) — Greenhouse job id; `token` (string, **required**) — Greenhouse board token

### `jobs_hiring_signals`

- **HTTP:** `GET /jobs/hiring-signals`
- **What:** Aggregate hiring signals for a company's board. Aggregates a company's ATS board into a hiring snapshot: total open roles, breakdowns by department/location/title, remote share, and how many roles are new in the last 7/30 days — a leading indicator of company growth. Supply provider plus that provider's slug params (token / company / org / tenant+datacenter+site / domain). Breakdowns are computed over the fetched postings. Credential-free public ATS JSON.
- **Params:** `board` (string, optional) — ukg job-board UUID; `company` (string, optional) — lever / smartrecruiters / workable / recruitee / rippling / personio / teamtailor / gem / pinpoint company slug; `datacenter` (string, optional) — workday datacenter shard; `domain` (string, optional) — icims careers domain / eightfold organization domain; `host` (string, optional) — oracle cloud host (*.oraclecloud.com); `org` (string, optional) — ashby org slug; `provider` (string, **required**) — ATS provider; `site` (string, optional) — workday / oracle career site; `tenant` (string, optional) — workday / eightfold tenant; `token` (string, optional) — greenhouse board token

### `jobs_icims_board`

- **HTTP:** `GET /jobs/icims/board`
- **What:** List an iCIMS tenant's job board. Lists a company's public iCIMS job board (served through the tenant's white-labeled careers domain, e.g. careers.costco.com — not the bare {company}.icims.com subdomain, which is an OAuth-gated employee portal), paged via page/limit, with the full description inline per job. domain is the tenant's careers domain from its careers URL. Credential-free public ATS JSON.
- **Params:** `domain` (string, **required**) — iCIMS tenant careers domain (careers URL); `keywords` (string, optional) — Free-text keyword search; `limit` (integer, optional) — Page size, default 20, max 50; `location` (string, optional) — Filter: location contains; `page` (integer, optional) — Page number, default 1

### `jobs_icims_job`

- **HTTP:** `GET /jobs/icims/job`
- **What:** Get a single iCIMS job. Returns a single iCIMS job with its full HTML/text description, department, and benefits. id is the req_id/slug from a board listing; lang defaults to en-us. Credential-free public ATS JSON.
- **Params:** `domain` (string, **required**) — iCIMS tenant careers domain; `id` (string, **required**) — iCIMS job req_id/slug from a board listing; `lang` (string, optional) — Language code, default en-us

### `jobs_lever_posting`

- **HTTP:** `GET /jobs/lever/posting`
- **What:** Get a single Lever posting. Returns a single Lever posting with its full HTML/text description. Credential-free public ATS JSON.
- **Params:** `company` (string, **required**) — Lever company slug; `id` (string, **required**) — Lever posting id

### `jobs_lever_postings`

- **HTTP:** `GET /jobs/lever/postings`
- **What:** List a company's Lever postings. Lists a company's public Lever postings (detail is inline), optionally filtered by department, location, or remote. The company is the Lever slug from its careers URL. Credential-free public ATS JSON.
- **Params:** `company` (string, **required**) — Lever company slug (careers URL); `department` (string, optional) — Filter: department contains; `location` (string, optional) — Filter: location contains; `remote` (boolean, optional) — Filter by remote (true or false)

### `jobs_oracle_board`

- **HTTP:** `GET /jobs/oracle/board`
- **What:** List an Oracle Recruiting (ORC) tenant's job board. Lists an Oracle Recruiting Cloud tenant's public requisitions, paged via limit/offset. host and site both come from the careers URL https://{host}/hcmUI/CandidateExperience/en/sites/{site}/ (host must be an *.oraclecloud.com hostname; site looks like CX_1). The listing carries a short description; use the single-job endpoint for full detail. Credential-free public ATS JSON.
- **Params:** `host` (string, **required**) — Oracle Cloud host (careers URL, *.oraclecloud.com); `limit` (integer, optional) — Page size, default 25, max 50; `offset` (integer, optional) — Page offset, default 0; `search` (string, optional) — Free-text keyword search; `site` (string, **required**) — Oracle career site number

### `jobs_oracle_job`

- **HTTP:** `GET /jobs/oracle/job`
- **What:** Get a single Oracle Recruiting (ORC) requisition. Returns a single Oracle Recruiting requisition with its full HTML/text description (description, responsibilities, qualifications). id is the requisition Id from a board listing; host/site as in the board endpoint. Credential-free public ATS JSON.
- **Params:** `host` (string, **required**) — Oracle Cloud host (*.oraclecloud.com); `id` (string, **required**) — Oracle requisition Id from a board listing; `site` (string, **required**) — Oracle career site number

### `jobs_personio_feed`

- **HTTP:** `GET /jobs/personio/feed`
- **What:** List a company's Personio job board. Lists a company's public Personio board feed (XML), normalized to the shared Job shape with detail inline, optionally filtered by department, location, or remote. The company is the Personio subdomain from its careers URL https://{company}.jobs.personio.de/. Credential-free public ATS feed.
- **Params:** `company` (string, **required**) — Personio subdomain (careers URL); `department` (string, optional) — Filter: department contains; `location` (string, optional) — Filter: location contains; `remote` (boolean, optional) — Filter by remote (true or false)

### `jobs_pinpoint_board`

- **HTTP:** `GET /jobs/pinpoint/board`
- **What:** List a tenant's Pinpoint job board. Lists a tenant's public Pinpoint (pinpointhq.com) board postings with inline detail (full HTML description, key responsibilities, skills, and benefits, plus structured compensation when the tenant publishes a pay range). The company is the tenant subdomain from its careers URL https://{company}.pinpointhq.com/. Credential-free public JSON.
- **Params:** `company` (string, **required**) — Pinpoint tenant subdomain (careers URL)

### `jobs_recruitee_offer`

- **HTTP:** `GET /jobs/recruitee/offer`
- **What:** Get a single Recruitee offer. Returns a single Recruitee offer with its full HTML/text description and structured compensation when the board exposes it. Credential-free public ATS JSON.
- **Params:** `company` (string, **required**) — Recruitee subdomain; `id` (string, **required**) — Recruitee offer id

### `jobs_recruitee_offers`

- **HTTP:** `GET /jobs/recruitee/offers`
- **What:** List a company's Recruitee offers. Lists a company's public Recruitee offers (detail is inline), optionally filtered by department, location, or remote. The company is the Recruitee subdomain from its careers URL https://{company}.recruitee.com/. Credential-free public ATS JSON.
- **Params:** `company` (string, **required**) — Recruitee subdomain (careers URL); `department` (string, optional) — Filter: department contains; `location` (string, optional) — Filter: location contains; `remote` (boolean, optional) — Filter by remote (true or false)

### `jobs_rippling_board`

- **HTTP:** `GET /jobs/rippling/board`
- **What:** List a company's Rippling job board. Lists a company's public Rippling board postings (thin listing — title, department, work location). The company is the Rippling board slug from its careers URL https://ats.rippling.com/{company}/jobs. Detail (full description, employment type) is fetched per job via the single-job endpoint. Credential-free public ATS JSON.
- **Params:** `company` (string, **required**) — Rippling board slug (careers URL); `department` (string, optional) — Filter: department contains; `location` (string, optional) — Filter: location contains; `remote` (boolean, optional) — Filter by remote (true or false)

### `jobs_rippling_job`

- **HTTP:** `GET /jobs/rippling/job`
- **What:** Get a single Rippling job. Returns a single Rippling job with its full HTML/text description, employment type, and work locations. The id is the job uuid from a listing. Credential-free public ATS JSON.
- **Params:** `company` (string, **required**) — Rippling board slug; `id` (string, **required**) — Rippling job uuid

### `jobs_smartrecruiters_posting`

- **HTTP:** `GET /jobs/smartrecruiters/posting`
- **What:** Get a single SmartRecruiters posting. Returns a single SmartRecruiters posting with its jobAd description. Recruiter personal data is intentionally omitted. Credential-free public ATS JSON.
- **Params:** `company` (string, **required**) — SmartRecruiters company id; `id` (string, **required**) — SmartRecruiters posting id

### `jobs_smartrecruiters_postings`

- **HTTP:** `GET /jobs/smartrecruiters/postings`
- **What:** List a company's SmartRecruiters postings. Lists a company's public SmartRecruiters postings, paged via limit/offset. The company is the SmartRecruiters identifier from its careers URL. Credential-free public ATS JSON.
- **Params:** `company` (string, **required**) — SmartRecruiters company id (careers URL); `limit` (integer, optional) — Page size, default 100, max 100; `offset` (integer, optional) — Page offset, default 0

### `jobs_teamtailor_jobs`

- **HTTP:** `GET /jobs/teamtailor/jobs`
- **What:** List a company's Teamtailor job board. Lists a company's public Teamtailor board feed (JSON Feed), normalized to the shared Job shape with detail inline, optionally filtered by department, location, or remote. The company is the Teamtailor subdomain from its careers URL https://{company}.teamtailor.com/. Credential-free public ATS feed.
- **Params:** `company` (string, **required**) — Teamtailor subdomain (careers URL); `department` (string, optional) — Filter: department contains; `location` (string, optional) — Filter: location contains; `remote` (boolean, optional) — Filter by remote (true or false)

### `jobs_ukg_board`

- **HTTP:** `GET /jobs/ukg/board`
- **What:** List a UKG Pro Recruiting tenant's job board. Lists a UKG Pro Recruiting (formerly UltiPro) tenant's public opportunities, paged via limit/offset. tenant and board both come from the careers URL https://recruiting.ultipro.com/{tenant}/JobBoard/{board}. Each posting carries a brief description inline (UKG's full detail page is HTML, not JSON). Credential-free public ATS JSON.
- **Params:** `board` (string, **required**) — UKG job-board UUID (careers URL); `limit` (integer, optional) — Page size, default 25, max 50; `offset` (integer, optional) — Page offset, default 0; `search` (string, optional) — Free-text keyword search; `tenant` (string, **required**) — UKG tenant code (careers URL)

### `jobs_workable_posting`

- **HTTP:** `GET /jobs/workable/posting`
- **What:** Get a single Workable posting. Returns a single Workable posting with its full HTML/text description. The id is the posting shortcode from a listing. Credential-free public ATS JSON.
- **Params:** `company` (string, **required**) — Workable account slug; `id` (string, **required**) — Workable posting shortcode

### `jobs_workable_postings`

- **HTTP:** `GET /jobs/workable/postings`
- **What:** List a company's Workable postings. Lists a company's public Workable postings, normalized to the shared Job shape, optionally filtered by department, location, or remote. The company is the Workable account slug from its careers URL https://apply.workable.com/{company}/. Detail (full description) is fetched per job via the single-posting endpoint. Credential-free public ATS JSON.
- **Params:** `company` (string, **required**) — Workable account slug (careers URL); `department` (string, optional) — Filter: department contains; `location` (string, optional) — Filter: location contains; `remote` (boolean, optional) — Filter by remote (true or false); `search` (string, optional) — Free-text search

### `jobs_workday_board`

- **HTTP:** `GET /jobs/workday/board`
- **What:** List a Workday tenant's job board. Lists a company's public Workday (CXS) postings, paged via limit/offset. tenant, datacenter (wd1/wd3/wd5/...), and site all come from the careers URL https://{tenant}.wd5.myworkdayjobs.com/{site}. Credential-free public ATS JSON.
- **Params:** `datacenter` (string, **required**) — Workday datacenter shard (wd1, wd3, wd5, ...); `limit` (integer, optional) — Page size, default 20, max 20; `offset` (integer, optional) — Page offset, default 0; `search` (string, optional) — Free-text search; `site` (string, **required**) — Workday career site; `tenant` (string, **required**) — Workday tenant

### `jobs_workday_job`

- **HTTP:** `GET /jobs/workday/job`
- **What:** Get a single Workday job. Returns a single Workday posting's full detail (description, location, req id). path is the externalPath from a board listing. tenant/datacenter/site as in the board endpoint. Credential-free public ATS JSON.
- **Params:** `datacenter` (string, **required**) — Workday datacenter shard; `path` (string, **required**) — Job externalPath from a board listing; `site` (string, **required**) — Workday career site; `tenant` (string, **required**) — Workday tenant

## JustWatch (21)

### `justwatch_age_certifications`

- **HTTP:** `GET /justwatch/age-certifications`
- **What:** Get JustWatch age certifications. Returns JustWatch age certification technical names for a country.
- **Params:** `country` (string, optional) — Two-letter country code

### `justwatch_discover`

- **HTTP:** `GET /justwatch/discover`
- **What:** Discover JustWatch titles. Returns popular movies and shows filtered by optional genre short names, provider short names, production countries, monetization types, and release year bounds. Combine `providers` with `production_countries` to build charts such as most popular Korean or Japanese titles on a given service. Type accepts only `all`, `movie`, or `show`; monetization_types accepts only `FLATRATE`, `FREE`, `ADS`, `RENT`, or `BUY`.
- **Params:** `country` (string, optional) — Two-letter country code; `genres` (string, optional) — Comma-separated JustWatch genre short names; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `monetization_types` (string, optional) — Comma-separated monetization types: FLATRATE, FREE, ADS, RENT, BUY; `production_countries` (string, optional) — Comma-separated two-letter ISO production-country codes; `providers` (string, optional) — Comma-separated JustWatch provider short names; `type` (string, optional) — Title type: all, movie, show; `year_max` (integer, optional) — Maximum release year; `year_min` (integer, optional) — Minimum release year

### `justwatch_episode_by_id`

- **HTTP:** `GET /justwatch/episode/by-id`
- **What:** Get JustWatch episode by raw id. Looks up an episode by raw JustWatch GraphQL id such as `tse5550494` and returns normalized metadata and offers.
- **Params:** `country` (string, optional) — Two-letter country code; `id` (string, **required**) — Raw JustWatch episode id matching tse[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_episode_offers`

- **HTTP:** `GET /justwatch/episode/offers`
- **What:** Get JustWatch episode offers. Returns normalized offers for a raw JustWatch episode id across one to five comma-separated country codes.
- **Params:** `countries` (string, optional) — One to five comma-separated two-letter country codes; `id` (string, **required**) — Raw JustWatch episode id matching tse[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_genre_titles`

- **HTTP:** `GET /justwatch/genre/titles`
- **What:** Get JustWatch genre titles. Returns popular titles for one JustWatch genre short name such as `act`. Type accepts only `all`, `movie`, or `show`.
- **Params:** `country` (string, optional) — Two-letter country code; `genre` (string, **required**) — JustWatch genre short name; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `type` (string, optional) — Title type: all, movie, show

### `justwatch_genres`

- **HTTP:** `GET /justwatch/genres`
- **What:** Get JustWatch genres. Returns JustWatch genre short names and localized translations.
- **Params:** `language` (string, optional) — Two-letter language code

### `justwatch_monetization_titles`

- **HTTP:** `GET /justwatch/monetization/titles`
- **What:** Get JustWatch monetization titles. Returns popular titles for one monetization type. monetization_type accepts only `FLATRATE`, `FREE`, `ADS`, `RENT`, or `BUY`; type accepts only `all`, `movie`, or `show`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `monetization_type` (string, **required**) — Monetization type: FLATRATE, FREE, ADS, RENT, BUY; `type` (string, optional) — Title type: all, movie, show

### `justwatch_new`

- **HTTP:** `GET /justwatch/new`
- **What:** Get new JustWatch titles. Returns newly available movies and shows from the public JustWatch website GraphQL endpoint. Type accepts only `all`, `movie`, or `show`; limit defaults to 20 and clamps to 50.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `type` (string, optional) — Title type: all, movie, show

### `justwatch_popular`

- **HTTP:** `GET /justwatch/popular`
- **What:** Get popular JustWatch titles. Returns popular movies and shows from the public JustWatch website GraphQL endpoint. Type accepts only `all`, `movie`, or `show`; limit defaults to 20 and clamps to 50.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `type` (string, optional) — Title type: all, movie, show

### `justwatch_provider_titles`

- **HTTP:** `GET /justwatch/provider/titles`
- **What:** Get JustWatch provider titles. Returns popular movie/show titles available through a JustWatch provider short name such as `nfx`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 20 and clamps to 50; `provider` (string, **required**) — JustWatch provider short name; `type` (string, optional) — Title type: all, movie, show

### `justwatch_providers`

- **HTTP:** `GET /justwatch/providers`
- **What:** Get JustWatch providers. Returns the credential-free public JustWatch provider catalog for a country.
- **Params:** `country` (string, optional) — Two-letter country code

### `justwatch_search`

- **HTTP:** `GET /justwatch/search`
- **What:** Search JustWatch titles. Searches JustWatch titles using the public credential-free website GraphQL endpoint. Country must be a two-letter ISO code such as `US`; language must be a two-letter code such as `en`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 10 and clamps to 25; `query` (string, **required**) — Search query

### `justwatch_season_by_id`

- **HTTP:** `GET /justwatch/season/by-id`
- **What:** Get JustWatch season by raw id. Looks up a season by raw JustWatch GraphQL id such as `tss297253`.
- **Params:** `country` (string, optional) — Two-letter country code; `id` (string, **required**) — Raw JustWatch season id matching tss[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_season_episodes`

- **HTTP:** `GET /justwatch/season/episodes`
- **What:** Get JustWatch season episodes. Returns episodes and normalized episode offers for a raw JustWatch season id such as `tss297253`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `season_id` (string, **required**) — Raw JustWatch season id matching tss[0-9]+

### `justwatch_show_seasons`

- **HTTP:** `GET /justwatch/show/seasons`
- **What:** Get JustWatch show seasons. Returns seasons for a raw JustWatch show id such as `ts287292`.
- **Params:** `country` (string, optional) — Two-letter country code; `language` (string, optional) — Two-letter language code; `show_id` (string, **required**) — Raw JustWatch show id matching ts[0-9]+

### `justwatch_title`

- **HTTP:** `GET /justwatch/title`
- **What:** Get JustWatch title details. Fetches a JustWatch title page and returns normalized metadata and current offers. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — JustWatch title path; `url` (string, optional) — Absolute https://www.justwatch.com title URL

### `justwatch_title_analysis`

- **HTTP:** `GET /justwatch/title/analysis`
- **What:** Analyze JustWatch title availability. Fetches a JustWatch title page and summarizes provider availability, monetization buckets, formats, price ranges, and best rent/buy/free/subscription options. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — JustWatch title path; `url` (string, optional) — Absolute https://www.justwatch.com title URL

### `justwatch_title_by_id`

- **HTTP:** `GET /justwatch/title/by-id`
- **What:** Get JustWatch title by raw id. Looks up a movie or show by raw JustWatch GraphQL id such as `tm92641` or `ts287292`.
- **Params:** `country` (string, optional) — Two-letter country code; `id` (string, **required**) — Raw JustWatch movie/show id matching tm[0-9]+ or ts[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_title_media`

- **HTTP:** `GET /justwatch/title/media`
- **What:** Get JustWatch title media. Returns normalized credits, clips, and backdrops for a raw JustWatch movie/show id such as `tm92641`.
- **Params:** `country` (string, optional) — Two-letter country code; `id` (string, **required**) — Raw JustWatch movie/show id matching tm[0-9]+ or ts[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_title_offers`

- **HTTP:** `GET /justwatch/title/offers`
- **What:** Get JustWatch title offers. Returns normalized offers for a raw JustWatch movie/show id across one to five comma-separated country codes.
- **Params:** `countries` (string, optional) — One to five comma-separated two-letter country codes; `id` (string, **required**) — Raw JustWatch movie/show id matching tm[0-9]+ or ts[0-9]+; `language` (string, optional) — Two-letter language code

### `justwatch_title_similar`

- **HTTP:** `GET /justwatch/title/similar`
- **What:** Get similar JustWatch titles. Returns similar titles for a raw JustWatch movie/show id such as `tm92641`.
- **Params:** `country` (string, optional) — Two-letter country code; `id` (string, **required**) — Raw JustWatch movie/show id matching tm[0-9]+ or ts[0-9]+; `language` (string, optional) — Two-letter language code; `limit` (integer, optional) — Maximum results, defaults to 10 and clamps to 25

## Kalshi (21)

### `kalshi_event`

- **HTTP:** `GET /kalshi/event/{event_ticker}`
- **What:** Kalshi event detail. Returns one normalized Kalshi event row and its normalized markets from credential-free public market-data JSON.
- **Params:** `event_ticker` (string, **required**) — Kalshi event ticker

### `kalshi_event_history`

- **HTTP:** `GET /kalshi/event/{event_ticker}/history`
- **What:** Kalshi event history. Returns normalized Kalshi candlesticks grouped by market for one event from credential-free public market-data JSON.
- **Params:** `end_ts` (integer, optional) — Unix end timestamp in seconds. Defaults to now.; `event_ticker` (string, **required**) — Kalshi event ticker; `include_latest_before_start` (boolean, optional) — Include the latest candle before start_ts when supported upstream.; `period_interval` (integer, optional) — Candlestick interval in minutes. Default: 1440.; `series_ticker` (string, optional) — Kalshi series ticker. Defaults to the event ticker prefix before the last dash.; `start_ts` (integer, optional) — Unix start timestamp in seconds. Defaults to 7 days ago.

### `kalshi_event_metadata`

- **HTTP:** `GET /kalshi/event/{event_ticker}/metadata`
- **What:** Kalshi event metadata. Returns media, market metadata, settlement sources, and optional competition context for one Kalshi event from credential-free public market-data JSON.
- **Params:** `event_ticker` (string, **required**) — Kalshi event ticker

### `kalshi_events`

- **HTTP:** `GET /kalshi/events`
- **What:** Kalshi events. Returns normalized Kalshi event rows from credential-free public market-data JSON.
- **Params:** `category` (string, optional) — Kalshi category filter; `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `limit` (integer, optional) — Rows to return, default 25, max 200; `min_close_ts` (integer, optional) — Minimum event close Unix timestamp in seconds; `min_updated_ts` (integer, optional) — Minimum event update Unix timestamp in seconds; `series_ticker` (string, optional) — Kalshi series ticker filter; `status` (string, optional) — Event status filter; `with_milestones` (boolean, optional) — Include event milestones when supported upstream; `with_nested_markets` (boolean, optional) — Include nested market rows when supported upstream

### `kalshi_exchange_schedule`

- **HTTP:** `GET /kalshi/exchange/schedule`
- **What:** Kalshi exchange schedule. Returns public exchange standard hours and maintenance windows from Kalshi market-data JSON.
- **Params:** _none_

### `kalshi_exchange_status`

- **HTTP:** `GET /kalshi/exchange/status`
- **What:** Kalshi exchange status. Returns public exchange and trading active flags from Kalshi market-data JSON.
- **Params:** _none_

### `kalshi_historical_cutoff`

- **HTTP:** `GET /kalshi/historical/cutoff`
- **What:** Kalshi historical data cutoff. Returns the cutoff timestamps Kalshi uses for historical market, order, and trade data migration.
- **Params:** _none_

### `kalshi_historical_market`

- **HTTP:** `GET /kalshi/historical/market/{ticker}`
- **What:** Kalshi historical market detail. Returns one normalized settled Kalshi historical market row from credential-free public market-data JSON.
- **Params:** `ticker` (string, **required**) — Kalshi historical market ticker

### `kalshi_historical_market_history`

- **HTTP:** `GET /kalshi/historical/market/{ticker}/history`
- **What:** Kalshi historical market history. Returns normalized Kalshi candlesticks for one settled historical market from credential-free public market-data JSON.
- **Params:** `end_ts` (integer, optional) — Unix end timestamp in seconds. Defaults to now.; `period_interval` (integer, optional) — Candlestick interval in minutes. Default: 1440.; `start_ts` (integer, optional) — Unix start timestamp in seconds. Defaults to 7 days ago.; `ticker` (string, **required**) — Kalshi historical market ticker

### `kalshi_historical_markets`

- **HTTP:** `GET /kalshi/historical/markets`
- **What:** Kalshi historical markets. Returns normalized settled Kalshi historical market rows from credential-free public market-data JSON. `tickers`, `event_ticker`, and `series_ticker` are mutually exclusive. The `mve_filter` enum accepts `exclude`.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `event_ticker` (string, optional) — Kalshi event ticker filter. Mutually exclusive with tickers and series_ticker.; `limit` (integer, optional) — Rows to return, default 25, max 1000; `mve_filter` (string, optional) — Multivariate event filter; `series_ticker` (string, optional) — Kalshi series ticker filter. Mutually exclusive with tickers and event_ticker.; `tickers` (string, optional) — Comma-separated Kalshi market tickers. Mutually exclusive with event_ticker and series_ticker.

### `kalshi_historical_trades`

- **HTTP:** `GET /kalshi/historical/trades`
- **What:** Kalshi historical trades. Returns normalized older Kalshi trades from credential-free historical market-data JSON.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `limit` (integer, optional) — Rows to return, default 25, max 200; `max_ts` (integer, optional) — Maximum created Unix timestamp in seconds; `min_ts` (integer, optional) — Minimum created Unix timestamp in seconds; `ticker` (string, optional) — Kalshi market ticker filter

### `kalshi_market`

- **HTTP:** `GET /kalshi/market/{ticker}`
- **What:** Kalshi market detail. Returns one normalized Kalshi market row from credential-free public market-data JSON.
- **Params:** `ticker` (string, **required**) — Kalshi market ticker

### `kalshi_market_history`

- **HTTP:** `GET /kalshi/market/{ticker}/history`
- **What:** Kalshi market history. Returns normalized Kalshi candlesticks for one market from credential-free public market-data JSON.
- **Params:** `end_ts` (integer, optional) — Unix end timestamp in seconds. Defaults to now.; `include_latest_before_start` (boolean, optional) — Include the latest candle before start_ts when supported upstream.; `period_interval` (integer, optional) — Candlestick interval in minutes. Default: 1440.; `series_ticker` (string, optional) — Kalshi series ticker. Defaults to the market ticker prefix before the last dash.; `start_ts` (integer, optional) — Unix start timestamp in seconds. Defaults to 7 days ago.; `ticker` (string, **required**) — Kalshi market ticker

### `kalshi_market_orderbook`

- **HTTP:** `GET /kalshi/market/{ticker}/orderbook`
- **What:** Kalshi market orderbook. Returns normalized yes/no bid levels for one Kalshi market ticker from public orderbook JSON.
- **Params:** `ticker` (string, **required**) — Kalshi market ticker

### `kalshi_markets`

- **HTTP:** `GET /kalshi/markets`
- **What:** Kalshi markets. Returns normalized Kalshi market rows from credential-free public market-data JSON. The `status` enum accepts `unopened`, `open`, `closed`, and `settled`.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `event_ticker` (string, optional) — Kalshi event ticker filter; `limit` (integer, optional) — Rows to return, default 25, max 200; `series_ticker` (string, optional) — Kalshi series ticker filter; `status` (string, optional) — Market status filter; `ticker` (string, optional) — Kalshi market ticker filter

### `kalshi_markets_history`

- **HTTP:** `GET /kalshi/markets/history`
- **What:** Kalshi batch market history. Returns normalized Kalshi candlesticks for up to 25 market tickers from credential-free public market-data JSON.
- **Params:** `end_ts` (integer, optional) — Unix end timestamp in seconds. Defaults to now.; `include_latest_before_start` (boolean, optional) — Include the latest candle before start_ts when supported upstream.; `market_tickers` (string, **required**) — Comma-separated Kalshi market tickers. Repeated query values are also accepted.; `period_interval` (integer, optional) — Candlestick interval in minutes. Default: 1440.; `start_ts` (integer, optional) — Unix start timestamp in seconds. Defaults to 7 days ago.

### `kalshi_markets_orderbooks`

- **HTTP:** `GET /kalshi/markets/orderbooks`
- **What:** Kalshi batch market orderbooks. Returns normalized yes/no bid levels for up to 25 Kalshi market tickers from public orderbook JSON.
- **Params:** `tickers` (string, **required**) — Comma-separated Kalshi market tickers. Repeated query values are also accepted.

### `kalshi_multivariate_events`

- **HTTP:** `GET /kalshi/events/multivariate`
- **What:** Kalshi multivariate events. Returns normalized Kalshi multivariate event rows from credential-free public market-data JSON. Kalshi's regular events endpoint excludes these MVE rows.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `limit` (integer, optional) — Rows to return, default 25, max 200

### `kalshi_series`

- **HTTP:** `GET /kalshi/series`
- **What:** Kalshi series. Returns normalized Kalshi series rows from credential-free public market-data JSON.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `limit` (integer, optional) — Rows to return, default 25, max 200

### `kalshi_series_detail`

- **HTTP:** `GET /kalshi/series/{series_ticker}`
- **What:** Kalshi series detail. Returns one normalized Kalshi series row from credential-free public market-data JSON.
- **Params:** `series_ticker` (string, **required**) — Kalshi series ticker

### `kalshi_trades`

- **HTTP:** `GET /kalshi/trades`
- **What:** Kalshi trades. Returns normalized recent Kalshi market trades from credential-free public market-data JSON.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous Kalshi response; `limit` (integer, optional) — Rows to return, default 25, max 200; `max_ts` (integer, optional) — Maximum created Unix timestamp in seconds; `min_ts` (integer, optional) — Minimum created Unix timestamp in seconds; `ticker` (string, optional) — Kalshi market ticker filter

## Letterboxd (8)

### `letterboxd_film`

- **HTTP:** `GET /letterboxd/film/{slug}`
- **What:** Get a Letterboxd film. Returns a normalized Letterboxd film: synopsis, director, cast, genres, countries, languages, runtime, and aggregate member rating. Credential-free public Letterboxd data (letterboxd.com), parsed from the film page's schema.org structured data.
- **Params:** `slug` (string, **required**) — Letterboxd film slug

### `letterboxd_film_rating_histogram`

- **HTTP:** `GET /letterboxd/film/{slug}/rating-histogram`
- **What:** Get a Letterboxd film's rating distribution. Returns a film's full star-rating distribution (0.5 to 5.0 in half-star buckets) with counts and percentages. Credential-free public Letterboxd data.
- **Params:** `slug` (string, **required**) — Letterboxd film slug

### `letterboxd_film_reviews`

- **HTTP:** `GET /letterboxd/film/{slug}/reviews`
- **What:** Get a Letterboxd film's popular reviews. Returns a film's popular reviews (reviewer, rating, date, text, like/comment counts, spoiler flag). Credential-free public Letterboxd data.
- **Params:** `limit` (integer, optional) — Max reviews, default 10, max 50; `slug` (string, **required**) — Letterboxd film slug

### `letterboxd_film_similar`

- **HTTP:** `GET /letterboxd/film/{slug}/similar`
- **What:** Get films similar to a Letterboxd film. Returns films Letterboxd recommends as similar to the given film. Credential-free public Letterboxd data.
- **Params:** `limit` (integer, optional) — Max films, default 10, max 50; `slug` (string, **required**) — Letterboxd film slug

### `letterboxd_member`

- **HTTP:** `GET /letterboxd/member/{username}`
- **What:** Get a Letterboxd member's public profile stats. Returns a member's public profile stats (films watched, lists, following/followers). No private data — everything is visible to a logged-out visitor. Credential-free public Letterboxd data.
- **Params:** `username` (string, **required**) — Letterboxd username

### `letterboxd_person`

- **HTTP:** `GET /letterboxd/person/{slug}`
- **What:** Get a Letterboxd person's filmography. Returns a person's Letterboxd filmography for a credit role. Credential-free public Letterboxd data.
- **Params:** `limit` (integer, optional) — Max films, default 10, max 50; `role` (string, optional) — Credit role, default actor; `slug` (string, **required**) — Letterboxd person slug

### `letterboxd_popular`

- **HTTP:** `GET /letterboxd/popular`
- **What:** Get a Letterboxd popularity-ranked film chart. Returns a popularity-ranked film chart, optionally scoped to a time window, genre, and/or decade. Credential-free public Letterboxd data.
- **Params:** `decade` (string, optional) — Decade filter, e.g. 2010s; `genre` (string, optional) — Genre slug filter; `limit` (integer, optional) — Max films, default 10, max 50; `period` (string, optional) — Popularity window, omit for all-time

### `letterboxd_search`

- **HTTP:** `GET /letterboxd/search`
- **What:** Search Letterboxd. Searches Letterboxd films, people, lists, and tags. Credential-free public Letterboxd data.
- **Params:** `limit` (integer, optional) — Max results, default 10, max 50; `q` (string, **required**) — Search query; `type` (string, optional) — Optional result type filter

## LinkedIn (3)

### `linkedin_company`

- **HTTP:** `GET /linkedin/company/{id}`
- **What:** Get LinkedIn Company info by ID. Returns detailed company information by LinkedIn ID.
- **Params:** `id` (string, **required**) — LinkedIn Company ID

### `linkedin_product`

- **HTTP:** `GET /linkedin/product/{id}`
- **What:** Get LinkedIn Product info by ID. Returns detailed product information from LinkedIn by product ID.
- **Params:** `id` (string, **required**) — LinkedIn Product ID

### `linkedin_showcase`

- **HTTP:** `GET /linkedin/showcase/{id}`
- **What:** Get Linkedin Showcase Page Info. Returns detailed information about a LinkedIn showcase page by ID.
- **Params:** `id` (string, **required**) — LinkedIn Showcase Page ID

## Manga (3)

### `manga_rankings`

- **HTTP:** `GET /manga/rankings`
- **What:** Rank manga. Returns a filterable, sorted manga ranking. Credential-free public AniList data. Filter by format, genre, and status.
- **Params:** `format` (string, optional) — Format filter: MANGA, NOVEL, ONE_SHOT.; `genre` (string, optional) — Genre filter, e.g. Fantasy.; `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 20, max 50; `sort` (string, optional) — Order: TRENDING_DESC, POPULARITY_DESC, SCORE_DESC, FAVOURITES_DESC, START_DATE_DESC, UPDATED_AT_DESC. Default TRENDING_DESC.; `status` (string, optional) — Status filter: FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED, HIATUS.

### `manga_search`

- **HTTP:** `GET /manga/search`
- **What:** Search manga. Searches manga by free-text query. Credential-free public manga data from AniList. Returns normalized entries: titles, scores, popularity, format, status, chapters, volumes, genres, and tags.
- **Params:** `page` (integer, optional) — 1-based page number, default 1; `per_page` (integer, optional) — Results per page, default 10, max 50; `query` (string, **required**) — Search text; `sort` (string, optional) — Ordering: SEARCH_MATCH, POPULARITY_DESC, SCORE_DESC, TRENDING_DESC, FAVOURITES_DESC, START_DATE_DESC. Default SEARCH_MATCH.

### `manga_title`

- **HTTP:** `GET /manga/title/{id}`
- **What:** Get a manga. Returns a normalized manga by AniList id: titles, MyAnimeList id, scores, popularity, favourites, format, status, chapters, volumes, genres, ranked tags, dates, description, and images. Pass mal=true to additionally enrich the response with the MyAnimeList community score (mal block: score on a 0-10 scale, plus scored-by count), scraped credential-free from the public MAL page. Credential-free public AniList data.
- **Params:** `id` (string, **required**) — AniList manga id; `mal` (boolean, optional) — Enrich with the MyAnimeList community score (adds one fetch; omitted when the title has no MAL id)

## Mercari (5)

### `mercari_autocomplete`

- **HTTP:** `GET /mercari/autocomplete`
- **What:** Mercari search autocomplete. Returns Mercari's own search-suggestion list for a partial keyword, in the upstream's own relevance order. An empty suggestion list is a normal outcome for obscure or gibberish input. Credential-free public data sourced from Mercari's own mobile-app API using an anonymous, login-free session.
- **Params:** `query` (string, **required**) — Partial keyword to get suggestions for

### `mercari_home`

- **HTTP:** `GET /mercari/home`
- **What:** Get Mercari home feed. Returns Mercari's own curated home-feed recommendations: normalized listing summaries (title, price, thumbnail, condition, seller). Credential-free public data sourced from Mercari's own mobile-app API using an anonymous, login-free session.
- **Params:** _none_

### `mercari_item`

- **HTTP:** `GET /mercari/item/{id}`
- **What:** Get Mercari item detail. Returns a normalized Mercari item-detail page: description, all photos, price, condition, category, hashtags, the shipping origin state, and a "similar items" carousel of related listings. Credential-free public data sourced from Mercari's own mobile-app API using an anonymous, login-free session.
- **Params:** `id` (string, **required**) — Mercari item id, e.g. from a search result's id field

### `mercari_master`

- **HTTP:** `GET /mercari/master`
- **What:** Get Mercari full taxonomy (categories, brands, sizes). Returns Mercari's full reference taxonomy in one call: every category (with parent linkage), every recognized brand, and every clothing/shoe/apparel size. Large (tens of thousands of brand entries) and effectively static -- cache this response rather than polling it. Credential-free public data sourced from Mercari's own mobile-app API using an anonymous, login-free session.
- **Params:** _none_

### `mercari_search`

- **HTTP:** `GET /mercari/search`
- **What:** Search Mercari listings. Searches Mercari's live resale marketplace by free-text keyword, returning normalized listing summaries (title, price, thumbnail, condition, seller) plus the total matching count. Credential-free public data sourced from Mercari's own mobile-app API using an anonymous, login-free session.
- **Params:** `query` (string, **required**) — Free-text keyword search

## Meta Jobs (3)

### `meta_jobs_job`

- **HTTP:** `GET /meta-jobs/job`
- **What:** Meta Jobs single posting. Returns one Meta Careers posting by its numeric job id (the `id` field returned by search or list). Parsed from metacareers.com's server-rendered job detail page.
- **Params:** `id` (string, **required**) — Meta job id

### `meta_jobs_list`

- **HTTP:** `GET /meta-jobs/list`
- **What:** Meta Jobs catalog listing. Returns a page of Meta's own public job sitemap -- every open requisition's id, canonical URL, and last-modified timestamp, with no team/location/keyword filtering. Use this for full-catalog enumeration or change tracking via last_modified; use search when you need to filter by team, technology, location, employment type, or keyword.
- **Params:** `page` (integer, optional) — Page number, 1-based, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 50, maxes at 200

### `meta_jobs_search`

- **HTTP:** `GET /meta-jobs/search`
- **What:** Meta Jobs search. Searches Meta's public careers site (metacareers.com) via its own anonymous jobsearch GraphQL endpoint, with the same team/technology/location/employment-type/keyword/remote/sort filters the live search page offers. All filters are optional and combine with AND semantics; an empty request returns Meta's entire open-requisition catalog in one response. `q` matches team, technology, location, or ref/req-code names -- it is NOT a free-text search over job titles or descriptions. `teams` enum (org teams + technologies, both use the same field): `Advertising Technology`, `AR/VR`, `Artificial Intelligence`, `Business Development & Partnerships`, `Communications & Public Policy`, `Creative`, `Data & Analytics`, `Data Center`, `Design & User Experience`, `Enterprise Engineering`, `Global Operations`, `Infrastructure`, `Internship - Business`, `Internship - Engineering, Tech & Design`, `Internship - PhD`, `Legal, Finance, Facilities & Admin`, `People & Recruiting`, `Product Management`, `Research`, `Sales & Marketing`, `Security`, `Software Engineering`, `Technical Program Management`, `University Grad - Business`, `University Grad - Engineering, Tech & Design`, `University Grad - PhD & Postdoc`, `Facebook`, `Messenger`, `Instagram`, `WhatsApp`, `Meta Quest`. `roles` enum: `Full time employment`, `Internship`, `Short term employment`. `results_per_page` enum: `all`, `five`, `ten`.
- **Params:** `is_remote_only` (boolean, optional) — Restrict to remote-only postings; `offices` (array, optional) — Repeatable location-id filter (OR) in Meta's own id format, e.g. menlo-park, london -- not a closed enum; `q` (string, optional) — Facet-name keyword: matches team, technology, location, or ref/req-code -- not a title/description search; `results_per_page` (string, optional) — Response size cap: all, five, ten; `roles` (array, optional) — Repeatable employment-type filter (OR); see roles enum above; `sort_by_new` (boolean, optional) — Sort newest-first instead of relevance; `teams` (array, optional) — Repeatable team-or-technology filter (OR); see teams enum above

## Metacritic (10)

### `metacritic_browse`

- **HTTP:** `GET /metacritic/browse`
- **What:** Browse Metacritic titles. Browse Metacritic titles by content type, optionally filtered by genre and ordered by Metascore, popularity, or release date. Returns paginated title cards with Metascore and user score. Credential-free public Metacritic data.
- **Params:** `genre` (string, optional) — Genre filter (e.g. Action); `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 24, max 100); `sort` (string, optional) — Sort order; `type` (string, **required**) — Content type

### `metacritic_game`

- **HTTP:** `GET /metacritic/game/{slug}`
- **What:** Get a Metacritic game. Returns a normalized Metacritic game: Metascore (critic) and user score with sentiment and review counts, genres, per-platform scores, developer/publisher, rating, release date, and trailer. Credential-free public Metacritic data.
- **Params:** `slug` (string, **required**) — Metacritic game slug

### `metacritic_game_critic_reviews`

- **HTTP:** `GET /metacritic/game/{slug}/critic-reviews`
- **What:** List a Metacritic game's critic reviews. Returns paginated professional/publication reviews for a game: publication, score, quote, author, platform, and source URL. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic game slug; `sort` (string, optional) — Sort order

### `metacritic_game_user_reviews`

- **HTTP:** `GET /metacritic/game/{slug}/user-reviews`
- **What:** List a Metacritic game's user reviews. Returns paginated user reviews for a game: author, score (0-10), quote, date, platform, helpfulness, and spoiler flag. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic game slug; `sort` (string, optional) — Sort order

### `metacritic_movie`

- **HTTP:** `GET /metacritic/movie/{slug}`
- **What:** Get a Metacritic movie. Returns a normalized Metacritic movie: Metascore (critic) and user score with sentiment and review counts, genres, cast/crew, rating, runtime, release date, IMDb id, and trailer. Credential-free public Metacritic data.
- **Params:** `slug` (string, **required**) — Metacritic movie slug

### `metacritic_movie_critic_reviews`

- **HTTP:** `GET /metacritic/movie/{slug}/critic-reviews`
- **What:** List a Metacritic movie's critic reviews. Returns paginated professional/publication reviews for a movie: publication, score, quote, author, and source URL. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic movie slug; `sort` (string, optional) — Sort order

### `metacritic_movie_user_reviews`

- **HTTP:** `GET /metacritic/movie/{slug}/user-reviews`
- **What:** List a Metacritic movie's user reviews. Returns paginated user reviews for a movie: author, score (0-10), quote, date, helpfulness, and spoiler flag. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic movie slug; `sort` (string, optional) — Sort order

### `metacritic_tv`

- **HTTP:** `GET /metacritic/tv/{slug}`
- **What:** Get a Metacritic TV show. Returns a normalized Metacritic TV show: Metascore (critic) and user score with sentiment and review counts, genres, networks, season count, rating, release date, IMDb id, and trailer. Credential-free public Metacritic data.
- **Params:** `slug` (string, **required**) — Metacritic TV show slug

### `metacritic_tv_critic_reviews`

- **HTTP:** `GET /metacritic/tv/{slug}/critic-reviews`
- **What:** List a Metacritic TV show's critic reviews. Returns paginated professional/publication reviews for a TV show: publication, score, quote, author, and source URL. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic TV show slug; `sort` (string, optional) — Sort order

### `metacritic_tv_user_reviews`

- **HTTP:** `GET /metacritic/tv/{slug}/user-reviews`
- **What:** List a Metacritic TV show's user reviews. Returns paginated user reviews for a TV show: author, score (0-10), quote, date, helpfulness, and spoiler flag. Credential-free public Metacritic data.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `per_page` (integer, optional) — Results per page (default 20, max 50); `slug` (string, **required**) — Metacritic TV show slug; `sort` (string, optional) — Sort order

## Metaculus (11)

### `metaculus_category_questions`

- **HTTP:** `GET /metaculus/category/{slug}/questions`
- **What:** Metaculus category questions. Returns normalized Metaculus question rows from a credential-free public category feed page. Allowed category slugs: artificial-intelligence, computing-and-math, cryptocurrencies, economy-business, elections, environment-climate, geopolitics, health-pandemics, law, metaculus, natural-sciences, nuclear, politics, social-sciences, space, sports-entertainment, technology.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `slug` (string, **required**) — Metaculus category slug

### `metaculus_comments_feed`

- **HTTP:** `GET /metaculus/comments-feed`
- **What:** Metaculus comments feed. Returns normalized Metaculus question rows for the questions referenced by the most recent public comments, in comment recency order. Derived from credential-free public Metaculus data; upstream comment bodies are not exposed.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `topic` (string, optional) — Optional Metaculus topic slug

### `metaculus_project_questions`

- **HTTP:** `GET /metaculus/project/{slug}/questions`
- **What:** Metaculus project questions. Returns normalized Metaculus question rows for one public project, filtered by its slug. A slug that does not exist returns 404.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `slug` (string, **required**) — Metaculus project slug

### `metaculus_question`

- **HTTP:** `GET /metaculus/question/{id}`
- **What:** Metaculus question detail. Returns one normalized Metaculus question from credential-free public page data.
- **Params:** `id` (string, **required**) — Metaculus question or post id

### `metaculus_question_forecast_history`

- **HTTP:** `GET /metaculus/question/{id}/forecast-history`
- **What:** Metaculus question forecast history. Returns public aggregation forecast history points for one Metaculus question from credential-free public page data. The `method` enum accepts `recency_weighted`, `unweighted`, and `single_aggregation`.
- **Params:** `id` (string, **required**) — Metaculus question or post id; `max_points` (integer, optional) — Maximum history points to return, default 500, max 2000; `method` (string, optional) — Aggregation method

### `metaculus_question_forecasts`

- **HTTP:** `GET /metaculus/question/{id}/forecasts`
- **What:** Metaculus question forecasts. Returns compact public latest forecast summaries by aggregation method for one Metaculus question.
- **Params:** `id` (string, **required**) — Metaculus question or post id

### `metaculus_question_metadata`

- **HTTP:** `GET /metaculus/question/{id}/metadata`
- **What:** Metaculus question metadata. Returns public metadata for one Metaculus question, including option labels, option history, scaling metadata, resolution fields, and timing fields when present.
- **Params:** `id` (string, **required**) — Metaculus question or post id

### `metaculus_question_options`

- **HTTP:** `GET /metaculus/question/{id}/options`
- **What:** Metaculus question options. Returns public multiple-choice option labels and latest option-level forecast values for one Metaculus question. The `method` enum accepts `recency_weighted`, `unweighted`, and `single_aggregation`.
- **Params:** `id` (string, **required**) — Metaculus question or post id; `method` (string, optional) — Aggregation method

### `metaculus_questions`

- **HTTP:** `GET /metaculus/questions`
- **What:** Metaculus questions. Returns normalized Metaculus question rows from credential-free public page data. The endpoint fails closed on authenticated API responses or Cloudflare challenge pages.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `topic` (string, optional) — Optional Metaculus topic slug

### `metaculus_top_comments`

- **HTTP:** `GET /metaculus/top-comments`
- **What:** Metaculus top comments feed. Returns normalized Metaculus question rows for the questions whose recent public comments collected the highest vote scores over roughly the last week. Derived from credential-free public Metaculus data; upstream comment bodies are not exposed.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `topic` (string, optional) — Optional Metaculus topic slug

### `metaculus_tournament_questions`

- **HTTP:** `GET /metaculus/tournament/{slug}/questions`
- **What:** Metaculus tournament questions. Returns normalized Metaculus question rows for one public tournament, filtered by its slug. A slug that does not exist returns 404.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 25; `slug` (string, **required**) — Metaculus tournament slug

## MLB (12)

### `mlb_game`

- **HTTP:** `GET /mlb/game`
- **What:** Get an MLB game feed. Returns a compact MLB game feed with status, teams, score, innings, probable pitchers, decisions, and team box-score totals.
- **Params:** `id` (string, **required**) — Numeric MLB game id

### `mlb_game_boxscore`

- **HTTP:** `GET /mlb/game-boxscore`
- **What:** Get an MLB player boxscore. Returns both teams' player batting, pitching, and fielding lines for a game.
- **Params:** `id` (string, **required**) — Numeric MLB game id

### `mlb_game_play_by_play`

- **HTTP:** `GET /mlb/game-play-by-play`
- **What:** Get MLB game play-by-play. Returns every at-bat and pitch/event record for an MLB game.
- **Params:** `id` (string, **required**) — Numeric MLB game id

### `mlb_league_stats`

- **HTTP:** `GET /mlb/league-stats`
- **What:** Get ranked MLB league statistics. Returns ranked MLB season stat splits across both leagues. The group enum accepts `hitting`, `pitching`, and `fielding`.
- **Params:** `group` (string, **required**) — Stat group; `limit` (integer, optional) — Results to return (1-100); `season` (integer, optional) — Four-digit season; defaults to current year

### `mlb_player`

- **HTTP:** `GET /mlb/player`
- **What:** Get an MLB player. Returns an MLB player's identity, biographical information, position, handedness, active status, and current team.
- **Params:** `id` (string, **required**) — Numeric MLB player id

### `mlb_player_stats`

- **HTTP:** `GET /mlb/player-stats`
- **What:** Get MLB player season statistics. Returns one player's MLB season statistics. The group enum accepts `hitting`, `pitching`, and `fielding`.
- **Params:** `group` (string, **required**) — Stat group; `id` (string, **required**) — Numeric MLB player id; `season` (integer, optional) — Four-digit season; defaults to current year

### `mlb_schedule`

- **HTTP:** `GET /mlb/schedule`
- **What:** Get the MLB schedule and scores. Returns MLB games, teams, scores, status, probable pitchers, venue, and series information for one date or date range, optionally filtered to a team.
- **Params:** `date` (string, optional) — Single date in YYYY-MM-DD format; `end_date` (string, optional) — Range end in YYYY-MM-DD format; `start_date` (string, optional) — Range start in YYYY-MM-DD format; `team_id` (string, optional) — Numeric MLB team id

### `mlb_standings`

- **HTTP:** `GET /mlb/standings`
- **What:** Get MLB standings. Returns American League and National League standings grouped by division. The type enum accepts `regularSeason`, `wildCard`, and `springTraining`.
- **Params:** `season` (integer, optional) — Four-digit season; defaults to current year; `type` (string, optional) — Standings type

### `mlb_team_roster`

- **HTTP:** `GET /mlb/team-roster`
- **What:** Get an MLB team roster. Returns a team's players, jersey numbers, positions, and roster status. The roster_type enum accepts `active`, `40Man`, and `fullSeason`.
- **Params:** `roster_type` (string, optional) — Roster type; `season` (integer, optional) — Four-digit season; defaults to current year; `team_id` (string, **required**) — Numeric MLB team id

### `mlb_team_stats`

- **HTTP:** `GET /mlb/team-stats`
- **What:** Get MLB team season statistics. Returns one team's season statistics. Group accepts `hitting`, `pitching`, and `fielding`.
- **Params:** `group` (string, **required**) — Statistics group; `season` (integer, optional) — Four-digit season; `team_id` (string, **required**) — Numeric MLB team id

### `mlb_teams`

- **HTTP:** `GET /mlb/teams`
- **What:** List MLB teams. Returns the 30 MLB clubs for a season with league, division, venue, and abbreviation metadata.
- **Params:** `season` (integer, optional) — Four-digit season; defaults to current year

### `mlb_transactions`

- **HTTP:** `GET /mlb/transactions`
- **What:** List MLB transactions. Lists signings, trades, options, assignments, injured-list moves, and other MLB transactions for a date range.
- **Params:** `end_date` (string, **required**) — Range end in YYYY-MM-DD format; `player_id` (string, optional) — Numeric MLB player id; `start_date` (string, **required**) — Range start in YYYY-MM-DD format; `team_id` (string, optional) — Numeric MLB team id

## Numbeo (8)

### `numbeo_cost_of_living_city`

- **HTTP:** `GET /numbeo/cost-of-living/city/{slug}`
- **What:** Get a Numbeo city's cost-of-living prices. Returns itemized cost-of-living prices for one city (restaurants, markets, transportation, utilities, rent, and more), grouped by category. Credential-free public Numbeo data (numbeo.com).
- **Params:** `slug` (string, **required**) — Numbeo city slug

### `numbeo_cost_of_living_country`

- **HTTP:** `GET /numbeo/cost-of-living/country`
- **What:** Get a Numbeo country's cost-of-living prices. Returns aggregate itemized cost-of-living prices for a country, plus the headline cost-of-living indices for every city Numbeo tracks there. Credential-free public Numbeo data (numbeo.com).
- **Params:** `country` (string, **required**) — Country name as Numbeo spells it

### `numbeo_cost_of_living_rankings`

- **HTTP:** `GET /numbeo/cost-of-living/rankings`
- **What:** Get the global Numbeo cost-of-living city ranking. Returns the global cost-of-living city ranking (Cost of Living, Rent, Cost of Living Plus Rent, Groceries, Restaurant Price, and Local Purchasing Power indices), either the continuously-updated current index or a historical periodic snapshot. Credential-free public Numbeo data (numbeo.com).
- **Params:** `period` (string, optional) — Required when scope=historical, e.g. 2026-mid or 2025; `scope` (string, optional) — current (default) or historical

### `numbeo_cost_of_living_rankings_by_country`

- **HTTP:** `GET /numbeo/cost-of-living/rankings-by-country`
- **What:** Get the global Numbeo cost-of-living country ranking. Returns the global country-level cost-of-living ranking (Cost of Living, Rent, Cost of Living Plus Rent, Groceries, Restaurant Price, and Local Purchasing Power indices). Credential-free public Numbeo data (numbeo.com).
- **Params:** _none_

### `numbeo_indices_city`

- **HTTP:** `GET /numbeo/indices/city/{slug}`
- **What:** Get a Numbeo city's data for an index family. Returns one city's data for a Numbeo index family (quality of life, crime, health care, pollution, traffic, or property investment): headline indices, and (depending on the family) titled sub-index sections and/or itemized prices. Credential-free public Numbeo data (numbeo.com).
- **Params:** `index` (string, **required**) — Index family; `slug` (string, **required**) — Numbeo city slug

### `numbeo_indices_country`

- **HTTP:** `GET /numbeo/indices/country`
- **What:** Get a Numbeo country's data for an index family. Returns one country's aggregate data for a Numbeo index family, plus every city Numbeo tracks there with its index breakdown. Credential-free public Numbeo data (numbeo.com).
- **Params:** `country` (string, **required**) — Country name as Numbeo spells it; `index` (string, **required**) — Index family

### `numbeo_indices_rankings`

- **HTTP:** `GET /numbeo/indices/rankings`
- **What:** Get the global Numbeo city ranking for an index family. Returns the global city ranking for a Numbeo index family, either the continuously-updated current index or a historical periodic snapshot. Credential-free public Numbeo data (numbeo.com).
- **Params:** `index` (string, **required**) — Index family; `period` (string, optional) — Required when scope=historical, e.g. 2026-mid or 2025; `scope` (string, optional) — current (default) or historical

### `numbeo_indices_rankings_by_country`

- **HTTP:** `GET /numbeo/indices/rankings-by-country`
- **What:** Get the global Numbeo country ranking for an index family. Returns the global country-level ranking for a Numbeo index family. Credential-free public Numbeo data (numbeo.com).
- **Params:** `index` (string, **required**) — Index family

## OpenTable (4)

### `opentable_restaurant`

- **HTTP:** `GET /opentable/restaurant`
- **What:** Get an OpenTable restaurant's profile and live availability. Returns a restaurant's profile (location, cuisines, hours, price band, review summary) plus real-time bookable timeslots for the given date/time and party size. Credential-free.
- **Params:** `date_time` (string, optional) — Reservation date/time, RFC3339-minute local format; defaults to now; `party_size` (integer, optional) — Party size, default 2; `restaurant_id` (string, **required**) — OpenTable restaurant id

### `opentable_restaurant_menus`

- **HTTP:** `GET /opentable/restaurant/menus`
- **What:** Get an OpenTable restaurant's menus. Returns a restaurant's menus (sections, items, prices). Credential-free.
- **Params:** `restaurant_id` (string, **required**) — OpenTable restaurant id

### `opentable_restaurant_reviews`

- **HTTP:** `GET /opentable/restaurant/reviews`
- **What:** Get a page of an OpenTable restaurant's diner reviews. Returns a page of diner reviews (author, text, per-category ratings) for a restaurant. Credential-free.
- **Params:** `page` (integer, optional) — Page number, default 1; `restaurant_id` (string, **required**) — OpenTable restaurant id; `size` (integer, optional) — Reviews per page, default 20

### `opentable_search`

- **HTTP:** `GET /opentable/search`
- **What:** Search OpenTable restaurants near a location. Searches restaurants by free-text term (cuisine, name, neighborhood) near a latitude/longitude, for a given date/time and party size, including inline live availability per result. Credential-free.
- **Params:** `date_time` (string, optional) — Reservation date/time, RFC3339-minute local format; defaults to now; `latitude` (number, **required**) — Search center latitude; `longitude` (number, **required**) — Search center longitude; `party_size` (integer, optional) — Party size, default 2; `size` (integer, optional) — Max results, default 10; `term` (string, **required**) — Free-text search term

## Pinterest (8)

### `pinterest_board`

- **HTTP:** `GET /pinterest/board/{username}/{slug}`
- **What:** Get a Pinterest board's detail. Returns a Pinterest board's metadata (name, description, cover image, pin/follower counts, owner) plus a page of pins from that board. Public data sourced from Pinterest's own board pages.
- **Params:** `slug` (string, **required**) — Board URL slug, from the board's own /{username}/{slug}/ URL; `username` (string, **required**) — Pinterest username that owns the board

### `pinterest_categories`

- **HTTP:** `GET /pinterest/categories`
- **What:** Get Pinterest's "Ideas" category list. Returns Pinterest's top-level "Ideas" category taxonomy (e.g. "Animals", "Home Decor", "Food And Drink"). Each entry's id is usable directly with GET /pinterest/ideas/{id}. Public data sourced from Pinterest's own ideas.pinterest.com-style category hub.
- **Params:** _none_

### `pinterest_idea`

- **HTTP:** `GET /pinterest/ideas/{id}`
- **What:** Get a Pinterest "Ideas" category's detail feed. Returns one "Ideas" category's metadata (name, description, follower count) plus a page of pins from that category's feed. Public data sourced from Pinterest's own ideas category pages.
- **Params:** `id` (string, **required**) — Pinterest ideas category id. See GET /pinterest/categories for the full list.

### `pinterest_pin`

- **HTTP:** `GET /pinterest/pin/{id}`
- **What:** Get a Pinterest pin's full detail. Returns a single Pinterest pin's full detail: title, description, image, board, pinner, comment count, save count, and creation time. Public data sourced from Pinterest's own pin pages.
- **Params:** `id` (string, **required**) — Pinterest pin id

### `pinterest_search`

- **HTTP:** `GET /pinterest/search`
- **What:** Search Pinterest pins. Returns public Pinterest pins matching a text query: title, description, image, board, and pinner for each result. Public data sourced from Pinterest's own web search.
- **Params:** `query` (string, **required**) — Search text

### `pinterest_user`

- **HTTP:** `GET /pinterest/user/{username}`
- **What:** Get a Pinterest user's public profile. Returns a Pinterest user's public profile: display name, bio, website, avatar, and follower/following/pin/board counts. Public data sourced from Pinterest's own profile pages.
- **Params:** `username` (string, **required**) — Pinterest username

### `pinterest_user_boards`

- **HTTP:** `GET /pinterest/user/{username}/boards`
- **What:** Get a Pinterest user's boards. Returns a page of a Pinterest user's own boards: name, description, cover image, and pin/follower counts for each. Public data sourced from Pinterest's own profile pages.
- **Params:** `username` (string, **required**) — Pinterest username

### `pinterest_user_pins`

- **HTTP:** `GET /pinterest/user/{username}/pins`
- **What:** Get a Pinterest user's own pins. Returns a page of a Pinterest user's own pins: title, description, image, board, and pinner for each. Public data sourced from Pinterest's own profile pages.
- **Params:** `username` (string, **required**) — Pinterest username

## PitchBook (5)

### `pitchbook_advisor`

- **HTTP:** `GET /pitchbook/advisor`
- **What:** PitchBook advisor profile. Returns the free/teaser content of a PitchBook advisor (service provider, e.g. investment bank, lender, or financing advisory firm) profile page: overview, description, contact/HQ, and a preview of serviced companies/deals, co-lenders, and subsidiaries. PitchBook gates most numeric figures and full lists behind a paid subscription; those come through as empty cells rather than being fabricated. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — PitchBook advisor id; `url` (string, optional) — Absolute https://pitchbook.com/profiles/advisor/<id> URL

### `pitchbook_company`

- **HTTP:** `GET /pitchbook/company`
- **What:** PitchBook company profile. Returns the free/teaser content of a PitchBook company profile page (overview, description, contact/HQ, industry, funding-round history without dollar amounts, a preview of investors, acquisitions, and subsidiaries). PitchBook gates most numeric figures (deal amounts, cap tables, full investor/LP lists) behind a paid subscription; those come through as empty cells rather than being fabricated. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — PitchBook company id; `url` (string, optional) — Absolute https://pitchbook.com/profiles/company/<id> URL

### `pitchbook_fund`

- **HTTP:** `GET /pitchbook/fund`
- **What:** PitchBook fund profile. Returns the free/teaser content of a PitchBook fund profile page (strategy, status, manager, size, vintage, and a preview of limited partners and benchmark peer funds). PitchBook gates most numeric figures (returns/IRR, full LP lists) behind a paid subscription; those come through as empty cells rather than being fabricated. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — PitchBook fund id; `url` (string, optional) — Absolute https://pitchbook.com/profiles/fund/<id> URL

### `pitchbook_investor`

- **HTTP:** `GET /pitchbook/investor`
- **What:** PitchBook investor profile. Returns the free/teaser content of a PitchBook investor (fund manager/firm) profile page (overview, description, contact/HQ, and a preview of investments, exits, and co-investors). PitchBook gates most numeric figures and full lists behind a paid subscription; those come through as empty cells rather than being fabricated. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — PitchBook investor id; `url` (string, optional) — Absolute https://pitchbook.com/profiles/investor/<id> URL

### `pitchbook_limited_partner`

- **HTTP:** `GET /pitchbook/limited-partner`
- **What:** PitchBook limited partner profile. Returns the free/teaser content of a PitchBook limited partner (institutional investor, e.g. pension fund, endowment, or insurance company) profile page: overview, description, contact, and a preview of fund commitments. PitchBook gates most numeric figures and full lists behind a paid subscription; those come through as empty cells rather than being fabricated. Some limited partner profiles have no FAQ section (thinner profiles) -- this is normal, not a sign of a blocked or broken response. Pass exactly one of `id` or `url`.
- **Params:** `id` (string, optional) — PitchBook limited partner id; `url` (string, optional) — Absolute https://pitchbook.com/profiles/limited-partner/<id> URL

## PlayStation (8)

### `playstation_browse`

- **HTTP:** `GET /playstation/browse`
- **What:** Browse the PlayStation Store all-games grid. Returns a page of the PlayStation Store "all games" grid with per-item price, platforms, and media, plus the available filter facets (price, genre, platform, subscription, content type, etc.) with value counts. Pass page to advance; next_page is set when more results exist. cc selects the store region (and price currency) and l the text language. Credential-free public PlayStation Store data.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `l` (string, optional) — Language code; `page` (integer, optional) — 1-based page number

### `playstation_category`

- **HTTP:** `GET /playstation/category`
- **What:** Browse a PlayStation Store category grid. Returns a page of a specific PlayStation Store category grid (by category UUID) with per-item price, platforms, and media, plus the available filter facets with value counts. Pass page to advance; next_page is set when more results exist. cc selects the store region (and price currency) and l the text language. Credential-free public PlayStation Store data.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `id` (string, **required**) — Category UUID; `l` (string, optional) — Language code; `page` (integer, optional) — 1-based page number

### `playstation_concept`

- **HTTP:** `GET /playstation/concept`
- **What:** Get PlayStation Store details for a concept (game hub). Returns normalized store metadata for a PlayStation concept: title, publisher, release date, platforms, genres, description, content rating, aggregate star rating, the default product's purchase price, media, and the full lists of purchasable editions and add-ons. cc selects the store region (and price currency) and l the text language. Credential-free public PlayStation Store data.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `id` (string, **required**) — Numeric PlayStation concept id; `l` (string, optional) — Language code

### `playstation_deals`

- **HTTP:** `GET /playstation/deals`
- **What:** Get PlayStation Store deals shelves. Returns the PlayStation Store deals landing page as a list of merchandising shelves (sections), each with its titles and per-item price, plus a flattened, de-duplicated item list across all shelves. cc selects the store region (and price currency) and l the text language. Credential-free public PlayStation Store data.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `l` (string, optional) — Language code

### `playstation_latest`

- **HTTP:** `GET /playstation/latest`
- **What:** Get PlayStation Store latest-release shelves. Returns the PlayStation Store latest-releases landing page as a list of merchandising shelves (sections), each with its titles and per-item price, plus a flattened, de-duplicated item list across all shelves. cc selects the store region (and price currency) and l the text language. Credential-free public PlayStation Store data.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `l` (string, optional) — Language code

### `playstation_page`

- **HTTP:** `GET /playstation/page`
- **What:** Get a PlayStation Store merchandising page by alias. Reads any PlayStation Store merchandising page by alias (e.g. collections, subscriptions, or a promotional alias) and returns its shelves (sections) plus the curated collection links found on the page. Each collection link carries a category_id (UUID) you can pass to /playstation/category to fetch that collection's full, paginated title grid — the credential-free way to browse themed/curated selections. Known aliases: collections, subscriptions, deals, latest. cc selects the store region (and price currency) and l the text language. Credential-free public PlayStation Store data.
- **Params:** `alias` (string, **required**) — Merchandising page alias; `cc` (string, optional) — Store country code (ISO, selects currency); `l` (string, optional) — Language code

### `playstation_product`

- **HTTP:** `GET /playstation/product`
- **What:** Get PlayStation Store details for a single product. Returns normalized store metadata for a single PlayStation product/edition: title, np title id, parent concept id, product type and store classification, edition name, publisher, release date, platforms, genres, spoken/screen languages, content rating, aggregate star rating, purchase price, and media. cc selects the store region (and price currency) and l the text language. Credential-free public PlayStation Store data.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `id` (string, **required**) — PlayStation product id; `l` (string, optional) — Language code

### `playstation_search`

- **HTTP:** `GET /playstation/search`
- **What:** Search the PlayStation Store. Returns a page of PlayStation Store search results (concepts and products) for a term, with pagination and per-item price, platforms, classification, and media. Pass page to advance; next_page is set when more results exist. cc selects the store region (and price currency) and l the text language. Credential-free public PlayStation Store data.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `l` (string, optional) — Language code; `page` (integer, optional) — 1-based page number; `term` (string, **required**) — Search term

## Polymarket (30)

### `polymarket_activity_trades`

- **HTTP:** `GET /polymarket/activity/trades`
- **What:** List Polymarket activity trades. Returns normalized public trade rows used by Polymarket's `/activity` page from credential-free Data API trades JSON. The `taker_only` enum accepts `true` and `false`; the `filter_type` enum accepts `CASH`; the `filter_amount` enum accepts `1`, `5`, `10`, `100`, `1000`, `10000`, and `100000`.
- **Params:** `event_id` (string, optional) — Optional Polymarket event id; `filter_amount` (string, optional) — Minimum filtered amount; `filter_type` (string, optional) — Activity amount filter type; `limit` (integer, optional) — Maximum trades, defaults to 50 and supports up to 100; `market` (string, optional) — Optional market condition id; `offset` (integer, optional) — Result offset, defaults to 0 and supports up to 10000; `taker_only` (string, optional) — Taker-only filter

### `polymarket_clob_market`

- **HTTP:** `GET /polymarket/clob/market/{condition_id}`
- **What:** Get Polymarket CLOB market. Returns one public CLOB market detail row by market condition id, including tokens, reward settings, order acceptance state, tags, and fees.
- **Params:** `condition_id` (string, **required**) — Polymarket market condition id

### `polymarket_dashboard_macro`

- **HTTP:** `GET /polymarket/dashboards/macro`
- **What:** List Polymarket macro dashboard events. Returns normalized macroeconomic event rows for Polymarket's `/dashboards/macro` page using credential-free Gamma `events/keyset` JSON with the `macro` tag.
- **Params:** `cursor` (string, optional) — Optional keyset cursor from a prior macro dashboard response; `limit` (integer, optional) — Maximum macro events, defaults to 20 and supports up to 100

### `polymarket_event_detail`

- **HTTP:** `GET /polymarket/event/{slug}`
- **What:** Get Polymarket event detail. Returns one normalized Polymarket event from credential-free public Gamma event JSON. This endpoint does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `slug` (string, **required**) — Polymarket event slug

### `polymarket_event_tags`

- **HTTP:** `GET /polymarket/events/{id}/tags`
- **What:** List tags for a Polymarket event. Returns normalized tag rows attached to one Polymarket event id.
- **Params:** `id` (string, **required**) — Polymarket event id

### `polymarket_events`

- **HTTP:** `GET /polymarket/events`
- **What:** List Polymarket events. Returns normalized event rows from Polymarket's credential-free public Gamma events JSON.
- **Params:** `ascending` (boolean, optional) — Sort ascending when true; `closed` (string, optional) — Closed filter; `limit` (integer, optional) — Maximum events, defaults to 25 and supports up to 100; `offset` (integer, optional) — Result offset, defaults to 0 and supports up to 10000; `order` (string, optional) — Sort field

### `polymarket_events_similar`

- **HTTP:** `GET /polymarket/events/similar`
- **What:** Find similar Polymarket events. Returns normalized similar events from Polymarket's credential-free public Gamma events/similar JSON.
- **Params:** `closed` (string, optional) — Closed filter; `event_slug` (string, optional) — Event slug; `event_title` (string, optional) — Event title; `id` (integer, optional) — Polymarket event id; `limit` (integer, optional) — Maximum events, defaults to 10 and supports up to 50; `market_slug` (string, optional) — Market slug; `market_title` (string, optional) — Market title

### `polymarket_homepage_feed`

- **HTTP:** `GET /polymarket/homepage/feed`
- **What:** List Polymarket homepage feed rows. Returns normalized rows for Polymarket homepage feeds discovered from the public web app and backed by credential-free Gamma JSON. The `feed` enum accepts `trending`, `breaking`, `new`, `politics`, `sports`, `crypto`, `esports`, `iran`, `finance`, `geopolitics`, `tech`, `culture`, `economy`, `weather`, `mentions`, and `elections`. Most feeds return events from Gamma `events/keyset`; `breaking` returns high-movement market rows and `mentions` returns open event search matches.
- **Params:** `cursor` (string, optional) — Optional keyset cursor from a prior event feed response; `feed` (string, optional) — Homepage feed; `limit` (integer, optional) — Maximum rows, defaults to 20 and supports up to 100

### `polymarket_leaderboard`

- **HTTP:** `GET /polymarket/leaderboard`
- **What:** List Polymarket leaderboard rows. Returns normalized trader leaderboard rows from Polymarket's credential-free Data API leaderboard JSON. The `window` enum accepts `1d`, `7d`, `30d`, and `all`; the `sort_by` enum accepts `profit` and `volume`.
- **Params:** `limit` (integer, optional) — Maximum rows, defaults to 20 and supports up to 100; `sort_by` (string, optional) — Leaderboard sort; `window` (string, optional) — Leaderboard time window

### `polymarket_market_detail`

- **HTTP:** `GET /polymarket/market/{id}`
- **What:** Get Polymarket market detail by id. Returns one normalized Polymarket market from credential-free public Gamma market JSON. This endpoint does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `id` (string, **required**) — Polymarket market id

### `polymarket_market_liquidity`

- **HTTP:** `GET /polymarket/market/{id}/liquidity`
- **What:** Get Polymarket market liquidity. Returns a public market liquidity snapshot that joins Gamma market detail with credential-free public CLOB market-data reads when token ids are available. This endpoint is not a trading endpoint and does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `id` (string, **required**) — Polymarket market id

### `polymarket_market_tags`

- **HTTP:** `GET /polymarket/market/{id}/tags`
- **What:** List tags for a Polymarket market. Returns normalized tag rows attached to one Polymarket market id.
- **Params:** `id` (string, **required**) — Polymarket market id

### `polymarket_markets`

- **HTTP:** `GET /polymarket/markets`
- **What:** List Polymarket markets. Returns normalized market rows from Polymarket's credential-free public Gamma markets JSON.
- **Params:** `ascending` (boolean, optional) — Sort ascending when true; `closed` (string, optional) — Closed filter; `limit` (integer, optional) — Maximum markets, defaults to 25 and supports up to 100; `offset` (integer, optional) — Result offset, defaults to 0 and supports up to 10000; `order` (string, optional) — Sort field

### `polymarket_predictions`

- **HTTP:** `GET /polymarket/predictions`
- **What:** List Polymarket predictions. Returns normalized event rows for the Polymarket `/predictions` page using credential-free Gamma `events/keyset` JSON. The `status` enum accepts `active`, `resolved`, and `all`; the `sort` enum accepts `competitive`, `volume`, `volume_24hr`, `ending_soon`, `liquidity`, `newest`, and `closed_time`; the `recurrence` enum accepts `hourly`, `daily`, `weekly`, `monthly`, and `yearly`.
- **Params:** `cursor` (string, optional) — Optional keyset cursor from a prior predictions response; `limit` (integer, optional) — Maximum events, defaults to 20 and supports up to 100; `recurrence` (string, optional) — Optional recurrence filter; `sort` (string, optional) — Prediction sort; `status` (string, optional) — Prediction status; `tag` (string, optional) — Optional tag slug

### `polymarket_public_data`

- **HTTP:** `GET /polymarket/fee-types`
- **What:** Polymarket fee types. Returns public fee type data from Polymarket Gamma. This is a normalized wrapper around credential-free public JSON.
- **Params:** `active` (string, optional) — Optional upstream active filter; `search` (string, optional) — Optional upstream search filter

### `polymarket_related_tags`

- **HTTP:** `GET /polymarket/tag/{id}/related-tags`
- **What:** Get related Polymarket tags by id. Returns normalized related tag rows from Polymarket's credential-free public Gamma related-tags JSON.
- **Params:** `id` (string, **required**) — Polymarket tag id; `locale` (string, optional) — Optional upstream locale; `omit_empty` (string, optional) — Omit empty related tags; `status` (string, optional) — Optional upstream status filter

### `polymarket_rewards_market`

- **HTTP:** `GET /polymarket/rewards/market/{condition_id}`
- **What:** Get Polymarket rewards market. Returns one public rewards-market row from Polymarket CLOB rewards JSON by market condition id.
- **Params:** `condition_id` (string, **required**) — Polymarket market condition id

### `polymarket_rewards_markets`

- **HTTP:** `GET /polymarket/rewards/markets`
- **What:** List Polymarket rewards markets. Returns normalized public rewards-market rows used by Polymarket's `/rewards` page. The `order_by` enum accepts `market`, `earnings`, `max_spread`, `min_size`, `rate_per_day`, `price`, `earning_percentage`, and `spread`; the `position` enum accepts `asc` and `desc`; the `tag_slug` enum accepts `all`, `politics`, `sports`, `crypto`, `pop-culture`, `middle-east`, `business`, and `science`.
- **Params:** `cursor` (string, optional) — Optional rewards cursor from a prior response; defaults to MA==; `date` (string, optional) — Reward program date in YYYY-MM-DD format; defaults to today in UTC; `limit` (integer, optional) — Maximum rows, defaults to 100 and supports up to 100; `order_by` (string, optional) — Rewards market sort; `position` (string, optional) — Sort direction; `q` (string, optional) — Optional market question search text; `tag_slug` (string, optional) — Rewards category

### `polymarket_search`

- **HTTP:** `GET /polymarket/search`
- **What:** Search Polymarket events. Searches Polymarket's credential-free public search JSON and returns normalized event results. The `status` enum accepts `open`, `closed`, and `all`; the `sort` enum accepts `relevance`, `volume24hr`, `volume`, `liquidity`, and `endDate`.
- **Params:** `ascending` (boolean, optional) — Sort ascending when true; `include_profiles` (boolean, optional) — Include matching profiles; `include_tags` (boolean, optional) — Include matching tags; `limit` (integer, optional) — Maximum events, defaults to 10 and supports up to 50; `q` (string, **required**) — Search query; `sort` (string, optional) — Search sort; `status` (string, optional) — Event status filter

### `polymarket_tag`

- **HTTP:** `GET /polymarket/tag/{id}`
- **What:** Get a Polymarket tag by id. Returns one normalized Polymarket tag from credential-free public Gamma tag JSON.
- **Params:** `id` (string, **required**) — Polymarket tag id; `include_template` (boolean, optional) — Include upstream template data when supported; `locale` (string, optional) — Optional upstream locale

### `polymarket_tags`

- **HTTP:** `GET /polymarket/tags`
- **What:** List Polymarket tags. Returns normalized tag rows from Polymarket's credential-free public Gamma tags JSON.
- **Params:** `ascending` (string, optional) — Sort ascending flag; `limit` (integer, optional) — Maximum tags, defaults to 25 and supports up to 100; `locale` (string, optional) — Optional upstream locale; `offset` (integer, optional) — Result offset, defaults to 0 and supports up to 10000; `order` (string, optional) — Sort field

### `polymarket_token_midpoint`

- **HTTP:** `GET /polymarket/token/{token_id}/midpoint`
- **What:** Get Polymarket token midpoint. Returns the public CLOB midpoint for one Polymarket token id.
- **Params:** `token_id` (string, **required**) — Polymarket CLOB token id

### `polymarket_token_orderbook`

- **HTTP:** `GET /polymarket/token/{token_id}/orderbook`
- **What:** Get Polymarket token order book. Returns public CLOB order-book depth for one Polymarket token id.
- **Params:** `token_id` (string, **required**) — Polymarket CLOB token id

### `polymarket_token_price`

- **HTTP:** `GET /polymarket/token/{token_id}/price`
- **What:** Get Polymarket token price. Returns the public CLOB buy or sell price for one Polymarket token id.
- **Params:** `side` (string, optional) — Order side used for the CLOB price; `token_id` (string, **required**) — Polymarket CLOB token id

### `polymarket_token_price_history`

- **HTTP:** `GET /polymarket/token/{token_id}/price-history`
- **What:** Get Polymarket token price history. Returns public CLOB price-history points for one Polymarket token id.
- **Params:** `end_ts` (integer, optional) — Optional Unix timestamp upper bound; `fidelity` (integer, optional) — Data point resolution in minutes; 0 uses the default 60; maximum 1440; `interval` (string, optional) — History interval; `start_ts` (integer, optional) — Optional Unix timestamp lower bound; `token_id` (string, **required**) — Polymarket CLOB token id

### `polymarket_token_spread`

- **HTTP:** `GET /polymarket/token/{token_id}/spread`
- **What:** Get Polymarket token spread. Returns the public CLOB spread for one Polymarket token id.
- **Params:** `token_id` (string, **required**) — Polymarket CLOB token id

### `polymarket_tokens_midpoints`

- **HTTP:** `POST /polymarket/tokens/midpoints`
- **What:** Get Polymarket token midpoints. Returns public CLOB midpoints for up to 25 Polymarket token ids. This uses credential-free public CLOB market-data JSON and does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `body` (object, **required**) — Token ids request body

### `polymarket_tokens_orderbooks`

- **HTTP:** `POST /polymarket/tokens/orderbooks`
- **What:** Get Polymarket token order books. Returns public CLOB order-book depth for up to 25 Polymarket token ids. This uses credential-free public CLOB market-data JSON and does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `body` (object, **required**) — Token ids request body

### `polymarket_tokens_prices`

- **HTTP:** `POST /polymarket/tokens/prices`
- **What:** Get Polymarket token prices. Returns public CLOB buy and sell prices for up to 25 Polymarket token ids. The `side` enum accepts `buy` and `sell`; when omitted, both sides are returned. This uses credential-free public CLOB market-data JSON and does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `body` (object, **required**) — Token ids request body

### `polymarket_tokens_spreads`

- **HTTP:** `POST /polymarket/tokens/spreads`
- **What:** Get Polymarket token spreads. Returns public CLOB spreads for up to 25 Polymarket token ids. This uses credential-free public CLOB market-data JSON and does not require a Polymarket user token, wallet signature, cookies, or personal account authentication.
- **Params:** `body` (object, **required**) — Token ids request body

## Poshmark (8)

### `poshmark_brand`

- **HTTP:** `GET /poshmark/brand/{name}`
- **What:** Browse Poshmark listings by brand. Returns a page of normalized Poshmark listings for a given brand name (e.g. Nike), the same browsing view as Poshmark's own brand pages. Pass a previous response's next_max_id back as max_id to fetch the next page. Credential-free public data sourced from Poshmark's own server-rendered brand page and, for pages past the first, Poshmark's own JSON pagination API.
- **Params:** `max_id` (string, optional) — Opaque pagination cursor from a previous response's next_max_id. Omit for the first page; `name` (string, **required**) — Poshmark brand name, matching the path segment of a /brand/{name} URL

### `poshmark_brands`

- **HTTP:** `GET /poshmark/brands`
- **What:** Get the full Poshmark brand directory. Returns Poshmark's full brand directory: every brand Poshmark recognizes (name, slug, logo, known aliases), not just brands with active listings for a given search or category filter. Useful for resolving a brand name to the exact value the brand/search filters expect. Credential-free public data sourced from Poshmark's own server-rendered brand directory page.
- **Params:** _none_

### `poshmark_categories`

- **HTTP:** `GET /poshmark/categories`
- **What:** Get the Poshmark department/category browse taxonomy. Returns Poshmark's full department/category browse taxonomy (e.g. Women > Shoes, Men > Jackets & Coats). Each entry's path resolves directly against the category endpoint. This is reference data that changes rarely, so responses are cached. Credential-free public data sourced from Poshmark's own server-rendered category pages.
- **Params:** _none_

### `poshmark_category`

- **HTTP:** `GET /poshmark/category/{path}`
- **What:** Browse Poshmark listings by category. Returns a page of normalized Poshmark listings for a given category path (e.g. Women-Shoes, Men-Shirts), the same browsing view as Poshmark's own category pages. Pass a previous response's next_max_id back as max_id to fetch the next page. Credential-free public data sourced from Poshmark's own server-rendered category page and, for pages past the first, Poshmark's own JSON pagination API.
- **Params:** `max_id` (string, optional) — Opaque pagination cursor from a previous response's next_max_id. Omit for the first page; `path` (string, **required**) — Poshmark category path segment, e.g. Women-Shoes, Men-Shirts

### `poshmark_closet`

- **HTTP:** `GET /poshmark/closet/{username}`
- **What:** Get Poshmark seller closet (storefront). Returns a normalized Poshmark closet (seller storefront) page: the seller's public profile and reputation stats (followers, ratings, items sold) plus a first page of their currently available listings and total listing count. Pass a previous response's next_max_id back as max_id to fetch the next page of listings; paginated responses omit the seller profile to avoid a second upstream fetch, so fetch without max_id first to get seller fields. Credential-free public data sourced from Poshmark's own server-rendered closet page and, for pages past the first, Poshmark's own JSON pagination API.
- **Params:** `max_id` (string, optional) — Opaque pagination cursor from a previous response's next_max_id. Omit for the first page; `username` (string, **required**) — Poshmark seller username, the path segment of a /closet/{username} URL

### `poshmark_listing`

- **HTTP:** `GET /poshmark/listing/{id}`
- **What:** Get Poshmark listing detail. Returns a normalized Poshmark item-detail page: the full listing (description, all photos, size/brand/condition, inventory), its seller's profile, public comments, and similar listings Poshmark itself surfaces on the same page. Credential-free public data sourced from Poshmark's own server-rendered listing page.
- **Params:** `id` (string, **required**) — Poshmark listing id, the trailing id segment of a /listing/{slug}-{id} URL

### `poshmark_search`

- **HTTP:** `GET /poshmark/search`
- **What:** Search Poshmark listings. Searches Poshmark for clothing, shoes, and accessory listings, returning normalized listing summaries (title, price, brand, size, condition, seller, images) plus the total matching count and an opaque pagination cursor. Pass a previous response's next_max_id back as max_id to fetch the next page. Credential-free public data sourced from Poshmark's own server-rendered search page and, for pages past the first, Poshmark's own JSON pagination API.
- **Params:** `department` (string, optional) — Department filter, e.g. Women, Men, Kids; `max_id` (string, optional) — Opaque pagination cursor from a previous response's next_max_id. Omit for the first page; `query` (string, **required**) — Free-text keyword search

### `poshmark_trend`

- **HTTP:** `GET /poshmark/trend/{id}`
- **What:** Browse a Poshmark trend/showroom collection. Returns a page of normalized Poshmark listings for a curated trend/showroom collection (e.g. "Vintage Celine Handbags"), the same browsing view as Poshmark's own trend pages. Pass a previous response's next_max_id back as max_id to fetch the next page. Credential-free public data sourced from Poshmark's own server-rendered trend page and, for pages past the first, Poshmark's own JSON pagination API.
- **Params:** `id` (string, **required**) — Poshmark trend/showroom id, the trailing id segment of a /trend/{slug}-{id} URL; `max_id` (string, optional) — Opaque pagination cursor from a previous response's next_max_id. Omit for the first page

## ProductHunt (11)

### `producthunt_about`

- **HTTP:** `GET /producthunt/product/{id}/about`
- **What:** Retrieve Product Hunt product about page. Returns the richer Product Hunt about-page payload, including launch, forum, review tags, and media data.
- **Params:** `id` (string, **required**) — Product Hunt slug

### `producthunt_alternatives`

- **HTTP:** `GET /producthunt/product/{id}/alternatives`
- **What:** Retrieve Product Hunt product alternatives. Returns paginated alternatives, tags, and related discussions for a Product Hunt product.
- **Params:** `cursor` (string, optional) — Pagination cursor; `first` (integer, optional) — Page size; `id` (string, **required**) — Product Hunt slug; `order` (string, optional) — Sort order; `tags` (string, optional) — Comma-separated tag slugs

### `producthunt_category`

- **HTTP:** `GET /producthunt/category/{slug}`
- **What:** Retrieve Product Hunt category details. Returns the category page payload for a Product Hunt category slug.
- **Params:** `slug` (string, **required**) — Product Hunt category slug

### `producthunt_category_products`

- **HTTP:** `GET /producthunt/category/{slug}/products`
- **What:** Retrieve Product Hunt category products. Returns the products in a Product Hunt category (now backed by Product Hunt topics), cursor-paginated. Pass the `cursor` from a previous response's `end_cursor` to page; `page_size` controls the batch size. `page`, `featured_only`, `order` and `tags` are accepted for compatibility but no longer affect the result.
- **Params:** `cursor` (string, optional) — Pagination cursor from a previous response's end_cursor; `featured_only` (boolean, optional) — Accepted for compatibility; no longer affects results; `order` (string, optional) — Accepted for compatibility; no longer affects results; `page` (integer, optional) — Accepted for compatibility; use cursor to paginate; `page_size` (integer, optional) — Page size (number of products); `slug` (string, **required**) — Product Hunt category slug; `tags` (string, optional) — Accepted for compatibility; no longer affects results

### `producthunt_customers`

- **HTTP:** `GET /producthunt/product/{id}/customers`
- **What:** Retrieve Product Hunt product customers. Returns paginated customer products for a Product Hunt product using Product Hunt's ProductCustomersPage GraphQL operation.
- **Params:** `id` (string, **required**) — Product Hunt slug; `order` (string, optional) — Product Hunt customers order; `page` (integer, optional) — Page number; `page_size` (integer, optional) — Results per page

### `producthunt_launches`

- **HTTP:** `GET /producthunt/product/{id}/launches`
- **What:** Retrieve Product Hunt product launches. Returns paginated launch posts for a Product Hunt product using Product Hunt's ProductPageLaunches GraphQL operation.
- **Params:** `cursor` (string, optional) — Pagination cursor; `id` (string, **required**) — Product Hunt slug; `order` (string, optional) — Product Hunt launch order

### `producthunt_leaderboard`

- **HTTP:** `GET /producthunt/leaderboard`
- **What:** Retrieve Product Hunt leaderboard. Fetches Product Hunt leaderboard data for daily, weekly, monthly, or yearly scopes via Product Hunt GraphQL.
- **Params:** `cursor` (string, optional) — Pagination cursor; `date` (string, optional) — Anchor date in YYYY-MM-DD format. Used to derive missing year/month/day/week values.; `day` (integer, optional) — Daily day override; `featured` (boolean, optional) — Featured products only; `month` (integer, optional) — Daily/monthly month override; `order` (string, optional) — Ranking order override. Defaults to scope rank enum.; `scope` (string, optional) — Leaderboard scope: daily, weekly, monthly, yearly; `week` (integer, optional) — Weekly ISO week override; `year` (integer, optional) — Leaderboard year override

### `producthunt_makers`

- **HTTP:** `GET /producthunt/product/{id}/makers`
- **What:** Retrieve Product Hunt product makers. Returns maker items for a Product Hunt product.
- **Params:** `cursor` (string, optional) — Pagination cursor; `id` (string, **required**) — Product Hunt slug

### `producthunt_product`

- **HTTP:** `GET /producthunt/product/{id}`
- **What:** Retrieve Product Hunt product details. Returns the core Product Hunt product details.
- **Params:** `id` (string, **required**) — Product Hunt slug or numeric ID

### `producthunt_reviews`

- **HTTP:** `GET /producthunt/product/{id}/reviews`
- **What:** Retrieve Product Hunt product detailed reviews. Returns detailed review items for a Product Hunt product.
- **Params:** `id` (string, **required**) — Product Hunt slug

### `producthunt_search`

- **HTTP:** `GET /producthunt/search`
- **What:** Search for products, users, or launches on Product Hunt. Performs a full-text Product Hunt search and returns matching products, users, or launches.
- **Params:** `featured` (boolean, optional) — Launch search only: featured launches only; `page` (integer, optional) — Page number (1-based); `query` (string, **required**) — Search keywords; `topics` (string, optional) — Launch search only: comma-separated topic slugs; `type` (string, optional) — Result type: **product** (default), **user**, or **launch**

## Reddit (11)

### `reddit_comments`

- **HTTP:** `GET /reddit/comments/{id}`
- **What:** Get Reddit post comments. Returns a Reddit post with its public comments. The default 1-credit mode uses RSS. Set `include_metrics=true` to use the anonymous HTML post page as the sole content request and return the server-rendered comments with public net score and award count plus post engagement metrics for 3 credits. Large threads may expose only an initial comment subset in anonymous HTML. Reddit does not expose per-comment upvote ratios or exact upvote/downvote totals anonymously. A post that exists but has no comments yet returns a 200 response with an empty comments list; a post that does not exist returns 404, and a temporary block or upstream failure returns 503 (retryable) rather than 404.
- **Params:** `depth` (integer, optional) — Maximum flat comment depth returned in metrics mode.; `id` (string, **required**) — Reddit post id or t3_ id; `include_metrics` (boolean, optional) — Include public post and per-comment engagement metrics; costs 3 credits instead of 1; `limit` (integer, optional) — Maximum comments returned, defaults to 25 and clamps to 100; `sort` (string, optional) — Comment order: confidence, top, new, controversial, old, or qa. Applied to the anonymous HTML request when metrics are enabled.

### `reddit_domain_posts`

- **HTTP:** `GET /reddit/domain/{domain}/posts`
- **What:** List Reddit domain posts. Returns normalized public posts submitted from a linked domain. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `domain` (string, **required**) — Domain hostname, without scheme or path; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `sort` (string, optional) — Sort: hot, new, top, or rising; `time` (string, optional) — Time window for top sort: hour, day, week, month, year, or all

### `reddit_post`

- **HTTP:** `GET /reddit/post/{id}`
- **What:** Get Reddit post. Returns a normalized public Reddit post. The default 1-credit mode uses RSS. Set `include_metrics=true` to use the anonymous HTML post page as the sole content request and return public net score, upvote ratio, comment count, award count, and estimated upvote/downvote totals for 3 credits. Reddit fuzzes voting data, so estimates are approximate; share, repost/crosspost, and view counts are not exposed anonymously.
- **Params:** `id` (string, **required**) — Reddit post id or t3_ id; `include_metrics` (boolean, optional) — Include public engagement metrics; costs 3 credits instead of 1

### `reddit_search`

- **HTTP:** `GET /reddit/search`
- **What:** Search Reddit posts. Searches public Reddit content and returns normalized public post entries. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `q` (string, **required**) — Search keywords; `sort` (string, optional) — Sort: relevance, hot, new, top, or comments; `subreddit` (string, optional) — Restrict search to a subreddit name, without r/; `time` (string, optional) — Time window for top/comments sorts: hour, day, week, month, year, or all

### `reddit_subreddit_about`

- **HTTP:** `GET /reddit/subreddit/{subreddit}/about`
- **What:** Get Reddit subreddit metadata. Returns public metadata and sample posts for a subreddit. Subscriber counts, icons, and banners are omitted because they are not available on anonymous Reddit pages. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `limit` (integer, optional) — Maximum sample posts inspected, defaults to 25 and clamps to 100; `subreddit` (string, **required**) — Subreddit name, without r/

### `reddit_subreddit_comments`

- **HTTP:** `GET /reddit/subreddit/{subreddit}/comments`
- **What:** List Reddit subreddit comments. Returns flat public comment entries from a subreddit latest-comments feed. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum comments, defaults to 25 and clamps to 100; `subreddit` (string, **required**) — Subreddit name, without r/

### `reddit_subreddit_posts`

- **HTTP:** `GET /reddit/subreddit/{subreddit}/posts`
- **What:** List Reddit subreddit posts. Returns normalized public posts from a subreddit. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `sort` (string, optional) — Sort: hot, new, top, or rising; `subreddit` (string, **required**) — Subreddit name, without r/; `time` (string, optional) — Time window for top sort: hour, day, week, month, year, or all

### `reddit_subreddits_posts`

- **HTTP:** `GET /reddit/subreddits/posts`
- **What:** List Reddit multi-subreddit posts. Returns normalized public posts from a combined multi-subreddit feed. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `sort` (string, optional) — Sort: hot, new, top, or rising; `subreddits` (string, **required**) — Comma-separated subreddit names, without r/, maximum 10; `time` (string, optional) — Time window for top sort: hour, day, week, month, year, or all

### `reddit_trends`

- **HTTP:** `GET /reddit/trends`
- **What:** List Reddit trends. Returns normalized public posts from broad Reddit hot, new, rising, or top feeds. For subreddit-specific trends, use `/reddit/subreddit/{subreddit}/posts` with `sort=hot`, `sort=new`, `sort=rising`, or `sort=top`. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `sort` (string, optional) — Sort: hot, new, rising, or top; `time` (string, optional) — Time window for top sort: hour, day, week, month, year, or all

### `reddit_user_comments`

- **HTTP:** `GET /reddit/user/{username}/comments`
- **What:** List Reddit user comments. Returns flat public comment entries from a public Reddit user's comments feed. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum comments, defaults to 25 and clamps to 100; `username` (string, **required**) — Public Reddit username, without u/

### `reddit_user_posts`

- **HTTP:** `GET /reddit/user/{username}/posts`
- **What:** List Reddit user posts. Returns normalized public posts from a public Reddit user's submitted feed. A `503` with a `Retry-After` header means Reddit is temporarily throttling the request; wait that many seconds and retry.
- **Params:** `after` (string, optional) — Reddit pagination token; `limit` (integer, optional) — Maximum posts, defaults to 25 and clamps to 100; `username` (string, **required**) — Public Reddit username, without u/

## Redfin (5)

### `redfin_estimate`

- **HTTP:** `GET /redfin/estimate`
- **What:** Get Redfin Estimate. Returns the Redfin Estimate for a property, including the current estimate, property facts, and the monthly estimate history with city/county/postal comparatives. Faithful pass-through of Redfin's public avm + avmHistoricalData resources.
- **Params:** `property_id` (string, **required**) — Redfin property id

### `redfin_property`

- **HTTP:** `GET /redfin/property`
- **What:** Get Redfin property. Returns normalized Redfin public property details. Provide a listing url, or a property_id (optionally with listing_id) to use Redfin's public stingray detail API.
- **Params:** `listing_id` (string, optional) — Redfin listing id, improves completeness with property_id; `property_id` (string, optional) — Redfin property id, used when url is not provided; `url` (string, optional) — Redfin listing URL (primary key)

### `redfin_region_trends`

- **HTTP:** `GET /redfin/region-trends`
- **What:** Get Redfin region market trends. Returns Redfin's aggregate market trends for a region (median list/sale price, sale-to-list, offers, days on market, inventory, year-over-year). Faithful pass-through of Redfin's public aggregate-trends resource.
- **Params:** `region_id` (integer, **required**) — Redfin region id from autocomplete; `region_type` (integer, optional) — Redfin region type from autocomplete (defaults to 6, city)

### `redfin_search`

- **HTTP:** `GET /redfin/search`
- **What:** Search Redfin listings. Returns normalized Redfin public listing search results from Redfin's credential-free region CSV endpoint. Pass region_id/region_type from autocomplete to skip location resolution.
- **Params:** `location` (string, optional) — Display location; resolved via autocomplete when region_id is omitted; `max_price` (integer, optional) — Maximum price filter; `min_baths` (number, optional) — Minimum bathrooms filter; `min_beds` (integer, optional) — Minimum bedrooms filter; `min_price` (integer, optional) — Minimum price filter; `page` (integer, optional) — 1-based page; `region_id` (integer, optional) — Redfin region id from autocomplete; `region_type` (integer, optional) — Redfin region type from autocomplete (defaults to 6, city); `status` (string, optional) — Listing status: for_sale or sold

### `redfin_similar`

- **HTTP:** `GET /redfin/similar`
- **What:** Get Redfin comparable listings. Returns Redfin's comparable ("similar") listings for a property as normalized listing rows. Faithful pass-through of Redfin's public similars resource.
- **Params:** `property_id` (string, **required**) — Redfin property id

## Rotten Tomatoes (9)

### `rottentomatoes_browse_movies`

- **HTTP:** `GET /rottentomatoes/browse/movies`
- **What:** Rotten Tomatoes movie discovery rows. Returns normalized movie rows from Rotten Tomatoes public browse pages using credential-free JSON-LD ItemList data. Supported `list` values are `movies_in_theaters`, `movies_at_home`, and `movies_coming_soon`. Supported `sort` values are `popular`, `newest`, and `top_box_office`; `top_box_office` is only valid with `movies_in_theaters`.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 20; `list` (string, optional) — Movie browse list: movies_in_theaters, movies_at_home, movies_coming_soon; `sort` (string, optional) — Sort: popular, newest, top_box_office

### `rottentomatoes_browse_tv`

- **HTTP:** `GET /rottentomatoes/browse/tv`
- **What:** Rotten Tomatoes TV discovery rows. Returns normalized TV series rows from Rotten Tomatoes public browse pages using credential-free JSON-LD ItemList data. Supported `list` value is `tv_series_browse`. Supported `sort` values are `popular` and `newest`.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 20; `list` (string, optional) — TV browse list: tv_series_browse; `sort` (string, optional) — Sort: popular, newest

### `rottentomatoes_episode`

- **HTTP:** `GET /rottentomatoes/episode`
- **What:** Rotten Tomatoes episode detail. Returns normalized Rotten Tomatoes TV episode metadata, scorecard data, parent series/season metadata, and public video metadata from a credential-free public episode page. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — Rotten Tomatoes episode path; `url` (string, optional) — Absolute https://www.rottentomatoes.com episode URL

### `rottentomatoes_movie`

- **HTTP:** `GET /rottentomatoes/movie`
- **What:** Rotten Tomatoes movie detail. Returns normalized Rotten Tomatoes movie metadata, scorecard data, and representative embedded audience reviews. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — Rotten Tomatoes movie path; `url` (string, optional) — Absolute https://www.rottentomatoes.com movie URL

### `rottentomatoes_movie_reviews`

- **HTTP:** `GET /rottentomatoes/movie/reviews`
- **What:** Rotten Tomatoes movie reviews. Returns normalized critic or audience reviews from Rotten Tomatoes public review JSON hydrated by the movie review page, including pagination metadata. Pass exactly one of `path` or `url`. Supported `type` values are `critics`, `top-critics`, `audience`, and `verified-audience`.
- **Params:** `after` (string, optional) — Pagination cursor from data.page_info.end_cursor; `limit` (integer, optional) — Reviews to return, default 10, max 20; `path` (string, optional) — Rotten Tomatoes movie path; `type` (string, optional) — Review type: critics, top-critics, audience, verified-audience; `url` (string, optional) — Absolute https://www.rottentomatoes.com movie URL

### `rottentomatoes_person`

- **HTTP:** `GET /rottentomatoes/person`
- **What:** Rotten Tomatoes person detail and filmography. Returns normalized Rotten Tomatoes celebrity/person metadata and filmography rows from public Person JSON-LD and the credential-free filmography module. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — Rotten Tomatoes person path; `url` (string, optional) — Absolute https://www.rottentomatoes.com person URL

### `rottentomatoes_search`

- **HTTP:** `GET /rottentomatoes/search`
- **What:** Rotten Tomatoes movie search. Returns normalized Rotten Tomatoes movie search rows from credential-free server-rendered search HTML.
- **Params:** `limit` (integer, optional) — Rows to return, default 10, max 20; `query` (string, **required**) — Search query

### `rottentomatoes_season`

- **HTTP:** `GET /rottentomatoes/season`
- **What:** Rotten Tomatoes season detail. Returns normalized Rotten Tomatoes TV season metadata, scorecard data, parent series metadata, and episode rows from a credential-free public season page. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — Rotten Tomatoes season path; `url` (string, optional) — Absolute https://www.rottentomatoes.com season URL

### `rottentomatoes_series`

- **HTTP:** `GET /rottentomatoes/series`
- **What:** Rotten Tomatoes series detail. Returns normalized Rotten Tomatoes TV series metadata and scorecard data from a credential-free public series page. Pass exactly one of `path` or `url`.
- **Params:** `path` (string, optional) — Rotten Tomatoes series path; `url` (string, optional) — Absolute https://www.rottentomatoes.com series URL

## SEC EDGAR (10)

### `sec_company_intelligence`

- **HTTP:** `GET /sec/company/intelligence`
- **What:** Company 360 overview from SEC data. Aggregates a company's profile, a latest-annual financial snapshot, the latest 10-K/10-Q/8-K, and recent material events into one call. Provide cik or ticker. Optionally fuse live cross-source data with enrich (a comma list of market, news, hiring): market and news are keyed on the ticker; hiring needs ats plus that ATS's careers slug (or tenant/datacenter/site for Workday). Enrichment is best-effort — requested-but-unavailable sources are listed under degraded and never fail the SEC-native response. Credential-free public data.
- **Params:** `ats` (string, optional) — ATS provider for hiring enrichment; `careers_slug` (string, optional) — Careers board slug for hiring (greenhouse/lever/ashby/smartrecruiters); `cik` (string, optional) — SEC CIK (numeric or zero-padded); `datacenter` (string, optional) — Workday datacenter shard (hiring, when ats=workday); `enrich` (string, optional) — Comma list of cross-source enrichments; `site` (string, optional) — Workday career site (hiring, when ats=workday); `tenant` (string, optional) — Workday tenant (hiring, when ats=workday); `ticker` (string, optional) — Ticker symbol (alternative to cik)

### `sec_company_search`

- **HTTP:** `GET /sec/company/search`
- **What:** Resolve a ticker or company name to EDGAR companies. Resolves a ticker symbol or company-name query to SEC EDGAR companies (CIK, ticker, name) using the official company_tickers map. Credential-free public SEC data.
- **Params:** `limit` (integer, optional) — Max matches, default 10, max 100; `q` (string, **required**) — Ticker symbol or company name

### `sec_company_submissions`

- **HTTP:** `GET /sec/company/submissions`
- **What:** List a company's EDGAR filings. Returns a company's recent SEC filings (form, dates, primary document URL) filtered by form type and date range, plus company profile fields as reported by EDGAR: entity_type, former_names, exchanges, category, fiscal_year_end, state_of_incorporation. Provide cik or ticker. Credential-free public SEC data.
- **Params:** `cik` (string, optional) — SEC CIK (numeric or zero-padded); `form` (string, optional) — Filter by form type, e.g. 10-K, 10-Q, 8-K; `from` (string, optional) — Earliest filing date (YYYY-MM-DD); `limit` (integer, optional) — Max filings, default 50, max 500; `ticker` (string, optional) — Ticker symbol (alternative to cik); `to` (string, optional) — Latest filing date (YYYY-MM-DD)

### `sec_filing`

- **HTTP:** `GET /sec/filing`
- **What:** Get a single filing by accession number. Returns a single SEC filing's metadata and primary document URL. Provide accession plus cik or ticker. Credential-free public SEC data.
- **Params:** `accession` (string, **required**) — Accession number; `cik` (string, optional) — SEC CIK (numeric or zero-padded); `ticker` (string, optional) — Ticker symbol (alternative to cik)

### `sec_filing_sections`

- **HTTP:** `GET /sec/filing/sections`
- **What:** Extract 10-K/10-Q/8-K item sections. Extracts item sections (e.g. 1A Risk Factors, 7 MD&A) from a 10-K/10-Q/8-K primary document as clean text. Provide accession plus cik or ticker. Credential-free public SEC data.
- **Params:** `accession` (string, **required**) — Accession number; `cik` (string, optional) — SEC CIK (numeric or zero-padded); `items` (string, optional) — Comma-separated item numbers to return, e.g. 1A,7; `max_chars` (integer, optional) — Max characters per section, default 20000, max 200000; `ticker` (string, optional) — Ticker symbol (alternative to cik)

### `sec_financials`

- **HTTP:** `GET /sec/financials`
- **What:** Normalized income statement, balance sheet, or cash flow. Returns a company's normalized financial statements across recent periods, resolving EDGAR's inconsistent XBRL tags to a stable schema. Provide cik or ticker. Credential-free public SEC data.
- **Params:** `cik` (string, optional) — SEC CIK (numeric or zero-padded); `limit` (integer, optional) — Number of periods, default 5, max 20; `period` (string, optional) — Period basis, default annual; `statement` (string, optional) — Statement, default income; `ticker` (string, optional) — Ticker symbol (alternative to cik)

### `sec_frames`

- **HTTP:** `GET /sec/frames`
- **What:** Cross-company values for one XBRL concept and period. Returns every filer's reported value for one XBRL concept in one reporting period (an EDGAR "frame"). Credential-free public SEC data.
- **Params:** `concept` (string, **required**) — XBRL concept tag, e.g. Assets, Revenues; `limit` (integer, optional) — Max companies, default 200, max 2000; `period` (string, **required**) — Reporting frame, e.g. CY2024, CY2024Q1, CY2024Q4I; `taxonomy` (string, optional) — XBRL taxonomy, default us-gaap; `unit` (string, optional) — Unit of measure, default USD

### `sec_full_text_search`

- **HTTP:** `GET /sec/full-text-search`
- **What:** Full-text search across EDGAR filings. Searches the full text of SEC EDGAR filings (efts), filtered by form and date, with pagination. Credential-free public SEC data; free where incumbents gate full-text search behind paid tiers.
- **Params:** `forms` (string, optional) — Filter by form types, comma-separated; `from` (string, optional) — Earliest filing date (YYYY-MM-DD); `page` (integer, optional) — 1-based page number, default 1; `q` (string, **required**) — Search query (supports quoted phrases); `to` (string, optional) — Latest filing date (YYYY-MM-DD)

### `sec_insider`

- **HTTP:** `GET /sec/insider`
- **What:** Insider transactions (Forms 3/4/5). Returns a company's recent insider transactions parsed from Form 3/4/5 ownership filings (owner, role, security, shares, price). Provide cik or ticker. Credential-free public SEC data.
- **Params:** `cik` (string, optional) — SEC CIK (numeric or zero-padded); `limit` (integer, optional) — Max transactions, default 10, max 30; `ticker` (string, optional) — Ticker symbol (alternative to cik)

### `sec_institutional_holdings`

- **HTTP:** `GET /sec/institutional-holdings`
- **What:** Institutional holdings (13F-HR). Returns the latest 13F-HR holdings for an institutional manager (by CIK): issuer, value, shares, sorted by value. Credential-free public SEC data.
- **Params:** `cik` (string, **required**) — Institutional manager CIK; `limit` (integer, optional) — Max holdings, default 50, max 1000

## Shop.app (16)

### `shop_app_analysis`

- **HTTP:** `GET /shop-app/analysis`
- **What:** Analyze Shop.app query results. Returns a market snapshot derived from Shop.app search results, including price ranges, currencies, sale counts, discounts, and top shops. Limit defaults to 20 and accepts values up to 50.
- **Params:** `deep_search` (boolean, optional) — Enable Shop.app deep search mode; `in_stock` (boolean, optional) — Request in-stock products; `limit` (integer, optional) — Maximum products to analyze, defaults to 20 and supports up to 50; `on_sale` (boolean, optional) — Request sale products; `query` (string, **required**) — Search query

### `shop_app_categories`

- **HTTP:** `GET /shop-app/categories`
- **What:** List Shop.app categories. Returns public Shop.app product categories.
- **Params:** _none_

### `shop_app_collection_products`

- **HTTP:** `GET /shop-app/shops/{handle}/collections/{collection_id}/products`
- **What:** List Shop.app collection products. Returns public product cards from a Shop.app merchant collection. sort_by allowed values: MOST_SALES, PRICE_LOW_TO_HIGH, PRICE_HIGH_TO_LOW, RELEVANCE.
- **Params:** `collection_id` (string, **required**) — Collection id; `handle` (string, **required**) — Shop handle; `in_stock` (boolean, optional) — Request in-stock products; `limit` (integer, optional) — Maximum products, defaults to 30 and supports up to 60; `sort_by` (string, optional) — Sort mode

### `shop_app_product`

- **HTTP:** `GET /shop-app/products/{id}`
- **What:** Get Shop.app product. Returns normalized public product details from Shop.app.
- **Params:** `id` (string, **required**) — Product id; `variant_id` (string, optional) — Variant id

### `shop_app_product_related`

- **HTTP:** `GET /shop-app/products/{id}/related`
- **What:** List Shop.app related products. Returns related product cards from a public Shop.app product page.
- **Params:** `id` (string, **required**) — Product id; `limit` (integer, optional) — Maximum products, defaults to 20 and supports up to 50

### `shop_app_product_reviews`

- **HTTP:** `GET /shop-app/products/{id}/reviews`
- **What:** List Shop.app product reviews. Returns public product reviews from a Shop.app product page.
- **Params:** `id` (string, **required**) — Product id; `limit` (integer, optional) — Maximum reviews, defaults to 20 and supports up to 50

### `shop_app_product_shop`

- **HTTP:** `GET /shop-app/products/{id}/shop`
- **What:** Get the Shop.app shop for a product. Resolves the public Shop.app merchant profile for a product id.
- **Params:** `id` (string, **required**) — Product id

### `shop_app_product_variant`

- **HTTP:** `GET /shop-app/products/{id}/variant`
- **What:** Get a Shop.app product variant by selected options. Returns the exact public product variant matching selected options. selected_options must be a JSON object when provided. Repeated option filters may also be sent as option.Name=value or option[Name]=value.
- **Params:** `id` (string, **required**) — Product id; `selected_options` (string, optional) — Selected options JSON object

### `shop_app_product_variants`

- **HTTP:** `GET /shop-app/products/{id}/variants`
- **What:** List Shop.app product variants. Returns adjacent variants for a Shop.app product. selected_options must be a JSON object when provided. Repeated option filters may also be sent as option.Name=value or option[Name]=value.
- **Params:** `id` (string, **required**) — Product id; `limit` (integer, optional) — Maximum variants, defaults to 50 and supports up to 100; `selected_options` (string, optional) — Selected options JSON object

### `shop_app_search`

- **HTTP:** `GET /shop-app/search`
- **What:** Search Shop.app products. Searches Shop.app product results using the credential-free public web search flow. Limit defaults to 20 and accepts values up to 50.
- **Params:** `deep_search` (boolean, optional) — Enable Shop.app deep search mode; `in_stock` (boolean, optional) — Request in-stock products; `limit` (integer, optional) — Maximum products, defaults to 20 and supports up to 50; `on_sale` (boolean, optional) — Request sale products; `query` (string, **required**) — Search query

### `shop_app_shop`

- **HTTP:** `GET /shop-app/shops/{handle}`
- **What:** Get Shop.app shop. Returns public Shop.app merchant profile details.
- **Params:** `handle` (string, **required**) — Shop handle

### `shop_app_shop_locations`

- **HTTP:** `GET /shop-app/shops/{handle}/locations`
- **What:** List Shop.app shop locations. Returns public retail locations for a Shop.app merchant profile.
- **Params:** `handle` (string, **required**) — Shop handle; `limit` (integer, optional) — Maximum locations, defaults to 10 and supports up to 50

### `shop_app_shop_products`

- **HTTP:** `GET /shop-app/shops/{handle}/products`
- **What:** List Shop.app shop products. Returns public product cards from a Shop.app merchant profile. sort_by allowed values: MOST_SALES, PRICE_LOW_TO_HIGH, PRICE_HIGH_TO_LOW, RELEVANCE.
- **Params:** `handle` (string, **required**) — Shop handle; `in_stock` (boolean, optional) — Request in-stock products; `limit` (integer, optional) — Maximum products, defaults to 30 and supports up to 60; `sort_by` (string, optional) — Sort mode

### `shop_app_shop_reviews`

- **HTTP:** `GET /shop-app/shops/{handle}/reviews`
- **What:** List Shop.app shop reviews. Returns public reviews for a Shop.app merchant profile.
- **Params:** `handle` (string, **required**) — Shop handle; `limit` (integer, optional) — Maximum reviews, defaults to 20 and supports up to 50

### `shop_app_shop_typeahead`

- **HTTP:** `GET /shop-app/shops/{handle}/typeahead`
- **What:** Suggest products and collections inside a Shop.app shop. Returns public store typeahead suggestions for a Shop.app merchant profile.
- **Params:** `handle` (string, **required**) — Shop handle; `limit` (integer, optional) — Maximum suggestions, defaults to 20 and supports up to 20; `query` (string, **required**) — Typeahead query

### `shop_app_suggestions`

- **HTTP:** `GET /shop-app/suggestions`
- **What:** Suggest Shop.app searches. Returns Shop.app autocomplete suggestions. Limit defaults to 10 and supports up to 20.
- **Params:** `limit` (integer, optional) — Maximum suggestions, defaults to 10 and supports up to 20; `query` (string, **required**) — Search query

## Shopify (11)

### `shopify_collection_products`

- **HTTP:** `GET /shopify/collections/{handle}/products`
- **What:** List Shopify collection products. Returns normalized products from a public Shopify collection `/products.json` endpoint.
- **Params:** `handle` (string, **required**) — Collection handle; `limit` (integer, optional) — Maximum products, defaults to 50 and supports up to 250; `page` (integer, optional) — 1-based page, defaults to 1; `url` (string, **required**) — Shopify storefront URL

### `shopify_collections`

- **HTTP:** `GET /shopify/collections`
- **What:** List Shopify collections. Returns normalized collections from a public Shopify `/collections.json` endpoint. Valid empty result pages return `200` with an empty collections array.
- **Params:** `limit` (integer, optional) — Maximum collections, defaults to 50 and supports up to 250; `page` (integer, optional) — 1-based page, defaults to 1; `url` (string, **required**) — Shopify storefront URL

### `shopify_page`

- **HTTP:** `GET /shopify/pages/{handle}`
- **What:** Get Shopify page. Returns normalized page detail from Shopify's credential-free `/pages/{handle}.json` endpoint. Page body HTML is returned as cleaned text only.
- **Params:** `handle` (string, **required**) — Page handle; `url` (string, **required**) — Shopify storefront URL

### `shopify_pages`

- **HTTP:** `GET /shopify/pages`
- **What:** List Shopify pages. Returns normalized static pages from a public Shopify `/pages.json` endpoint. Page body HTML is returned as cleaned text only.
- **Params:** `limit` (integer, optional) — Maximum pages, defaults to 50 and supports up to 250; `page` (integer, optional) — 1-based page, defaults to 1; `url` (string, **required**) — Shopify storefront URL

### `shopify_product`

- **HTTP:** `GET /shopify/products/{handle}`
- **What:** Get Shopify product. Returns normalized product detail from Shopify's credential-free product handle `.js` endpoint.
- **Params:** `handle` (string, **required**) — Product handle; `url` (string, **required**) — Shopify storefront URL

### `shopify_product_recommendations`

- **HTTP:** `GET /shopify/products/{handle}/recommendations`
- **What:** List Shopify product recommendations. Returns normalized recommended products from Shopify's credential-free recommendations Ajax endpoint. The route handle is resolved to a Shopify product id before fetching recommendations.
- **Params:** `handle` (string, **required**) — Product handle; `intent` (string, optional) — Recommendation intent. Allowed values: related, complementary; `limit` (integer, optional) — Maximum products, defaults to 10 and supports up to 20; `url` (string, **required**) — Shopify storefront URL

### `shopify_products`

- **HTTP:** `GET /shopify/products`
- **What:** List Shopify products. Returns normalized products from a public Shopify `/products.json` endpoint. Valid empty result pages return `200` with an empty products array.
- **Params:** `limit` (integer, optional) — Maximum products, defaults to 50 and supports up to 250; `page` (integer, optional) — 1-based page, defaults to 1; `url` (string, **required**) — Shopify storefront URL

### `shopify_search_suggest`

- **HTTP:** `GET /shopify/search/suggest`
- **What:** Get Shopify search suggestions. Returns products, collections, and query suggestions from Shopify's credential-free predictive search Ajax endpoint.
- **Params:** `limit` (integer, optional) — Maximum results per type, defaults to 10 and supports up to 20; `q` (string, **required**) — Search query; `types` (string, optional) — Comma-separated suggestion types. Allowed values: product, collection, query; `url` (string, **required**) — Shopify storefront URL

### `shopify_sitemap_urls`

- **HTTP:** `GET /shopify/sitemap/urls`
- **What:** List Shopify sitemap URLs. Fetches capped URL entries from Shopify child sitemaps matching the requested type.
- **Params:** `limit` (integer, optional) — Maximum URL entries, defaults to 50 and supports up to 250; `type` (string, optional) — Sitemap type. Allowed values: all, products, collections, pages, blogs, agentic_discovery, other; `url` (string, **required**) — Shopify storefront URL

### `shopify_sitemaps`

- **HTTP:** `GET /shopify/sitemaps`
- **What:** List Shopify sitemaps. Returns child sitemap URLs from a public Shopify `/sitemap.xml` index with inferred sitemap types.
- **Params:** `url` (string, **required**) — Shopify storefront URL

### `shopify_store`

- **HTTP:** `GET /shopify/store`
- **What:** Get Shopify store metadata. Resolves a public Shopify storefront and returns normalized metadata from credential-free storefront JSON. If the vanity domain blocks `/products.json`, the service may fall back to a public `*.myshopify.com` domain discovered from the storefront page.
- **Params:** `url` (string, **required**) — Shopify storefront URL

## SimilarWeb (2)

### `similarweb_search`

- **HTTP:** `GET /similarweb/search`
- **What:** Search SimilarWeb Info. Returns SimilarWeb data for a given query (typically a domain).
- **Params:** `q` (string, **required**) — Domain or keyword to search

### `similarweb_web`

- **HTTP:** `GET /similarweb/web/{domain}`
- **What:** Get SimilarWeb Web Info. Returns traffic and engagement data from SimilarWeb for a specific domain.
- **Params:** `domain` (string, **required**) — Domain to fetch SimilarWeb data for

## SofaScore (15)

### `sofascore_event`

- **HTTP:** `GET /sofascore/event`
- **What:** SofaScore event detail. Returns one match's detail (teams, score, status, venue, referee) from SofaScore's credential-free public JSON.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_h2h`

- **HTTP:** `GET /sofascore/event-h2h`
- **What:** SofaScore event head-to-head. Returns the historical head-to-head win/draw record between a match's two teams (and managers, when available) from SofaScore's credential-free public JSON.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_incidents`

- **HTTP:** `GET /sofascore/event-incidents`
- **What:** SofaScore event incidents. Returns one match's goal, card, substitution, and period timeline from SofaScore's credential-free public JSON. An empty `incidents` list is a valid response before kickoff.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_lineups`

- **HTTP:** `GET /sofascore/event-lineups`
- **What:** SofaScore event lineups. Returns one match's starting XI and substitutes per side, with formation, from SofaScore's credential-free public JSON. Returns 404 when SofaScore has no lineups for the match.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_odds`

- **HTTP:** `GET /sofascore/event-odds`
- **What:** SofaScore event odds. Returns one match's betting markets and choices from SofaScore's credential-free public JSON. Returns 404 when SofaScore has no odds for the match.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_event_statistics`

- **HTTP:** `GET /sofascore/event-statistics`
- **What:** SofaScore event statistics. Returns one match's statistics (possession, shots, passes, and more, grouped and split by period) from SofaScore's credential-free public JSON. Returns 404 when SofaScore has no tracked statistics for the match.
- **Params:** `id` (string, **required**) — Numeric SofaScore event (match) id

### `sofascore_live_events`

- **HTTP:** `GET /sofascore/live-events`
- **What:** SofaScore live events. Returns currently live events for a sport from SofaScore's credential-free public JSON. The `sport` enum accepts `football`, `basketball`, and `tennis`. An empty `events` list is a valid response when nothing is live right now.
- **Params:** `sport` (string, **required**) — Sport key

### `sofascore_player`

- **HTTP:** `GET /sofascore/player`
- **What:** SofaScore player detail. Returns one player's bio (position, height, market value, current team) from SofaScore's credential-free public JSON.
- **Params:** `id` (string, **required**) — Numeric SofaScore player id

### `sofascore_round_events`

- **HTTP:** `GET /sofascore/round-events`
- **What:** SofaScore round fixtures. Returns fixtures for one round of a competition season from SofaScore's credential-free public JSON. Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `round` (integer, **required**) — Round number; `season` (string, **required**) — Numeric SofaScore season id

### `sofascore_search`

- **HTTP:** `GET /sofascore/search`
- **What:** SofaScore universal search. Searches SofaScore's credential-free public JSON for teams, players, and competitions matching a free-text query. An empty `results` list is a valid response when nothing matches.
- **Params:** `q` (string, **required**) — Free-text search query

### `sofascore_standings`

- **HTTP:** `GET /sofascore/standings`
- **What:** SofaScore standings. Returns a league table for a competition season from SofaScore's credential-free public JSON. The `type` enum accepts `total`, `home`, and `away`. Get `id` from search and `season` from tournament-seasons.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id; `season` (string, **required**) — Numeric SofaScore season id; `type` (string, **required**) — Standings variant

### `sofascore_team`

- **HTTP:** `GET /sofascore/team`
- **What:** SofaScore team detail. Returns one team's detail (identity, manager, venue, primary competition) from SofaScore's credential-free public JSON.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_team_events`

- **HTTP:** `GET /sofascore/team-events`
- **What:** SofaScore team fixtures. Returns a page of a team's upcoming or recent fixtures from SofaScore's credential-free public JSON. The `direction` enum accepts `next` and `last`. An empty `events` list is a valid response when there is no fixture on that page.
- **Params:** `direction` (string, **required**) — Fixture direction; `id` (string, **required**) — Numeric SofaScore team id; `page` (integer, optional) — Zero-based page number

### `sofascore_team_players`

- **HTTP:** `GET /sofascore/team-players`
- **What:** SofaScore team players. Returns a team's full squad from SofaScore's credential-free public JSON.
- **Params:** `id` (string, **required**) — Numeric SofaScore team id

### `sofascore_tournament_seasons`

- **HTTP:** `GET /sofascore/tournament-seasons`
- **What:** SofaScore competition seasons. Returns the season list for a competition from SofaScore's credential-free public JSON. Use a returned season id with the standings and round-events endpoints.
- **Params:** `id` (string, **required**) — Numeric SofaScore unique-tournament (competition) id

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

## Steam (21)

### `steam_achievements`

- **HTTP:** `GET /steam/achievements`
- **What:** Get global achievement completion percentages for a Steam app. Returns the global unlock percentage for each of an app's achievements, sorted most-unlocked first. Apps without global achievement stats return an empty list. Credential-free public Steam WebAPI JSON.
- **Params:** `appid` (string, **required**) — Numeric Steam app id

### `steam_app`

- **HTTP:** `GET /steam/app`
- **What:** Get Steam store details for an app. Returns normalized store metadata for a single Steam app (title, type, price, developers/publishers, platforms, genres, categories, release date, metacritic, recommendation and achievement counts). cc selects the store region (and price currency) and l the text language. filters is a comma-separated subset of allowed fields to shrink the payload. Credential-free public Steam storefront JSON.
- **Params:** `appid` (string, **required**) — Numeric Steam app id; `cc` (string, optional) — Store country code (ISO, selects currency); `filters` (string, optional) — Comma-separated fields: basic, price_overview, developers, publishers, categories, genres, release_date, platforms, metacritic, achievements, screenshots, movies, recommendations, controller_support, dlc, short_description, supported_languages, packages, package_groups, ratings, content_descriptors, background; `l` (string, optional) — Language code

### `steam_category`

- **HTTP:** `GET /steam/category/{slug}`
- **What:** Browse a store category (tag) with weighted community tags. Returns a catalog slice for a community tag / category via Steam's keyless IStoreQueryService, carrying each item's WEIGHTED community tags, review-score breakdown, developer/publisher credits, release date, platforms and price. The slug is a numeric tag id or a tag name (case- and separator-insensitive, e.g. rogue_like); resolve ids via /steam/tags/list. Ordering is Steam's default relevance — for sorted or os/price-faceted browse use /steam/tags. Credential-free public Steam store query API.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `coming_soon_only` (boolean, optional) — Only unreleased / coming-soon titles; `count` (integer, optional) — Results per page (max 100); `free` (boolean, optional) — Only free titles; `l` (string, optional) — Steam store language name; `released_only` (boolean, optional) — Only already-released titles; `slug` (string, **required**) — Community tag id (numeric) or tag name slug; `start` (integer, optional) — Result offset for pagination

### `steam_charts_concurrent`

- **HTTP:** `GET /steam/charts/concurrent`
- **What:** Get Steam's live games-by-concurrent-players leaderboard. Returns the live leaderboard of games ranked by current concurrent players (rank, appid, current concurrent, peak). By default each row is enriched with the game name and review summary; pass enrich=false for raw ranked app ids. Credential-free public Steam WebAPI JSON.
- **Params:** `cc` (string, optional) — Store country code (ISO) for name enrichment; `enrich` (boolean, optional) — Attach game name and review summary to each rank; `l` (string, optional) — Steam store language name for name enrichment

### `steam_charts_most_played`

- **HTTP:** `GET /steam/charts/most-played`
- **What:** Get Steam's weekly most-played games chart. Returns Steam's weekly most-played chart: the top games ranked by peak concurrent players over the last week (rank, appid, previous-week rank, peak players). By default each row is enriched with the game name and review summary via a batch lookup; pass enrich=false for the raw ranked app ids only. Credential-free public Steam WebAPI JSON.
- **Params:** `cc` (string, optional) — Store country code (ISO) for name enrichment; `enrich` (boolean, optional) — Attach game name and review summary to each rank; `l` (string, optional) — Steam store language name for name enrichment

### `steam_charts_top_releases`

- **HTTP:** `GET /steam/charts/top-releases`
- **What:** Get Steam's monthly best-new-releases index. Returns Steam's monthly top-releases index: one page per month, each listing that month's top-released app ids (with the month label and start date). The app-id lists are large and not name-enriched; resolve names via /steam/items. Credential-free public Steam WebAPI JSON.
- **Params:** _none_

### `steam_community_recommendations`

- **HTTP:** `GET /steam/community-recommendations`
- **What:** Get the store's community-recommended reviews feed. Returns a batch of recent, quality user reviews recommended across the whole store (author, playtime, helpful votes, and the recommended app). Filter by review kind/sort, reviewer playtime window, review language, and store region. The upstream serves a fixed batch and, unauthenticated, does not support tag filtering or deep pagination. Credential-free public Steam storefront JSON.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `l` (string, optional) — Language code; `playtime_max` (integer, optional) — Maximum reviewer playtime in hours (0 = no maximum); `playtime_min` (integer, optional) — Minimum reviewer playtime in hours (0 = no minimum); `review_filter` (string, optional) — Review kind / sort; `review_language` (string, optional) — Review language: 'my_languages' or a Steam language name

### `steam_featured`

- **HTTP:** `GET /steam/featured`
- **What:** Get the Steam store featured capsules. Returns the storefront's featured capsules for a region (per-platform featured lists plus large spotlight capsules), including discount and price fields. Credential-free public Steam storefront JSON.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `l` (string, optional) — Language code

### `steam_featured_categories`

- **HTTP:** `GET /steam/featured-categories`
- **What:** Get Steam top sellers, new releases, specials and coming soon. Returns the storefront merchandising buckets for a region: specials, top_sellers, new_releases, and coming_soon, each with its item list. Credential-free public Steam storefront JSON.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `l` (string, optional) — Language code

### `steam_items`

- **HTTP:** `GET /steam/items`
- **What:** Resolve a batch of app ids to store items with weighted tags. Resolves up to 100 Steam app ids in one call to normalized store items via Steam's keyless IStoreBrowseService, each carrying its WEIGHTED community tags, review-score breakdown, developer/publisher credits, release date, platforms and price. The batch enrichment primitive for the community-tag taxonomy. Credential-free public Steam store query API.
- **Params:** `appids` (string, **required**) — Comma-separated numeric app ids (max 100); `cc` (string, optional) — Store country code (ISO, selects currency); `l` (string, optional) — Steam store language name

### `steam_news`

- **HTTP:** `GET /steam/news`
- **What:** Get recent news posts for a Steam app. Returns recent news/announcement posts for an app (title, author, contents, feed, date). Credential-free public Steam WebAPI JSON.
- **Params:** `appid` (string, **required**) — Numeric Steam app id; `count` (integer, optional) — Number of posts (max 50); `maxlength` (integer, optional) — Max characters of each post body; default 300, set -1 for full content

### `steam_package`

- **HTTP:** `GET /steam/package`
- **What:** Get Steam store details for a package. Returns normalized details for a Steam package (a purchasable bundle): name, the apps it contains, price, platforms, and release date. cc selects the store region and price currency. Credential-free public Steam storefront JSON.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `l` (string, optional) — Language code; `packageid` (string, **required**) — Numeric Steam package id

### `steam_players`

- **HTTP:** `GET /steam/players`
- **What:** Get the current concurrent-player count for a Steam app. Returns the official current concurrent-players count for an app. Credential-free public Steam WebAPI JSON.
- **Params:** `appid` (string, **required**) — Numeric Steam app id

### `steam_reviews`

- **HTTP:** `GET /steam/reviews`
- **What:** List reviews for a Steam app. Returns a page of user reviews for an app with cursor pagination and an aggregate query_summary (score, positive/negative totals). Aggregate totals populate only on the first page (cursor=*). Pass the returned cursor back to page. Credential-free public Steam storefront JSON.
- **Params:** `appid` (string, **required**) — Numeric Steam app id; `cursor` (string, optional) — Pagination cursor from the previous page; `day_range` (integer, optional) — Look-back window in days (filter=all only, max 365); `filter` (string, optional) — Sort order; `language` (string, optional) — Steam language name or 'all'; `num_per_page` (integer, optional) — Reviews per page (max 100); `purchase_type` (string, optional) — Purchase source filter; `review_type` (string, optional) — Review sentiment filter

### `steam_reviews_histogram`

- **HTTP:** `GET /steam/reviews/histogram`
- **What:** Get the review up/down histogram for a Steam app. Returns the positive/negative recommendation counts over time (the store review graph): weekly/monthly rollups plus recent daily buckets. Credential-free public Steam storefront JSON.
- **Params:** `appid` (string, **required**) — Numeric Steam app id; `language` (string, optional) — Steam language name or 'all'

### `steam_search`

- **HTTP:** `GET /steam/search`
- **What:** Search the Steam store by title. Resolves a search term to Steam apps via the store typeahead JSON (title, appid, price, platforms, metascore). Best for title -> appid lookup; returns roughly ten results. For faceted, paginated search use /steam/search/results. Credential-free public Steam storefront JSON.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `l` (string, optional) — Language code; `term` (string, **required**) — Search term

### `steam_search_results`

- **HTTP:** `GET /steam/search/results`
- **What:** Faceted, paginated Steam store search. Runs the Steam store search with pagination and sorting and returns the result rows (appid, title, release date, review summary, price, platforms). Supports start/count paging and sort_by. Credential-free public Steam storefront JSON.
- **Params:** `cc` (string, optional) — Store country code (ISO, selects currency); `count` (integer, optional) — Results per page (max 100); `l` (string, optional) — Language code; `sort_by` (string, optional) — Sort order; `start` (integer, optional) — Result offset for pagination; `term` (string, **required**) — Search term

### `steam_steamspy`

- **HTTP:** `GET /steam/steamspy`
- **What:** Get SteamSpy third-party ownership and playtime estimates. Returns third-party ownership, concurrent-user, playtime, and review estimates for an app from SteamSpy. These are SteamSpy estimates, not official Steam figures. Credential-free public third-party JSON.
- **Params:** `appid` (string, **required**) — Numeric Steam app id

### `steam_tags`

- **HTTP:** `GET /steam/tags`
- **What:** Browse the Steam store by community tag and store facets. Browses the store by the community-tag taxonomy (Roguelike, Metroidvania, Cozy...) and the store filter facets, with no free-text term. Filter by one or more tag ids, a store category id, platform (os), a maximum price, specials-only, and hide-free-to-play; sort and page the browse-rank rows. Each row includes its community tag ids (resolve names via /steam/tags/list). Pagination runs the full result set (total is the real, fully-pageable match count); paging past total returns an empty page. Credential-free public Steam storefront JSON.
- **Params:** `category1` (string, optional) — Numeric Steam store category id (e.g. 998 games, 21 dlc); `category2` (string, optional) — Additional numeric store category id (feature); `category3` (string, optional) — Additional numeric store category id (feature); `cc` (string, optional) — Store country code (ISO, selects currency); `count` (integer, optional) — Results per page (max 100); `deck_compatibility` (string, optional) — Steam Deck compatibility filter: 1 unsupported, 2 playable, 3 verified; `filter` (string, optional) — Curated preset applied within the other facets; `hidef2p` (boolean, optional) — Hide free-to-play titles; `l` (string, optional) — Language code; `maxprice` (string, optional) — Maximum price as whole cents in the cc currency, or the literal 'free'; `os` (string, optional) — Comma-separated platform filter subset of: win, mac, linux; `sort_by` (string, optional) — Sort order; `specials` (boolean, optional) — Only discounted titles; `start` (integer, optional) — Result offset for pagination; `supportedlang` (string, optional) — Only titles supporting this Steam language name; `tags` (string, optional) — Comma-separated numeric community tag ids (all must match); resolve ids via /steam/tags/list; `untags` (string, optional) — Comma-separated numeric community tag ids to EXCLUDE; `vrsupport` (string, optional) — Comma-separated VR-support filter ids (e.g. 401 seated, 402 standing, 403 roomscale)

### `steam_tags_list`

- **HTTP:** `GET /steam/tags/list`
- **What:** List Steam community tag ids and names. Returns Steam's popular community tags (numeric id + localized name) so callers can map a tag name to the id that /steam/tags and /steam/category expect. Credential-free public Steam storefront JSON.
- **Params:** `l` (string, optional) — Steam store language name for the tag labels

### `steam_top_sellers`

- **HTTP:** `GET /steam/top-sellers`
- **What:** Get Steam's weekly top-sellers chart for a country. Returns the store's weekly top-sellers chart for a country, each rank carrying the full store item (name, price, weighted community tags, review summary, platforms). cc selects the country whose sales ranking and currency are returned. Credential-free public Steam store top-sellers API.
- **Params:** `cc` (string, optional) — Country code (ISO) whose weekly sales ranking is returned; `l` (string, optional) — Steam store language name

## StockX (5)

### `stockx_brands`

- **HTTP:** `GET /stockx/brands`
- **What:** Get StockX brand catalog. Returns StockX's full brand catalog (name and URL slug for every brand in its own brand directory), suitable for building GET /stockx/search's brand parameter or GET /stockx/search's model parameter's required single-brand context. Credential-free public data from the same navigation API backing StockX's own site menu.
- **Params:** _none_

### `stockx_categories`

- **HTTP:** `GET /stockx/categories`
- **What:** Get StockX category/subcategory taxonomy. Returns StockX's full category/subcategory reference: the 7 top-level categories accepted by GET /stockx/search's category parameter, each with its subcategories (e.g. Shoes -> Boots, Cleats, Clogs). Credential-free public data from the same navigation API backing StockX's own site menu.
- **Params:** _none_

### `stockx_product`

- **HTTP:** `GET /stockx/product/{slug}`
- **What:** Get StockX product detail. Returns a normalized StockX product: identity (title, brand, model, colorway, style id, retail price, release date, description, image), current market data (lowest ask, highest bid, last sale, trailing average price/sales count, delivery-speed ask tiers), individual seller listings (price, condition, size), related-product recommendations (other colorways/siblings StockX surfaces on the product page), and any promotional badges. Credential-free public data from StockX's own product-page GraphQL API.
- **Params:** `slug` (string, **required**) — StockX product URL slug (the urlKey), the path segment of a https://stockx.com/{slug} product page

### `stockx_releases`

- **HTTP:** `GET /stockx/releases`
- **What:** Get StockX upcoming release calendar. Returns a date-ordered page (release date ascending) of StockX's upcoming release calendar: new and restocked products releasing on or after the given date, with normalized product summaries, headline pricing, and each item's published release date. Credential-free public data from the same GraphQL API backing StockX's own releases page.
- **Params:** `from` (string, optional) — Only include releases on or after this date (YYYY-MM-DD, UTC). Defaults to today; `limit` (integer, optional) — Results per page, defaults to 20, maximum 100; `page` (integer, optional) — 1-indexed result page, defaults to 1

### `stockx_search`

- **HTTP:** `GET /stockx/search`
- **What:** Search/browse StockX products. Browses StockX's product catalog by category with optional free-text keyword search and facet filters (gender, brand, color, shoe height, activity, availability), returning normalized product summaries with headline pricing plus the total matching count. Credential-free public data from the same GraphQL API backing StockX's own category browse pages.
- **Params:** `activity` (string, optional) — Filter by activity, comma-separated for multiple values; `available_now` (boolean, optional) — Only include products with at least one active ask; `below_retail` (boolean, optional) — Only include products currently trading below original retail price; `brand` (string, optional) — Filter by one or more brand slugs, comma-separated, e.g. jordan,nike; `category` (string, **required**) — StockX top-level category; `color` (string, optional) — Filter by color, comma-separated for multiple values; `gender` (string, optional) — Filter by gender, comma-separated for multiple values; `limit` (integer, optional) — Results per page, defaults to 20, maximum 100; `model` (string, optional) — Filter by a single model slug, e.g. air-force-1. Requires exactly one value in brand; `page` (integer, optional) — 1-indexed result page, defaults to 1; `query` (string, optional) — Free-text keyword search within the category, e.g. a model name or colorway; `shoe_height` (string, optional) — Filter by shoe height, comma-separated for multiple values; `sort` (string, optional) — Result sort order, defaults to featured; `xpress_ship` (boolean, optional) — Only include products with StockX Xpress Ship availability

## Strava (4)

### `strava_challenges`

- **HTTP:** `GET /strava/challenges`
- **What:** Strava's public challenge gallery. Returns Strava's public challenge gallery: the currently promoted challenge plus every gallery section (partner challenges, and one section per sport such as run/ride), each with its challenges' goal, duration, and cover art. Public data, sourced from Strava's own challenge gallery.
- **Params:** _none_

### `strava_club`

- **HTTP:** `GET /strava/clubs/{id}`
- **What:** A Strava club's public profile. Returns a Strava club's public profile: name, verified/private flags, location, description, member count, and cover/avatar images. Only the base public profile is returned -- discussion, leaderboard, member list, and recent-activity data require a logged-in Strava session and are not available. Public data, sourced from Strava's own server-rendered club page.
- **Params:** `id` (string, **required**) — Strava club ID

### `strava_route_detail`

- **HTTP:** `GET /strava/routes/detail`
- **What:** A single Strava route's detail page. Returns a single Strava route's detail: type, difficulty, distance, elevation gain, estimated time, and summary. `path` is the relative route path returned by `/strava/routes` results (e.g. `hiking/usa/colorado/boulder/mallory-cave_5171952737974445730`). Public data, sourced from Strava's own server-rendered route pages.
- **Params:** `path` (string, **required**) — Relative route path, from a /strava/routes result's path field

### `strava_routes`

- **HTTP:** `GET /strava/routes`
- **What:** Strava route-index listing for a sport, country, and region. Returns a page of Strava's public route recommendations for a sport, country, and region (state, or state/city). `sport` values: `hiking`, `road-biking`, `mountain-biking`, `trail-running`, `gravel-biking`. Public data, sourced from Strava's own server-rendered route pages.
- **Params:** `country` (string, **required**) — Country slug, e.g. usa; `page` (integer, optional) — Page number, starting at 1; `region` (string, **required**) — Region slug: a state (colorado) or state/city (colorado/boulder); `sport` (string, **required**) — Route sport. Allowed values: hiking, road-biking, mountain-biking, trail-running, gravel-biking

## Target (7)

### `target_categories`

- **HTTP:** `GET /target/categories`
- **What:** List all Target categories. Returns Target's current top-level category menu and the complete grouped shop-all directory, including category ids and canonical URLs.
- **Params:** _none_

### `target_category_products`

- **HTTP:** `GET /target/category-products`
- **What:** Browse Target category products. Returns paginated products for any category id from target-categories. Each response also contains every available dynamic filter group and option. Pass selected option ids through filter_ids as a comma-separated list. The sort enum accepts `relevance`, `featured`, `price-low`, `price-high`, `rating`, `bestselling`, and `newest`.
- **Params:** `category_id` (string, **required**) — Target category id; `filter_ids` (string, optional) — Comma-separated Target filter option ids; `page` (integer, optional) — One-based page (1-50); `sort` (string, optional) — Result order; `store_id` (integer, optional) — Target store id used for pricing

### `target_filter_options`

- **HTTP:** `GET /target/filter-options`
- **What:** List Target filter options. Returns every dynamic filter group and option for either a product query or category. Provide exactly one of q or category_id. Pass currently selected option ids through filter_ids to obtain the remaining context-aware options.
- **Params:** `category_id` (string, optional) — Target category id; mutually exclusive with q; `filter_ids` (string, optional) — Comma-separated selected Target filter option ids; `q` (string, optional) — Product search query; mutually exclusive with category_id; `store_id` (integer, optional) — Target store id used for pricing

### `target_product`

- **HTTP:** `GET /target/product`
- **What:** Get a Target product. Returns normalized product details for one Target item, including product content, images, price, rating, category, and availability flags for the selected store.
- **Params:** `store_id` (integer, optional) — Target store id used for pricing and availability; `tcin` (string, **required**) — Numeric Target item id (TCIN)

### `target_questions`

- **HTTP:** `GET /target/questions`
- **What:** List Target product questions and answers. Returns paginated product questions with their nested answers.
- **Params:** `page` (integer, optional) — Zero-based page; `per_page` (integer, optional) — Questions per page; `tcin` (string, **required**) — Numeric Target item id

### `target_reviews`

- **HTTP:** `GET /target/reviews`
- **What:** List Target product reviews. Returns paginated written reviews for a Target item. Pagination is zero-based and page 50 is the upstream maximum.
- **Params:** `page` (integer, optional) — Zero-based page; `per_page` (integer, optional) — Reviews per page; `tcin` (string, **required**) — Numeric Target item id

### `target_search`

- **HTTP:** `GET /target/search`
- **What:** Search Target products. Searches Target products and returns normalized products plus every filter group and option available for the current result set. Pass option ids back through filter_ids as a comma-separated list. A zero total with an empty products list is a valid no-results response. The sort enum accepts `relevance`, `featured`, `price-low`, `price-high`, `rating`, `bestselling`, and `newest`.
- **Params:** `filter_ids` (string, optional) — Comma-separated Target filter option ids; `page` (integer, optional) — One-based page (1-50); `q` (string, **required**) — Product search query; `sort` (string, optional) — Result order; `store_id` (integer, optional) — Target store id used for pricing

## Tesla Jobs (2)

### `tesla_jobs_job`

- **HTTP:** `GET /tesla-jobs/job`
- **What:** Tesla Jobs single posting. Returns one Tesla Careers posting by its numeric job id (the `id` field returned by the list endpoint). Parsed from tesla.com's own job detail JSON endpoint.
- **Params:** `id` (string, **required**) — Tesla job id

### `tesla_jobs_list`

- **HTTP:** `GET /tesla-jobs/list`
- **What:** Tesla Jobs listing. Searches Tesla's public careers site (tesla.com/careers) via its own careers-state JSON endpoint. Tesla's own endpoint always returns its entire global job dataset regardless of query parameters; this filters and paginates that snapshot server-side. Listings carry identity/department/location metadata only — call the job endpoint for the full description, responsibilities, and requirements.
- **Params:** `location` (string, optional) — Filter by location, case-insensitive substring match; `page` (integer, optional) — Page number, 1-based; `page_size` (integer, optional) — Results per page, up to 100; `query` (string, optional) — Filter by title or department, case-insensitive substring match

## Threads (5)

### `threads_post`

- **HTTP:** `GET /threads/post/{username}/{code}`
- **What:** Retrieve a public Threads post. Returns the public text, author, canonical URL, and preview image for a Threads post.
- **Params:** `code` (string, **required**) — Threads post code; `username` (string, **required**) — Threads username

### `threads_post_replies`

- **HTTP:** `GET /threads/post/{username}/{code}/replies`
- **What:** Retrieve public replies to a Threads post. Returns the public replies currently exposed to logged-out visitors. The response identifies when Threads reports additional replies but withholds a usable continuation cursor.
- **Params:** `code` (string, **required**) — Threads post code; `username` (string, **required**) — Threads username

### `threads_profile`

- **HTTP:** `GET /threads/profile/{username}`
- **What:** Retrieve a public Threads profile. Returns public profile metadata for a Threads username, including the visible biography and counts.
- **Params:** `username` (string, **required**) — Threads username

### `threads_profile_posts`

- **HTTP:** `GET /threads/profile/{username}/posts`
- **What:** Retrieve public posts from a Threads profile. Returns public profile posts with an opaque continuation cursor when more posts are available.
- **Params:** `cursor` (string, optional) — Opaque cursor returned by the previous response; `username` (string, **required**) — Threads username

### `threads_search`

- **HTTP:** `GET /threads/search`
- **What:** Search public Threads posts. Returns the public first page of Threads search results for a query. Logged-out search does not expose a continuation cursor.
- **Params:** `q` (string, **required**) — Search query (1-100 characters)

## Ticketmaster (11)

### `ticketmaster_attraction`

- **HTTP:** `GET /ticketmaster/attraction`
- **What:** Get a Ticketmaster attraction. Returns normalized details for one Ticketmaster artist, team, or other attraction.
- **Params:** `id` (string, **required**) — Numeric Ticketmaster attraction id

### `ticketmaster_attraction_events`

- **HTTP:** `GET /ticketmaster/attraction-events`
- **What:** List an attraction's Ticketmaster events. Returns upcoming Ticketmaster events for one attraction. The sort enum accepts `relevance` and `date`.
- **Params:** `id` (string, **required**) — Numeric Ticketmaster attraction id; `page` (integer, optional) — Zero-based page (0-49); `sort` (string, optional) — Result order

### `ticketmaster_discover_categories`

- **HTTP:** `GET /ticketmaster/discover-categories`
- **What:** List Ticketmaster discover categories. Lists every current Concerts, Sports, Arts & Theater, and Family category with pagination. Section accepts `all`, `concerts`, `sports`, `arts-theater`, and `family`.
- **Params:** `page` (integer, optional) — One-based page; `per_page` (integer, optional) — Categories per page; `section` (string, optional) — Discover section

### `ticketmaster_discover_category_events`

- **HTTP:** `GET /ticketmaster/discover-category-events`
- **What:** List events in a Ticketmaster discover category. Returns a zero-based paginated event feed for any category returned by ticketmaster-discover-categories.
- **Params:** `category_id` (string, **required**) — Ticketmaster discover category id; `page` (integer, optional) — Zero-based page

### `ticketmaster_discover_cities`

- **HTTP:** `GET /ticketmaster/discover-cities`
- **What:** List Ticketmaster discover cities. Lists Ticketmaster city discovery destinations for a country with pagination.
- **Params:** `country` (string, optional) — Two-letter country code; `page` (integer, optional) — One-based page; `per_page` (integer, optional) — Cities per page

### `ticketmaster_discover_city_events`

- **HTTP:** `GET /ticketmaster/discover-city-events`
- **What:** List events in a Ticketmaster discover city. Returns a zero-based paginated event feed for a city slug returned by ticketmaster-discover-cities.
- **Params:** `city` (string, **required**) — Ticketmaster discover city slug; `country` (string, optional) — Two-letter country code matching the selected city; `page` (integer, optional) — Zero-based page

### `ticketmaster_event`

- **HTTP:** `GET /ticketmaster/event`
- **What:** Get a Ticketmaster event. Returns normalized details for one Ticketmaster event, including its venue, attractions, timing, availability flags, and classification.
- **Params:** `id` (string, **required**) — Ticketmaster event id

### `ticketmaster_search_events`

- **HTTP:** `GET /ticketmaster/search-events`
- **What:** Search Ticketmaster events. Searches Ticketmaster events by artist, event, team, or venue. A zero total with an empty events list is a valid no-results response. The sort enum accepts `relevance` and `date`.
- **Params:** `page` (integer, optional) — Zero-based page (0-49); `q` (string, **required**) — Artist, event, team, or venue query; `sort` (string, optional) — Result order

### `ticketmaster_suggest`

- **HTTP:** `GET /ticketmaster/suggest`
- **What:** Suggest Ticketmaster artists, events, and venues. Returns autocomplete suggestions for a partial query.
- **Params:** `q` (string, **required**) — Partial artist, event, team, or venue query

### `ticketmaster_venue`

- **HTTP:** `GET /ticketmaster/venue`
- **What:** Get a Ticketmaster venue. Returns normalized details and visitor information for one Ticketmaster venue.
- **Params:** `id` (string, **required**) — Numeric Ticketmaster venue id

### `ticketmaster_venue_events`

- **HTTP:** `GET /ticketmaster/venue-events`
- **What:** List a venue's Ticketmaster events. Returns upcoming Ticketmaster events at one venue. The sort enum accepts `relevance` and `date`.
- **Params:** `id` (string, **required**) — Numeric Ticketmaster venue id; `page` (integer, optional) — Zero-based page (0-49); `sort` (string, optional) — Result order

## TikTok (25)

### `tiktok_category`

- **HTTP:** `GET /tiktok/category`
- **What:** List TikTok explore categories. Returns the category list exposed by the TikTok Explore page.
- **Params:** _none_

### `tiktok_challenge`

- **HTTP:** `GET /tiktok/hashtag/{name}`
- **What:** Retrieve TikTok hashtag details. Returns the metadata payload for a TikTok hashtag page.
- **Params:** `name` (string, **required**) — Hashtag name (e.g., 'christmas')

### `tiktok_challenge_list`

- **HTTP:** `GET /tiktok/hashtags`
- **What:** Retrieve TikTok hashtag posts. Returns the videos listed for a TikTok hashtag id with cursor-based pagination.
- **Params:** `cursor` (integer, optional) — Pagination cursor; `id` (string, **required**) — Hashtag id returned by the hashtag detail endpoint

### `tiktok_comments`

- **HTTP:** `GET /tiktok/comments`
- **What:** Retrieve TikTok video comments. Returns top-level TikTok video comments with cursor-based pagination.
- **Params:** `aweme_id` (string, **required**) — TikTok video id from the video URL; `cursor` (integer, optional) — Pagination cursor

### `tiktok_creative_center_hashtags`

- **HTTP:** `GET /tiktok/creative-center/hashtags`
- **What:** Retrieve TikTok Creative Center trending hashtags. Returns TikTok Creative Center's ranked trending hashtags for a country and period. TikTok gates this endpoint's full result set behind a logged-in TikTok One account: an anonymous request always receives at most 3 hashtags regardless of country or period.
- **Params:** `country_code` (string, **required**) — ISO-2 country code; `period` (integer, optional) — Lookback window in days

### `tiktok_creative_center_videos`

- **HTTP:** `GET /tiktok/creative-center/videos`
- **What:** Retrieve TikTok Creative Center trending videos. Returns TikTok Creative Center's ranked trending videos for a country, period, and sort order. TikTok reports the true result-set size (see total_count/page_count in the response) but gates access to it behind a logged-in TikTok One account: an anonymous request always receives page 1 (4 videos) regardless of sort order or period. Country coverage is uneven: US, JP, ID, VN, and TH reliably return populated results; other countries have been observed to return an empty videos array (a genuine no-data response, not an error).
- **Params:** `content_label_id` (string, optional) — Content tag id to filter by; `country_code` (string, **required**) — ISO-2 country code; `organic_only` (boolean, optional) — Restrict to organic (non-paid) videos only; `period` (integer, optional) — Lookback window in days; `sort_by` (string, optional) — Sort order

### `tiktok_explore`

- **HTTP:** `GET /tiktok/explore/{id}`
- **What:** Retrieve the TikTok explore feed for a category. Returns explore videos for a TikTok category id from the category endpoint.
- **Params:** `id` (integer, **required**) — Category type id returned by the category endpoint

### `tiktok_popular_trend_country_industry_meta`

- **HTTP:** `GET /tiktok/popular-trend/country-industry-meta`
- **What:** Retrieve TikTok popular-trend country and industry metadata. Returns the country and industry metadata used by the TikTok Creative Center popular-trend endpoints.
- **Params:** _none_

### `tiktok_post`

- **HTTP:** `GET /tiktok/post/{id}`
- **What:** Retrieve TikTok video details. Returns the TikTok video detail payload for a video id.
- **Params:** `id` (string, **required**) — TikTok video id

### `tiktok_posts`

- **HTTP:** `GET /tiktok/posts`
- **What:** Retrieve posts from a TikTok profile. Returns posts from a TikTok profile by `secUid`, with optional cursor pagination and sort mode.
- **Params:** `cursor` (integer, optional) — Pagination cursor; `secUid` (string, **required**) — TikTok secUid for the profile; `sort_type` (integer, optional) — Sort mode: 0 latest, 1 popular, 2 oldest

### `tiktok_profile`

- **HTTP:** `GET /tiktok/profile/{handler}`
- **What:** Retrieve a TikTok profile. Returns the TikTok profile payload for a public handle.
- **Params:** `handler` (string, **required**) — TikTok handle without the leading @

### `tiktok_search`

- **HTTP:** `GET /tiktok/search`
- **What:** Search TikTok videos. Searches TikTok videos by keyword with cursor-based pagination.
- **Params:** `count` (integer, optional) — Result count, clamped to 50; `cursor` (integer, optional) — Pagination cursor; `keyword` (string, **required**) — Search keyword

### `tiktok_search_hashtag`

- **HTTP:** `GET /tiktok/search/hashtag`
- **What:** Search TikTok hashtags. Searches TikTok hashtags/challenges by keyword with cursor-based pagination.
- **Params:** `count` (integer, optional) — Result count, clamped to 50; `cursor` (integer, optional) — Pagination cursor; `keyword` (string, **required**) — Search keyword

### `tiktok_search_user`

- **HTTP:** `GET /tiktok/search/user`
- **What:** Search TikTok users. Searches TikTok users by keyword with cursor-based pagination.
- **Params:** `cursor` (integer, optional) — Pagination cursor; `keyword` (string, **required**) — Search keyword

### `tiktok_top_ads_analysis`

- **HTTP:** `GET /tiktok/top-ads/analysis`
- **What:** Retrieve TikTok Top Ads interactive time analysis. Returns the detail-page interactive time analysis chart and percentile for a Top Ads material. Metric values are `retain_ctr` (CTR), `retain_cvr` (CVR), `click_cnt` (Clicks), `convert_cnt` (Conversion), and `play_retain_cnt` (Remain).
- **Params:** `material_id` (string, **required**) — Top Ads material id; `metric` (string, optional) — Interactive time analysis metric; `period_type` (integer, optional) — Percentile lookback period in days

### `tiktok_top_ads_detail`

- **HTTP:** `GET /tiktok/top-ads/detail`
- **What:** Retrieve TikTok Top Ads detail. Returns detail for one TikTok Creative Center Top Ads material. Use `material_id`; the upstream does not accept `id` or `materialId`.
- **Params:** `material_id` (string, **required**) — Top Ads material id

### `tiktok_top_ads_filters`

- **HTTP:** `GET /tiktok/top-ads/filters`
- **What:** Retrieve TikTok Top Ads filters. Returns filter metadata for TikTok Creative Center Top Ads. Dynamic values come from TikTok; static UI enums are included for `order_by`, `duration`, `like`, and `ad_format`.
- **Params:** _none_

### `tiktok_top_ads_list`

- **HTTP:** `GET /tiktok/top-ads/list`
- **What:** Retrieve TikTok Top Ads. Returns high-performing auction ads from TikTok Creative Center. The service defaults `period` to 30, `page` to 1, `limit` to 20, and `order_by` to `for_you`. Use `/tiktok/top-ads/filters` for dynamic enum values and static enums for order, duration, likes, and ad format.
- **Params:** `ad_format` (string, optional) — Ad format id; `ad_language` (string, optional) — Ad language id or comma-separated ids from /tiktok/top-ads/filters; `country_code` (string, optional) — Country code or comma-separated country codes from /tiktok/top-ads/filters; `duration` (string, optional) — Video duration bucket; `industry` (string, optional) — Industry filter id or comma-separated ids from /tiktok/top-ads/filters; `keyword` (string, optional) — Brand or product keyword search; `like` (string, optional) — Like percentile bucket id or comma-separated ids; `limit` (integer, optional) — Maximum number of ads to return; `objective` (string, optional) — Objective filter id or comma-separated ids from /tiktok/top-ads/filters; `order_by` (string, optional) — Sort order; `page` (integer, optional) — Page number; `pattern_label` (string, optional) — Pattern label id or comma-separated ids from /tiktok/top-ads/filters; `period` (integer, optional) — Lookback period in days

### `tiktok_top_ads_location_info`

- **HTTP:** `GET /tiktok/top-ads/location-info`
- **What:** Retrieve TikTok Top Ads location info. Returns the initial location and industry context used by TikTok Creative Center Top Ads.
- **Params:** `module` (integer, optional) — Creative Center module id

### `tiktok_top_ads_locations`

- **HTTP:** `GET /tiktok/top-ads/locations`
- **What:** Retrieve TikTok Top Ads locations. Returns available Top Ads location filters from TikTok Creative Center.
- **Params:** _none_

### `tiktok_top_ads_recommend`

- **HTTP:** `GET /tiktok/top-ads/recommend`
- **What:** Retrieve TikTok Top Ads recommendations. Returns recommended Top Ads materials related to a material id.
- **Params:** `limit` (integer, optional) — Maximum number of ads to return; `material_id` (string, **required**) — Top Ads material id; `page` (integer, optional) — Page number

### `tiktok_top_ads_safety`

- **HTTP:** `GET /tiktok/top-ads/safety`
- **What:** Retrieve TikTok Top Ads safety configuration. Returns public Creative Center safety configuration flags related to search surfaces.
- **Params:** _none_

### `tiktok_top_ads_spotlight`

- **HTTP:** `GET /tiktok/top-ads/spotlight`
- **What:** Retrieve TikTok Top Ads Spotlight. Returns Top Ads Spotlight materials handpicked by TikTok Creative Center.
- **Params:** `limit` (integer, optional) — Maximum number of ads to return; `page` (integer, optional) — Page number

### `tiktok_top_ads_suggestions`

- **HTTP:** `GET /tiktok/top-ads/suggestions`
- **What:** Retrieve TikTok Top Ads suggestions. Returns Top Ads search suggestions from TikTok Creative Center.
- **Params:** `count` (integer, optional) — Maximum number of suggestions to return; `scenario` (integer, optional) — Suggestion scenario id

### `tiktok_trending`

- **HTTP:** `GET /tiktok/trending`
- **What:** Retrieve TikTok trending posts. Returns the current TikTok trending feed.
- **Params:** _none_

## TMDB (7)

### `tmdb_movie`

- **HTTP:** `GET /tmdb/movie/{id}`
- **What:** Get a TMDB movie. Returns a normalized TMDB movie: overview, tagline, genres, countries, runtime, budget/revenue, top-billed cast, top crew (director/writer), and aggregate rating. Credential-free public TMDB data (themoviedb.org) — not the official api.themoviedb.org, which requires an API key.
- **Params:** `id` (string, **required**) — TMDB movie id

### `tmdb_movie_list`

- **HTTP:** `GET /tmdb/movie/list`
- **What:** Get a TMDB movie chart. Returns a TMDB movie chart (popular, top rated, now playing, or upcoming). Credential-free public TMDB data.
- **Params:** `category` (string, optional) — Movie chart, default popular; `date_from` (string, optional) — Release date lower bound (YYYY-MM-DD); `date_to` (string, optional) — Release date upper bound (YYYY-MM-DD); `include_adult` (boolean, optional) — Include adult titles; `limit` (integer, optional) — Max movies, default 10, max 20; `max_rating` (number, optional) — Maximum rating, 0-10; `max_runtime` (integer, optional) — Maximum runtime in minutes; `min_rating` (number, optional) — Minimum rating, 0-10; `min_runtime` (integer, optional) — Minimum runtime in minutes; `min_votes` (integer, optional) — Minimum vote count; `original_language` (string, optional) — Two-letter original-language code; `page` (integer, optional) — 1-based page, default 1; `sort_by` (string, optional) — Sort order; `with_genres` (string, optional) — Comma- or pipe-separated TMDB genre ids

### `tmdb_person`

- **HTTP:** `GET /tmdb/person/{id}`
- **What:** Get a TMDB person. Returns a normalized TMDB person: biography, birth date, photo, and filmography (movie and TV credits). Credential-free public TMDB data.
- **Params:** `id` (string, **required**) — TMDB person id; `limit` (integer, optional) — Max filmography credits, default 10, max 20

### `tmdb_person_list`

- **HTTP:** `GET /tmdb/person/list`
- **What:** List popular people on TMDB. Returns one page from TMDB's Popular People directory, including each person's id, name, known-for titles, profile image, and detail URL. Credential-free public TMDB data.
- **Params:** `limit` (integer, optional) — Max people, default 10, max 20; `page` (integer, optional) — 1-based page, default 1

### `tmdb_search`

- **HTTP:** `GET /tmdb/search`
- **What:** Search TMDB. Searches TMDB movies, TV shows, and people. An unscoped query interleaves results across all three types rather than returning whichever type happens to rank first upstream. Credential-free public TMDB data.
- **Params:** `limit` (integer, optional) — Max results, default 10, max 20; `page` (integer, optional) — 1-based results page, default 1; `query` (string, **required**) — Search query; `type` (string, optional) — Optional result type filter

### `tmdb_tv`

- **HTTP:** `GET /tmdb/tv/{id}`
- **What:** Get a TMDB TV show. Returns a normalized TMDB TV show: overview, tagline, genres, countries, episode count, first/last air year, top-billed cast, top crew (creator), and aggregate rating. Credential-free public TMDB data.
- **Params:** `id` (string, **required**) — TMDB TV show id

### `tmdb_tv_list`

- **HTTP:** `GET /tmdb/tv/list`
- **What:** Get a TMDB TV chart. Returns a TMDB TV chart (popular, top rated, airing today, or on the air). Credential-free public TMDB data.
- **Params:** `category` (string, optional) — TV chart, default popular; `date_from` (string, optional) — First-air date lower bound (YYYY-MM-DD); `date_to` (string, optional) — First-air date upper bound (YYYY-MM-DD); `include_adult` (boolean, optional) — Include adult titles; `limit` (integer, optional) — Max shows, default 10, max 20; `max_rating` (number, optional) — Maximum rating, 0-10; `max_runtime` (integer, optional) — Maximum runtime in minutes; `min_rating` (number, optional) — Minimum rating, 0-10; `min_runtime` (integer, optional) — Minimum runtime in minutes; `min_votes` (integer, optional) — Minimum vote count; `original_language` (string, optional) — Two-letter original-language code; `page` (integer, optional) — 1-based page, default 1; `sort_by` (string, optional) — Sort order; `with_genres` (string, optional) — Comma- or pipe-separated TMDB genre ids

## Trip.com (2)

### `tripcom_hotel_detail`

- **HTTP:** `GET /tripcom/hotels/{id}`
- **What:** Get Trip.com hotel detail. Returns a normalized Trip.com hotel-detail page: identity (name, local name, star rating, city/province/country), location (address, zone, latitude/longitude, nearby-transport description), guest rating (overall score plus cleanliness/amenities/location/service breakdown), images, description, check-in/check-out and child policy summaries, and popular facilities. Credential-free public data sourced from Trip.com's own server-rendered hotel-detail page. Pricing is not included: Trip.com's detail page only returns per-night rates alongside check-in/check-out dates, which this endpoint does not take as input -- use the search endpoint for a city's current display prices.
- **Params:** `id` (string, **required**) — Trip.com hotel id, from a prior search call's hotel_id field; `slug` (string, optional) — Optional slug segment for a nicer canonical source URL (e.g. the district/city slug from a search result's url). Not required and not validated by Trip.com.

### `tripcom_hotels_search`

- **HTTP:** `GET /tripcom/hotels/search`
- **What:** Search Trip.com hotels by city. Returns Trip.com's own top-hotels page for a city: normalized hotel summaries (name, location, star rating, guest rating, review count, image, display price) for the hotels Trip.com features on that city's hotel-list page. Trip.com does not expose a credential-free free-text city search, so callers supply the exact city_slug and city_id pair from a known Trip.com hotel-list URL of the form https://www.trip.com/hotels/{city_slug}-hotels-list-{city_id}/. Credential-free public data sourced from Trip.com's own server-rendered hotel-list page.
- **Params:** `city_id` (string, **required**) — Trip.com numeric city id, the trailing number of a /hotels/{city_slug}-hotels-list-{city_id}/ URL; `city_slug` (string, **required**) — Trip.com city slug, the text segment of a /hotels/{city_slug}-hotels-list-{city_id}/ URL

## TripAdvisor (6)

### `tripadvisor_autocomplete`

- **HTTP:** `GET /tripadvisor/autocomplete`
- **What:** Autocomplete TripAdvisor locations and places. Returns normalized TripAdvisor public typeahead candidates from the credential-free GraphQL endpoint.
- **Params:** `limit` (integer, optional) — Maximum results; `locale` (string, optional) — TripAdvisor locale; `q` (string, **required**) — Autocomplete query; `route_uid` (string, optional) — Optional captured route uid; `scope_geo_id` (integer, optional) — Optional scoped geo id; `search_session_id` (string, optional) — Optional captured search session id; `type` (string, optional) — Optional result type hint; `typeahead_id` (string, optional) — Optional captured typeahead id

### `tripadvisor_enums`

- **HTTP:** `GET /tripadvisor/enums`
- **What:** Get TripAdvisor enum metadata. Returns supported TripAdvisor enum values for place/listing filters, including locales, currencies, languages, listing types, filters, amenities, and category ids.
- **Params:** _none_

### `tripadvisor_hotels`

- **HTTP:** `GET /tripadvisor/hotels`
- **What:** Search TripAdvisor hotels. Returns normalized TripAdvisor hotel listing results from public credential-free GraphQL listing data.
- **Params:** `amenities` (array, optional) — Amenity filter ids; `class` (integer, optional) — Hotel class filter; `currency` (string, optional) — Currency code; `filter_id` (string, optional) — Optional filter id such as class or ufe; `geo_id` (integer, **required**) — TripAdvisor geo id; `limit` (integer, optional) — Maximum results; `offset` (integer, optional) — Zero-based result offset; `price_max` (integer, optional) — Maximum price filter; `price_min` (integer, optional) — Minimum price filter; `pricing_mode` (string, optional) — Pricing mode; `sort` (string, optional) — Sort value; `travelers_choice` (boolean, optional) — Filter Travelers' Choice properties; `travelers_choice_botb` (boolean, optional) — Filter Best of the Best properties

### `tripadvisor_place`

- **HTTP:** `GET /tripadvisor/place`
- **What:** Get TripAdvisor place. Returns a rich normalized TripAdvisor place profile. Destination and bookable tour/experience pages resolve through a faster dedicated lookup; everything else comes from public place HTML, using configured browser fallbacks when direct HTML is blocked.
- **Params:** `id` (string, optional) — TripAdvisor location id fallback; `url` (string, optional) — TripAdvisor place URL

### `tripadvisor_reviews`

- **HTTP:** `GET /tripadvisor/reviews`
- **What:** Get TripAdvisor reviews. Returns normalized TripAdvisor public reviews from credential-free GraphQL review data. Pass either id or url.
- **Params:** `do_machine_translation` (boolean, optional) — Enable upstream machine translation; `id` (string, optional) — TripAdvisor location id; `language` (string, optional) — Review language; `limit` (integer, optional) — Maximum reviews; `page` (integer, optional) — 1-based review page; `photos_per_review_limit` (integer, optional) — Maximum photos per review; `ratings` (array, optional) — Rating filters; `sort_by` (string, optional) — Review sort field; `sort_type` (string, optional) — Review sort type; `url` (string, optional) — TripAdvisor place URL

### `tripadvisor_search`

- **HTTP:** `GET /tripadvisor/search`
- **What:** Search TripAdvisor places. Returns normalized TripAdvisor place listings for hotels, restaurants, attractions, and supported attraction category types.
- **Params:** `amenities` (array, optional) — Hotel amenity filter ids; `class` (integer, optional) — Hotel class filter; `currency` (string, optional) — Currency code; `establishment_types` (array, optional) — Restaurant establishment type ids; `filter_id` (string, optional) — Optional hotel filter id; `geo_id` (integer, **required**) — TripAdvisor geo id; `limit` (integer, optional) — Maximum results; `locale` (string, optional) — TripAdvisor locale; `offset` (integer, optional) — Zero-based result offset; `online_options` (array, optional) — Restaurant online option ids; `price_max` (integer, optional) — Maximum hotel price filter; `price_min` (integer, optional) — Minimum hotel price filter; `pricing_mode` (string, optional) — Hotel pricing mode; `restaurant_date` (string, optional) — Restaurant availability date; `restaurant_guests` (integer, optional) — Restaurant guest count; `restaurant_time` (string, optional) — Restaurant availability time; `sort` (string, optional) — Sort value; `travelers_choice` (boolean, optional) — Filter Travelers' Choice hotels; `travelers_choice_botb` (boolean, optional) — Filter Best of the Best hotels; `type` (string, **required**) — Listing type

## TrustMRR (7)

### `trustmrr_acquire`

- **HTTP:** `GET /trustmrr/acquire`
- **What:** Get TrustMRR acquisition listings. Returns the for-sale startups rendered on the public TrustMRR /acquire marketplace page, with deal metrics (asking price, revenue, multiple, growth). Verified revenue figures come from supported payment providers.
- **Params:** _none_

### `trustmrr_categories`

- **HTTP:** `GET /trustmrr/categories`
- **What:** Get TrustMRR categories. Returns the TrustMRR startup category directory (slug, label, description, and keywords for each category).
- **Params:** _none_

### `trustmrr_category`

- **HTTP:** `GET /trustmrr/category/{slug}`
- **What:** Get TrustMRR category detail. Returns a single TrustMRR category page and the startups listed under it, with verified revenue and MRR figures.
- **Params:** `slug` (string, **required**) — TrustMRR category slug

### `trustmrr_leaderboard`

- **HTTP:** `GET /trustmrr/leaderboard`
- **What:** Get TrustMRR revenue leaderboard. Returns the top 100 startups ranked by the selected metric from the public TrustMRR leaderboard. Revenue and MRR figures are verified through supported payment providers.
- **Params:** `metric` (string, optional) — Leaderboard metric to rank by (default mrr)

### `trustmrr_marketplace`

- **HTTP:** `GET /trustmrr/marketplace`
- **What:** Get TrustMRR marketplace snapshot. Returns the public TrustMRR marketplace snapshot: the 25 most recently listed startups for sale and the current 25 best deals ranked by TrustMRR's recency-aware deal score. Revenue figures are verified through supported payment providers.
- **Params:** _none_

### `trustmrr_startup`

- **HTTP:** `GET /trustmrr/startup/{slug}`
- **What:** Get TrustMRR startup detail. Returns the full verified profile for a single TrustMRR startup by slug: revenue and MRR, growth, asking price and marketplace status, tech stack, marketing channels, and TrustMRR's AI-generated business summary.
- **Params:** `slug` (string, **required**) — TrustMRR startup slug

### `trustmrr_startups`

- **HTTP:** `GET /trustmrr/startups`
- **What:** List all TrustMRR startups. Returns a paginated list of every startup in the TrustMRR directory, discovered from the site's public sitemap. Each entry is a slug you can pass to /trustmrr/startup/{slug} for the full verified profile — together these two endpoints let you enumerate and scrape the entire directory without the authenticated marketplace API.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `page_size` (integer, optional) — Items per page (default 100, max 1000)

## Trustpilot (7)

### `trustpilot_business`

- **HTTP:** `GET /trustpilot/business/{slug}`
- **What:** Get Trustpilot business profile. Returns a summary Trustpilot business profile parsed from the public business page.
- **Params:** `slug` (string, **required**) — Trustpilot business slug

### `trustpilot_business_related`

- **HTTP:** `GET /trustpilot/business/{slug}/related`
- **What:** Get Trustpilot related businesses. Returns related company cards from Trustpilot's public business page rails.
- **Params:** `slug` (string, **required**) — Trustpilot business slug

### `trustpilot_business_reviews`

- **HTTP:** `GET /trustpilot/business/{slug}/reviews`
- **What:** Get Trustpilot business reviews. Returns paginated Trustpilot business reviews parsed from the public review page.
- **Params:** `date_from` (string, optional) — Date range start in YYYY-MM-DD; currently rejected by upstream; `date_to` (string, optional) — Date range end in YYYY-MM-DD; currently rejected by upstream; `language` (string, optional) — Review language code used by Trustpilot; `page` (integer, optional) — 1-based page number; defaults to 1; `q` (string, optional) — Text search within reviews; `replied` (boolean, optional) — Filter to reviews with business replies; `slug` (string, **required**) — Trustpilot business slug; `stars` (integer, optional) — Filter by star rating from 1 to 5; `verified` (boolean, optional) — Filter to verified reviews

### `trustpilot_business_search`

- **HTTP:** `GET /trustpilot/business-units/search`
- **What:** Search Trustpilot business units. Returns normalized business-unit search results from Trustpilot's JSON business-unit search API.
- **Params:** `country` (string, optional) — Two-letter country code; defaults to US; `page` (integer, optional) — 1-based page number; defaults to 1; `page_size` (integer, optional) — Results per page; defaults to 20, maximum 100; `q` (string, **required**) — Search query

### `trustpilot_categories`

- **HTTP:** `GET /trustpilot/categories`
- **What:** Get Trustpilot categories. Returns the Trustpilot public category index grouped by top-level category.
- **Params:** _none_

### `trustpilot_category`

- **HTTP:** `GET /trustpilot/category/{slug}`
- **What:** Get Trustpilot category detail. Returns category metadata, company cards, and side rails from Trustpilot's public category page.
- **Params:** `page` (integer, optional) — 1-based page number; defaults to 1; `slug` (string, **required**) — Trustpilot category slug

### `trustpilot_category_search`

- **HTTP:** `GET /trustpilot/categories/search`
- **What:** Search Trustpilot categories. Returns normalized category search results from Trustpilot's JSON category search API.
- **Params:** `country` (string, optional) — Two-letter country code; defaults to US; `locale` (string, optional) — Locale in ll-CC format; defaults to en-US; `q` (string, **required**) — Search query; `size` (integer, optional) — Maximum number of categories; defaults to 20

## UberEats (5)

### `ubereats_feed`

- **HTTP:** `GET /ubereats/feed`
- **What:** Browse UberEats location feed. Returns restaurants delivering to a specific location: name, rating, review count, delivery estimate, cuisine tags, and cover image. Credential-free public UberEats data.
- **Params:** `latitude` (number, **required**) — Delivery search center latitude; `limit` (integer, optional) — Number of restaurants to return, clamped to 50. Default 20; `longitude` (number, **required**) — Delivery search center longitude; `offset` (integer, optional) — Result offset for the location feed. Default 0

### `ubereats_search`

- **HTTP:** `GET /ubereats/search`
- **What:** Search UberEats restaurants. Returns restaurants delivering to a location: name, rating, review count, delivery estimate, cuisine tags, and image. Pass a keyword to search by name/cuisine/dish, or omit it to browse the general feed for that location. Credential-free public UberEats data.
- **Params:** `cursor` (string, optional) — Opaque pagination cursor from a previous keyword-search response; `latitude` (number, **required**) — Delivery search center latitude; `limit` (integer, optional) — Number of restaurants to return, clamped to 50. Default 20; `longitude` (number, **required**) — Delivery search center longitude; `offset` (integer, optional) — Result offset for the location feed (used only when query is omitted). Default 0; `query` (string, optional) — Keyword — restaurant name, cuisine, or dish

### `ubereats_store`

- **HTTP:** `GET /ubereats/store/{store_id}`
- **What:** Get an UberEats store. Returns a normalized UberEats store: address, phone, rating, cuisine tags, hours tagline, and the full menu (sections with items, descriptions, and prices). Credential-free public UberEats data.
- **Params:** `store_id` (string, **required**) — UberEats store UUID, as returned by the search endpoint's storeUuid field

### `ubereats_store_menu`

- **HTTP:** `GET /ubereats/store/{store_id}/menu`
- **What:** Get an UberEats store menu. Returns the full menu for an UberEats store: section titles, items, item descriptions, prices, and availability status. Credential-free public UberEats data.
- **Params:** `store_id` (string, **required**) — UberEats store UUID, as returned by the search endpoint's storeUuid field

### `ubereats_store_reviews`

- **HTTP:** `GET /ubereats/store/{store_id}/reviews`
- **What:** Get UberEats store reviews. Returns the reviews snapshot embedded in an UberEats store page: aggregate rating, review count, and a sample of recent reviews (reviewer name, text, and relative/absolute date). This is a single on-page snapshot, not a full paginated feed. A store with no written reviews returns an empty reviews list. Credential-free public UberEats data.
- **Params:** `store_id` (string, **required**) — UberEats store UUID, as returned by the search endpoint's storeUuid field

## Upwork (3)

### `upwork_freelancer`

- **HTTP:** `GET /upwork/freelancer/{id}`
- **What:** Get Upwork freelancer profile. Returns a normalized Upwork freelancer profile: name, title, verification badge, overview, hourly rate, rating and review count, Job Success Score, location and local time, total jobs/hours worked, and recent client feedback (title, comment, date, client name, rating). Public data sourced from Upwork's own server-rendered profile pages via a real browser-rendering backend.
- **Params:** `id` (string, **required**) — Upwork freelancer id, the value after \

### `upwork_job`

- **HTTP:** `GET /upwork/job/{id}`
- **What:** Get Upwork job posting detail. Returns a normalized Upwork job posting: title, full description, employment type, budget (hourly range or fixed amount), location/remote type, experience level, duration, project type, proposal count, allowed applicant countries, and a summary of the posting client (member since, location, total spend, hires, hours, industry, company size). Public data sourced from Upwork's own server-rendered job pages via a real browser-rendering backend.
- **Params:** `id` (string, **required**) — Upwork job id, e.g. from a search result's id field

### `upwork_search`

- **HTTP:** `GET /upwork/search`
- **What:** Search Upwork job postings. Searches Upwork's public job listings by free-text keyword, returning normalized job summaries (title, budget, experience level, duration, posted date, description snippet, skill tags). Public data sourced from Upwork's own server-rendered search pages via a real browser-rendering backend.
- **Params:** `page` (integer, optional) — 1-based result page. Defaults to 1.; `q` (string, **required**) — Free-text job search keyword

## Usage (4)

### `usage_endpoints`

- **HTTP:** `GET /usage/me/endpoints`
- **What:** Get current user's endpoint usage breakdown. Returns per-endpoint request and credit totals for the selected UTC time range, ordered by request volume.
- **Params:** `from` (string, optional) — Custom lower bound in RFC3339 format when range=custom; `limit` (integer, optional) — Maximum endpoints to return. Defaults to 20 and clamps to 100.; `range` (string, optional) — Time range preset. Defaults to the current billing period.; `to` (string, optional) — Custom upper bound in RFC3339 format when range=custom

### `usage_overview`

- **HTTP:** `GET /usage/me/overview`
- **What:** Get current user's usage overview. Returns a JWT-authenticated user's current billing snapshot plus recent request and credit consumption metrics for the selected UTC time range. The `requests` summary is limited to product API traffic and excludes console, billing, usage, and user-management endpoints.
- **Params:** `from` (string, optional) — Custom lower bound in RFC3339 format when range=custom; `range` (string, optional) — Time range preset. Defaults to the current billing period.; `to` (string, optional) — Custom upper bound in RFC3339 format when range=custom

### `usage_recent_ips`

- **HTTP:** `GET /usage/me/recent-ips`
- **What:** Get current user's recent API client IPs. Returns recent client IP addresses observed for the JWT-authenticated user's product API traffic, ordered by last seen time. Console, billing, usage, and user-management endpoints are excluded.
- **Params:** `from` (string, optional) — Custom lower bound in RFC3339 format when range=custom; `limit` (integer, optional) — Maximum IPs to return. Defaults to 20 and clamps to 100.; `range` (string, optional) — Time range preset. Defaults to the current billing period.; `to` (string, optional) — Custom upper bound in RFC3339 format when range=custom

### `usage_timeseries`

- **HTTP:** `GET /usage/me/timeseries`
- **What:** Get current user's usage timeseries. Returns JWT-authenticated request and credit consumption buckets for chart rendering. Results use UTC buckets.
- **Params:** `bucket` (string, optional) — Bucket size. Defaults to hour for day range and day otherwise.; `endpoint` (string, optional) — Optional endpoint filter; `from` (string, optional) — Custom lower bound in RFC3339 format when range=custom; `range` (string, optional) — Time range preset. Defaults to the current billing period.; `to` (string, optional) — Custom upper bound in RFC3339 format when range=custom

## Vinted (7)

### `vinted_brand`

- **HTTP:** `GET /vinted/brand`
- **What:** Vinted listings for a brand. Returns Vinted listings for a specific brand, with optional price filtering and sort order. `order` values: `relevance`, `newest_first`, `price_high_to_low`, `price_low_to_high`. Public data, sourced from Vinted's own server-rendered brand page.
- **Params:** `id` (string, **required**) — Numeric Vinted brand ID, from a /vinted/item result's brand link; `order` (string, optional) — Sort order. Allowed values: relevance, newest_first, price_high_to_low, price_low_to_high; `page` (integer, optional) — Page number, starting at 1; `price_from` (number, optional) — Minimum price; `price_to` (number, optional) — Maximum price

### `vinted_brands`

- **HTTP:** `GET /vinted/brands`
- **What:** Vinted popular-brands directory. Returns Vinted's "Popular brands" directory. This is Vinted's own curated list, not an exhaustive list of every brand in its catalog. Each entry's `id` is usable directly as the `id` query parameter to /vinted/brand. Public data, sourced from Vinted's own server-rendered brands page.
- **Params:** _none_

### `vinted_catalog`

- **HTTP:** `GET /vinted/catalog`
- **What:** Vinted listing search. Returns Vinted resale listings matching a text search, with optional price filtering and sort order. `order` values: `relevance`, `newest_first`, `price_high_to_low`, `price_low_to_high`. Public data, sourced from Vinted's own server-rendered catalog page.
- **Params:** `order` (string, optional) — Sort order. Allowed values: relevance, newest_first, price_high_to_low, price_low_to_high; `page` (integer, optional) — Page number, starting at 1; `price_from` (number, optional) — Minimum price; `price_to` (number, optional) — Maximum price; `search_text` (string, **required**) — Search text

### `vinted_categories`

- **HTTP:** `GET /vinted/categories`
- **What:** Vinted top-level catalog categories. Returns Vinted's top-level catalog categories (e.g. Women, Men, Kids, Home, Electronics, Sports, Entertainment, Hobbies & collectibles). This is the root level only -- Vinted's full category tree goes several levels deeper on the live site, but deeper levels aren't server-rendered so aren't covered here. Each entry's `id` is usable directly as the `id` query parameter to /vinted/category. Public data, sourced from Vinted's own server-rendered catalog navigation.
- **Params:** _none_

### `vinted_category`

- **HTTP:** `GET /vinted/category`
- **What:** Vinted listings for a category. Returns Vinted listings for a specific category, with optional price filtering and sort order. `order` values: `relevance`, `newest_first`, `price_high_to_low`, `price_low_to_high`. Public data, sourced from Vinted's own server-rendered category page.
- **Params:** `id` (string, **required**) — Numeric Vinted category ID, from a /vinted/item result's categories breadcrumb link; `order` (string, optional) — Sort order. Allowed values: relevance, newest_first, price_high_to_low, price_low_to_high; `page` (integer, optional) — Page number, starting at 1; `price_from` (number, optional) — Minimum price; `price_to` (number, optional) — Maximum price

### `vinted_item`

- **HTTP:** `GET /vinted/item`
- **What:** A single Vinted listing's detail. Returns a single Vinted listing's detail: title, description, brand, size, condition, material, color, price, category breadcrumb, and photos. Public data, sourced from Vinted's own server-rendered item page.
- **Params:** `id` (string, **required**) — Numeric Vinted item ID, from a /vinted/catalog result's id field

### `vinted_member`

- **HTTP:** `GET /vinted/member`
- **What:** A Vinted seller's public storefront profile. Returns a Vinted seller's public storefront profile: username, self-disclosed coarse location, rating, and follower/following counts. Deliberately excludes online-presence and activity data (last-seen timestamps, upload-frequency badges) present on the live page. Public data, sourced from Vinted's own server-rendered member page.
- **Params:** `id` (string, **required**) — Numeric Vinted member ID, from a /vinted/item result's seller link

## Walmart (3)

### `walmart_product`

- **HTTP:** `GET /walmart/product/{item_id}`
- **What:** Get a Walmart product. Returns a normalized Walmart product: price, availability, brand, images, rating, seller, description, highlights, specifications, and variants. Credential-free public Walmart data, rendered from the product page through proxied browser renderers.
- **Params:** `item_id` (string, **required**) — Walmart item id (the numeric id in a /ip/{id} URL)

### `walmart_product_reviews`

- **HTTP:** `GET /walmart/product/{item_id}/reviews`
- **What:** Get Walmart product reviews. Returns the reviews snapshot embedded in a Walmart product page: average rating, total review count, the per-star rating breakdown, the recommended percentage, the top positive and top negative review, and a sample of recent reviews. This is a single on-page snapshot, not a full paginated feed. A product that exists but has no reviews returns zero counts and an empty reviews list. Credential-free public Walmart data, rendered from the product page through proxied browser renderers.
- **Params:** `item_id` (string, **required**) — Walmart item id (the numeric id in a /ip/{id} URL)

### `walmart_search`

- **HTTP:** `GET /walmart/search`
- **What:** Search Walmart products. Returns Walmart search results: item id, title, brand, price, image, availability, seller, and rating per product. Credential-free public Walmart data, rendered from the search page through proxied browser renderers.
- **Params:** `page` (integer, optional) — 1-based page number (default 1); `q` (string, **required**) — Search query; `sort` (string, optional) — Sort order

## Web (3)

### `extract`

- **HTTP:** `POST /extract`
- **What:** Extract schema-conforming JSON from a URL. Scrapes a public URL into clean Markdown, then returns data that strictly conforms to the supplied bounded JSON Schema.
- **Params:** `extractOption` (object, **required**) — Extraction options

### `web_scrape`

- **HTTP:** `POST /web/scrape`
- **What:** Scrape a URL into markdown, HTML, links or metadata. Fetches a single public URL and returns clean content in the requested formats (markdown, html, raw_html, links, metadata). With render=auto the request starts as a fast HTTP fetch and escalates to a real browser when the page is blocked or rendered with JavaScript. only_main_content (default true) strips navigation, headers, footers and other boilerplate before conversion. Only public pages are supported; respect each site's terms of use and robots directives.
- **Params:** `scrapeOption` (object, **required**) — Scrape options

### `web_techstack`

- **HTTP:** `POST /web/techstack`
- **What:** Tech stack — detect what a website is built with. Fetches a public URL and fingerprints the web technologies it is built with — a BuiltWith / Wappalyzer-style detector. Returns a list of detected `technologies`, each with its `categories`, a `confidence` (`high`, `medium`, `low`), an optional `version`, and the `evidence` that matched. Covers JavaScript frameworks and libraries (React, Vue.js, Angular, Svelte, jQuery), web frameworks / static site generators (Next.js, Nuxt.js, Gatsby, Remix, SvelteKit, Astro, Hugo), CMS and website builders (WordPress, Drupal, Joomla, Ghost, Wix, Squarespace, Webflow), e-commerce (Shopify, WooCommerce, Magento, BigCommerce), analytics, ad pixels, and tag managers (Google Analytics, Google Tag Manager, Meta Pixel, LinkedIn, Bing, TikTok/Pinterest/Reddit pixels, Segment, Hotjar, Microsoft Clarity), CDNs, UI frameworks and fonts, payments (Stripe, PayPal, Klarna), live chat, marketing automation, A/B testing, consent management, CAPTCHAs (reCAPTCHA, hCaptcha, Turnstile), video, and search. It also inspects response headers (from a plain HTTP fetch) to identify the web server (nginx, Apache, IIS), the CDN / hosting provider (Cloudflare, CloudFront, Fastly, Vercel, Netlify), and the server-side language / framework (PHP, ASP.NET, Ruby on Rails, Django, Laravel, Express). Results are directional, not exhaustive. The `render` fetch strategy is one of `browser` (headless browser that executes JavaScript — the default, so client-injected scripts like analytics, tag managers and pixels are detected), `auto` (Chrome-impersonated HTTP, escalating to a real browser only when blocked or JS-rendered), or `http` (HTTP only, no JavaScript — fastest, but sees only the server HTML); defaults to `browser`. Only public pages are supported; respect each site's terms of use and robots directives.
- **Params:** `request` (object, **required**) — Target URL (and optional render strategy)

## Whatnot (3)

### `whatnot_browse`

- **HTTP:** `GET /whatnot/browse`
- **What:** Browse Whatnot live shows by category. Returns the live and upcoming shows currently listed under a Whatnot category: seller, title, status, start time, thumbnail, and tags. Public data sourced from Whatnot's own GraphQL API.
- **Params:** `category` (string, **required**) — Whatnot category slug. See GET /whatnot/categories for the full list.

### `whatnot_categories`

- **HTTP:** `GET /whatnot/categories`
- **What:** Get Whatnot's category list. Returns Whatnot's full top-level category list (e.g. "Trading Card Games", "Sneakers & Streetwear"). Each entry's slug is usable directly with /whatnot/browse's category filter. Public data sourced from Whatnot's own GraphQL API.
- **Params:** _none_

### `whatnot_live`

- **HTTP:** `GET /whatnot/live/{id}`
- **What:** Get a Whatnot live show's current shop feed. Returns a Whatnot live show's current shop feed: every product, auction, and giveaway listing currently visible in the show, each with its seller's rating. Public data sourced from Whatnot's own GraphQL API.
- **Params:** `id` (string, **required**) — Whatnot live show id, e.g. from a browse result's id field

## X (3)

### `x_post`

- **HTTP:** `GET /x/post/{id}`
- **What:** Retrieve an X post. Returns a public X post by numeric post id, including author, text, visible metrics, and a quoted post preview when present.
- **Params:** `id` (string, **required**) — X post id; `username` (string, optional) — Expected author username. When provided, mismatched authors return 404.

### `x_profile`

- **HTTP:** `GET /x/profile/{username}`
- **What:** Retrieve an X profile. Returns public profile details for an X username, including visible counts and profile media when available.
- **Params:** `username` (string, **required**) — X username

### `x_profile_posts`

- **HTTP:** `GET /x/profile/{username}/posts`
- **What:** List public X profile posts. Returns posts present in the first public profile page payload for an X username. The endpoint does not paginate replies, media-only tabs, or search results.
- **Params:** `limit` (integer, optional) — Maximum posts returned from the first page payload. Defaults to 20 and must be 1-50.; `username` (string, **required**) — X username

## Yahoo Finance (39)

### `yahoo_finance_calendar_results`

- **HTTP:** `GET /yahoo-finance/calendars/{type}`
- **What:** Yahoo Finance calendar results. Returns global Yahoo Finance calendar rows for earnings, IPOs, economic events, or splits.
- **Params:** `end` (string, optional) — End date as YYYY-MM-DD, RFC3339, or Unix seconds; `filter_most_active` (boolean, optional) — Earnings-only most-active filter, default true; `limit` (integer, optional) — Result count, max 100; `market_cap` (number, optional) — Earnings-only market cap minimum; `offset` (integer, optional) — Result offset; `start` (string, optional) — Start date as YYYY-MM-DD, RFC3339, or Unix seconds; `type` (string, **required**) — Calendar type: earnings, ipo, economic-events, or splits

### `yahoo_finance_calendars`

- **HTTP:** `GET /yahoo-finance/calendars`
- **What:** Yahoo Finance calendar types. Lists global Yahoo Finance calendar types supported by this integration.
- **Params:** _none_

### `yahoo_finance_download`

- **HTTP:** `POST /yahoo-finance/download`
- **What:** Yahoo Finance batch historical prices. Returns historical price data for up to 25 symbols.
- **Params:** `request` (object, **required**) — Batch download request

### `yahoo_finance_industries`

- **HTTP:** `GET /yahoo-finance/industries`
- **What:** Yahoo Finance industries. Lists Yahoo Finance industry keys that can be queried with the industry endpoint.
- **Params:** _none_

### `yahoo_finance_industry`

- **HTTP:** `GET /yahoo-finance/industries/{key}`
- **What:** Yahoo Finance industry detail. Returns overview, sector linkage, top companies, growth companies, and research reports for an industry key.
- **Params:** `key` (string, **required**) — Industry key such as semiconductors

### `yahoo_finance_lookup`

- **HTTP:** `GET /yahoo-finance/lookup`
- **What:** Yahoo Finance lookup. Returns Yahoo Finance instrument matches for a query, optionally filtered by instrument type.
- **Params:** `count` (integer, optional) — Result count; `query` (string, **required**) — Ticker symbol or company name; `start` (integer, optional) — Result offset; `type` (string, optional) — Instrument type filter

### `yahoo_finance_market_status`

- **HTTP:** `GET /yahoo-finance/market/{market}/status`
- **What:** Yahoo Finance market status. Returns Yahoo Finance open/close status for a market such as US.
- **Params:** `market` (string, **required**) — Market such as US

### `yahoo_finance_market_summary`

- **HTTP:** `GET /yahoo-finance/market/{market}/summary`
- **What:** Yahoo Finance market summary. Returns Yahoo Finance market summary rows for a market such as US.
- **Params:** `market` (string, **required**) — Market such as US

### `yahoo_finance_screener`

- **HTTP:** `GET /yahoo-finance/screener/{id}`
- **What:** Yahoo Finance predefined screener results. Runs a predefined Yahoo Finance screener such as day_gainers or most_actives.
- **Params:** `count` (integer, optional) — Result count; `id` (string, **required**) — Predefined screener id; `offset` (integer, optional) — Result offset; `sort_asc` (boolean, optional) — Sort ascending; `sort_field` (string, optional) — Sort field for offset/customized runs

### `yahoo_finance_screener_custom`

- **HTTP:** `POST /yahoo-finance/screener`
- **What:** Yahoo Finance custom screener. Runs a constrained Yahoo Finance custom screener query using Yahoo's public screener JSON shape.
- **Params:** `request` (object, **required**) — Custom screener request

### `yahoo_finance_screeners`

- **HTTP:** `GET /yahoo-finance/screeners`
- **What:** Yahoo Finance predefined screeners. Lists the predefined screeners supported by the Yahoo Finance integration.
- **Params:** _none_

### `yahoo_finance_search`

- **HTTP:** `GET /yahoo-finance/search`
- **What:** Yahoo Finance search. Returns normalized Yahoo Finance quotes, news, lists, and optional research reports for a query.
- **Params:** `enable_fuzzy_query` (boolean, optional) — Enable fuzzy matching; `include_research` (boolean, optional) — Include research reports when Yahoo returns them; `lists_count` (integer, optional) — List result count; `news_count` (integer, optional) — News result count; `q` (string, **required**) — Ticker symbol or company name; `quotes_count` (integer, optional) — Quote result count

### `yahoo_finance_sector`

- **HTTP:** `GET /yahoo-finance/sectors/{key}`
- **What:** Yahoo Finance sector detail. Returns overview, top companies, ETFs, mutual funds, industries, and research reports for a sector key.
- **Params:** `key` (string, **required**) — Sector key such as technology

### `yahoo_finance_sectors`

- **HTTP:** `GET /yahoo-finance/sectors`
- **What:** Yahoo Finance sectors. Lists Yahoo Finance sector keys that can be queried with the sector endpoint.
- **Params:** _none_

### `yahoo_finance_ticker_actions`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/actions`
- **What:** Yahoo Finance corporate actions. Returns dividends, splits, and capital gains for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_analysts`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/analysts`
- **What:** Yahoo Finance analyst data. Returns recommendations, upgrades/downgrades, price targets, and estimate modules where Yahoo provides them.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_calendar`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/calendar`
- **What:** Yahoo Finance calendar. Returns Yahoo Finance calendar events for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_capital_gains`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/capital-gains`
- **What:** Yahoo Finance capital gains. Returns capital gain events for ETF or mutual fund symbols when Yahoo provides them.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as SPY

### `yahoo_finance_ticker_dividends`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/dividends`
- **What:** Yahoo Finance dividends. Returns dividend events for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_earnings`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/earnings`
- **What:** Yahoo Finance earnings. Returns Yahoo Finance earnings modules for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_earnings_dates`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/earnings-dates`
- **What:** Yahoo Finance earnings dates. Returns standalone earnings-date rows from Yahoo Finance calendar HTML when Yahoo serves the table.
- **Params:** `limit` (integer, optional) — Result count, max 100; `offset` (integer, optional) — Result offset; `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_financials`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/financials`
- **What:** Yahoo Finance financial statements. Returns annual, quarterly, or supported trailing income, balance sheet, or cash flow statement data.
- **Params:** `period` (string, optional) — annual, quarterly, or trailing; `statement` (string, optional) — Statement type. Allowed values: income (alias income-statement), balance-sheet (alias balance), cash-flow (alias cashflow); `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_funds`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/funds`
- **What:** Yahoo Finance fund data. Returns fund profile, top holdings, equity/bond holdings, and sector weighting modules for ETF and mutual fund symbols.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as SPY

### `yahoo_finance_ticker_history`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/history`
- **What:** Yahoo Finance historical prices. Returns normalized OHLCV points for a symbol. Use either period or start/end.
- **Params:** `auto_adjust` (boolean, optional) — Adjust OHLC prices with adjusted close; `back_adjust` (boolean, optional) — Back-adjust OHLC prices while keeping close; `end` (string, optional) — Unix seconds, RFC3339, or YYYY-MM-DD; `include_actions` (boolean, optional) — Include dividends, splits, and capital gains; `include_prepost` (boolean, optional) — Include pre/post market data; `interval` (string, optional) — Interval such as 1d, 1h, 5m; `keepna` (boolean, optional) — Keep fully empty chart rows; `period` (string, optional) — Range such as 1d, 1mo, 1y, max; `rounding` (boolean, optional) — Round prices to two decimals; `start` (string, optional) — Unix seconds, RFC3339, or YYYY-MM-DD; `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_history_metadata`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/history-metadata`
- **What:** Yahoo Finance history metadata. Returns Yahoo Finance chart metadata for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_holders`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/holders`
- **What:** Yahoo Finance holders. Returns major, institutional, fund, and insider holder modules for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_info`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/info`
- **What:** Yahoo Finance ticker info. Returns normalized profile, quote type, price, statistics, and summary modules for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_isin`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/isin`
- **What:** Yahoo Finance ticker ISIN. Returns the experimental yfinance-compatible ISIN lookup result for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_news`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/news`
- **What:** Yahoo Finance ticker news. Returns Yahoo Finance news search results for a symbol.
- **Params:** `count` (integer, optional) — News result count; `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL; `tab` (string, optional) — News tab: news, all, or press_releases

### `yahoo_finance_ticker_options`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/options`
- **What:** Yahoo Finance options chain. Returns option expiration dates and the current option chain for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_options_expiration`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/options/{expiration}`
- **What:** Yahoo Finance options chain by expiration. Returns calls and puts for a specific Unix expiration timestamp.
- **Params:** `expiration` (string, **required**) — Unix expiration timestamp; `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_quote`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/quote`
- **What:** Yahoo Finance ticker quote. Returns normalized fast quote fields for one Yahoo Finance symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_sec_filings`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/sec-filings`
- **What:** Yahoo Finance SEC filings. Returns Yahoo Finance SEC filing summaries for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_shares`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/shares`
- **What:** Yahoo Finance share counts. Returns current share-count fields from Yahoo key statistics.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_shares_full`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/shares-full`
- **What:** Yahoo Finance historical share counts. Returns historical shares-out rows from Yahoo fundamentals timeseries.
- **Params:** `end` (string, optional) — End date as YYYY-MM-DD, RFC3339, or Unix seconds; `start` (string, optional) — Start date as YYYY-MM-DD, RFC3339, or Unix seconds; `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_splits`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/splits`
- **What:** Yahoo Finance splits. Returns split events for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_sustainability`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/sustainability`
- **What:** Yahoo Finance sustainability. Returns ESG and sustainability modules for a symbol.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_ticker_valuation`

- **HTTP:** `GET /yahoo-finance/ticker/{symbol}/valuation`
- **What:** Yahoo Finance valuation measures. Returns the valuation table from the Yahoo Finance key statistics page when Yahoo serves the table.
- **Params:** `symbol` (string, **required**) — Yahoo Finance symbol such as AAPL

### `yahoo_finance_trending`

- **HTTP:** `GET /yahoo-finance/trending/{region}`
- **What:** Yahoo Finance trending symbols. Returns trending Yahoo Finance symbols for a region.
- **Params:** `count` (integer, optional) — Symbol count; `region` (string, **required**) — Region such as US

## Yahoo Search (1)

### `yahoo_search`

- **HTTP:** `GET /yahoo-search/search`
- **What:** Search Yahoo web results. Returns normalized Yahoo web search results for a query string: title, destination URL, description, and hostname, plus page-based pagination. Yahoo wraps every result link in its own click-tracking redirect; this endpoint always returns the decoded destination URL, never the raw redirect link. Results are fetched from Yahoo's own server-rendered search page.
- **Params:** `page` (integer, optional) — 1-based page number, defaults to 1; `q` (string, **required**) — Search query

## Yelp (8)

### `yelp_business`

- **HTTP:** `GET /yelp/business/{id}`
- **What:** Get Yelp business detail. Looks up a single Yelp business by alias or encoded id via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id

### `yelp_business_menu`

- **HTTP:** `GET /yelp/business/{id}/menu`
- **What:** Get Yelp business menu. Fetches menu items for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id

### `yelp_business_photos`

- **HTTP:** `GET /yelp/business/{id}/photos`
- **What:** Get Yelp business photos. Fetches the photo gallery for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id; `limit` (integer, optional) — Max photos to return, 1-50; `offset` (integer, optional) — Pagination offset

### `yelp_business_review_highlights`

- **HTTP:** `GET /yelp/business/{id}/reviews/highlights`
- **What:** Get Yelp business review highlights. Fetches thematic review snippets (extracted talking points with a supporting quote) for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id

### `yelp_business_reviews`

- **HTTP:** `GET /yelp/business/{id}/reviews`
- **What:** Get Yelp business reviews. Fetches reviews for a Yelp business via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id; `limit` (integer, optional) — Max reviews to return, 1-50; `offset` (integer, optional) — Pagination offset

### `yelp_business_reviews_search`

- **HTTP:** `GET /yelp/business/{id}/reviews/search`
- **What:** Search Yelp business reviews by keyword. Searches a Yelp business's reviews for a keyword via Yelp's real Android app backend, returning a highlighted excerpt per match. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `id` (string, **required**) — Yelp business alias or encoded id; `term` (string, **required**) — Keyword to search reviews for

### `yelp_geocode`

- **HTTP:** `GET /yelp/geocode`
- **What:** Geocode a free-form address. Resolves a free-form address into structured location data (coordinates, city, state, zip, county) via Yelp's real Android app backend. Credential-free: no login, no API key, no cookie required from the caller. Not business-scoped.
- **Params:** `address` (string, **required**) — Free-form address to geocode

### `yelp_search`

- **HTTP:** `GET /yelp/search`
- **What:** Search Yelp businesses. Searches Yelp's real Android app business-search backend for a term and location. Credential-free: no login, no API key, no cookie required from the caller.
- **Params:** `limit` (integer, optional) — Max results to return, 1-50; `location` (string, **required**) — Neighborhood, city, state, or zip code; `offset` (integer, optional) — Pagination offset; `term` (string, **required**) — Search term

## YouTube (13)

### `youtube_captions`

- **HTTP:** `GET /youtube/captions/{id}`
- **What:** Retrieve auto-generated or human captions. Returns the caption cues for a specific YouTube video.
- **Params:** `id` (string, **required**) — YouTube video ID (11-character code); `lang` (string, optional) — Caption language code (ISO 639-1), defaults to **en**

### `youtube_channel_playlists`

- **HTTP:** `GET /youtube/channel/{id}/playlists`
- **What:** Retrieve the playlists tab for a YouTube channel. Returns normalized playlist items from a channel's Playlists tab and an optional continuation token.
- **Params:** `continuation_token` (string, optional) — Pagination token returned by a previous request; `id` (string, **required**) — Channel ID, @handle, /c path, /user path, or full YouTube channel URL

### `youtube_channel_search`

- **HTTP:** `GET /youtube/channel/{id}/search`
- **What:** Search within a YouTube channel. Returns normalized video search items scoped to a specific channel, including the resolved top-level `query`.
- **Params:** `continuation_token` (string, optional) — Pagination token returned by a previous request; `id` (string, **required**) — Channel ID, @handle, /c path, /user path, or full YouTube channel URL; `q` (string, **required**) — Search query

### `youtube_channel_shorts`

- **HTTP:** `GET /youtube/channel/{id}/shorts`
- **What:** Retrieve the shorts tab for a YouTube channel. Returns normalized short-form video entries from a channel's Shorts tab.
- **Params:** `id` (string, **required**) — Channel ID, @handle, /c path, /user path, or full YouTube channel URL

### `youtube_channel_videos`

- **HTTP:** `GET /youtube/channel/{id}/videos`
- **What:** Retrieve the videos tab for a YouTube channel. Returns normalized video items from a channel's Videos tab and an optional continuation token.
- **Params:** `continuation_token` (string, optional) — Pagination token returned by a previous request; `id` (string, **required**) — Channel ID, @handle, /c path, /user path, or full YouTube channel URL

### `youtube_comments`

- **HTTP:** `GET /youtube/comments/{id}`
- **What:** Retrieve video comments (top-level & replies). Returns a page of comments for a specific YouTube video.
- **Params:** `continuation_token` (string, optional) — Pagination token returned by a previous request, first page if empty; `id` (string, **required**) — YouTube video ID (11-character code)

### `youtube_playlist`

- **HTTP:** `GET /youtube/playlist/{id}`
- **What:** Retrieve playlist metadata and items. Returns playlist metadata, normalized video items, and an optional continuation token for pagination.
- **Params:** `continuation_token` (string, optional) — Pagination token returned by a previous request; `id` (string, **required**) — YouTube playlist ID or full playlist URL

### `youtube_profile`

- **HTTP:** `GET /youtube/profile/{id}`
- **What:** Retrieve channel profile. Returns full profile details for a YouTube channel.
- **Params:** `id` (string, **required**) — Channel ID, @handle, /c path, /user path, bare username, or full YouTube channel URL

### `youtube_search`

- **HTTP:** `GET /youtube/search`
- **What:** Search YouTube. Returns normalized YouTube search results using YouTube's InnerTube search API. Pass `continuation_token` from a previous response to retrieve the next page. Use `q` as the primary query parameter; `search_query` is accepted as an alias.
- **Params:** `continuation_token` (string, optional) — Pagination token returned by a previous request; `duration` (string, optional) — Filter by duration; `features` (string, optional) — Comma-separated feature filters; `params` (string, optional) — Raw protobuf-encoded search filter (base64); `q` (string, optional) — Search query; `search_query` (string, optional) — Alias for q; `sort_by` (string, optional) — Sort results; `type` (string, optional) — Filter by type; `upload_date` (string, optional) — Filter by upload date

### `youtube_tag`

- **HTTP:** `GET /youtube/tag/{tag}`
- **What:** Retrieve YouTube videos by tag. Returns normalized videos from the public YouTube hashtag page for the supplied tag. Set `type=shorts` to use the Shorts tab, or pass `continuation_token` from a previous response to fetch the next page.
- **Params:** `continuation_token` (string, optional) — Continuation token for pagination, first page if empty; `tag` (string, **required**) — Tag to filter videos; `type` (string, optional) — Result tab to load

### `youtube_transcript`

- **HTTP:** `GET /youtube/transcript/{id}`
- **What:** Retrieve transcript for a YouTube video. Returns transcript segments for a YouTube video using YouTube's native player captions. Set `format=text`, `format=srt`, or `format=vtt` to receive plain-text output instead of the standard response envelope.
- **Params:** `format` (string, optional) — Response format; `id` (string, **required**) — YouTube video ID (11-character code); `lang` (string, optional) — Preferred transcript language; `timestamps` (boolean, optional) — Include timestamps in the JSON response; `translate_to` (string, optional) — Translate transcript to this language code

### `youtube_transcript_languages`

- **HTTP:** `GET /youtube/transcript/{id}/languages`
- **What:** List transcript languages for a YouTube video. Returns the transcript languages exposed by YouTube for a specific video.
- **Params:** `id` (string, **required**) — YouTube video ID (11-character code)

### `youtube_video`

- **HTTP:** `GET /youtube/video/{id}`
- **What:** Retrieve video metadata & captions. Returns title, description, stats, and captions for a YouTube video ID.
- **Params:** `id` (string, **required**) — YouTube video ID (11-char code)

## Zalando (5)

### `zalando_category`

- **HTTP:** `GET /zalando/category`
- **What:** Browse a Zalando category or brand. Browses a Zalando category or brand listing by URL slug (e.g. shoes, womens-dresses, on-running) and returns the same normalized result cards as zalando-search, plus the category's upstream total_count. Category slugs are market-specific (each storefront uses its own local-language slug, e.g. "shoes" on de/gb, "chaussures" on fr, "scarpe" on it) — take them from that market's own site navigation or a product's url field. market is required (there is no default storefront) and accepts 25 country storefronts — see zalando-markets for the full current list with domains.
- **Params:** `category` (string, **required**) — Zalando category or brand URL slug, in the target market's own language; `market` (string, **required**) — Zalando country storefront

### `zalando_markets`

- **HTTP:** `GET /zalando/markets`
- **What:** List supported Zalando country storefronts. Returns the Zalando country storefronts currently supported by the required market parameter on zalando-search, zalando-category, and zalando-product, with each market's domain. Static, credential-free metadata with no upstream request.
- **Params:** _none_

### `zalando_product`

- **HTTP:** `GET /zalando/product`
- **What:** Get a Zalando product. Returns normalized product details for one Zalando product, including brand, description, images, and per-size price/availability/GTIN. Pass the sku returned by zalando-search or zalando-category; Zalando's own site search resolves the sku to its canonical product page. market is required and must match the storefront the sku was found in (there is no default, and a sku is generally only listed for sale on the market(s) that carry it) — see zalando-markets for the full reference list.
- **Params:** `market` (string, **required**) — Zalando country storefront the sku was found in; `sku` (string, **required**) — Zalando product SKU (article number) from zalando-search or zalando-category

### `zalando_search`

- **HTTP:** `GET /zalando/search`
- **What:** Search Zalando products. Searches a Zalando country storefront by keyword and returns normalized result cards with price, brand, and image. Returns the first page of results as rendered by Zalando plus the upstream total_count; deeper pagination is not yet supported. market is required (there is no default storefront) and accepts 25 country storefronts — see zalando-markets for the full current list with domains.
- **Params:** `market` (string, **required**) — Zalando country storefront; `q` (string, **required**) — Product search keyword

### `zalando_suggest`

- **HTTP:** `GET /zalando/suggest`
- **What:** Autocomplete a Zalando search query. Returns Zalando's own search-box query completions for a partial keyword, e.g. "running sho" -> "running shoes", "running shoes nike". market is required (there is no default storefront) and accepts 25 country storefronts — see zalando-markets for the full current list with domains.
- **Params:** `market` (string, **required**) — Zalando country storefront; `q` (string, **required**) — Partial search text to complete

## Zillow (3)

### `zillow_autocomplete`

- **HTTP:** `GET /zillow/autocomplete`
- **What:** Autocomplete Zillow locations. Returns normalized Zillow public web autocomplete candidates. Semantic candidates may include region_id/region_type compatibility aliases plus region_ids/region_types arrays; prefer complete bounds metadata for Zillow search when present.
- **Params:** `limit` (integer, optional) — Maximum results, clamped to 20; `query` (string, **required**) — Location query; `status` (string, optional) — Search context. Allowed values: for_sale (aliases sale, for-sale), for_rent (aliases rent, for-rent), sold

### `zillow_property`

- **HTTP:** `GET /zillow/property/{zpid}`
- **What:** Get Zillow property. Returns normalized Zillow public property details using Zillow's public persisted GraphQL property payload, including optional typed sections for address parts, listing attribution, pricing, history, media, facts, schools, and nearby homes when present.
- **Params:** `zpid` (string, **required**) — Zillow property id

### `zillow_search`

- **HTTP:** `GET /zillow/search`
- **What:** Search Zillow listings. Returns normalized Zillow public listing search results. Callers must pass complete map bounds from autocomplete when available, or a region id fallback.
- **Params:** `east` (number, optional) — Map east bound from autocomplete; `location` (string, **required**) — Display location; `north` (number, optional) — Map north bound from autocomplete; `page` (integer, optional) — 1-based page; `region_id` (integer, optional) — Zillow region id from autocomplete, used when complete bounds are not provided; `region_type` (integer, optional) — Zillow region type from autocomplete, used with region_id fallback; `south` (number, optional) — Map south bound from autocomplete; `status` (string, optional) — Search context. Allowed values: for_sale (aliases sale, for-sale), for_rent (aliases rent, for-rent), sold; `west` (number, optional) — Map west bound from autocomplete
