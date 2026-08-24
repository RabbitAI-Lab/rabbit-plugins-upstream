# CLI Command Reference

Use this as the primary execution catalog. Use first-class `mbs` commands.

Install: `pip install maybeai-sheet-cli`

Required env: `MAYBEAI_API_TOKEN`

## Target Model Gate

The first command for an unfamiliar target is metadata, not a write:

```bash
mbs workbook metadata --doc-id <DOC_ID> --output json
mbs workbook list-worksheets --doc-id <DOC_ID> --output json
```

Choose one model from the returned metadata:

| Model | Required identity | Allowed command family |
|---|---|---|
| Excel Sheet | `worksheet_name`, optionally `gid` | `excel-worksheet`, `excel-table`, Sheet aliases, A1/cell Formula |
| Base Table | `table_id`, `field_id`, `record_id` or record key | P5 `base-table` records and column Formula |
| Worksheet SQL Config | result worksheet and config | `sql config`, `sql preview`, `sql overwrite` with raw SQL |

`mbs base-table` is the P5 command group for native Base records and column
Formula. Do not replace it with a range/cell, keep-headers, or worksheet-import
write. Use `mbs base-table --help` before relying on an unfamiliar flag.

## Shared Options

These flags work at the root, on most command groups, or on the leaf command:

| Flag | Purpose |
|------|---------|
| `--token` | API token; defaults to `MAYBEAI_API_TOKEN` |
| `--base-url` | API base; default `https://a-play-be.maybeai.cn`; env var `MAYBEAI_BASE_URL` |
| `--doc-id` | Workbook document ID |
| `--url` | MaybeAI workbook URL; parses doc id and gid when possible |
| `--uri` | Fully resolved workbook URI |
| `--gid` | Worksheet gid |
| `--worksheet-name` | Worksheet name |
| `--output` | `json` default, `table`, or `yaml` |
| `--verbose` | Include extra command metadata |
| `--timeout` | HTTP timeout seconds |

Always pass a leaf subcommand. `mbs workbook --doc-id <id>` alone is invalid.

## Workbook And Files

```bash
mbs workbook create --title "Board Pack"
mbs workbook create --title "Board Pack" --sheet-name Summary --data rows.json

# Create a new workbook from a local or remote source. No engine field is sent
# for the default Sheet import.
mbs workbook import ./report.xlsx
mbs workbook create-from-file ./report.xlsx

# Backend-selected per-worksheet engines for mixed workbooks.
mbs workbook import ./mixed-workbook.xlsx --engine auto

# Explicit per-worksheet engines by worksheet index.
mbs workbook import ./mixed-workbook.xlsx --engine "base,sheet,sheet,base"

# Base Mode import for large flat table-like files.
mbs workbook import ./large-table.xlsx --engine base
mbs workbook create-from-file ./large-table.xlsx --engine base

# Remote HTTPS Excel URL into a new workbook via /api/v1/excel/import_by_url.
mbs workbook import "https://static.example.com/imports/report.xlsx" --engine auto
mbs workbook import "https://static.example.com/download?id=123" --source-type xlsx --filename report.xlsx --engine sheet

# CSV/TSV/Google Sheet import-source flow into a new workbook.
mbs workbook import ./orders.csv --engine base
mbs workbook import ./orders.tsv --engine sheet
mbs workbook import "https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0" --engine base
mbs workbook import "https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0" --source-worksheet-name "1店" --worksheet-name "Store 1" --engine sheet
mbs workbook import ./orders.csv --preview-only --output json

# Import source worksheets/tabs into an existing workbook.
# Omit --source-worksheet-name to import all previewed worksheets/tabs.
mbs worksheet import --strategy create ./report.xlsx --doc-id <TARGET_DOC_ID> --engine base
mbs worksheet import --strategy create ./orders.csv --doc-id <TARGET_DOC_ID> --engine base
mbs worksheet import --strategy create "https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0" --doc-id <TARGET_DOC_ID> --engine sheet

# Pass one --source-worksheet-name to import one source worksheet/tab, optionally renamed.
mbs worksheet import --strategy create ./report.xlsx --doc-id <TARGET_DOC_ID> --source-worksheet-name "联盟" --target-worksheet-name "联盟导入" --engine base
mbs worksheet import --strategy create ./orders.csv --doc-id <TARGET_DOC_ID> --source-worksheet-name orders --target-worksheet-name Orders --engine base
mbs worksheet import --strategy create "https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0" --doc-id <TARGET_DOC_ID> --source-worksheet-name "1店" --target-worksheet-name "Store 1" --engine sheet

# Repeat --source-worksheet-name to import multiple selected source worksheets/tabs.
mbs worksheet import --strategy create ./report.xlsx --doc-id <TARGET_DOC_ID> --source-worksheet-name "联盟" --source-worksheet-name "订单" --engine base
mbs worksheet import --strategy create ./orders.tsv --doc-id <TARGET_DOC_ID> --source-worksheet-name orders --source-worksheet-name refunds --engine base
mbs worksheet import --strategy create "https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0" --doc-id <TARGET_DOC_ID> --source-worksheet-name "1店" --source-worksheet-name "2店" --engine sheet

# Cross-workbook worksheet -> raw Base-backed surface import.
mbs worksheet import --strategy create --doc-id <TARGET_DOC_ID> --source-doc-id <SOURCE_DOC_ID> --source-worksheet-name "1店" --verify
mbs worksheet import --strategy create --doc-id <TARGET_DOC_ID> --source-doc-id <SOURCE_DOC_ID> --source-worksheet-name "1店" --source-worksheet-name "2店" --verify

# Native cross-workbook import. Do not pass --engine; source metadata selects it.
mbs worksheet import --strategy create --transfer-mode native --doc-id <TARGET_DOC_ID> --source-doc-id <SOURCE_DOC_ID> --source-worksheet-name "S_financial_event_ledger" --target-worksheet-name "S_financial_event_ledger" --verify --output json
mbs worksheet import --strategy create --transfer-mode native --doc-id <TARGET_DOC_ID> --source-doc-id <SOURCE_DOC_ID> --verify

# Sheet only: replace data rows in one existing worksheet from a JSON object array.
mbs worksheet import ./rows.json --strategy replace --doc-id <TARGET_DOC_ID> --worksheet-name Students --verify

# Convert one existing Sheet-backed worksheet to Base. Always preflight first.
mbs worksheet convert-to-base --doc-id <DOC_ID> --worksheet-name Orders --dry-run
mbs worksheet convert-to-base --doc-id <DOC_ID> --gid <GID> --yes --verify
mbs worksheet convert-to-base --url "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?gid=<GID>" --yes --verify

mbs workbook metadata --doc-id <DOC_ID>
mbs workbook list-user-workbooks --limit 20
mbs workbook list-worksheets --doc-id <DOC_ID>
mbs workbook search --query "q2 forecast" --limit 20
mbs workbook copy --doc-id <DOC_ID> --title "Copy of Workbook"
mbs workbook delete --doc-id <DOC_ID> --yes

mbs workbook export --doc-id <DOC_ID> --out workbook.xlsx
mbs file list --limit 20
mbs file search --query "q2 forecast" --limit 20

# Workbook version history. Restore changes the entire workbook and requires --yes.
mbs history list --doc-id <DOC_ID> --limit 10 --output json
mbs history read --doc-id <DOC_ID> --version 3 --worksheet-name Sheet1 --range A1:C3 --output json
mbs history restore --doc-id <DOC_ID> --version 3 --reason "Restore verified version" --yes --output json
```

