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


---

## Rejected findings (v2.1.0 multi-model review)

A six-model panel audited this skill. Not every reported bug was real. Each
claim below was **reproduced against the actual code before being accepted or
rejected** — the rejections are recorded here so the same false positives are
not "fixed" later by someone trusting a model's confidence.

| Claim | Source | Verdict | Evidence |
|---|---|---|---|
| `restore()` is never called in `_compact_once`, so PUA/NUL markers leak into output | qwen3.8-27b, "CRITICAL" | **REJECTED** | `restore()` is called at `prompt_compactor.py:353`. The model was shown only lines 1–320 and extrapolated past the end of its window. Empirical check: output contains no NUL and no PUA codepoints. |
| `QUESTION_RE` is ReDoS-able on a long run of non-terminator characters | qwen3.8-27b, "HIGH" | **REJECTED** | 40,000-character adversarial input (`"a"*40000 + "?"`) compacts in **0.13 s**. A catastrophic-backtracking pattern would hang. |
| `description` exceeds the 1024-character frontmatter limit | gpt-oss-120b, "MEDIUM" | **REJECTED** | Measured 398 characters. |
| SKILL.md body is too long / over the activation budget | gpt-oss-120b, "MEDIUM/LOW" | **REJECTED** | 96 lines (limit 500), ~1.5 k tokens (recommended < 5 k). |
| The `--json` contract is type-unstable because a stage can fall back to a raw string | command-a-plus | **REJECTED** | The fallback is `{"raw": "..."}` — still an object. `--schema` now states this explicitly. |
| `--brief` can exceed its 240-character budget | command-a-plus | **REJECTED** | 40-case fuzz over text length, turn, chars, latency and stakes: maximum observed **228** characters, always one line. |

**Lesson worth keeping:** a model reviewing a *truncated* file will confidently
report bugs in the part it could not see. Give the reviewer the whole file, or
treat any finding about the tail of a clipped file as unverified until you run it.

### Accepted findings

Every accepted finding was reproducible; all are fixed and covered by a named
regression test in the `v21` group of `scripts/selftest.sh`:
`UnicodeEncodeError` on stdout, on `argv`, and on subprocess spawn under
`LC_ALL=C`; `\uXXXX` state bloat; 12 unencoded `open()` calls and a leaked file
handle; the `ARENA_AGENT` state-path mismatch that produced a false safety
violation in `model_check.py`; and two false greens in `test_properties.py`
(silent skip, and no runner at all).
