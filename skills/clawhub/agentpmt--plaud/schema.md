# Plaud Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `plaud`

x402 availability: not enabled for this product.

## `get_current_user`

Action slug: `get-current-user`

Price: `5` credits

Get current authenticated user info

Parameters:

This action does not require parameters.

Sample parameters:

```json
{}
```

Generated JSON parameter schema:

```json
{}
```

## `get_file`

Action slug: `get-file`

Price: `5` credits

Get details of a specific Plaud recording by ID

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | The file ID to retrieve |

Sample parameters:

```json
{
  "file_id": "example file id"
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "The file ID to retrieve",
    "required": false,
    "type": "string"
  }
}
```

## `get_note`

Action slug: `get-note`

Price: `5` credits

Fetch AI-generated notes for a Plaud recording — compact summary, action items, and key topics

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | The file ID to retrieve notes for |

Sample parameters:

```json
{
  "file_id": "example file id"
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "The file ID to retrieve notes for",
    "required": false,
    "type": "string"
  }
}
```

## `get_transcript`

Action slug: `get-transcript`

Price: `5` credits

Fetch the full timestamped transcript with speaker attribution for a Plaud recording

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `file_id` | `string` | no | The file ID to retrieve transcript for |

Sample parameters:

```json
{
  "file_id": "example file id"
}
```

Generated JSON parameter schema:

```json
{
  "file_id": {
    "description": "The file ID to retrieve transcript for",
    "required": false,
    "type": "string"
  }
}
```

## `list_files`

Action slug: `list-files`

Price: `5` credits

List Plaud recordings. Supports optional client-side filtering: `query` (case-insensitive name substring), `date_from`/`date_to` (YYYY-MM-DD, inclusive). When any filter is set, paginates up to 5 pages × 100 recordings and returns all matches.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `date_from` | `string` | no | Start date inclusive, YYYY-MM-DD |
| `date_to` | `string` | no | End date inclusive, YYYY-MM-DD |
| `page` | `number` | no | Page number (ignored when filters are set) |
| `page_size` | `number` | no | Items per page (ignored when filters are set) |
| `query` | `string` | no | Case-insensitive substring match on recording name |

Sample parameters:

```json
{
  "date_from": "example date from",
  "date_to": "example date to",
  "page": 1,
  "page_size": 20,
  "query": "example search query"
}
```

Generated JSON parameter schema:

```json
{
  "date_from": {
    "description": "Start date inclusive, YYYY-MM-DD",
    "required": false,
    "type": "string"
  },
  "date_to": {
    "description": "End date inclusive, YYYY-MM-DD",
    "required": false,
    "type": "string"
  },
  "page": {
    "default": 1,
    "description": "Page number (ignored when filters are set)",
    "required": false,
    "type": "number"
  },
  "page_size": {
    "default": 20,
    "description": "Items per page (ignored when filters are set)",
    "required": false,
    "type": "number"
  },
  "query": {
    "description": "Case-insensitive substring match on recording name",
    "required": false,
    "type": "string"
  }
}
```
