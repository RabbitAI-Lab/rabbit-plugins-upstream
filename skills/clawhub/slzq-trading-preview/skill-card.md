## Description:

三立智期 抢先版 helps agents get a simulated trading key, query futures market and account data, and place or cancel simulated orders; live trading requires a live-capable key copied from the app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sqringwang](https://clawhub.ai/user/sqringwang)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub and OpenClaw users use this skill to interact with Sanli Zhiqi futures services from an agent: request simulated trading credentials, view market/account/position/order data, and route simulated or authorized live order actions through documented tools. The skill is not a source of investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can place or cancel live orders when configured with a live-capable key and live environment.

Mitigation: Keep the default simulated environment unless live trading is deliberate, verify the live-capable key and environment before use, and require the agent to restate order details for confirmation before any live place or cancel action.

Risk: The skill can persist trading credentials in local configuration files.

Mitigation: Treat local credential files as sensitive, avoid sharing machines or config files that contain the key, and remove or rotate the key if exposure is possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sqringwang/skills/slzq-trading-preview)
- [Usage notes](references/usage-notes.md)
- [Open API index](references/api.md)
- [OpenAPI contract](references/openapi.yaml)
- [Company FAQ](references/company-faq.md)
- [MCP runtime README](runtime/mcp/README.md)
- [Sanli Futures official website](https://www.sxslqh.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, API calls, guidance]

**Output Format:** [Markdown guidance with shell commands, configuration values, and API/tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist local API credentials and can access simulated or live trading capabilities depending on the user's key and selected environment.]

## Skill Version(s):

1.2.8 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
