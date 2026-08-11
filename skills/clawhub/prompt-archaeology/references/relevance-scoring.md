# Relevance Scoring in Depth

`excavate.py` ranks sessions with a **transparent, composite score** — not a black-box embedding. Every ranking is explainable. This doc covers the math, normalization, and how to retune for your corpus.

## The four signals

| Signal | What it measures | Default weight | Range |
|---|---|---|---|
| `density` | match count relative to session length | 0.25 | [0, 1] |
| `recency` | newer sessions score higher | 0.15 | [0, 1] |
| `code` | does the session contain runnable code/commands? | 0.25 | [0, 1] |
| `resolution` | success markers like "that fixed it", "works now", "merged" | 0.35 | [0, 1] |

Weights sum to 1.0. Composite score is the weighted sum, also in [0, 1].

## Why these weights

- **Resolution dominates (0.35).** A session that explicitly says "that fixed it" is the strongest possible signal. Prose that merely mentions the term is weak evidence by comparison.
- **Density and code tie (0.25).** A session densely packed with the term is probably *about* it; a session with code is probably *solving* it. Both matter; neither alone is decisive.
- **Recency is the tiebreaker (0.15).** Useful, but not authoritative — a two-year-old fix to an algorithmic problem is still correct.

## Normalization

Each signal is normalized to **[0, 1]** before weighting, so a corpus change doesn't silently inflate one signal.

### density

```
density(session) = match_count / max(match_count across corpus)
```

A session with 12 matches ranks at density 1.0 *only if* 12 is the max in the corpus; if another session has 50 matches, the 12-match session ranks 0.24. This is why raw match count is a bad proxy — density is relative.

The implementation also applies a **log saturation** so that one very long session doesn't dominate:

```
density(session) = log(1 + match_count) / log(1 + max_match_count)
```

### recency

```
recency(session) = (session_mtime - corpus_min_time) / (corpus_max_time - corpus_min_time)
```

Linear interpolation between the oldest and newest session in the corpus. If the corpus spans 2022–2025, a mid-2024 session scores ~0.6.

### code

```
code(session) = 1.0 if session contains ≥1 fenced code block or shell command
              = 0.5 if session contains inline `code` only
              = 0.0 otherwise
```

Binary-ish. A session with code is qualitatively different from one without.

### resolution

```
resolution(session) = (count of resolution markers) / max(count of resolution markers across corpus)
```

Capped at 1.0. Resolution markers (see below) are weighted by type.

## Resolution markers

The marker lexicon lives in `excavate.py` as `RESOLUTION_MARKERS`. It groups phrases by strength:

| Strength | Examples |
|---|---|
| Strong (×1.0) | "that fixed it", "works now", "merged", "deployed", "shipped" |
| Medium (×0.7) | "fixed", "resolved", "solved", "working" |
| Weak (×0.4) | "seems to work", "might be it", "I think that's it" |

A session with one strong marker outscores a session with three weak ones.

## Retuning weights

Weights are constants at the top of `excavate.py`:

```python
WEIGHT_DENSITY    = 0.25
WEIGHT_RECENCY    = 0.15
WEIGHT_CODE       = 0.25
WEIGHT_RESOLUTION = 0.35
```

### When to retune

| Your corpus | Change |
|---|---|
| Fast-moving domain (frontend deps, infra) | Bump `RECENCY` to 0.25, drop `DENSITY` to 0.15 |
| Stable domain (algorithms, math, CS theory) | Drop `RECENCY` to 0.05, bump `RESOLUTION` to 0.45 |
| Mostly code (debugging transcripts) | Bump `CODE` to 0.35, drop `DENSITY` to 0.15 |
| Prose-heavy (design discussions, few markers) | Drop `RESOLUTION` to 0.20, bump `DENSITY` to 0.40 |
| Logs lack success markers entirely | Set `RESOLUTION` to 0.0 — it'll only add noise |

### How to retune

Edit the constants, then validate on a small labeled set (sessions where you *know* the right answer). The top-1 hit rate should climb as you tune toward your corpus's character.

## Why not embeddings?

Embeddings would raise recall on the semantic-adjacent pass, but:

1. **They're opaque.** The user asks "why did you trust that session?" and you can't answer. The composite score answers in one line.
2. **They need a model.** `excavate.py` is stdlib-only and runs anywhere. Adding a model breaks that.
3. **They need a corpus big enough to matter.** For most personal session corpora (hundreds to low thousands of sessions), keyword + structural + the composite ranker is competitive with embedding search and far cheaper.

If you have a large corpus and want semantic recall, run `session_search` (FTS5) or an embedding index for the semantic pass, then feed those candidates into `excavate.py`'s scorer. The signals compose.

## The `--explain` output

`excavate.py --explain` prints, per result:

```
sessions/2024-03-12-kafka-fix.md
  score: 0.82
    density    0.71   (12 matches, log-saturated)
    recency    0.64   (2024-03-12, within corpus range)
    code       1.00   (3 fenced blocks)
    resolution 1.00   (1 strong marker: "that fixed it")
```

This is the explainability contract. If a ranking looks wrong, `--explain` shows you exactly which signal is off and whether to retune.