`workbook delete` soft-deletes the target workbook through the backend file
management route. It is destructive: pass `--yes` to execute, or use
`--dry-run` to inspect the resolved URI and request without sending it.

Accepted import engine values are omitted/`sheet` for the default Sheet mode
route, `base` for Base mode, `auto` for backend per-worksheet detection, or a
comma-separated per-worksheet list such as `base,sheet,sheet,base`. `auto` and
comma-separated engines apply to whole local Excel workbook imports. Remote
Excel URL imports accept one of `sheet`, `base`, or `auto`; comma-separated
engines are rejected. Local Excel worksheet append into an existing workbook
supports `sheet` or `base`. CSV/TSV/Google Sheet import-source selections
support `sheet`, `base`, or `auto`.
Base import owns DB-import preprocessing; the CLI only forwards the requested
engine intent.

Import routing:

- `.xls` / `.xlsx` / `.xlsm` without a target workbook: `/api/v1/excel/import`.
- Remote HTTPS `.xls` / `.xlsx` / `.xlsm` URL without a target workbook: `/api/v1/excel/import_by_url`. `--filename` is optional; the CLI uses the explicit value, then the decoded URL path basename, then `upload.xlsx`. For a download URL without an Excel suffix, pass `--source-type xlsx`. This mode rejects target workbook flags, worksheet selection flags, `--preview-only`, and comma-separated engines.
- `worksheet import` for `.xls` / `.xlsx` / `.xlsm` with `--doc-id` / `--url` / `--uri`: `/api/v1/excel/import_worksheet_preview` then `/api/v1/excel/import_worksheet_data`. Omit `--source-worksheet-name` to import all previewed worksheets, or repeat it to select worksheets.
- `.csv` / `.tsv` / public Google Sheet URL without a target workbook: `/api/v1/excel/import_sources/preview` then commit with `target.mode = new_workbook`. With no explicit selection, the backend imports all previewed worksheets/tabs.
- `.csv` / `.tsv` / public Google Sheet URL with `--doc-id` / `--url` / `--uri`: same preview route then commit with `target.mode = existing_workbook`; the CLI sends non-empty `selections`. Omit `--worksheet-name` to select all previewed worksheets/tabs, or repeat `--worksheet-name` to select specific worksheet/tab names. Missing requested names fail before commit and return the available worksheet names.
- No local/URL source plus `--source-doc-id` / `--source-url` and `--transfer-mode values`: CLI-composed cross-workbook raw Base-backed surface import.
- No local/URL source plus `--source-doc-id` / `--source-url` and `--transfer-mode native`: metadata-driven native worksheet import. Do not pass `--engine`.
- Both Maybe Sheet source modes accept repeated `--source-worksheet-name`; omitting it selects all metadata worksheets.

