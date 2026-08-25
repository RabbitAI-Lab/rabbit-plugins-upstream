## Description:

Read a SimplePractice Client Portal through the simplepractice-mcp server, including upcoming appointments, invoices, statements, superbills, receipts, balances, saved cards, paperwork waiting to be signed, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to read their SimplePractice client portal for appointments, billing documents, balances, paperwork requests, and practice announcements without making changes in the portal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive health and billing information from a SimplePractice client portal.

Mitigation: Use it only when the user is comfortable sharing portal data with the agent, and report only the specific information requested.

Risk: A single login can cover multiple client profiles, such as a parent managing children.

Mitigation: Confirm the correct client record before reporting appointments, billing, documents, or other portal details.

Risk: Sign-in links and PINs are sensitive, single-use authentication material.

Mitigation: Ask before sending a sign-in email, avoid repeated requests, and only process links or PINs the user initiated.

Risk: Persisted sessions on shared machines may allow later portal access.

Mitigation: Clear or expire the session when the machine is shared or when the user no longer wants portal access available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or plain text guidance with MCP tool calls and portal data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal access; session state may persist between runs.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
