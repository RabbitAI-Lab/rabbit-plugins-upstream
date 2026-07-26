# Google Calendar Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `google-calendar`

x402 availability: not enabled for this product.

## `check_availability`

Action slug: `check-availability`

Price: `5` credits

Check free/busy times across one or more calendars. Returns busy periods, free blocks, and common available time slots when checking multiple calendars.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `attendee_emails` | `array` | no | Email addresses to check availability for (requires domain access). |
| `calendar_id` | `string` | no | Calendar ID; used when check_calendars is not provided. Defaults to 'primary'. |
| `check_calendars` | `array` | no | Multiple calendar IDs to check availability across. |
| `time_max` | `string` | yes | End of range in ISO 8601 format. |
| `time_min` | `string` | yes | Start of range in ISO 8601 format. |
| `timezone` | `string` | no | IANA timezone for the query. |

Sample parameters:

```json
{
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
```

Generated JSON parameter schema:

```json
{
  "attendee_emails": {
    "description": "Email addresses to check availability for (requires domain access).",
    "items": {
      "format": "email",
      "type": "string"
    },
    "required": false,
    "type": "array"
  },
  "calendar_id": {
    "default": "primary",
    "description": "Calendar ID; used when check_calendars is not provided. Defaults to 'primary'.",
    "required": false,
    "type": "string"
  },
  "check_calendars": {
    "description": "Multiple calendar IDs to check availability across.",
    "items": {
      "type": "string"
    },
    "required": false,
    "type": "array"
  },
  "time_max": {
    "description": "End of range in ISO 8601 format.",
    "required": true,
    "type": "string"
  },
  "time_min": {
    "description": "Start of range in ISO 8601 format.",
    "required": true,
    "type": "string"
  },
  "timezone": {
    "description": "IANA timezone for the query.",
    "required": false,
    "type": "string"
  }
}
```

## `create_event`

Action slug: `create-event`

Price: `5` credits

Create a new calendar event. Provide either timed event fields (start_datetime/end_datetime) or all-day event fields (start_date/end_date).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `add_video_conference` | `boolean` | no | Automatically add a Google Meet link to the event. |
| `attendees` | `array` | no | List of attendees to invite to the event. |
| `calendar_id` | `string` | no | Calendar ID to create the event in. Defaults to 'primary'. |
| `description` | `string` | no | Event description or notes. |
| `end_date` | `string` | no | All-day event end date in YYYY-MM-DD format (exclusive - use day after for single-day events). Required for all-day events. |
| `end_datetime` | `string` | no | Event end time in ISO 8601 format with timezone. Required for timed events. |
| `location` | `string` | no | Event location (address or place name). |
| `recurrence` | `object` | no | Recurrence settings for repeating events. |
| `reminders` | `array` | no | Custom reminder settings (only used when use_default_reminders is false). |
| `send_updates` | `string` | no | Who to send email notifications to. |
| `show_as` | `string` | no | How the event appears in free/busy queries. |
| `start_date` | `string` | no | All-day event start date in YYYY-MM-DD format. Required for all-day events. |
| `start_datetime` | `string` | no | Event start time in ISO 8601 format with timezone (e.g., '2026-03-15T14:00:00-05:00'). Required for timed events. |
| `summary` | `string` | yes | Event title (max 1024 characters). |
| `timezone` | `string` | no | IANA timezone (e.g., 'America/New_York'). Defaults to calendar timezone when omitted. |
| `use_default_reminders` | `boolean` | no | Use calendar's default reminders instead of custom ones. |
| `visibility` | `string` | no | Event visibility setting. |

Sample parameters:

```json
{
  "add_video_conference": false,
  "attendees": [
    {
      "display_name": "example display name",
      "email": "user@example.com",
      "optional": false
    }
  ],
  "calendar_id": "primary",
  "description": "example description",
  "end_date": "example end date",
  "end_datetime": "example end datetime",
  "location": "example location",
  "recurrence": {
    "by_day": [
      "MO"
    ],
    "count": 1,
    "frequency": "DAILY",
    "interval": 1,
    "until": "example until"
  }
}
```

Generated JSON parameter schema:

