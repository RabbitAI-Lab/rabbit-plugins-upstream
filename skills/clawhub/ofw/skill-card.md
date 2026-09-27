## Description:

Connects an agent to OurFamilyWizard to review and manage co-parenting messages, calendar events, expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing co-parenting arrangements use this skill to check OurFamilyWizard messages, calendars, expenses, and journal entries, and to prepare or perform account actions with approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive family and legal information, including the account password and downloaded data, may be exposed.

Mitigation: Protect credentials and downloaded data; keep configuration files out of repositories and backups where possible.

Risk: Write actions can change a co-parenting record or share information with others.

Mitigation: Require explicit user approval before sending, deleting, recording expenses, changing events or journal entries, or sharing attachments.

Risk: Reading unread messages can mark them as viewed, while cached results may be stale or incomplete.

Mitigation: Warn before fetching unread messages and verify live status, freshness, and completeness before stating current account facts.

## Reference(s):

- [ofw on ClawHub](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Conversational text and Markdown with tool-backed results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account data may be cached or incomplete; verify freshness and completeness before reporting current status.]

## Skill Version(s):

2.19.4 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
