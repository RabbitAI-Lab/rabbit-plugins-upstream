## Description:

Automate Zalo messaging, Official Account (OA), and MCP server integration via zalo-agent-cli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[phucmpham](https://clawhub.ai/user/phucmpham)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to guide agents through Zalo CLI messaging, Official Account workflows, webhook listening, and MCP server setup. It is suited to account owners automating Zalo conversations, groups, followers, and related payment-message formats with explicit control over credentials and outbound messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read message history, save event logs, and forward private message payloads to webhooks or MCP clients.

Mitigation: Use only accounts and Official Accounts you control, limit history searches to the minimum necessary scope, and forward message data only to approved localhost or authenticated HTTPS endpoints.

Risk: Login, OA, webhook, and MCP workflows can expose credentials, tokens, QR login endpoints, or bearer-auth endpoints if misconfigured.

Mitigation: Protect credential and log files, require explicit user confirmation before credential export, avoid exposing temporary QR or MCP endpoints publicly, and use bearer authentication for HTTP MCP mode.

Risk: Outbound Zalo and OA message commands can send account messages, files, payment-related QR content, or bulk communications.

Mitigation: Require explicit confirmation before sending messages or files, especially to groups, followers, or third-party recipients, and verify target IDs and message content before execution.

Risk: Skipping webhook verification on exposed OA listeners can allow untrusted event injection.

Mitigation: Use verified domains and authenticated HTTPS for production OA webhooks, and do not use --no-verify on exposed webhook listeners.

## Reference(s):

- [Zalo Agent CLI skill page](https://clawhub.ai/phucmpham/skills/zalo-agent)
- [Publisher profile](https://clawhub.ai/user/phucmpham)
- [zalo-agent CLI homepage](https://github.com/PhucMPham/zalo-agent-cli)
- [Login Flow](references/login-flow.md)
- [zalo-agent CLI Full Command Reference](references/command-reference.md)
- [Listen Mode Real-Time Event Monitoring](references/listen-mode-guide.md)
- [Official Account Command Reference](references/oa-command-reference.md)
- [Zalo MCP Server Guide](references/mcp-guide.md)
- [Evaluation Scenarios](evals/eval-scenarios.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-installed zalo-agent binary on Darwin or Linux. Some workflows require an authenticated Zalo account, human QR scan, OA credentials, or user-supplied webhook and MCP endpoints.]

## Skill Version(s):

1.7.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
