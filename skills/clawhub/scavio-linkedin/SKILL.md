---
name: scavio-linkedin
description: Pull LinkedIn person and company profiles, posts, contact info, company people and jobs, and search people, jobs, and posts as structured JSON. 14 endpoints for prospecting, recruiting, and market research.
version: 1.0.0
tags: linkedin, b2b, people-search, company-data, jobs, profiles, posts, prospecting, recruiting, lead-generation, agents, langchain, crewai, autogen, structured-data, json, ai-agents, research
metadata:
  openclaw:
    requires:
      env:
        - SCAVIO_API_KEY
    primaryEnv: SCAVIO_API_KEY
    timeout: 120
    throttle: 1
    emoji: "\U0001F4BC"
    homepage: https://scavio.dev/docs/linkedin-api
---

# LinkedIn via Scavio

Look up LinkedIn people and companies, read their posts, pull public contact info, list a company's people and open jobs, get job and post details with comments, and search across people, jobs, and posts. All endpoints return structured JSON.

## When to trigger

Use this skill when the user asks to:
- Look up a LinkedIn member's profile, about section, posts, or contact info
- Look up a company profile, its posts, its people, or its open jobs
- Search for people by name, title, company, or school
- Search for jobs or posts by keyword
- Read a single job listing or a single post with its comments
- Build B2B prospecting, recruiting, or market-research pipelines

Note: LinkedIn upstream can be slow and occasionally flaky. Set a client timeout of at least 60 seconds and be ready to retry.

## Setup

Get a free API key at https://scavio.dev (50 free credits to get started, no card required):

```bash
export SCAVIO_API_KEY=sk_live_your_key
```

Every request is a `POST` with a JSON body and:

```
Authorization: Bearer $SCAVIO_API_KEY
```

## Endpoints

Base URL: `https://api.scavio.dev`. All paths are under `/api/v1/linkedin`. Most endpoints cost **4 credits**; the two company endpoints (`/company` and `/company/posts`) cost **1 credit**.

| Endpoint | Credits | Description |
|---|---|---|
| `POST /api/v1/linkedin/person` | 4 | Full profile for a member |
| `POST /api/v1/linkedin/person/about` | 4 | About/overview metadata for a member |
| `POST /api/v1/linkedin/person/posts` | 4 | A member's recent posts |
| `POST /api/v1/linkedin/person/contact` | 4 | Public contact info for a member |
| `POST /api/v1/linkedin/company` | 1 | Profile for a company |
| `POST /api/v1/linkedin/company/posts` | 1 | A company's recent posts |
| `POST /api/v1/linkedin/company/people` | 4 | People who work at a company |
| `POST /api/v1/linkedin/company/jobs` | 4 | A company's open job listings |
| `POST /api/v1/linkedin/search/people` | 4 | Search people by name, title, company, or school |
| `POST /api/v1/linkedin/search/jobs` | 4 | Search jobs by keyword |
| `POST /api/v1/linkedin/search/posts` | 4 | Search posts by keyword |
| `POST /api/v1/linkedin/job` | 4 | Full details for a single job listing |
| `POST /api/v1/linkedin/post` | 4 | Full details for a single post |
| `POST /api/v1/linkedin/post/comments` | 4 | Comments on a post |

## Workflow

1. **A person:** call `/linkedin/person` with `username` (the vanity handle). The response includes a member `urn`.
2. **Person detail:** `/linkedin/person/about` and `/linkedin/person/posts` accept either the `urn` or the `username` (username is resolved to a urn automatically). `/linkedin/person/contact` takes `username`.
3. **A company:** call `/linkedin/company` with `company` (a universal name / slug like `microsoft`, or a full LinkedIn company URL). Use `/linkedin/company/posts` for its posts.
4. **Company detail:** `/linkedin/company/people` and `/linkedin/company/jobs` accept a numeric `company_id`, or a `company` slug/url that is resolved to a company_id automatically.
5. **Search:** `/linkedin/search/people` (by `search` name plus optional `title`, `company`, `school`, `location`), `/linkedin/search/jobs` (`search` keyword), `/linkedin/search/posts` (`search` keyword).
6. **Details:** `/linkedin/job` with `job_id`, `/linkedin/post` with `post_id`, and `/linkedin/post/comments` with `post_id`.

