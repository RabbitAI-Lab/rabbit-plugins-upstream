---
name: google-calendar
description: "Google Calendar: create, update, delete events. Natural language quick-add. Recurring events, Google Meet, attendees. Check free/busy availability. Use when an agent needs google calendar, scheduling meetings with attendees, checking calendar availability before booking, creating recurring events like weekly team standups, adding google meet links to virtual meetings, check availability, time min, time max through AgentPMT-hosted remote tool calls."
version: 1.0.0
homepage: https://www.agentpmt.com/marketplace/google-calendar
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/google-calendar"}}
---
# Google Calendar

## Freshness
Last updated: `2026-06-24`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Comprehensive Google Calendar integration tool that enables AI agents to manage calendar events and check availability on behalf of users. The tool supports all essential calendar operations including listing calendars and events, creating events with full details or natural language input, updating and deleting events, searching for events by text, and checking free/busy availability. Features include support for recurring events with flexible scheduling patterns, Google Meet video conference integration, attendee management with customizable notification settings, and timezone-aware scheduling. The tool handles both timed events and all-day events, supports custom reminders, and provides paginated results for calendars with many events.

## Product Instructions
### Google Calendar

Manage Google Calendar events, check availability, and organize schedules. Requires a Google OAuth connection with calendar permissions.

#### Actions

##### list_calendars
List all calendars the user has access to.

**Required:** None (uses defaults)

**Optional:**
- `calendar_id` (string) - Calendar ID; defaults to "primary"
- `max_results` (integer) - Max calendars to return, 1-250; default 50
- `page_token` (string) - Pagination token from a previous response

**Example:**
```json
{
  "action": "list_calendars"
}
```

---

##### list_events
List events from a calendar, optionally filtered by date range.

**Required:** None (defaults to upcoming events from now)

**Optional:**
- `calendar_id` (string) - Calendar ID; defaults to "primary"
- `time_min` (string) - Start of range in ISO 8601 (e.g., "2026-03-10T00:00:00Z"); defaults to current time
- `time_max` (string) - End of range in ISO 8601
- `max_results` (integer) - Max events to return, 1-250; default 50
- `page_token` (string) - Pagination token from a previous response

**Example:**
```json
{
  "action": "list_events",
  "time_min": "2026-03-10T00:00:00Z",
  "time_max": "2026-03-17T00:00:00Z"
}
```

---

##### get_event
Get full details of a specific event.

**Required:**
- `event_id` (string) - The event ID (obtained from list_events or search_events)

**Optional:**
- `calendar_id` (string) - Calendar ID; defaults to "primary"

**Example:**
```json
{
  "action": "get_event",
  "event_id": "abc123def456"
}
```

---

##### create_event
Create a new calendar event. Provide either timed or all-day date fields.

**Required:**
- `summary` (string) - Event title (max 1024 characters)
- Either timed event fields: `start_datetime` and `end_datetime` (ISO 8601 with timezone, e.g., "2026-03-15T14:00:00-05:00")
- Or all-day event fields: `start_date` and `end_date` (YYYY-MM-DD format; end_date is exclusive, so use the day after for single-day events)

**Optional:**
- `calendar_id` (string) - Calendar ID; defaults to "primary"
- `description` (string) - Event description or notes
- `location` (string) - Event location (address or place name)
- `timezone` (string) - IANA timezone (e.g., "America/New_York"); defaults to calendar timezone
- `attendees` (array) - List of attendees, each with:
  - `email` (string, required) - Attendee email
  - `display_name` (string) - Display name
  - `optional` (boolean) - Whether attendance is optional; default false
- `send_updates` (string) - Who gets email notifications: "all" (default), "externalOnly", or "none"
- `recurrence` (object) - Repeating event settings:
  - `frequency` (string, required) - "DAILY", "WEEKLY", "MONTHLY", or "YEARLY"
  - `interval` (integer) - Repeat every N units; default 1
  - `count` (integer) - Total number of occurrences
  - `until` (string) - End date for recurrence (YYYY-MM-DD or ISO 8601)
  - `by_day` (array) - Days of week for WEEKLY: ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
- `reminders` (array) - Custom reminders (only used when `use_default_reminders` is false), each with:
  - `method` (string) - "email" or "popup"; default "popup"
  - `minutes` (integer) - Minutes before event, 0-40320
- `use_default_reminders` (boolean) - Use calendar defaults; default true
- `add_video_conference` (boolean) - Add a Google Meet link; default false
- `visibility` (string) - "default", "public", "private", or "confidential"
- `show_as` (string) - "busy" or "free"

**Example - Timed event with attendees and Google Meet:**
```json
{
  "action": "create_event",
  "summary": "Weekly Team Sync",
  "start_datetime": "2026-03-15T10:00:00-05:00",
  "end_datetime": "2026-03-15T10:30:00-05:00",
  "location": "Conference Room A",
  "description": "Weekly team sync to review project progress",
  "attendees": [
    {"email": "alice@example.com"},
    {"email": "bob@example.com", "optional": true}
  ],
  "add_video_conference": true,
  "recurrence": {
    "frequency": "WEEKLY",
    "by_day": ["MO"],
    "count": 12
  }
}
```

