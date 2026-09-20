## Description:

Use this skill to look up, search, and manage Google Contacts and Google People API records through gogcli.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users install this MCP server when they want an assistant to search personal contacts, query Google Workspace directory profiles, inspect manager or report relationships, and perform contact-management tasks through an authenticated gogcli setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist Google credentials through gogcli and expose account or directory data to an agent.

Mitigation: Install it only for accounts where agent-mediated contact management is intended, isolate and protect the persistent data directory and keyring, and use GOG_READONLY=1 for lookup-only deployments.

Risk: Contact deletion and dedupe apply operations can make destructive changes without a built-in confirmation step.

Mitigation: Require explicit human review before delete or dedupe apply actions, and preview dedupe plans before applying them.

Risk: Broad contacts_run and auth_run tools can execute arbitrary gog subcommands.

Mitigation: Avoid broad run tools unless the exact gog subcommand has been inspected and approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, files]

**Output Format:** [MCP tool responses with text, JSON dumps, setup snippets, and vCard file exports when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 22 or later, gogcli, and an authenticated Google account.]

## Skill Version(s):

4.1.0 (source: evidence release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
