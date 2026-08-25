# Workbook Metadata Reference

## When to use it

Run `mbs workbook metadata` before acting on an unfamiliar workbook. It is the
read-only routing step that identifies worksheet names, gids, engines, and Base
table IDs. It does not read samples, generate an LLM summary, or replace an
exact worksheet/table read.

```bash
mbs workbook metadata --doc-id <DOC_ID> --output json
mbs workbook metadata --url "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?gid=2" --output json
```

The CLI accepts `--doc-id`, `--url`, or `--uri`. It resolves those to a
MaybeAI workbook URI and calls:

```text
POST /api/v1/excel_v2/worksheet/metadata
{"uri": "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>"}
```

## Response contract

The CLI wraps the backend response in its normal command envelope:

```json
{
  "success": true,
  "endpoint": "/api/v1/excel_v2/worksheet/metadata",
  "result": {
    "document_id": "<DOC_ID>",
    "engine": "composite",
    "worksheet_count": 2,
    "worksheets": [
      {
        "worksheet_name": "Orders",
        "gid": 5,
        "data_engine": "base",
        "table_id": "tbl_orders"
      },
      {
        "worksheet_name": "Dashboard",
        "gid": 6,
        "data_engine": "sheet"
      }
    ]
  },
  "target": {
    "document_id": "<DOC_ID>",
    "uri": "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>"
  }
}
```

Use these fields as routing identities:

| Metadata | Meaning | Next command family |
|---|---|---|
| `data_engine: sheet` | Excel-style worksheet | `worksheet`, `table`, A1/range operations |
| `data_engine: base` plus `table_id` | Base-backed table | canonical `table`, `row`, `column`, `formula` operations (`table` is compatibility) |
| `gid` | worksheet locator | Use with worksheet/table lookup when a command needs it |

Do not treat `worksheet_name` as a Base record identity, and do not infer row
counts or exact headers from this route. Use a bounded Sheet read or
`table inspect`/`schema` after resolving the target.

## Recommended workflows

### Inspect an unfamiliar workbook

1. Run `mbs workbook metadata --doc-id <DOC_ID> --output json`.
2. Choose the target by `worksheet_name` and `data_engine`.
3. For Sheet, read a bounded range:

   ```bash
   mbs range read --doc-id <DOC_ID> --worksheet-name Orders --range A1:H20 --output table
   ```

4. For Base, retain `table_id`, then inspect native schema/sample:

   ```bash
   mbs table schema --doc-id <DOC_ID> --table-id <TABLE_ID> --output json
   mbs table sample --doc-id <DOC_ID> --table-id <TABLE_ID> --limit 20 --output table
   ```

### Verify a native worksheet import

Run `worksheet import --transfer-mode native --verify`. Its
`result.operations[]` contains `final_target_name`, `final_engine`, `rows`, and
`verify.status`. Follow with `workbook metadata` only to confirm the target
name/gid/engine. For a large Base source, the import operation's `rows` is the
copy-completeness evidence; do not substitute a default bounded read.

## Compatibility and recovery

- `workbook manifest` and `workbook capabilities` are compatibility commands
  that may still use `/api/v1/excel/workbook_profile`.
- `workbook metadata` must use `/api/v1/excel_v2/worksheet/metadata`. If output
  shows a 500 from `workbook_profile`, the installed CLI is stale; update or
  reinstall the local package and rerun the unchanged `mbs workbook metadata`
  command.
- `403`: confirm `MAYBEAI_API_TOKEN` and document access.
- Missing target worksheet: refresh metadata, then use the exact returned
  worksheet name or gid.
- Missing Base `table_id`: stop before a Base mutation and resolve the table by
  `mbs table inspect --name <TABLE_NAME>`.
