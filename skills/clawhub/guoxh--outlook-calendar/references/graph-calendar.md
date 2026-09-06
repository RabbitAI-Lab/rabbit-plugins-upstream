# Microsoft Graph — Calendar reference (this skill's subset)

This is a quick crib sheet for the endpoints this skill actually calls. It is **not**
a substitute for the full Microsoft Graph documentation at <https://learn.microsoft.com/graph/>.
Everything here is constrained to the calendar-only scope set; nothing in this file
attempts to document mail, contacts, files, or directory.

## Endpoints used

| Method | Path | Purpose |
|---|---|---|
| `GET`  | `/me?$select=id,userPrincipalName[,displayName]` | probe token at sign-in / `token status` |
| `GET`  | `/me/calendarView?startDateTime=…&endDateTime=…&$orderby=start/dateTime&$top=…` | list events in a window |
| `GET`  | `/me/events/{id}` | fetch a single event (preview before delete) |
| `POST` | `/me/events` | create an event |
| `PATCH`| `/me/events/{id}` | update an event (only changed fields) |
| `DELETE` | `/me/events/{id}` | delete an event (returns 204) |

`/me/calendarView` automatically expands recurring events in the window and respects
the user's working-hours / showAs / free-busy information.

## Required headers

| Header | When | Value |
|---|---|---|
| `Authorization: Bearer <access_token>` | all calls | required |
| `Accept: application/json` | all calls | required |
| `Content-Type: application/json` | POST / PATCH | required |
| `Prefer: outlook.timezone="Asia/Shanghai"` | `/me/calendarView` (this skill) | recommended |

The `Prefer: outlook.timezone=…` header tells Graph to **return** all `start.dateTime`
and `end.dateTime` values pre-converted into that IANA zone, so you don't have to
do timezone math in the client. The skill sets this to whatever the user passed to
`--tz` (default `Asia/Shanghai`).

## Event body (POST / PATCH)

```json
{
  "subject":  "string",
  "body":     { "contentType": "Text", "content": "string" },
  "start":    { "dateTime": "2026-06-18T12:00:00+08:00", "timeZone": "Asia/Shanghai" },
  "end":      { "dateTime": "2026-06-18T13:00:00+08:00", "timeZone": "Asia/Shanghai" },
  "location": { "displayName": "string" },
  "isAllDay": false,
  "attendees": [
    { "emailAddress": { "name": "Alice", "address": "alice@contoso.com" },
      "type": "required" }
  ]
}
```

PATCH uses the same shape but you may omit any field you do not want to change.

## Selected fields returned (for `select=…`)

| Field | Why we use it |
|---|---|
| `id` | uniquely identifies the event (needed for update / delete) |
| `subject` | display in summary |
| `start`, `end` | render in summary / check overlaps |
| `location.displayName` | render in summary |
| `organizer.emailAddress.{name,address}` | shown before delete |
| `attendees[].emailAddress.address` | shown in detail; **not** written by this skill |
| `isAllDay` | disambiguate all-day events |
| `showAs` | `busy` / `free` / `tentative` / `oof` / `workingElsewhere` |
| `bodyPreview` | short summary (we do not download full `body` for privacy) |
| `webLink` | open in Outlook on the web |
| `responseStatus.response` | `none` / `organizer` / `tentativelyAccepted` / `accepted` / `declined` / `notResponded` |

We do **not** request `body.content` over the wire from the read path — the default
`bodyPreview` is enough for typical "what's on my calendar" listings and avoids
pushing potentially-sensitive free-text through the agent.

## Pagination

`/me/calendarView` returns at most `1000` events per page; the default is `10`.
We pass `$top` (configurable via `--top`, default `100`) and follow `@odata.nextLink`
until it is absent or we hit `--max-pages` (default `5`, i.e. up to 500 events).

## Status codes we care about

| Code | Meaning | What this skill does |
|---|---|---|
| `200` | OK | parse JSON body |
| `201` | Created | parse JSON body, print `id` |
| `204` | No Content (delete) | success |
| `400` | Bad Request | surface sanitized snippet and exit non-zero |
| `401` | Unauthorized | try one silent refresh using `refresh_token`, then fail |
| `403` | Forbidden | fail — likely a scope / consent issue |
| `404` | Not Found | fail (delete / update on a missing event) |
| `429` | Too Many Requests | currently **not** retried; surfaces error. (TODO if usage grows.) |

## Scopes this skill actually requests

```
offline_access
https://graph.microsoft.com/User.Read
https://graph.microsoft.com/Calendars.ReadWrite
```

Anything outside this list is a bug — please report it.

## Time zone notes

- `Asia/Shanghai` is a fixed offset (`+08:00`) zone — no DST. Sending
  `2026-06-18T12:00:00+08:00` is unambiguous.
- For zones with DST (`America/New_York`, `Europe/Berlin`, …) the **naive** form
  `2026-06-18T12:00:00` is *also* accepted by Graph when paired with the
  `timeZone` field; Graph converts to UTC server-side. This skill always sends an
  explicit offset, which is the safest form.
- `dateWithTz` / `normalize_dt` use Python's `zoneinfo` (Python 3.9+), which is
  IANA-backed and DST-correct. We deliberately do **not** use `date -d` for timezone
  math because the GNU coreutils `TZ` handling differs between Linux and macOS BSD
  `date`.

## Things we deliberately do NOT do

- We do not call `/me/messages`, `/me/mailFolders`, `/me/sendMail`, or anything in
  the `Mail.*` namespace.
- We do not call `/me/contacts`, `/me/photo`, or `/me/people`.
- We do not call `/me/drive/*` (OneDrive / SharePoint files).
- We do not call any directory/admin endpoint (`/users`, `/groups`, `/organization`).
- We do not invite attendees. The skill creates simple "no-attendee" events
  only. If a future revision needs attendees, it must add a `--invite <email>`
  flag and the documentation must call out the consent implications.
- We do not read or set `body.content` over the read path (we use `bodyPreview`).
