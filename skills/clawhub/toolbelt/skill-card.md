## Description:

Toolbelt helps agents set up and use a shared MCP workspace for ingesting approved data, querying structured and unstructured sources, recording findings, and sharing context across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[toolbeltai](https://clawhub.ai/user/toolbeltai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to provision a Toolbelt MCP connection, ingest approved documents or tables, query hybrid data sources, and preserve or share findings across agents and sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account provisioning, MCP configuration writes, uploads, recorded findings, and share URL creation can affect external services, local configuration, or persistent workspace state.

Mitigation: Require explicit user consent before each network call, configuration write, upload, persistence-sensitive action, or share URL creation.

Risk: Uploaded documents and recorded findings may persist in the Toolbelt namespace and become visible to future connected agents.

Mitigation: Upload or record only content approved by the user, scope saved information to the task, and avoid sensitive material unless the user explicitly requires it.

Risk: The Toolbelt bearer token stored in an MCP client configuration grants access to the configured namespace.

Mitigation: Disclose the exact configuration path before writing, store the token only in that MCP configuration after consent, avoid echoing the full token, and explain revocation by removing the MCP entry or using the Toolbelt UI.

Risk: A Toolbelt share URL can grant namespace access to whoever receives it.

Mitigation: Confirm the intended workspace, recipient, and access level before creating a share URL, and send it only through a user-controlled channel.

## Reference(s):

- [Toolbelt homepage](https://toolbelt.ai)
- [Toolbelt documentation](https://toolbelt.ai/docs)
- [Toolbelt agent-readable documentation](https://toolbelt.ai/llms-full.txt)
- [ClawHub skill listing](https://clawhub.ai/toolbeltai/skills/toolbelt)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTP examples, shell commands, JSON configuration snippets, and brief YAML connection status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit user consent before network calls, MCP configuration writes, uploads, recorded findings, or share URL creation.]

## Skill Version(s):

1.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
