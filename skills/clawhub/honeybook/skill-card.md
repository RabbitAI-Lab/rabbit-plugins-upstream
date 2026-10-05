## Description:

Helps users review and manage HoneyBook client-portal projects, messages, contracts, invoices, payments, meetings, and tasks across vendors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

HoneyBook clients can check vendor projects, questionnaires, messages, contracts, invoices, meetings, and tasks, and prepare replies or links for signing and payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Magic links and cached sessions can expose sensitive client-portal messages, contracts, invoices, and payment records.

Mitigation: Share links only with the intended agent, protect portal access, and request raw records only when needed.

Risk: Outbound messages reach workspace participants, while signing and payment links can lead to consequential actions.

Mitigation: Review recipients and message previews, and personally approve each message, signing, or payment step.

## Reference(s):

- [HoneyBook skill release on ClawHub](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text, structured portal summaries, and links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact views are the default; signing and payment use portal links.]

## Skill Version(s):

1.2.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
