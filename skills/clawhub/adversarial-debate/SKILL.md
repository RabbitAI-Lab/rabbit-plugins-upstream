---
name: adversarial-debate
description: Cross-vendor adversarial review. Ship a plan, proposal, or design to a model from a DIFFERENT vendor to attack it; the defender rules on every objection; a final round converges on a joint consensus list. Optionally add a fresh-session judge to catch the blind spots both sides share. Invoke only when the user explicitly asks for an adversarial review by a model from another vendor. One model role-playing several experts is not this skill.
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
- **Nature of the output (thin contract)**: the R3 joint consensus is an **unauthorized candidate decision**, not a settled one. It goes back to the main session and needs the user's confirmation before anything lands. This skill writes no decision records, no plans, and no code of its own.

## Meta-request guard

If the argument you were handed is a request to modify, improve, or ask about **this skill itself** (a meta-request), **do not start the debate protocol**. Handle it as an ordinary edit or an ordinary answer — no brief, no attacker, no consensus list.

Learned the hard way: once a meta-request slips into the protocol, the ceremony of it (decision items, consensus lists, proposed decision records) buries what the user actually wanted, and it took two rounds of clarification to get back on track.

## Protocol (three rounds, plus an optional fourth)

1. **Prep the brief.** Write the proposal under review as one self-contained markdown file: background / claims / risks already identified / **what is not up for debate**. Save it to disk. The attacker sees nothing but this file, so the background has to be complete — and the out-of-scope list has to be explicit, or the debate will wander into questions that were already settled.
2. **R1 — Attack.** The attacker reads the brief through the channel picked below and attacks along clear dimensions. Every objection must carry **a concrete failure scenario or a quantified rationale, plus a workable alternative**. Cap the number of objections, force a ranking, and force a final verdict on each (ship / defer / drop). Uncapped attacks decay into list-making.
3. **R2 — Defense and ruling** (written by the main session itself — never outsourced). **Spot-check the files and line numbers the attacker cited before you rule on anything.** Their citations are usually good, but they are not scripture; in practice each side has caught factual errors in the other. Rule on every objection — accept / partially accept / reject — and give reasons when you cut something as over-engineering. Close with a few questions for the attacker to answer in the final round.
4. **R3 — Final round.** The attacker (**necessarily the same model on the same session thread as R1**) reads R1 and R2, expands only on what it still disagrees with, and outputs a **joint consensus list** (ranked by priority) plus **open disagreements**.
5. **R4 — Fresh judge** (optional; reserve it for consequential proposals). Open a **brand-new session** with a judge persona. The consensus is presumed valid; the judge hunts only three things: new problems the consensus itself introduces, mistaken premises both sides share, and mechanisms that will rot under long-term operation. Adversarial stance and fresh perspective are two orthogonal checks — neither substitutes for the other.

## Core stances

- The attacker's sharpest weapon is **demanding evidence that some past failure is attributable to the missing thing**. Put that sentence in the attacker's prompt verbatim. Most over-engineering dies right there.
- The defender should concede cleanly. The moment your own data contradicts your own motivation, stop arguing — don't perform the remaining rounds for form's sake.
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

**Anti-pattern**: never queue the attacker's task into a live thread that is already running a different protocol. The contexts contaminate each other, you lose control of when output arrives, and when both share the same credentials you find out far too late that the other end died. Observed in practice: a `codex exec` call and the live thread it was queued behind died on the same expired token, and that R1 was never coming back.

**The cross-vendor constraint survives every fallback**: the defender is whichever model you are working in, and all three attacker rungs come from other vendors — dropping to any rung preserves the adversarial value. For the R4 fresh judge, prefer **a vendor different from this debate's attacker**: adversarial stance × fresh perspective × vendor diversity, three orthogonal axes.
