## Description:

Helps clients review HoneyBook vendor portals for contracts, invoices, payments, questionnaires, messages, meetings, and tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Clients use this skill to review wedding-vendor portal information, track outstanding contracts and invoices, and communicate with vendors through HoneyBook.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad wedding-related prompts may trigger access to sensitive HoneyBook portal data unnecessarily.

Mitigation: Confirm that the user wants HoneyBook accessed before opening portal data for an ambiguous request.

Risk: Raw portal views and saved sessions can expose sensitive account or client information.

Mitigation: Prefer compact views, request raw data only when necessary, and safeguard portal sessions.

Risk: Sending a portal message can email vendors and other workspace participants.

Mitigation: Preview the recipients and message, and obtain the user's explicit approval before sending.

## Reference(s):

- [HoneyBook skill on ClawHub](https://clawhub.ai/chrischall/skills/honeybook)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Links]

**Output Format:** [Text or Markdown with portal deep links when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can summarize portal records and provide signing or payment links; outgoing messages require confirmation.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