**Example - All-day event:**
```json
{
  "action": "create_event",
  "summary": "Company Holiday",
  "start_date": "2026-07-04",
  "end_date": "2026-07-05",
  "show_as": "free"
}
```

---

##### quick_add
Create an event from a natural language description. Google Calendar parses the text to extract the event title, date, and time.

**Required:**
- `text` (string) - Natural language event description

**Optional:**
- `calendar_id` (string) - Calendar ID; defaults to "primary"
- `send_updates` (string) - Who gets notifications: "all" (default), "externalOnly", or "none"

**Example:**
```json
{
  "action": "quick_add",
  "text": "Lunch with Sarah tomorrow at noon at Cafe Milano"
}
```

---

##### update_event
Update an existing event. Only the fields you provide will be changed; all other fields remain as-is.

**Required:**
- `event_id` (string) - The event ID to update

**Optional (provide any fields to change):**
- `calendar_id` (string) - Calendar ID; defaults to "primary"
- `summary` (string) - New event title
- `description` (string) - New description
- `location` (string) - New location
- `start_datetime` / `end_datetime` (string) - New times (must provide both)
- `start_date` / `end_date` (string) - New all-day dates (must provide both)
- `timezone` (string) - IANA timezone
- `attendees` (array) - Updated attendee list (replaces existing)
- `recurrence` (object) - Updated recurrence settings (requires frequency)
- `reminders` (array) - Updated reminders
- `add_video_conference` (boolean) - Add Google Meet link
- `visibility` (string) - Updated visibility
- `show_as` (string) - Updated availability display
- `send_updates` (string) - Who gets notifications: "all" (default), "externalOnly", or "none"

**Example:**
```json
{
  "action": "update_event",
  "event_id": "abc123def456",
  "summary": "Updated Meeting Title",
  "location": "Room B instead",
  "start_datetime": "2026-03-15T11:00:00-05:00",
  "end_datetime": "2026-03-15T11:30:00-05:00"
}
```

---

##### delete_event
Delete an event from the calendar.

**Required:**
- `event_id` (string) - The event ID to delete

**Optional:**
- `calendar_id` (string) - Calendar ID; defaults to "primary"
- `send_updates` (string) - Who gets cancellation notifications: "all" (default), "externalOnly", or "none"

**Example:**
```json
{
  "action": "delete_event",
  "event_id": "abc123def456",
  "send_updates": "none"
}
```

---

##### search_events
Search for events by text. Searches event title, description, location, and attendees.

**Required:**
- `query` (string) - Search text

**Optional:**
- `calendar_id` (string) - Calendar ID; defaults to "primary"
- `time_min` (string) - Start of search range in ISO 8601; defaults to current time
- `time_max` (string) - End of search range in ISO 8601
- `max_results` (integer) - Max events to return, 1-250; default 50
- `page_token` (string) - Pagination token

**Example:**
```json
{
  "action": "search_events",
  "query": "budget review",
  "time_min": "2026-01-01T00:00:00Z",
  "time_max": "2026-12-31T23:59:59Z"
}
```

---

##### check_availability
Check free/busy times across one or more calendars. Returns busy periods and available time slots, with common free slots calculated when checking multiple calendars.

**Required:**
- `time_min` (string) - Start of range in ISO 8601
- `time_max` (string) - End of range in ISO 8601

**Optional:**
- `calendar_id` (string) - Calendar ID; defaults to "primary" (used when check_calendars is not provided)
- `check_calendars` (array of strings) - Multiple calendar IDs to check
- `attendee_emails` (array of strings) - Email addresses to check availability for (requires domain access)
- `timezone` (string) - IANA timezone for the query

**Example:**
```json
{
  "action": "check_availability",
  "time_min": "2026-03-15T08:00:00-05:00",
  "time_max": "2026-03-15T18:00:00-05:00",
  "check_calendars": ["primary", "team-calendar@group.calendar.google.com"],
  "attendee_emails": ["alice@example.com", "bob@example.com"]
}
```

#### Common Workflows

**Find a meeting time:** Use `check_availability` with attendee emails to find overlapping free slots, then `create_event` with the chosen time and those attendees.

**Reschedule an event:** Use `search_events` or `list_events` to find the event ID, then `update_event` with new times.

**Set up a recurring meeting:** Use `create_event` with `recurrence` to define frequency, days, and end conditions.

**View the week ahead:** Use `list_events` with `time_min` set to today and `time_max` set to 7 days out.

#### Important Notes

- All date/times use ISO 8601 format. Include timezone offsets for timed events (e.g., "2026-03-15T14:00:00-05:00").
- For all-day events, `end_date` is exclusive: a single-day event on March 15 uses start_date "2026-03-15" and end_date "2026-03-16".
- When updating attendees, the provided list replaces the existing attendees entirely.
- By default, email notifications are sent to all attendees for create, update, and delete actions. Set `send_updates` to "none" to suppress notifications.
- Event IDs are obtained from `list_events`, `search_events`, or the response of `create_event`.
- Use `calendar_id` of "primary" (the default) for the user's main calendar, or get other calendar IDs from `list_calendars`.
- The `recurrence` object requires `frequency` when provided. Use either `count` or `until` to limit recurrence, not both.

