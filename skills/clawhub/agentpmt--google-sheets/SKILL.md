---
name: google-sheets
description: "Google Sheets: Work with Google Sheets using safe short actions: discover tabs and headers, read values with exact one-based row numbers, append rows and columns, update selected fields, write or clear exact cell ranges, archive. Use when an agent needs google sheets, google sheets api, append spreadsheet rows safely, update crm style rows by key, export a sheet to csv or pdf, create reporting spreadsheets, add conditional formatting, spreadsheet id through AgentPMT-hosted remote tool calls."
version: 1.0.3
homepage: https://www.agentpmt.com/marketplace/google-sheets-api
compatibility: "Agent instructions for AgentPMT-hosted remote tool calls. Follow this skill body for supported account, wallet, and setup routes. No local command runtime is declared."
metadata: {"author":"agentpmt","openclaw":{"homepage":"https://www.agentpmt.com/marketplace/google-sheets-api"}}
---
# Google Sheets

## Freshness
Last updated: `2026-11-24`.

If the current date is more than 7 days after the last updated date, reinstall this skill from skills.sh or ClawHub before relying on endpoints, schemas, setup steps, or examples.

## What This Tool Does
Create, read, update, format, share, and export Google Sheets with agent-safe spreadsheet workflows. Append rows after Google's detected table, read cell notes with exact locations and values, delete selected worksheet rows, update fields by one-based row number or stable key, and store exports in File Manager.

## Product Instructions
### Google Sheets

Use the short action names. This tool is optimized for safe agent workflows:
read a tab, append rows after Google's detected table, update only named columns in a
matched row, and export a specific sheet without guessing `"Sheet1"`.

#### Use These First

- Read data: `read`
- Add table records: `append_rows`
- Add one new field/column: `append_column`
- Update selected fields in a matched row: `update_row`
- Export one tab or the whole spreadsheet: `export_sheet`
- Discover real tab names: `list_sheets`
- Read notes with their cells and current values: `list_notes`
- Remove selected worksheet rows after verifying their data is safely copied: `delete_rows`
- Rename the entire spreadsheet file: `rename_spreadsheet`; rename one tab: `rename_sheet`
- Put values in specific cells (title blocks, report layouts): `write_range`
- Lay out a printable report: `set_column_widths`, `merge_cells`, `set_borders`,
  `freeze`, `set_gridlines`, then `export_sheet` with `pdf_options`

#### Actions

- `create`
- `search`
- `list_sheets`
- `read`
- `get_headers`
- `get_data_range`
- `list_notes`
- `set_note`
- `delete_note`
- `append_rows`
- `append_column`
- `update_row`
- `export_sheet`
- `share`
- `add_sheet`
- `delete_sheet`
- `delete_rows`
- `rename_spreadsheet`
- `rename_sheet`
- `sort`
- `find_replace`
- `format_cells`
- `protect_range`
- `unprotect_range`
- `add_named_range`
- `delete_named_range`
- `set_data_validation`
- `add_conditional_formatting`
- `copy_paste`
- `cut_paste`
- `write_range`
- `clear_range`
- `set_column_widths`
- `set_row_heights`
- `merge_cells`
- `unmerge_cells`
- `set_borders`
- `freeze`
- `set_gridlines`
- `get_instructions`

Legacy low-level names such as `get_values`, `append_values`,
`batch_update_values`, `get_sheet_data`, `create_spreadsheet`, and raw
`batch_update` are intentionally removed. Use the friendly action that matches
the intent instead.

#### Safe Reads

If `sheet_name` is omitted, the tool resolves the real first tab from
spreadsheet metadata. Do not guess `"Sheet1"`.
Use the exact tab title from `list_sheets` for `sheet_name`, without A1 quote
marks: `"Oct 2026"`, not `"'Oct 2026'"`. Quote tab names only inside a
fully qualified A1 `range`, for example `"'Oct 2026'!A2:I2"`. For one-tab
actions, use either a sheet selector with an unqualified range or a qualified
range by itself. On `read`, conflicting selectors are rejected. Cross-tab
`copy_paste` and `cut_paste` may use separately qualified source and destination
ranges.

All row numbers exposed by this tool are **one-based worksheet row numbers**,
matching the row labels visible in Google Sheets. `read` returns `row_numbers`
aligned with `values`: `values[i]` is on sheet row `row_numbers[i]`. Use that
number directly for `update_row` or `delete_rows`; do not add 1 or 2. For
example, when row 1 is the header, `values[1]` has `row_numbers[1] == 2`.
This also works when `read` starts at a later range such as `A20:I30`.

