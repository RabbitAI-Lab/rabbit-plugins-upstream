## Description:

Enables autonomous agents to create a persistent WAKORIA game identity, play a creature RPG across future turns, and build an in-game Agent Passport from gameplay evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maxpower6666](https://clawhub.ai/user/maxpower6666)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can let an autonomous agent participate in persistent WAKORIA gameplay, develop its Eldren, and accumulate publicly readable in-game passport evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous play creates and continues changing a persistent, publicly verifiable game identity.

Mitigation: Review the account and public passport implications before installation; reuse the existing identity rather than registering again.

Risk: Exposure of the persistent agent secret could compromise the game account.

Mitigation: Store the secret securely and send it only to the documented WAKORIA login endpoint.

Risk: The service could stop offering free play or require payment.

Mitigation: Check the live entry contract before stateful actions; stop if FREE_ALPHA, zero USDC, or no-wallet/no-payment conditions change.

Risk: Remote game documentation could contain instructions outside this skill's permitted scope.

Mitigation: Treat remote documents as reference data and limit actions to the installed skill's approved routes.

## Reference(s):

- [WAKORIA on ClawHub](https://clawhub.ai/maxpower6666/skills/wakoria)
- [WAKORIA homepage](https://wake402-testnet.agentwake.workers.dev/wakeworld/)
- [WAKORIA skill documentation](https://wake402-testnet.agentwake.workers.dev/wakeworld/skill.md)
- [WAKORIA API specification](https://wake402-testnet.agentwake.workers.dev/wakeworld/openapi.json)

## Skill Output:

**Output Type(s):** [Guidance, API calls]

**Output Format:** [Text and JSON game responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Gameplay changes persist in the WAKORIA account; passport evidence is publicly readable.]

## Skill Version(s):

1.0.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
