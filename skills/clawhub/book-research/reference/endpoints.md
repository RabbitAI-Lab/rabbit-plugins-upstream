# book-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**32 endpoints across 3 platform group(s).**

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
- **What:** Get a Goodreads Listopia list. Returns a Goodreads Listopia list (ranked book list) by id, paginated. Credential-free public Goodreads data; page 1 of well-known lists may be served from a faster live source, with the public list page itself as fallback for every other case.
- **Params:** `id` (string, **required**) — Goodreads list id; `page` (integer, optional) — 1-based page number, default 1

### `goodreads_lists`

- **HTTP:** `GET /goodreads/lists`
- **What:** List curated Goodreads Listopia lists. Returns a catalog of well-known Goodreads Listopia lists (id, name, category). Goodreads has no directory or search endpoint for the tens of thousands of user-created lists, so this is served from a live popular-lists source when available, falling back to a curated, hand-picked catalog otherwise. Pass a returned id to GET /goodreads/list/{id} for that list's ranked book contents. Category enum: `general`, `genre`, `era`, `young_adult`, `children`, `holiday`.
- **Params:** _none_

### `goodreads_search`

- **HTTP:** `GET /goodreads/search`
- **What:** Search Goodreads books. Searches Goodreads books by title/author. Credential-free public Goodreads data via the autocomplete endpoint (book results only).
- **Params:** `limit` (integer, optional) — Max results, default 10, max 50; `q` (string, **required**) — Search query

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

## Audible (10)

### `audible_categories`

- **HTTP:** `GET /audible/categories`
- **What:** Get Audible's genre/category tree. Returns Audible's full genre/category tree (root genres with their subgenres), including the category ids accepted by GET /audible/search's category_id filter. Credential-free public catalog data from api.audible.com.
- **Params:** _none_

### `audible_category`

- **HTTP:** `GET /audible/category/{id}`
- **What:** Get one Audible category node. Returns one Audible category node and its immediate children by id — cheaper than fetching the full tree from GET /audible/categories when only one node is needed. Credential-free public catalog data from api.audible.com.
- **Params:** `id` (string, **required**) — Audible category id from GET /audible/categories

### `audible_charts`

- **HTTP:** `GET /audible/charts`
- **What:** Get an Audible chart (audible.com/charts). Returns one page of an Audible chart — a ranked list with real chart position, price, and rating that has no equivalent on api.audible.com's public JSON API. This is an HTML scrape of audible.com/charts, a different, less stable source class than the rest of this family, though its own filters (category, access level, language, duration, Audible-Originals-only) were individually verified to actually change results. category_id, access_level, and content_type=podcasts are mutually exclusive.
- **Params:** `access_level` (string, optional) — Membership access level, default all; `category_id` (string, optional) — Restrict to a category id from GET /audible/categories; `chart` (string, optional) — Chart type, default most_listened; `content_type` (string, optional) — Content type, default audiobooks; `duration` (string, optional) — Runtime-length filter, default all; `language` (string, optional) — Language filter, default all; `originals_only` (boolean, optional) — Restrict to Audible Originals only; `page` (integer, optional) — 1-based result page, default 1, 20 results per page

### `audible_editorial_list`

- **HTTP:** `GET /audible/list/{list}`
- **What:** Get an Audible curated editorial list. Returns one of Audible's hand-curated "Popular Lists" pages, normalized into its themed shelves (heading + ordered ASINs). This is an HTML scrape of a marketing/editorial page (audible.com), not api.audible.com's JSON API — pair an ASIN from any shelf with GET /audible/products (batch) or GET /audible/product/{asin} for full title/author/price/rating detail. "Best of the Year" is not covered — its layout has no consistent structure to parse.
- **Params:** `list` (string, **required**) — Editorial list slug

### `audible_product`

- **HTTP:** `GET /audible/product/{asin}`
- **What:** Get an Audible audiobook. Returns a normalized Audible audiobook: description, authors, narrators, series, category ladders, publisher, release date, runtime, language, sample audio URL, rating (overall/performance/story), and public list price. Credential-free public catalog data from api.audible.com.
- **Params:** `asin` (string, **required**) — Audible ASIN

### `audible_product_related`

- **HTTP:** `GET /audible/product/{asin}/related`
- **What:** Get Audible titles related to an audiobook. Returns Audible titles related to a given ASIN by a required relation type: same series, same narrator, same author, next in series, or raw upstream similarity. Credential-free public catalog data from api.audible.com.
- **Params:** `asin` (string, **required**) — Audible ASIN; `limit` (integer, optional) — Max results, default 10, max 50; `similarity_type` (string, **required**) — How to relate titles to the given ASIN

### `audible_product_reviews`

- **HTTP:** `GET /audible/product/{asin}/reviews`
- **What:** Get an Audible audiobook's customer reviews. Returns a page of an Audible audiobook's customer reviews (author, title, body, overall/performance/story ratings, helpful votes, submission date). Credential-free public catalog data from api.audible.com.
- **Params:** `asin` (string, **required**) — Audible ASIN; `limit` (integer, optional) — Max reviews, default 10, max 50; `page` (integer, optional) — Zero-based result page, default 0

### `audible_products`

- **HTTP:** `GET /audible/products`
- **What:** Get multiple Audible audiobooks in one call. Returns normalized Audible audiobooks for up to 50 ASINs in a single request — the same fields as GET /audible/product/{asin}. Unrecognized ASINs are silently omitted rather than failing the whole batch. Credential-free public catalog data from api.audible.com.
- **Params:** `asins` (string, **required**) — Comma-separated Audible ASINs, up to 50

### `audible_search`

- **HTTP:** `GET /audible/search`
- **What:** Search Audible's catalog. Searches Audible's audiobook catalog by keyword, title, author, narrator, or category id. At least one filter is required. Credential-free public catalog data from api.audible.com.
- **Params:** `author` (string, optional) — Match by author name; `category_id` (string, optional) — Restrict to a category id from GET /audible/categories; `limit` (integer, optional) — Max results, default 10, max 50; `narrator` (string, optional) — Match by narrator name; `page` (integer, optional) — Zero-based result page, default 0; `q` (string, optional) — Free-text query matched across title, subtitle, and author; `title` (string, optional) — Match by title

### `audible_series`

- **HTTP:** `GET /audible/series/{asin}`
- **What:** Get an Audible series' ordered book list. Returns an Audible series and every book in it, in series order. A series has its own ASIN distinct from any book in it — find one via a book's series[].asin field from GET /audible/product/{asin}. Credential-free public catalog data from api.audible.com.
- **Params:** `asin` (string, **required**) — Audible series ASIN, from a product's series[].asin field
