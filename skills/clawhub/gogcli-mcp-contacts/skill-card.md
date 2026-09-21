## Description:

Use when the user asks to look up, search, or manage Google Contacts, Workspace directory users, profile fields, manager/reports relations, or other People API data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and developers use this skill to let an agent search Google Contacts, inspect Google Workspace People directory records, and manage contact records through an authenticated gogcli setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Destructive contact operations can create, update, merge, or delete Google Contacts without an enforced confirmation step.

Mitigation: Install only for trusted users and clients, keep GOG_READONLY=1 unless write access is required, and add an approval layer before enabling mutation tools.

Risk: Authentication and health tools may reveal account or token-status details in shared or prompt-injection-prone environments.

Mitigation: Limit auth-status and auth-health exposure to trusted clients and avoid enabling them in shared agent environments without additional access controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/gogcli-mcp-contacts)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [gogcli project](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [text, JSON, files, configuration]

**Output Format:** [MCP tool responses, JSON People API dumps, and optional vCard export files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the configured Google account and gogcli authentication state.]

## Skill Version(s):

4.2.4 (source: server release metadata and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
