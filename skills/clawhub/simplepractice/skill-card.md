## Description:

Read a SimplePractice Client Portal through the simplepractice-mcp server, including upcoming appointments, billing records, balances, saved payment-method summaries, paperwork, documents, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill with an agent to read their SimplePractice client portal for healthcare or therapy appointments, billing records, insurance superbills, forms, documents, and announcements. The skill is intended for read-only reporting and should not be used to infer facts beyond the portal records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose healthcare, billing, document, appointment, balance, and saved payment-method summary information from a user's SimplePractice client portal.

Mitigation: Use it only in conversations where that context is appropriate, report only what was asked, and sign out when session reuse is no longer wanted.

Risk: A single portal login can cover multiple clients, such as a parent viewing more than one child's record.

Mitigation: Confirm whose record is being reported before sharing appointment, billing, document, or paperwork details.

Risk: Portal billing data may be incomplete when a practice invoices outside SimplePractice.

Mitigation: Describe empty portal billing lists as no portal records found rather than as proof that nothing is owed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text summaries of portal records and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SimplePractice portal access; compact responses are the default for supported read tools.]

## Skill Version(s):

0.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
