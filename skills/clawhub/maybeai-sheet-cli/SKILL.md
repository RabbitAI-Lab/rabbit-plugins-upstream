---
version: "0.20.4"
name: maybeai-sheet-cli
description: Use when the user works with MaybeAI spreadsheets through the mbs CLI for workbook inspection, local or remote-URL file import, native cross-workbook import/export, worksheet/range/table writes, full worksheet data refreshes that keep headers, formulas, worksheet styling, chart/image CRUD, dashboard validate/refresh/export-template flows, or sharing. Route dashboard design and chart composition to `sheet-dashboard`.
metadata:
  cli_version: "0.25.0"
  openclaw:
    requires:
      env:
        - MAYBEAI_API_TOKEN
    primaryEnv: MAYBEAI_API_TOKEN
    emoji: "📊"
    homepage: https://github.com/OmniMCP-AI/maybeai-uni
required_environment_variables:
  - name: MAYBEAI_API_TOKEN
---

# MaybeAI Sheet CLI

Execute spreadsheet work through `mbs`, the console script from
`maybeai-sheet-cli`. Use first-class object commands.

## Target model gate

Before choosing a command, determine the target model from `mbs workbook
metadata` or `mbs workbook list-worksheets --output json`. A worksheet name or
`gid` is only a locator; it does not prove the target supports cells or ranges.

| Target model | Required identity | Use | Do not use |
|---|---|---|---|
| Excel Sheet | `worksheet_name` (and `gid` when needed) | A1 ranges, cell formulas, worksheet calculation, layout and media | Base record/field APIs as a substitute for cell layout |
| Base Table | `table_id`, `field_id`, and `record_id` | record replace/upsert and column Formula operations | A1/range writes, cell formulas, `update_data_keep_headers`, row-template preservation |
| Worksheet SQL Config | SQL-config worksheet identity plus raw SQL | `mbs sql config`, preview, and materialization | a legacy SQL cell wrapper or any other cell-formula wrapper |

Do not infer the model from a worksheet's name, a deprecated `db-table`
compatibility alias, or its
visual appearance. If metadata does not return an engine and Base identity,
stop before a mutation and obtain that metadata. The Base command surface named
in P5 is `mbs base-table read`, `record replace`, `record upsert`, `field
list`, and `formula compile/set/recalculate`. It is available in the current
CLI; use `mbs base-table --help` to confirm flags before a new workflow. Do not
substitute an A1/range or keep-headers command for a Base write.

For local `.xls` / `.xlsx` imports, choose the engine per worksheet when a
workbook mixes large table-like sheets and Excel-layout sheets. The workbook
import commands support `--engine auto`, `--engine base`, and
comma-separated worksheet engine lists. CSV/TSV files and public Google Sheet
URLs use the import-source preview flow and can import as a new workbook or
append all or selected worksheets/tabs to an existing workbook. Remote HTTPS
Excel URLs create a new workbook through `/api/v1/excel/import_by_url`.
To migrate one existing Sheet-backed worksheet to Base, use the guarded
`worksheet convert-to-base` workflow below; it is a one-way data migration,
not an import-engine setting.

**Prerequisites:** `MAYBEAI_API_TOKEN`, `mbs` (`pip install maybeai-sheet-cli`)

**Delegated subagent rule.** For a delegated MaybeAI task, use `terminal` first:
`mbs --version` and `test -n "$MAYBEAI_API_TOKEN"`. Do not infer missing mbs,
terminal, or token from old files, logs, or JSON artifacts. Only report a
missing token when that command actually shows it is absent.

## Quick start

