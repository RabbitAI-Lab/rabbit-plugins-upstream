---
name: adversarial-debate
description: Cross-vendor adversarial review. Ship a plan, proposal, or design to a model from a DIFFERENT vendor to attack it; every objection carries a verifiable anchor; the defender rules with an evidence tag on each ruling; the final round classifies into still-disputed / unresolved / verified-consensus instead of forcing agreement; a fresh-session judge is mandatory whenever the outcome looks too clean. Invoke only when the user explicitly asks for an adversarial review by a model from another vendor. One model role-playing several experts is not this skill.
---

# adversarial-debate — Cross-Vendor Adversarial Review

## What this skill sends where

Worth knowing before you run a debate: **the brief you write in step 1 is sent verbatim to a model hosted by another vendor.** That is the whole mechanism — there is no way to get cross-vendor adversarial value without it.

- The brief goes to whichever channel you selected (OpenAI through the Codex CLI, xAI through the Cursor CLI, or whichever backend you configured for handoff). Write it accordingly: it should carry the argument, not your secrets.
- Nothing else leaves your machine. This skill reads the brief you wrote and the attacker's replies. It does not scan your repository, collect telemetry, or send anything to a destination you did not configure.
- Every channel runs its own CLI under your existing credentials for that vendor. This skill never handles, stores, or forwards a key.

## Scope and boundaries

- **One model playing several roles** (a simulated expert panel, self-refereed red-teaming) → not this skill. It is one set of weights talking to itself, and agreement comes far too cheaply.
- **A genuinely foreign adversary** (a model from another vendor, with different training biases) → this skill. That is where the value comes from: the attacker walks in carrying a different set of priors, so it can puncture the proposer's self-consensus.
- Its relationship to an internal panel is **an orthogonal review stage, not a sub-mode of one**. A panel's output can be brought here for external red-teaming, but a panel must never escalate into this skill on its own. Start only when the user explicitly asks.
- **Nature of the output (thin contract)**: the verified-consensus items from the final round are an **unauthorized candidate decision**, not a settled one. Landing them anywhere durable — a decision log, a project plan, a ticket, whatever your own system uses for that — needs the user's explicit confirmation. This skill writes no decision records, no plans, and no code of its own; see step 6 for what closing a debate actually requires.

## Meta-request guard

If the argument you were handed is a request to modify, improve, or ask about **this skill itself** (a meta-request), **do not start the debate protocol**. Handle it as an ordinary edit or an ordinary answer — no brief, no attacker, no consensus list.

Learned the hard way: once a meta-request slips into the protocol, the ceremony of it (decision items, consensus lists, proposed decision records) buries what the user actually wanted, and it took two rounds of clarification to get back on track.

## Protocol (three rounds, a trigger-mandatory fourth, and a closing handoff)

1. **Prep the brief.** Write the proposal under review as one self-contained markdown file: background / claims / risks already identified / **what is not up for debate**. Save it to disk. **Attach a list of the actual source file paths, not just a summary written for the defender** — an attacker that only reads a summary can only nitpick within the proposer's own framing. The one debate where the attacker went and read the real source documents instead of a summary was the only one where errors got caught in both directions.
2. **R1 — Attack.** The attacker reads the brief through the channel picked below and attacks along clear dimensions. Every objection must carry **a concrete failure scenario or a quantified rationale, plus a workable alternative**. Cap the number of objections, force a ranking, and force a final verdict on each (ship / defer / drop). Uncapped attacks decay into list-making. Two hard requirements:
   - **Every objection needs a verifiable anchor** — a file:line, a runnable command, or citable data. An objection that can't produce one gets self-labeled `[speculative]`; the defender has no obligation to accept it.
   - **The attacker must answer, at the end: "if the verdict is don't-do-this, what's the failure scenario for not doing it?"** Without this question, nobody in the room argues for action, and every consensus drifts toward the conservative side by construction.
