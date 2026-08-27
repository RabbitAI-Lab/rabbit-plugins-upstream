# MCP tools

Endpoint: `https://worthtotry.com/api/mcp/` — Streamable HTTP.

Every tool returns its payload twice: as JSON text in `content`, and as the same object in
`structuredContent`. Parse `structuredContent`.

A failing tool returns `isError: true` and a single text message. That message is written for you to
relay — pass it on rather than inventing your own wording.

## Authorization

| Tool                         | Needs authorization |
| ---------------------------- | ------------------- |
| `search_tools`               | No                  |
| `get_tool`                   | No                  |
| `list_categories`            | No                  |
| `check_submission_readiness` | No                  |
| `submit_tool`                | Yes                 |
| `get_my_submissions`         | Yes                 |

Authorization is OAuth 2.1 in the browser. The first call to a protected tool returns a 401 carrying
a `WWW-Authenticate` challenge; a compliant client discovers the authorization server from it,
registers itself, and opens a consent page. The person approves once. Scopes:

- `submit` — open draft listings on their behalf
- `read:submissions` — see the listings they have submitted and their status

Access tokens are short-lived and refreshed by the client. You never handle one.

---

## `search_tools`

Find listings in plain language.

| Argument     | Type                                                         | Default |
| ------------ | ------------------------------------------------------------ | ------- |
| `query`      | string, max 120 — matched against name, tagline, description | —       |
| `category`   | string — a category slug, e.g. `developer-tools`             | —       |
| `pricing`    | `free` `freemium` `paid` `subscription` `one_time` `contact` | —       |
| `openSource` | boolean                                                      | —       |
| `sort`       | `newest` or `top` (`top` ranks by upvotes)                   | —       |
| `limit`      | integer 1–50                                                 | 10      |
| `cursor`     | string — pass back `nextCursor` from the previous call       | —       |

Returns `{ items, nextCursor }`. Each item: `slug`, `name`, `tagline`, `url`, `categories` (display
names), `pricing`, `openSource`, `upvotes`, `toolUrl`.

`nextCursor` is opaque. Do not construct one; page by passing back what you were given, and stop
when it is null.

## `get_tool`

| Argument | Type                                  |
| -------- | ------------------------------------- |
| `slug`   | string — the slug from `search_tools` |

Returns `slug`, `name`, `tagline`, `description`, `url`, `categories`, `pricing`, `openSource`,
`upvotes`, `commentCount`, `twitterHandle`, `launchDate`, `toolUrl`.

Errors if the slug does not exist or the listing is not published.

## `list_categories`

No arguments. Returns `{ items }` of `{ slug, name, toolCount }` for every category that has at
least one published tool. Use the `slug` values when filtering a search or drafting a listing.

## `check_submission_readiness`

| Argument | Type                                |
| -------- | ----------------------------------- |
| `url`    | string — the product's homepage URL |

Fetches the page and returns:

| Field              | What it is                                                             |
| ------------------ | ---------------------------------------------------------------------- |
| `url`              | The URL after redirects were followed                                  |
| `score`            | 0–100, weighted across the six checks                                  |
| `submittable`      | False only when the `duplicate` check fails                            |
| `checks`           | Six objects: `id`, `label`, `status`, `detail`, `fix`                  |
| `suggestedListing` | The listing that would be drafted, or null if too little could be read |
| `note`             | A one-line summary of what to do next                                  |

`suggestedListing` carries `name`, `tagline`, `description`, `categories`, `pricing`, `logo` and
`twitterHandle`. `targetKeyword` is never suggested — that is deliberate.

Results are cached per host for 15 minutes, so re-running straight after a fix may return the
previous audit.

See `readiness-checks.md` for what each check means.

## `submit_tool`

Opens a draft listing for the person who authorized the connection.

| Argument        | Type                                                         |
| --------------- | ------------------------------------------------------------ |
| `url`           | string, required, max 2048 — the product's homepage          |
| `name`          | string, max 40 — overrides the extracted name                |
| `tagline`       | string, max 60                                               |
| `description`   | string, max 600                                              |
| `categories`    | array of at most 3 category slugs or display names           |
| `pricing`       | `free` `freemium` `paid` `subscription` `one_time` `contact` |
| `openSource`    | boolean                                                      |
| `twitterHandle` | string, max 15                                               |
| `targetKeyword` | string, max 100 — leave to the person                        |

Only `url` is required; every other field falls back to what the audit extracted. Category display
names and slugs both resolve, and anything unrecognised is dropped rather than rejected.

Returns:

| Field            | What it is                                                       |
| ---------------- | ---------------------------------------------------------------- |
| `ok`             | `true`                                                           |
| `slug`           | The listing's slug                                               |
| `status`         | `draft` — always                                                 |
| `reviewUrl`      | Where the person finishes the submission                         |
| `readinessScore` | The score from the audit it ran                                  |
| `warnings`       | Everything left to fix, including every failing check's `detail` |
| `note`           | A restatement of the boundary                                    |

It runs its own audit first, so a duplicate is refused here too.

**It cannot publish, set a launch date, or pay.** There is no argument for any of those, and there is
no tool that does them. There is also no argument for the first comment or for a screenshot — both
are added in the browser.

## `get_my_submissions`

No arguments. Returns `{ items }`, one per listing the authorized person owns, in any state:

`slug`, `name`, `status` (`draft` `pending` `approved` `rejected` `published`), `rejectionReason`,
`requestedLaunchDate`, `publishedAt`, `upvotes`, `views`, `badgeStatus`, `submittedVia`,
`reviewUrl`, and `toolUrl` once published.

Use it to answer "where is my submission" without asking the person to check the dashboard.