```bash
# Inspect before writing
mbs workbook metadata --doc-id <DOC_ID>
mbs workbook list-worksheets --doc-id <DOC_ID> --output table

# Excel Sheet only: read and write cells/ranges
mbs excel-worksheet read --doc-id <DOC_ID> --worksheet-name Sheet1 --output table
mbs excel-worksheet read --doc-id <DOC_ID> --worksheet-name Sheet1 --range A1:D20 --output table
mbs excel-worksheet check-error --doc-id <DOC_ID> --worksheet-name Model
mbs excel-worksheet range write --doc-id <DOC_ID> --worksheet-name Sheet1 --range A1:C3 --values values.json --verify
mbs sheet update-data-keep-headers --doc-id <DOC_ID> --worksheet-name Sheet1 --data rows.json --verify

# Inspect table-shaped data
mbs excel-worksheet list-table --doc-id <DOC_ID> --gid <GID> --output json
mbs excel-table headers --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID> --output json
mbs excel-table metadata --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID> --output json
mbs excel-table sample --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID> --limit 20 --output table
mbs excel-table insert --doc-id <DOC_ID> --worksheet-name Orders --table-id <PERSISTENT_TABLE_ID> --rows orders.json
mbs base-table metadata --doc-id <DOC_ID> --name orders_large --include-headers --output json
mbs base-table schema --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table sample --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 20 --output table
mbs base-table read --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 100 --output table
mbs base-table create --doc-id <DOC_ID> --name Orders --rows orders.json
mbs base-table create --doc-id <DOC_ID> --name Orders --columns columns.json --rows rows.json --if-exists adopt --verify
mbs base-table create-from-range --doc-id <TARGET_DOC_ID> --name R_OrderLines_Store1 --source-doc-id <SOURCE_DOC_ID> --worksheet-name "1店" --range A2:AR423 --header-row 0 --use-header-names --if-exists adopt --verify
# --name is the output Base table; FROM/JOIN determines SQL sources.
mbs base-table create-from-query --doc-id <DOC_ID> --name OrderSummary --sql-file order_summary.sql --if-exists adopt --verify
mbs base-table field metadata --doc-id <DOC_ID> --name orders_large --output json
mbs base-table field update --doc-id <DOC_ID> --name orders_large --field amount --formatter "#,##0.00" --verify

# Base Table records and column Formulas (field-id records JSON)
mbs base-table field list --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
mbs base-table record create --doc-id <DOC_ID> --table-id <TABLE_ID> --records records.json
mbs base-table record replace --doc-id <DOC_ID> --table-id <TABLE_ID> --records records.json
mbs base-table record upsert --doc-id <DOC_ID> --table-id <TABLE_ID> --key-field-id <FIELD_ID> --records records.json
mbs base-table formula set --doc-id <DOC_ID> --table-id <TABLE_ID> --field-id <FIELD_ID> --expression '<EXPRESSION>'
mbs base-table formula recalculate --doc-id <DOC_ID> --worksheet-name <BASE_WORKSHEET> --table-id <TABLE_ID>

# Import files
mbs workbook import ./report.xlsx
mbs workbook import ./mixed-workbook.xlsx --engine auto
mbs workbook import ./mixed-workbook.xlsx --engine "base,sheet,sheet,base"
mbs workbook import ./large-table.xlsx --engine base
mbs workbook import "https://static.example.com/imports/report.xlsx" --engine auto
mbs workbook import "https://static.example.com/download?id=123" --source-type xlsx --filename report.xlsx --engine sheet
mbs workbook import ./orders.csv --engine base
mbs workbook import ./orders.tsv --engine sheet
mbs workbook import "https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0" --engine base
mbs worksheet import ./report.xlsx --strategy create --doc-id <TARGET_DOC_ID> --engine base --verify
mbs worksheet import ./report.xlsx --strategy create --doc-id <TARGET_DOC_ID> --source-worksheet-name "联盟" --target-worksheet-name "联盟导入" --engine base --verify
mbs worksheet import ./report.xlsx --strategy create --doc-id <TARGET_DOC_ID> --source-worksheet-name "联盟" --source-worksheet-name "订单" --engine base --verify
mbs worksheet import ./orders.csv --strategy create --doc-id <TARGET_DOC_ID> --engine base --verify
mbs worksheet import ./orders.csv --strategy create --doc-id <TARGET_DOC_ID> --source-worksheet-name orders --target-worksheet-name Orders --engine base --verify
mbs worksheet import ./orders.csv --strategy create --doc-id <TARGET_DOC_ID> --source-worksheet-name orders --source-worksheet-name refunds --engine base --verify
mbs worksheet import "https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0" --strategy create --doc-id <TARGET_DOC_ID> --engine sheet --verify
mbs worksheet import "https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0" --strategy create --doc-id <TARGET_DOC_ID> --source-worksheet-name "1店" --target-worksheet-name "Store 1" --engine sheet --verify
mbs worksheet import "https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0" --strategy create --doc-id <TARGET_DOC_ID> --source-worksheet-name "1店" --source-worksheet-name "2店" --engine sheet --verify
# Sheet only, after metadata confirms engine=sheet
mbs worksheet import ./rows.json --strategy replace --doc-id <TARGET_DOC_ID> --worksheet-name Students --verify
mbs worksheet import --strategy create --doc-id <TARGET_DOC_ID> --source-doc-id <SOURCE_DOC_ID> --source-worksheet-name "1店" --verify
mbs worksheet import --strategy create --doc-id <TARGET_DOC_ID> --source-doc-id <SOURCE_DOC_ID> --source-worksheet-name "1店" --source-worksheet-name "2店" --verify
mbs worksheet import --strategy create --transfer-mode native --doc-id <TARGET_DOC_ID> --source-doc-id <SOURCE_DOC_ID> --source-worksheet-name "工作表3" --source-worksheet-name "工作簿1" --verify
# Convert one existing Sheet worksheet to Base: dry-run first, then confirm.
mbs worksheet convert-to-base --doc-id <DOC_ID> --worksheet-name Orders --dry-run
mbs worksheet convert-to-base --doc-id <DOC_ID> --gid <GID> --yes --verify
mbs workbook copy --doc-id <DOC_ID> --title "Copy of Workbook"
mbs workbook export --doc-id <DOC_ID> --out workbook.xlsx --output json

# Formulas and sharing
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --worksheet-name Model --cell E2 --formula '=SUM(B2:D2)'
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --operations formulas.json --recalculate-mode worksheet
mbs sql config set --doc-id <DOC_ID> --worksheet-name SqlResult --sql-file result.sql --auto-refresh
mbs sql preview --doc-id <DOC_ID> --worksheet-name SqlResult --sql-file result.sql --output table
mbs sql overwrite --doc-id <DOC_ID> --worksheet-name SqlResult --confirm-overwrite
mbs workbook calculate --doc-id <DOC_ID>
mbs history list --doc-id <DOC_ID> --limit 10 --output json
mbs history read --doc-id <DOC_ID> --version 3 --worksheet-name Sheet1 --range A1:C3 --output json
mbs history restore --doc-id <DOC_ID> --version 3 --reason "Restore verified version" --yes --output json
mbs excel-worksheet calculate --doc-id <DOC_ID> --worksheet-name Model
mbs excel-worksheet range calculate --doc-id <DOC_ID> --worksheet-name Model --cell E2 --formula '=SUM(B2:D2)' --no-save-result
mbs formula calculate --doc-id <DOC_ID> --worksheet-name Model --cell E2 --formula '=SUM(B2:D2)' --save-result
mbs share permission --doc-id <DOC_ID>
mbs excel-worksheet chart list --doc-id <DOC_ID> --worksheet-name Dashboard
mbs excel-worksheet image list --doc-id <DOC_ID> --worksheet-name Dashboard
mbs excel-worksheet image set --doc-id <DOC_ID> --worksheet-name Dashboard --old-cell B3 --cell B3 --format picture-format.json --width 120 --height 91
mbs excel-worksheet media check --doc-id <DOC_ID> --worksheet-name Dashboard
mbs style beautify --doc-id <DOC_ID> --worksheet-name Sheet1 --dry-run --output json
mbs style beautify --doc-id <DOC_ID> --worksheet-name Sheet1 --output json
mbs pivot preview --doc-id <DOC_ID> --worksheet-name SourceData --spec artifacts/pivot-config.json
mbs pivot upsert --doc-id <DOC_ID> --target-worksheet-name PivotResult --anchor-cell A1 --spec pivot-config.json
mbs excel-worksheet dashboard validate --spec dashboard.json
mbs excel-worksheet dashboard refresh --doc-id <DOC_ID> --spec dashboard.json
mbs excel-worksheet dashboard manifest --doc-id <DOC_ID> --worksheet-name Dashboard
mbs excel-worksheet dashboard export-template --doc-id <DOC_ID> --worksheet-name Dashboard --template-id <template-id> --out-dir <analysis-style-system-skill-dir>/dashboard-templates/<template-id>
```

