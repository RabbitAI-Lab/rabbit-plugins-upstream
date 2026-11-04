## Description:

OpenClaw DeFi execution with FarmDash's MCP contract: LI.FI and Relay swaps, simulation, zero-custody settlement verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[parmasanandgarlic](https://clawhub.ai/user/parmasanandgarlic)

### License/Terms of Use:

MIT-0

## Use Case:

DeFi agent operators use this skill to research protocols, assess portfolio and trading strategies, and prepare swaps or other wallet actions. It guides users through simulations and approvals before wallet-affecting actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-affecting trades and optional automation can move funds and incur fees or losses.

Mitigation: Start with research-only or user-signed mode; review token addresses, destinations, allowances, signatures, and fees before approving. Set explicit spending limits, expiration, and a verified revocation method before enabling automation.

Risk: Use of the service can involve sharing public wallet and transaction-related data.

Mitigation: Review FarmDash's security boundaries and keep onboarding and installation analytics disabled unless needed; those analytics are optional.

## Reference(s):

- [FarmDash agent integration documentation](https://www.farmdash.one/docs)
- [FarmDash OpenAPI contract](https://www.farmdash.one/agents/openapi.yaml)
- [FarmDash MCP discovery manifest](https://www.farmdash.one/.well-known/mcp.json)
- [FarmDash security boundaries](https://www.farmdash.one/security)
- [Live agent capability status](https://www.farmdash.one/api/v1/agent/status)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Text, Guidance]

**Output Format:** [Structured tool requests and response summaries with concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on current market and service data; wallet-affecting actions require user approval and signing.]

## Skill Version(s):

1.2.27 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
