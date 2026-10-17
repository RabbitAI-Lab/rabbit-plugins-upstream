## Description:

Helps users review HoneyBook client-portal projects, contracts, invoices, messages, meetings, tasks, and payments across vendors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

HoneyBook clients use this skill to review vendor projects, questionnaires, contracts, invoices, messages, meetings, and tasks, and to request portal links for signing or payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal links and cached sessions grant access to sensitive client and vendor data.

Mitigation: Install only if you trust the requested access; share portal links only with the intended agent and avoid raw views unless additional fields are needed.

Risk: Sending a message emails the vendor and potentially other workspace participants.

Mitigation: Review the message preview and recipients, then explicitly approve each send; keep confirmation prompts enabled.

Risk: Contract signing and invoice payment may have legal or financial consequences.

Mitigation: Confirm the intended contract or invoice and review the portal page before signing or paying.

## Reference(s):

- [honeybook skill release on ClawHub](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text summaries and portal links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Compact summaries by default; signing and payment use portal links.]

## Skill Version(s):

1.2.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
