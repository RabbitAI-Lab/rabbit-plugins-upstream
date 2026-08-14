# Capture — Turning Input Into Things You Can Be Tested On

Read during and after any input session: reading, a lecture, a video, a mentor conversation, a debugging session. The output is queue items, error-log rows, and occasionally an artifact — never a pile of notes nobody reopens.

**Contents:** [The Only Question That Matters](#the-only-question-that-matters) · [Notes vs Items](#notes-vs-items) · [Writing an Item](#writing-an-item) · [Atomicity](#atomicity) · [Item Shapes](#item-shapes) · [What Not to Capture](#what-not-to-capture) · [Capturing From Each Source](#capturing-from-each-source) · [Cheat Sheets](#cheat-sheets) · [The Backlog Trap](#the-backlog-trap)

## The Only Question That Matters

For every candidate: **"When will I need to produce this without looking it up?"**

| Answer | Destination |
|---|---|
| Regularly, and lookup would break my flow | Queue item (`schedule.md`) |
| Rarely, and lookup is cheap | Nowhere. Leave it in the source |
| Never — but I will need the *conclusion* | A line in the plan or a cheat sheet |
| I got this wrong just now | `## Error Log`, with the misconception |
| It is a procedure I will re-execute | `artifacts/` as a written procedure |

Everything captured has a cost paid daily for years (Rule 3's ratio). The default answer is "nowhere", and applying that default is what keeps the queue alive.

## Notes vs Items

Notes are for **thinking**; items are for **remembering**. They are different artefacts with different lifetimes, and merging them produces a vault that is neither.

- Notes written during input are working memory extended to paper. They are allowed to be messy and they are allowed to be thrown away.
- Items are the subset that survives the question above. Making them is a separate pass, ideally at the end of the session while context is still loaded.
- The pass has a time cost of roughly 20-30% of the input time. Budget it, or the input session ends with nothing durable and the "I'll make cards later" backlog begins.
- Notes that are genuinely re-read — a derived summary, a procedure, a decision — are artifacts, not notes: they go in `artifacts/` with a read condition (`memory-template.md`).

## Writing an Item

Five properties. An item missing any of them becomes a leech (`schedule.md`).

| Property | Test | Failure |
|---|---|---|
| One fact | Only one thing can be wrong | "Name the three types and their uses" |
| Unambiguous cue | Exactly one answer fits | "What is the default?" — of what, where? |
| Produces, not recognises | The answer must be generated | Any yes/no or option list |
| Context-free | Makes sense without the surrounding chapter | "What does it return in this case?" |
| Answerable in <10 s | Longer means it is a procedure, not an item | "Explain the memory model" |

Add the **why** to the answer side where one exists. An item whose answer is a bare string is memorisation; adding the reason makes it a small piece of understanding and, in practice, easier to retrieve.

## Atomicity

Break compound material until each item can fail independently.

Compound: *"HTTP 401 vs 403 vs 404"* → three items, plus one contrast item:

- "Which status code says the request was not authenticated?"
- "Which status code says authenticated but not permitted?"
- "Which status code hides the existence of a resource from an unauthorised caller?"
- "401 vs 403 — what distinguishes them?" (the contrast item, which is where the actual confusion lives)

The contrast item is the one usually omitted and the one that prevents the pair from becoming mutual leeches. Whenever two items interfere, the fix is a third item that contrasts them and the deletion of neither.

## Item Shapes

| Shape | Use it for | Example |
|---|---|---|
| Question → answer | Facts with a why | "Why does a floor of 1.3 exist on ease?" |
| Cloze deletion | Facts embedded in a phrase, sequences, syntax | "ease starts at {{2.5}} and floors at {{1.3}}" |
| Reverse pair | Anything needed in both directions (vocabulary, notation) | word→meaning **and** meaning→word, as two items |
| Cue → procedure | Short procedures with fixed steps | "Queue overdue by two days — what is the first action?" |
| Contrast | Two confusable things | "Blocked vs interleaved — what does each buy?" |
| Image or audio occlusion | Anatomy, diagrams, chords, pronunciation | Hide the label, produce it |
| Production prompt | Skills, not facts — no card, a drill | Not an item at all; goes to `practice.md` |

The last row matters: pushing a skill into the queue is the most common capture error. Queues hold what must be *recalled*; skills are maintained by being *performed*.

## What Not to Capture

- Anything you can derive in under a minute from something already in the queue.
- Anything you will look up in an IDE, a manual, or a search box in the moment — the queue is not documentation.
- The definition of a term you will meet constantly anyway; frequency is a free scheduler.
- Anything you do not currently understand. A memorised string with no model transfers to nothing and inflates false confidence (`verification.md`).
- Version-specific trivia in a volatile field: it will be wrong before it matures in the queue.

## Capturing From Each Source

| Source | Capture protocol |
|---|---|
| Book chapter | Do the exercises first; the items come from what the exercises exposed, not from the highlights |
| Lecture or video | Notes during, items after, from memory — writing items from memory is itself a retrieval rep |
| Documentation | Capture only what you looked up twice. The second lookup is the signal |
| Mentor or code review | Capture the **correction**, and the reasoning behind it, as an error-log row before an item |
| Your own debugging | The root cause and the tell that would have shortened it. Nothing else from a debugging session is worth keeping |
| A conversation in a target language | The gap you hit, not the whole exchange — the sentence you could not finish is one item |

## Cheat Sheets

The compressed reference the learner derives themselves, kept as `artifacts/cheatsheet-<topic>.md`.

- Built **from the error log**, not from the source. A cheat sheet copied from a book is a worse copy of the book; one built from your own mistakes is the shortest possible reference for you specifically.
- Rebuilding it from memory once a month is a high-value retrieval exercise, and the diff shows what decayed.
- It is a bridge, not a destination: anything still on the sheet after the topic reaches Retention level is a candidate queue item, because it is being looked up and not recalled.

## The Backlog Trap

"I will make the items later" produces a growing pile of un-processed material and a growing sense of debt. Two rules kill it:

1. **Items are made in the session that produced them**, or not at all. Material re-opened cold costs 3-4× the time because context has to be rebuilt.
2. **Cap the pile.** If un-processed material exceeds one session's worth, process the newest and delete the rest. Old un-processed input is not an asset; it is a reminder of a session that did not finish.

Write items straight into `## Review Queue` in `memory.md` (or `reviews/<topic>.md` once split) as they are made, never into a holding file. Corrections and misconceptions go to `## Error Log` in the same turn. A derived cheat sheet or procedure becomes `artifacts/<kebab-name>.md` with its `## Boxes` line and a read condition. Formats and thresholds in `memory-template.md`.
