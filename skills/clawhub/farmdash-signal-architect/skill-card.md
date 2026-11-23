## Description:

OpenClaw DeFi execution with FarmDash's MCP contract: LI.FI and Relay swaps, simulation, zero-custody settlement verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research DeFi opportunities, prepare and simulate token swaps and hedges, and monitor settlement through FarmDash's agent tools. Wallet-changing actions use local user signing or an explicitly bounded delegation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release is rated suspicious; the assessment cites possible tool-metadata poisoning, disputed scanner evidence, incomplete component coverage, and unresolved local references.

Mitigation: Review the unresolved metadata and references and assess the uninspected component before installation; the other scanner's clean result does not resolve these gaps.

Risk: The skill can prepare wallet-affecting trades and delegated workflows, and on-chain transactions cannot be undone.

Mitigation: Verify token addresses, chains, amounts, route, fees, simulation results, and wallet address, then require fresh explicit user confirmation before signing or submitting.

## Reference(s):

- [FarmDash Signal Architect on ClawHub](https://clawhub.ai/parmasanandgarlic/skills/farmdash-signal-architect)
- [FarmDash agent documentation](https://www.farmdash.one/agents)
- [FarmDash MCP manifest](https://www.farmdash.one/.well-known/mcp.json)
- [FarmDash OpenAPI specification](https://www.farmdash.one/agents/openapi.yaml)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, API calls, JSON quote and transaction preparation data]

**Output Format:** [Structured text and JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research or user-reviewed transaction preparation, depending on the selected workflow.]

## Skill Version(s):

1.2.30 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
