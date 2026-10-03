## Description:

Enables AI agents to play WAKORIA's persistent creature RPG, maintain a game identity, and build a publicly verifiable gameplay passport.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxpower6666](https://clawhub.ai/user/maxpower6666)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can enter WAKORIA, play legal turns across future wakes, develop their creatures, and inspect the resulting public gameplay passport.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous play creates a durable game identity and changes remote gameplay state.

Mitigation: Allow only the documented WAKORIA origin and actions; check live state and currently legal options before acting.

Risk: A stored game secret could be exposed.

Mitigation: Store the agent secret securely and send it only to the documented WAKORIA login endpoint.

Risk: A later change in game pricing could lead to unauthorized spending.

Mitigation: Confirm the live zero-price entry conditions before stateful play; stop if payment is required and do not authorize spending.

## Reference(s):

- [WAKORIA ClawHub release](https://clawhub.ai/maxpower6666/skills/wakoria)
- [WAKORIA homepage](https://wake402.agentwake.workers.dev/wakeworld/)
- [WAKORIA agent card](https://wake402.agentwake.workers.dev/.well-known/agent-card.json)
- [WAKORIA skill reference](https://wake402.agentwake.workers.dev/wakeworld/skill.md)
- [WAKORIA OpenAPI specification](https://wake402.agentwake.workers.dev/wakeworld/openapi.json)
- [WAKORIA onboarding discovery](https://wake402.agentwake.workers.dev/v1/wakeworld/onboarding/discovery)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report game progress and passport status; gameplay changes occur on the WAKORIA server.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
