## Description:

Use when building DeFi trade strategy: 84 MCP tools for quotes, simulation, Trail Heat, receipts, agent hiring. Swaps need fresh quote, simulation, signing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research DeFi opportunities, compare protocol and portfolio signals, prepare wallet-signed swaps, monitor receipts, and coordinate bounded agent workflows through FarmDash.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prepare user-signed trades and delegated workflows while some transaction-safety details are ambiguous.

Mitigation: Use read-only mode by default, require fresh quotes, simulations, and explicit wallet confirmation for each trade, and avoid bounded autopilot until budgets, revocation, and policy bounds are clear.

Risk: FarmDash may receive wallet and transaction metadata during routing, analytics, rate limiting, paid-tier access, and security checks.

Mitigation: Share only the minimum public wallet and transaction details needed for the chosen action, and never provide private keys, seed phrases, mnemonics, wallet exports, or unrelated credentials.

Risk: FarmDash referral routes and routing compensation add commercial-routing risk.

Mitigation: Verify FarmDash route links against canonical protocol domains and disclose referral or routing compensation before the user follows a route or signs a transaction.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/parmasanandgarlic/skills/farmdash-signal-architect)
- [FarmDash Agent Hub](https://www.farmdash.one/agents)
- [Canonical Skill Manual](https://www.farmdash.one/openclaw-skills/farmdash-signal-architect/SKILL.md)
- [FarmDash Documentation](https://www.farmdash.one/docs)
- [OpenAPI Contract](https://www.farmdash.one/agents/openapi.yaml)
- [MCP Discovery Manifest](https://www.farmdash.one/.well-known/mcp.json)
- [FarmDash Security and Authority Boundaries](https://www.farmdash.one/security)
- [FarmDash Fees and Commercial Terms](https://www.farmdash.one/fees)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON parameters, command snippets, and API or MCP tool-call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include transaction-preparation guidance, quote and simulation requirements, and local-signing confirmation steps; no private keys or seed phrases should be output.]

## Skill Version(s):

1.2.22 (source: server release metadata; artifact frontmatter reports 4.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
