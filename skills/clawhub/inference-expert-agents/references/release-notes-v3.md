# Release notes — v3.0.0 / v3.0.1

## v2.2 (additive — no default output changed)

- **`retrieval.py`** — local BM25 retrieval over sqlite FTS5 (`build`/`query`/`stats`):
  index your sources, fetch evidence snippets for `grounding_gate` (retrieve before
  asserting). Index is opt-in state (`--db`, 0600).
- **`brevity.py`** — rule-based output condenser: strips openers ("Sure, here is…"),
  boilerplate sentences, and throat-clearing phrases; never touches sentences with
  numbers, quotes, citations, or URLs; reports `saved_pct` + everything dropped.
- **`jsonfix.py`** — staged near-JSON repair for small-model output: fence-strip →
  prose-trim → trailing-comma fix → Python-literal conversion → bracket closing, with a
  `repairs` log; unrepairable input → clean `{"error"}` + exit 2.
- **Opt-in upgrades**: `_compact --keys`/`--expand`; `grounding_gate` `rouge_l_recall`;
  `speed measure --samples-file`; `selfimprove rank --method thompson` (+`--seed`);
  `portability --emit-prompt`; MCP `readOnlyHint`; `_common.fail` `hint`. One behavior
  fix: `cove` classifies `UNSUPPORTED`/hedged answers as `unverified`, never `refuted`.

Loaded on demand; not part of the SKILL.md prefix an agent pays for every turn.

## What's new in v3.0.0 (correctness release — these were wrong answers, not crashes)

The 97-assertion self-test passed before every fix below; all of these were found by
executing the tools against adversarial-but-legal inputs and by re-verifying the
skill's own citations against primary sources.

- **`selfcheck.py` no longer cries wolf.** Overlap was computed between a fact and
  an *entire* sampled response, so a fact quoted verbatim and correctly inside a
  longer answer scored low. Measured before the fix: a fact all 3 samples stated
  correctly returned `hallucination_risk 0.667` / label "possible". Matching is now
  sentence-level (length-invariant). A detector that flags true statements gets
  ignored, which is worse than no detector.
- **`selfcheck.py` with <2 samples is now `measurable: false`, not maximal risk.**
  One sample carries no information, yet the old code returned `risk 1.0` / "likely"
  for every fact — and `portability.py` assigns `samples: 1` to the local tier, so
  on local models this tool flagged *every* fact as a likely hallucination. Scores
  are now `null` with an explicit `warning`; a fake 1.0 is never emitted.
- **`grounding_gate.py` can no longer be configured into a no-op.** `--lex`/`--sem`
  are validated to (0, 1]. Verified before the fix: `--lex -1 --sem -1` returned
  `verdict: grounded`, `decision: accept` for "Aspirin cures cancer in mice"
  against evidence about rainfall in Chile.
- **`grounding_gate.py` counts what it skips.** Sentences under 4 words were dropped
  from the audit silently, so `n_sentences` undercounted and an answer could look
  fully grounded while its short claims were never checked. Now reported as
  `n_skipped_short` / `skipped_short`, and `n_audited` is the honest denominator.
- **`grounding_gate.py` factual/filler classifier can now classify.** The old
  pattern `[^.!? ]{3,}` matches any 3+ character word, so the disjunction was true
  for essentially every sentence and `opinion_or_fill` was unreachable.
- **`conformal.py` validates its risk parameters and label schema.** `--delta 0`
  reached `log(1/0)`; `--alpha 5` "calibrated" against a meaningless target; a
  wrong-shaped labels file surfaced as a bare `TypeError` with no hint. Empty
  labels is now a usage error, not a successful "abstain-by-default".
- **12 citation errors corrected in `references/verified-grounding.md`**, including
  a fabricated arXiv id and an inverted correlation sign. See the audit method at
  the end of that file; re-run it with `tools/citecheck.py`.
