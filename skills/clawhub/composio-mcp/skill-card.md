## Description:

Use when the user asks to connect an AI agent to external apps via Composio, or when Composio CLI or MCP setup fails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to configure Composio CLI or MCP access, authenticate with the right key type, discover tool slugs, and troubleshoot failed Composio setup across supported agent clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup helper can add Composio MCP access persistently to multiple installed agent clients.

Mitigation: Use dry-run first, choose the single intended agent client before installation, and remove unwanted client entries after testing.

Risk: A plaintext ck_* consumer key can be written into agent client configuration files.

Mitigation: Prefer environment variables or a secret-store reference, avoid logging keys, and rotate the consumer key if it may have been exposed.

Risk: Bypassing checks or using raw proxy and run commands can perform actions with connected third-party accounts.

Mitigation: Inspect schemas and use dry-run before mutating tools; avoid skip-checks, raw proxy, or composio run unless the task explicitly requires them.

## Reference(s):

- [Composio documentation](https://docs.composio.dev)
- [Composio Connect documentation](https://docs.composio.dev/docs/composio-connect)
- [Consumer project boundaries and auth selection](https://docs.composio.dev/kb/guide/consumer-project-boundaries-and-auth-selection)
- [Composio GitHub repository](https://github.com/ComposioHQ/composio)
- [Publisher source repository](https://github.com/afonsoft/skills)
- [Composio CLI reference](references/cli-reference.md)
- [Composio MCP configuration reference](references/mcp-config.md)
- [MCP platform config quirks](references/platform-quirks.md)
- [Composio tool inventory](references/tools-inventory.md)
- [Composio troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash, JSON, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Composio CLI commands, MCP configuration blocks, verification commands, and edits to local agent client configuration files.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