3. **R2 — Defense and ruling** (written by the main session itself — never outsourced). **Spot-check the files and line numbers the attacker cited before you rule on anything.** Their citations are usually good, but they are not scripture; in practice each side has caught factual errors in the other. Rule on every objection — accept / partially accept / reject — and give reasons when you cut something as over-engineering. Close with a few questions for the attacker to answer in the final round. **Every ruling needs an evidence tag:**
   - `[verified]` — you ran the command or read the line, and you name which one. Only these are eligible for the consensus list.
   - `[reasoned]` — argument only, nothing checked. **Does not enter the consensus list** — it goes into a separate "still to verify" list instead.
   - `[to-verify]` — should have been checked this round but wasn't. Say what needs to run next time.

   The defender also has to price **the cost of not acting** — the mirror of the attacker's closing question above.
4. **R3 — Final round.** The attacker (**necessarily the same model on the same session thread as R1**) reads R1 and R2, and expands only on what it still disagrees with. Output **three categories, not a consensus list**: ① still disputed, ② neither side can produce evidence for (parked as unresolved — **must not be merged into consensus**), ③ verified consensus (every item carries its R2 `[verified]` anchor). **Failing to converge is not a failure of the process** — don't force agreement just to close cleanly.
5. **R4 — Fresh judge** (**mandatory whenever triggered**, no longer optional). Dispatch it the moment any trigger fires: the consensus contains a prohibition / gate / "don't do this"; or R2 recorded zero rejections across the whole session; or the consensus list has 5+ items. Open a **brand-new session** with a judge persona. The consensus is presumed valid; the judge hunts only three things: new problems the consensus itself introduces, mistaken premises both sides share, and mechanisms that will rot under long-term operation. Adversarial stance and fresh perspective are two orthogonal checks — **the more unanimous a session looks, the more it needs this; unanimity itself is a trigger.** One debate that produced zero rejections had its fresh judge surface six blind spots — four of them a shared mistaken premise, one of which broke the consensus's own internal consistency: both sides had used the identical argument to kill one metric, then left the same flaw standing on a second metric and called it legitimate.
6. **Closing handoff.** Once R3 (and R4, if triggered) has landed, someone has to decide what happens to the verified-consensus items — otherwise they evaporate. When this debate is reviewing another process's output (a panel discussion, a design review), that process's own closing step picks the consensus back up. **When run standalone, there is no outer process waiting to catch it** — a three-category report is not an endpoint. The session should propose, item by item, where each verified-consensus entry should land (a decision log, a plan, a ticket, or simply "noted, no action"), and wait for explicit confirmation before writing anything down. An item nobody confirmed gets flagged **"unresolved — not recorded,"** never silently dropped. Parked and still-disputed items are never routed anywhere — they stay exactly as open questions for the user.

## Core stances

- The attacker's sharpest weapon is **demanding evidence that some past failure is attributable to the missing thing**. Put that sentence in the attacker's prompt verbatim. Most over-engineering dies right there.
- **Don't mistake "the defender accepted everything" for evidence the debate worked — it is this protocol's strongest systematic bias.** Across an archived sample of debates (roughly a dozen sessions, ~84 objections total), only about 1 in 40 objections was actually rejected in a way that changed the ruling — and every one of those rejections came from the defender running real production data. Pure conceptual back-and-forth produced zero rejections. Multiple sessions closed with "still disputed: none," and the attacker sometimes withdrew its own R1 point along the way. Capitulation doesn't happen through flattery — it happens because conceding reads as a virtue.
- **The easiest consensus for both sides to reach is "don't do it / defer it / add a gate"** — because neither side has to stand behind an action. When a consensus list is almost entirely prohibitions, suspect convergence pressure before you suspect it found the truth.
- The defender should concede cleanly. The moment your own data contradicts your own motivation, stop arguing — don't perform the remaining rounds for form's sake. But **a concession needs its `[verified]` tag too** — a concession with no anchor is capitulation, not a real concession.
- The attacker's own objections can contradict each other (a classic pair: "add cross-links" alongside "wait for evidence before touching it"). **Name the contradiction** and force the final round to resolve it, instead of writing both down as findings.
- Consensus gets written up; disagreements are handed to the user exactly as they stand. Neither the attacker nor the judge decides anything on the user's behalf.