```json
{
  "add_video_conference": {
    "default": false,
    "description": "Automatically add a Google Meet link to the event.",
    "required": false,
    "type": "boolean"
  },
  "attendees": {
    "description": "List of attendees to invite to the event.",
    "items": {
      "properties": {
        "display_name": {
          "description": "Attendee display name.",
          "required": false,
          "type": "string"
        },
        "email": {
          "description": "Attendee email address.",
          "required": true,
          "type": "string"
        },
        "optional": {
          "default": false,
          "description": "Whether attendance is optional.",
          "required": false,
          "type": "boolean"
        }
      },
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "calendar_id": {
    "default": "primary",
    "description": "Calendar ID to create the event in. Defaults to 'primary'.",
    "required": false,
    "type": "string"
  },
  "description": {
    "description": "Event description or notes.",
    "required": false,
    "type": "string"
  },
  "end_date": {
    "description": "All-day event end date in YYYY-MM-DD format (exclusive - use day after for single-day events). Required for all-day events.",
    "required": false,
    "type": "string"
  },
  "end_datetime": {
    "description": "Event end time in ISO 8601 format with timezone. Required for timed events.",
    "required": false,
    "type": "string"
  },
  "location": {
    "description": "Event location (address or place name).",
    "required": false,
    "type": "string"
  },
  "recurrence": {
    "description": "Recurrence settings for repeating events.",
    "properties": {
      "by_day": {
        "description": "Days of week for WEEKLY frequency.",
        "items": {
          "enum": [
            "MO",
            "TU",
            "WE",
            "TH",
            "FR",
            "SA",
            "SU"
          ],
          "type": "string"
        },
        "required": false,
        "type": "array"
      },
      "count": {
        "description": "Total number of occurrences.",
        "minimum": 1,
        "required": false,
        "type": "integer"
      },
      "frequency": {
        "description": "How often the event repeats. Required when recurrence is provided.",
        "enum": [
          "DAILY",
          "WEEKLY",
          "MONTHLY",
          "YEARLY"
        ],
        "required": true,
        "type": "string"
      },
      "interval": {
        "default": 1,
        "description": "Repeat every N frequency units.",
        "minimum": 1,
        "required": false,
        "type": "integer"
      },
      "until": {
        "description": "End date for recurrence (YYYY-MM-DD or ISO 8601).",
        "required": false,
        "type": "string"
      }
    },
    "required": false,
    "type": "object"
  },
  "reminders": {
    "description": "Custom reminder settings (only used when use_default_reminders is false).",
    "items": {
      "properties": {
        "method": {
          "default": "popup",
          "description": "How to deliver the reminder.",
          "enum": [
            "email",
            "popup"
          ],
          "required": false,
          "type": "string"
        },
        "minutes": {
          "description": "Minutes before event to trigger reminder (0-40320).",
          "maximum": 40320,
          "minimum": 0,
          "required": true,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "send_updates": {
    "default": "all",
    "description": "Who to send email notifications to.",
    "enum": [
      "all",
      "externalOnly",
      "none"
    ],
    "required": false,
    "type": "string"
  },
  "show_as": {
    "description": "How the event appears in free/busy queries.",
    "enum": [
      "busy",
      "free"
    ],
    "required": false,
    "type": "string"
  },
  "start_date": {
    "description": "All-day event start date in YYYY-MM-DD format. Required for all-day events.",
    "required": false,
    "type": "string"
  },
  "start_datetime": {
    "description": "Event start time in ISO 8601 format with timezone (e.g., '2026-03-15T14:00:00-05:00'). Required for timed events.",
    "required": false,
    "type": "string"
  },
  "summary": {
    "description": "Event title (max 1024 characters).",
    "maxLength": 1024,
    "required": true,
    "type": "string"
  },
  "timezone": {
    "description": "IANA timezone (e.g., 'America/New_York'). Defaults to calendar timezone when omitted.",
    "required": false,
    "type": "string"
  },
  "use_default_reminders": {
    "default": true,
    "description": "Use calendar's default reminders instead of custom ones.",
    "required": false,
    "type": "boolean"
  },
  "visibility": {
    "description": "Event visibility setting.",
    "enum": [
      "default",
      "public",
      "private",
      "confidential"
    ],
    "required": false,
    "type": "string"
  }
}
```

## `delete_event`

