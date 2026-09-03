## Description:

Reads a SimplePractice Client Portal through the simplepractice-mcp server for upcoming appointments, billing records, balances, saved cards, paperwork, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to read their SimplePractice client portal for therapy or healthcare appointments, billing records, document requests, payment method metadata, and practice announcements without modifying portal data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive health and billing information from a SimplePractice client portal after sign-in.

Mitigation: Install and use it only when the user is comfortable letting the agent read appointments, billing records, paperwork status, and payment method metadata.

Risk: One portal login can cover multiple clients, which could cause the agent to report the wrong person's records.

Mitigation: Confirm whose record is being accessed before reporting portal details.

Risk: A saved SimplePractice session can remain sensitive until it expires or is cleared.

Mitigation: Treat saved sessions as sensitive and clear or let them expire when portal access is no longer needed.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text responses summarizing portal information]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only output may include sensitive health and billing information after user sign-in.]

## Skill Version(s):

0.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
