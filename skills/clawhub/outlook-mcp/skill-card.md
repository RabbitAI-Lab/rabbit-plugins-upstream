## Description:

Connects AI agents to personal Outlook mail, calendars, contacts, and tasks through Microsoft Graph tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT

## Use Case:

Agent builders and users of personal Outlook accounts use this server to summarize and organize mail, manage calendars and contacts, and track tasks. Write actions require the user's chosen permissions and configuration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Granting an agent access to personal mail, calendar, contacts, and tasks exposes sensitive account data.

Mitigation: Install only when Outlook access is needed; start with read_only enabled and use read_only_consent with a separate read-only Azure app when Microsoft-enforced read-only access is required.

Risk: Enabled write tools can change or send account content.

Mitigation: Enable only the write categories the user intends the agent to use.

Risk: Attachment tools can read or save local files within their configured directory.

Mitigation: Keep attachments_dir narrowly scoped.

## Reference(s):

- [Outlook MCP on ClawHub](https://clawhub.ai/mpalermiti/skills/outlook-mcp)
- [outlook-graph-mcp on PyPI](https://pypi.org/project/outlook-graph-mcp/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [MCP tool responses with text or structured data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses depend on the selected tools and account permissions.]

## Skill Version(s):

1.24.0 (source: ClawHub release, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