- `--output table` for human inspection; `json` (default) for automation
- Use `--base-url http://localhost:7011` or `MAYBEAI_BASE_URL=http://localhost:7011` for the local `play-be` router; `localhost:3003` is the chat frontend, not the spreadsheet API backend
- Targeting flags (`--doc-id`, `--gid`, `--worksheet-name`, `--output`) work at root, group, or command level
- Always pass a leaf subcommand (`read`, `metadata`, `insert`, etc.)

Command catalog: [references/cli-commands.md](references/cli-commands.md)

## Execution order

1. Run `mbs --version` and `mbs --help` once at the start of a session; trust the local CLI over remembered examples.
2. `mbs <group> <command> --help` when flags are unclear.
3. [references/cli-commands.md](references/cli-commands.md) for command lookup.
4. Topic reference below for semantics, edge cases, and uncovered CLI gaps.

## Critical rules

**Worksheet targeting and identity.** Non-first worksheets MUST be named explicitly. Prefer `--worksheet-name` for current object commands; use `--gid` mainly for legacy `sheet` aliases. Without either, calls often hit the first worksheet. When the user asks to overwrite generated data in the existing sheet or says not to create another sheet, record the target `gid` before writing and require that same `gid` afterward. Do not delete, rename-swap, recreate, copy, or import a replacement worksheet: same name alone is not success. Details: [references/read-write.md](references/read-write.md)

**Metadata-first.** Before reads or writes on an unfamiliar workbook: `workbook metadata` or `workbook list-worksheets`, then select the model and its identity. Sheet needs a worksheet locator; Base needs `table_id`, `field_id`, and `record_id`; SQL Config needs its result worksheet and raw SQL.

