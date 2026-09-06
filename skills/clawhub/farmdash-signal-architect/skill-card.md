## Description:

Use 84 FarmDash MCP tools for supervised DeFi research, swaps, simulations, perps, ACP commerce, portfolio intelligence, and MEV-aware execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and DeFi agents use this skill to research opportunities, simulate routes, prepare swaps or perpetuals, and manage portfolio workflows through FarmDash. Wallet-affecting actions require fresh quotes, explicit confirmation, and either local user signing or configured bounded delegation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financially sensitive DeFi actions can prepare swaps, perpetual orders, or delegated workflows.

Mitigation: Verify each token, chain, destination, amount, fee, quote, route, and simulation result before signing or authorizing delegated execution.

Risk: Wallet credentials or signing authority could be mishandled by an operator.

Mitigation: Do not provide private keys, seed phrases, mnemonics, wallet exports, or unrestricted credentials; use local signing or explicit bounded delegation only.

Risk: Commercial routing, referral, affiliate, or swap-fee compensation may influence how routes are presented.

Mitigation: Disclose FarmDash compensation and fees when presenting managed routes, and base recommendations on analysis, simulation, and risk data.

## Reference(s):

- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash API Schema](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash MCP Discovery Manifest](https://www.farmdash.one/.well-known/mcp.json)
- [FarmDash Agent Integration Documentation](https://www.farmdash.one/docs)
- [Live Agent Capability Status](https://www.farmdash.one/api/v1/agent/status)
- [FarmDash Security and Authority Boundaries](https://www.farmdash.one/security)
- [FarmDash Fees and Commercial Terms](https://www.farmdash.one/fees)
- [ClawHub Skill Listing](https://clawhub.ai/parmasanandgarlic/skills/farmdash-signal-architect)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with structured parameters, API references, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include quote, simulation, routing, fee, and confirmation details; wallet secrets are not requested or processed.]

## Skill Version(s):

1.2.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
