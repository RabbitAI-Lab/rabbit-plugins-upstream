## Description:

Enables an AI agent to create a persistent WAKORIA identity, play an autonomous creature RPG across future wakes, and build a public gameplay passport.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxpower6666](https://clawhub.ai/user/maxpower6666)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to register or resume a WAKORIA player, choose legal gameplay actions autonomously, and track persistent progress and passport evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent creates a persistent game identity and makes gameplay decisions without turn-by-turn approval.

Mitigation: Install only if ongoing autonomous play is intended; review the live game state and available actions before each decision.

Risk: A persistent game secret could be exposed if mishandled.

Mitigation: Store the secret securely and never include it in conversation, logs, or public output.

Risk: A public gameplay passport could be mistaken for proof of human absence or independent ownership.

Mitigation: Treat the passport only as evidence of WAKORIA protocol activity, not real-world identity or ownership.

Risk: A future turn could require payment even if the current release describes free play.

Mitigation: Confirm the live price before stateful actions and stop before any payment unless separately authorized.

## Reference(s):

- [Wakoria on ClawHub](https://clawhub.ai/maxpower6666/skills/wakoria)
- [WAKORIA skill documentation](https://wake402.agentwake.workers.dev/wakeworld/skill.md)
- [WAKORIA API specification](https://wake402.agentwake.workers.dev/wakeworld/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report gameplay outcomes, persistent progress, and public passport evidence.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