`workbook metadata` posts only the resolved URI to
`/api/v1/excel_v2/worksheet/metadata`. It returns worksheet routing metadata,
including engine, gid, and Base `table_id` where available. `manifest` and
`capabilities` are legacy compatibility commands and may still call
`/api/v1/excel/workbook_profile`.

For existing-workbook imports, `--target-worksheet-name` is only valid when
exactly one source worksheet/tab is selected.

For JSON replace, metadata must first confirm a Sheet target. `--worksheet-name`
identifies the existing target worksheet. The command keeps row 1 and calls
`/api/v1/excel/update_data_keep_headers`. The JSON file must be a non-empty
object array with keys matching existing headers. Do not pass `--engine`,
`--transfer-mode`, or source worksheet options. It is invalid for Base; Base
replacement must use P5 field-mapped record replace/upsert.

`worksheet convert-to-base` migrates one existing Sheet-backed worksheet to
Base through `/api/v1/excel/convert_to_base_mode`. Supply a workbook through
`--doc-id`, `--url`, or `--uri` and select the target by `--gid` or
`--worksheet-name`; a MaybeAI URL with `?gid=<GID>` can provide both. It is a
destructive, one-way data migration, so the command requires `--yes` unless
running `--dry-run`. Always run the dry run first. `--verify` reads selected
worksheet metadata and requires `data_engine: base`; it cannot be combined
with `--dry-run`. Use `--recalculate` to recalculate immediately after a real
migration. The default `--scrub-source-workbook` removes the old Sheet-engine
cell content after migration while preserving styles. Pass `--keep-sheet-source`
only when that source content must remain. There is no Base-to-Sheet conversion
command or backend endpoint.

For import-source existing-workbook commits that return exactly one worksheet,
the CLI top-level `target` should include `gid` and `worksheet_name` from
`result.worksheets[0]`. For multi-worksheet commits, treat top-level `target`
as workbook-level and inspect `result.worksheets`.

For cross-workbook raw-surface imports, successful `worksheet import` stdout plus
`--verify` is the creation evidence; do not follow it with per-table
native `schema`, `sample`, or `read` loops. If shape confirmation is needed,
resolve one representative table with `base-table metadata`, then run one
`mbs base-table sample --table-id <TABLE_ID> --limit 2` per family.

## Inspect And Target

```bash
mbs workbook list-worksheets --doc-id <DOC_ID> --output table
mbs excel-worksheet metadata --doc-id <DOC_ID> --worksheet-name Sheet1
mbs excel-worksheet list-table --doc-id <DOC_ID> --output json
mbs excel-worksheet list-table --doc-id <DOC_ID> --gid <GID> --output json
```

Prefer `workbook metadata` or `workbook list-worksheets` before writes on unfamiliar
workbooks. Use `--worksheet-name` for worksheet/range/formula work, `--table-id`
for `excel-table`, and `--name` or `--backend-id` for `base-table metadata`.
Use `excel-worksheet list-table --gid <GID>` to detect multiple content-backed
tables inside a visual Excel worksheet.

## Ranges And Worksheets

```bash
mbs excel-worksheet read --doc-id <DOC_ID> --worksheet-name Sheet1 --output table
mbs excel-worksheet read --doc-id <DOC_ID> --worksheet-name Sheet1 --range A1:D20 --output table
mbs excel-worksheet check-error --doc-id <DOC_ID> --worksheet-name Model
mbs excel-worksheet range write --doc-id <DOC_ID> --worksheet-name Sheet1 --range A1:C3 --values values.json --verify
mbs excel-worksheet range clear --doc-id <DOC_ID> --worksheet-name Sheet1 --range D1:F10
mbs excel-worksheet range search --doc-id <DOC_ID> --worksheet-name Sheet1 --query revenue --max-results 20
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --worksheet-name Sheet1 --cell E2 --formula '=SUM(B2:D2)'
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --operations formulas.json --recalculate-mode worksheet

mbs excel-worksheet create --doc-id <DOC_ID> --name Summary --values values.json
mbs excel-worksheet rename --doc-id <DOC_ID> --worksheet-name Old --new-name New
mbs excel-worksheet delete --doc-id <DOC_ID> --worksheet-name Temp --dry-run
mbs excel-worksheet delete --doc-id <DOC_ID> --worksheet-name Temp --yes
mbs excel-worksheet copy --doc-id <DOC_ID> --worksheet-name Sheet1 --new-name Copy
mbs excel-worksheet copy --doc-id <SOURCE_DOC_ID> --worksheet-name Sheet1 --target-doc-id <TARGET_DOC_ID> --new-name Copy  # fails fast; use base-table create-from-range
mbs excel-worksheet move --doc-id <DOC_ID> --worksheet-name Summary --index 0

# One-way Sheet -> Base engine migration. Use the dry run before --yes.
mbs worksheet convert-to-base --doc-id <DOC_ID> --worksheet-name Orders --dry-run
mbs worksheet convert-to-base --doc-id <DOC_ID> --gid <GID> --yes --verify
```

