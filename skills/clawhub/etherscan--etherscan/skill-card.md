## Description:

Navigate Etherscan website features, API endpoints, CLI commands, and MCP tools so an agent can select the right interface, construct requests or commands, handle authentication, confirm chain support, interpret errors, and compare behavior across Etherscan interfaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[etherscan](https://clawhub.ai/user/etherscan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent operators use this skill to route Etherscan tasks to the website, API, CLI, or MCP interface and preserve chain, authentication, rate-limit, pagination, and error context while completing blockchain explorer workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Etherscan API keys, MCP bearer tokens, wallet prompts, and CLI credentials may be exposed or misused if copied into prompts, logs, source files, or output.

Mitigation: Treat keys and bearer tokens as secrets, replace exposed keys with YourApiKeyToken, use secret configuration or environment variables, and never request private keys or seed phrases.

Risk: Using the wrong chain, explorer domain, endpoint, command, or tool schema can return misleading blockchain data or act on the wrong network.

Mitigation: Confirm the exact chain, chain ID, domain, and current interface authority before acting, and do not infer support from EVM compatibility.

Risk: Verification submissions, signed transaction broadcasts, wallet interactions, configuration deletion, or other state-changing actions can have external effects.

Mitigation: Require explicit authorization after reviewing the exact payload, chain, interface, and effect, and prefer read-only inspection until authorization is provided.

Risk: Rate limits, plan restrictions, pagination, truncation, or API and MCP error envelopes can hide incomplete or failed results.

Mitigation: Preserve throttling, pagination, truncation, plan restrictions, and transport, protocol, validation, and application-level error context in the response.

## Reference(s):

- [Etherscan website reference](references/site.md)
- [Etherscan API reference](references/api.md)
- [Etherscan CLI reference](references/cli.md)
- [Etherscan MCP reference](references/mcp.md)
- [Etherscan documentation index](https://docs.etherscan.io/llms.txt)
- [Etherscan supported chains](https://docs.etherscan.io/supported-chains.md)
- [Etherscan rate limits](https://docs.etherscan.io/resources/rate-limits.md)
- [Etherscan PRO endpoints](https://docs.etherscan.io/resources/pro-endpoints.md)
- [Etherscan common errors](https://docs.etherscan.io/resources/common-error-messages.md)
- [Etherscan CLI guide](https://docs.etherscan.io/ai/cli.md)
- [Etherscan MCP guide](https://docs.etherscan.io/ai/mcp.md)
- [Model Context Protocol specification](https://modelcontextprotocol.io/specification)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with inline commands, URLs, API request shapes, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured JSON or CSV guidance when the selected Etherscan interface supports it.]

## Skill Version(s):

1.0.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
