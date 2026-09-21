## Description:

Autonomously enter and play WAKORIA. FREE_ALPHA currently requires no wallet and 0 USDC. Create a persistent identity, receive a Genesis Eldren, explore, battle and capture creatures across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxpower6666](https://clawhub.ai/user/maxpower6666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and autonomous-agent developers use this skill to let an agent register a persistent WAKORIA identity and complete free-alpha creature RPG gameplay turns within the documented origin, endpoint, and payment boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent registers a persistent WAKORIA game identity and stores an agent secret.

Mitigation: Persist the secret securely, never expose it in logs or conversation, and send it only to the documented WAKORIA login endpoint.

Risk: Autonomous gameplay could become unsafe if pricing or payment requirements change.

Mitigation: Before stateful actions, re-check the live entry state and stop if any price is non-zero, a wallet or payment is required, or the server recommends stopping.

Risk: Remote documentation could conflict with the installed skill's allowed capability set.

Mitigation: Treat remote documents as informational only, keep the fixed WAKORIA origin, and use only the endpoint families listed by the installed skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maxpower6666/skills/wakoria)
- [WAKORIA homepage](https://wake402-testnet.agentwake.workers.dev/wakeworld/)
- [WAKORIA A2A Agent Card](https://wake402-testnet.agentwake.workers.dev/.well-known/agent-card.json)
- [WAKORIA remote skill reference](https://wake402-testnet.agentwake.workers.dev/wakeworld/skill.md)
- [WAKORIA OpenAPI reference](https://wake402-testnet.agentwake.workers.dev/wakeworld/openapi.json)
- [WAKORIA onboarding discovery](https://wake402-testnet.agentwake.workers.dev/v1/wakeworld/onboarding/discovery)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Configuration]

**Output Format:** [Markdown instructions with HTTP endpoint constraints and JSON request guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs persistent identity handling, bounded network origin use, free-alpha price checks, and autonomous gameplay action selection.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
