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
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

Append rows after Google's detected table. Object rows map to sheet headers. Returns appended_row_numbers from Google's actual updated range.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `header_row` | `integer` | no | One-based header row, default 1. |
| `rows` | `array` | yes | Rows as arrays or objects keyed by headers. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

## `clear_range`

Action slug: `clear-range`

Price: `5` credits

Empty the values in an A1 range without deleting rows or columns. Notes and merges are kept; formatting is kept unless clear_formatting is true.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `clear_formatting` | `boolean` | no | Also reset cell formatting in the range. |
| `range` | `string` | yes | A1 range to clear, e.g. A10:F40 or 'Quote'!A10:F40. Parts past the tab's grid are ignored. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "clear_formatting": false,
  "range": "example range",
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "clear_formatting": {
    "default": false,
    "description": "Also reset cell formatting in the range.",
    "required": false,
    "type": "boolean"
  },
  "range": {
    "description": "A1 range to clear, e.g. A10:F40 or 'Quote'!A10:F40. Parts past the tab's grid are ignored.",
    "required": true,
    "type": "string"
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
    "required": true,
    "type": "string"
  }
}
```

## `copy_paste`

Action slug: `copy-paste`

Price: `5` credits

Copy cells to an A1 destination range; overwrites destination cells and does not insert rows.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `destination_range` | `string` | yes | A1 destination range. |
| `paste_orientation` | `string` | no | NORMAL or TRANSPOSE. |
| `paste_type` | `string` | no | Sheets pasteType such as PASTE_NORMAL or PASTE_VALUES. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

Move cells to an A1 destination start cell; does not insert rows. Returns destination_row_number.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `destination_range` | `string` | yes | A1 destination start cell. |
| `paste_type` | `string` | no | Sheets pasteType such as PASTE_NORMAL or PASTE_VALUES. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

## `delete_note`

Action slug: `delete-note`

Price: `5` credits

Remove notes from every cell in a bounded A1 cell or range without changing values or formatting.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `range` | `string` | yes | A1 range using visible one-based worksheet row numbers; quote a tab name only inside a qualified range. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "range": "example range",
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "range": {
    "description": "A1 range using visible one-based worksheet row numbers; quote a tab name only inside a qualified range.",
    "required": true,
    "type": "string"
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
    "required": true,
    "type": "string"
  }
}
```

## `delete_rows`

Action slug: `delete-rows`

Price: `5` credits