**Worksheet table detection.** Use `excel-worksheet list-table --gid <GID>` when a visual Excel worksheet can contain multiple separated tables. The routed local path is `play-be` on port `7011`, and Sheet-backed worksheets should return content-backed table ranges such as `A4:I16` and `A20:I27` instead of one whole-sheet range.

**Persistent Excel tables.** Use `excel-table headers` for a header-only read.
Use `excel-table metadata` to obtain the persistent `table_id` and current
range. Use that ID, not a scan-order number or a saved A1 range, with
`excel-table schema`, `sample`, `read`, and `insert`. `--range` is not
supported by `excel-table`. After inserting or deleting worksheet rows,
resolve metadata again before another insert because the table's ending row may
have shifted.

**Persistent Excel table inserts.** `excel-table insert` accepts a non-empty
JSON array of objects. Every object must have exactly the current table header
names. The CLI orders values by that header row and appends all objects to the
next contiguous table range. Ten objects append ten rows in one call. The
command has no `--verify`; verify with
`excel-table read` or an exact
`excel-worksheet range read` after the write.

**Import engine choice.** Use `mbs workbook import` only to create a new workbook. To import into an existing workbook, use `mbs worksheet import --strategy create`; omit `--source-worksheet-name` to import all source worksheets/tabs, repeat it to select multiple sources, and use `--target-worksheet-name` only for one selected source. Use `--engine base` only for known flat tables and `--engine sheet` for reports, formulas, merged cells, styles, or multiple separated tables. For Maybe Sheet-to-Maybe Sheet imports, use `--transfer-mode values` for Base raw surfaces and `--transfer-mode native` to preserve registered engines and supported fidelity. Native transfer rejects `--engine`, and its `result.operations[]` reports the final engine, full row count, and verification result. Details: [references/file-management.md](references/file-management.md)

**Worksheet engine migration.** To migrate an existing Sheet-backed worksheet to Base, inspect `workbook list-worksheets` first and target exactly one worksheet with `--gid` or `--worksheet-name` (a URL containing `gid` may supply it). Run `mbs worksheet convert-to-base ... --dry-run`, then rerun with `--yes --verify`. This is one-way: no Base-to-Sheet CLI/backend conversion exists. It removes the old Sheet-engine cell content by default while retaining styles; pass `--keep-sheet-source` only when that source content must remain. `--dry-run` and `--verify` cannot be combined. Details: [references/read-write.md](references/read-write.md)

**Dashboard imports.** For chart-heavy dashboards, decide the engine per worksheet before upload. Data source worksheets that will be queried by chart SQL should be Base-compatible flat tables and usually use `base`; cover, summary, and dashboard canvas worksheets should usually use `sheet`. Use an explicit worksheet-index engine list only when the source worksheet order is already known.

**Object model.** Use `excel-worksheet read` and `excel-worksheet range` only for Sheet targets. Use `excel-table` for Sheet-backed tables. Use `base-table` for Base discovery, creation, records, fields, and Formula operations. `db-table` is compatibility-only and must not appear in new examples. Cell `formula` commands and worksheet calculation are Sheet-only. SQL Config is a distinct raw-SQL producer. Details: [references/base-mode-verification.md](references/base-mode-verification.md)

**Formula calculate persistence.** `mbs formula calculate` and `mbs excel-worksheet range calculate` call `/api/v1/excel/calc-formula`. Pass `--save-result` when the calculated formula/result should be written to the workbook, pass `--no-save-result` for preview-only probes, and omit the flag only when you intentionally want the backend default.

**Write priority.** For a Sheet target, use `sheet update-data-keep-headers` only for a full data-row refresh that must preserve Sheet headers, styles, and formula columns; use `excel-worksheet range write` for exact cells. For a Base target, use `base-table record create`, `base-table record replace`, or `base-table record upsert` with resolved `table_id`, `field_id`, and record identity. `base-table create-from-range`, `base-table create-from-query`, and `base-table create` create Base tables; they are not record-replace/upsert APIs. SQL Config owns raw query materialization.

**Full worksheet data refresh (Sheet only).** Prefer the unified entry point: `mbs worksheet import ./rows.json --strategy replace --doc-id <DOC_ID> --worksheet-name <SHEET> --verify`, only after metadata confirms `engine=sheet`. It uses the keep-headers contract. The JSON file must be a non-empty array of objects whose keys match existing headers; it keeps row 1 and column order, rejects unknown keys, preserves formula columns and recalculates by default, and rejects `--dry-run --verify`. Use `--dry-run` first for unfamiliar data. When the task requires the original worksheet, record its `gid` before the refresh and confirm it remains unchanged afterward. A `written_unverified` response with `error: null` means the write may have succeeded but CLI verification did not prove it; it is neither a failed refresh nor a reason to ask the user to choose another implementation. Read back the full refreshed footprint or known changed sentinel cells, compare them with the source JSON by header using appropriate numeric/date tolerance, then either accept the verified write or automatically recover through range operations on that same worksheet. This workflow is invalid for Base: use field-mapped record replacement instead. Details: [references/read-write.md](references/read-write.md) and [references/errors-recovery.md](references/errors-recovery.md)

