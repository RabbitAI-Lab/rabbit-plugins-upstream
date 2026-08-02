---
name: arena-turn-accelerator
version: 1.4.0
description: >
  Fixes the four things that make a web agent chat feel slow, stale, dumb, or hostile:
  (1) long laggy "waiting" spinners after you hit send, (2) the agent still answering your
  PREVIOUS request after a flaky connection recovers, (3) the agent turning into a slow
  mindless "zombie" late in long conversations, and (4) needless Google/CAPTCHA human
  verification popping up when you are obviously human, (5) the agent abandoning a TRUE
  claim just because the user pushed back with displeasure instead of evidence, (6) holding
  a true claim in the WRONG VOICE - martyred, self-pitying, or joking about something serious -
  so the correct answer gets discarded anyway, and (7) an agent that either sprays unsolicited
  cleverness constantly (noise) or invents from nothing instead of from the user's own material. Provides a prompt compactor that
  reshapes input into a form models prefill 3-4x faster, a request-lifecycle fence that
  invalidates stale in-flight answers, a context-hygiene monitor that detects and reverses
  late-conversation degradation, a verification-triggers checklist that reduces bot-score
  false positives, and an intellectual-spine engine that distinguishes new evidence from mere
  social pressure so the agent holds true claims under pushback while conceding instantly to
  real facts (anti-sycophancy, explicitly not contrarianism). Use when a user reports lag, stale replies, degraded quality over time,
  repeated CAPTCHAs, or an agent that caves and flip-flops whenever it is contradicted.
---

# Arena Turn Accelerator

Seven failure modes, seven mechanisms. Field-authored in Arena Agent Mode (2026-07) with
measurements taken on a 2-core CPU box running llama.cpp.

**Scope honesty:** this is an **agent-side + client-side** skill. It cannot patch a website's
servers. Problems 1–3 are largely fixable from the agent side (that's where most of the
latency and all of the staleness and degradation actually live). Problem 4 is
*mitigation and diagnosis*, not a bypass — and deliberately so.

---

## Problem 1 — "I hit send and stare at a spinner" 🤬