## Attacker channel ladder (chosen once per debate; never switch vendors mid-debate)

Picking a channel is a **once-per-debate** decision, not a per-call one: R1 and R3 must run on the same model and the same session thread, because convergence in the final round depends on the attacker's continuity. Open with a one-word-answer health probe and take the first channel that responds.

The three channels below are references, ordered by availability. **Use whatever is actually installed on your machine** — the point of a ladder is having a fallback when the primary dies, not these three vendors specifically.

**P1 — Codex CLI (OpenAI)**

```bash
codex exec --skip-git-repo-check --sandbox read-only -C <brief-dir> "<prompt>" < /dev/null > rN.md 2>&1
```

Run it in the background. The response body follows the **last** `codex` marker block in the output, and `tokens used` marks the end. Continue the thread with `codex exec ... resume --last -` — **flags must come before `resume`**, or they get parsed as arguments to it. Known killer: `401 token_expired` is unrecoverable in a headless environment (the OAuth flow needs a browser). Tell the user to run `codex login` and drop to the next channel immediately.

**P2 — Cursor CLI (can drive Grok and others)**

```bash
cursor-agent -p --output-format stream-json --mode plan --model cursor-grok-4.6-xhigh "<prompt>"
```

The prompt **must** state: "**do not call CreatePlan — emit the full text as your final message**." Under plan mode with `-p`, CreatePlan swallows the entire output and you get a silent empty return. Read the `result` event out of the stream-json, and fall back to `createPlanToolCall.args.plan`. Plan mode is read-only, which fits the attacker role naturally. Continue the thread with `--resume <chatId>`.

**P3 — DeepSeek (or any configured backend) via the handoff CLI**

`handoff` is a public dispatcher (install it with your Python tool manager — pin the version your policy requires — then `handoff init` and declare your backends in `~/.handoff/config.yaml`). It meets both requirements this skill puts on a channel — it reads a file, and it can resume the same conversation — so R1 and R3 stay on one thread.

```bash
handoff new --backend deepseek --slug <slug> --write < brief.md      # prints the .prompt.md path
handoff run --backend deepseek ~/.handoff/tasks/<RUN_ID>.prompt.md   # run in background
# R3, continuing the same conversation:
handoff resume <RUN_ID> - <<'EOF'
<R3 prompt: read R1 and R2, expand only on what you still disagree with>
EOF
```

RUN_ID is the basename of the path `handoff new` printed (e.g. `0828-ds-04-debate-r1`). The answer lands at `~/.handoff/tasks/<RUN_ID>.result.md`, with raw output alongside it in `.out.txt`. **Poll by RUN_ID, never by recency** — a second attempt under the same slug leaves the older result files sitting right next to the new ones. `handoff tail` follows a run that is still going.

Any other vendor's CLI that can read a file and resume a session works here just as well. If you only have two vendors, run a two-rung ladder rather than wiring up a third channel you have not verified.

**Passing the prompt on the command line**: an attacker or final-round prompt will almost always contain code markers (backticks, `fn()`). Embed one directly inside a double-quoted shell argument and the shell treats it as command substitution — the whole command fails to parse and produces an empty file. **Always write the prompt to a file first (a quoted heredoc), then pass it with `"$(cat file)"`.**

**Anti-pattern**: never queue the attacker's task into a live thread that is already running a different protocol. The contexts contaminate each other, you lose control of when output arrives, and when both share the same credentials you find out far too late that the other end died. Observed in practice: a `codex exec` call and the live thread it was queued behind died on the same expired token, and that R1 was never coming back.

**The cross-vendor constraint survives every fallback**: the defender is whichever model you are working in, and all three attacker rungs come from other vendors — dropping to any rung preserves the adversarial value. For the R4 fresh judge, prefer **a vendor different from this debate's attacker**: adversarial stance × fresh perspective × vendor diversity, three orthogonal axes.