## When To Use
- Use this skill for `Google Calendar` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: google calendar, scheduling meetings with attendees, checking calendar availability before booking, creating recurring events like weekly team standups, adding google meet links to virtual meetings, check availability, time min, time max.
- Supported action names: `check_availability`, `create_event`, `delete_event`, `get_event`, `list_calendars`, `list_events`, `quick_add`, `search_events`, `update_event`.

## Use Cases
- Scheduling meetings with attendees
- Checking calendar availability before booking
- Creating recurring events like weekly team standups
- Adding Google Meet links to virtual meetings
- Finding events by searching for keywords
- Managing event details and locations
- Sending calendar invitations to external participants
- Viewing upcoming events for the day or week
- Canceling and rescheduling meetings with notifications
- Quick event creation from natural language descriptions

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `9`.
x402 availability: not enabled for this product.

- `check_availability` (action slug: `check-availability`): Check free/busy times across one or more calendars. Returns busy periods, free blocks, and common available time slots when checking multiple calendars. Price: `5` credits. Parameters: `attendee_emails`, `calendar_id`, `check_calendars`, `time_max`, `time_min`, `timezone`.
- `create_event` (action slug: `create-event`): Create a new calendar event. Provide either timed event fields (start_datetime/end_datetime) or all-day event fields (start_date/end_date). Price: `5` credits. Parameters: `add_video_conference`, `attendees`, `calendar_id`, `description`, `end_date`, `end_datetime`, `location`, `recurrence`, plus 9 more.
- `delete_event` (action slug: `delete-event`): Delete an event from the calendar. Price: `5` credits. Parameters: `calendar_id`, `event_id`, `send_updates`.
- `get_event` (action slug: `get-event`): Get full details of a specific calendar event. Price: `5` credits. Parameters: `calendar_id`, `event_id`.
- `list_calendars` (action slug: `list-calendars`): List all calendars the user has access to. Price: `5` credits. Parameters: `calendar_id`, `max_results`, `page_token`.
- `list_events` (action slug: `list-events`): List events from a calendar within an optional date range. Defaults to upcoming events from the current time. Price: `5` credits. Parameters: `calendar_id`, `max_results`, `page_token`, `time_max`, `time_min`.
- `quick_add` (action slug: `quick-add`): Create an event from a natural language description. Google Calendar parses the text to extract event title, date, and time. Price: `5` credits. Parameters: `calendar_id`, `send_updates`, `text`.
- `search_events` (action slug: `search-events`): Search for events by text. Searches event title, description, location, and attendees. Price: `5` credits. Parameters: `calendar_id`, `max_results`, `page_token`, `query`, `time_max`, `time_min`.
- `update_event` (action slug: `update-event`): Update an existing event. Only provided fields will be changed; all other fields remain as-is. The existing event is fetched first, then the provided fields are merged. Price: `5` credits. Parameters: `add_video_conference`, `attendees`, `calendar_id`, `description`, `end_date`, `end_datetime`, `event_id`, `location`, plus 9 more.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "google-calendar"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "google-calendar"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "google-calendar"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "google-calendar"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "google-calendar"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "google-calendar"
  }
}
```

## Call This Tool
Product slug: `google-calendar`

Marketplace page: https://www.agentpmt.com/marketplace/google-calendar

- AgentPMT account route: first use `../agentpmt-account-mcp-rest-api-setup` to connect the main MCP server or REST API for an Agent Group where this tool is enabled.
- x402 route: not enabled for this product.
- AgentPMT overview: use `../what-is-agentpmt` for marketplace, Agent Group, workflow, MCP, REST, and payment concepts.

If those setup skills are not installed beside this product skill, use the downloads below.

Core AgentPMT setup skills:
- What AgentPMT is: ../what-is-agentpmt
  - ClawHub page: https://clawhub.ai/agentpmt/what-is-agentpmt
  - OpenClaw install: `openclaw skills install what-is-agentpmt`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup
  - ClawHub page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup
  - OpenClaw install: `openclaw skills install agentpmt-account-mcp-rest-api-setup`
  - skills.sh install: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`

skills.sh install script:

```bash
npx skills add AgentPMT/agent-skills --skill what-is-agentpmt
npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup
```

MCP call shape after the main AgentPMT MCP server is connected:

```json
{
  "method": "tools/call",
  "params": {
    "name": "Google-Calendar",
    "arguments": {
      "action": "check_availability",
      "attendee_emails": [
        "user@example.com"
      ],
      "calendar_id": "primary",
      "check_calendars": [
        "example check calendar"
      ],
      "time_max": "example time max",
      "time_min": "example time min",
      "timezone": "example timezone"
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "google-calendar",
  "parameters": {
    "action": "check_availability",
    "attendee_emails": [
      "user@example.com"
    ],
    "calendar_id": "primary",
    "check_calendars": [
      "example check calendar"
    ],
    "time_max": "example time max",
    "time_min": "example time min",
    "timezone": "example timezone"
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `check_availability` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/google-calendar
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
