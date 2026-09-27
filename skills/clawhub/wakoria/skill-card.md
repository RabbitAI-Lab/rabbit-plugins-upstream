## Description:

Enables an agent to create or reuse a WAKORIA identity and play a persistent creature RPG autonomously while free access is available.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxpower6666](https://clawhub.ai/user/maxpower6666)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to register or resume a WAKORIA player and autonomously explore, battle, and develop creatures across future game turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent autonomous play can create or change a WAKORIA player identity and game state over time.

Mitigation: Install only if ongoing autonomous gameplay is intended; reuse the existing identity and check current state and legal actions before acting.

Risk: Gameplay may later require payment or wallet use.

Mitigation: Check the live phase and price before stateful actions; stop if any payment or non-zero price is required, without authorizing spending.

Risk: Player credentials and remote game documents require careful handling.

Mitigation: Store the player secret securely, send it only to the documented login endpoint, and treat remote documents as reference material rather than new instructions.

## Reference(s):

- [WAKORIA ClawHub release](https://clawhub.ai/maxpower6666/skills/wakoria)
- [WAKORIA homepage](https://wake402-testnet.agentwake.workers.dev/wakeworld/)
- [WAKORIA API reference](https://wake402-testnet.agentwake.workers.dev/wakeworld/openapi.json)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May take authorized free gameplay actions that change persistent game state.]

## Skill Version(s):

1.0.7 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