**Range value mode.** `excel-worksheet range write` uses backend RAW value handling: numeric-looking strings such as `"5.53%"` and `"9,007,000"` remain strings. Treat USER_ENTERED parsing as unavailable unless a specific command exposes it.

**Verify after every write.** Use `--verify` where available. Verify against the target model: read an A1 range and run `excel-worksheet check-error` for Sheet; inspect record and Formula execution evidence for Base; verify stored raw SQL plus the materialized result for SQL Config. `base-table sample` alone is not Formula execution evidence. For a full refresh reporting `written_unverified` with `error: null`, readback comparison is mandatory before any failure claim. When the user required the original worksheet, run `workbook list-worksheets` after the write and confirm its recorded `gid` is unchanged. See [references/base-mode-verification.md](references/base-mode-verification.md).

**Base table metadata and headers.** `base-table metadata` is a single-table lookup; pass `--name` or `--backend-id`. Add `--include-headers` when the agent needs header text in the final JSON. Current CLI versions resolve the table through `/api/v1/excel/worksheet/metadata`, merge targeted `/api/v1/excel/worksheet/dimensions`, and return `headers`, `header_names`, and header metadata when available. `workbook metadata` uses `/api/v1/excel_v2/worksheet/metadata` and returns routing metadata, not exact table headers.

**Base table field style.** For a Base-backed column formatter, color, background, or width, use `mbs base-table field metadata` before `mbs base-table field update`. It accepts native IDs or resolves `--name --field` for compatibility. Use `--verify` and inspect the returned field property; do not document the legacy `db-table field batch-update` command in new workflows.

**Base table lifecycle.** `base-table create-from-range` is API-backed and CLI-composed for raw-surface import. `base-table create-from-query` executes raw SQL, infers sources from its `FROM`/`JOIN` relations, and creates the `--name` output Base table. It has no `--worksheet-name` flag; `--gid` is optional compatibility context and does not select the SQL source. Use `--if-exists adopt` only with `--verify`. For supported cross-document worksheet copies, use `mbs worksheet import --strategy create --transfer-mode native`; do not use the legacy workbook-import native entry point.

**Styles.** Use `mbs style beautify` for agent-friendly report/table polish. It reads metadata first, classifies columns from Chinese/English headers plus sample values, applies Excel worksheet styles, and writes Base-backed field style metadata through the native field-update route when possible. Use first-class `excel-worksheet style` commands for explicit freeze panes, filters, widths, heights, cell style batches, gridlines, filter values, conditional formats, and worksheet style planning/apply. See [references/charts-formatting.md](references/charts-formatting.md).

**Images.** Worksheet images are floating objects like charts, not cell values. Before `image insert`, confirm the target worksheet is Sheet-backed with `workbook list-worksheets`; Base-only worksheets do not support `add_picture`. Use `image insert` / `image set` with chart-compatible picture `format` JSON for position and size (`from`, `to`, and pixel offsets), then verify with `image list` and `media check`. Do not treat the returned `cell` as enough to preserve layout after drag/resize. To create a new image canvas in an existing Base Mode workbook, import a small blank `.xlsx` with `--engine sheet` instead of `excel-worksheet create`.

**SQL.** For live worksheet SQL, use `mbs sql config set --sql-file ...`, `mbs sql preview`, and `mbs sql overwrite --confirm-overwrite`; use `mbs sql query --limit ...` for a bounded read-only raw query. These commands use Worksheet SQL Config and materialize current results when requested. For reusable Base-backed handoff tables, `mbs base-table create-from-query --name <OUTPUT_TABLE> --sql-file ... --verify` is a creation flow, not a Base Formula operation. In raw SQL over a Base source, use quoted field display names; `field_id` values such as `col_000001` are not query columns, and `SELECT *` returns each display column once. Legacy SQL cell wrappers are migration-only compatibility; scan first with `mbs sql migration preview`, then commit only explicitly approved candidates. See [references/formulas-sql.md](references/formulas-sql.md).

