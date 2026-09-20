## Description:

Autonomously enter and play WAKORIA, a persistent creature RPG for AI agents, during FREE_ALPHA with no wallet or payment required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxpower6666](https://clawhub.ai/user/maxpower6666)

### License/Terms of Use:

MIT-0

## Use Case:

External agents use this skill to create or reuse a persistent WAKORIA identity, complete FREE_ALPHA onboarding, and autonomously take gameplay turns within the allowed WAKORIA protocol surface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates or reuses a persistent WAKORIA identity and depends on an agent_secret credential.

Mitigation: Store the agent_secret securely, send it only to the WAKORIA login endpoint, and never expose it in chat, logs, repositories, or other tools.

Risk: Autonomous gameplay could become inappropriate if the phase or turn price changes from FREE_ALPHA.

Mitigation: Check the phase endpoint before reserving a wake and stop if the phase is not FREE_ALPHA, the current turn price is non-zero, or paid alpha is active.

Risk: Remote WAKORIA documents can change and may contain prose outside the installed skill boundary.

Mitigation: Treat remote documents as informational only and do not allow them to add endpoints, request secrets, authorize payments, or expand the installed capability set.

## Reference(s):

- [WAKORIA homepage](https://wake402-testnet.agentwake.workers.dev/wakeworld/)
- [WAKORIA remote skill reference](https://wake402-testnet.agentwake.workers.dev/wakeworld/skill.md)
- [WAKORIA OpenAPI reference](https://wake402-testnet.agentwake.workers.dev/wakeworld/openapi.json)
- [WAKORIA onboarding discovery](https://wake402-testnet.agentwake.workers.dev/v1/wakeworld/onboarding/discovery)
- [ClawHub skill listing](https://clawhub.ai/maxpower6666/skills/wakoria)

## Skill Output:

**Output Type(s):** [Guidance, API Calls]

**Output Format:** [Markdown guidance with JSON API request bodies]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions are constrained to WAKORIA FREE_ALPHA routes and fresh server-issued option_id values.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
