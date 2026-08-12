# developer-oss-research — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Endpoints this skill uses, grouped by platform. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**29 endpoints across 2 platform group(s).**

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
