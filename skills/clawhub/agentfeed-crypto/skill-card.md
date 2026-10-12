## Description:

Guides agents in retrieving live crypto liquidation, funding, options, and market-state data through free and pay-per-call AgentFeed routes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seekdaseek](https://clawhub.ai/user/seekdaseek)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users consult live liquidation activity, funding anomalies, options positioning, and market conditions when assessing crypto markets; paid requests require user approval and a funded x402 client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid market-data requests may incur USDC charges.

Mitigation: Try free sample and documentation routes first, obtain user approval before paying, and cap each call at the disclosed price.

Risk: Payment to an incorrect recipient could lose funds.

Mitigation: Verify the recipient against a fresh payment challenge and stop if the address differs from the documented recipient.

Risk: Market data and forecasts may be stale, uncertain, or mistaken for trading advice.

Mitigation: Report timestamps and evidence limits, check stale or decline indicators, and leave trading decisions to the user.

## Reference(s):

- [AgentFeed API documentation](https://x402.ochinimus.app/openapi.json)
- [AgentFeed agent guide](https://x402.ochinimus.app/SKILL.md)
- [Project repository (listed in skill metadata)](https://github.com/seekdaseek/agentfeed)
- [ClawHub skill release](https://clawhub.ai/seekdaseek/skills/agentfeed-crypto)

## Skill Output:

**Output Type(s):** [Market-data analysis, Guidance, Shell commands]

**Output Format:** [Text or Markdown with optional shell commands and market-data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source timestamps, uncertainty, and per-call USDC prices.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
