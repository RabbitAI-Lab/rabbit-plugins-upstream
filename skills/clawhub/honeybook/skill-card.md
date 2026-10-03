## Description:

Helps users review and manage HoneyBook client-portal contracts, invoices, questionnaires, messages, meetings, tasks, and payments across vendors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

HoneyBook clients use this skill to check vendor contracts, invoices, questionnaires, messages, meetings, payments, and tasks, and to request portal links or send messages with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal magic links and questionnaire flow links can grant access to private client information.

Mitigation: Treat links as login credentials and provide them only when you intend to grant the agent portal or questionnaire access.

Risk: Detailed views can disclose more vendor and portal data than a summary needs.

Mitigation: Use compact or summary views by default and request raw data only when necessary.

Risk: Messages reach workspace recipients, and signing or payment links initiate consequential user actions.

Mitigation: Review message previews and recipients, and confirm each send, sign, or pay action before proceeding.

## Reference(s):

- [HoneyBook skill on ClawHub](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Conversational summaries, message previews, and portal links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact responses by default; some detailed views expose additional vendor or portal data.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
