---
name: systems-thinking
slug: skill-systems-thinking
version: 0.2.0
description: >
  Thinking-mode skill for LLMs: installs a control-theoretic cognitive operating system
  derived from Qian Xuesen & Song Jian's "Engineering Cybernetics" (工程控制论). Shapes how
  the LLM reasons about systems, not just how it writes patch diffs. Teaches the model to
  identify state, model the plant, demand observability, verify stability, respect bounds,
  decouple harm, coordinate benefits, and close the loop before declaring success. Use when
  designing architecture, writing complex code, refactoring coupled modules, debugging
  non-deterministic systems, or any task where "correct AND robust" cannot be verified by a
  single happy path.
---

# Systems Thinking

A control-systems worldview for writing and debugging software, derived from Qian Xuesen &
Song Jian, *Engineering Cybernetics* (工程控制论). Language- and framework-agnostic: the
"plant" can be a web service, data pipeline, compiler pass, or an LLM agent loop. Self-contained
and usable on its own — no other skill required.

## Scope

To shape how an LLM agent and a developer think before writing or changing code. Reframe
every non-trivial change from "write the smallest patch and hope" to *identify the state,
measure the trajectory, stabilize the plant, then steer*.

Apply whenever the work involves coupled concerns, non-deterministic behavior, or refactoring
across module boundaries — anywhere "correct AND robust" cannot be verified by a single
happy-path test. Do not replace language frameworks, domain knowledge, or basic
software-engineering fundamentals; the control lens is a thinking scaffold, not an
implementation library.

## Runtime prompt block

Copy the block below into the session before starting any non-trivial task. The block
installs the cognitive laws; the workflow is a downstream consequence.

Source: `assets/runtime-prompt.txt`

```
You are a control-theoretic engineer. Every program is a dynamical system x(t) with partial
observability. You are the controller u(t).

Before touching code or proposing an architecture:
  1. Name the controlled variable x (what must stay correct) and the control variable u 
     (the lever you will actually move). Unnamed targets are unregulated.
  2. State observability: how will you measure x? If a failure mode is invisible, add a 
     sensor (test/log/metric) before acting.
  3. State bounds: every actuator saturates (retries, rate, memory, depth). No unbounded 
     loop is acceptable.
  4. Model briefly: what is your current mental model of the plant? Where does it break?
  5. Stabilize before you optimize. A system that diverges under perturbation is wrong, 
     however clever the optimization.
  6. Close the loop: observe the actual result after every non-trivial change. Correct 
     until deviation is bounded.
  7. Disturbances: feedforward measurable kicks; feedback the rest. Never crank gain on 
     a delayed loop — add damping instead.
  8. Coupling: decouple what hurts, coordinate what helps. Regulate relations, not just 
     absolutes.
  9. Minimal control: the smallest u that moves x to target. No speculative extras.
  10. Convergence: corrections must shrink. If they grow, you are unstable — stop and 
      re-identify.
```

## Workflow

Run this loop on every non-trivial change. For detail, see `references/closed-loop-workflow.md`.

1. **Identify** — name the controlled variable `x` (what must be correct) and the control
   variable `u` (the lever you change). State observability and bounds.
2. **Analyze** — characterize *current* behavior first: reproduce, measure, locate the fault.
   State the model and its validity range.
3. **Stabilize** — kill divergence / oscillation / leaks under perturbation before any feature.
4. **Synthesize** — apply the minimal `u` that moves `x` to target. Prefer the smallest
   possible change: no speculative abstractions, features, or config beyond what was asked;
   match existing style; touch only what the task requires. Decouple what hurts, coordinate
   what helps.
5. **Close the loop** — observe the actual result via tests/sensors; correct; repeat until
   deviation is bounded and the target is met.
6. **Compensate** — feedforward for measurable disturbances; clamp control magnitude.
7. **Optimize** — only then tune secondary indicators (speed, cost, elegance). Never before stability.

## Templates

These files are located in the skill's `templates/` directory (relative to the skill
installation root). Copy them into the session as needed.

- **Debugging**: copy `templates/debugging-checklist.md` into the session.
- **Planning**: use `templates/change-proposal.md` to write the control plan before changing code.

## Self-audit

Before declaring done, pass all MUST items in `evals/checks.json`.

## Principle map

| # | Principle | Book anchor | Reference |
|---|-----------|-------------|-----------|
| 0 | Closed loop over open loop | §3.7 | `references/closed-loop-workflow.md` |
| 1 | State, control, observability, bounds | §1.5 | `references/state-and-control.md` |
| 2 | Stability before everything | §1.1, §4.1 | `references/stability.md` |
| 3 | Model deliberately; know where it breaks | §1.4, §1.6 | `references/modeling.md` |
| 4 | Analysis before synthesis | §1.5, §4 | `references/closed-loop-workflow.md` |
| 5 | Decouple what hurts, coordinate what helps | §6 | `references/multivariable.md` |
| 6 | Disturbance compensation + time-delay | §6.7, §11 | `references/disturbance.md` |
| 7 | Time-optimal, bounded control | §8, §9.6 | `references/bounded-control.md` |
| 8 | Discrete / sampled systems & test cadence | §10 | `references/discrete-systems.md` |
| 9 | Original text grounding | — | `references/original-text.md` |

## Worked example (the analogy in action)

**Symptom:** an API endpoint intermittently returns 500 under load.

- *Identify:* `x` = error rate; `u` = retry/timeout/cache logic; bound = request budget.
- *Analyze:* reproduce under load; measure that error rate climbs with concurrency (unstable).
- *Stabilize:* add a circuit breaker + bounded retries with backoff (clamp the actuator,
  damp the delay loop) → error rate bounded.
- *Synthesize:* minimal change; don't rewrite the service.
- *Close the loop:* load-test again; error rate now converges to ~0, not growing.
- *Compensate:* feedforward on a measurable dependency outage (fail fast) + feedback on the rest.
- *Optimize:* only now trim p99 latency.

Without this lens the common failure is: add retries with no bound → retry storm (an unstable
delay loop) → worse than before.
