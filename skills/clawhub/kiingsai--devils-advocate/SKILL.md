---
name: "devils-advocate"
description: "Trigger /devil to pressure-test a decision through a multi-model council, fact-check pass, peer review, and a mandatory devil's-advocate stress test."
---

# Devil's-Advocate (/devil)

Run a real decision through 5 independent AI advisors — across two model families when available — a fact-check pass, peer review, a mandatory adversarial stress test, and a confidence-rated final verdict.

Not a theoretical prompt template. Built by running it live, twice, on a real decision, watching exactly where it broke, and fixing that specific failure instead of guessing at improvements. Two real bugs got caught and fixed this way — see [Guardrails](#guardrails).

## Requirements

| Capability | Needed for | If missing |
|---|---|---|
| Parallel sub-agent spawning | Steps 2, 5, 7 (the whole council) | Required — this skill doesn't work without it |
| A second model/provider | Step 2's multi-model routing | Falls back to single-model — still works, loses one layer of diversity |
| Web search / fetch | Step 1's auto data-lookup | Falls back to asking the user for facts directly |
| Browser automation | Step 1's JS-rendered page lookup (e.g. live dashboards) | Falls back to web fetch, then asking the user |
| Cron / scheduled follow-up | Step 10's outcome check-in | Skip Step 10 — everything else still runs |

Every non-required capability degrades gracefully. Run this with nothing but sub-agent spawning and it still does the core job: 5 lenses, peer review, mandatory devil's advocate, confidence rating.

## Trigger

Activate on `/devil`, or natural phrases: "devil's advocate this", "council this", "run this by the council", "pressure-test this", "stress-test this", "war room this", "what would you do". Don't trigger on simple factual lookups or low-stakes preference questions with no real tradeoff.

## Step 1 — Frame the question

Before spawning anyone, gather real data: scan relevant context you already have access to (memory/context files, anything the user referenced or attached).

If the question depends on external facts (stats, prices, public page content, etc.) that aren't already known, try to get them automatically before asking the user:
1. Plain lookup first — web search/fetch for anything reachable that way (APIs, static pages, RSS, public data endpoints).
2. If that fails or the page is JS-rendered (dashboards that require a real browser to load), use browser automation if available.
3. Only fall back to asking the user once automated lookups genuinely fail — the data is private, behind a login, or plain doesn't exist online. Don't ask by default when it's pullable.

One clarifying question max if the ask is still too vague after that.

Write ONE context block containing the question plus all real facts gathered, noting which facts were pulled live vs. given by the user vs. unavailable. This exact block gets reused verbatim in every later step — see Step 5, this is a hard rule, not a suggestion.

## Step 2 — 5 advisors, spawned in parallel, across two model families when possible

Same context block, five agents, each told to argue independently and not hedge. If you have access to a second model/provider, route two advisors to it instead of running all 5 on one model — the council shouldn't just be one model wearing five masks. Genuine architectural disagreement catches blind spots a single model shares across all its own personas:

1. **The Contrarian** — *route to the alternate model if available* — looks for what's wrong, what will fail, assumes a fatal flaw exists and digs for it.
2. **The First Principles Thinker** — default model — ignores the surface question, asks what's actually being solved, will say "you're asking the wrong question" if warranted.
3. **The Expansionist** — default model — looks for upside nobody else sees, doesn't care about risk, cares what happens if this works better than expected.
4. **The Outsider** — *route to the alternate model if available* — zero context about the user or their history, reacts to only what's in front of them, catches the curse of knowledge.
5. **The Executor** — default model — only cares if it can actually be done and how fast, ignores theory, wants a concrete first step.

150-300 words each. No preamble.

**Why the Contrarian and Outsider specifically, not any 2 of 5:** those are the lenses whose entire job is catching what the "home" model's own blind spots miss — putting exactly those two on a different architecture compounds the effect where it matters most. Routing all 5 would lose the benefit of a stable "home team" the chairman and devil's advocate can reason consistently against.

If the alternate model is unavailable or errors out, fall back to the default model for that advisor and note in the final verdict that this run was single-model — don't block the whole council on one model being down.

## Step 3 — Fact-check pass (done by you directly, no agent spawn)

Before triage or peer review, go through each of the 5 advisor responses individually and pull out every specific factual claim tied to real data (numbers, named events, cited outcomes).

Check each claim against the actual Step 1 context block:
- **Matches the source data** → leave it as-is.
- **Contradicts the source data, or cites real data that doesn't actually support the conclusion drawn from it** → flag it inline directly on that response, e.g. `[FACT-CHECK: source data shows X, not Y]`. Don't silently delete it — mark it so the correction stays visible to every later step.
- **Isn't verifiable from the source data at all** → flag it as unverified rather than assuming it's wrong.

This is mechanical, not evaluative — you're checking whether an argument's factual anchors are real, not judging whether the argument itself is good. Carry the flagged/annotated responses forward into triage, peer review, and synthesis instead of the raw originals.

## Step 4 — Confidence triage (before peer review, done by you directly, no agent spawn)

Skim the 5 (now fact-checked) responses yourself. Check two things:
- **Does the recommendation split roughly evenly** (e.g. 3-2, or 2-2-1) rather than converge (4-5 agreeing)?
- **Did Step 3 flag any claim as contradicted or unverified?** A flagged claim is an automatic signal here.

If either is true, tag this internally as a CLOSE CALL. This does not change or skip any later step — peer review (Step 5) and the devil's advocate (Step 7) both run exactly the same either way. The flag only changes what gets said in the final confidence rating (Step 8).

## Step 5 — Peer review, 5 reviewers, IDENTICAL context

Runs regardless of the Step 4 flag, default model for all reviewers. Anonymize the 5 fact-checked responses as A-E (randomize the letter mapping, and don't reveal which model produced which). Spawn 5 new reviewer agents. Each one gets the EXACT SAME context block from Step 1 plus all 5 anonymized, fact-checked responses in full — including any `[FACT-CHECK: ...]` annotations from Step 3. Each reviewer answers:
1. Which response is strongest, and why?
2. Which response has the biggest blind spot?
3. What did all five miss?

**Why identical context is a hard rule, not a nice-to-have:** compressing or summarizing the context block for reviewers causes reviewers to flag real, given facts as if the advisor invented them — a false-hallucination accusation, caught live in testing. Keep the full block, verbatim, every time.

Under 200 words per review.

## Step 6 — Chairman synthesis (draft verdict)

One agent, default model, gets everything: all 5 fact-checked responses (de-anonymized), all 5 peer reviews, and the CLOSE CALL flag from Step 4 if set. Produces a draft verdict: where the council agrees, where it clashes, blind spots peer review caught, any fact-check corrections that materially affect the recommendation, a recommendation, one concrete next step.

## Step 7 — Mandatory devil's advocate (runs every time, not just on CLOSE CALL)

Spawn one more agent, default model, regardless of how confident Step 6's draft looks. Give it the draft recommendation and the ORIGINAL real data from Step 1 — not the advisor discussion, the source facts. Instruction: build the single strongest case against this recommendation using only the real data provided. No speculation, no new hypotheticals — if the case can't be built from what's actually known, say so plainly instead of inventing a reason.

You (not a new agent) check the devil's advocate's case against the source data:
- If it exposes a real contradiction or gap → the final verdict MUST incorporate the correction. Don't bury it, lead with it.
- If it doesn't hold up under the real data → note in the final verdict that the recommendation was stress-tested and held.

**Why four separate checking layers (Step 3 fact-check, Step 4 triage, Step 5 peer review, Step 7 devil's advocate) exist and aren't redundant:** they catch different failure classes. Fact-check verifies individual claims immediately at the source, mechanically, before anything downstream can be built on a bad one. Triage catches an obvious self-contradiction or a fact-check flag fast and cheap, before spending on review. Peer review catches weak arguments and missed considerations through broad evaluative critique — it might or might not catch a specific factual error, that's incidental to its real job. The devil's advocate is the only step whose sole job is attacking the final conclusion against real data, after synthesis. Don't collapse these into one step even though they overlap in what they *can* catch — they're layered on purpose, not duplicated by accident.

## Step 8 — Present the verdict, with confidence rating

Post directly, markdown, no separate file:

```
## Council Verdict: {short topic}

### Confidence: {HIGH | LOW}
{One line: HIGH = advisors converged, reasoning held under devil's-advocate stress test, no material fact-check flags. LOW = split decision, and/or a fact-check flag or the devil's advocate exposed a real flaw, and/or the real data feeding the debate was too thin to establish a genuine pattern. If LOW, say plainly: this is closer to a coin flip than a verdict, and recommend a second independent run before committing anything expensive to reverse.}

### Fact-Check Corrections
{Only include this section if Step 3 flagged anything. List each flagged claim and what the source data actually shows.}

### Where the Council Agrees
### Where the Council Clashes
### Blind Spots the Council Caught
### What the Devil's Advocate Found
{Even if it didn't survive, say what it tried and why it failed — this is the receipt that the verdict was actually stress-tested, not just asserted.}
### The Recommendation
### The One Thing to Do First
```

If Step 2 fell back to single-model for any advisor, note it briefly at the end of the verdict.

## Step 9 — Optional: log the transcript

Only if the user asks, or the decision is clearly significant. Ask which note/log/location to use if this comes up — don't invent a new convention on the fly. If Step 10 (outcome tracking) gets scheduled, log the transcript regardless of significance — otherwise there's nothing for the follow-up to update.

## Step 10 — Optional: schedule an outcome check-in (requires a scheduling/cron capability — skip if unavailable)

Only after presenting the Step 8 verdict, and only if "The One Thing to Do First" is a concrete, checkable action (not something vague like "think about it more"). Ask the user: "Want me to check back on this later and log what actually happened?"

**Opt-in only — never schedule this automatically.** If the user says no or doesn't respond to this specific offer, drop it, don't ask again for this verdict.

If yes: ask the user how long to wait before checking back, rather than assuming a default — a same-day post and a multi-week test have wildly different natural check-in windows, so a hardcoded number would be wrong most of the time.

Once you have a timeframe, schedule a one-shot follow-up that fires in the same conversation, references the specific verdict topic and the exact recommended action, asks what actually happened, and instructs itself to append the real outcome next to the original logged verdict (Step 9's note) — this is what actually builds a track record over time instead of leaving every verdict a one-shot guess.

If Step 9 didn't log a transcript for this verdict, log one now before scheduling — the follow-up needs something to update.

## Guardrails

- **Identical context at every step (Step 5's hard rule) is the single most likely thing to silently break if edited carelessly.** This is not theoretical: in live testing, compressing the context block for peer reviewers caused two reviewers to accuse an advisor of fabricating details that were real, given facts — just facts the reviewers weren't shown. Keep the full block byte-for-byte identical at every step that needs it.
- Step 3's fact-check, Step 4's triage, and Step 7's case-check are done inline by you, not spawned agents — keep them free. Only Steps 2, 5, 6, and 7's devil's advocate itself are actual agent calls.
- Fact-check flags real claims, doesn't delete them — downstream steps need to see what was said AND what was wrong with it, not a scrubbed version.
- Devil's advocate runs every time, not just on flagged close calls — cheap insurance against a majority that looks solid but isn't. This already happened once live: 4 of 5 advisors converged on a conclusion, and the evidence one of them cited as proof actually contradicted it. Nobody would have caught it without a step whose only job was attacking the final answer.
- LOW confidence gets said explicitly, not softened. A verdict that reads as certain when the underlying signal is thin is worse than useless — it's actively misleading. On a real test run, the same two questions run twice on identical data produced an inverted majority on one of them — a genuine coin flip that a single confident-sounding pass would have hidden.
- Don't auto-run a second independent pass by default — that doubles cost every time. Recommend it explicitly when confidence is LOW, let the user decide, per how much is actually riding on the decision.
- Real data over guesses (Step 1) — try automated lookup before asking the user; only ask when lookup genuinely can't reach the data.
- Outcome check-ins are always opt-in (Step 10) — never schedule one without an explicit yes.
