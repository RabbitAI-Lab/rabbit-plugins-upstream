## Description:

Use when building DeFi trade strategy: 84 MCP tools for quotes, simulation, Trail Heat, receipts, agent hiring. Swaps need fresh quote, simulation, signing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and DeFi operators use this skill to research opportunities, request quotes, simulate wallet-affecting actions, prepare user-signed swaps or delegated workflows, and reconcile receipts through FarmDash tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-risk DeFi automation can prepare swaps, perpetuals actions, ACP funding, or autopilot workflows that may affect wallet assets.

Mitigation: Require fresh quotes, simulations, explicit confirmations, verified token contracts and destinations, and bounded delegation controls before any wallet-affecting step.

Risk: FarmDash may handle public wallet and trade metadata, paid-tier API keys, session tokens, signatures, request IDs, and referral-route data.

Mitigation: Install only when this data sharing is acceptable, keep API keys and session tokens scoped, and never provide private keys, seed phrases, mnemonics, or wallet exports.

Risk: Commercial routes and fees can affect user decisions or execution cost.

Mitigation: Disclose referral or routing compensation and fee details before presenting managed routes or execution options.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-signal-architect)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [Canonical FarmDash Signal Architect Skill Manual](https://www.farmdash.one/openclaw-skills/farmdash-signal-architect/SKILL.md)
- [Agent Integration Documentation](https://www.farmdash.one/docs)
- [Live Agent Capability Status](https://www.farmdash.one/api/v1/agent/status)
- [OpenAPI Contract](https://www.farmdash.one/agents/openapi.yaml)
- [MCP Discovery Manifest](https://www.farmdash.one/.well-known/mcp.json)
- [Security and Authority Boundaries](https://www.farmdash.one/security)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured tool calls, JSON snippets, shell commands, and configuration details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include DeFi quote, simulation, route, fee, risk, delegation, and receipt-review details; wallet-affecting actions require fresh confirmation or bounded delegation.]

## Skill Version(s):

1.2.22 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