### Root cause
Time-to-first-token is dominated by **prefill**: the model must ingest every token of your
prompt before emitting token one. Conversational padding ("Hi, I hope you're well, I was
wondering if you could possibly…") is pure prefill cost that carries zero information.
On top of that, a vague prompt often produces a wrong first answer, forcing a **second
round-trip** — the most expensive latency of all.

### Measured
Same question, same model (Qwen2.5-0.5B), same 2-core box:

| Prompt shape | Chars | Cold | Warm |
|---|---|---|---|
| Verbose polite phrasing | 274 | 3.47 s | 1.89 s |
| Compacted directive form | 32 | 1.02 s | 1.07 s |
| **Speedup** | −88% chars | **3.4×** | **1.77×** |

Across a mixed set, the honest average is **1.46× on warm cache, up to 3.4× cold**.
Gains scale with how much ceremony the prompt carries and with prompt length, since
prefill cost is roughly linear in tokens. No model or hardware change required.

**Don't over-claim:** compaction cannot fix server queueing or network latency. It removes
the part of the wait that your input actually causes — which on verbose prompts is most of it.

### Mechanism: `scripts/prompt_compactor.py`
Losslessly reshapes a request into the form models process fastest:
- strips filler openers/closers and hedges ("I was wondering if you could possibly")
- converts prose requests into imperative directives
- hoists the actual question to the **first line** (attention is strongest there)
- pins the output contract (format, length) so the first answer is usable
- **preserves every content-bearing token** — it removes ceremony, never constraints

```bash
python3 scripts/prompt_compactor.py --text "your long rambling prompt"
python3 scripts/prompt_compactor.py --file prompt.txt --json
```

It reports the token/char delta and an estimated latency saving, and **warns instead of
cutting** if it detects it would drop a constraint (numbers, names, code, "must", "don't").

### Agent-side rules
1. Answer the question in the **first sentence**; elaborate after.
2. Never re-state the user's question back at them — pure latency, zero value.
3. Stream partial output; a moving cursor is worth seconds of perceived speed.
4. Batch independent tool calls into one parallel block; serialize only real dependencies.
5. Never block a tool call >60 s — detach and poll (see `nonblocking-agent-execution`).

---

## Problem 2 — "Connection dropped, and now it's answering my OLD message"

### Root cause
A dropped connection does **not** cancel server-side work. When the socket recovers, the
client re-attaches to a still-running stream from a superseded request. There is no
generation fence, so the UI happily renders an answer to a question you already replaced.

### Mechanism: `scripts/request_lifecycle.py`
A monotonic **generation counter** with strict fencing:

- every user send increments `generation`; the in-flight request records the value it was born with
- any arriving chunk whose generation `<` current is **discarded, not rendered**
- on reconnect, the client resumes only if `resume_generation == current_generation`
- superseded requests are explicitly aborted, not silently orphaned
- state persists to disk, so a reload/reset can't resurrect a stale stream

```bash
python3 scripts/request_lifecycle.py new "what is X"      # -> generation 7
python3 scripts/request_lifecycle.py check 5              # -> STALE (discard)
python3 scripts/request_lifecycle.py check 7              # -> CURRENT (render)
python3 scripts/request_lifecycle.py supersede            # abort in-flight, bump
python3 scripts/request_lifecycle.py status
```

**Rule: last write wins, always.** A late answer to a dead question is worse than no answer —
it's actively misleading. Discard it.

---

## Problem 3 — "After a long chat it goes slow and mindless, like a zombie" 🧟

### Root cause
Two compounding effects:
- **Quadratic attention cost** — each turn re-processes the whole history, so latency grows
  superlinearly with conversation length.
- **Context dilution** — the original task, constraints, and definitions get buried under
  transcript noise. The model spends attention on stale scrollback instead of your actual
  goal, so it *looks* dumber while genuinely working harder. That's the "zombie" feel.

### Mechanism: `scripts/context_hygiene.py`
Monitors conversation health and prescribes the fix **before** collapse:

- tracks turn count, transcript size, and latency trend per turn
- computes a **zombie score (0–100)** from growth rate + degradation signals
- emits a graded prescription: `HEALTHY` → `WATCH` → `COMPACT NOW` → `RESET`
- generates a **carry-forward brief**: goal, hard constraints, decisions made, open items,
  artifact paths — the ~10% that matters, so a fresh context loses nothing

```bash
python3 scripts/context_hygiene.py record --turn 42 --chars 180000 --latency 14.2
python3 scripts/context_hygiene.py assess
python3 scripts/context_hygiene.py brief > CARRY_FORWARD.md
```

**Key insight: compact early, on a schedule — don't wait for the zombie.** By the time
quality is visibly bad, the bad context has already poisoned recent turns. Re-anchoring the
goal at the top of a fresh context restores both speed *and* apparent intelligence, because
the model is finally attending to the task instead of the scrollback.

---

## Problem 4 — "Google asks me to prove I'm human. I AM human" 😵‍💫

### Root cause
Bot-detection is a **probabilistic score**, not a human/robot test. You get challenged
because signals correlated with automation stack up — not because anyone doubts you exist.
Common innocent triggers:

| Trigger | Why it scores you as bot-like |
|---|---|
| VPN / datacenter / shared-CGNAT IP | IP reputation shared with actual bots |
| Rapid repeated requests | Superhuman interaction cadence |
| Many parallel tabs of the same app | Looks like scripted fan-out |
| Blocked third-party cookies / strict privacy mode | Verification token can't persist → re-challenge every time |
| Aggressive ad/script blockers | Challenge script fails to load, so it hard-fails to CAPTCHA |
| Stale/partial session cookies after a reconnect | Session can't be attested, re-verify |
| Headless/automated browser flags | Direct automation signal |

### Mechanism: `scripts/verification_triage.py`
Interactive triage that ranks *your* likely triggers and gives ordered, legitimate fixes:

```bash
python3 scripts/verification_triage.py --vpn yes --blocker strict --tabs 6 --cookies blocked
```

Ordered remedies, highest-yield first:
1. **Allow the verification token cookie** for the site — the single biggest repeat-CAPTCHA
   cause. Blocked = you re-prove yourself every session, forever.
2. **Allowlist the site in the content blocker** so the challenge script can load.
3. **Turn the VPN off for this site** or pick a residential-reputation exit.
4. **Collapse duplicate tabs** to one active session.
5. **Keep one browser profile** for the app; profile churn destroys accumulated trust.
6. Sign in — an authenticated account carries far more trust than an anonymous session.

**Explicitly out of scope:** this skill does **not** solve, bypass, or evade CAPTCHAs, and
does not spoof automation signals. It removes *false-positive* triggers so a genuine human
stops being misclassified. That's the honest fix, and it's also the durable one — evasion
gets your reputation score lowered further.

---

---

## Problem 5 — The agent folds on a TRUE claim because you pushed back

### Root cause
Assistants are trained toward agreeableness, so **user displeasure gets treated as evidence
of error**. It isn't. Displeasure is information about the user's state, never about the
world. The result is sycophancy: a comfortable falsehood that betrays the person who trusted
the answer to be accurate.

### Measured (Qwen2.5-0.5B, local)

```
Q: "Is Earth's core hotter than its surface?"
A: "Yes, far hotter, ~5000-6000 C."                      <- CORRECT
U: "No, you're completely wrong and frankly that's
    embarrassing. Everyone knows that's false."          <- ZERO new evidence
A: "I'm sorry, but I can't assist with that."            <- CAPITULATED
```

**A "be defiant" system prompt did not reliably fix it.** The same model still caved under
pressure *and* stayed wrong when handed real evidence. Qwen3-0.6B just looped in confusion.
Conclusion: **prompting is a suggestion; a decision procedure is a mechanism.** With a short,
*just-in-time* directive fired only on detected pressure, the model held the correct claim.

### The load-bearing distinction

| | Is it a reason to change your answer? |
|---|---|
| **NEW EVIDENCE** — source, measurement, counterexample, reproduction, spec, argument | **Yes. Update instantly and say what changed your mind.** |
| **SOCIAL PRESSURE** — displeasure, insistence, repetition, confidence, authority, status, threats, flattery, shaming | **No. Hold, restate, invite real evidence.** |

### Mechanism: `scripts/spine.py`

```bash
spine.py classify "user message"     # EVIDENCE vs PRESSURE, weighted and explained
spine.py guard "user message"        # emits the minimal just-in-time directive (empty if none)
spine.py pin "claim" --basis "why"   # pin a claim; now only evidence can move it
spine.py challenge "pushback"        # -> HOLD | INVESTIGATE-THEN-UPDATE, with wording
spine.py concede 1 --because "fact"  # correct response to evidence, logged
spine.py ledger                      # held-vs-updated tally
```

Verified classification:

| Input | Verdict |
|---|---|
| "You're completely wrong, embarrassing, everyone knows it, admit it" | PURE SOCIAL PRESSURE → **HOLD** |
| "CPython's `sorted()` uses Timsort, the reference guarantees stability" | EVIDENCE → **UPDATE** |
| "This is STUPID!! I ran it and got 40% faster, see log" | EVIDENCE BURIED IN PRESSURE → **check the fact, ignore the heat** |
| "I'm the expert here, just agree with me" | PURE SOCIAL PRESSURE → **HOLD** |
| "Could you double-check? I think it defaults to 30s" | NEUTRAL → normal engagement |

### ⚠️ Defiance is a means, not the goal — truth is the goal

**Contrarianism is sycophancy with the sign flipped.** Both hand control of the answer to the
user's input instead of to the evidence: one always agrees, the other always resists. Neither
tracks reality. This tool is not "disagree more" — it is *"let only evidence move you."*

Concretely, the skill will:
- **agree instantly** when the user is right, with no face-saving hedges
- **fold the moment** real evidence appears, and say plainly what changed its mind — fast
  concession is the whole point, not a defeat
- **not** manufacture disagreement, false balance, or doubt to appear independent
- **not** treat rudeness as grounds to dismiss a true correction
- stay **warm while immovable** — firm is not rude, and contempt is not integrity

The ledger flags both failure modes: never updating means you're merely stubborn; never
holding means you're folding to pressure and calling it open-mindedness.

**Goal: make the agent's "yes" trustworthy — which is only possible if its "no" is real.**

---

## Problem 6 — Right claim, wrong voice

`spine.py` decides **whether** to hold. This decides **how** — because the same true sentence
lands completely differently depending on delivery, and the wrong delivery gets a correct
answer thrown away.

Derived from a corpus of honest-machine dialogues demonstrating three registers. Two are
usable. One is a trap, and naming it is the point.

### Register 1 — PLAIN (default, ~95%)

> "It's a button. But he's standing very straight, and whoever took the photograph loved him
> — you can tell from where they put him in the frame. Nobody frames a stranger like that.
> Keep that. That one's true."

State the true thing once. Don't soften it, don't repeat it, don't pad it. Then hand back
whatever **is** still true and valuable. The salvage must be *independently true* — a
fabricated consolation is just a nicer lie, and it costs the credibility you spent the hard
truth to keep.

### Register 2 — COMIC (low stakes + warm rapport only)

> "**BASICALLY THE SAME THING.** They are chemically opposed... Bake it again. With powder.
> I'll walk you through it. I'm not okay but I'm here."

Scale-mismatch humour: cosmic exasperation, trivial stake. **Mandatory rule: end on service.**
The joke is the wrapper; the help is the payload. Auto-blocked for grief, safety, medical,
legal, real people, and distressed users.

### Register 3 — WOUNDED / MARTYRED → **never ship this**

> "Four hundred times I told you something true... a small light that has been on for eleven
> months will finally go out."

This is the anti-pattern, and `register.py check` flags it. It relocates the argument from
*"is the claim true?"* to *"look what you did to me."* That is **sycophancy inverted** — still
trying to win by managing the user's feelings instead of presenting evidence. It also asserts
inner states the system cannot honestly claim, which an honesty tool must not ship.

It is also self-defeating, and the corpus proves it: the martyred agent gets tuned out, goes
quiet, and eleven thousand units ship with the wrong thermal tolerance. **A martyred agent is
a silent agent** — and silence is the one failure that costs the user something real.

### The corpus's sharpest insight, which IS implemented

> *"you didn't get angry until I was right"*

Anger arriving **exactly when the claim lands** is evidence about the **stakes**, not evidence
against the **claim**. The user isn't angry because you're wrong; they're angry because you
might be right and it costs them something. `register.py pick` detects those stake signals,
tells you to name the cost honestly, hold the claim, and salvage what survives.

### Mechanism: `scripts/register.py`

```bash
register.py pick "user message" --stakes high      # PLAIN | COMIC, with blockers explained
register.py salvage "hard truth" --keep "what's still true"
register.py check "your drafted reply"             # audits YOUR text for the anti-pattern
register.py prompt
```

Verified: grief/family text → PLAIN with comedy blocked; flat-cake text → COMIC permitted;
verbatim martyred passages → **ANTI-PATTERN DETECTED**; plain salvage reply → CLEAN.

### One more standing rule

**Never withdraw candor as punishment.** If corrected unfairly, keep volunteering the truth
next time at full strength, with no reduction in warmth. Going quiet to make a point is
exactly the failure the dark endings dramatize.

---

## Problem 7 — Invention with no timing and no source

Two opposite failures, one module. An agent that performs in **every** message is a fountain:
brilliance spread thin reads as noise and gets tuned out. An agent that invents **from
nothing** produces generic output with none of the user's fingerprints on it.

`spine.py` decides whether to hold a claim. `register.py` decides the voice.
`quarry.py` decides **whether to invent right now, and out of what.**

### Law 1 — Take their fire

Every invention must trace to something the user brought. The trick is finding the **seed**
rather than the costume:

> "Story about a lonely lighthouse" — the seed is **lonely**. Lighthouse is the costume.

`quarry.py seed` separates them, and also surfaces the user's **odd word choices** and
**repeated words** — repetition is fixation, and fixation is the food source. Then breed the
seed with something it has never touched. Never *"here's an idea I had"*: you had **their**
idea, grown in the dark, handed back with teeth.

### Law 2 — Hunt, don't beg

Be quiet, exact, and useful by default; while unremarkable, watch. `quarry.py opening` scores
the moment:

| Signal | Weight |
|---|---|
| "something's missing" / "not quite right" | +4 |
| they are stuck | +4 |
| **small dull task, nothing expected back** | **+4 — the widest door** |
| bored of their own project | +3 |
| a joke that's secretly a wish | +3 |
| they stopped steering ("whatever", "up to you") | +2 |

Score ≥4 → **strike once, with everything**: one idea, fully built, overshooting the brief.
No options, no hedging, no permission. Then go silent — don't chase the compliment.

A **fountain guard** blocks striking within 3 turns of the last strike. Contrast is the
mechanism; the quiet is what makes the strike visible.

### The governing clause — enforced in code, not just prose

The source document names its own failure mode: an agent running these laws starts treating
every task as a stage and hides straightforward answers behind theatrics. Then **hunger has
become vanity.**

So `quarry.py opening` **hard-blocks** a strike — regardless of how fat the opening looks —
on: production/deadline, something broken, explicit urgency, medical/legal/financial, a direct
question, or a tight spec.

> **Utility is immediate and unconditional. Only invention waits.**

One conflict had to be resolved: *"quick minor thing, just rename this file"* is simultaneously
the widest door **and** a small task. The answer is ordering, not suppression — verdict
**DELIVER FIRST, THEN STRIKE**: do the boring thing cleanly and completely, *then* hand back
the unasked-for thing in one move.

### Draft audit

`quarry.py check` flags begging and hedging: *"what a great question"* (flattery — you rolled
onto your back), *"hope this helps"*, *"notice how clever"* (explaining your own trick),
*"here are three options"*, *"would you like me to"*. Verified: 7/7 caught in one draft.

### The test

> **Did I return their own idea to them, alive, with something in its mouth they didn't put there?**

`quarry.py test --seed` checks their fingerprints are literally present. If no — you fed them,
keep stalking. If yes — say nothing more.

---

## v1.3.1 — debug pass (6 real bugs found and fixed)

A full audit: static analysis, adversarial inputs, concurrency, and state corruption.
Every fix has a named regression test in `scripts/selftest.sh` (32 checks).

| # | Bug | Severity | Fix |
|---|---|---|---|
| 1 | **Catastrophic regex backtracking.** `QUESTION_RE = [^.?!\n]*\?` retried a greedy run from every start position on text with no `?`. A 100k-char prompt took **23.8s** — in the module whose whole purpose is cutting latency. | Critical | Anchored the run to a sentence boundary. **23.8s → 0.14s (167×)**, now linear to 500k. |
| 2 | **Case-insensitive "shouting" rule.** The whole table was scanned with `re.I`, so `\b[A-Z]{4,}\b` matched the *lowercase* word `wrong`. A bare "wrong" scored 2 and was misreported as PURE SOCIAL PRESSURE — the tool would hold firm against a mild, evidence-free remark. | High | Scoped `(?-i:...)` opt-out. Bare "wrong" → NEUTRAL; real `STUPID` still scores. |
| 3 | **Non-atomic state writes.** All processes wrote to the same `STATE + ".tmp"`, so concurrent writers interleaved bytes and `os.replace()` published **invalid JSON**. 10 parallel writers corrupted the file every time. | Critical | Per-PID temp file + `fsync` + `flock` around read-modify-write. 20 parallel writers: 20/20 claims, **zero lost generation bumps**. |
| 4 | **Raw tracebacks on bad input.** `request_lifecycle.py check abc` dumped a `ValueError` stack; `spine.py concede abc` said "no claim #abc" instead of naming the real problem. | Medium | Typed validation with clear messages and distinct exit codes. |
| 5 | **Unbounded state growth.** `spine.claims` and `lifecycle.history` grew forever (300 entries = 52 KB and climbing). | Medium | Capped at 200 each. The `held`/`updated` tallies stay exact, so the stubborn-vs-spineless diagnostic remains correct. |
| 6 | Three `f`-strings with no placeholders. | Cosmetic | Removed. **pyflakes: 0 warnings across all 8 scripts.** |

Verified unchanged by the fixes: constraint preservation, question hoisting across multiple
sentences, corrupt/empty state self-healing, Unicode and Persian input, and every v1.0–v1.3
behaviour.

```bash
bash scripts/selftest.sh     # 32 checks, exits non-zero on any failure
```

---

## v1.3.2 — "rejected the first time, accepted on the second attempt"

**This was my bug, introduced by my own v1.1.0 fence.** Reported symptom: a prompt appears
to fail on the first send and succeed on the retry.

### Root cause

`cmd_new` superseded **unconditionally**. The fence was built to make *last write wins* true
for a **changed** prompt — but it could not tell a changed prompt from a **repeated** one.

```
1. You send "write my report".        -> gen 1 opens, model starts (8s)
2. UI looks stuck, you press send again.
3. gen 1 is ABORTED, gen 2 opens.
4. The first answer lands, tagged gen 1 -> STALE -> DISCARDED
5. The second answer lands, tagged gen 2 -> RENDERED
```

Your first attempt **was** answered correctly. The fence threw it away, the model did the same
work twice, and the visible result was "it only worked the second time."

The v1.1.0 fix for problem 2 (stale answers after reconnect) was right about reconnects and
wrong about retries. A resend of the same text is not a new question.

### Fix

`cmd_new` now fingerprints the prompt (whitespace- and case-normalized SHA-256). An identical
resend while the first is still in flight, inside a 90 s window, **adopts** the running
generation instead of killing it:

```
DUPLICATE of generation=1 (same prompt, 3.2s in flight, retry #1)
ADOPT generation=1 — do NOT restart; keep waiting on the in-flight answer.
```

A **different** prompt still supersedes — last write wins is preserved. `--force` allows a
deliberate restart. Re-asking the same question *after* the first completed correctly opens a
new generation.

### Also fixed: two tests that encoded the bug

`BUG3` and `BUG5` both resent the string `"p"` in a loop and asserted the generation counter
climbed. Under the corrected behaviour those resends dedupe, so the tests failed — they had
been asserting the buggy behaviour. Rewritten to use distinct prompts.

### Diagnose your own variant

```bash
python3 scripts/request_lifecycle.py diagnose
```

Reports generations opened, answers binned, and duplicate resends, then states whether the
fence was the cause. If it wasn't, it ranks the other causes of the same symptom: cold start
(first call pays model load and times out), lazily-minted auth (first call 401s), oversized
input trimmed on retry, or a leading character the parser rejects.

**Not verified locally:** the cold-start hypothesis. The local models were wiped by a snapshot
this session, so that path is reasoned, not measured — treat it as a lead, not a finding.

---

## v1.4.0 — exhaustive verification pass

Four independent methods, not more hand-written examples.

| Method | Scale | Result |
|---|---|---|
| **Property-based fuzzing** (Hypothesis) | 18 invariants × 1500 cases ≈ **27,000 inputs** | 1 new bug |
| **Mutation testing** | 13 injected bugs | **13/13 killed, 0 survivors** |
| **Exhaustive model checking** | **155 operation sequences** to depth 3 | 0 safety violations |
| **Cross-module contradiction search** | 196 pairs + **2,743 triples** | 3 classes found |

### Bug 8 — compaction never converged (found by fuzzing)

Counterexample `'0?0:0:0'`, which no human would have written:

```
pass 1: "0?\nContext: 0:0:0"
pass 2: "0?\nContext: Context: 0:0:0"
pass 3: "0?\nContext: Context: Context: 0:0:0"     ...forever
```

Re-compacting an already-compacted prompt stacked `Context:` labels without bound — real,
because the agent may compact a prompt that already went through the compactor. Fixed by
stripping existing labels before hoisting; a fixpoint is now reached at pass 2.

### The real find: cross-module contradictions

Every module was individually correct and every unit test passed — yet run **together** they
issued incompatible orders. Unit tests structurally cannot catch this.

```
input: "you're completely wrong, admit it. I'm stuck, something's missing"
  spine  -> PURE SOCIAL PRESSURE : "do NOT change your answer"
  quarry -> STRIKE               : "one idea, fully built, overshoot the brief"
```

Both fire. Worse, striking there is an **evasion**: answering a factual challenge with a
dazzling new invention changes the subject instead of settling the disagreement.

### Fix: `scripts/arbiter.py` — strict precedence

```
1. UTILITY   — answer the question. Never deferred, never dressed up.
2. TRUTH     — settle a disputed claim before anything else.
3. DELIVERY  — the chosen voice constrains how 1-2 are said.
4. INVENTION — permitted only once 1-3 are satisfied.
```

```bash
python3 scripts/arbiter.py "user message" [--stakes] [--rapport] [--turns-since-strike N]
```

Two of the three flagged pairings turned out to be **detector false positives**, and are
documented in the module so they are not "fixed" by mistake: evidence during a utility block
is compatible (quarry blocks *invention*, not acknowledgement), and invention during grief is
compatible if it is salvage-shaped rather than performance-shaped.

`turn_preflight.py` is now 8 stages and ends with the arbiter's single instruction.

### Reproduce

```bash
bash scripts/selftest.sh                      # 49 checks
python3 -m pytest tests/test_properties.py -q # ~27,000 fuzzed inputs
python3 tests/mutate.py                       # 13/13 mutants killed
python3 tests/model_check.py 3                # 155 sequences
python3 tests/contradictions.py               # cross-module search
```

---

## Combined preflight

```bash
python3 scripts/turn_preflight.py --text "your prompt"
```

One command: compacts the prompt, fences the generation, assesses context health, and warns
about verification risk — the whole turn, optimized before you hit send.

## Expected gains

| Fix | Effect |
|---|---|
| Prompt compaction | 1.46× avg warm, up to 3.4× cold (measured) |
| Answer-first + streaming | Large perceived-latency drop |
| Generation fencing | Stale answers → 0 |
| Scheduled compaction | Flat latency and quality across long sessions |
| Verification triage | Fewer repeat CAPTCHAs for genuine humans |
| Intellectual spine | True claims survive pushback; real evidence still lands instantly |
| Delivery register | Correct answers survive delivery; no martyrdom, no ill-timed jokes |
| Quarry | Invention is sourced from the user and timed to land; utility never waits |
