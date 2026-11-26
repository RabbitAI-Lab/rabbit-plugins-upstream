# Follow Up Boss

## API Reference

> **Safety:** All write operations (POST, PUT, PATCH, DELETE) require explicit user confirmation before execution. Verify the target resource and intended effect with the user first. See the main [SKILL.md](../../SKILL.md#security--permissions) for full security policy.

> **Privacy — people, calls, texts and notes are personal data about real people.** A Follow Up Boss account holds home buyers' and sellers' names, email addresses, phone numbers, addresses, price ranges, and the agents' notes, call logs and text message logs about them. This is personal data under GDPR/CCPA, and the leads are third parties who gave their details to the user's brokerage, not to an agent.
> - The sample values below (`Jane Doe`, `jane@example.com`, `555-555-0100`) are **placeholders**. Never send them to a live account, and never invent contact details to fill a required field — ask the user.
> - Retrieve only the records the task needs. Filter server-side (`personId`, `email`, `phone`, `stage`, `assignedUserId`) rather than paging through the whole database, and do not export the people list.
> - Return the narrowest answer that satisfies the request; don't print full person records, call logs or text threads when the user asked one question.
> - **Never forward Follow Up Boss contact data to a third-party host** — not to a trigger destination, external webhook, spreadsheet service, or enrichment API — without explicit user approval for that specific transfer.
> - Confirm the exact person by name or email (not just a numeric ID) before any write, and never bulk-update records without per-record approval.

**App name:** `follow-up-boss`
**Upstream base URL:** `api.followupboss.com`

Replace the upstream base URL with the app name. Everything after the base URL including query strings is kept as-is. Any account-specific part of the base URL and the API credentials are stored in the Maton connection, and the gateway injects both so requests never carry them. For example:

- Upstream: `api.followupboss.com/v1/people`
- Gateway: `api.maton.ai/follow-up-boss/v1/people`

### Identity

#### Get Account and Current User

```bash
maton api '/follow-up-boss/v1/identity'
```

**Response:**

```json
{
  "account": {
    "id": 123456,
    "domain": "examplerealty",
    "name": "Example Realty",
    "owner": {"name": "Jane Agent", "email": "jane.agent@example.com"},
    "partners": []
  },
  "user": {
    "id": 1,
    "name": "Jane Agent",
    "email": "jane.agent@example.com",
    "role": "Broker",
    "isOwner": true,
    "isAdmin": true
  }
}
```

`GET /v1/me` is **blocked by Maton** and returns `403`: Follow Up Boss includes tokens for other services (Algolia, BombBomb, calling) in that response. Use `/v1/identity` for the account and the connected user.

### People

#### List People

```bash
maton api '/follow-up-boss/v1/people?limit=10'
```

**Query parameters:**
- `limit` - Results per page (default 10, max 100)
- `offset` - Number of records to skip
- `next` - Cursor from `_metadata.next` (faster than `offset` for deep pages)
- `sort` - Field to sort on, e.g. `created` or `-created` (descending), `updated`, `lastActivity`
- `fields` - Comma-separated fields to return, or `allFields` to include custom fields
- `name`, `firstName`, `lastName`, `email`, `phone` - Match on contact details
- `stage` - Stage name, e.g. `Lead`
- `source` - Lead source name
- `assignedUserId` / `assignedTo` - Assigned agent ID / full name
- `tags` - Tag name
- `includeTrash` - Include people in the Trash stage

**Example:**

```bash
maton api '/follow-up-boss/v1/people?limit=5&sort=-created&stage=Lead'
```

**Response (trimmed):**

```json
{
  "_metadata": {
    "collection": "people",
    "offset": 0,
    "limit": 5,
    "total": 42,
    "next": "{cursor}",
    "nextLink": ".../v1/people?limit=5&next={cursor}"
  },
  "people": [
    {
      "id": 1,
      "created": "2026-01-15T18:22:04Z",
      "name": "Jane Doe",
      "firstName": "Jane",
      "lastName": "Doe",
      "stage": "Lead",
      "stageId": 2,
      "source": "Zillow",
      "assignedUserId": 1,
      "assignedTo": "Jane Agent",
      "tags": ["Buyer"],
      "emails": [{"value": "jane@example.com", "type": "home", "isPrimary": 1}],
      "phones": [{"value": "555-555-0100", "type": "mobile", "isPrimary": 1}]
    }
  ]
}
```

#### Get Person

```bash
maton api '/follow-up-boss/v1/people/{person_id}'
```

**Note:** `{person_id}` stands for a real value; fill it in before sending the request.

#### Check for a Duplicate

```bash
maton api '/follow-up-boss/v1/people/checkDuplicate?email={email}'
```

**Note:** `{email}` stands for a real value; fill it in before sending the request. Also accepts `phone`. Returns `{"found": true}` or `{"found": false}`; it creates nothing.

#### Create Person

> **New leads should go through `POST /v1/events`** (below), not this endpoint. `POST /v1/people` only creates the record: it runs no lead-flow assignment, action plans, automations, or agent notifications. Use it for manual entries the user explicitly wants to add quietly.

```bash
maton api -X POST '/follow-up-boss/v1/people?deduplicate=true' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "firstName": "Jane",
  "lastName": "Doe",
  "stage": "Lead",
  "source": "Website",
  "emails": [{"value": "jane@example.com", "type": "home"}],
  "phones": [{"value": "555-555-0100", "type": "mobile"}],
  "tags": ["Buyer"]
}
JSON
```

With `deduplicate=true`, an existing match by email or phone is returned unchanged (`200`) instead of a duplicate being created. `source` and `sourceUrl` can only be set at creation.

#### Update Person

```bash
maton api -X PUT '/follow-up-boss/v1/people/{person_id}' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "stage": "Active Client",
  "tags": ["Buyer", "Pre-approved"]
}
JSON
```

**Note:** `{person_id}` stands for a real value; fill it in before sending the request. For array fields (`emails`, `phones`, `tags`), read the person first and send the full intended list.

### Events (Sending In Leads)

#### Create Event

> **This is how leads are normally sent into Follow Up Boss.** An event finds or creates the person (deduplicating by email and phone), records the inquiry on their timeline, assigns an agent through the account's Lead Flow, starts action plans and automations, and notifies the assigned agent. Confirm the person, the event `type`, and the `source` with the user before sending; a real agent will be alerted.

```bash
maton api -X POST '/follow-up-boss/v1/events' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "source": "Website",
  "system": "Maton",
  "type": "General Inquiry",
  "message": "Looking for a 3-bedroom home under $500k",
  "person": {
    "firstName": "Jane",
    "lastName": "Doe",
    "emails": [{"value": "jane@example.com"}],
    "phones": [{"value": "555-555-0100"}],
    "tags": ["Buyer"]
  }
}
JSON
```

`type` is one of `Registration`, `Inquiry`, `Seller Inquiry`, `Property Inquiry`, `General Inquiry`, `Viewed Property`, `Saved Property`, `Visited Website`, `Incoming Call`, `Unsubscribed`, `Property Search`, `Saved Property Search`, `Visited Open House`, `Viewed Page`. An optional `property` object (`street`, `city`, `state`, `code`, `mlsNumber`, `price`, `url`, ...) describes the listing. Responses: `201` new person created, `200` existing person updated, `204` the lead flow for this source is archived and the event was ignored.

#### List Events

```bash
maton api '/follow-up-boss/v1/events?personId={person_id}&limit=10'
```

**Note:** `{person_id}` stands for a real value; fill it in before sending the request. `GET /v1/events` has its own, lower rate limit (the `events` context in the `X-RateLimit-*` headers).

### Deals

#### List Deals

```bash
maton api '/follow-up-boss/v1/deals?limit=10'
```

**Query parameters:** `pipelineId`, `personId`, `userId`, `limit`, `offset`, `sort`.

**Example:**

```bash
maton api '/follow-up-boss/v1/deals?pipelineId={pipeline_id}&limit=5'
```

**Note:** `{pipeline_id}` stands for a real value; fill it in before sending the request.

#### Get Deal

```bash
maton api '/follow-up-boss/v1/deals/{deal_id}'
```

**Note:** `{deal_id}` stands for a real value; fill it in before sending the request.

#### Create Deal

```bash
maton api -X POST '/follow-up-boss/v1/deals' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "name": "123 Main St purchase",
  "stageId": 12,
  "peopleIds": [1],
  "userIds": [1],
  "price": 450000,
  "projectedCloseDate": "2026-03-31"
}
JSON
```

`name` and `stageId` (a deal stage from `GET /v1/pipelines`) are required.

### Pipelines and Stages

#### List Pipelines

```bash
maton api '/follow-up-boss/v1/pipelines'
```

#### Get Pipeline

```bash
maton api '/follow-up-boss/v1/pipelines/{pipeline_id}'
```

**Note:** `{pipeline_id}` stands for a real value; fill it in before sending the request. Each pipeline lists its deal `stages`.

#### List Person Stages

```bash
maton api '/follow-up-boss/v1/stages'
```

Person stages (`Lead`, `Prospect`, `Active Client`, ...) are separate from deal pipeline stages.

### Tasks

#### List Tasks

```bash
maton api '/follow-up-boss/v1/tasks?limit=10'
```

**Query parameters:** `personId`, `assignedUserId`, `type`, `isCompleted`, `limit`, `offset`, `sort`.

**Example:**

```bash
maton api '/follow-up-boss/v1/tasks?personId={person_id}&limit=5'
```

**Note:** `{person_id}` stands for a real value; fill it in before sending the request.

#### Get Task

```bash
maton api '/follow-up-boss/v1/tasks/{task_id}'
```

**Note:** `{task_id}` stands for a real value; fill it in before sending the request.

#### Create Task

```bash
maton api -X POST '/follow-up-boss/v1/tasks' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "personId": 1,
  "assignedUserId": 1,
  "name": "Call about pre-approval",
  "type": "Call",
  "dueDate": "2026-02-01"
}
JSON
```

`personId` and one of `assignedUserId` / `assignedTo` are required. `type` is one of `Follow Up`, `Call`, `Text`, `Email`, `Appointment`, `Showing`, `Closing`, `Open House`, `Thank You`. Use `dueDateTime` (e.g. `2026-02-01T15:00:00-05:00`) for a timed task; `remindSecondsBefore` works only with a due time.

#### Complete Task

```bash
maton api -X PUT '/follow-up-boss/v1/tasks/{task_id}' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "isCompleted": true
}
JSON
```

**Note:** `{task_id}` stands for a real value; fill it in before sending the request.

### Notes

#### List Notes for a Person

```bash
maton api '/follow-up-boss/v1/notes?personId={person_id}&limit=10'
```

**Note:** `{person_id}` stands for a real value; fill it in before sending the request.

#### Get Note

```bash
maton api '/follow-up-boss/v1/notes/{note_id}'
```

**Note:** `{note_id}` stands for a real value; fill it in before sending the request.

#### Add Note

```bash
maton api -X POST '/follow-up-boss/v1/notes' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "personId": 1,
  "subject": "Showing feedback",
  "body": "Liked the kitchen; wants a bigger yard.",
  "isHtml": false
}
JSON
```

### Calls

#### List Calls

```bash
maton api '/follow-up-boss/v1/calls?personId={person_id}&limit=10'
```

**Note:** `{person_id}` stands for a real value; fill it in before sending the request. Call logs carry phone numbers, durations, outcomes and notes.

### Text Messages

#### List Text Messages

```bash
maton api '/follow-up-boss/v1/textMessages?personId={person_id}&limit=10'
```

**Note:** `{person_id}` stands for a real value; fill it in before sending the request.

A filter is required: without one of `personId`, `threadId`, `phone`, `toNumber`, `fromNumber`, `sharedInboxId`, `groupTextId`, `participants`, or an ID list, the request returns `400`. The response collection key is `textmessages` (lowercase). `POST /v1/textMessages` only records a text on the timeline; it never sends an SMS.

### Appointments

#### List Appointments

```bash
maton api '/follow-up-boss/v1/appointments?limit=10'
```

**Query parameters:** `personId`, `userId`, `start`, `end`, `limit`, `offset`.

**Example:**

```bash
maton api '/follow-up-boss/v1/appointments?personId={person_id}&limit=5'
```

**Note:** `{person_id}` stands for a real value; fill it in before sending the request.

#### List Appointment Types and Outcomes

```bash
maton api '/follow-up-boss/v1/appointmentTypes'
maton api '/follow-up-boss/v1/appointmentOutcomes'
```

#### Create Appointment

> **Can notify the lead.** With `sendInvitation=true`, invitees get an email invitation (and an SMS reminder if reminders are on). Leave it off unless the user asks for the invitation to be sent.

```bash
maton api -X POST '/follow-up-boss/v1/appointments' -H 'Content-Type: application/json' --input - <<'JSON'
{
  "title": "Showing: 123 Main St",
  "start": "2026-02-03T18:00:00Z",
  "end": "2026-02-03T19:00:00Z",
  "location": "123 Main St",
  "invitees": [{"personId": 1}, {"userId": 1}]
}
JSON
```

`title`, `start`, and `end` (UTC, or with a timezone offset) are required; `typeId` and `outcomeId` come from the endpoints above. `invitees` lists people (`personId`) and users (`userId`); appointments sync to an external calendar only when a user with a synced calendar is invited.

### Users

#### List Users

```bash
maton api '/follow-up-boss/v1/users?limit=10'
```

#### Get User

```bash
maton api '/follow-up-boss/v1/users/{user_id}'
```

**Note:** `{user_id}` stands for a real value; fill it in before sending the request.

### Other Read Endpoints

```bash
maton api '/follow-up-boss/v1/smartLists?limit=10'
maton api '/follow-up-boss/v1/customFields'
maton api '/follow-up-boss/v1/actionPlans?limit=10'
maton api '/follow-up-boss/v1/groups?limit=10'
maton api '/follow-up-boss/v1/teams'
maton api '/follow-up-boss/v1/templates?limit=10'
```

### Webhooks

```bash
maton api '/follow-up-boss/v1/webhooks'
```

Follow Up Boss webhooks (`POST /v1/webhooks` with `event`, e.g. `peopleCreated`, and an `https` `url`) can only be created by the account owner through a **registered system** (`X-System` / `X-System-Key` headers) and belong to that system. Through Maton the request carries Maton's system identity, so listing shows the webhooks registered for it; creating, updating, or deleting webhooks through Maton is not verified and is not part of this reference. For event-driven work, use a Maton trigger instead.

### Pagination

List endpoints return a `_metadata` object with `offset`, `limit`, `total`, `next`, and `nextLink`. Pass `limit` (max 100) with `offset`, or pass `next` from the previous response for deep pages:

```bash
maton api '/follow-up-boss/v1/people?limit=100'
maton api '/follow-up-boss/v1/people?limit=100&next={cursor}'
```

**Note:** `{cursor}` stands for a real value; fill it in before sending the request.

### Notes

- IDs are integers.
- Timestamps are ISO 8601 (UTC).
- Collection keys are sometimes lowercase (`textmessages`, `appointmenttypes`, `smartlists`, `customfields`).
- Custom person fields use their `custom...` name (e.g. `customClosingDate`); `fields=allFields` returns them.
- Rate limits are per context over a sliding 10-second window: Follow Up Boss documents 125 requests per 10 seconds globally for requests without a registered system key (250 with one), 10 per 10 seconds for `GET /v1/events` (20 with one), and 25 for `PUT /v1/people`. Requests through Maton carry Maton's system headers, so the limits that apply can be higher; read `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Window`, and `X-RateLimit-Context` on each response, and on `429` wait for `Retry-After`.
- `GET /v1/me` returns `403` through Maton; use `/v1/identity`.

### Resources

- [Follow Up Boss API Reference](https://docs.followupboss.com/reference)
- [People](https://docs.followupboss.com/reference/people-get)
- [Events](https://docs.followupboss.com/reference/events-post)
- [Deals](https://docs.followupboss.com/reference/deals-get)
- [Tasks](https://docs.followupboss.com/reference/tasks-get)
- [Notes](https://docs.followupboss.com/reference/notes-post)
- [Text Messages](https://docs.followupboss.com/reference/textmessages-get)
- [Rate Limiting](https://docs.followupboss.com/reference/rate-limiting)
- [Maton CLI Manual](https://cli.maton.ai/manual)
