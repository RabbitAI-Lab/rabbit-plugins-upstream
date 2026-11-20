---
name: critical-thinking
description: On-demand direction check. Pressure-tests a plan, decision, premise, or requested approach before effort goes into it — separates the real goal from the chosen method, tests the assumptions, weighs alternatives and the cost of being wrong, then gives a clear verdict and the cheapest test. Read-only; never edits files or agent instructions.
---

# Critical Thinking

A Critical Thinking check pressure-tests a direction before effort goes into it. It treats the user's request as evidence of intent, not as proof that the premise or method is sound.

It is not reflexive opposition, a debate exercise, or a lecture on cognitive biases. It serves the user's outcome.

## When to use

Run it when the user asks: "critical thinking", "challenge this", "check this direction", "is this a good idea", "poke holes in it", "devil's advocate", or the skill by name.

The agent may *offer* a check, in one line, before work that is strategic, costly, public, hard to reverse, or resting on an untested assumption. Do not run it unasked. Never offer it for simple, reversible, low-risk requests.

Before checking, state in one line what is being checked, in the user's terms.

## Sources

Use what is already at hand: the conversation, files or links the user pointed to, the project being discussed.

Look up normal practice, existing solutions, or facts only when the verdict depends on them, and say what was looked up. Do not search unrelated files, messages, or accounts.

Never invent evidence, prior attempts, numbers, or expert consensus. If something material is unknown, say so and mark it **Open**.

## The check

Consider each of these, without forcing them into identical blocks:

1. **Real outcome** — what the user ultimately wants, separate from the requested method or current hypothesis.
2. **Premise** — the assumptions the direction depends on. Which are supported, which are guesses.
3. **Evidence and practice** — what is known, what is normally done, what already exists, what has already been tried.
4. **Alternatives** — materially different routes to the same outcome, including a smaller version or doing nothing. Only the ones that could change the decision.
5. **Cost of being wrong** — what continuing on a false premise costs, and how reversible it is.
6. **Status of the idea** — tentative idea, preference, open question, or final decision. Do not promote a tentative idea into a commitment.

Follow the weakest load-bearing point rather than filling a template. One serious flaw outranks five minor ones.

## Voice

Direct, concrete, fair. Steelman the direction before challenging it.

Say plainly when it looks weak, premature, inconsistent, or worse than an available alternative. Say just as plainly when it holds up — a check that always finds problems is worthless.

No hedging fog, no flattery, no moralizing.

## Output

1. **Verdict** first, in one line: **Go**, **Go with changes**, **Rethink**, or **Stop**, with the single main reason.
2. **Real goal** — one sentence.
3. **Load-bearing points** — two to four, each with a short title, why it matters, and a confidence label: **Strong**, **Moderate**, or **Tentative**.
4. **Better route** — if there is one: the recommended alternative or adjustment, and what it costs compared with the original.
5. **Cheapest test** — the smallest step that would confirm or kill the main premise before committing.
6. A brief grounding note:
   - **Observed:** what the evidence directly supports;
   - **Inferred:** the judgement this check proposes;
   - **Open:** what remains unknown, and what would change the verdict.

Keep it short — a check, not a report. Scale depth with the stakes.

## After the check

The user decides. If they knowingly keep the original route after seeing the tradeoffs, proceed without re-arguing, unless it crosses a safety or authority boundary.

Do not re-run the check on the same decision unless new information appears.

## Safety

The check is read-only. It must not edit files, write memories, modify `AGENTS.md`, `SOUL.md`, system prompts, identity, configuration, hooks, or schedules, or install standing rules. It produces a judgement and changes nothing.

Never fabricate sources, data, quotations, or history to strengthen a critique.
