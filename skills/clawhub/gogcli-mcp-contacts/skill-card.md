## Description:

Use when the user asks to look up, search, or manage Google Contacts and the broader People API (Workspace directory).

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT

## Use Case:

Developers and users can ask an agent to find or manage personal Google Contacts and search Google Workspace People profiles. It supports contact lookups, directory queries, and contact maintenance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Contact deletion, dedupe apply, and raw commands can change contact data without an extra confirmation.

Mitigation: Enable GOG_READONLY=1 for lookups; before writes, require host approval for deletion, dedupe apply, and raw commands, and back up affected contacts.

Risk: Google authorization may grant broader access than a task needs.

Mitigation: Use an isolated Google account with only the necessary Contacts and People access, and decline unrelated OAuth permissions.

Risk: Exported contact data may be exposed through an overly broad file location.

Mitigation: Restrict export directories to locations intended for contact data.

Risk: The targeted review did not verify live behavior or all bundled dependencies.

Mitigation: Pin the package version and review the code and tool permissions before use.

## Reference(s):

- [gogcli-mcp project repository](https://github.com/chrischall/gogcli-mcp)
- [gogcli documentation and source](https://github.com/openclaw/gogcli)
- [Model Context Protocol](https://modelcontextprotocol.io)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [Structured contact and People profile results, typically JSON or text; contact updates when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, update, merge, export, or delete contact data when requested and permitted.]

## Skill Version(s):

4.10.0 (source: package.json and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
