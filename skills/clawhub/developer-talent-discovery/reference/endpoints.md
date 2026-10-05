# developer-talent-discovery — endpoint reference

> Generated from `scripts/tools.json` by `scripts/generate.mjs` — do not edit by hand.

Only the endpoints used by this workflow. Call them via `scripts/crawlora.sh` (see SKILL.md).

All paths are relative to the API base `https://api.crawlora.net/api/v1` and require the header `x-api-key: $CRAWLORA_API_KEY`. Path params like `{id}` are substituted into the URL; `GET` params go in the query string; `POST` params go in a JSON body.

**12 endpoints across 2 platform group(s).**

## Datasets (3)

### `datasets_github_users_facets`

- **HTTP:** `GET /datasets/github-users/facets`
- **What:** Facet the GitHub users dataset. Returns terms aggregation counts for the GitHub users dataset. Facet enum: `influence_tier`, `type`, `country`, `country_code`, `state`, `city`, `domains`, `company`, `reachable`, `has_email`, `has_twitter`, `has_blog`, `active_90d`, `hireable`, `is_org`, `is_bot`, `is_suspected_automation`. influence_tier enum: `nano`, `micro`, `mid`, `macro`, `mega`. Suspected-automation records are excluded by default unless is_suspected_automation is set.
- **Params:** `active_90d` (boolean, optional) — Filter by activity within the last 90 days; `city` (string, optional) — Exact geocoded city filter, max 128 characters; `company` (string, optional) — Exact normalized-company filter, max 128 characters; `country` (string, optional) — Exact geocoded country filter, max 128 characters; `country_code` (string, optional) — Exact ISO country-code filter, max 128 characters; `domain` (string, optional) — Interest-domain tag filter, max 128 characters; `facet` (string, **required**) — Facet enum: influence_tier, type, country, country_code, state, city, domains, company, reachable, has_email, has_twitter, has_blog, active_90d, hireable, is_org, is_bot, is_suspected_automation; `has_blog` (boolean, optional) — Filter by public blog/website presence; `has_email` (boolean, optional) — Filter by public email presence; `has_twitter` (boolean, optional) — Filter by public Twitter/X handle presence; `hireable` (boolean, optional) — Filter by the GitHub available-for-hire flag; `influence_tier` (string, optional) — Follower-tier enum: nano, micro, mid, macro, mega; `is_bot` (boolean, optional) — Bot filter; `is_org` (boolean, optional) — Organization filter; `is_suspected_automation` (boolean, optional) — Suspected automation filter; omitted these are hidden by default; `lat` (number, optional) — Latitude for radius filtering; `login` (string, optional) — Exact login filter, max 128 characters; `lon` (number, optional) — Longitude for radius filtering; `max_account_age_years` (number, optional) — Maximum account age in years; `max_followers` (integer, optional) — Maximum follower count; `min_account_age_years` (number, optional) — Minimum account age in years; `min_followers` (integer, optional) — Minimum follower count; `min_rank_score` (integer, optional) — Minimum composite rank score; `min_repos` (integer, optional) — Minimum public repository count; `q` (string, optional) — Full-text query over login, name, company, bio and location, max 256 characters; `radius_m` (integer, optional) — Radius in meters, 1 through 50000; requires lat and lon when supplied; `reachable` (boolean, optional) — Filter by any public contact channel; `sort` (string, optional) — Sort enum: relevance, rank_score_desc, followers_desc, account_age_desc, account_age_asc, distance_asc; `state` (string, optional) — Exact geocoded state filter, max 128 characters

### `datasets_github_users_item`

- **HTTP:** `GET /datasets/github-users/items/{login}`
- **What:** Get a GitHub user from the dataset. Returns one enriched GitHub user record by login from dataset id enum value `github-users`.
- **Params:** `login` (string, **required**) — GitHub login, max 128 characters

### `datasets_github_users_search`

