## Description:

Use when the user asks to look up, search, or manage Google Contacts and the broader People API (Workspace directory).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this MCP server to let an agent search, inspect, export, and manage Google Contacts and Google Workspace People directory records through gogcli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access broader Google Contacts and People API data than basic personal-contact lookup.

Mitigation: Use the narrowest Google OAuth scopes possible and review requested contact and directory access before installing.

Risk: Mutation tools can update, delete, or merge contacts when enabled.

Mitigation: Set GOG_READONLY=1 unless edits are required, and preview dedupe operations before applying changes.

Risk: A configurable remote runner can receive contact commands and OAuth access tokens.

Mitigation: Do not configure GOG_RUNNER_URL unless the endpoint uses HTTPS, is controlled by you, is allowed by egress policy, and is approved to receive those commands and tokens.

Risk: Generic run tools can broaden what an autonomous agent may execute through gogcli.

Mitigation: Avoid exposing generic run tools to autonomous agents unless their use is reviewed and constrained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [gogcli CLI](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)
- [Project documentation](https://github.com/chrischall/gogcli-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [MCP tool responses, including text, JSON, vCard export data, and setup snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return contact, People API, Workspace directory, authentication status, or command-runner output depending on the selected MCP tool.]

## Skill Version(s):

2.30.0 (source: package.json, manifest.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