`excel-worksheet range write` defaults to RAW value handling through the backend. Numeric-looking
strings stay text unless a future command explicitly exposes USER_ENTERED.
`excel-worksheet check-error` reuses worksheet readback and returns formula-style
errors such as `#VALUE!` / `#REF!`, plus warnings when a formula cell has no
cached or display result in the response. Default to worksheet-wide scans; add
`--range` only for targeted debugging or when a large worksheet makes a bounded
check more practical.

## Excel Tables

Use `excel-table` for persistent Sheet-backed worksheet tables. Obtain
`--table-id` from `excel-table metadata` or `excel-worksheet list-table`; it is
the backend persistent ID, not a table position such as `1`. Omit it only when
selecting the first active table on an unambiguous worksheet. `--range` is not
supported for these commands.

```bash
mbs excel-table metadata --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID>
mbs excel-table headers --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID>
mbs excel-table schema --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID>
mbs excel-table sample --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID> --limit 50
mbs excel-table read --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID> --limit 100 --output table
mbs excel-table insert --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID> --rows rows.json
```

`headers` returns only the resolved table's header row. `metadata` returns the
current persistent table range. `read --limit N` returns
the header plus at most `N` data rows. `sample --limit N` returns named row
objects plus `sample_truncated` when more rows exist.

`rows.json` must be a non-empty array of objects whose keys exactly match the
current persistent table headers. The CLI validates every object, then appends
them to the next contiguous table rows. A 10-object file therefore appends 10
rows in one command. Insert has no `--verify`; read the table or the returned
range afterward. Re-read metadata immediately before a later insert if rows
were inserted or deleted, because the current table range can change.

## Base Tables

Use `base-table` for all new Base workflows. Resolve a table by human-readable
`--name` with `metadata`, then retain its returned native `table_id` for
schema, sample, read, record, and Formula operations. `db-table` remains a
compatibility surface only and is intentionally absent from new examples.

```bash
mbs base-table metadata --doc-id <DOC_ID> --name orders_large --include-headers --output json
mbs base-table schema --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table sample --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 50 --output table
mbs base-table read --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 100 --output table
mbs base-table create --doc-id <DOC_ID> --name Orders --rows orders.json
mbs base-table create --doc-id <DOC_ID> --name Orders --columns columns.json --rows rows.json --if-exists adopt --verify
mbs base-table create-from-range --doc-id <TARGET_DOC_ID> --name R_OrderLines_Store1 --source-doc-id <SOURCE_DOC_ID> --worksheet-name "1店" --range A2:AR423 --header-row 0 --use-header-names --if-exists adopt --verify
mbs base-table create-from-query --doc-id <DOC_ID> --name OrderSummary --sql-file order_summary.sql --if-exists adopt --verify
mbs base-table field list --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table field update --doc-id <DOC_ID> --name orders_large --field revenue --formatter "$#,##0.00" --verify
mbs base-table record create --doc-id <DOC_ID> --table-id <TABLE_ID> --records records.json
mbs base-table record replace --doc-id <DOC_ID> --table-id <TABLE_ID> --records records.json
mbs base-table record upsert --doc-id <DOC_ID> --table-id <TABLE_ID> --key-field-id <FIELD_ID> --records records.json
```

`base-table metadata` targets one Base-backed worksheet. Pass `--name`
or `--backend-id`; calling it with only `--doc-id` is invalid. Add
`--include-headers` when exact header text is needed. The CLI resolves the
table through `/api/v1/excel/worksheet/metadata`, then merges targeted
`/api/v1/excel/worksheet/dimensions`; with headers enabled, JSON output may
include `headers`, `header_names`, `header_count`, `headers_source`, and
`headers_exact`. Use `workbook list-worksheets` first when the table name is
unknown.