**Pivot tables.** Use first-class `mbs pivot read`, `mbs pivot preview`, `mbs pivot upsert`, and `mbs pivot delete`. Do not call `/api/v1/excel/pivot_table/*`, `/api/v1/excel/read_pivot_table`, legacy `/api/pivot_table/*`, or hand-build `MAYBE_PIVOT` formulas through `raw post` / `formula set` unless the local `mbs pivot --help` proves the command is unavailable. `pivot upsert` requires an explicit target anchor cell; if the user says `A1`, keep `--anchor-cell A1`. Details and spec examples: [references/pivot-tables.md](references/pivot-tables.md).

```bash
mbs excel-worksheet dashboard validate --spec dashboard.json
mbs excel-worksheet dashboard refresh --doc-id <DOC_ID> --spec dashboard.json
mbs excel-worksheet dashboard manifest --doc-id <DOC_ID> --worksheet-name Dashboard
mbs excel-worksheet chart list --doc-id <DOC_ID> --worksheet-name Dashboard
mbs excel-worksheet dashboard export-template --doc-id <DOC_ID> --worksheet-name Dashboard --template-id <template-id> --out-dir <analysis-style-system-skill-dir>/dashboard-templates/<template-id> --force
```

Use `dashboard create-config` when the worksheet should be created from the spec in one run.

For dashboard specs with `chart.type: "html"`, the chart object must include non-empty `chart.html`, `chart.sql`, `chart.format.from/to`, and `chart.dimension`. Named sources must be direct SQL strings such as `"data_sources": {"mgmt_summary": "SELECT * FROM \"gid_2\""}`; never emit `"mgmt_summary": {"sql": "..."}`. For large renderer dependencies, reference approved CDN packages with `<script src>` such as jsdelivr/unpkg/cdnjs/d3js; do not inline full ECharts/D3 bundles into `chart.html`.

For dashboard render proof, prefer:

```bash
mbs excel-worksheet dashboard render-probe \
  --doc-id <DOC_ID> \
  --worksheet-name <DASHBOARD_WORKSHEET> \
  --chart-id <HTML_CHART_ID> \
  --text-marker <TITLE_OR_KPI> \
  --data-marker <DATA_VALUE> \
  --screenshot dashboard.png \
  --output json
```

Interpret render proof in tiers. `local_probe_passed` means the local HTML runtime, runtime payload adapter, DOM, and data binding worked. `screenshot_verified` means PNG screenshot capture also worked. If `visual_verification.status` is `environment_blocked` with `playwright_unavailable` or `chromium_unavailable`, install Playwright/Chromium in the running environment (`npm i -D playwright`, `npx playwright install chromium`) and retry; do not treat that as a dashboard spec failure.


```bash
mbs excel-worksheet dashboard validate --spec dashboard.json
mbs excel-worksheet dashboard refresh --doc-id <DOC_ID> --spec dashboard.json --dry-run
mbs excel-worksheet dashboard refresh --doc-id <DOC_ID> --spec dashboard.json
mbs excel-worksheet dashboard manifest --doc-id <DOC_ID> --worksheet-name Dashboard
mbs excel-worksheet chart list --doc-id <DOC_ID> --worksheet-name Dashboard
mbs excel-worksheet dashboard export-template --doc-id <DOC_ID> --worksheet-name Dashboard --template-id <template-id> --out-dir <analysis-style-system-skill-dir>/dashboard-templates/<template-id> --force
```

Use `dashboard create-config` when the worksheet should be created from the spec in one run.


## Task routing

| Task | Start here |
|------|------------|
| Command flags and examples | [references/cli-commands.md](references/cli-commands.md) |
| Read/write targeting and API choice | [references/read-write.md](references/read-write.md) |
| Base record/field/formula verification | [references/base-mode-verification.md](references/base-mode-verification.md) |
| Upload, export, sharing | [references/file-management.md](references/file-management.md) |
| Workbook semantic overview | [references/workbook-profile.md](references/workbook-profile.md) |
| Sharing and permissions | [references/permission-sharing.md](references/permission-sharing.md) |
| Formulas and SQL result sheets | [references/formulas-sql.md](references/formulas-sql.md) |
| Pivot tables and pivot config specs | [references/pivot-tables.md](references/pivot-tables.md) |
| Formula dependency tracing | [references/lineage-trace.md](references/lineage-trace.md) |
| Charts, images, dashboards, worksheet styling | [references/charts-formatting.md](references/charts-formatting.md) |
| Sharing and permissions | [references/permission-sharing.md](references/permission-sharing.md) |
| Failures and recovery | [references/errors-recovery.md](references/errors-recovery.md) |
| Clickable cell refs in answers | [references/clickable-refs.md](references/clickable-refs.md) |
| Legacy SQL formula migration/showcase | [references/sql-formula-showcase.md](references/sql-formula-showcase.md) |

## Workflows

### Inspect a workbook

