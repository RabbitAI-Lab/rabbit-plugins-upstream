# Google Meet Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `google-meet-connector`

x402 availability: not enabled for this product.

## `create_space`

Action slug: `create-space`

Price: `5` credits

Create a new Google Meet meeting space.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `config` | `object` | no | Space configuration |

Sample parameters:

```json
{
  "config": {
    "access_type": "OPEN",
    "entry_point_access": "ALL"
  }
}
```

Generated JSON parameter schema:

```json
{
  "config": {
    "description": "Space configuration",
    "properties": {
      "access_type": {
        "description": "OPEN (anyone joins), TRUSTED (org auto-join), RESTRICTED (invitees only)",
        "enum": [
          "OPEN",
          "TRUSTED",
          "RESTRICTED"
        ],
        "required": false,
        "type": "string"
      },
      "entry_point_access": {
        "description": "Who can use entry points to join: ALL or CREATOR_APP_ONLY",
        "enum": [
          "ALL",
          "CREATOR_APP_ONLY"
        ],
        "required": false,
        "type": "string"
      }
    },
    "required": false,
    "type": "object"
  }
}
```

## `end_conference`

Action slug: `end-conference`

Price: `5` credits

End the currently active conference in a space.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `space_name` | `string` | yes | Space resource name or meeting code |

Sample parameters:

```json
{
  "space_name": "example space name"
}
```

Generated JSON parameter schema:

```json
{
  "space_name": {
    "description": "Space resource name or meeting code",
    "required": true,
    "type": "string"
  }
}
```

## `get_conference_record`

Action slug: `get-conference-record`

Price: `5` credits

Get details of a specific conference record.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `conference_record_name` | `string` | yes | Conference record resource name (e.g. conferenceRecords/abc123) |

Sample parameters:

```json
{
  "conference_record_name": "example conference record name"
}
```

Generated JSON parameter schema:

```json
{
  "conference_record_name": {
    "description": "Conference record resource name (e.g. conferenceRecords/abc123)",
    "required": true,
    "type": "string"
  }
}
```

## `get_participant`

Action slug: `get-participant`

Price: `5` credits

Get details of a specific participant.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `participant_name` | `string` | yes | Participant resource name (e.g. conferenceRecords/abc/participants/xyz) |

Sample parameters:

```json
{
  "participant_name": "example participant name"
}
```

Generated JSON parameter schema:

```json
{
  "participant_name": {
    "description": "Participant resource name (e.g. conferenceRecords/abc/participants/xyz)",
    "required": true,
    "type": "string"
  }
}
```

## `get_recording`

Action slug: `get-recording`

Price: `5` credits

Get details of a specific recording.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `recording_name` | `string` | yes | Recording resource name (e.g. conferenceRecords/abc/recordings/xyz) |

Sample parameters:

```json
{
  "recording_name": "example recording name"
}
```

Generated JSON parameter schema:

```json
{
  "recording_name": {
    "description": "Recording resource name (e.g. conferenceRecords/abc/recordings/xyz)",
    "required": true,
    "type": "string"
  }
}
```

## `get_space`

Action slug: `get-space`

Price: `5` credits

Get details of an existing meeting space.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `space_name` | `string` | yes | Space resource name (e.g. spaces/abc123) or meeting code (e.g. abc-mnop-xyz) |

Sample parameters:

```json
{
  "space_name": "example space name"
}
```

Generated JSON parameter schema:

```json
{
  "space_name": {
    "description": "Space resource name (e.g. spaces/abc123) or meeting code (e.g. abc-mnop-xyz)",
    "required": true,
    "type": "string"
  }
}
```

## `get_transcript`

Action slug: `get-transcript`

Price: `5` credits

Get details of a specific transcript.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `transcript_name` | `string` | yes | Transcript resource name (e.g. conferenceRecords/abc/transcripts/xyz) |

Sample parameters:

```json
{
  "transcript_name": "example transcript name"
}
```

Generated JSON parameter schema:

```json
{
  "transcript_name": {
    "description": "Transcript resource name (e.g. conferenceRecords/abc/transcripts/xyz)",
    "required": true,
    "type": "string"
  }
}
```

## `list_conference_records`

Action slug: `list-conference-records`

Price: `5` credits

List conference records. Only returns conferences where the authenticated user is the organizer.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `filter` | `string` | no | Filter expression (e.g. space.name="spaces/abc123") |
| `page_size` | `integer` | no | Max results per page (1-250, default 25) |
| `page_token` | `string` | no | Pagination token from previous response |

Sample parameters:

```json
{
  "filter": "example filter",
  "page_size": 25,
  "page_token": "example page token"
}
```

Generated JSON parameter schema:

```json
{
  "filter": {
    "description": "Filter expression (e.g. space.name=\"spaces/abc123\")",
    "required": false,
    "type": "string"
  },
  "page_size": {
    "default": 25,
    "description": "Max results per page (1-250, default 25)",
    "maximum": 250,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token from previous response",
    "required": false,
    "type": "string"
  }
}
```

## `list_participant_sessions`

Action slug: `list-participant-sessions`

Price: `5` credits