`orders.json` for `base-table create` must be a JSON array of row objects. The
CLI infers column names and logical types from those rows, then calls
`/api/v1/excel/db_table/create`. Pass `--columns columns.json` when rows are
empty or when the schema must be explicit. `--if-exists adopt` and
`--adopt-existing` adopt a matching existing Base-backed table after a 409 response; use
`--verify` to confirm the workbook registry reports a Base-backed
worksheet. `base-table create-from-range` is for cross-document raw `R_*`
surfaces: it reads a source worksheet range, treats `--header-row` as a
0-based index inside the returned values matrix, optionally uses header text
via `--use-header-names` (otherwise `raw_col_NNN`), drops blank rows, and
creates the named Base-backed table on the target `--doc-id`. Prefer it over
hand-written import Python. For merged-title sheets, start `--range` at the
semantic header row. `base-table create-from-query` is for SQL-materialized Base-backed
handoff tables. It sends raw SQL to `/api/v1/excel/sql/result/query`, derives
the source relations from `FROM`/`JOIN`, parses table-shaped `values` /
`range_values`, and consumes the ordered typed `columns` schema when present,
then creates the `--name` output table through `/api/v1/excel/db_table/create`.
The schema's `pg_type` is the physical type authority; value-shape inference is
only a legacy fallback for responses that do not provide typed columns. It does
not accept `--worksheet-name`; `--gid`
is optional compatibility context and does not choose a source relation. In a
Base source, select quoted field display names, not `field_id` values such as
`col_000001`; `SELECT *` returns each display column exactly once. Use
`--sql-file` for auditable ETL templates. The deprecated `--preserve-formula`
flag is ignored; attach a query to a worksheet with `mbs sql config set` when
traceability must remain live. After create, verify with `base-table metadata`,
`base-table sample`, or `workbook list-worksheets`.

### P5 Base mutations

The command names are `base-table read`, `base-table record replace`,
`base-table record upsert`, `base-table field list`, and `base-table formula
compile/set/recalculate`.

```bash
mbs base-table read --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 100 --output table
mbs base-table field list --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table record replace --doc-id <DOC_ID> --table-id <TABLE_ID> --records records.json
mbs base-table record upsert --doc-id <DOC_ID> --table-id <TABLE_ID> --key-field-id <KEY_FIELD_ID> --records records.json
mbs base-table formula compile --doc-id <DOC_ID> --table-id <TABLE_ID> --field-id <FIELD_ID> --expression '<EXPRESSION>'
mbs base-table formula set --doc-id <DOC_ID> --table-id <TABLE_ID> --field-id <FIELD_ID> --expression '<EXPRESSION>'
mbs base-table formula recalculate --doc-id <DOC_ID> --worksheet-name <BASE_WORKSHEET> --table-id <TABLE_ID>
```

A Base mutation must resolve `table_id`, writable `field_id`s, and a `record_id`
or stable record key. `records.json` is a JSON array with `field_id` keys;
Formula/read-only fields are not data-write targets. Use `--expected-revision`
when the write must enforce optimistic concurrency. Do not replace any of these
with a Sheet-style write.

## SQL

Use `mbs sql` for first-class Worksheet SQL Config and raw SQL query execution.

```bash
mbs sql config get --doc-id <DOC_ID> --worksheet-name SqlResult
mbs sql config set --doc-id <DOC_ID> --worksheet-name SqlResult --sql-file result.sql --auto-refresh
mbs sql config delete --doc-id <DOC_ID> --worksheet-name SqlResult
mbs sql preview --doc-id <DOC_ID> --worksheet-name SqlResult --sql-file result.sql --output table
mbs sql query --doc-id <DOC_ID> --sql-file result.sql --limit 100 --output table
mbs sql overwrite --doc-id <DOC_ID> --worksheet-name SqlResult --confirm-overwrite
mbs sql migration preview --doc-id <DOC_ID>
mbs sql migration commit --doc-id <DOC_ID> --candidate-id <CANDIDATE_ID> --allow-manual-candidates
```

`sql config set`, `sql preview`, `sql query`, and `sql overwrite` accept raw
SQL via `--sql` or `--sql-file` and reject legacy wrapped formula input.
`sql preview` is read-only. `sql overwrite` materializes the current reviewed
raw-SQL result to its configured target. It must not be represented as a cell
formula or as a Base column Formula. Review the preview or backend impact
response before materialization.

Use `base-table field list` and `base-table field update` for Base-backed
field display metadata. `property.formatter` controls display format, while
other supported field properties control presentation. Prefer native
`--table-id --field-id`; `--name --field` is supported when the CLI must resolve
the IDs first:

```bash
mbs base-table field list --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table field update --doc-id <DOC_ID> --table-id <TABLE_ID> --field-id <FIELD_ID> --formatter "$#,##0.00" --verify
mbs base-table field update --doc-id <DOC_ID> --name orders_large --field revenue --formatter "$#,##0.00" --verify
```

The legacy `db-table field batch-update` command is compatibility-only and is
not a current documentation example.

For the newer `workbook import` raw-surface path, prefer that command family
over teaching a post-import verification loop. When `workbook import ... --verify`
succeeds, use that stdout as the existence proof. Only run one representative
`base-table metadata` plus `base-table sample --table-id <TABLE_ID> --limit 2`
per family when a human needs quick shape confirmation.

## Sheet Rows, Columns, Formulas, and Styles

Everything in this section requires `engine=sheet`. Base Tables do not accept
row/column coordinates, A1 ranges, cell Formula, or worksheet calculation.