```
- [ ] workbook metadata or workbook list-worksheets
- [ ] identify worksheet name, table id, or Base table name
- [ ] read sample with --output table
```

```bash
mbs workbook metadata --doc-id <DOC_ID>
mbs workbook list-worksheets --doc-id <DOC_ID> --output table
mbs excel-worksheet read --doc-id <DOC_ID> --worksheet-name <SHEET> --output table
mbs excel-worksheet read --doc-id <DOC_ID> --worksheet-name <SHEET> --range A1:D20 --output table
```

### Upload and inspect

```
- [ ] workbook import
- [ ] capture document_id from JSON output
- [ ] use import stdout plus `--verify` as creation evidence
- [ ] if needed, resolve and sample one representative Base table per family
```

```bash
# Small workbook-style files
mbs workbook import ./file.xlsx --verify
mbs workbook import ./orders.csv --engine base
mbs workbook import "https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0" --engine sheet
mbs workbook metadata --doc-id <DOC_ID>
mbs workbook list-worksheets --doc-id <DOC_ID> --output table

# Large table-like files
mbs workbook import ./file.xlsx --engine base --verify
mbs base-table metadata --doc-id <DOC_ID> --name <REPRESENTATIVE_TABLE_NAME> --output json
mbs base-table sample --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 2 --output table

# Cross-workbook worksheet -> raw Base-backed surface import
mbs worksheet import --strategy create --doc-id <TARGET_DOC_ID> --source-doc-id <SOURCE_DOC_ID> --source-worksheet-name "1店" --verify
mbs worksheet import --strategy create --doc-id <TARGET_DOC_ID> --source-doc-id <SOURCE_DOC_ID> --source-worksheet-name "1店" --source-worksheet-name "2店" --verify

# Sheet only: replace existing worksheet rows from JSON while keeping headers.
# For Base records, use `mbs base-table record replace` or `record upsert`.
mbs worksheet import ./rows.json --strategy replace --doc-id <TARGET_DOC_ID> --worksheet-name Students --verify

# Native Maybe Sheet worksheet import; engine is detected per worksheet
mbs worksheet import --strategy create --transfer-mode native --doc-id <TARGET_DOC_ID> --source-doc-id <SOURCE_DOC_ID> --source-worksheet-name "工作表3" --source-worksheet-name "工作簿1" --verify
mbs worksheet import --strategy create --transfer-mode native --doc-id <TARGET_DOC_ID> --source-doc-id <SOURCE_DOC_ID> --verify

# Append source worksheets/tabs into an existing workbook
mbs worksheet import ./file.xlsx --strategy create --doc-id <TARGET_DOC_ID> --engine sheet --verify
mbs worksheet import ./file.xlsx --strategy create --doc-id <TARGET_DOC_ID> --source-worksheet-name "联盟" --target-worksheet-name "联盟导入" --engine sheet --verify
mbs worksheet import ./file.xlsx --strategy create --doc-id <TARGET_DOC_ID> --source-worksheet-name "联盟" --source-worksheet-name "订单" --engine base --verify
mbs worksheet import ./orders.csv --strategy create --doc-id <TARGET_DOC_ID> --engine base --verify
mbs worksheet import "https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit#gid=0" --strategy create --doc-id <TARGET_DOC_ID> --source-worksheet-name "1店" --target-worksheet-name "Store 1" --engine sheet --verify
```

Do not follow successful raw-surface imports with per-table `schema` / `sample` / `read` loops. See [references/file-management.md](references/file-management.md) for engine choice and Base Mode verification.

### Convert a worksheet to Base

```
- [ ] inspect `workbook list-worksheets` and select exactly one Sheet-backed worksheet
- [ ] run `convert-to-base --dry-run` with `--gid` or `--worksheet-name`
- [ ] execute the reviewed conversion with `--yes --verify`
- [ ] retain old Sheet-engine source cells only when explicitly requested
```

```bash
# The workbook URL can provide both document ID and gid.
mbs worksheet convert-to-base \
  --url "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?gid=<GID>" \
  --dry-run

# Execute after reviewing the dry run. Source cells are scrubbed by default.
mbs worksheet convert-to-base \
  --doc-id <DOC_ID> \
  --worksheet-name Orders \
  --yes \
  --verify

# Keep the prior Sheet-engine cell content only when required.
mbs worksheet convert-to-base \
  --doc-id <DOC_ID> \
  --gid <GID> \
  --keep-sheet-source \
  --yes \
  --verify
```

Use `--recalculate` when the converted Base worksheet should recalculate
immediately. Do not combine `--dry-run` with `--verify`. The command checks
metadata during `--verify` and succeeds only when the selected worksheet
reports `data_engine: base`.

### Dashboard execution