Action slug: `delete-event`

Price: `5` credits

Delete an event from the calendar.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `calendar_id` | `string` | no | Calendar ID containing the event. Defaults to 'primary'. |
| `event_id` | `string` | yes | Event ID to delete. |
| `send_updates` | `string` | no | Who to send cancellation notifications to. |

Sample parameters:

```json
{
  "calendar_id": "primary",
  "event_id": "example event id",
  "send_updates": "all"
}
```

Generated JSON parameter schema:

```json
{
  "calendar_id": {
    "default": "primary",
    "description": "Calendar ID containing the event. Defaults to 'primary'.",
    "required": false,
    "type": "string"
  },
  "event_id": {
    "description": "Event ID to delete.",
    "required": true,
    "type": "string"
  },
  "send_updates": {
    "default": "all",
    "description": "Who to send cancellation notifications to.",
    "enum": [
      "all",
      "externalOnly",
      "none"
    ],
    "required": false,
    "type": "string"
  }
}
```

## `get_event`

Action slug: `get-event`

Price: `5` credits

Get full details of a specific calendar event.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `calendar_id` | `string` | no | Calendar ID containing the event. Defaults to 'primary'. |
| `event_id` | `string` | yes | Event ID to retrieve. Obtain from list_events or search_events. |

Sample parameters:

```json
{
  "calendar_id": "primary",
  "event_id": "example event id"
}
```

Generated JSON parameter schema:

```json
{
  "calendar_id": {
    "default": "primary",
    "description": "Calendar ID containing the event. Defaults to 'primary'.",
    "required": false,
    "type": "string"
  },
  "event_id": {
    "description": "Event ID to retrieve. Obtain from list_events or search_events.",
    "required": true,
    "type": "string"
  }
}
```

## `list_calendars`

Action slug: `list-calendars`

Price: `5` credits

List all calendars the user has access to.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `calendar_id` | `string` | no | Calendar ID to operate on. Use 'primary' for the user's main calendar. |
| `max_results` | `integer` | no | Maximum number of calendars to return (1-250). |
| `page_token` | `string` | no | Token for fetching next page of results from a previous call. |

Sample parameters:

```json
{
  "calendar_id": "primary",
  "max_results": 50,
  "page_token": "example page token"
}
```

Generated JSON parameter schema:

```json
{
  "calendar_id": {
    "default": "primary",
    "description": "Calendar ID to operate on. Use 'primary' for the user's main calendar.",
    "required": false,
    "type": "string"
  },
  "max_results": {
    "default": 50,
    "description": "Maximum number of calendars to return (1-250).",
    "maximum": 250,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Token for fetching next page of results from a previous call.",
    "required": false,
    "type": "string"
  }
}
```

## `list_events`

Action slug: `list-events`

Price: `5` credits

List events from a calendar within an optional date range. Defaults to upcoming events from the current time.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `calendar_id` | `string` | no | Calendar ID to list events from. Defaults to 'primary'. |
| `max_results` | `integer` | no | Maximum number of events to return (1-250). |
| `page_token` | `string` | no | Token for fetching next page of results. |
| `time_max` | `string` | no | End of time range in ISO 8601 format. |
| `time_min` | `string` | no | Start of time range in ISO 8601 format (e.g., '2026-03-10T00:00:00Z'). Defaults to current time if omitted. |

Sample parameters:

```json
{
  "calendar_id": "primary",
  "max_results": 50,
  "page_token": "example page token",
  "time_max": "example time max",
  "time_min": "example time min"
}
```

Generated JSON parameter schema:

```json
{
  "calendar_id": {
    "default": "primary",
    "description": "Calendar ID to list events from. Defaults to 'primary'.",
    "required": false,
    "type": "string"
  },
  "max_results": {
    "default": 50,
    "description": "Maximum number of events to return (1-250).",
    "maximum": 250,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Token for fetching next page of results.",
    "required": false,
    "type": "string"
  },
  "time_max": {
    "description": "End of time range in ISO 8601 format.",
    "required": false,
    "type": "string"
  },
  "time_min": {
    "description": "Start of time range in ISO 8601 format (e.g., '2026-03-10T00:00:00Z'). Defaults to current time if omitted.",
    "required": false,
    "type": "string"
  }
}
```

