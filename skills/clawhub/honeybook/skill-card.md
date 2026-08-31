## Description:

HoneyBook helps agents work with HoneyBook client-portal data for wedding-vendor contracts, invoices, proposals, payments, and signing links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use this skill to review HoneyBook wedding-vendor portal data, including active sessions, shared files, unsigned contracts, invoice status, saved payment methods, and deep links for signing or payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Magic links and captured portal sessions can grant access to sensitive HoneyBook client-portal data.

Mitigation: Treat pasted magic links like login credentials and share them only in trusted agent sessions.

Risk: Signing and payment workflows may expose payment-related data or lead the user toward consequential portal actions.

Mitigation: Review any sign or payment deep link yourself before acting on it.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text summaries with portal deep links when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference sensitive portal sessions, payment-related data, and sign or payment deep links.]

## Skill Version(s):

0.7.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
