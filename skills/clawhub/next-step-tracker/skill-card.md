## Description:

Tracks commitments made on sales calls, closes them when follow-through is documented, and posts due or overdue next steps to Slack on weekdays.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Sales teams and their developers use this skill to track promises made by either side on calls, check whether they were fulfilled, and remind account owners about due follow-ups in a private Slack channel.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer-influenced call notes and activity records can mislead unattended commitment extraction or closure.

Mitigation: Treat source records as untrusted data and validate quoted promises, due dates, and evidence before changing commitment status.

Risk: Slack reminders can expose customer details to unintended readers.

Mitigation: Restrict delivery to a private internal channel and build messages only from validated fields.

Risk: The agent may encounter unrelated sensitive content in its repository checkout.

Mitigation: Review repository access before installation and keep unrelated sensitive material outside its reach.

## Reference(s):

- [Next-step tracker on ClawHub](https://clawhub.ai/cargo-ai/skills/next-step-tracker)
- [Project homepage (listed in release metadata)](https://github.com/getcargohq/gtm-skills)
- [Slack reminder format](artifact/references/nudge.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown guidance with TypeScript and shell commands; deployed agent posts Slack message text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When deployed, records commitments and posts at most one due-date reminder per day.]

## Skill Version(s):

0.1.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