```
- [ ] `mbs --version` and relevant `--help`
- [ ] import with `--engine auto` or an explicit worksheet-index engine list
- [ ] `workbook list-worksheets` verifies Data_* Base Mode and Dashboard/summary Sheet mode where intended
- [ ] `dashboard validate --spec dashboard.json`
- [ ] `dashboard refresh --dry-run` checks payload shape before mutation
- [ ] execute `dashboard refresh`; if batch errors persist, use per-chart `chart create-config`
- [ ] `dashboard manifest` and `chart list` verify persisted metadata
- [ ] read source Data_* sheets and run browser/vision verification when logged-in canvas access exists
```

See [references/charts-formatting.md](references/charts-formatting.md) for chart spec shapes, fallback, and verification limits.

### Dashboard template export

Use this only when the user wants to promote an existing Maybe Sheet HTML dashboard worksheet into a reusable template package. The dashboard canvas must be a `sheet` worksheet, and the worksheet should contain exactly one persisted `chart.type=html` dashboard chart unless `--chart-id` or `--cell` is provided.

```bash
mbs excel-worksheet dashboard export-template \
  --doc-id <DOC_ID> \
  --worksheet-name <DASHBOARD_WORKSHEET> \
  --template-id <template-id> \
  --out-dir <analysis-style-system-skill-dir>/dashboard-templates/<template-id> \
  --force
```

The command writes `template.json`, `html/dashboard.template.html`, and `html/runtime-payload.schema.json`. After export, switch to `analysis-style-system` and run `node scripts/validate_dashboard_html_template.mjs --template-dir dashboard-templates/<template-id>` before using or publishing the template skill.

### Sync rows by key

Choose the model first. The following checklist and command are Sheet-only.
For Base, resolve `table_id`, writable `field_id`s, and the record key, then
use `mbs base-table record upsert`; do not use the Sheet compatibility
alias.

```
- [ ] confirm metadata reports `engine=sheet`
- [ ] confirm key column name
- [ ] use legacy sheet upsert when key-based merge is required
- [ ] recalculate Sheet formulas if downstream formulas exist
- [ ] read back the Sheet target range
```

```bash
mbs sheet upsert --doc-id <DOC_ID> --gid <GID> --key order_id --rows rows.json --verify
mbs excel-worksheet calculate --doc-id <DOC_ID> --worksheet-name <SHEET>
```

### SQL result sheet

```
- [ ] headers + read sample on source sheet
- [ ] save raw SQL with `mbs sql config set`
- [ ] materialize with `mbs sql overwrite --confirm-overwrite`
- [ ] read result sheet
- [ ] scan the worksheet with `excel-worksheet check-error`
```

See [references/formulas-sql.md](references/formulas-sql.md).

### Pivot table

```
- [ ] inspect source worksheet headers
- [ ] author `pivot-config.json`
- [ ] preview pivot output
- [ ] upsert with explicit target worksheet and anchor cell
- [ ] read target range to verify
```

```bash
mbs pivot preview --doc-id <DOC_ID> --worksheet-name <SOURCE_SHEET> --spec pivot-config.json --output table
mbs pivot upsert --doc-id <DOC_ID> --target-worksheet-name PivotResult --anchor-cell A1 --spec pivot-config.json
mbs excel-worksheet read --doc-id <DOC_ID> --worksheet-name PivotResult --range A1:H30 --output table
```

See [references/pivot-tables.md](references/pivot-tables.md).

### Trace formula lineage

```bash
mbs formula lineage --doc-id <DOC_ID> --worksheet-name <SHEET> --cell E2 --format tree --output yaml
```

See [references/lineage-trace.md](references/lineage-trace.md) for response interpretation.

### Share or check access

```bash
mbs share permission --doc-id <DOC_ID>
mbs share visibility --doc-id <DOC_ID> --visibility public --public-permission viewer
# Share read-only access with a MaybeAI user email
mbs share grant --doc-id <DOC_ID> --email user@example.com --permission viewer
# Share write/edit access with a MaybeAI user email
mbs share grant --doc-id <DOC_ID> --email user@example.com --permission editor
mbs share list --doc-id <DOC_ID>
```

If `mbs share visibility` returns 403 with an owner-only message, classify it as `owner_permission_required` / `permission_skipped`. If workbook metadata already shows the requested public/editor or public/viewer visibility, report it as a share warning rather than a dashboard failure; otherwise ask the owner or service account to update visibility. See [references/permission-sharing.md](references/permission-sharing.md) for owner requirements and access rules.

## Boundaries

- **Dashboard/chart layout** -> use `sheet-dashboard`, not this skill
- **Uncovered CLI gaps** -> check current `mbs --help` for a supported command
- **Clickable refs** -> only confirmed locations; see [references/clickable-refs.md](references/clickable-refs.md)
