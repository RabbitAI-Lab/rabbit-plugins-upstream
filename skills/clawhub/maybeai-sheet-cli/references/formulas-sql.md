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

- Use `mbs excel-worksheet range set-formula` when you need to persist one worksheet formula or a batch of worksheet formulas.
- Use `mbs formula batch-set` when you need the workbook-level batch alias for many formulas across worksheets.
- Treat `mbs formula set` as a compatibility alias for single worksheet formula writes; prefer the `excel-worksheet range` form in new examples.
- Use `mbs excel-worksheet range calculate --no-save-result` for temporary preview or debugging.
- Use `mbs formula calculate --save-result` or `mbs excel-worksheet range calculate --save-result` only when a one-cell calculation should also persist the formula/result.
- Use `mbs excel-worksheet calculate` for one-sheet refresh after data changes.
- Use `mbs workbook calculate` when downstream formulas span worksheets.
- Use `mbs excel-worksheet check-error` after writes or recalculation when the result worksheet must be free of worksheet errors.
- For batch report builds, prefer rectangular `operations[]` and one final `recalculate_mode`.
- Batch formula setting is for ordinary workbook formulas; do not use it for SQL Config or pivot formulas. For persisted pivots, use `mbs pivot preview` / `mbs pivot upsert`.
- `mbs excel-worksheet range set-formula` is a saved workbook write. If the command succeeds, the target cell contains the formula; there is no separate save command.
- If you explicitly pass `--skip-recalculation`, the formula is still saved, but the displayed value or SQL spill output may not refresh until you call `mbs excel-worksheet calculate` or `mbs workbook calculate`.

CLI:

```bash
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --worksheet-name <SHEET> --cell E2 --formula '=SUM(B2:D2)'
mbs excel-worksheet range set-formula --doc-id <DOC_ID> --operations ops.json --recalculate-mode worksheet
mbs formula batch-set --doc-id <DOC_ID> --operations ops.json --recalculate-mode worksheet
mbs excel-worksheet calculate --doc-id <DOC_ID> --worksheet-name <SHEET>
mbs workbook calculate --doc-id <DOC_ID>
mbs formula read --doc-id <DOC_ID> --worksheet-name <SHEET> --range A1:E20
mbs excel-worksheet range calculate --doc-id <DOC_ID> --worksheet-name <SHEET> --cell E2 --formula '=SUM(B2:D2)' --no-save-result
mbs formula calculate --doc-id <DOC_ID> --worksheet-name <SHEET> --cell E2 --formula '=SUM(B2:D2)' --save-result
mbs excel-worksheet check-error --doc-id <DOC_ID> --worksheet-name <SHEET>
```

Use `mbs formula lineage` only for A1-style worksheet formula lineage. It does
not make a Base Table cell-addressable.

## 3. Base column Formula

A Base Formula belongs to a field and evaluates across the table's records. Its
inputs and outputs are identified by `table_id`, `field_id`, and records, not
by `E2`, a range, or a copied row template.

Use the separate P5 command surface:

```bash
mbs base-table formula compile --doc-id <DOC_ID> --table-id <TABLE_ID> --field-id <FIELD_ID> --expression '<EXPRESSION>'
mbs base-table formula set --doc-id <DOC_ID> --table-id <TABLE_ID> --field-id <FIELD_ID> --expression '<EXPRESSION>'
mbs base-table formula recalculate --doc-id <DOC_ID> --worksheet-name <BASE_WORKSHEET> --table-id <TABLE_ID>
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
Base `field_id` used by `mbs base-table` record and Formula commands. Quote the
display names when needed:

```sql
select "mainImage", "categoryId", "skc"
from "Base"
```

`col_000001`-style field IDs are not SQL columns. `SELECT * FROM "Base"`
returns each display column once, so it is valid when all source columns are
needed. For a reusable materialized result, `mbs base-table create-from-query`
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
