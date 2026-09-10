## Description:

MCP server for HoneyBook's client portal, covering contracts, invoices, questionnaires, messages, meetings, tasks, payments, session capture, in-portal messaging, and deep-link fallback for signing and paying.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to inspect and manage HoneyBook client-portal records across wedding vendors, including contracts, invoices, questionnaires, messages, meetings, tasks, notes, attachments, and payments. The skill also guides confirmation-sensitive actions such as sending messages and opening payment or signing deep links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HoneyBook magic links, flow links, portal sessions, and questionnaire credentials can expose sensitive client-portal data.

Mitigation: Treat these links like credentials, share them only when needed, and remove cached sessions or flow credentials when access is no longer required.

Risk: Messages sent through HoneyBook are real emails to workspace participants.

Mitigation: Review the generated message preview before rerunning send_message with confirm:true.

Risk: Payment and contract actions may affect legal or financial workflows.

Mitigation: Use the returned HoneyBook deep links yourself and confirm signing or payment steps directly in the portal.

Risk: Raw project or workspace file views may include broader vendor-side or high-volume portal data.

Mitigation: Use compact views and section-specific file reads first, escalating to raw output only when a required field is missing.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or plain text responses with tool-call guidance, previews, status summaries, and deep links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compact or raw views for selected records, confirmation-gated message sends, and portal deep links for signing or payment.]

## Skill Version(s):

0.10.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