- **HTTP:** `GET /datasets/github-users/search`
- **What:** Search the GitHub users dataset. Searches enriched public GitHub user profiles stored in a search index. influence_tier enum: `nano`, `micro`, `mid`, `macro`, `mega`. Sort enum: `relevance`, `rank_score_desc`, `followers_desc`, `account_age_desc`, `account_age_asc`, `distance_asc`.
- **Params:** `active_90d` (boolean, optional) — Filter by activity within the last 90 days; `city` (string, optional) — Exact geocoded city filter, max 128 characters; `company` (string, optional) — Exact normalized-company filter, max 128 characters; `country` (string, optional) — Exact geocoded country filter, max 128 characters; `country_code` (string, optional) — Exact ISO country-code filter, max 128 characters; `domain` (string, optional) — Interest-domain tag filter (e.g. ml-ai, web, devops), max 128 characters; `has_blog` (boolean, optional) — Filter by public blog/website presence; `has_email` (boolean, optional) — Filter by public email presence; `has_twitter` (boolean, optional) — Filter by public Twitter/X handle presence; `hireable` (boolean, optional) — Filter by the GitHub available-for-hire flag; `influence_tier` (string, optional) — Follower-tier enum: nano, micro, mid, macro, mega; `is_bot` (boolean, optional) — Bot filter (normally false; the crawl skips bots); `is_org` (boolean, optional) — Organization filter (normally false; the crawl indexes individuals); `is_suspected_automation` (boolean, optional) — Suspected automation (commit-farm/mass-repo bots); omitted these are hidden by default, pass true to isolate them; `lat` (number, optional) — Latitude for radius filtering or distance sort; `login` (string, optional) — Exact login filter, max 128 characters; `lon` (number, optional) — Longitude for radius filtering or distance sort; `max_account_age_years` (number, optional) — Maximum account age in years; `max_followers` (integer, optional) — Maximum follower count; `min_account_age_years` (number, optional) — Minimum account age in years; `min_followers` (integer, optional) — Minimum follower count; `min_rank_score` (integer, optional) — Minimum composite rank score; `min_repos` (integer, optional) — Minimum public repository count; `page` (integer, optional) — Page number, defaults to 1; `page_size` (integer, optional) — Page size, defaults to 20 and maxes at 100; page * page_size must be <= 10000; `q` (string, optional) — Full-text query over login, name, company, bio and location, max 256 characters; `radius_m` (integer, optional) — Radius in meters, 1 through 50000; requires lat and lon when supplied; `reachable` (boolean, optional) — Filter by any public contact channel; `sort` (string, optional) — Sort enum: relevance, rank_score_desc, followers_desc, account_age_desc, account_age_asc, distance_asc; `state` (string, optional) — Exact geocoded state filter, max 128 characters

## GitHub (9)

### `github_repo`

- **HTTP:** `GET /github/repo/{owner}/{repo}`
- **What:** Retrieve a GitHub repository. Returns public detail for a single repository (the core project object).
- **Params:** `owner` (string, **required**) — Repository owner (user or org login); `repo` (string, **required**) — Repository name

### `github_repo_contributors`

- **HTTP:** `GET /github/repo/{owner}/{repo}/contributors`
- **What:** List a repository's contributors. Returns a page of a repository's contributors (who builds a project).
- **Params:** `owner` (string, **required**) — Repository owner (user or org login); `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `repo` (string, **required**) — Repository name

### `github_repo_languages`

- **HTTP:** `GET /github/repo/{owner}/{repo}/languages`
- **What:** Retrieve a repository's language breakdown. Returns the language byte breakdown for a repository, sorted by bytes descending (tech fingerprint).
- **Params:** `owner` (string, **required**) — Repository owner (user or org login); `repo` (string, **required**) — Repository name

### `github_search_repositories`

- **HTTP:** `GET /github/search/repositories`
- **What:** Search public GitHub repositories. Searches public GitHub repositories (market/competitive discovery). Unauthenticated search is rate limited to roughly 10 requests per minute.
- **Params:** `order` (string, optional) — Sort order; `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `q` (string, **required**) — GitHub repository search query; `sort` (string, optional) — Sort field

### `github_search_users`

- **HTTP:** `GET /github/search/users`
- **What:** Search public GitHub users. Searches public GitHub users (developer discovery). Unauthenticated search is rate limited to roughly 10 requests per minute.
- **Params:** `order` (string, optional) — Sort order; `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `q` (string, **required**) — GitHub user search query; `sort` (string, optional) — Sort field

### `github_user`

- **HTTP:** `GET /github/user/{username}`
- **What:** Retrieve a GitHub user profile. Returns a public GitHub user's profile plus user-published social links. Email is included only when the user has made it public on their profile.
- **Params:** `username` (string, **required**) — GitHub username

### `github_user_events`

- **HTTP:** `GET /github/user/{username}/events`
- **What:** List a GitHub user's recent public activity. Returns a page of a user's recent public events, normalized to type, repository, and timestamp (freshness signal).
- **Params:** `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `username` (string, **required**) — GitHub username

### `github_user_pinned`

- **HTTP:** `GET /github/user/{username}/pinned`
- **What:** List a GitHub user's pinned repositories. Returns the repositories a user pinned on their public profile (showcase signal). Empty when the user pinned nothing.
- **Params:** `username` (string, **required**) — GitHub username

### `github_user_repos`

- **HTTP:** `GET /github/user/{username}/repos`
- **What:** List a GitHub user's public repositories. Returns a page of a user's public repositories (tech-stack signal).
- **Params:** `direction` (string, optional) — Sort direction; `page` (integer, optional) — Page number; `per_page` (integer, optional) — Results per page (max 100); `sort` (string, optional) — Sort field; `type` (string, optional) — Repository type; `username` (string, **required**) — GitHub username
