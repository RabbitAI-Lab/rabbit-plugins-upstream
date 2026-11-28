# Microsoft Clarity

## API Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../../SKILL.md#security--permissions) for full security policy.

> **Quota — about 10 calls per project per day.** The Clarity Data Export API is read-only and has one endpoint, and Microsoft allows roughly 10 requests per project per day; after that every call returns `429` until the quota resets. The quota is shared by everything that uses the project's tokens, not just this connection.
> - **Make one call and reuse it.** Decide which dimensions the question needs, ask for all of them (up to three) in a single request, and answer follow-up questions from that result instead of calling again.
> - **Never poll, loop, or retry on `429`.** A retry burns quota without new data; tell the user the daily limit is reached.
> - Do not make a call just to check that the connection works.

**App name:** `microsoft-clarity`
**Upstream base URL:** `www.clarity.ms`

Replace the upstream base URL with the app name. Everything after the base URL including query strings is kept as-is. Any account-specific part of the base URL and the API credentials are stored in the Maton connection, and the gateway injects both so requests never carry them. For example:

- Upstream: `www.clarity.ms/export-data/api/v1/project-live-insights?numOfDays=1`
- Gateway: `api.maton.ai/microsoft-clarity/export-data/api/v1/project-live-insights?numOfDays=1`

The connection holds a Data Export API token, which is scoped to a single Clarity project. One connection is one project: there is no project ID in the path, and there is no endpoint to list projects.

### Project Live Insights

#### Get Project Live Insights

```bash
maton api '/microsoft-clarity/export-data/api/v1/project-live-insights?numOfDays={numOfDays}&dimension1={dimension1}'
```

**Note:** `{numOfDays}` and `{dimension1}` stand for real values; fill them in before sending the request.

Returns the project's dashboard metrics for the last 24, 48, or 72 hours, optionally broken down by up to three dimensions.

| Parameter | Required | Values |
|-----------|----------|--------|
| `numOfDays` | Yes | `1`, `2`, or `3`: the last 24, 48, or 72 hours, counted back from the time of the call. Older data is not available through the API. |
| `dimension1` | No | First breakdown dimension (see below). |
| `dimension2` | No | Second breakdown dimension. |
| `dimension3` | No | Third breakdown dimension. |

Dimensions: `Browser`, `Device`, `Country/Region`, `OS`, `Source`, `Medium`, `Campaign`, `Channel`, `URL`. Use the names exactly as listed, URL-encoded (`Country/Region` is `Country%2FRegion`).

**Example** (the last 24 hours, no breakdown):

```bash
maton api '/microsoft-clarity/export-data/api/v1/project-live-insights?numOfDays=1'
```

**Example** (the last 72 hours, broken down by device and traffic source in one call):

```bash
maton api '/microsoft-clarity/export-data/api/v1/project-live-insights?numOfDays=3&dimension1=Device&dimension2=Source'
```

**Response (trimmed, from Microsoft's documentation for `dimension1=OS`):**

```json
[
  {
    "metricName": "Traffic",
    "information": [
      {
        "totalSessionCount": "9554",
        "totalBotSessionCount": "8369",
        "distantUserCount": "189733",
        "PagesPerSessionPercentage": 1.0931,
        "OS": "Other"
      },
      {
        "totalSessionCount": "291942",
        "totalBotSessionCount": "31076",
        "distantUserCount": "212836",
        "PagesPerSessionPercentage": 2.2609,
        "OS": "Android"
      }
    ]
  }
]
```

The response is an array with one entry per metric; `information` holds one row per combination of the requested dimension values, each row carrying the dimension values as keys alongside the metric's figures. Counts are returned as strings. Metrics include `Traffic`, `EngagementTime`, `ScrollDepth`, `DeadClickCount`, `RageClickCount`, `ExcessiveScroll`, `QuickbackClick`, `ScriptErrorCount`, and `ErrorClickCount`. An undimensioned request also returns breakdown metrics such as `Browser`, `Device`, and `OS` (and, per Microsoft's docs, country/region, popular pages, page titles, and referrer URLs); a dimensioned request returns only the core metrics, split by the dimensions. An empty `information` array means no sessions matched in the window, which is common for low-traffic projects with several dimensions.

### Notes

- **Daily quota:** about 10 requests per project per day; a `429` (`Exceeded daily limit`) means the quota is spent until the next day. Do not retry it.
- **Window:** only the last 1 to 3 days (`numOfDays`), in UTC. There is no date-range parameter and no historical export.
- **Response size:** at most 1,000 rows per response, with no pagination. Adding dimensions multiplies rows, so a three-dimension request on a busy project (for example with `URL`) can be truncated; drop a dimension if the breakdown needs to be complete.
- **Read-only:** the Data Export API has no write endpoints. Session recordings, heatmaps, and project settings are not available through it.
- Errors: `400` (invalid parameters, for example a misspelled dimension or `numOfDays` out of range), `401` (missing, invalid, or expired token), `403` (token not authorized, including a revoked or replaced token), `429` (daily limit).
- Tokens are generated by a project admin under the Clarity project's **Settings → Data Export → Generate new API token**. Replacing or deleting that token in Clarity breaks the connection; reauthorize it with a new token.
- Authentication is handled by the gateway. Upstream, Clarity takes the token as a bearer `Authorization` header, but that token belongs to the Maton connection and is injected server-side: do not build an `Authorization` header for Clarity, never request a Clarity token, and never place one in a request, a script, or a trigger destination. Requests carry the Maton credential only, exactly like every other app in this gateway.

### Resources

- [Clarity Data Export API](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-data-export-api)
- [Maton CLI Manual](https://cli.maton.ai/manual)