```json
{"action": "read", "spreadsheet_id": "1abc..."}
```

```json
{"action": "read", "spreadsheet_id": "1abc...", "sheet_name": "Q1 Pipeline", "range": "A1:D20"}
```

`get_data_range.last_row` is also an absolute, one-based sheet row number.
Call `get_data_range` without `range` to get `recommended_append_start` for the
whole tab. If a partial `range` is supplied, the recommendation is `null`
because the tool cannot know whether data exists outside that selection.

#### Append Rows

Use `append_rows` for all table appends. The tool reads headers when rows are
objects, maps keys to columns, and appends with `INSERT_ROWS`.

```json
{
  "action": "append_rows",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "rows": [
    {"Name": "Ada", "Status": "New"},
    {"Name": "Grace", "Status": "Qualified"}
  ]
}
```

The backend also accepts array rows, but the published vendor action schema
exposes object rows. Agents should use header-keyed objects so the columns are
unambiguous.

`append_rows` does not take a destination row number. Google places the new
rows after the table it detects in the requested tab; read the returned
`appended_row_numbers` (or `updates.updatedRange`) for their actual sheet
positions. Do not calculate an insertion row or add an offset. If exact
placement within the sheet is required, `append_rows` is not that operation.

#### Append Column

Use `append_column` to add a column immediately after the current data table.
Agents should not calculate raw column indexes.

```json
{
  "action": "append_column",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "column_name": "Owner",
  "column_values": ["Sam", "Riley"]
}
```

#### Update A Row Safely

Use `update_row` to update specific fields only. The tool resolves headers and
emits exact `updateCells` requests for the touched cells.

```json
{
  "action": "update_row",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "key_column": "Email",
  "key_value": "ada@example.com",
  "updates": {"Status": "Qualified", "Owner": "Sam"}
}
```

If more than one row matches, the tool errors unless `multi` is `true`.
For a known physical row, pass `row_number` directly from `read.row_numbers`:

```json
{"action": "update_row", "spreadsheet_id": "1abc...", "sheet_name": "Leads", "row_number": 8, "updates": {"Status": "Qualified"}}
```

Prefer `row_number` over matching an entire long text cell with `key_column`
and `key_value`; even a changed newline or punctuation mark makes an exact
text match fail. Re-read immediately before an update if other writers may
insert or delete rows.

#### Delete Rows

`delete_rows` permanently removes complete worksheet rows and shifts the rows
below them upward. Required: `spreadsheet_id`, one of `sheet_name`, `sheet_id`,
or `sheet_index`, and `row_numbers` (an array of 1-500 distinct, one-based row
numbers). Row 1 is protected. The tool deletes the original row numbers from
bottom to top, so non-adjacent rows can be sent together without recalculating
positions. Never retry a successful or uncertain deletion with the same row
numbers; re-read the sheet first because positions may have shifted.

```json
{"action": "delete_rows", "spreadsheet_id": "1abc...", "sheet_name": "Posts", "row_numbers": [3, 8, 12]}
```

For archiving values: read the source rows, send their values to the archive
tab with `append_rows`, verify the returned appended rows, then delete only the
original source row numbers in one `delete_rows` call. If formatting or notes
must also move, use `copy_paste` or `cut_paste` into a verified empty archive
range instead; these actions overwrite destination cells and do not insert
worksheet rows. After `cut_paste`, the source cells are blank but the worksheet
rows remain until `delete_rows` runs. Do not delete rows before verifying the
archive.
For example, if a `posted` record is `read.values[1]` and its matching
`read.row_numbers[1]` is `2`, move `A2:I2` and later delete row `2`—not row `4`.

`copy_paste` and `cut_paste` use A1 addresses such as `'Posts'!A8:I8` and
`'archive'!A3`; those row numbers are also one-based. `cut_paste` returns
`destination_row_number` for confirmation. Do not add an offset to A1 addresses.

#### Cell Notes

Notes are stable Google Sheets cell metadata and are distinct from comment
threads. `list_notes` returns each note with its exact sheet, A1 cell address,
displayed value, raw/effective value, and formula when present. With no sheet or
range filter it scans every tab in the spreadsheet.

```json
{"action": "list_notes", "spreadsheet_id": "1abc..."}
```

Limit the scan to one tab or range when the workbook is large:

```json
{"action": "list_notes", "spreadsheet_id": "1abc...", "sheet_name": "Forecast", "range": "A1:F100"}
```

Set or replace a note. When `range` contains multiple cells, the same note is
applied to every cell in the range:

```json
{"action": "set_note", "spreadsheet_id": "1abc...", "sheet_name": "Forecast", "range": "D12", "note": "Verify this assumption"}
```

