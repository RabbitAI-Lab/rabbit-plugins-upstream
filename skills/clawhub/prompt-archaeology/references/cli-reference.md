# `excavate.py` CLI Reference

`excavate.py` is a stdlib-only Python script for excavating session logs and markdown files. It supports three subcommands: `dig`, `index`, and `query`.

## Global behavior

- **No third-party dependencies.** Runs on Python 3.8+ with the standard library only.
- **Reads** `.md`, `.txt`, `.json`, and `.jsonl` files (see [File formats](#file-formats)).
- **Writes** nothing unless `--out` is given (index subcommand).
- **Exits non-zero** on argument errors; zero on successful search (even with no hits).

## Subcommands

### `dig` — search a directory directly

```bash
python3 scripts/excavate.py dig <directory> --query <terms> [options]
```

Scans `<directory>` recursively, scores every file against the query, prints the top matches. Use `dig` for one-off searches; use `index` + `query` for repeated searches over the same corpus.

**Options:**

| Flag | Type | Default | Description |
|---|---|---|---|
| `--query`, `-q` | str (required) | — | Search terms. Multiple terms are AND'd within a file (all must appear). Use `--query "a b c"` or repeat `--query` for OR semantics is not supported; pass a single string. |
| `--top`, `-n` | int | 5 | Number of top results to print. |
| `--after` | date (ISO) | — | Only include files modified on/after this date (`YYYY-MM-DD`). |
| `--before` | date (ISO) | — | Only include files modified on/before this date (`YYYY-MM-DD`). |
| `--not` | str | — | Exclude files containing this term. Repeatable. |
| `--explain` | flag | off | Print per-signal score breakdown for each result. |
| `--extract` | `code` \| `all` \| `none` | `none` | Print extracted code blocks (`code`), full extraction (`all`), or just scores (`none`). |
| `--dedup` | flag | off | Collapse near-duplicate results into clusters. |
| `--dedup-threshold` | float | 0.85 | Jaccard threshold for near-dup (0–1). |
| `--keep-variants` | flag | off | With `--dedup`, report all version/path variants instead of collapsing. |

**Examples:**

```bash
# Basic dig
python3 scripts/excavate.py dig ./sessions --query "kafka rebalance"

# Top 10 with score breakdown
python3 scripts/excavate.py dig ./sessions --query "pool exhaustion" --top 10 --explain

# Date window, exclude sidekiq mentions, dedup
python3 scripts/excavate.py dig ./sessions \
  --query "redis cache" \
  --after 2024-01-01 --before 2024-06-30 \
  --not sidekiq \
  --dedup

# Extract code blocks only
python3 scripts/excavate.py dig ./sessions --query "ffmpeg concat" --extract code
```

### `index` — build a reusable index

```bash
python3 scripts/excavate.py index <directory> --out <index-file> [options]
```

Scans `<directory>` once and serializes the `ArchaeologyIndex` to `<index-file>` (pickle format). Subsequent `query` calls load the index instead of re-scanning.

**Options:**

| Flag | Type | Default | Description |
|---|---|---|---|
| `--out`, `-o` | path (required) | — | Output index file path. |
| `--after` / `--before` | date | — | Pre-filter by mtime at index time (cannot be relaxed later). |

**Example:**

```bash
python3 scripts/excavate.py index ./sessions --out sessions.idx
```

### `query` — search an existing index

```bash
python3 scripts/excavate.py query <index-file> --query <terms> [options]
```

Loads `<index-file>` and runs a search. Accepts the same options as `dig` (`--top`, `--not`, `--explain`, `--extract`, `--dedup`, etc.), except date filters (those were applied at index time).

**Example:**

```bash
python3 scripts/excavate.py query sessions.idx --query "oauth refresh" --top 3 --explain --dedup
```

## File formats

`excavate.py` auto-detects format by extension:

| Extension | Parsing |
|---|---|
| `.md`, `.markdown` | Raw text. Honors YAML frontmatter (between `---` fences) for date extraction. Fenced code blocks (``` ``` ```) extracted for structural pass. |
| `.txt` | Raw text. No frontmatter support. |
| `.json` | Expected to be a single object or array of message objects with `role` and `content` fields. Content fields are concatenated. |
| `.jsonl` | Each line is a JSON object with `role` and `content`. Concatenated in order. |

For `.json` / `.jsonl`, the script looks for common field names: `content`, `text`, `message`, `body`. If your format differs, pre-process to `.md` or `.txt`.

## Scoring flags

See `references/relevance-scoring.md` for the scoring model. The weights are constants in the script; retune by editing:

```python
WEIGHT_DENSITY    = 0.25
WEIGHT_RECENCY    = 0.15
WEIGHT_CODE       = 0.25
WEIGHT_RESOLUTION = 0.35
```

## Programmatic API

```python
from excavate import ArchaeologyIndex, SearchHit

idx = ArchaeologyIndex()
idx.scan("./sessions")                    # walk directory, parse files
idx.save("sessions.idx")                  # serialize
idx2 = ArchaeologyIndex.load("sessions.idx")

hits: list[SearchHit] = idx.search(
    query="kafka rebalance",
    top=5,
    explain=True,                         # populate hit.explanation
    exclude=("sidekiq",),                 # --not terms
)

for hit in hits:
    print(hit.path, hit.score, hit.explanation)
    print(hit.extraction)                 # extracted code/text
```

### `SearchHit` fields

| Field | Type | Description |
|---|---|---|
| `path` | str | File path. |
| `score` | float | Composite score in [0, 1]. |
| `explanation` | dict \| None | Per-signal breakdown (populated when `explain=True`). |
| `extraction` | str | Extracted artifact (code block or relevant excerpt). |
| `matches` | list[str] | Matched line snippets. |
| `mtime` | float | File modification time. |

## Exit codes

| Code | Meaning |
|---|---|
| 0 | Search completed (including no hits). |
| 2 | Argument error (missing required flag, bad value). |
| 3 | I/O error (directory not found, unreadable file). |

## Performance

- **Scan speed:** ~1,000 files/sec on markdown, ~3,000/sec on plain text (single-threaded, SSD).
- **Index size:** roughly 30–50% of the source corpus (pickle-serialized parsed text + metadata).
- **Query speed:** <100ms for corpora under 10k files (in-memory).
- **Memory:** proportional to corpus size; the index holds parsed text in memory for fast repeated queries.

For corpora above ~50k files, prefer `session_search` (FTS5-backed) over `excavate.py`.