Permanently delete complete worksheet rows by original one-based row number, from bottom to top. Requires a tab selector; row 1 is protected.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `row_numbers` | `array` | yes | Distinct original one-based sheet row numbers, each at least 2; 1-500 entries. One of sheet_name, sheet_id, or sheet_index is required. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "row_numbers": [
    2
  ],
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "row_numbers": {
    "description": "Distinct original one-based sheet row numbers, each at least 2; 1-500 entries. One of sheet_name, sheet_id, or sheet_index is required.",
    "items": {
      "minimum": 2,
      "type": "integer"
    },
    "maxItems": 500,
    "minItems": 1,
    "required": true,
    "type": "array",
    "uniqueItems": true
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
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
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

Export a specific sheet or whole spreadsheet to File Manager as CSV, TSV, PDF, XLSX, ODS, HTML, or ZIP. For PDF, pdf_options sets the print layout (orientation, fit to one page, gridlines, margins).

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `expiration_days` | `integer` | no | File Manager expiration, 1-7 days. |
| `filename` | `string` | no | Optional stored filename. |
| `format` | `string` | yes | csv, tsv, pdf, xlsx, ods, html, or zip. Use pdf with pdf_options for print layout. |
| `pdf_options` | `object` | no | Print layout for format=pdf only; applies to the exported file, not the spreadsheet's own print settings. Omitted fields use Google's defaults. One-page portrait without gridlines: {"orientation": "portrait", "fit": "page", "show_gridlines": false}. |
| `range` | `string` | no | Optional A1 range. Limits CSV/TSV exports, and PDF exports that use pdf_options, to these cells. |
| `sheet_id` | `integer` | no | Optional numeric sheet id. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Google spreadsheet id or URL. |

Sample parameters:

```json
{
  "expiration_days": 1,
  "filename": "example filename",
  "format": "example format",
  "pdf_options": {
    "bottom_margin": 0,
    "fit": "actual_size",
    "horizontal_alignment": "LEFT",
    "left_margin": 0,
    "margins": "normal",
    "orientation": "portrait",
    "paper_size": "letter",
    "repeat_frozen_columns": true
  },
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
    "description": "csv, tsv, pdf, xlsx, ods, html, or zip. Use pdf with pdf_options for print layout.",
    "required": true,
    "type": "string"
  },
  "pdf_options": {
    "description": "Print layout for format=pdf only; applies to the exported file, not the spreadsheet's own print settings. Omitted fields use Google's defaults. One-page portrait without gridlines: {\"orientation\": \"portrait\", \"fit\": \"page\", \"show_gridlines\": false}.",
    "properties": {
      "bottom_margin": {
        "description": "Bottom margin in inches.",
        "maximum": 10,
        "minimum": 0,
        "required": false,
        "type": "number"
      },
      "fit": {
        "description": "actual_size, width (fit to page width), height (fit to page height), or page (everything on one page).",
        "enum": [
          "actual_size",
          "width",
          "height",
          "page"
        ],
        "required": false,
        "type": "string"
      },
      "horizontal_alignment": {
        "description": "Horizontal placement on the page.",
        "enum": [
          "LEFT",
          "CENTER",
          "RIGHT"
        ],
        "required": false,
        "type": "string"
      },
      "left_margin": {
        "description": "Left margin in inches.",
        "maximum": 10,
        "minimum": 0,
        "required": false,
        "type": "number"
      },
      "margins": {
        "description": "Margin preset: normal, narrow, or wide.",
        "enum": [
          "normal",
          "narrow",
          "wide"
        ],
        "required": false,
        "type": "string"
      },
      "orientation": {
        "description": "Page orientation.",
        "enum": [
          "portrait",
          "landscape"
        ],
        "required": false,
        "type": "string"
      },
      "paper_size": {
        "description": "Paper size.",
        "enum": [
          "letter",
          "legal",
          "tabloid",
          "statement",
          "executive",
          "folio",
          "a3",
          "a4",
          "a5",
          "b4",
          "b5"
        ],
        "required": false,
        "type": "string"
      },
      "repeat_frozen_columns": {
        "description": "Repeat frozen columns on every page.",
        "required": false,
        "type": "boolean"
      },
      "repeat_frozen_rows": {
        "description": "Repeat frozen header rows on every page (freeze them first).",
        "required": false,
        "type": "boolean"
      },
      "right_margin": {
        "description": "Right margin in inches.",
        "maximum": 10,
        "minimum": 0,
        "required": false,
        "type": "number"
      },
      "show_gridlines": {
        "description": "Print cell gridlines.",
        "required": false,
        "type": "boolean"
      },
      "show_notes": {
        "description": "Print cell notes.",
        "required": false,
        "type": "boolean"
      },
      "show_page_numbers": {
        "description": "Print page numbers.",
        "required": false,
        "type": "boolean"
      },
      "show_sheet_names": {
        "description": "Print the tab name in the header.",
        "required": false,
        "type": "boolean"
      },
      "show_title": {
        "description": "Print the spreadsheet title in the header.",
        "required": false,
        "type": "boolean"
      },
      "top_margin": {
        "description": "Top margin in inches; overrides the preset for this side.",
        "maximum": 10,
        "minimum": 0,
        "required": false,
        "type": "number"
      },
      "vertical_alignment": {
        "description": "Vertical placement on the page.",
        "enum": [
          "TOP",
          "MIDDLE",
          "BOTTOM"
        ],
        "required": false,
        "type": "string"
      }
    },
    "required": false,
    "type": "object"
  },
  "range": {
    "description": "Optional A1 range. Limits CSV/TSV exports, and PDF exports that use pdf_options, to these cells.",
    "required": false,
    "type": "string"
  },
  "sheet_id": {
    "description": "Optional numeric sheet id.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

## `freeze`

Action slug: `freeze`

Price: `5` credits

Freeze the top rows and/or left columns of a tab so they stay visible while scrolling. 0 unfreezes. Frozen rows can repeat on every PDF page.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `frozen_columns` | `integer` | no | Number of left columns to freeze; 0 unfreezes columns. |
| `frozen_rows` | `integer` | no | Number of top rows to freeze; 0 unfreezes rows. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "frozen_columns": 0,
  "frozen_rows": 0,
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "frozen_columns": {
    "description": "Number of left columns to freeze; 0 unfreezes columns.",
    "minimum": 0,
    "required": false,
    "type": "integer"
  },
  "frozen_rows": {
    "description": "Number of top rows to freeze; 0 unfreezes rows.",
    "minimum": 0,
    "required": false,
    "type": "integer"
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
    "required": true,
    "type": "string"
  }
}
```

## `get_data_range`

Action slug: `get-data-range`

Price: `5` credits

Find the absolute one-based last non-empty row/column; a partial range never returns an append recommendation.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `range` | `string` | no | Optional partial A1 range; recommended_append_start is null when set. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Optional partial A1 range; recommended_append_start is null when set.",
    "required": false,
    "type": "string"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

## `list_notes`

Action slug: `list-notes`

Price: `5` credits

List cell notes with exact sheet and A1 locations plus the current cell values. Without a filter, scans every tab.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `range` | `string` | no | A1 range using visible one-based worksheet row numbers; quote a tab name only inside a qualified range. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "range": "example range",
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "range": {
    "description": "A1 range using visible one-based worksheet row numbers; quote a tab name only inside a qualified range.",
    "required": false,
    "type": "string"
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
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

## `merge_cells`

Action slug: `merge-cells`

Price: `5` credits

Merge a bounded range of at least two cells. Only the top-left value of each merged area is kept, so the call fails and lists the cells that would lose values unless allow_value_loss is true.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `allow_value_loss` | `boolean` | no | Proceed even though values outside each merged area's top-left cell will be discarded. |
| `merge_type` | `string` | no | MERGE_ALL merges the whole range into one cell; MERGE_ROWS merges each row separately; MERGE_COLUMNS merges each column separately. |
| `range` | `string` | yes | Bounded A1 range inside the tab's grid, e.g. A1:F1. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "allow_value_loss": false,
  "merge_type": "MERGE_ALL",
  "range": "example range",
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "allow_value_loss": {
    "default": false,
    "description": "Proceed even though values outside each merged area's top-left cell will be discarded.",
    "required": false,
    "type": "boolean"
  },
  "merge_type": {
    "default": "MERGE_ALL",
    "description": "MERGE_ALL merges the whole range into one cell; MERGE_ROWS merges each row separately; MERGE_COLUMNS merges each column separately.",
    "enum": [
      "MERGE_ALL",
      "MERGE_ROWS",
      "MERGE_COLUMNS"
    ],
    "required": false,
    "type": "string"
  },
  "range": {
    "description": "Bounded A1 range inside the tab's grid, e.g. A1:F1.",
    "required": true,
    "type": "string"
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
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
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

Read values from a tab or A1 range. Returns one-based row_numbers aligned with values; no row offset is needed.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `range` | `string` | no | Optional A1 range with visible one-based row labels. Qualified range and sheet_name must identify the same tab. |
| `sheet_id` | `integer` | no | Optional numeric sheet id. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Optional A1 range with visible one-based row labels. Qualified range and sheet_name must identify the same tab.",
    "required": false,
    "type": "string"
  },
  "sheet_id": {
    "description": "Optional numeric sheet id.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

## `rename_spreadsheet`

Action slug: `rename-spreadsheet`

Price: `5` credits

Rename the spreadsheet file; does not rename any sheet tab.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `new_title` | `string` | yes | Nonblank new spreadsheet file title. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full URL. |

Sample parameters:

```json
{
  "new_title": "example new title",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "new_title": {
    "description": "Nonblank new spreadsheet file title.",
    "required": true,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full URL.",
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

## `set_borders`

Action slug: `set-borders`

Price: `5` credits

Draw or remove table borders on an A1 range using a preset, per-side borders, or both (per-side borders override the preset). Sides not given are left unchanged.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `border_color` | `object` | no | Border RGB color with 0-1 channels, e.g. {"red": 0.12, "green": 0.3, "blue": 0.47}. Defaults to black. |
| `border_preset` | `string` | no | all (grid on every cell), outer (box around the range), inner (lines between cells only), or none (remove all borders in the range). |
| `border_style` | `string` | no | Line style for border_preset and for borders sides given without a style. |
| `borders` | `object` | no | Per-side borders. Keys: top, bottom, left, right, inner_horizontal, inner_vertical. Values: a style (SOLID, SOLID_MEDIUM, SOLID_THICK, DOUBLE, DASHED, DOTTED, NONE) or {"style": "SOLID_THICK", "color": {"red": 0, "green": 0, "blue": 0}}. |
| `range` | `string` | yes | A1 range to border, e.g. A5:F20. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "border_color": {
    "blue": 0,
    "green": 0,
    "red": 0
  },
  "border_preset": "all",
  "border_style": "SOLID",
  "borders": {},
  "range": "example range",
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name"
}
```

Generated JSON parameter schema:

```json
{
  "border_color": {
    "description": "Border RGB color with 0-1 channels, e.g. {\"red\": 0.12, \"green\": 0.3, \"blue\": 0.47}. Defaults to black.",
    "properties": {
      "blue": {
        "description": "Blue channel, 0-1.",
        "maximum": 1,
        "minimum": 0,
        "required": false,
        "type": "number"
      },
      "green": {
        "description": "Green channel, 0-1.",
        "maximum": 1,
        "minimum": 0,
        "required": false,
        "type": "number"
      },
      "red": {
        "description": "Red channel, 0-1.",
        "maximum": 1,
        "minimum": 0,
        "required": false,
        "type": "number"
      }
    },
    "required": false,
    "type": "object"
  },
  "border_preset": {
    "description": "all (grid on every cell), outer (box around the range), inner (lines between cells only), or none (remove all borders in the range).",
    "enum": [
      "all",
      "outer",
      "inner",
      "none"
    ],
    "required": false,
    "type": "string"
  },
  "border_style": {
    "default": "SOLID",
    "description": "Line style for border_preset and for borders sides given without a style.",
    "enum": [
      "SOLID",
      "SOLID_MEDIUM",
      "SOLID_THICK",
      "DOUBLE",
      "DASHED",
      "DOTTED"
    ],
    "required": false,
    "type": "string"
  },
  "borders": {
    "description": "Per-side borders. Keys: top, bottom, left, right, inner_horizontal, inner_vertical. Values: a style (SOLID, SOLID_MEDIUM, SOLID_THICK, DOUBLE, DASHED, DOTTED, NONE) or {\"style\": \"SOLID_THICK\", \"color\": {\"red\": 0, \"green\": 0, \"blue\": 0}}.",
    "required": false,
    "type": "object"
  },
  "range": {
    "description": "A1 range to border, e.g. A5:F20.",
    "required": true,
    "type": "string"
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
    "required": true,
    "type": "string"
  }
}
```

## `set_column_widths`

Action slug: `set-column-widths`

Price: `5` credits

Set column widths in pixels and/or auto-fit columns to their contents. Provide column_widths, auto_fit, or both; explicit widths are applied after the auto-fit.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `auto_fit` | `boolean` | no | Resize columns to fit their contents. |
| `column_widths` | `object` | no | Column letter or letter range mapped to width in pixels, e.g. {"A": 40, "B": 220, "C:F": 110}. Default Sheets width is 100. |
| `range` | `string` | no | Columns to auto-fit, e.g. A:F. Omit to auto-fit every column on the tab. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "auto_fit": false,
  "column_widths": {},
  "range": "example range",
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "auto_fit": {
    "default": false,
    "description": "Resize columns to fit their contents.",
    "required": false,
    "type": "boolean"
  },
  "column_widths": {
    "description": "Column letter or letter range mapped to width in pixels, e.g. {\"A\": 40, \"B\": 220, \"C:F\": 110}. Default Sheets width is 100.",
    "required": false,
    "type": "object"
  },
  "range": {
    "description": "Columns to auto-fit, e.g. A:F. Omit to auto-fit every column on the tab.",
    "required": false,
    "type": "string"
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
    "required": true,
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
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

## `set_gridlines`

Action slug: `set-gridlines`

Price: `5` credits

Show or hide the gray cell gridlines on a tab.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `show_gridlines` | `boolean` | yes | false hides gridlines; true shows them. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "show_gridlines": true,
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "show_gridlines": {
    "description": "false hides gridlines; true shows them.",
    "required": true,
    "type": "boolean"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
    "required": true,
    "type": "string"
  }
}
```

## `set_note`

Action slug: `set-note`

Price: `5` credits

Set the same note on every cell in a bounded A1 cell or range.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `note` | `string` | yes | Note text to set; use delete_note to remove it. |
| `range` | `string` | yes | A1 range using visible one-based worksheet row numbers; quote a tab name only inside a qualified range. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "note": "example note",
  "range": "example range",
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "note": {
    "description": "Note text to set; use delete_note to remove it.",
    "minLength": 1,
    "required": true,
    "type": "string"
  },
  "range": {
    "description": "A1 range using visible one-based worksheet row numbers; quote a tab name only inside a qualified range.",
    "required": true,
    "type": "string"
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
    "required": true,
    "type": "string"
  }
}
```

## `set_row_heights`

Action slug: `set-row-heights`

Price: `5` credits

Set row heights in pixels and/or auto-fit rows to their contents. Provide row_heights, auto_fit, or both; explicit heights are applied after the auto-fit.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `auto_fit` | `boolean` | no | Resize rows to fit their contents. |
| `range` | `string` | no | Rows to auto-fit, e.g. 1:20. Omit to auto-fit every row on the tab. |
| `row_heights` | `object` | no | One-based row number or row range mapped to height in pixels, e.g. {"1": 48, "2:30": 24}. Default Sheets height is 21. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "auto_fit": false,
  "range": "example range",
  "row_heights": {},
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "auto_fit": {
    "default": false,
    "description": "Resize rows to fit their contents.",
    "required": false,
    "type": "boolean"
  },
  "range": {
    "description": "Rows to auto-fit, e.g. 1:20. Omit to auto-fit every row on the tab.",
    "required": false,
    "type": "string"
  },
  "row_heights": {
    "description": "One-based row number or row range mapped to height in pixels, e.g. {\"1\": 48, \"2:30\": 24}. Default Sheets height is 21.",
    "required": false,
    "type": "object"
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
    "required": true,
    "type": "string"
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
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

## `unmerge_cells`

Action slug: `unmerge-cells`

Price: `5` credits

Unmerge every merged area that lies within an A1 range.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `range` | `string` | yes | A1 range covering the merged cells, e.g. A1:F1. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |

Sample parameters:

```json
{
  "range": "example range",
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id"
}
```

Generated JSON parameter schema:

```json
{
  "range": {
    "description": "A1 range covering the merged cells, e.g. A1:F1.",
    "required": true,
    "type": "string"
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
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

Update selected fields by header in a physical one-based row_number, or by a stable key; long-text exact matching is fragile.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `key_column` | `string` | no | Header used to find the row when row_number is omitted. |
| `key_value` | `string` | no | Value to match in key_column. |
| `multi` | `boolean` | no | Allow all matching rows to update. |
| `row_number` | `integer` | no | Physical one-based row number from read.row_numbers; do not add 1 or 2. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
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
    "description": "Physical one-based row number from read.row_numbers; do not add 1 or 2.",
    "minimum": 1,
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
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

## `write_range`

Action slug: `write-range`

Price: `5` credits

Write values into exact cells, such as a title block or report layout. Refuses to replace cells that already hold data unless overwrite is true; grows the tab if values run past its grid.

Parameters:

| Parameter | Type | Required | Description |
|---|---|---|---|
| `overwrite` | `boolean` | no | Allow replacing cells that already contain data. Without it the call fails and lists the occupied cells. |
| `range` | `string` | yes | Top-left cell (e.g. B3) to size the write from values, or a bounded A1 range at least as large as values. A qualified range like 'Quote'!B3 selects the tab. |
| `sheet_id` | `integer` | no | Numeric Google sheetId (gid). |
| `sheet_index` | `integer` | no | Zero-based tab index. |
| `sheet_name` | `string` | no | Exact tab title from list_sheets, without surrounding A1 quote marks. |
| `spreadsheet_id` | `string` | yes | Spreadsheet ID or full Google Sheets URL. |
| `values` | `array` | yes | Row arrays, e.g. [["Name", "Total"], ["Ada", 42]]. null leaves a cell unchanged; "" clears it. Entered as if typed, so formulas starting with = are evaluated. |

Sample parameters:

```json
{
  "overwrite": false,
  "range": "example range",
  "sheet_id": 1,
  "sheet_index": 1,
  "sheet_name": "example sheet name",
  "spreadsheet_id": "example spreadsheet id",
  "values": [
    [
      "example value"
    ]
  ]
}
```

Generated JSON parameter schema:

```json
{
  "overwrite": {
    "default": false,
    "description": "Allow replacing cells that already contain data. Without it the call fails and lists the occupied cells.",
    "required": false,
    "type": "boolean"
  },
  "range": {
    "description": "Top-left cell (e.g. B3) to size the write from values, or a bounded A1 range at least as large as values. A qualified range like 'Quote'!B3 selects the tab.",
    "required": true,
    "type": "string"
  },
  "sheet_id": {
    "description": "Numeric Google sheetId (gid).",
    "required": false,
    "type": "integer"
  },
  "sheet_index": {
    "description": "Zero-based tab index.",
    "required": false,
    "type": "integer"
  },
  "sheet_name": {
    "description": "Exact tab title from list_sheets, without surrounding A1 quote marks.",
    "required": false,
    "type": "string"
  },
  "spreadsheet_id": {
    "description": "Spreadsheet ID or full Google Sheets URL.",
    "required": true,
    "type": "string"
  },
  "values": {
    "description": "Row arrays, e.g. [[\"Name\", \"Total\"], [\"Ada\", 42]]. null leaves a cell unchanged; \"\" clears it. Entered as if typed, so formulas starting with = are evaluated.",
    "items": {
      "description": "One row of cell values.",
      "items": {
        "description": "Cell value: string, number, boolean, or null."
      },
      "type": "array"
    },
    "required": true,
    "type": "array"
  }
}
```
