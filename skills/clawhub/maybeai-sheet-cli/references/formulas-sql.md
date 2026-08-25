# Formulas and Worksheet SQL Reference

## 1. Pick one computation model

There are three different producers. Resolve the engine before creating one.

| Model | Formula/query identity | Author with |
|---|---|---|
| Excel Sheet | A1 cell and `worksheet_name` | ordinary cell/range formula |
| Base Table | `table_id` and target `field_id` | column Formula |
| Worksheet SQL Config | SQL result worksheet and config | raw SQL |

Do not translate a cell address into a Base Formula, and do not turn raw SQL
into a cell-formula wrapper. See [base-mode-verification.md](base-mode-verification.md)
for the Base evidence contract.

## 2. Excel Sheet formulas

These commands are only for a target confirmed as `engine=sheet`.

Guidance:

- Use `mbs range set-formula` when you need to persist one worksheet formula or a batch of worksheet formulas.
- Use `mbs formula batch-set` when you need the workbook-level batch alias for many formulas across worksheets.
- Treat `mbs formula set` as a compatibility alias for single worksheet formula writes; prefer the `range` form in new examples.
- Use `mbs range calculate --no-save-result` for temporary preview or debugging.
- Use `mbs formula calculate --save-result` or `mbs range calculate --save-result` only when a one-cell calculation should also persist the formula/result.
- Use `mbs formula recalculate` for one-sheet refresh after data changes.
- Use `mbs workbook calculate` when downstream formulas span worksheets.
- Use `mbs range inspect` after writes or recalculation when the result worksheet must be free of worksheet errors.
- For batch report builds, prefer rectangular `operations[]` and one final `recalculate_mode`.
- Batch formula setting is for ordinary workbook formulas; do not use it for SQL Config or pivot formulas. For persisted pivots, use `mbs pivot preview` / `mbs pivot upsert`.
- `mbs range set-formula` is a saved workbook write. If the command succeeds, the target cell contains the formula; there is no separate save command.
- If you explicitly pass `--skip-recalculation`, the formula is still saved, but the displayed value or SQL spill output may not refresh until you call `mbs formula recalculate` or `mbs workbook calculate`.

CLI:

```bash
mbs range set-formula --doc-id <DOC_ID> --worksheet-name <SHEET> --cell E2 --formula '=SUM(B2:D2)'
mbs range set-formula --doc-id <DOC_ID> --operations ops.json --recalculate-mode worksheet
mbs formula batch-set --doc-id <DOC_ID> --operations ops.json --recalculate-mode worksheet
mbs formula recalculate --doc-id <DOC_ID> --worksheet-name <SHEET>
mbs workbook calculate --doc-id <DOC_ID>
mbs formula read --doc-id <DOC_ID> --worksheet-name <SHEET> --range A1:E20
mbs range calculate --doc-id <DOC_ID> --worksheet-name <SHEET> --cell E2 --formula '=SUM(B2:D2)' --no-save-result
mbs formula calculate --doc-id <DOC_ID> --worksheet-name <SHEET> --cell E2 --formula '=SUM(B2:D2)' --save-result
mbs range inspect --doc-id <DOC_ID> --worksheet-name <SHEET>
```

Use `mbs range lineage --range <A1_CELL_OR_RANGE>` for A1-style worksheet
formula lineage; do not use its removed `--cell` option. It does not make a
Base Table cell-addressable.

## 3. Base column Formula

A Base Formula belongs to a field and evaluates across the table's records. Its
inputs and outputs are identified by `table_id`, `field_id`, and records, not
by `E2`, a range, or a copied row template.

Use the canonical `formula` command surface:

```bash
mbs formula compile --target "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?tid=<TABLE_ID>" --field-id <FIELD_ID> --expression '<EXPRESSION>'
mbs formula set --target "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?tid=<TABLE_ID>" --field-id <FIELD_ID> --expression '<EXPRESSION>'
mbs formula recalculate --target "https://www.maybe.ai/docs/spreadsheets/d/<DOC_ID>?tid=<TABLE_ID>" --field-id <FIELD_ID>
```

