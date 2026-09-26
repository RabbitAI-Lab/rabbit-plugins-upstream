## Description:

Helps users read their SimplePractice client portal for appointments, billing records, outstanding paperwork, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Clients and authorized caregivers use this skill to check upcoming appointments, balances, invoices, superbills, forms, and announcements in a SimplePractice Client Portal. The skill only reads portal information; it does not pay bills, sign forms, or cancel appointments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive health and billing information may expose private details.

Mitigation: Install only if comfortable with this access, confirm the intended client record, and report only what the user requested.

Risk: Emailed sign-in links can grant access to the client portal.

Mitigation: Treat sign-in links as sensitive and sign out on shared or untrusted machines.

Risk: Missing portal billing items may be mistaken for no balance owed.

Mitigation: Describe absent records as absent from the portal rather than asserting that nothing is owed.

## Reference(s):

- [SimplePractice skill on ClawHub](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language summaries of client portal records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; report only the requested client's relevant records.]

## Skill Version(s):

1.2.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
