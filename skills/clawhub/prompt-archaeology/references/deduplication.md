# Deduplication

The same fix often appears in three sessions: the first attempt, the retry, and the "oh and also" follow-up. Deduplication collapses these into a single canonical answer before you report.

`excavate.py --dedup` runs three layers of dedup in order: exact → near-dup → variant.

## Layer 1: Exact dedup

**Rule:** identical fenced code blocks collapse to one.

Two sessions with byte-identical ` ```bash ... ``` ` blocks are the same artifact. Keep the higher-scoring session as the canonical instance; drop the others from the result set but note them as duplicates.

```
sessions/fix-v1.md        score 0.71    [canonical]
  ≡ sessions/fix-v1-retry.md             (exact dup of fix-v1.md)
  ≡ sessions/fix-v1-followup.md          (exact dup of fix-v1.md)
```

Exact dedup is cheap (a hash) and catches the easy cases.

## Layer 2: Near-dup detection

**Rule:** normalized text similarity > 0.85 merges into a cluster.

Two sessions that describe the same fix in slightly different words are the same artifact. Near-dup uses **normalized token overlap**:

1. Lowercase, strip punctuation, remove stopwords.
2. Tokenize on whitespace.
3. Compute Jaccard similarity: `|A ∩ B| / |A ∪ B|`.
4. If Jaccard > 0.85, merge.

Keep the highest-scoring session in the cluster as canonical.

```
sessions/2024-03-12-a.md  score 0.82    [canonical]
  ≈ sessions/2024-03-13-b.md            (near-dup, Jaccard 0.91)
  ≈ sessions/2024-03-14-c.md            (near-dup, Jaccard 0.88)
```

### Tuning the threshold

- **0.85 (default):** conservative. Only clearly-the-same fixes merge.
- **0.75:** aggressive. Catches more dups but risks merging distinct fixes that share boilerplate (e.g., two different nginx fixes with similar config structure).
- **0.95:** paranoid. Almost only exact dups merge.

Set via `--dedup-threshold` on the CLI, or `DEDUP_THRESHOLD` in code.

### What gets normalized away

- Case (`Error` ≡ `error`)
- Punctuation (`failed.` ≡ `failed`)
- Stopwords (`the connection pool` ≡ `connection pool`)
- Whitespace runs

### What does NOT get normalized away

- Numbers and identifiers (`pool_size=20` ≢ `pool_size=50`)
- Code structure (two fenced blocks with different commands stay distinct)
- File paths

## Layer 3: Variant detection

**Rule:** if two snippets differ only in a version number, path, or date, treat as the same artifact and note the latest variant.

```
sessions/2023-09-01.md:  pip install fastapi==0.68.0
sessions/2024-03-12.md:  pip install fastapi==0.110.0
```

These are the same artifact ("install fastapi") with a version variant. Collapse to one, note the latest (0.110.0).

Variant detection works by:

1. Masking version-like tokens (`\d+\.\d+\.\d++`), date-like tokens, and path-like tokens.
2. Re-running near-dup (Layer 2) on the masked text.
3. If they merge, they're variants.

### When variants matter

Sometimes the variant *is* the artifact — e.g., "the exact version that worked with Python 3.9." Variant detection has a `--keep-variants` flag that reports all variants instead of collapsing, for these cases.

## Output format

With `--dedup`, results print as clusters:

```
=== Cluster 1 (3 sessions, canonical score 0.82) ===
  [canonical] sessions/2024-03-12-a.md        score 0.82
  [dup]       sessions/2024-03-13-b.md        near-dup (Jaccard 0.91)
  [dup]       sessions/2024-03-14-c.md        near-dup (Jaccard 0.88)

=== Cluster 2 (1 session, canonical score 0.64) ===
  [canonical] sessions/2024-02-20-x.md        score 0.64
```

Report only the canonical session per cluster to the user; mention duplicate counts inline if relevant ("found in 3 sessions").

## Anti-patterns

- **Dedup before scoring.** Always score first, then dedup — the highest-scoring session must be the canonical one.
- **Aggressive near-dup on small corpora.** With <50 sessions, a 0.75 threshold will over-merge. Stick to 0.85+.
- **Collapsing variants when versions matter.** If the user asked "which version worked?", `--keep-variants` is mandatory.
- **Reporting every member of a cluster.** The user wants the answer, not the cluster graph. Report canonical; mention dup count.
- **Dedup across different artifact types.** A fix and a rejection of the same approach are *different artifacts* even if textually similar. Dedup within artifact type.