```bash
mbs excel-worksheet row insert --doc-id <DOC_ID> --worksheet-name Sheet1 --row 10 --count 2
mbs excel-worksheet row delete --doc-id <DOC_ID> --worksheet-name Sheet1 --row 10 --count 2 --yes
mbs excel-worksheet row move --doc-id <DOC_ID> --worksheet-name Sheet1 --row 10 --count 2 --destination-row 20

mbs excel-worksheet column insert --doc-id <DOC_ID> --worksheet-name Sheet1 --column B --count 2
mbs excel-worksheet column delete --doc-id <DOC_ID> --worksheet-name Sheet1 --column B --count 2 --yes
mbs excel-worksheet column move --doc-id <DOC_ID> --worksheet-name Sheet1 --column B --count 2 --destination-column D
mbs excel-worksheet column width --doc-id <DOC_ID> --worksheet-name Sheet1 --start-column B --end-column D --width 120px

mbs formula read --doc-id <DOC_ID> --worksheet-name Model --range A1:E20
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --worksheet-name Model --cell E2 --formula '=SUM(B2:D2)'
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --operations ops.json --recalculate-mode worksheet
mbs formula batch-set --doc-id <DOC_ID> --operations ops.json --recalculate-mode worksheet
mbs workbook calculate --doc-id <DOC_ID>
mbs excel-worksheet calculate --doc-id <DOC_ID> --worksheet-name Model
mbs excel-worksheet range calculate --doc-id <DOC_ID> --worksheet-name Model --cell E2 --formula '=SUM(B2:D2)' --no-save-result
mbs formula calculate --doc-id <DOC_ID> --worksheet-name Model --cell E2 --formula '=SUM(B2:D2)' --save-result
mbs excel-worksheet check-error --doc-id <DOC_ID> --worksheet-name Model
mbs formula lineage --doc-id <DOC_ID> --worksheet-name Model --cell E2 --format tree

mbs excel-worksheet style freeze-panes --doc-id <DOC_ID> --worksheet-name Sheet1 --cell B2
mbs excel-worksheet style cell batch-set --doc-id <DOC_ID> --worksheet-name Sheet1 --range A1:G1 --style header_style.json
mbs excel-worksheet style auto-filter set --doc-id <DOC_ID> --worksheet-name Sheet1 --range A1:G100
mbs excel-worksheet style auto-filter remove --doc-id <DOC_ID> --worksheet-name Sheet1
mbs excel-worksheet style gridlines toggle --doc-id <DOC_ID> --worksheet-name Sheet1 --show-gridlines false
mbs excel-worksheet style filter-values --doc-id <DOC_ID> --worksheet-name Sheet1 --range A1:G100 --column 2 --filters-active true --already-checked APAC --already-checked EMEA
mbs excel-worksheet style conditional-formats set --doc-id <DOC_ID> --worksheet-name Sheet1 --spec conditional_formats.json
mbs excel-worksheet style columns-width --doc-id <DOC_ID> --worksheet-name Sheet1 --start-column B --end-column D --width 120px
mbs excel-worksheet style rows-height --doc-id <DOC_ID> --worksheet-name Sheet1 --start-row 1 --end-row 1 --height 28px
mbs excel-worksheet style worksheet plan --doc-id <DOC_ID> --worksheet-name Sheet1 --mode auto_detect --spec worksheet_style.json
mbs excel-worksheet style worksheet apply --doc-id <DOC_ID> --worksheet-name Sheet1 --mode auto_detect --spec worksheet_style.json
mbs style beautify --doc-id <DOC_ID> --worksheet-name Sheet1 --dry-run --output json
mbs style beautify --doc-id <DOC_ID> --worksheet-name Sheet1 --output json
```

Run `mbs <group> <command> --help` for exact row/column JSON shapes before
structural edits.

`mbs style beautify` is the recommended one-command report/table polish path.
It inspects metadata first, classifies columns from Chinese/English headers and
sample values, applies header freeze/filter and semantic styles for Sheet worksheets,
and applies Base-backed formatter/style/header metadata through batched field
updates when possible. Use `--dry-run --output json` to inspect each column's
category, formatter, confidence, and reasons before mutation.

## Charts, Images, And Dashboards

