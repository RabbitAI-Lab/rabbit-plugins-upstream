## Description:

Read a SimplePractice Client Portal through the simplepractice-mcp server for upcoming appointments, invoices, statements, superbills, receipts, balances, saved cards, unsigned paperwork, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to read their own SimplePractice client portal information, including appointments, billing records, paperwork, announcements, and account context. It is intended for read-only reporting and guidance about portal data, not for paying bills, signing forms, or cancelling appointments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connected portal can expose sensitive medical, appointment, billing, paperwork, announcement, and saved-card metadata.

Mitigation: Use it only for the user's own portal access, report only the information requested, confirm the correct client record when one login covers multiple people, and sign out when the retained session is no longer needed.

Risk: Requesting repeated sign-in emails can consume rate limits and interfere with the user's only authentication path.

Mitigation: Check session status first, use an existing email link when available, ask before sending a sign-in link, and avoid retry loops.

Risk: Portal data can be misread as broader billing or appointment authority.

Mitigation: Treat empty portal billing lists as portal-only results, do not infer that the user owes nothing, and do not tell the user they can cancel an appointment unless the portal data and practice policy support that.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text guidance with SimplePractice portal tool names and result interpretation notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may summarize sensitive medical, appointment, billing, paperwork, announcement, and saved-card metadata returned by the connected portal tools.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
