## Description:

Provides read-only DeFi research on opportunities, public-wallet portfolios, hypothetical allocations, routes, Trail Heat, and Sybil risk without executing transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

DeFi researchers and agents use this skill to compare protocols and points opportunities, review public-wallet health, and preview hypothetical allocations and routes before deciding whether to act separately.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research requests can disclose public wallet addresses, query details, and an optional API key to FarmDash.

Mitigation: Share only data needed for research; do not provide private keys, seed phrases, signed messages, or wallet exports.

Risk: Partner route links may carry referral or routing compensation.

Mitigation: Disclose commercial relationships, check fees, and independently verify destination domains before proceeding.

Risk: Research results and route previews can be mistaken for authorization to trade.

Mitigation: Keep this skill read-only; use a separate execution tool only after explicit user confirmation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/parmasanandgarlic/skills/farmdash-trail-intelligence)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [FarmDash agent documentation](https://www.farmdash.one/docs)
- [FarmDash MCP configuration](https://www.farmdash.one/.well-known/mcp.json)
- [FarmDash API contract](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash security boundaries](https://www.farmdash.one/security)
- [FarmDash fees and commercial terms](https://www.farmdash.one/fees)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research and route previews; no signing, trading, or fund transfers.]

## Skill Version(s):

1.0.21 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