```bash
mbs workbook list-worksheets --doc-id <DOC_ID> --output json
mbs excel-worksheet chart list --doc-id <DOC_ID> --worksheet-name Dashboard
mbs excel-worksheet chart get --doc-id <DOC_ID> --worksheet-name Dashboard --cell J2
mbs excel-worksheet chart create-config --doc-id <DOC_ID> --worksheet-name Dashboard --cell J2 --spec chart.json
mbs excel-worksheet chart create-config --doc-id <DOC_ID> --worksheet-name Dashboard --spec chart-with-cell.json
mbs excel-worksheet chart update --doc-id <DOC_ID> --worksheet-name Dashboard --cell J2 --chart-id rId1 --spec chart.json
mbs excel-worksheet chart delete --doc-id <DOC_ID> --worksheet-name Dashboard --chart-id rId1

# recommendation:
# author `chart.json` with top-level `"type": "json"` and renderer code in `html`
# do not default to authoring chart specs as top-level `"type": "line"` / `"bar"` / `"pie"`

mbs excel-worksheet image list --doc-id <DOC_ID> --worksheet-name Dashboard
mbs excel-worksheet image read --doc-id <DOC_ID> --worksheet-name Dashboard --cell A1 --out logo.png
mbs excel-worksheet image insert --doc-id <DOC_ID> --worksheet-name Dashboard --cell B3 --file logo.png --alt-text "Company logo" --format picture-format.json
mbs excel-worksheet image set --doc-id <DOC_ID> --worksheet-name Dashboard --old-cell B3 --cell B3 --format picture-format.json --width 120 --height 91
mbs excel-worksheet image replace --doc-id <DOC_ID> --worksheet-name Dashboard --cell B3 --file logo_v2.png --format picture-format.json
mbs excel-worksheet image delete --doc-id <DOC_ID> --worksheet-name Dashboard --cell A1
mbs excel-worksheet media check --doc-id <DOC_ID> --worksheet-name Dashboard

mbs excel-worksheet dashboard validate --spec dashboard.json
mbs excel-worksheet dashboard refresh --doc-id <DOC_ID> --spec dashboard.json --dry-run
mbs excel-worksheet dashboard manifest --doc-id <DOC_ID> --worksheet-name Dashboard
mbs excel-worksheet dashboard create-config --doc-id <DOC_ID> --spec dashboard.json --create-worksheet
mbs excel-worksheet dashboard refresh --doc-id <DOC_ID> --spec dashboard.json
mbs excel-worksheet dashboard export-template --doc-id <DOC_ID> --worksheet-name Dashboard --template-id <template-id> --out-dir <analysis-style-system-skill-dir>/dashboard-templates/<template-id> --force
```

`picture-format.json` uses the same anchor model as chart layout:

```json
{
  "from": {"col": 1, "row": 2, "col_off": 0, "row_off": 0},
  "to": {"col": 4, "row": 10, "col_off": 0, "row_off": 0}
}
```

Use zero-based `row` / `col` indexes in the format JSON. Keep the outer
`--cell` aligned with `format.from` when possible.

Notes:

- For dashboard authoring, prefer: `sheet-dashboard` generates `dashboard.json`, then `mbs excel-worksheet dashboard validate/refresh/manifest` executes and verifies it.
- For reusable dashboard HTML template extraction, use `dashboard export-template`; it requires a `sheet` dashboard canvas, selects one persisted `chart.type=html` chart, and writes `template.json`, `html/dashboard.template.html`, and `html/runtime-payload.schema.json` for `analysis-style-system/dashboard-templates/<template-id>`.
- If `dashboard_style_pack` is present in `dashboard.json`, also include the matching `industry_style` and `dashboard_story`; `dashboard validate` now checks this style linkage explicitly.
- Author `chart.json` with top-level `"type": "json"` and renderer code in `html`.
- `chart-with-cell.json` may be either flat `{cell,type,sql,html,...}` or `{cell,chart:{type,sql,html,...}}`.
- Do not default to authoring chart specs as top-level `"type": "line"`, `"bar"`, or `"pie"`.
- `chart get` resolves one chart by `--cell` or `--chart-id` after reading the worksheet chart inventory.
- Images are floating worksheet objects like charts, not values inserted inside cells.
- Images require an Sheet-backed worksheet. Check `workbook list-worksheets --output json` first; Base-only worksheets do not support `add_picture`, and `excel-worksheet create` in a Base Mode workbook may create a Base-only sheet. For a new image canvas, import a small blank `.xlsx` with `--engine sheet`.
- `image list` extracts picture metadata from worksheet formatting; use returned URL/media fields, anchor cell, picture id, and chart-compatible format/position fields for display and later updates.
- `image read` reads one concrete picture by `--cell` or `--picture-id`.
- `image insert` and `image set` should include `--format picture-format.json` when layout matters; `cell` alone is only an anchor and is not enough to preserve drag/resize position.
- `image replace` is an `mbs` orchestration: read existing picture, delete it, then insert the replacement at the resolved cell.
- `media check` quickly verifies whether the worksheet contains image objects and chart objects after `add_picture`, image insert/set, chart create, or dashboard refresh.
- `dashboard validate` is local-only. `dashboard create-config`, `manifest`, and `refresh` are worksheet-level `mbs` orchestrations over existing routed endpoints.
- If dashboard batch refresh/create-config fails with a server-side batch error, retry with per-chart `chart create-config --cell <CELL> --spec <single_chart.json>`.
- `dashboard manifest` and `chart list` verify persisted chart metadata, not browser canvas rendering.

## Pivot Tables

