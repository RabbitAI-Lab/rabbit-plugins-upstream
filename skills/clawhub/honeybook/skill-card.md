## Description:

Honeybook helps an agent work with HoneyBook client-portal data for vendor contracts, invoices, questionnaires, messages, meetings, tasks, and payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to let an agent review HoneyBook portal information across wedding vendors, including contracts, invoices, questionnaires, messages, meetings, tasks, notes, and payments. It can also prepare confirmed portal actions such as sending messages or opening signing and payment links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: HoneyBook magic links and flow links can grant access to sensitive portal data.

Mitigation: Only use links from trusted vendor communications and treat pasted portal links like login credentials.

Risk: Confirmed message sends can email vendors and co-clients.

Mitigation: Review message previews carefully before confirming a send.

Risk: Portal records can contain personal, payment, contract, and event details.

Mitigation: Request raw or expanded records only when needed and avoid sharing outputs beyond the intended workflow.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text with portal summaries, message previews, status lists, and action links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compact or raw portal records depending on the requested tool view or section.]

## Skill Version(s):

0.10.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
