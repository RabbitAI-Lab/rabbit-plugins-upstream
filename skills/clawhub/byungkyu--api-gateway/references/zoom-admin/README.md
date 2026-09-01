# Zoom Admin Routing Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../SKILL.md#security--permissions) for full security policy.

> **⚠ Account-wide administrative access.** This app is not the ordinary Zoom integration — it connects with **admin-level OAuth scopes covering the entire Zoom account**, so calls act across every user in the organization, not just the connected user. That reach includes other people's meetings and webinars, their per-user settings, account-level settings, and **cloud recordings and transcripts of meetings the user did not attend** — which routinely contain confidential discussion, personal data, and third-party confidences.
>
> - **Prefer the `zoom` app** for anything scoped to the user's own meetings and recordings. Reach for `zoom-admin` only when the task genuinely requires acting on other users or account-level configuration, and say why.
> - **Name the target user before acting.** `{userId}` is an opaque ID; resolve it, show the user whose account is being read or changed, and never fan out across users to "find" something.
> - **Recordings and transcripts are the most sensitive resource here.** Do not list, download, or summarize another user's recordings without the user confirming that specific person and that they are authorized to access it. Never bulk-export recordings.
> - **Account settings and per-user settings changes affect everyone** and are not obviously reversible. Read the current value, show the exact before/after, and get explicit approval per setting.
> - Deleting a meeting or webinar notifies and disrupts external participants — see the high-impact operations list in [SKILL.md](../SKILL.md#security--permissions).

**App name:** `zoom-admin`
**Base URL proxied:** `api.zoom.us`

## API Path Pattern

```
/zoom-admin/v2/{resource}
```

## Common Endpoints

### Users

#### List Users
```bash
GET /zoom-admin/v2/users?status=active&page_size=30
```

#### Get User
```bash
GET /zoom-admin/v2/users/{userId}
GET /zoom-admin/v2/users/me
```

#### Get User Settings
```bash
GET /zoom-admin/v2/users/{userId}/settings
```

### Meetings

#### List User's Meetings
```bash
GET /zoom-admin/v2/users/{userId}/meetings?type=scheduled&page_size=30
```

#### Get Meeting
```bash
GET /zoom-admin/v2/meetings/{meetingId}
```

#### Create Meeting
```bash
POST /zoom-admin/v2/users/{userId}/meetings
Content-Type: application/json

{
  "topic": "Team Meeting",
  "type": 2,
  "start_time": "2026-05-02T10:00:00Z",
  "duration": 30,
  "timezone": "America/Los_Angeles",
  "settings": {
    "host_video": true,
    "participant_video": true,
    "mute_upon_entry": true
  }
}
```

#### Update Meeting
```bash
PATCH /zoom-admin/v2/meetings/{meetingId}
Content-Type: application/json

{
  "topic": "Updated Title",
  "duration": 45
}
```

#### Delete Meeting
```bash
DELETE /zoom-admin/v2/meetings/{meetingId}
```

#### Get Past Meeting Details
```bash
GET /zoom-admin/v2/past_meetings/{meetingId}
```

#### List Past Meeting Instances
```bash
GET /zoom-admin/v2/past_meetings/{meetingId}/instances
```

### Webinars

**Note:** Requires Webinar add-on plan.

#### List Webinars
```bash
GET /zoom-admin/v2/users/{userId}/webinars?page_size=30
```

#### Get Webinar
```bash
GET /zoom-admin/v2/webinars/{webinarId}
```

### Recordings

#### List User Recordings
```bash
GET /zoom-admin/v2/users/{userId}/recordings?from=2026-04-01&to=2026-04-30
```

#### Get Meeting Recordings
```bash
GET /zoom-admin/v2/meetings/{meetingId}/recordings
```

### Account

#### Get Account Settings
```bash
GET /zoom-admin/v2/accounts/me/settings
```

**Note:** Requires a paid Zoom plan.

## Meeting Types

| Type | Description |
|------|-------------|
| 1 | Instant meeting |
| 2 | Scheduled meeting |
| 3 | Recurring meeting (no fixed time) |
| 4 | PMI meeting |
| 8 | Recurring meeting (fixed time) |

## Pagination

Token-based pagination using `next_page_token` (15-minute expiry):

```bash
GET /zoom-admin/v2/users?page_size=30&next_page_token={token}
```

## Notes

- Uses admin-level OAuth scopes for account-wide access - every call can reach any user in the account (see the warning at the top of this file)
- Use `me` to reference the authenticated user or account
- Meeting IDs are numeric; UUIDs are base64-encoded
- Double-encode UUID if it starts with `/` or contains `//`
- Webinar endpoints require Webinar add-on subscription
- Account Settings endpoint requires a paid Zoom plan
- Rate limits vary by plan; returns HTTP 429 when exceeded

## Resources

- [Zoom API Documentation](https://developers.zoom.us/docs/api/)
- [Zoom REST API Reference](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/)
