## Description:

Connects agents to Sanli Zhiqi futures workflows for market data, account and position queries, news, leaderboard data, simulated order placement, and live conditional or stop-profit/stop-loss orders when authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[13371979982](https://clawhub.ai/user/13371979982)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to Sanli Zhiqi futures account, market, news, and order workflows. It supports simulated trading by default and live trading workflows only when the user supplies appropriately authorized credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can affect real trading accounts when live credentials and live trading environment are configured.

Mitigation: Keep the environment set to sim unless live trading is explicitly intended, and require clear user confirmation before live order, cancellation, condition-order, or stop-profit/stop-loss actions.

Risk: Unsafe endpoint configuration could expose trading requests or credentials.

Mitigation: Use only https:// endpoints and avoid http:// API domains.

Risk: API keys may be persisted locally in skill or OpenClaw configuration.

Mitigation: Avoid displaying full keys, protect local configuration files, and rotate or revoke the API key if the local machine or OpenClaw configuration may be exposed.

Risk: The server-resolved provenance for this version is unavailable.

Mitigation: Do not infer GitHub provenance from the skill text; rely on ClawHub release evidence and independently verify broker or account-opening channels through official regulator or firm sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/13371979982/skills/slzq-trading)
- [Publisher profile](https://clawhub.ai/user/13371979982)
- [Open API index](references/api.md)
- [OpenAPI specification](references/openapi.yaml)
- [Usage notes](references/usage-notes.md)
- [Company FAQ](references/company-faq.md)
- [MCP runtime README](runtime/mcp/README.md)
- [Sanli official website](https://www.sxslqh.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown guidance with inline commands, configuration snippets, and structured tool or API call instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use local MCP tools and HTTPS API calls; outputs should avoid exposing full API keys.]

## Skill Version(s):

1.5.0 (source: frontmatter, VERSION, manifest.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