Compile/validate before setting the target `field_id`, then retain the execution
evidence returned by table-level recalculation. `--result-type` and
`--expected-revision` are optional when the workflow needs an expected formula
type or optimistic concurrency. Do not use the legacy range-formula path: it
turns a column intent into a cell operation and cannot represent a Base column
Formula.

## 4. Worksheet SQL Config

SQL Config persists and materializes a raw query. Supply a plain `SELECT` or
`WITH ... SELECT` body using `--sql` or `--sql-file`:

```bash
mbs sql config get --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET>
mbs sql config set --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --sql-file result.sql --auto-refresh
mbs sql preview --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --sql-file result.sql --output table
mbs sql overwrite --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET> --confirm-overwrite
mbs sql config delete --doc-id <DOC_ID> --worksheet-name <SQL_RESULT_SHEET>
```

`sql preview` is read-only. `sql overwrite` materializes the reviewed result;
verify both the saved config and a bounded result read/sample. A raw SQL Config
can materialize a Sheet result or a Base result, but it remains SQL Config and
does not become either a cell formula or a column Formula.

### Typed result schema

Use `--output json` when an automation needs the schema. A current SQL result
contains an ordered `columns` array; every column must have a non-empty `name`
and `pg_type`. `pg_type` is the PostgreSQL type of the final SQL projection and
is the only physical type source for Base field creation and materialization.
Do not replace it with a type inferred from sample values. For example, a
numeric expression must remain numeric even when the preview rows are empty or
contain values that happen to look like text.

```json
{
  "columns": [
    {"name": "amount", "pg_type": "numeric(12,2)"},
    {"name": "created_at", "pg_type": "timestamp with time zone"}
  ]
}
```

The backend may add `ui_type` and `ui_type_source`. Treat those fields as a
verified display-type hint only when `ui_type_source` identifies a source
field, such as a strict `SELECT * FROM <one source>` projection. Do not infer
or preserve a source UI type for joins, expressions, aliases, aggregates,
casts, CTEs, or other computed projections; use their returned `pg_type` and
the normal PostgreSQL-to-Base mapping instead. `ui_type` never overrides a
conflicting `pg_type`.

For `table create-from-query`, pass the complete typed schema to the Base
create request. If any result column is missing `pg_type`, stop before the
mutation and report an invalid typed SQL schema. If a same-name field already
exists in the target Base table with an incompatible physical type, reject the
write and preserve the existing table; do not silently coerce it to text.

Example `result.sql`:

```sql
select "Region", sum("Revenue") as "Revenue"
from "Orders"
group by "Region"
order by "Revenue" desc
```

## 5. SQL constraints

Use a single read-only `SELECT` or `WITH ... SELECT`. Do not use multiple
statements, DDL/DML, `SELECT INTO`, row locks, or internal metadata schemas.
Prefer exact worksheet/table names; quote names containing spaces.

For a Base source, SQL column references use field display names, not the
Base `field_id` used by `mbs table` record and Formula commands. Quote the
display names when needed:

```sql
select "mainImage", "categoryId", "skc"
from "Base"
```

`col_000001`-style field IDs are not SQL columns. `SELECT * FROM "Base"`
returns each display column once, so it is valid when all source columns are
needed. For a reusable materialized result, `mbs table create-from-query`
infers its sources from these `FROM`/`JOIN` relations; `--name` identifies the
new Base table and `--worksheet-name` is not accepted.

## 6. Existing legacy SQL formulas

Some older workbooks contain cell formulas of the legacy SQL-wrapper form.
They are migration-only compatibility objects: do not create, edit, or copy
them. Use:

```bash
mbs sql migration preview --doc-id <DOC_ID>
mbs sql migration commit --doc-id <DOC_ID> --candidate-id <CANDIDATE_ID> --allow-manual-candidates
```

Run preview first; commit only in an approved migration window. New SQL work
uses Worksheet SQL Config raw SQL.
