## Description: <br>
Production-grade MCP server for personal Outlook (Outlook.com / Hotmail / Live). 62 typed Graph tools across mail, calendar, contacts, to-do, drafts, attachments, folders, threading, batch ops, delta-sync. Granular permissions, OS-keyring auth, /$batch-optimized triage and bulk read. Built for agents that need real Outlook coverage, not a CLI wrapper. BYO Azure app; zero telemetry. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mpalermiti](https://clawhub.ai/user/mpalermiti) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agent builders and MCP client users use this skill to let agents read, triage, write, and organize personal Outlook mail, calendar, contacts, and tasks through typed Microsoft Graph tools. It is intended for personal Microsoft accounts, with work or school Entra ID accounts out of scope. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agents can access sensitive Outlook mailbox, calendar, contact, and task data. <br>
Mitigation: Install only for trusted agents and begin with read_only enabled. <br>
Risk: Write-capable tools can send, delete, move, or modify Outlook data. <br>
Mitigation: Enable only the needed allow_categories and toolsets, and gate destructive operations in the MCP client. <br>
Risk: Attachment tools can interact with local file paths. <br>
Mitigation: Avoid exposing attachment tools unless the agent is trusted with local file access. <br>
Risk: Authentication uses persistent token storage. <br>
Mitigation: Use OS keyring-backed token storage and configure encrypted keyring support on Linux before authenticating. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mpalermiti/skills/outlook-mcp) <br>
- [Publisher profile](https://clawhub.ai/user/mpalermiti) <br>
- [Project homepage](https://github.com/mpalermiti/outlook-mcp) <br>
- [PyPI package](https://pypi.org/project/outlook-graph-mcp/) <br>
- [MCP Registry listing](https://registry.modelcontextprotocol.io/v0/servers?search=mpalermiti) <br>
- [Security policy](SECURITY.md) <br>
- [Release changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, configuration, shell commands, guidance] <br>
**Output Format:** [MCP tool responses with structured text and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can read or modify Outlook data through Microsoft Graph and can save downloaded attachments to local file paths when attachment tools are enabled.] <br>

## Skill Version(s): <br>
1.12.0 (source: server evidence, pyproject.toml, CHANGELOG, server.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
