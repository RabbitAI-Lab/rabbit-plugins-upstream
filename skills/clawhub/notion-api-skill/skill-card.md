## Description:

Notion API integration with managed OAuth for querying databases, searching pages, reading workspace content, and performing confirmed Notion writes through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to access Notion workspaces through a managed Maton connection for read/list workflows, explicit user-confirmed writes, and optional user-approved automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the external Maton CLI and a Maton account to access Notion data.

Mitigation: Install and authenticate Maton deliberately, prefer OAuth, and verify the active profile before making Notion requests.

Risk: Long-lived API keys or raw response dumps can expose workspace data or credentials.

Mitigation: Prefer OAuth, avoid exporting API keys, and return only the fields needed for the user's task.

Risk: Write operations, connection changes, hosted functions, and triggers can affect Notion resources or continue running after setup.

Mitigation: Confirm the exact connection, target resource, handler, trigger, destination, and network posture with the user before taking those actions, and remove automation when it is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/notion-api-skill)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Notion API Introduction](https://developers.notion.com/reference/intro)
- [Notion trigger reference](references/notion/triggers.md)
- [Time trigger reference](references/time/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [Google Mail trigger reference](references/google-mail/triggers.md)
- [HubSpot trigger reference](references/hubspot/triggers.md)
- [Linear trigger reference](references/linear/triggers.md)
- [Calendly trigger reference](references/calendly/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user confirmation before connection creation, writes, function deployment, trigger setup, or deletion.]

## Skill Version(s):

1.2.2 (source: ClawHub server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
