## Description:

Composio MCP helps agents configure and use Composio CLI or MCP access to connect with external apps, authenticate credentials, discover tools, execute actions, and troubleshoot setup issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect agents to Composio-backed applications, configure CLI or MCP credentials, choose the right execution path, and recover from common authentication or platform configuration failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad persistent access to Composio and connected external accounts could let multiple local agents act on email, code, messaging, calendar, or document services.

Mitigation: Use least-privilege, revocable Composio credentials, configure only the intended MCP platform, and review live execute, proxy, or run commands before allowing side effects.

Risk: Credential values may be placed into local MCP configuration if users paste keys directly.

Mitigation: Prefer environment variables or an agent secret store for COMPOSIO_API_KEY and COMPOSIO_CONSUMER_KEY, and avoid logging, committing, or echoing ak_* or ck_* values.

Risk: Setup helpers can modify local agent configuration and may persist access after installation.

Mitigation: Run setup in dry-run mode first, target a single platform when possible, and verify or remove the Composio MCP entry when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/composio-mcp)
- [Publisher profile](https://clawhub.ai/user/afonsoft)
- [Composio documentation](https://docs.composio.dev)
- [Composio Connect documentation](https://docs.composio.dev/docs/composio-connect)
- [Composio GitHub repository](https://github.com/ComposioHQ/composio)
- [Consumer project boundaries and auth selection](https://docs.composio.dev/kb/guide/consumer-project-boundaries-and-auth-selection)
- [CLI reference](references/cli-reference.md)
- [MCP config reference](references/mcp-config.md)
- [Platform quirks](references/platform-quirks.md)
- [Tools inventory](references/tools-inventory.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and JSON configuration blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Composio CLI commands, MCP client configuration snippets, troubleshooting checks, and credential-handling guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact metadata.version is 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
