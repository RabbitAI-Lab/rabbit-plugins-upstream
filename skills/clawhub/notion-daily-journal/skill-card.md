## Description:

Collects daily activity from Linear, Slack, and DM chat, writes or updates a Notion daily journal page, and sends a DM completion notice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[p-take55](https://clawhub.ai/user/p-take55)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals or teams can use this skill to turn daily Linear, Slack, and DM activity into a concise Notion journal for personal work tracking and handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private Slack or DM content may be copied into Notion more broadly than intended.

Mitigation: Limit Slack and DM sources to intended workspaces and conversations, and review journal content before writing it to Notion.

Risk: The skill may write to the wrong Notion parent or disclose the resulting page link to the wrong DM recipient.

Mitigation: Configure a fixed Notion parent page and intended DM recipient before use, then confirm both before sending completion messages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/p-take55/skills/notion-daily-journal)
- [Server-resolved GitHub provenance](https://github.com/p-take55/phase1-selfedit-demo/tree/main/skills/notion-daily-journal)
- [Publisher profile](https://clawhub.ai/user/p-take55)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Configuration]

**Output Format:** [Concise Markdown sections written to Notion plus a short DM notification]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires configured Notion destination and access to intended Linear, Slack, and DM sources.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
