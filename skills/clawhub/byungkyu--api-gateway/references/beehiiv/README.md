# beehiiv Routing Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../SKILL.md#security--permissions) for full security policy.

**App name:** `beehiiv`
**Base URL proxied:** `api.beehiiv.com`

## API Path Pattern

```
/beehiiv/v2/{resource}
```

## Common Endpoints

### Publications

#### List Publications
```bash
GET /beehiiv/v2/publications
```

#### Get Publication
```bash
GET /beehiiv/v2/publications/{publication_id}
```

### Subscriptions

#### List Subscriptions
```bash
GET /beehiiv/v2/publications/{publication_id}/subscriptions
```

#### Get Subscription by ID
```bash
GET /beehiiv/v2/publications/{publication_id}/subscriptions/{subscription_id}
```

#### Get Subscription by Email
```bash
GET /beehiiv/v2/publications/{publication_id}/subscriptions/by_email/{email}
```

> **⚠ This endpoint puts a subscriber's email address in the URL path.** Unlike a request body, a URL is routinely recorded in access logs, proxy and CDN logs, monitoring and error-tracking tools, and command history — so calling this leaves a real person's email address in more places than the API call itself. URL-encode the address (`@` becomes `%40`), look up one subscriber the user actually named rather than probing addresses to see who is subscribed, and do not build lists of subscribers this way. Prefer the subscription ID (`.../subscriptions/{subscription_id}`) when you already have it. Subscriber records are personal data belonging to the publication's readers: retrieve only what the task needs and avoid echoing full addresses back in output where they are not required.

#### Create Subscription
```bash
POST /beehiiv/v2/publications/{publication_id}/subscriptions
Content-Type: application/json

{
  "email": "subscriber@example.com",
  "utm_source": "api"
}
```

#### Update Subscription
```bash
PATCH /beehiiv/v2/publications/{publication_id}/subscriptions/{subscription_id}
```

#### Delete Subscription
```bash
DELETE /beehiiv/v2/publications/{publication_id}/subscriptions/{subscription_id}
```

### Posts

#### List Posts
```bash
GET /beehiiv/v2/publications/{publication_id}/posts
```

#### Get Post
```bash
GET /beehiiv/v2/publications/{publication_id}/posts/{post_id}
```

### Custom Fields

#### List Custom Fields
```bash
GET /beehiiv/v2/publications/{publication_id}/custom_fields
```

#### Create Custom Field
```bash
POST /beehiiv/v2/publications/{publication_id}/custom_fields
```

### Segments

```bash
GET /beehiiv/v2/publications/{publication_id}/segments
GET /beehiiv/v2/publications/{publication_id}/segments/{segment_id}
```

### Tiers

```bash
GET /beehiiv/v2/publications/{publication_id}/tiers
POST /beehiiv/v2/publications/{publication_id}/tiers
PATCH /beehiiv/v2/publications/{publication_id}/tiers/{tier_id}
```

### Automations

```bash
GET /beehiiv/v2/publications/{publication_id}/automations
GET /beehiiv/v2/publications/{publication_id}/automations/{automation_id}
```

## Pagination

Cursor-based (recommended) or page-based (deprecated):

```bash
# Cursor-based
GET /beehiiv/v2/publications/{pub_id}/subscriptions?limit=10&cursor={next_cursor}

# Page-based (max 100 pages)
GET /beehiiv/v2/publications?page=2&limit=10
```

## Notes

- Publication IDs start with `pub_`
- Subscription IDs start with `sub_`
- Timestamps are Unix timestamps
- Cursor-based pagination is recommended
- Page-based pagination limited to 100 pages

## Resources

- [beehiiv Developer Documentation](https://developers.beehiiv.com/)
- [beehiiv API Reference](https://developers.beehiiv.com/api-reference)
