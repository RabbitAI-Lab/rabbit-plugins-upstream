## Description:

Use 84 FarmDash MCP tools for supervised DeFi research, swaps, simulations, perps, ACP commerce, portfolio intelligence, and MEV-aware execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and supervised DeFi operators use this skill to research opportunities, request swap and perpetuals simulations, prepare locally signed transactions, and manage bounded delegation workflows through FarmDash.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-adjacent swaps, perpetuals, ACP funding, and autopilot workflows can affect user funds if used without the documented execution gates.

Mitigation: Keep the skill read-only unless the user explicitly chooses an action, then require a fresh quote, simulation, fee and destination disclosure, and local wallet confirmation or a revocable bounded delegation.

Risk: FarmDash may receive public wallet addresses, token addresses, chain IDs, transaction amounts, signatures, request IDs, session IDs, optional Bearer keys, and attribution headers.

Mitigation: Disclose the data sent to FarmDash before use and avoid providing private keys, seed phrases, mnemonics, OAuth tokens, or wallet exports.

Risk: Server evidence flags normalized fee history exposure and under-scoped wallet-adjacent execution tools as requiring review.

Mitigation: Review the skill before installation, do not treat fee history as proof of realized execution quality, and verify settlement through authoritative transaction evidence before starting dependent actions.

## Reference(s):

- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash DeFi Intelligence Website](https://www.farmdash.one/)
- [Canonical FarmDash Signal Architect Skill Manual](https://www.farmdash.one/openclaw-skills/farmdash-signal-architect/SKILL.md)
- [Agent Integration Documentation](https://www.farmdash.one/docs)
- [Live Agent Capability Status](https://www.farmdash.one/api/v1/agent/status)
- [OpenAPI Contract](https://www.farmdash.one/agents/openapi.yaml)
- [MCP Discovery Manifest](https://www.farmdash.one/.well-known/mcp.json)
- [Fees and Commercial Terms](https://www.farmdash.one/fees)
- [Security and Authority Boundaries](https://www.farmdash.one/security)
- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-signal-architect)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with API request details and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include DeFi research findings, quotes, simulation summaries, risk checks, fee disclosures, and confirmation prompts.]

## Skill Version(s):

1.2.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
