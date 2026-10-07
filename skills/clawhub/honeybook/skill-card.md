## Description:

Helps users review HoneyBook client-portal records, manage vendor messages, and access contract-signing and invoice-payment links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

HoneyBook clients use this skill to review wedding-vendor contracts, invoices, questionnaires, projects, messages, meetings, tasks, and payments, and to prepare replies or obtain signing and payment links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal data and locally stored portal or questionnaire credentials are sensitive.

Mitigation: Install only if comfortable with this access and local credential storage; share portal and flow links only when needed.

Risk: Sending a message emails the vendor and other workspace participants.

Mitigation: Review the message preview and obtain explicit approval before sending.

Risk: Signing or paying can create binding or financial consequences.

Mitigation: Approve signing or payment confirmations only when the action is intended.

## Reference(s):

- [HoneyBook skill listing](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Text, structured records, and portal links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Message listings show previews; full messages require a separate request. Signing and payment actions return portal links.]

## Skill Version(s):

1.2.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