List individual join/leave sessions for a participant.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `page_size` | `integer` | no | Max results per page (1-250, default 25) |
| `page_token` | `string` | no | Pagination token |
| `participant_name` | `string` | yes | Participant resource name |

Sample parameters:

```json
{
  "page_size": 25,
  "page_token": "example page token",
  "participant_name": "example participant name"
}
```

Generated JSON parameter schema:

```json
{
  "page_size": {
    "default": 25,
    "description": "Max results per page (1-250, default 25)",
    "maximum": 250,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token",
    "required": false,
    "type": "string"
  },
  "participant_name": {
    "description": "Participant resource name",
    "required": true,
    "type": "string"
  }
}
```

## `list_participants`

Action slug: `list-participants`

Price: `5` credits

List participants in a conference.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `conference_record_name` | `string` | yes | Conference record resource name |
| `filter` | `string` | no | Filter by earliest_start_time or latest_end_time |
| `page_size` | `integer` | no | Max results per page (1-250, default 25) |
| `page_token` | `string` | no | Pagination token |

Sample parameters:

```json
{
  "conference_record_name": "example conference record name",
  "filter": "example filter",
  "page_size": 25,
  "page_token": "example page token"
}
```

Generated JSON parameter schema:

```json
{
  "conference_record_name": {
    "description": "Conference record resource name",
    "required": true,
    "type": "string"
  },
  "filter": {
    "description": "Filter by earliest_start_time or latest_end_time",
    "required": false,
    "type": "string"
  },
  "page_size": {
    "default": 25,
    "description": "Max results per page (1-250, default 25)",
    "maximum": 250,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token",
    "required": false,
    "type": "string"
  }
}
```

## `list_recordings`

Action slug: `list-recordings`

Price: `5` credits

List recordings for a conference.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `conference_record_name` | `string` | yes | Conference record resource name |
| `page_size` | `integer` | no | Max results per page (1-250, default 25) |
| `page_token` | `string` | no | Pagination token |

Sample parameters:

```json
{
  "conference_record_name": "example conference record name",
  "page_size": 25,
  "page_token": "example page token"
}
```

Generated JSON parameter schema:

```json
{
  "conference_record_name": {
    "description": "Conference record resource name",
    "required": true,
    "type": "string"
  },
  "page_size": {
    "default": 25,
    "description": "Max results per page (1-250, default 25)",
    "maximum": 250,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token",
    "required": false,
    "type": "string"
  }
}
```

## `list_transcript_entries`

Action slug: `list-transcript-entries`

Price: `5` credits

List individual spoken entries within a transcript with speaker, text, language, and timestamps.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `page_size` | `integer` | no | Max results per page (1-250, default 25) |
| `page_token` | `string` | no | Pagination token |
| `transcript_name` | `string` | yes | Transcript resource name |

Sample parameters:

```json
{
  "page_size": 25,
  "page_token": "example page token",
  "transcript_name": "example transcript name"
}
```

Generated JSON parameter schema:

```json
{
  "page_size": {
    "default": 25,
    "description": "Max results per page (1-250, default 25)",
    "maximum": 250,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token",
    "required": false,
    "type": "string"
  },
  "transcript_name": {
    "description": "Transcript resource name",
    "required": true,
    "type": "string"
  }
}
```

## `list_transcripts`

Action slug: `list-transcripts`

Price: `5` credits

List transcripts for a conference.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `conference_record_name` | `string` | yes | Conference record resource name |
| `page_size` | `integer` | no | Max results per page (1-250, default 25) |
| `page_token` | `string` | no | Pagination token |

Sample parameters:

```json
{
  "conference_record_name": "example conference record name",
  "page_size": 25,
  "page_token": "example page token"
}
```

Generated JSON parameter schema:

```json
{
  "conference_record_name": {
    "description": "Conference record resource name",
    "required": true,
    "type": "string"
  },
  "page_size": {
    "default": 25,
    "description": "Max results per page (1-250, default 25)",
    "maximum": 250,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "page_token": {
    "description": "Pagination token",
    "required": false,
    "type": "string"
  }
}
```

## `update_space`

Action slug: `update-space`

Price: `5` credits

Update configuration of an existing meeting space.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `config` | `object` | no | Updated space configuration |
| `space_name` | `string` | yes | Space resource name or meeting code |

Sample parameters:

```json
{
  "config": {
    "access_type": "OPEN",
    "entry_point_access": "ALL"
  },
  "space_name": "example space name"
}
```

Generated JSON parameter schema:

```json
{
  "config": {
    "description": "Updated space configuration",
    "properties": {
      "access_type": {
        "description": "OPEN, TRUSTED, or RESTRICTED",
        "enum": [
          "OPEN",
          "TRUSTED",
          "RESTRICTED"
        ],
        "required": false,
        "type": "string"
      },
      "entry_point_access": {
        "description": "ALL or CREATOR_APP_ONLY",
        "enum": [
          "ALL",
          "CREATOR_APP_ONLY"
        ],
        "required": false,
        "type": "string"
      }
    },
    "required": false,
    "type": "object"
  },
  "space_name": {
    "description": "Space resource name or meeting code",
    "required": true,
    "type": "string"
  }
}
```