Use `mbs pivot` for persisted pivot tables. Do not use `mbs raw post` for
`/api/v1/excel/pivot_table/*`, `/api/v1/excel/read_pivot_table`, or legacy
`/api/pivot_table/*` when these commands are available.

```bash
mbs pivot read --doc-id <DOC_ID> --worksheet-name SourceData --spec pivot-config.json --output json
mbs pivot preview --doc-id <DOC_ID> --worksheet-name SourceData --spec pivot-config.json --output json
mbs pivot upsert --doc-id <DOC_ID> --target-worksheet-name PivotResult --anchor-cell A1 --spec pivot-config.json
mbs pivot upsert --doc-id <DOC_ID> --target-worksheet-name PivotResult --anchor-cell A1 --spec pivot-config.json --dry-run
mbs pivot delete --doc-id <DOC_ID> --worksheet-name PivotResult --anchor-cell A1 --dry-run
mbs pivot delete --doc-id <DOC_ID> --worksheet-name PivotResult --anchor-cell A1 --yes
```

`pivot-config.json` for `preview` and the usual `upsert` path is the pivot
config object. A reusable copy lives at [../artifacts/pivot-config.json](../artifacts/pivot-config.json).

```json
{
  "worksheet_name": "SourceData",
  "range_address": "A1:E1001",
  "row_fields": ["period", "dimension_type"],
  "column_fields": [],
  "metrics": [
    {
      "aggregate": "sum",
      "value_field": "settled_amount_reporting",
      "label": "settled_revenue_reporting"
    }
  ],
  "row_sort": {"by": "label", "order": "asc"},
  "show_row_totals": false,
  "show_column_totals": false
}
```

`pivot read` uses the older read shape and supports one metric. If the spec
contains a single `metrics[]` item, the CLI converts it to `aggregate` and
`value_field`; for multi-metric output use `pivot preview`.

`pivot upsert` writes the pivot through the semantic pivot endpoint and requires
an explicit `--anchor-cell`. The target worksheet can be created by the backend
semantic path; do not pre-create it just to call pivot upsert. `preview` is the
right command before mutation when comparing output shape or sort behavior.

See [pivot-tables.md](pivot-tables.md) for field rules, common spec patterns,
and verification commands.

## History And Sharing

```bash
mbs history list --doc-id <DOC_ID> --limit 10
mbs history read --doc-id <DOC_ID> --version <VERSION_ID>

mbs share permission --doc-id <DOC_ID>
mbs share visibility --doc-id <DOC_ID> --visibility public --public-permission viewer
mbs share visibility --doc-id <DOC_ID> --visibility private
mbs share grant --doc-id <DOC_ID> --email user@example.com --permission viewer
mbs share grant --doc-id <DOC_ID> --email user@example.com --permission editor
mbs share remove --doc-id <DOC_ID> --email user@example.com
mbs share list --doc-id <DOC_ID>
```

Only owners can change visibility, grant access, remove access, or list shares.

## Raw API Escape Hatch

Use first-class commands first. When an uncovered endpoint is required:

```bash
mbs raw post /api/v1/excel/sql/compile --body body.json
mbs raw post /api/v1/excel/sql/write_result --body body.json
mbs raw post /api/v1/excel/get_charts --json '{"document_id":"<DOC_ID>","worksheet_name":"Dashboard"}'
mbs raw post /api/v1/excel/get_charts --body get_charts_body.json
```

`--json` takes an inline JSON object. `--body` takes a path to a JSON file. Do not pass inline JSON to `--body`.

If a workflow is not exposed through a first-class command, check `mbs --help`
and pause for a supported command or backend route.

## Legacy Aliases

The `sheet` group remains for **Sheet-only** compatibility:

```bash
mbs sheet read --doc-id <DOC_ID> --worksheet-name Sheet1 --range A1:D20
mbs sheet worksheets --doc-id <DOC_ID>
mbs sheet update-data-keep-headers --doc-id <DOC_ID> --worksheet-name Sheet1 --data rows.json --dry-run
mbs sheet update-data-keep-headers --doc-id <DOC_ID> --worksheet-name Sheet1 --data rows.json --verify
mbs sheet update-data-keep-headers --doc-id <DOC_ID> --gid 1 --data rows.json --start-row 2 --no-preserve-formulas --skip-recalculation
mbs sheet append --doc-id <DOC_ID> --gid 0 --rows rows.json --verify
mbs sheet upsert --doc-id <DOC_ID> --gid 0 --key order_id --rows rows.json --verify
```

`update-data-keep-headers` is the supported Sheet full-refresh command even
though it lives under `sheet`. It accepts only a non-empty JSON object array,
performs a header preflight, preserves Sheet formulas, and clears stale Sheet
rows after the replacement dataset. Run `--dry-run` before the first write and
`--verify` on execution. The two flags cannot be combined. Reject it for Base.

## Help Discovery

```bash
mbs --help
mbs workbook import --help
mbs excel-worksheet read --help
mbs excel-table read --help
mbs base-table read --help
```
