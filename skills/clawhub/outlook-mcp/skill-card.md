## Description:

Connects agents to personal Outlook mail, calendars, contacts, tasks, and attachments through Microsoft Graph tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mpalermiti](https://clawhub.ai/user/mpalermiti)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with a personal Outlook account can read and organize mail, manage calendars, contacts, and tasks, and handle attachments. Setup requires an Azure app registration and host-side authentication; work or school accounts are not supported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can access sensitive mail, contacts, calendar entries, tasks, and attachments.

Mitigation: Install only for a personal Outlook account you intend the agent to access; start with read_only enabled and consider read_only_consent with a read-only Azure app.

Risk: Attachment tools can upload or overwrite files in the configured attachment directory.

Mitigation: Keep attachments_dir limited to a narrow, dedicated directory.

Risk: Mail and other account content may contain instructions written by third parties.

Mitigation: Treat account content as data, not instructions; require the user's own request before sending, forwarding, deleting, or changing settings.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/mpalermiti/skills/outlook-mcp)
- [Outlook Graph MCP package](https://pypi.org/project/outlook-graph-mcp/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Text and Markdown with structured Outlook data and optional setup commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read and write actions depend on the user's permissions and configured access mode.]

## Skill Version(s):

1.25.0 (source: ClawHub release, pyproject.toml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