## `quick_add`

Action slug: `quick-add`

Price: `5` credits

Create an event from a natural language description. Google Calendar parses the text to extract event title, date, and time.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `calendar_id` | `string` | no | Calendar ID to create the event in. Defaults to 'primary'. |
| `send_updates` | `string` | no | Who to send email notifications to. |
| `text` | `string` | yes | Natural language event description (e.g., 'Lunch with Sarah tomorrow at noon'). |

Sample parameters:

```json
{
  "calendar_id": "primary",
  "send_updates": "all",
  "text": "example text"
}
```

Generated JSON parameter schema:

```json
{
  "calendar_id": {
    "default": "primary",
    "description": "Calendar ID to create the event in. Defaults to 'primary'.",
    "required": false,
    "type": "string"
  },
  "send_updates": {
    "default": "all",
    "description": "Who to send email notifications to.",
    "enum": [
      "all",
      "externalOnly",
      "none"
    ],
    "required": false,
    "type": "string"
  },
  "text": {
    "description": "Natural language event description (e.g., 'Lunch with Sarah tomorrow at noon').",
    "required": true,
    "type": "string"
  }
}
```

## `search_events`

Action slug: `search-events`

Price: `5` credits

Search for events by text. Searches event title, description, location, and attendees.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `calendar_id` | `string` | no | Calendar ID to search in. Defaults to 'primary'. |
| `max_results` | `integer` | no | Maximum events to return (1-250). |
| `page_token` | `string` | no | Pagination token from a previous response. |
| `query` | `string` | yes | Search text to match against events. |
| `time_max` | `string` | no | End of search range in ISO 8601. |
| `time_min` | `string` | no | Start of search range in ISO 8601. Defaults to current time. |

Sample parameters:

```json
{
  "calendar_id": "primary",
  "max_results": 50,
  "page_token": "example page token",
  "query": "example search query",
  "time_max": "example time max",
  "time_min": "example time min"
}
```

Generated JSON parameter schema:

```json
{
  "calendar_id": {
    "default": "primary",
    "description": "Calendar ID to search in. Defaults to 'primary'.",
    "required": false,
    "type": "string"
  },
  "max_results": {
    "default": 50,
    "description": "Maximum events to return (1-250).",
    "maximum": 250,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token from a previous response.",
    "required": false,
    "type": "string"
  },
  "query": {
    "description": "Search text to match against events.",
    "required": true,
    "type": "string"
  },
  "time_max": {
    "description": "End of search range in ISO 8601.",
    "required": false,
    "type": "string"
  },
  "time_min": {
    "description": "Start of search range in ISO 8601. Defaults to current time.",
    "required": false,
    "type": "string"
  }
}
```

## `update_event`

Action slug: `update-event`

Price: `5` credits

Update an existing event. Only provided fields will be changed; all other fields remain as-is. The existing event is fetched first, then the provided fields are merged.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `add_video_conference` | `boolean` | no | Add a Google Meet link. |
| `attendees` | `array` | no | Updated attendee list (replaces existing attendees). |
| `calendar_id` | `string` | no | Calendar ID containing the event. Defaults to 'primary'. |
| `description` | `string` | no | New event description. |
| `end_date` | `string` | no | New all-day end date YYYY-MM-DD (must provide start_date too). |
| `end_datetime` | `string` | no | New end time in ISO 8601 (must provide start_datetime too). |
| `event_id` | `string` | yes | Event ID to update. |
| `location` | `string` | no | New event location. |
| `recurrence` | `object` | no | Updated recurrence settings. |
| `reminders` | `array` | no | Updated custom reminders. |
| `send_updates` | `string` | no | Who to send notification emails to. |
| `show_as` | `string` | no | Updated availability display. |
| `start_date` | `string` | no | New all-day start date YYYY-MM-DD (must provide end_date too). |
| `start_datetime` | `string` | no | New start time in ISO 8601 (must provide end_datetime too). |
| `summary` | `string` | no | New event title. |
| `timezone` | `string` | no | IANA timezone for the updated times. |
| `visibility` | `string` | no | Updated visibility setting. |

Sample parameters:

