## Description:

This skill should be used when the user asks about HoneyBook client-portal data. Triggers on phrases like "check HoneyBook", "sign contract", "pay invoice", "HoneyBook vendors", "unsigned contracts", "open invoices", "message the planner", "reply to my vendor", "next meeting with the planner", or any request involving wedding-vendor contracts, invoices, brochures, proposals, payments, messages, meetings or tasks via HoneyBook.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

HoneyBook clients use the skill to review information shared by their wedding vendors, including projects, questionnaires, files, invoices, payments, messages, meetings, tasks, and notes. It can also provide portal links for signing or paying and send messages after the user reviews and approves them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Magic links and cached sessions can provide access to HoneyBook client-portal data.

Mitigation: Use only trusted vendor-issued links and treat links and saved sessions as credentials; avoid sharing them.

Risk: A sent message reaches everyone in the workspace, including the vendor and any co-clients.

Mitigation: Review the recipients and message content, then obtain the user's explicit approval before sending.

Risk: Signing a contract or paying an invoice has consequential effects.

Mitigation: Review the target contract or invoice and obtain the user's explicit approval before opening the signing or payment link.

Risk: Raw views can expose broader vendor account data, and external server behavior was not verified.

Mitigation: Use a trusted MCP server, prefer compact responses, and request raw vendor data only when necessary.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Concise text or structured data, including summaries and portal links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain vendor-provided content; raw views can include broader account data. Messages, signing, and payment actions require user review and approval.]

## Skill Version(s):

1.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