Paginated endpoints return `next_cursor` (or a `page`/`has_more` pair); pass `cursor` back for the next page.

## Parameters

### Person (`/person`)

| Parameter | Type | Default | Description |
|---|---|---|---|
| `username` | string | required | Public identifier (vanity handle), e.g. `williamhgates` |
| `include_experiences` | bool | -- | Include work experience |
| `include_educations` | bool | -- | Include education |
| `include_skills` | bool | -- | Include skills |
| `include_certifications` | bool | -- | Include certifications |
| `include_follower_and_connection` | bool | -- | Include follower/connection counts |

### Person about (`/person/about`) and person posts (`/person/posts`)

| Parameter | Type | Default | Description |
|---|---|---|---|
| `urn` | string | one of | Member urn |
| `username` | string | one of | Public identifier; resolved to a urn if `urn` is omitted |
| `cursor` | string | -- | (posts only) pagination cursor |

Provide `urn` or `username`.

### Person contact (`/person/contact`)

`username`* — public identifier.

### Company (`/company`)

`company`* — a company universal name (slug) or LinkedIn company URL.

### Company posts (`/company/posts`)

| Parameter | Type | Default | Description |
|---|---|---|---|
| `company` | string | required | Company slug or URL |
| `cursor` | string | -- | Pagination cursor |
| `count` | number | -- | Page size (1-100) |

### Company people (`/company/people`) and company jobs (`/company/jobs`)

| Parameter | Type | Default | Description |
|---|---|---|---|
| `company_id` | string | one of | Numeric company id |
| `company` | string | one of | Company slug/url; resolved to a company_id if `company_id` is omitted |
| `cursor` | string | -- | Pagination cursor |

Provide `company_id` or `company`.

### Search people (`/search/people`)

| Parameter | Type | Default | Description |
|---|---|---|---|
| `search` | string | one of | Name to search for |
| `title` | string | -- | Job title filter |
| `company` | string | -- | Company filter |
| `school` | string | -- | School filter |
| `location` | string | -- | A geo name or id filter |
| `cursor` | string | -- | Page cursor (page number) |

Provide at least one of `search`, `title`, `company`, `school`.

### Search jobs (`/search/jobs`)

`search`* , plus optional `cursor`, `date_posted`, `geocode`, `experience_level`, `remote`, `job_type`.

### Search posts (`/search/posts`)

`search`* , plus optional `cursor`, `date_posted`, `sort_by`, `content_type`.

### Job (`/job`)

`job_id`* , `include_skills` (bool, optional).

### Post (`/post`)

`post_id`* — a post id or activity urn.

### Post comments (`/post/comments`)

| Parameter | Type | Default | Description |
|---|---|---|---|
| `post_id` | string | required | Post id or activity urn |
| `cursor` | string | -- | Pagination cursor |
| `sort_order` | string | -- | `relevance` or `recent` |
| `post_type` | string | -- | `activity` or `ugc` |

## Examples

```python
import os, requests

BASE = "https://api.scavio.dev"
HEADERS = {"Authorization": f"Bearer {os.environ['SCAVIO_API_KEY']}"}

# 1. A person's profile (returns a urn)
person = requests.post(f"{BASE}/api/v1/linkedin/person", headers=HEADERS,
    json={"username": "williamhgates"}).json()

urn = person["data"]["urn"]

# 2. Their recent posts (urn or username works)
posts = requests.post(f"{BASE}/api/v1/linkedin/person/posts", headers=HEADERS,
    json={"urn": urn}).json()

# 3. Company profile (1 credit) then its open jobs
company = requests.post(f"{BASE}/api/v1/linkedin/company", headers=HEADERS,
    json={"company": "microsoft"}).json()

jobs = requests.post(f"{BASE}/api/v1/linkedin/company/jobs", headers=HEADERS,
    json={"company": "microsoft"}).json()

# 4. Search people by title + company
people = requests.post(f"{BASE}/api/v1/linkedin/search/people", headers=HEADERS,
    json={"title": "data engineer", "company": "stripe"}).json()
```

