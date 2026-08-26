<p align="center">
  <img src="assets/judgment-loop-hero.png" alt="Judgment Loop — evidence, counterevidence, verification, action" width="100%">
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> · <strong>English</strong>
</p>

<h1 align="center">Judgment Loop</h1>

<p align="center"><strong>The missing step between thinking and acting.</strong></p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT-0" src="https://img.shields.io/badge/license-MIT--0-F2C94C.svg"></a>
  <a href="https://skills.sh/sirsws/judgment-loop"><img alt="skills.sh installs" src="https://skills.sh/b/sirsws/judgment-loop"></a>
  <img alt="Version 1.0.1" src="https://img.shields.io/badge/version-1.0.1-2563EB.svg">
</p>

Judgment Loop is an open Agent Skill for consequential choices, uncertain claims, recurring failures, serious learning, and evidence-based review. It turns vague confidence into a provisional judgment, a cheap falsification test, and an action the user still owns.

It is not a prompt that makes an AI sound deeper. It is a guardrail against answering the wrong question beautifully.

## Why it exists

AI can produce a coherent answer before a person has identified the real target. That creates four common failures:

- proxy metrics improve while reality does not;
- an attractive plan becomes part of the user's identity;
- elegant explanations outrun evidence;
- the AI completes the cognitive work, leaving no user-owned judgment or action.

Judgment Loop interrupts that pattern without turning every task into a ceremony.

## Five modes

| Mode | Use it for | Core move |
|---|---|---|
| **Quick** | A vague problem or solution attachment | Real target → strongest failure → cheapest action |
| **Decision** | Costly or hard-to-reverse choices | Downside, reversibility, convexity, exploration budget |
| **Research** | Papers, reports, data and causal claims | Mechanism, increment, evidence, boundary, falsification |
| **Learning** | Understanding that must transfer | Reconstruct, counterexample, transfer, no-AI recall |
| **Review** | Work that has produced real results | Prediction gap, evidence update, keep/remove, next cycle |

## Install

### skills.sh / universal skills CLI

```bash
npx skills add sirsws/judgment-loop
```

Install only this skill for Codex:

```bash
npx skills add sirsws/judgment-loop --skill judgment-loop -g -a codex -y
```

### ClawHub / OpenClaw

```bash
clawhub install judgment-loop
```

### Manual

Copy the repository folder into your agent's skill directory. For Codex, the global location is `~/.codex/skills/judgment-loop/`.

## Use

Explicit invocation:

```text
$judgment-loop Should I publish this now, or keep improving it?
```

The skill also supports implicit activation when meaningful consequences and uncertainty coexist. It deliberately stays out of simple facts, clear execution, low-risk reversible tasks, freeform creation, and emotional companionship alone.

## What a good run produces

```text
Provisional judgment
    ↓
Real target vs. proxy
    ↓
Verified facts / inferences / hypotheses
    ↓
Strongest failure reason
    ↓
Cheapest falsification
    ↓
User-owned action and stopping condition
```

The loop is intentionally open: action closes; belief remains updateable.

## Examples

- “This paper reports a strong result. Should we integrate the method?”
- “I keep switching projects. Is exploration still helping me?”
- “We shipped the feature. Did it improve the real target?”
- “I understood the explanation. Can I reconstruct and transfer it without AI?”

See [examples](examples/README.md) for before/after cases and [trigger evals](evals/trigger-cases.md) for the routing contract.

## Design principles

1. **User sovereignty** — the model does not make value choices for the user.
2. **Evidence before elegance** — clear labels separate facts, inferences, and hypotheses.
3. **Strongest failure first** — the loop looks for the load-bearing weakness, not decorative balance.
4. **Cheap falsification** — test competing explanations before adding process.
5. **Action closed, cognition open** — decide when necessary, remain updateable.
6. **Proportionality** — a small reversible task should stay small.

## Language

The runtime skill is written in English for broad agent compatibility and instructs the agent to answer in the user's language. A maintained Chinese reference translation is available under [`translations/zh-CN`](translations/zh-CN/).

## Repository map

```text
SKILL.md                  Runtime entrypoint
references/              Decision, research, learning, and review modes
agents/openai.yaml       Codex interface and implicit invocation policy
examples/                Realistic usage examples
evals/                   Positive, negative, and boundary trigger cases
translations/zh-CN/      Chinese reference translation
assets/                  Project visual assets
```

## License

[MIT-0](LICENSE). Use, modify, redistribute, and commercialize without attribution requirements.
