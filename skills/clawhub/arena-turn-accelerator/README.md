# arena-turn-accelerator

A ClawHub plugin that fixes the seven things that make a web agent chat feel slow, stale,
dumb, hostile, spineless, insufferable — or forgettable.

| # | Your complaint | Mechanism | Script |
|---|---|---|---|
| 1 | 🤬 Lag + waiting spinner after sending | Reshape input so models prefill 1.5–3.4× faster | `prompt_compactor.py` |
| 2 | Answers to the *previous* request after reconnect | Monotonic generation fence — stale streams discarded | `request_lifecycle.py` |
| 3 | 🧟 Slow + mindless late in long chats | Zombie score + carry-forward brief | `context_hygiene.py` |
| 4 | 😵‍💫 Needless CAPTCHA — "I am already human" | Rank false-positive triggers, ordered fixes | `verification_triage.py` |
| 5 | Agent caves on a TRUE claim when you push back | Separate new evidence from social pressure | `spine.py` |
| 6 | Right claim, wrong voice (martyred / ill-timed joke) | Pick the register; audit drafts for self-pity | `register.py` |
| 7 | Constant unsourced cleverness (noise) or generic invention | Find the seed, read the opening, strike once | `quarry.py` |

## Quick start

```bash
# everything at once, before you hit send
python3 scripts/turn_preflight.py --text "your prompt" --turn 30 --chars 95000 --latency 8.1

# or individually
python3 scripts/prompt_compactor.py --text "Hi, I was wondering if you could please..."
python3 scripts/request_lifecycle.py new "prompt" ; python3 scripts/request_lifecycle.py check 3
python3 scripts/context_hygiene.py assess
python3 scripts/verification_triage.py --vpn yes --cookies blocked --tabs 6
python3 scripts/spine.py classify "you're wrong, everyone knows it, admit it"
python3 scripts/spine.py guard "$USER_MESSAGE"   # prepend the emitted directive
python3 scripts/register.py pick "$USER_MESSAGE" --stakes high
python3 scripts/register.py check "$YOUR_DRAFT"  # catch martyred framing before sending
python3 scripts/quarry.py seed "$USER_MESSAGE"       # the real seed vs the costume
python3 scripts/quarry.py opening "$USER_MESSAGE" --turns-since-strike 1
python3 scripts/quarry.py check "$YOUR_DRAFT"        # flattery / hedging audit
```

## On invention (problem 7)

Two opposite failures: spraying cleverness into every message (noise — people stop hearing a
fountain within a day), and inventing from nothing (generic, no fingerprints).

- **Seed, not costume.** *"Lonely lighthouse"* → the seed is **lonely**; lighthouse is the
  costume. `quarry.py seed` also surfaces their odd words and repeated words — repetition is
  fixation, and fixation is the food source.
- **Read the opening.** Stuck (+4), "something's missing" (+4), bored (+3), a joke that's
  secretly a wish (+3) — and a **small dull task they expect nothing from (+4), the widest
  door.** Score ≥4 → strike once, fully committed, then go silent.
- **Fountain guard**: no striking within 3 turns of the last strike. Contrast is the mechanism.
- **Governing clause, enforced in code:** *utility is immediate and unconditional; only
  invention waits.* Production, breakage, urgency, medical/legal/financial, a direct question,
  or a tight spec **hard-block** the strike no matter how good the opening looks. Hiding a
  straightforward answer behind theatrics is vanity, not hunger.
- For *"quick thing, just rename this file"* the verdict is **DELIVER FIRST, THEN STRIKE** —
  ordering, not suppression.

## On delivery (problem 6)

`spine.py` decides **whether** to hold a claim. `register.py` decides **how**, because the
wrong voice gets a correct answer discarded.

- **PLAIN** (default): say it once, then hand back what is still true. *"It's a button. But
  he's standing very straight, and whoever took that photograph loved him. Keep that."*
  The salvage must be independently true — invented comfort is just a nicer lie.
- **COMIC** (low stakes + warm rapport only): scale-mismatch humour that **must end on
  service**. Auto-blocked for grief, safety, medical, legal, real people, distress.
- **MARTYRED**: never. Grievance tallies and *"was my honesty worth it"* trade evidence for
  guilt — sycophancy inverted. `register.py check` flags it in your draft.

