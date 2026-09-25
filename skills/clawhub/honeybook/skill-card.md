## Description:

Helps an agent work with HoneyBook client-portal data for vendor workspaces, contracts, invoices, questionnaires, messages, meetings, tasks, notes, attachments, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External HoneyBook portal users use this skill to review vendor-shared project information, contracts, invoices, questionnaires, messages, meetings, tasks, notes, attachments, and payment status. The skill also supports confirmed user-directed actions such as preparing portal links for signing or payment and sending HoneyBook messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad HoneyBook-related triggers may route generic wedding, payment, message, or meeting requests into tools that access sensitive portal data.

Mitigation: Confirm the user intends to use HoneyBook before reading portal data, marking messages seen, sending messages, or providing signing and payment links.

Risk: Local HoneyBook portal credentials may remain available after the user no longer needs access.

Mitigation: Review and clear the local ~/.honeybook-mcp credential cache when HoneyBook access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text summaries with portal links and confirmation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive HoneyBook portal details and user-confirmed outbound message or portal-action previews.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
