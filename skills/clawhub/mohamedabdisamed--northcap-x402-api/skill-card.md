## Description:

Provides pay-per-call crypto trading signals with entry, stop-loss and take-profit via the x402 standard (USDC on Ethereum). Live DRT/ICT signals for agents and traders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohamedabdisamed](https://clawhub.ai/user/mohamedabdisamed)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, agents, and traders use this skill to discover, purchase access to, and call a paid crypto trading-signal API that returns symbols, direction, entry, stop-loss, take-profit, and risk-reward values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each paid API call may incur a USDC charge.

Mitigation: Run the skill only when the user has explicitly accepted the external service charge and payment flow.

Risk: Trading signals can be incorrect or financially harmful.

Mitigation: Treat signal output as decision-support information and require human review before trading or automating financial actions.

Risk: The API key and request parameters are sent to an external Northcap endpoint.

Mitigation: Use a scoped API key, avoid sending unnecessary sensitive data, and confirm network access is expected before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mohamedabdisamed/skills/northcap-x402-api)
- [Northcap x402 API endpoint](https://x402.186.240.156.169.sslip.io)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Configuration]

**Output Format:** [Markdown instructions with JSON API request and response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3, network access to the Northcap endpoint, and X402_API_KEY for authenticated signal requests.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
