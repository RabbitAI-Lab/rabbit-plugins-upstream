## Description:

Helps users access and manage HoneyBook client-portal contracts, invoices, questionnaires, messages, meetings, tasks, and payments across wedding vendors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

HoneyBook clients can review vendor contracts, invoices, questionnaires, messages, meetings, and tasks, and request links to sign or pay through the portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pasted magic links grant access to client-portal data.

Mitigation: Treat magic links as account credentials and share them only when portal access is intended.

Risk: Vendor, invoice, payment, and message details may be sensitive.

Mitigation: Review portal information before sharing it and limit access to the intended task.

Risk: Messages or payment and signature links can lead to consequential actions.

Mitigation: Confirm the recipient and user intent before sending messages or opening payment or signature links; clarify ambiguous requests.

## Reference(s):

- [HoneyBook skill listing](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Text, Guidance, Links]

**Output Format:** [Plain text and portal links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive client-portal details and confirmation-gated links for signing or payment.]

## Skill Version(s):

1.2.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