## Response shapes

Every response uses the envelope `{ data, response_time, credits_used, credits_remaining }`. Key `data` fields per endpoint:

- **person** — `id`, `urn`, `public_identifier`, `first_name`, `last_name`, `full_name`, `headline`, `location`, `is_premium`, `is_open_to_work`, `is_hiring`, `avatar`, `about`, `experiences[]`, `educations[]`, `skills[]`, `follower_count`, `connection_count`.
- **person/about** — `joined`, `contact_information`, `profile_photo`.
- **person/posts** — `data[]` (`id`, `post_type`, `text`, `content{images,video,article,poll}`, `activity{num_likes,num_comments,num_shares}`), `next_cursor`.
- **person/contact** — public contact fields for the member.
- **company** — company profile fields (name, description, industry, size, url, logo, etc.).
- **company/posts** — `data[]` posts, `next_cursor`.
- **company/people** — `people[]` / `data[]` member items, `next_cursor`.
- **company/jobs** — `jobs[]` / `data[]` job items, `next_cursor`.
- **search/people** — `page`, `total`, `has_more`, `data[]` (`id`, `urn`, `url`, `public_identifier`, `full_name`, `title`, `location`, `is_verified`, `is_premium`, `is_open_to_work`, `is_hiring`, `avatar`).
- **search/jobs** — `page`, `total`, `has_more`, `data[]` job items.
- **search/posts** — `page`, `total`, `has_more`, `data[]` (`id`, `url`, `title`, `activity{num_likes,num_comments,num_shares}`, `created_at`, `author{name,description,url,avatar}`).
- **job** — full job listing fields.
- **post** — full post fields.
- **post/comments** — `comments[]` / `data[]` comment items, `next_cursor`.

```json
{
  "data": {
    "page": 1,
    "total": 128,
    "has_more": true,
    "data": [
      {
        "id": "ACoAAA8BYqE",
        "urn": "ACoAAA8BYqEBCGLg_vT_ca6mMEqkpp9nVffJ3hc",
        "url": "https://www.linkedin.com/in/jane-dev/",
        "public_identifier": "jane-dev",
        "full_name": "Jane Dev",
        "title": "Data Engineer at Stripe",
        "location": "San Francisco Bay Area",
        "is_verified": true,
        "is_premium": false,
        "is_open_to_work": false,
        "is_hiring": false,
        "avatar": "https://media.licdn.com/dms/image/..."
      }
    ]
  },
  "credits_used": 4,
  "credits_remaining": 996
}
```

## Guardrails

- Credits are not uniform: `/company` and `/company/posts` cost **1 credit**; every other LinkedIn endpoint costs **4 credits**. Warn the user before paginating deeply.
- `/person` returns the member `urn` — reuse it for `/person/about` and `/person/posts` to avoid re-resolving, though `username` also works.
- `/company/people` and `/company/jobs` take a numeric `company_id` or a `company` slug/url that gets resolved automatically.
- Never fabricate names, titles, employers, job listings, post text, or counts. Only return API data.
- This is public profile data — treat it accordingly and do not infer private details.

## Failure handling

- `400` means an invalid or missing parameter (e.g. no `username`/`company_id`) — fix and retry.
- `401` means the API key is invalid or missing. Check `SCAVIO_API_KEY`.
- `429` means rate or usage limit exceeded. Wait before retrying. See https://scavio.dev/docs/rate-limits.
- `502` / `503` mean upstream is temporarily unavailable — LinkedIn upstream is flaky, so wait a few seconds and retry, up to a few times.
- If a search returns no results, relax filters or try different keywords.
- If `SCAVIO_API_KEY` is not set, prompt the user to export it before continuing.

## LangChain

```bash
pip install langchain-scavio
```

```python
from langchain_scavio import ScavioSearchTool
tool = ScavioSearchTool(engine="linkedin")
```