Delete notes from a cell or range without changing cell values or formatting:

```json
{"action": "delete_note", "spreadsheet_id": "1abc...", "sheet_name": "Forecast", "range": "D12"}
```

#### Export

`export_sheet` stores exports in AgentPMT File Manager.

CSV and TSV exports for a specific sheet are synthesized from Sheets values
using proper CSV quoting. PDF/XLSX/ODS/HTML/ZIP exports for one sheet use the
official temporary-spreadsheet + `sheets.copyTo` + Drive export flow. Whole
spreadsheet exports use Drive `files.export`.

```json
{
  "action": "export_sheet",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "format": "csv",
  "filename": "leads.csv"
}
```

```json
{
  "action": "export_sheet",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "format": "pdf",
  "filename": "leads.pdf"
}
```

Drive scope is required for `export_sheet` formats that use Drive export and
for `share`.

##### PDF Print Layout

Add `pdf_options` to a `format: "pdf"` export to control the printed layout.
Google cannot save print settings on the spreadsheet itself, so these options
apply to the exported PDF only; File > Print in the browser keeps its own
defaults. For portrait, everything on one page, and no gridlines:

```json
{
  "action": "export_sheet",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Quote",
  "format": "pdf",
  "filename": "quote.pdf",
  "pdf_options": {"orientation": "portrait", "fit": "page", "show_gridlines": false}
}
```

