## Description:

Read a SimplePractice Client Portal through the simplepractice-mcp server: upcoming appointments, invoices, statements, superbills, receipts, balance and saved cards, paperwork waiting to be signed, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to answer questions about SimplePractice Client Portal appointments, billing, documents, saved cards, paperwork, and announcements. It is intended for read-only access to the patient-side portal, not for cancelling appointments, signing forms, or paying bills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive health or billing information could be shared from the wrong covered client record.

Mitigation: Start with the account view and confirm which client record is being discussed before reporting portal information.

Risk: Full portal records may expose more health, billing, document, or announcement detail than the user needs.

Mitigation: Prefer compact views unless the user explicitly needs full records, and report only what was asked.

Risk: A saved portal session on a shared device or agent environment may expose client-portal access to another user.

Mitigation: Sign out after use when the device or agent environment is shared.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [guidance, shell commands]

**Output Format:** [Markdown guidance with inline tool names and shell command references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SimplePractice portal workflow; compact views are preferred unless full records are needed.]

## Skill Version(s):

1.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
