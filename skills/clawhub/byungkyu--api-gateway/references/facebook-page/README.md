# Facebook Page Routing Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../SKILL.md#security--permissions) for full security policy.

**App name:** `facebook-page`
**Base URL proxied:** `graph.facebook.com`

## API Path Pattern

```
/facebook-page/v25.0/{resource}
```

## Page Access Token

Facebook's Graph API requires a **Page Access Token** for page-scoped endpoints (feed, insights, comments). The gateway injects the connection's User Access Token, which authorizes `me/accounts` and page metadata but not page-scoped operations. This is a Facebook API constraint, not a gateway feature — the token is issued by Facebook, scoped to pages the connected user already administers, and grants no access beyond what that user's existing connection already permits.

> **Handling rules — the page token is a credential.** `api.maton.ai` is the only host that issues it and the only host that accepts it.
> - **Never** write it to disk, logs, environment files, shell history, or scrollback.
> - **Never** print, echo, or include it in any output shown to the user or returned to a caller.
> - **No other host may receive it** — not a webhook destination, trigger header, body template, or third-party request.
> - Hold it in an in-memory variable for the duration of the current request sequence only; discard it afterward. Do not cache or reuse it across sessions.
> - Request it only when a page-scoped call actually requires it. Prefer the endpoints below that need no page token at all.

**Start here — do not retrieve a token you don't need.** These endpoints work with the gateway-injected User Access Token alone, with no `access_token` parameter and no token retrieval step:
- `GET /facebook-page/v25.0/me/accounts`
- `GET /facebook-page/v25.0/{page_id}`

If one of these satisfies the task, stop — no page token is needed at all.

**Obtaining a page token** — only when a specific page-scoped endpoint below actually requires one, and only for the page the user named:
1. `GET /facebook-page/v25.0/me/accounts?fields=id,name,access_token` — the response carries an `access_token` field for that one page
2. Pass it as the `access_token` query parameter on that page-scoped call, then discard it

Retrieve and consume it inside a single script so the value never crosses a process boundary and never lands in shell history or scrollback:

```bash
python3 <<'EOF'
import json, re, subprocess

BASE = '/facebook-page/v25.0'

# Each call goes through `maton api`, so the gateway injects the credential and this
# script never reads or holds a Maton key. Only the page token lives in memory.
def call(path):
    p = subprocess.run(['maton', 'api', path], capture_output=True, text=True, check=True)
    return json.loads(p.stdout)

pages = call(f'{BASE}/me/accounts?fields=id,name,access_token')   # token is never printed
page = pages['data'][0]
page_id, page_token = page['id'], page['access_token']

# These came out of an API response, and they are about to go into a request path.
# Check their shape first rather than trusting the response (see Security & Permissions).
if not re.fullmatch(r'[0-9]+', page_id) or not re.fullmatch(r'[A-Za-z0-9_-]+', page_token):
    raise SystemExit('unexpected page id or token format - stopping')

feed = call(f'{BASE}/{page_id}/feed?fields=id,message,created_time&limit=10'
            f'&access_token={page_token}')
del page_token                                              # discard immediately after use
print(json.dumps(feed, indent=2))                           # response only
EOF
```

In the endpoint examples below, `{page_access_token}` marks **where the runtime value goes, not something to fill in ahead of time.** Substitute the in-memory variable at call time. Never paste a literal token into a command, a file, or a saved example, and never build a reusable snippet with a real token embedded in the URL — a token in a query string is a credential in plain text.

## Common Endpoints

### List Pages
```bash
maton api '/facebook-page/v25.0/me/accounts?fields=id,name,category,fan_count,followers_count'
```

### Get Page Details
```bash
maton api '/facebook-page/v25.0/{page_id}?fields=id,name,about,category,fan_count,followers_count,website,link'
```

### Get Page Feed
```bash
maton api '/facebook-page/v25.0/{page_id}/feed?fields=id,message,created_time&limit=10&access_token={page_access_token}'
```

### Get Published Posts
```bash
maton api '/facebook-page/v25.0/{page_id}/published_posts?fields=id,message,created_time&limit=10&access_token={page_access_token}'
```

### Publish a Post
```bash
maton api -X POST '/facebook-page/v25.0/{page_id}/feed?access_token={page_access_token}' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "message": "Hello from my page!"
}
EOF
```

### Update a Post
```bash
maton api -X POST '/facebook-page/v25.0/{post_id}?access_token={page_access_token}' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "message": "Updated post content"
}
EOF
```

### Delete a Post
```bash
maton api '/facebook-page/v25.0/{post_id}?access_token={page_access_token}' -X DELETE
```

### Get Comments on a Post
```bash
maton api '/facebook-page/v25.0/{post_id}/comments?fields=id,message,from,created_time&access_token={page_access_token}'
```

### Post a Comment
```bash
maton api -X POST '/facebook-page/v25.0/{post_id}/comments?access_token={page_access_token}' \
  -H 'Content-Type: application/json' \
  --input - <<'EOF'
{
  "message": "Thanks for your feedback!"
}
EOF
```

### Get Page Insights
```bash
maton api '/facebook-page/v25.0/{page_id}/insights?metric=page_views_total,page_posts_impressions,page_video_views&period=day&access_token={page_access_token}'
```

### Get Page Insights with Date Range
```bash
maton api '/facebook-page/v25.0/{page_id}/insights?metric=page_views_total&period=day&since=2026-01-01&until=2026-01-31&access_token={page_access_token}'
```

### Get Page Photos
```bash
maton api '/facebook-page/v25.0/{page_id}/photos?fields=id,name,created_time,images&limit=10&access_token={page_access_token}'
```

### Get Page Videos
```bash
maton api '/facebook-page/v25.0/{page_id}/videos?fields=id,title,description,created_time&limit=10&access_token={page_access_token}'
```

### Get Product Catalogs
```bash
maton api '/facebook-page/v25.0/{page_id}/product_catalogs?access_token={page_access_token}'
```

#### Get Products in a Catalog
```bash
maton api '/facebook-page/v25.0/{catalog_id}/products?fields=id,name,price,image_url&access_token={page_access_token}'
```

## Notes

- Post IDs follow the format `{page_id}_{post_id}`
- Uses cursor-based pagination with `before`/`after` cursors
- Maximum 100 results per page for feed endpoints
- Approximately 600 ranked, published posts per year are accessible
- Insight period values: `day`, `week`, `days_28`
- Deprecated metrics: use `page_views_total` instead of `page_impressions`, `page_posts_impressions` instead of `page_engaged_users`

## Resources

- [Facebook Graph API Overview](https://developers.facebook.com/docs/graph-api/overview)
- [Page API Reference](https://developers.facebook.com/docs/graph-api/reference/page/)
- [Pages API Getting Started](https://developers.facebook.com/docs/pages-api/getting-started)