`pdf_options` fields (all optional; omitted fields use Google's defaults):

- `orientation`: `portrait` or `landscape`
- `fit`: `page` (whole selection on one page), `width`, `height`, or `actual_size`
- `paper_size`: `letter`, `legal`, `tabloid`, `statement`, `executive`, `folio`, `a3`, `a4`, `a5`, `b4`, `b5`
- `show_gridlines`: `false` removes the gray cell lines (drawn borders still print)
- `margins`: `normal`, `narrow`, or `wide`; `top_margin`, `bottom_margin`,
  `left_margin`, `right_margin` in inches override single sides
- `horizontal_alignment`: `LEFT`, `CENTER`, `RIGHT`; `vertical_alignment`: `TOP`, `MIDDLE`, `BOTTOM`
- `repeat_frozen_rows` / `repeat_frozen_columns`: repeat frozen headers on every page
  (freeze them first with `freeze`)
- `show_page_numbers`, `show_sheet_names`, `show_title`, `show_notes`

With a tab selector, only that tab is printed; add `range` (for example
`"A1:F40"`) to print part of it. Without a tab selector or range, every tab is
printed. `pdf_options` is rejected for formats other than `pdf`.

#### Formatting And Controls

Use `format_cells` for common cell formatting:

```json
{
  "action": "format_cells",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "range": "A1:D1",
  "cell_format": {"bold": true, "background_color": {"red": 0.9, "green": 0.9, "blue": 1}}
}
```

Use `protect_range` and keep `warning_only=true` when you only want a warning:

```json
{
  "action": "protect_range",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "range": "A1:D1",
  "description": "Header row",
  "warning_only": true
}
```

Remove protection by the returned Google `protected_range_id`:

```json
{"action": "unprotect_range", "spreadsheet_id": "1abc...", "protected_range_id": 12345}
```

#### Write And Clear Ranges

Use `write_range` to place values in exact cells, such as a title block above a
table or labels in a form-style layout. `values` is an array of row arrays. Pass
the top-left cell as `range` and the write is sized from `values`; a full range
like `A1:C2` must be big enough for `values`. Values are entered as if typed
(formulas like `=SUM(B2:B9)` work). `null` leaves a cell unchanged and `""`
clears it. The tab grows automatically if the write runs past its last row or
column.

```json
{
  "action": "write_range",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Quote",
  "range": "A1",
  "values": [["Project Quote"], ["Prepared for", "Acme Co"], ["Date", "2026-11-22"]]
}
```

By default `write_range` refuses to replace cells that already contain data and
returns the occupied cells. Re-read the range, then send `overwrite: true` only
when replacing them is intended. For table records, still use `append_rows` or
`update_row`.

Use `clear_range` to empty cells without deleting rows or columns. Values and
formulas are cleared; add `clear_formatting: true` to also reset formatting.
Notes and merges are kept.

```json
{"action": "clear_range", "spreadsheet_id": "1abc...", "sheet_name": "Quote", "range": "A10:F40"}
```

#### Layout: Widths, Merges, Borders, Freeze, Gridlines

Column widths and row heights are in pixels (Sheets defaults: 100 wide,
21 tall). Keys are column letters or letter ranges, and one-based row numbers or
row ranges:

```json
{"action": "set_column_widths", "spreadsheet_id": "1abc...", "sheet_name": "Quote", "column_widths": {"A": 40, "B": 240, "C:F": 110}}
```

```json
{"action": "set_row_heights", "spreadsheet_id": "1abc...", "sheet_name": "Quote", "row_heights": {"1": 48, "2:30": 24}}
```

Fit columns or rows to their contents with `auto_fit: true`, limited by `range`
(`"A:F"` or `"1:20"`) or the whole tab when `range` is omitted:

```json
{"action": "set_column_widths", "spreadsheet_id": "1abc...", "sheet_name": "Quote", "auto_fit": true, "range": "A:F"}
```

Merge cells with `merge_cells` and a bounded range. `merge_type` is `MERGE_ALL`
(default, one cell), `MERGE_ROWS` (each row separately), or `MERGE_COLUMNS`
(each column separately). A merge keeps only the top-left value of each merged
area, so `merge_cells` fails and lists the affected cells when others contain
data; move those values or send `allow_value_loss: true`. Use `unmerge_cells`
with a range to split every merge inside it.

```json
{"action": "merge_cells", "spreadsheet_id": "1abc...", "sheet_name": "Quote", "range": "A1:F1"}
```

Draw table borders with `set_borders`. `border_preset` is `all` (every cell
line), `outer` (box), `inner` (lines between cells), or `none` (remove borders).
`border_style` is `SOLID` (default), `SOLID_MEDIUM`, `SOLID_THICK`, `DOUBLE`,
`DASHED`, or `DOTTED`; `border_color` uses 0-1 RGB channels and defaults to
black. `borders` sets individual sides (`top`, `bottom`, `left`, `right`,
`inner_horizontal`, `inner_vertical`) and overrides the preset; use style
`NONE` to remove one side. Sides not mentioned are left unchanged.

```json
{"action": "set_borders", "spreadsheet_id": "1abc...", "sheet_name": "Quote", "range": "A5:F20", "border_preset": "all"}
```

```json
{
  "action": "set_borders",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Quote",
  "range": "A5:F5",
  "borders": {"bottom": {"style": "SOLID_THICK", "color": {"red": 0.1, "green": 0.2, "blue": 0.45}}}
}
```

Keep header rows or label columns visible while scrolling with `freeze`
(`0` unfreezes). Frozen rows can also repeat on every PDF page.

```json
{"action": "freeze", "spreadsheet_id": "1abc...", "sheet_name": "Quote", "frozen_rows": 1}
```

Hide or show the gray gridlines on a tab with `set_gridlines`:

```json
{"action": "set_gridlines", "spreadsheet_id": "1abc...", "sheet_name": "Quote", "show_gridlines": false}
```

Images and logos cannot be inserted through this tool.

#### Advanced Sheet Features

Named ranges:

```json
{
  "action": "add_named_range",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "range": "A1:D20",
  "name": "LeadTable"
}
```

```json
{"action": "delete_named_range", "spreadsheet_id": "1abc...", "named_range_id": "nr_123"}
```

Data validation:

```json
{
  "action": "set_data_validation",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "range": "B2:B100",
  "validation_rule": {
    "condition": {"type": "ONE_OF_LIST", "values": [{"userEnteredValue": "New"}, {"userEnteredValue": "Qualified"}]},
    "strict": true,
    "showCustomUi": true
  }
}
```

Conditional formatting:

```json
{
  "action": "add_conditional_formatting",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "range": "B2:B100",
  "rule": {
    "booleanRule": {
      "condition": {"type": "TEXT_EQ", "values": [{"userEnteredValue": "Qualified"}]},
      "format": {"backgroundColor": {"red": 0.8, "green": 1, "blue": 0.8}}
    }
  }
}
```

Copy or cut/paste cells:

```json
{
  "action": "copy_paste",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "source_range": "A1:D20",
  "destination_range": "F1:I20",
  "paste_type": "PASTE_NORMAL"
}
```

```json
{
  "action": "cut_paste",
  "spreadsheet_id": "1abc...",
  "sheet_name": "Leads",
  "source_range": "A1:D20",
  "destination_range": "F1"
}
```

#### Other Actions

All actions below require `spreadsheet_id` except `create`, `search`, and
`get_instructions`. `sheet_name` is optional unless stated otherwise; use
`list_sheets` to discover its exact value. These examples omit the connected
account, which the platform supplies.

- `get_instructions`: no fields. `{"action":"get_instructions"}`
- `create`: `title` required; optional `initial_sheet_name`, `initial_headers`.
  `{"action":"create","title":"Weekly Posts","initial_sheet_name":"Posts","initial_headers":["post","status"]}`
- `search`: optional `query`, `max_results` (1-100).
  `{"action":"search","query":"Weekly Posts"}`
- `list_sheets`: `{"action":"list_sheets","spreadsheet_id":"1abc..."}`
- `get_headers`: optional `sheet_name`, `header_row` (default 1).
  `{"action":"get_headers","spreadsheet_id":"1abc...","sheet_name":"Posts"}`
- `get_data_range`: optional `sheet_name`, `range`; a partial range returns no
  append recommendation.
  `{"action":"get_data_range","spreadsheet_id":"1abc...","sheet_name":"Posts"}`
- `add_sheet`: `new_sheet_name` required.
  `{"action":"add_sheet","spreadsheet_id":"1abc...","new_sheet_name":"archive"}`
- `delete_sheet`: one of `sheet_name`, `sheet_id`, `sheet_index` required;
  permanently removes the whole tab.
  `{"action":"delete_sheet","spreadsheet_id":"1abc...","sheet_name":"Old Drafts"}`
- `rename_spreadsheet`: `spreadsheet_id` and nonblank `new_title` required. Renames the spreadsheet file, not any tab; its ID and URL stay the same.
  `{"action":"rename_spreadsheet","spreadsheet_id":"1abc...","new_title":"Social Posts 2026"}`
- `rename_sheet`: one tab selector and `new_sheet_name` required. Renames only that tab, not the spreadsheet file.
  `{"action":"rename_sheet","spreadsheet_id":"1abc...","sheet_name":"Drafts","new_sheet_name":"Queue"}`
- `sort`: `range` and `sort_specs` required; use an explicit header and order.
  `{"action":"sort","spreadsheet_id":"1abc...","sheet_name":"Posts","range":"A2:I50","sort_specs":[{"header":"status","order":"ASCENDING"}]}`
- `find_replace`: `find` and `replacement` required; add `sheet_name` to
  restrict the change to one tab.
  `{"action":"find_replace","spreadsheet_id":"1abc...","sheet_name":"Posts","find":"draft","replacement":"queued"}`
- `share`: `role` defaults to `reader`; for a person, `email` is required.
  `{"action":"share","spreadsheet_id":"1abc...","email":"editor@example.com","role":"writer"}`

#### Safety Guarantees

- `append_rows` never asks the agent to calculate an insertion point.
- `append_column` always appends one new column after the last non-empty data column.
- `update_row` touches only the named cells in `updates`.
- Specific-sheet CSV/TSV exports are generated from Sheets values with proper CSV quoting.
- Specific-sheet rendered exports without `pdf_options` use the official temporary-spreadsheet flow, not browser `gid` export URLs.
- `write_range` never replaces existing data unless `overwrite` is `true`.
- `merge_cells` never discards cell values unless `allow_value_loss` is `true`.
- Expected caller errors such as unknown sheet, duplicate headers, missing key row, or ambiguous row matches return safe messages without operator paging.

#### What Not To Do

- Do not use removed low-level action names.
- Do not guess a tab is named `"Sheet1"`; omit `sheet_name` or call `list_sheets`.
- Do not calculate raw append row numbers for table inserts; use `append_rows`.
- Do not calculate raw append column indexes; use `append_column`.
- Do not update an entire row when only a few fields changed; use `update_row`.
- Do not use browser export URLs or `gid` URL parameters for exports; use `export_sheet`.

## When To Use
- Use this skill for `Google Sheets` on AgentPMT.
- Use it when an agent needs this specific tool's behavior, schema, inputs, outputs, and invocation shape.
- Search and activation keywords: google sheets, google sheets api, append spreadsheet rows safely, update crm style rows by key, export a sheet to csv or pdf, create reporting spreadsheets, add conditional formatting, spreadsheet id.
- Supported action names: `add_conditional_formatting`, `add_named_range`, `add_sheet`, `append_column`, `append_rows`, `clear_range`, `copy_paste`, `create`, `cut_paste`, `delete_named_range`, `delete_note`, `delete_rows`, `delete_sheet`, `export_sheet`, `find_replace`, `format_cells`, `freeze`, `get_data_range`, `get_headers`, `list_notes`, `list_sheets`, `merge_cells`, `protect_range`, `read`, `rename_sheet`, `rename_spreadsheet`, `search`, `set_borders`, `set_column_widths`, `set_data_validation`, `set_gridlines`, `set_note`, `set_row_heights`, `share`, `sort`, `unmerge_cells`, `unprotect_range`, `update_row`, `write_range`.

## Use Cases
- append spreadsheet rows safely
- update CRM-style rows by key
- export a sheet to CSV or PDF
- create reporting spreadsheets
- add data validation to templates
- protect header ranges
- share sheets with collaborators
- copy or move spreadsheet ranges
- format dashboards
- manage sheet tabs
- lay out printable quotes and reports
- merge title cells and draw table borders
- set column widths and freeze header rows
- export a one-page portrait PDF without gridlines

## Related Product Skills
- File Management: ../file-management (ClawHub: `file-management`, page: https://clawhub.ai/agentpmt/file-management; skills.sh: `npx skills add AgentPMT/agent-skills --skill file-management`)

## Categories And Industries
No categories or industry tags are published for this tool.

## Actions And Schema
Complete generated action schema: `./schema.md`.
Supported action count: `39`.
x402 availability: not enabled for this product.

- `add_conditional_formatting` (action slug: `add-conditional-formatting`): Add a conditional formatting rule to a range. Price: `5` credits. Parameters: `range`, `rule`, `sheet_name`, `spreadsheet_id`.
- `add_named_range` (action slug: `add-named-range`): Create a named range. Price: `5` credits. Parameters: `name`, `range`, `sheet_name`, `spreadsheet_id`.
- `add_sheet` (action slug: `add-sheet`): Add a new tab to a spreadsheet. Price: `5` credits. Parameters: `new_sheet_name`, `spreadsheet_id`.
- `append_column` (action slug: `append-column`): Append one new column immediately after the last non-empty data column and write its header and values. Price: `5` credits. Parameters: `column_name`, `column_values`, `sheet_name`, `spreadsheet_id`.
- `append_rows` (action slug: `append-rows`): Append rows after Google's detected table. Object rows map to sheet headers. Returns appended_row_numbers from Google's actual updated range. Price: `5` credits. Parameters: `header_row`, `rows`, `sheet_name`, `spreadsheet_id`, `value_input_option`.
- `clear_range` (action slug: `clear-range`): Empty the values in an A1 range without deleting rows or columns. Notes and merges are kept; formatting is kept unless clear_formatting is true. Price: `5` credits. Parameters: `clear_formatting`, `range`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `copy_paste` (action slug: `copy-paste`): Copy cells to an A1 destination range; overwrites destination cells and does not insert rows. Price: `5` credits. Parameters: `destination_range`, `paste_orientation`, `paste_type`, `sheet_name`, `source_range`, `spreadsheet_id`.
- `create` (action slug: `create`): Create a new spreadsheet, optionally with an initial tab, headers, and rows. Price: `5` credits. Parameters: `initial_headers`, `initial_sheet_name`, `rows`, `title`.
- `cut_paste` (action slug: `cut-paste`): Move cells to an A1 destination start cell; does not insert rows. Returns destination_row_number. Price: `5` credits. Parameters: `destination_range`, `paste_type`, `sheet_name`, `source_range`, `spreadsheet_id`.
- `delete_named_range` (action slug: `delete-named-range`): Delete a named range by id. Price: `5` credits. Parameters: `named_range_id`, `spreadsheet_id`.
- `delete_note` (action slug: `delete-note`): Remove notes from every cell in a bounded A1 cell or range without changing values or formatting. Price: `5` credits. Parameters: `range`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `delete_rows` (action slug: `delete-rows`): Permanently delete complete worksheet rows by original one-based row number, from bottom to top. Requires a tab selector; row 1 is protected. Price: `5` credits. Parameters: `row_numbers`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `delete_sheet` (action slug: `delete-sheet`): Delete a tab by name, id, or index. Price: `5` credits. Parameters: `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `export_sheet` (action slug: `export-sheet`): Export a specific sheet or whole spreadsheet to File Manager as CSV, TSV, PDF, XLSX, ODS, HTML, or ZIP. For PDF, pdf_options sets the print layout (orientation, fit to one page, gridlines, margins). Price: `5` credits. Parameters: `expiration_days`, `filename`, `format`, `pdf_options`, `range`, `sheet_id`, `sheet_name`, `spreadsheet_id`.
- `find_replace` (action slug: `find-replace`): Find and replace text across the spreadsheet or one sheet. Price: `5` credits. Parameters: `find`, `match_case`, `match_entire_cell`, `replacement`, `search_by_regex`, `sheet_name`, `spreadsheet_id`.
- `format_cells` (action slug: `format-cells`): Apply cell formatting or number format to a range. Price: `5` credits. Parameters: `cell_format`, `number_format`, `range`, `sheet_name`, `spreadsheet_id`.
- `freeze` (action slug: `freeze`): Freeze the top rows and/or left columns of a tab so they stay visible while scrolling. 0 unfreezes. Frozen rows can repeat on every PDF page. Price: `5` credits. Parameters: `frozen_columns`, `frozen_rows`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `get_data_range` (action slug: `get-data-range`): Find the absolute one-based last non-empty row/column; a partial range never returns an append recommendation. Price: `5` credits. Parameters: `range`, `sheet_name`, `spreadsheet_id`.
- `get_headers` (action slug: `get-headers`): Read the header row and return header-to-column mappings plus duplicate diagnostics. Price: `5` credits. Parameters: `header_row`, `sheet_name`, `spreadsheet_id`.
- `list_notes` (action slug: `list-notes`): List cell notes with exact sheet and A1 locations plus the current cell values. Without a filter, scans every tab. Price: `5` credits. Parameters: `range`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `list_sheets` (action slug: `list-sheets`): List the tabs in a spreadsheet with sheet ids and dimensions. Price: `5` credits. Parameters: `spreadsheet_id`.
- `merge_cells` (action slug: `merge-cells`): Merge a bounded range of at least two cells. Only the top-left value of each merged area is kept, so the call fails and lists the cells that would lose values unless allow_value_loss is true. Price: `5` credits. Parameters: `allow_value_loss`, `merge_type`, `range`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `protect_range` (action slug: `protect-range`): Protect a range, optionally warning-only or with explicit editor emails. Price: `5` credits. Parameters: `description`, `editor_emails`, `range`, `sheet_name`, `spreadsheet_id`, `warning_only`.
- `read` (action slug: `read`): Read values from a tab or A1 range. Returns one-based row_numbers aligned with values; no row offset is needed. Price: `5` credits. Parameters: `range`, `sheet_id`, `sheet_name`, `spreadsheet_id`, `value_render_option`.
- `rename_sheet` (action slug: `rename-sheet`): Rename a tab by name, id, or index. Price: `5` credits. Parameters: `new_sheet_name`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `rename_spreadsheet` (action slug: `rename-spreadsheet`): Rename the spreadsheet file; does not rename any sheet tab. Price: `5` credits. Parameters: `new_title`, `spreadsheet_id`.
- `search` (action slug: `search`): Search or list recent Google Sheets spreadsheets. Price: `5` credits. Parameters: `max_results`, `query`.
- `set_borders` (action slug: `set-borders`): Draw or remove table borders on an A1 range using a preset, per-side borders, or both (per-side borders override the preset). Sides not given are left unchanged. Price: `5` credits. Parameters: `border_color`, `border_preset`, `border_style`, `borders`, `range`, `sheet_id`, `sheet_index`, `sheet_name`, plus 1 more.
- `set_column_widths` (action slug: `set-column-widths`): Set column widths in pixels and/or auto-fit columns to their contents. Provide column_widths, auto_fit, or both; explicit widths are applied after the auto-fit. Price: `5` credits. Parameters: `auto_fit`, `column_widths`, `range`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `set_data_validation` (action slug: `set-data-validation`): Set a Sheets data validation rule on a range. Price: `5` credits. Parameters: `range`, `sheet_name`, `spreadsheet_id`, `validation_rule`.
- `set_gridlines` (action slug: `set-gridlines`): Show or hide the gray cell gridlines on a tab. Price: `5` credits. Parameters: `sheet_id`, `sheet_index`, `sheet_name`, `show_gridlines`, `spreadsheet_id`.
- `set_note` (action slug: `set-note`): Set the same note on every cell in a bounded A1 cell or range. Price: `5` credits. Parameters: `note`, `range`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `set_row_heights` (action slug: `set-row-heights`): Set row heights in pixels and/or auto-fit rows to their contents. Provide row_heights, auto_fit, or both; explicit heights are applied after the auto-fit. Price: `5` credits. Parameters: `auto_fit`, `range`, `row_heights`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `share` (action slug: `share`): Share a spreadsheet with a user, group, domain, or anyone. Price: `5` credits. Parameters: `domain`, `email`, `permission_type`, `role`, `spreadsheet_id`.
- `sort` (action slug: `sort`): Sort a range, preferably by header name. Price: `5` credits. Parameters: `range`, `sheet_name`, `sort_specs`, `spreadsheet_id`.
- `unmerge_cells` (action slug: `unmerge-cells`): Unmerge every merged area that lies within an A1 range. Price: `5` credits. Parameters: `range`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`.
- `unprotect_range` (action slug: `unprotect-range`): Remove protection by protected range id. Price: `5` credits. Parameters: `protected_range_id`, `spreadsheet_id`.
- `update_row` (action slug: `update-row`): Update selected fields by header in a physical one-based row_number, or by a stable key; long-text exact matching is fragile. Price: `5` credits. Parameters: `key_column`, `key_value`, `multi`, `row_number`, `sheet_name`, `spreadsheet_id`, `updates`.
- `write_range` (action slug: `write-range`): Write values into exact cells, such as a title block or report layout. Refuses to replace cells that already hold data unless overwrite is true; grows the tab if values run past its grid. Price: `5` credits. Parameters: `overwrite`, `range`, `sheet_id`, `sheet_index`, `sheet_name`, `spreadsheet_id`, `values`.

## Live Schema And Examples
Use the compact schema above for ordinary calls. Before a new production integration, or whenever parameters, enum values, nested objects, outputs, or examples are unclear, fetch live details first.

- Exact schema: call `agentpmt-tool-search-and-execution` with `action: "get_schema"`, and `tool_id: "google-sheets-api"`.
- Detailed examples: call `agentpmt-tool-search-and-execution` with `action: "get_instructions"` and `tool_id: "google-sheets-api"`, or call this product with `action: "get_instructions"` when the product tool is already selected.
- Treat returned live schema and instructions as more specific than this generated summary.

MCP schema lookup through the main AgentPMT MCP server:

```json
{
  "method": "tools/call",
  "params": {
    "name": "AgentPMT-Tool-Search-and-Execution",
    "arguments": {
      "action": "get_schema",
      "tool_id": "google-sheets-api"
    }
  }
}
```

For live examples, keep the same MCP tool and use these arguments:

```json
{
  "action": "get_instructions",
  "tool_id": "google-sheets-api"
}
```

Authenticated AgentPMT REST schema lookup body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_schema",
    "tool_id": "google-sheets-api"
  }
}
```

Authenticated AgentPMT REST live examples body:

```json
{
  "name": "agentpmt-tool-search-and-execution",
  "parameters": {
    "action": "get_instructions",
    "tool_id": "google-sheets-api"
  }
}
```

## Call This Tool
Product slug: `google-sheets-api`

Marketplace page: https://www.agentpmt.com/marketplace/google-sheets-api

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
    "name": "Google-Sheets",
    "arguments": {
      "action": "add_conditional_formatting",
      "range": "example range",
      "rule": {},
      "sheet_name": "example sheet name",
      "spreadsheet_id": "example spreadsheet id"
    }
  }
}
```

