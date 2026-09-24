# Schedule — Spaced Review, Its Math, and Its Bill

Read when items go into the queue, when reviews are graded, when the queue is overdue, and before adding new material at volume. Every threshold here scales with `daily_review_limit` and `retention_target`.

**Contents:** [The Interval Formula](#the-interval-formula) · [Grading](#grading) · [The Workload Bill](#the-workload-bill) · [Retention Target Economics](#retention-target-economics) · [The First Interval](#the-first-interval) · [Overflow and Backlog](#overflow-and-backlog) · [Leeches](#leeches) · [When Spacing Is the Wrong Tool](#when-spacing-is-the-wrong-tool) · [Running It Without an App](#running-it-without-an-app) · [Deck-Free Spacing](#deck-free-spacing)

## The Interval Formula

SM-2 shape, which every mainstream scheduler is a variation of:

```
next_interval = last_interval × ease
ease starts at 2.5, floor 1.3, no ceiling in practice above ~3.0
```

Worked example, one item at `retention_target` 0.90:

| Review | Grade | Ease after | Interval after | Next due |
|---|---|---|---|---|
| 1 (new) | good | 2.50 | 1 d | +1 d |
| 2 | good | 2.50 | 3 d | +3 d |
| 3 | good | 2.50 | 7 d | +7 d |
| 4 | hard | 2.35 | 8 d (7 × 1.2, the hard step) | +8 d |
| 5 | again | 2.15 | 1 d, history kept | +1 d |
| 6 | good | 2.15 | 4 d (post-lapse restart at ~50% of the pre-lapse 8 d, not 1 × 2.15) | +4 d |

Two properties that matter more than the exact numbers: intervals **expand multiplicatively**, and a failure costs ease permanently while costing the interval only temporarily. That asymmetry is what stops a bad item from silently consuming the schedule forever — it drives the item toward the leech threshold instead.

## Grading

Four grades, and the grade is about **retrieval effort**, not about whether the answer was eventually produced:

| Grade | Meaning | Interval effect | Ease effect |
|---|---|---|---|
| again | Could not produce it, or produced it wrong | Reset to 1 d, history kept | −0.20 |
| hard | Produced it, slowly or partially | × ~1.2 (a small step, not a repeat) | −0.15 |
| good | Produced it with normal effort | × ease | unchanged |
| easy | Instant, no reconstruction at all | × ease × 1.3 | +0.15 |

- **"Easy" is a diagnosis, not a reward.** Three easies in a row means the item was already known and is stealing review budget — suspend it or fold it into a harder item.
- Grade **before** discussing the answer. A grade assigned after the explanation is a grade on the explanation.
- Partial credit does not exist for a two-state fact and does exist for a procedure. For procedures, grade the step that failed, not the whole chain.

## The Workload Bill

The number nobody computes before starting, and the reason most queues are abandoned:

```
steady_state_daily_reviews ≈ new_items_per_day × R
R ≈ 8-12 at retention_target 0.90
```

`R` is the empirical ratio observed in mature queues, not a derived constant — it drifts with material difficulty and grading honesty. Use 10 for planning.

| New items/day | Steady-state daily reviews | Minutes/day at ~8 s per item |
|---|---|---|
| 5 | ~50 | ~7 |
| 10 | ~100 | ~13 |
| 20 | ~200 | ~27 |
| 50 | ~500 | ~67 |

Steady state arrives at roughly month 3, which is why the collapse always feels sudden. Derive the sustainable intake from the cap instead:

```
sustainable_new_per_day = daily_review_limit ÷ 10
```

At the default `daily_review_limit` of 20, that is **2 new items a day** — an unpopular number, and the one that produces a queue still alive next year. Raise it only after a full month at the cap without overflow.

## Retention Target Economics

`retention_target` sets how much recall probability is purchased and how steeply.

| Target | Relative review load | Sensible for |
|---|---|---|
| 0.80 | ~0.6× baseline | Large, low-stakes bodies of material; broad exposure |
| 0.90 | 1× (default) | Almost everything |
| 0.95 | ~1.5-2× | Material where a lapse is expensive and the set is small |

Above 0.95 the load grows faster than the retention gained — this is the single most common self-inflicted workload problem, and the fix is a settings change, not more discipline. Below 0.80 the failure rate itself becomes demoralising and re-learning cost eats the savings.

## The First Interval

- First review **within ~24 hours** of first encounter. The largest drop is early; a single retrieval inside a day changes the shape of everything after it.
- Do not review new material again in the same session beyond the retrieval interrupts of the hard block (SKILL.md Rule 5). Same-session repetition feels effective and buys almost nothing on delayed tests.
- Encountered in the wild before the first review? Grade it as a review — real use is the best possible retrieval.

## Overflow and Backlog

**Overflow** (today's due count exceeds `daily_review_limit`):

1. Do the oldest-due first — an item at +9 days is closer to being lost than one at +1.
2. Push the remainder to tomorrow **without penalty**. Overdue is not a failure; the schedule's job is to serve the learner.
3. Two consecutive overflow days means intake is above the sustainable ratio. Suspend new items until the queue drains.

**Backlog** (returning after days or weeks away):

```
daily_dose = min(daily_review_limit, backlog ÷ 7)
```

Drain over a week, oldest first, adding **zero** new items until the backlog is gone. Two harder rules that save abandoned queues:

- **Never mass-delete a backlog.** Most of those items are still retrievable; the queue is more intact than it feels, and deleting is the decision that makes the previous months worthless.
- **Past ~60 days away, treat the queue as relearning, not review** (`plateaus.md`): expect a high failure rate, and do not let it re-price the ease of every item — reset intervals rather than grading a hundred `again`s.

## Leeches

An item at **5 lapses** is a leech. The memory is not the problem; the item is.

| Leech pattern | Fix |
|---|---|
| Tests two or three facts at once | Split into atomic items (`capture.md`) |
| Answer is a list | One item per element, or an ordered-recall item with a cue for each slot |
| Cue is ambiguous — several answers fit | Add the disambiguating context into the prompt |
| Interferes with a similar item (two words, two shortcuts, two theorems) | Make one item that **contrasts** them directly and delete both originals |
| Genuinely never used | Drop it. A queue is not a completeness obligation |

Record which fix was applied in `## Error Log`, and move the item to the `## Suspended` table of its review file rather than deleting it silently — a leech that vanishes without a note is re-added three months later.

## When Spacing Is the Wrong Tool

Spaced review buys **fast, unaided recall**. It is the wrong instrument when:

- Lookup is instant, free, and available at the moment of use — put the workflow in practice instead, and let the reference stay a reference.
- The thing is a **skill**, not a fact: scheduling "how to write a function" is a category error. Skills are maintained by doing them (`practice.md`, `maintenance.md`).
- The material will be used daily anyway — daily use *is* the schedule.
- Understanding is missing. Spacing a fact that makes no sense produces a memorised string that transfers to nothing; fix the misconception first (`verification.md`).

## Running It Without an App

With `sr_tool: this-skill`, the queue is the table in `memory.md` or `reviews/<topic>.md`. It works because the volume is deliberately small — the sustainable intake above is 2 items a day, and the tables stay readable at that rate.

Session protocol: read the queue, take rows whose `Next` ≤ today, oldest first, up to `daily_review_limit`; ask the prompt; take the confidence rating **before** revealing; grade; recompute `Interval`, `Ease` and `Next` by the formula; write the rows back. Overflow rows are untouched and reappear tomorrow.

With `sr_tool: anki` or another app, do not mirror the deck here: the duplicate diverges within a fortnight. Keep only the cadence row in `## Due`, the leech decisions, and the daily workload number, and say where the queue actually lives (`anki` covers deck options, FSRS and imports).

## Deck-Free Spacing

For material that resists items — a technique, a piece, a proof, a conversation topic — space the **performance** instead of a card:

| Encounter | Gap |
|---|---|
| 1 → 2 | next day |
| 2 → 3 | +3 days |
| 3 → 4 | +1 week |
| 4 → 5 | +3 weeks |
| 5 → 6 | +2 months, then maintenance (`maintenance.md`) |

Track it as a topic row with a `## Due` line, not as a hundred queue items.

After grading, write the updated rows back to `## Review Queue` in `memory.md` (or `reviews/<topic>.md` once split) in the same turn, with the confidence rating recorded before the reveal; leech decisions go to `## Error Log` and the `## Suspended` table; and the review cadence itself is a row in `## Due`. Format and split thresholds in `memory-template.md`. An interval computed and not written is a review that happens twice or never.
