## Description:

Read a SimplePractice Client Portal through the simplepractice-mcp server for appointments, billing documents, balances, saved cards, paperwork, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to read patient-side SimplePractice portal information about therapy or healthcare appointments, account balance, billing records, insurance superbills, provider forms, and practice announcements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can surface sensitive medical and billing information from a SimplePractice client portal.

Mitigation: Report only the information the user asked for and treat returned appointment, billing, form, and client details as sensitive.

Risk: A single portal login can cover multiple clients, so the agent could report the wrong person's records.

Mitigation: Confirm the correct client record before sharing portal details.

Risk: Billing results can be incomplete when a practice invoices outside the portal.

Mitigation: Describe empty portal billing lists as no invoices found in the portal rather than saying nothing is owed.

## Reference(s):


## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration]

**Output Format:** [Markdown guidance with tool names and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal access guidance; resulting agent responses may contain sensitive healthcare and billing information.]

## Skill Version(s):

0.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