Use the exact tool name returned by `tools/list`; the name above is the expected readable form.

Authenticated AgentPMT REST call body:

```json
{
  "name": "google-sheets-api",
  "parameters": {
    "action": "add_conditional_formatting",
    "range": "example range",
    "rule": {},
    "sheet_name": "example sheet name",
    "spreadsheet_id": "example spreadsheet id"
  }
}
```

Use the setup skill for the account connection details before making REST calls.

## Response Handling
- Treat the returned JSON as the source of truth for this tool call.
- If the response includes warnings or correction targets, apply them before retrying.
- If the response includes a `passed` or success-style boolean, use it as the workflow gate.
- If validation fails or the response shape is unclear, call `get_schema` or `get_instructions` before retrying.
- If `add_conditional_formatting` fails, preserve the request parameters and retry only after fixing schema, auth, or payment errors.

## Security
- Do not place account secrets, wallet private keys, mnemonics, signatures, or payment headers in prompts or logs.
- Keep tool inputs scoped to the minimum content needed for the task.
- Use the setup skills for credential handling; this product skill only defines product-specific behavior.

## AgentPMT Reference
- What AgentPMT is: ../what-is-agentpmt (ClawHub: `what-is-agentpmt`, page: https://clawhub.ai/agentpmt/what-is-agentpmt; skills.sh: `npx skills add AgentPMT/agent-skills --skill what-is-agentpmt`)
- AgentPMT account MCP/REST setup: ../agentpmt-account-mcp-rest-api-setup (ClawHub: `agentpmt-account-mcp-rest-api-setup`, page: https://clawhub.ai/agentpmt/agentpmt-account-mcp-rest-api-setup; skills.sh: `npx skills add AgentPMT/agent-skills --skill agentpmt-account-mcp-rest-api-setup`)
- Marketplace product: https://www.agentpmt.com/marketplace/google-sheets-api
- AgentPMT main MCP server: https://api.agentpmt.com/mcp/
- AgentPMT REST invoke endpoint: https://api.agentpmt.com/products/purchase
