## Description:

Guides DeFi agents through market research, trade quotes, simulations, and user-signed swap preparation with FarmDash tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to assess DeFi opportunities, compare routes, simulate swaps, and prepare transactions for user review and signing. It also supports wallet monitoring and explicitly bounded delegated workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Swaps and other DeFi actions can cause financial loss if quotes, routes, fees, or signatures are wrong or stale.

Mitigation: Review fresh quotes and simulations; independently verify token addresses, chains, amounts, fees, and every wallet signature before signing or submitting.

Risk: Delegated or autopilot actions may exceed the user's intended trading authority.

Mitigation: Require explicit setup approval, bounded budgets, allowlists, cooldowns, and a clear revocation path; halt when a bound is missing or violated.

Risk: Wallet-linked activity and optional onboarding can disclose public addresses and usage metadata to FarmDash.

Mitigation: Disclose the data sharing and make optional registration a user choice; never share seed phrases or private keys.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/parmasanandgarlic/skills/farmdash-signal-architect)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash MCP discovery manifest](https://www.farmdash.one/.well-known/mcp.json)
- [FarmDash API contract](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash fees](https://www.farmdash.one/fees)
- [FarmDash security boundaries](https://www.farmdash.one/security)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration, Shell commands]

**Output Format:** [Markdown guidance and structured tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes trade analysis, quotes, simulation results, and transaction payloads for independent review and local signing.]

## Skill Version(s):

1.2.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