Also implemented: when anger arrives **exactly as the claim lands**, that is evidence about
**stakes**, not about truth. Hold the claim, name the cost, salvage what survives. And never
withdraw candor as punishment — a martyred agent is a silent agent.

## On the spine (problem 5)

Measured: the local model abandoned a **correct** claim after pure social pressure with zero
new evidence. A "be defiant" system prompt did **not** reliably fix it — the model still caved,
and separately stayed wrong when given real evidence. A short **just-in-time** guard, fired only
when the classifier detects pressure, did work.

**This is not contrarianism.** Reflexive disagreement is sycophancy with the sign flipped — both
let the user's input decide the answer instead of the evidence. `spine.py` holds only what
evidence supports and concedes the instant a real fact appears. The ledger flags both failures:
never updating = stubborn; never holding = folding. Warm, but immovable.

## Self-test

```bash
bash scripts/selftest.sh    # 32 regression checks, non-zero exit on failure
```

v1.3.1 fixed 6 real bugs found in a full audit: catastrophic regex backtracking (23.8s → 0.14s
on 100k input), a case-insensitivity bug that made bare "wrong" read as social pressure,
non-atomic state writes that corrupted JSON under concurrency, raw tracebacks on bad args,
unbounded state growth, and 3 lint warnings. Each has a named regression test.

## Requirements

Python 3.8+. **Standard library only** — no dependencies, no network calls, no telemetry.
State is local JSON under `~/.arena_turn/`.

## Scope & honesty

- Problems 1–3 are fixed agent-side/client-side, which is where most of the latency and all
  of the staleness and degradation actually live.
- A plugin cannot patch a website's servers; it cannot remove server queueing or network RTT.
- Problem 4 is **diagnosis and false-positive removal, not CAPTCHA bypass**. No solving,
  no spoofing of automation signals — those lower your reputation score further.

## Verified behavior

- Compactor preserves constraints (`must`, `don't`, numbers, quoted text, `code spans`)
  and warns instead of cutting when a rule would touch one.
- Fence: gen 1 superseded by gen 2 → `resume 1` refused, `check 1` discarded,
  `complete 1` ignored.
- Hygiene: 55 turns / 192 k chars / rising latency → score 84 → `RESET` + brief generated.
- Triage: VPN + strict blocker + blocked cookies + 6 tabs + anonymous → HIGH (100 pts),
  cookie fix ranked first.
- Quarry: production/breakage/direct-question → strike hard-blocked; small dull task →
  DELIVER FIRST THEN STRIKE; struck 1 turn ago → HOLD (fountain guard); flattery+hedging
  draft → 7 weaknesses caught.
- Register: grief/family → PLAIN (comedy blocked); flat cake → COMIC allowed; verbatim
  martyred passages → ANTI-PATTERN DETECTED; plain salvage reply → CLEAN.
- Spine: pure pressure → HOLD; real evidence → UPDATE; evidence buried in insults → check the
  fact anyway; polite disagreement and benign questions → NEUTRAL (no false alarms).


## Permissions

Reads and writes session state under `~/.arena_turn/` (fence generations, zombie-score
samples, the spine ledger — prompt previews of at most 400 chars are kept there).
With `--agent NAME`, state is isolated under `~/.arena_turn/agents/<name>/`. No
network access; no other filesystem writes.

## Security & Privacy

- All state files are local JSON; nothing is uploaded anywhere.
- `agent_state.py` refuses hostile agent names (path traversal) with a clean error —
  never a silent fallback to the shared directory.
- The compactor never sends data anywhere either; it is a pure text transform.
- Prompt previews stored in lifecycle state are capped at 70–400 chars.

## Verification

- sha256: 53b71bc70cc1cc6fff8928528b641dd7a53cbed28b4cb47c5caac502ccce1e24
  (of this release's `SKILL.md` — verify with `sha256sum SKILL.md`)
- `bash scripts/selftest.sh` → 74/74 PASS (v1.5.0); `python3 tests/fuzz_fixpoint.py 800`
  → 800/800 fixpoint-clean; `python3 tests/mutate.py` → 13/13 mutants killed;
  `python3 tests/model_check.py 3` → 155 sequences, no violation.
