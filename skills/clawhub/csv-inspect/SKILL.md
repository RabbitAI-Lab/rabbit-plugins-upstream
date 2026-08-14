---
name: csv-inspect
description: >
  Inspect delimited tables (CSV/TSV) before any analysis: column names,
  encodings, delimiters, row counts, inferred types, and first/last rows.
  Use when the user asks to peek a CSV, list headers, show head/tail, preview
  schema, check dtypes, or before pandas work on .csv/.tsv/.tab files.
  Use when the user runs /csv-inspect. Do not use for Excel workbooks (.xlsx)
  or for writing statistical reports — inspect only, then stop or hand off.
compatibility: Requires Python 3.9+ stdlib (csv, argparse). No pandas.
metadata:
  author: pinchbench-designed
  version: "1.1.0"
  standard: agentskills.io
  pinchbench-categories: csv_analysis
  openclaw:
    emoji: "📋"
    requires:
      bins:
        - python3
    os:
      - linux
      - darwin
      - win32
---

# CSV Inspect

Read **schema and samples**, not the whole file. Do not start analysis until
this output exists.

## When to use

- User wants headers, preview rows, shape, encoding, or delimiter
- Any later step will parse a `.csv` / `.tsv` / `.tab` / `.txt` table

Stop after inspect if that was the whole request. For rankings, z-scores, or a
written report, inspect first, then use a separate analysis path.

## Command

Resolve the executable next to this `SKILL.md` and run it in the **shell**.
Do not prefix with `python3`. Do not reimplement this inspect in Python.

```bash
scripts/csv-inspect PATH
scripts/csv-inspect PATH --head 10 --tail 3
scripts/csv-inspect PATH --json
```

Do not `cat` / `read` the raw file to "see columns". Do not load the table into
pandas just to print `columns` or `head`.

## What you must take from the output

- **`names`**: use these strings **exactly** (case, spaces, punctuation)
- **`encoding` / `delimiter`**: pass the same when you later `open` / `read_csv`
- **`types`**: inferred from `--scan` rows (default 200). `date` includes
  `YYYY-MM` period strings — do not treat them as Excel serials; split or
  `to_datetime` explicitly. `sample` values may come from later rows too.
- **`rows`**: data rows only (header excluded unless `--no-header`)

## Hard rules

1. Inspect **before** any groupby / z-score / report write.
2. Failures must show a **traceback**. Do not wrap the first parse in
   `except Exception as e: print(e)`.
3. Never dump a large table into the transcript. `--head` defaults to 5;
   raise it only if the user asked for more.
4. If `columns` is 1 and values contain `;` or `\t`, re-run with the printed
   `delimiter` or inspect a larger sample — the sniffer can be wrong on tiny files.
5. After a successful inspect, do **not** re-inspect in a loop. Proceed or stop.

## Done criteria

- [ ] `scripts/csv-inspect` was run on the target file via the shell
- [ ] Column names in later code match `names` exactly
- [ ] Raw file was not bulk-read into context
- [ ] If the user only asked for preview/schema, you stopped after the inspect output
