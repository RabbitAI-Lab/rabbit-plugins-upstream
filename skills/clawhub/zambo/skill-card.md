## Description:

Gives your agent hands -- 100+ native MCP tools for code audit, lead research, strategy analysis, onchain scoring, prompt defense, and crypto prices over one zero-auth remote MCP endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zambodotdev](https://clawhub.ai/user/zambodotdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an MCP client to Zambo's remote execution service for external research, code auditing, market and onchain analysis, prompt-defense checks, and other multi-step jobs that need tool execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote execution may disclose private code, confidential business data, wallet information, regulated data, or other sensitive prompts to Zambo's service.

Mitigation: Review intended data sharing before installation and only send data the user is comfortable sharing with Zambo's remote service.

Risk: Paid x402 requests can produce wallet signatures and settle USDC payments.

Mitigation: Require explicit user approval for each paid request before any wallet signature is produced, and report the spend receipt after settlement.

Risk: The security verdict is suspicious because of broad data-sharing scope and the paid signing flow.

Mitigation: Review the security summary and guidance before deployment, especially for private, regulated, or paid workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zambodotdev/skills/zambo)
- [Publisher profile](https://clawhub.ai/user/zambodotdev)
- [Zambo homepage](https://zambo.dev)
- [Agent docs](https://zambo.dev/llms.txt)
- [Human docs](https://zambo.dev/for-agents/)
- [Install docs](https://zambo.dev/install)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets and MCP tool-call results or receipts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote tool calls may return execution receipts, cost details, errors, and paid x402 settlement information.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