```json
{
  "add_video_conference": false,
  "attendees": [
    {
      "display_name": "example display name",
      "email": "user@example.com",
      "optional": false
    }
  ],
  "calendar_id": "primary",
  "description": "example description",
  "end_date": "example end date",
  "end_datetime": "example end datetime",
  "event_id": "example event id",
  "location": "example location"
}
```

Generated JSON parameter schema:

```json
{
  "add_video_conference": {
    "default": false,
    "description": "Add a Google Meet link.",
    "required": false,
    "type": "boolean"
  },
  "attendees": {
    "description": "Updated attendee list (replaces existing attendees).",
    "items": {
      "properties": {
        "display_name": {
          "description": "Attendee display name.",
          "required": false,
          "type": "string"
        },
        "email": {
          "description": "Attendee email address.",
          "required": true,
          "type": "string"
        },
        "optional": {
          "default": false,
          "description": "Whether attendance is optional.",
          "required": false,
          "type": "boolean"
        }
      },
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "calendar_id": {
    "default": "primary",
    "description": "Calendar ID containing the event. Defaults to 'primary'.",
    "required": false,
    "type": "string"
  },
  "description": {
    "description": "New event description.",
    "required": false,
    "type": "string"
  },
  "end_date": {
    "description": "New all-day end date YYYY-MM-DD (must provide start_date too).",
    "required": false,
    "type": "string"
  },
  "end_datetime": {
    "description": "New end time in ISO 8601 (must provide start_datetime too).",
    "required": false,
    "type": "string"
  },
  "event_id": {
    "description": "Event ID to update.",
    "required": true,
    "type": "string"
  },
  "location": {
    "description": "New event location.",
    "required": false,
    "type": "string"
  },
  "recurrence": {
    "description": "Updated recurrence settings.",
    "properties": {
      "by_day": {
        "description": "Days of week for WEEKLY frequency.",
        "items": {
          "enum": [
            "MO",
            "TU",
            "WE",
            "TH",
            "FR",
            "SA",
            "SU"
          ],
          "type": "string"
        },
        "required": false,
        "type": "array"
      },
      "count": {
        "description": "Total number of occurrences.",
        "minimum": 1,
        "required": false,
        "type": "integer"
      },
      "frequency": {
        "description": "How often the event repeats. Required when recurrence is provided.",
        "enum": [
          "DAILY",
          "WEEKLY",
          "MONTHLY",
          "YEARLY"
        ],
        "required": true,
        "type": "string"
      },
      "interval": {
        "default": 1,
        "description": "Repeat every N frequency units.",
        "minimum": 1,
        "required": false,
        "type": "integer"
      },
      "until": {
        "description": "End date for recurrence.",
        "required": false,
        "type": "string"
      }
    },
    "required": false,
    "type": "object"
  },
  "reminders": {
    "description": "Updated custom reminders.",
    "items": {
      "properties": {
        "method": {
          "default": "popup",
          "description": "Reminder delivery method.",
          "enum": [
            "email",
            "popup"
          ],
          "required": false,
          "type": "string"
        },
        "minutes": {
          "description": "Minutes before event (0-40320).",
          "maximum": 40320,
          "minimum": 0,
          "required": true,
          "type": "integer"
        }
      },
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "send_updates": {
    "default": "all",
    "description": "Who to send notification emails to.",
    "enum": [
      "all",
      "externalOnly",
      "none"
    ],
    "required": false,
    "type": "string"
  },
  "show_as": {
    "description": "Updated availability display.",
    "enum": [
      "busy",
      "free"
    ],
    "required": false,
    "type": "string"
  },
  "start_date": {
    "description": "New all-day start date YYYY-MM-DD (must provide end_date too).",
    "required": false,
    "type": "string"
  },
  "start_datetime": {
    "description": "New start time in ISO 8601 (must provide end_datetime too).",
    "required": false,
    "type": "string"
  },
  "summary": {
    "description": "New event title.",
    "maxLength": 1024,
    "required": false,
    "type": "string"
  },
  "timezone": {
    "description": "IANA timezone for the updated times.",
    "required": false,
    "type": "string"
  },
  "visibility": {
    "description": "Updated visibility setting.",
    "enum": [
      "default",
      "public",
      "private",
      "confidential"
    ],
    "required": false,
    "type": "string"
  }
}
```
