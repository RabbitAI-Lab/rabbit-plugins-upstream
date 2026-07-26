# Google Sheets Schema

This generated reference belongs to the adjacent `SKILL.md`. Use it for exact action names, action slugs, parameter summaries, sample parameters, and generated JSON parameter schemas.

Product slug: `google-sheets-api`

x402 availability: not enabled for this product.

## `add_conditional_formatting`

Action slug: `add-conditional-formatting`

Price: `5` credits

Add a conditional formatting rule to a range.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `range` | `string` | yes | A1 range for the rule. |
| `rule` | `object` | yes | Sheets ConditionalFormatRule object; ranges can be omitted. |
| `sheet_name` | `string` | no | Optional tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "range": "example range",
  "rule": {},
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "range": {
    "description": "A1 range for the rule.",
    "required": true,
    "type": "string"
  },
  "rule": {
    "description": "Sheets ConditionalFormatRule object; ranges can be omitted.",
    "required": true,
    "type": "object"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `add_named_range`

Action slug: `add-named-range`

Price: `5` credits

Create a named range.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | yes | Named range name. |
| `range` | `string` | yes | A1 range. |
| `sheet_name` | `string` | no | Optional tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "name": "example name",
  "range": "example range",
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "name": {
    "description": "Named range name.",
    "required": true,
    "type": "string"
  },
  "range": {
    "description": "A1 range.",
    "required": true,
    "type": "string"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `add_sheet`

Action slug: `add-sheet`

Price: `5` credits

Add a new tab to a spreadsheet.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `new_sheet_name` | `string` | yes | New tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "new_sheet_name": "example new sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "new_sheet_name": {
    "description": "New tab name.",
    "required": true,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `append_column`

Action slug: `append-column`

Price: `5` credits

Append one new column immediately after the last non-empty data column and write its header and values.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `column_name` | `string` | yes | New column header. |
| `column_values` | `array` | yes | Values to write below the header at the data table edge. |
| `sheet_name` | `string` | no | Optional tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "column_name": "example column name",
  "column_values": [
    "example column value"
  ],
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "column_name": {
    "description": "New column header.",
    "required": true,
    "type": "string"
  },
  "column_values": {
    "description": "Values to write below the header at the data table edge.",
    "items": {
      "type": "string"
    },
    "required": true,
    "type": "array"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `append_rows`

Action slug: `append-rows`

Price: `5` credits

Append rows at the true table end. Object rows are mapped by sheet headers.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `header_row` | `integer` | no | One-based header row, default 1. |
| `rows` | `array` | yes | Rows as arrays or objects keyed by headers. |
| `sheet_name` | `string` | no | Optional tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |
| `value_input_option` | `string` | no | USER_ENTERED or RAW. |

Sample parameters:

```json
{
  "header_row": 1,
  "rows": [
    {}
  ],
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id",
  "value_input_option": "example value input option"
}
```

Generated JSON parameter schema:

```json
{
  "header_row": {
    "description": "One-based header row, default 1.",
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "rows": {
    "description": "Rows as arrays or objects keyed by headers.",
    "items": {
      "type": "object"
    },
    "required": true,
    "type": "array"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  },
  "value_input_option": {
    "description": "USER_ENTERED or RAW.",
    "required": false,
    "type": "string"
  }
}
```

## `copy_paste`

Action slug: `copy-paste`

Price: `5` credits

Copy a source range to a destination range.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `destination_range` | `string` | yes | A1 destination range. |
| `paste_orientation` | `string` | no | NORMAL or TRANSPOSE. |
| `paste_type` | `string` | no | Sheets pasteType such as PASTE_NORMAL or PASTE_VALUES. |
| `sheet_name` | `string` | no | Optional tab name. |
| `source_range` | `string` | yes | A1 source range. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "destination_range": "example destination range",
  "paste_orientation": "example paste orientation",
  "paste_type": "example paste type",
  "sheet_name": "example sheet name",
  "source_range": "example source range",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "destination_range": {
    "description": "A1 destination range.",
    "required": true,
    "type": "string"
  },
  "paste_orientation": {
    "description": "NORMAL or TRANSPOSE.",
    "required": false,
    "type": "string"
  },
  "paste_type": {
    "description": "Sheets pasteType such as PASTE_NORMAL or PASTE_VALUES.",
    "required": false,
    "type": "string"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "source_range": {
    "description": "A1 source range.",
    "required": true,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `create`

Action slug: `create`

Price: `5` credits

Create a new spreadsheet, optionally with an initial tab, headers, and rows.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `initial_headers` | `array` | no | Optional first header row. |
| `initial_sheet_name` | `string` | no | Optional first tab name. |
| `rows` | `array` | no | Optional initial rows as arrays or objects keyed by headers. |
| `title` | `string` | yes | Spreadsheet title. |

Sample parameters:

```json
{
  "initial_headers": [
    "example initial header"
  ],
  "initial_sheet_name": "example initial sheet name",
  "rows": [
    {}
  ],
  "title": "example title"
}
```

Generated JSON parameter schema:

```json
{
  "initial_headers": {
    "description": "Optional first header row.",
    "items": {
      "type": "string"
    },
    "required": false,
    "type": "array"
  },
  "initial_sheet_name": {
    "description": "Optional first tab name.",
    "required": false,
    "type": "string"
  },
  "rows": {
    "description": "Optional initial rows as arrays or objects keyed by headers.",
    "items": {
      "type": "object"
    },
    "required": false,
    "type": "array"
  },
  "title": {
    "description": "Spreadsheet title.",
    "required": true,
    "type": "string"
  }
}
```

## `cut_paste`

Action slug: `cut-paste`

Price: `5` credits

Move a source range to a destination start cell.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `destination_range` | `string` | yes | A1 destination start cell. |
| `paste_type` | `string` | no | Sheets pasteType such as PASTE_NORMAL or PASTE_VALUES. |
| `sheet_name` | `string` | no | Optional tab name. |
| `source_range` | `string` | yes | A1 source range. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "destination_range": "example destination range",
  "paste_type": "example paste type",
  "sheet_name": "example sheet name",
  "source_range": "example source range",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "destination_range": {
    "description": "A1 destination start cell.",
    "required": true,
    "type": "string"
  },
  "paste_type": {
    "description": "Sheets pasteType such as PASTE_NORMAL or PASTE_VALUES.",
    "required": false,
    "type": "string"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "source_range": {
    "description": "A1 source range.",
    "required": true,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `delete_named_range`

Action slug: `delete-named-range`

Price: `5` credits

Delete a named range by id.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `named_range_id` | `string` | yes | Google namedRangeId to delete. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "named_range_id": "example named range id",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "named_range_id": {
    "description": "Google namedRangeId to delete.",
    "required": true,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `delete_sheet`

Action slug: `delete-sheet`

Price: `5` credits

Delete a tab by name, id, or index.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `sheet_id` | `integer` | no | Numeric sheet id. |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "sheet_id": {
    "description": "Numeric sheet id.",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `export_sheet`

Action slug: `export-sheet`

Price: `5` credits

Export a specific sheet or whole spreadsheet to File Manager as CSV, TSV, PDF, XLSX, ODS, HTML, or ZIP.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `expiration_days` | `integer` | no | File Manager expiration, 1-7 days. |
| `filename` | `string` | no | Optional stored filename. |
| `format` | `string` | yes | csv, tsv, pdf, xlsx, ods, html, or zip. |
| `range` | `string` | no | Optional range for CSV/TSV exports. |
| `sheet_id` | `integer` | no | Optional numeric sheet id. |
| `sheet_name` | `string` | no | Optional tab name for specific-sheet export. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "expiration_days": 1,
  "filename": "example filename",
  "format": "example format",
  "range": "example range",
  "sheet_id": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "expiration_days": {
    "description": "File Manager expiration, 1-7 days.",
    "maximum": 7,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "filename": {
    "description": "Optional stored filename.",
    "required": false,
    "type": "string"
  },
  "format": {
    "description": "csv, tsv, pdf, xlsx, ods, html, or zip.",
    "required": true,
    "type": "string"
  },
  "range": {
    "description": "Optional range for CSV/TSV exports.",
    "required": false,
    "type": "string"
  },
  "sheet_id": {
    "description": "Optional numeric sheet id.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Optional tab name for specific-sheet export.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `find_replace`

Action slug: `find-replace`

Price: `5` credits

Find and replace text across the spreadsheet or one sheet.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `find` | `string` | yes | Text or regex to find. |
| `match_case` | `boolean` | no | Case-sensitive match. |
| `match_entire_cell` | `boolean` | no | Match entire cell contents only. |
| `replacement` | `string` | yes | Replacement text. |
| `search_by_regex` | `boolean` | no | Treat find as regex. |
| `sheet_name` | `string` | no | Optional tab limit. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "find": "example find",
  "match_case": true,
  "match_entire_cell": true,
  "replacement": "example replacement",
  "search_by_regex": true,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "find": {
    "description": "Text or regex to find.",
    "required": true,
    "type": "string"
  },
  "match_case": {
    "description": "Case-sensitive match.",
    "required": false,
    "type": "boolean"
  },
  "match_entire_cell": {
    "description": "Match entire cell contents only.",
    "required": false,
    "type": "boolean"
  },
  "replacement": {
    "description": "Replacement text.",
    "required": true,
    "type": "string"
  },
  "search_by_regex": {
    "description": "Treat find as regex.",
    "required": false,
    "type": "boolean"
  },
  "sheet_name": {
    "description": "Optional tab limit.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `format_cells`

Action slug: `format-cells`

Price: `5` credits

Apply cell formatting or number format to a range.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `cell_format` | `object` | no | Text/background/alignment/wrap formatting. |
| `number_format` | `object` | no | Sheets numberFormat object. |
| `range` | `string` | yes | A1 range to format. |
| `sheet_name` | `string` | no | Optional tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "cell_format": {},
  "number_format": {},
  "range": "example range",
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "cell_format": {
    "description": "Text/background/alignment/wrap formatting.",
    "required": false,
    "type": "object"
  },
  "number_format": {
    "description": "Sheets numberFormat object.",
    "required": false,
    "type": "object"
  },
  "range": {
    "description": "A1 range to format.",
    "required": true,
    "type": "string"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `get_data_range`

Action slug: `get-data-range`

Price: `5` credits

Find the last non-empty row/column and recommended append start for a tab.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `range` | `string` | no | Optional A1 range to inspect. |
| `sheet_name` | `string` | no | Optional tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "range": "example range",
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "range": {
    "description": "Optional A1 range to inspect.",
    "required": false,
    "type": "string"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `get_headers`

Action slug: `get-headers`

Price: `5` credits

Read the header row and return header-to-column mappings plus duplicate diagnostics.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `header_row` | `integer` | no | One-based header row, default 1. |
| `sheet_name` | `string` | no | Optional tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "header_row": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "header_row": {
    "description": "One-based header row, default 1.",
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `list_sheets`

Action slug: `list-sheets`

Price: `5` credits

List the tabs in a spreadsheet with sheet ids and dimensions.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `protect_range`

Action slug: `protect-range`

Price: `5` credits

Protect a range, optionally warning-only or with explicit editor emails.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `description` | `string` | no | Protection description. |
| `editor_emails` | `array` | no | Users allowed to edit protected range. |
| `range` | `string` | yes | A1 range to protect. |
| `sheet_name` | `string` | no | Optional tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |
| `warning_only` | `boolean` | no | If true, warn instead of blocking edits. |

Sample parameters:

```json
{
  "description": "example description",
  "editor_emails": [
    "user@example.com"
  ],
  "range": "example range",
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id",
  "warning_only": true
}
```

Generated JSON parameter schema:

```json
{
  "description": {
    "description": "Protection description.",
    "required": false,
    "type": "string"
  },
  "editor_emails": {
    "description": "Users allowed to edit protected range.",
    "items": {
      "type": "string"
    },
    "required": false,
    "type": "array"
  },
  "range": {
    "description": "A1 range to protect.",
    "required": true,
    "type": "string"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  },
  "warning_only": {
    "description": "If true, warn instead of blocking edits.",
    "required": false,
    "type": "boolean"
  }
}
```

## `read`

Action slug: `read`

Price: `5` credits

Read values from a tab or A1 range. If sheet_name is omitted, resolves the real first tab.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `range` | `string` | no | Optional A1 range. Bare ranges are qualified with sheet_name. |
| `sheet_id` | `integer` | no | Optional numeric sheet id. |
| `sheet_name` | `string` | no | Optional tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |
| `value_render_option` | `string` | no | FORMATTED_VALUE, UNFORMATTED_VALUE, or FORMULA. |

Sample parameters:

```json
{
  "range": "example range",
  "sheet_id": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id",
  "value_render_option": "example value render option"
}
```

Generated JSON parameter schema:

```json
{
  "range": {
    "description": "Optional A1 range. Bare ranges are qualified with sheet_name.",
    "required": false,
    "type": "string"
  },
  "sheet_id": {
    "description": "Optional numeric sheet id.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  },
  "value_render_option": {
    "description": "FORMATTED_VALUE, UNFORMATTED_VALUE, or FORMULA.",
    "required": false,
    "type": "string"
  }
}
```

## `rename_sheet`

Action slug: `rename-sheet`

Price: `5` credits

Rename a tab by name, id, or index.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `new_sheet_name` | `string` | yes | New tab name. |
| `sheet_id` | `integer` | no | Numeric sheet id. |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Current tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "new_sheet_name": "example new sheet name",
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "new_sheet_name": {
    "description": "New tab name.",
    "required": true,
    "type": "string"
  },
  "sheet_id": {
    "description": "Numeric sheet id.",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Current tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `search`

Action slug: `search`

Price: `5` credits

Search or list recent Google Sheets spreadsheets.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `max_results` | `integer` | no | Maximum results to return, 1-100. |
| `query` | `string` | no | Optional search text matched against spreadsheet name/content. |

Sample parameters:

```json
{
  "max_results": 1,
  "query": "example search query"
}
```

Generated JSON parameter schema:

```json
{
  "max_results": {
    "description": "Maximum results to return, 1-100.",
    "maximum": 100,
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "query": {
    "description": "Optional search text matched against spreadsheet name/content.",
    "required": false,
    "type": "string"
  }
}
```

## `set_data_validation`

Action slug: `set-data-validation`

Price: `5` credits

Set a Sheets data validation rule on a range.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `range` | `string` | yes | A1 range. |
| `sheet_name` | `string` | no | Optional tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |
| `validation_rule` | `object` | yes | Sheets DataValidationRule object. |

Sample parameters:

```json
{
  "range": "example range",
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id",
  "validation_rule": {}
}
```

Generated JSON parameter schema:

```json
{
  "range": {
    "description": "A1 range.",
    "required": true,
    "type": "string"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  },
  "validation_rule": {
    "description": "Sheets DataValidationRule object.",
    "required": true,
    "type": "object"
  }
}
```

## `share`

Action slug: `share`

Price: `5` credits

Share a spreadsheet with a user, group, domain, or anyone.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `domain` | `string` | no | Domain for domain shares. |
| `email` | `string` | no | Email for user/group shares. |
| `permission_type` | `string` | no | user, group, domain, or anyone. |
| `role` | `string` | no | reader, commenter, writer, organizer, fileOrganizer, or owner. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "domain": "example domain",
  "email": "user@example.com",
  "permission_type": "example permission type",
  "role": "example role",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "domain": {
    "description": "Domain for domain shares.",
    "required": false,
    "type": "string"
  },
  "email": {
    "description": "Email for user/group shares.",
    "required": false,
    "type": "string"
  },
  "permission_type": {
    "description": "user, group, domain, or anyone.",
    "required": false,
    "type": "string"
  },
  "role": {
    "description": "reader, commenter, writer, organizer, fileOrganizer, or owner.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `sort`

Action slug: `sort`

Price: `5` credits

Sort a range, preferably by header name.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `range` | `string` | yes | A1 range to sort. |
| `sheet_name` | `string` | no | Optional tab name when range is bare A1 notation. |
| `sort_specs` | `array` | yes | Sort specs with header/column_name or dimensionIndex and order/sortOrder. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "range": "example range",
  "sheet_name": "example sheet name",
  "sort_specs": [
    {}
  ],
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "range": {
    "description": "A1 range to sort.",
    "required": true,
    "type": "string"
  },
  "sheet_name": {
    "description": "Optional tab name when range is bare A1 notation.",
    "required": false,
    "type": "string"
  },
  "sort_specs": {
    "description": "Sort specs with header/column_name or dimensionIndex and order/sortOrder.",
    "items": {
      "type": "object"
    },
    "required": true,
    "type": "array"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `unprotect_range`

Action slug: `unprotect-range`

Price: `5` credits

Remove protection by protected range id.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `protected_range_id` | `integer` | yes | Google protectedRangeId to delete. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "protected_range_id": 1,
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "protected_range_id": {
    "description": "Google protectedRangeId to delete.",
    "required": true,
    "type": "integer"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  }
}
```

## `update_row`

Action slug: `update-row`

Price: `5` credits

Update selected columns in a matched row using header names. Touches only requested cells.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `key_column` | `string` | no | Header used to find the row when row_number is omitted. |
| `key_value` | `string` | no | Value to match in key_column. |
| `multi` | `boolean` | no | Allow all matching rows to update. |
| `row_number` | `integer` | no | Optional one-based row number. |
| `sheet_name` | `string` | no | Optional tab name. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |
| `updates` | `object` | yes | Column patch keyed by header names. |

Sample parameters:

```json
{
  "key_column": "example key column",
  "key_value": "example key value",
  "multi": true,
  "row_number": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id",
  "updates": {}
}
```

Generated JSON parameter schema:

```json
{
  "key_column": {
    "description": "Header used to find the row when row_number is omitted.",
    "required": false,
    "type": "string"
  },
  "key_value": {
    "description": "Value to match in key_column.",
    "required": false,
    "type": "string"
  },
  "multi": {
    "description": "Allow all matching rows to update.",
    "required": false,
    "type": "boolean"
  },
  "row_number": {
    "description": "Optional one-based row number.",
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Optional tab name.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Google spreadsheet id or URL.",
    "required": true,
    "type": "string"
  },
  "updates": {
    "description": "Column patch keyed by header names.",
    "required": true,
    "type": "object"
  }
}
```
