## Description:

Read a SimplePractice Client Portal through the simplepractice-mcp server for upcoming appointments, billing documents, balances, saved cards, paperwork, documents, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users with an authenticated SimplePractice Client Portal session use this skill to answer specific questions about healthcare appointments, billing artifacts, balances, paperwork, documents, payment methods, and announcements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive healthcare, billing, document, appointment, and payment-method metadata through the configured SimplePractice MCP server.

Mitigation: Install only when that access is acceptable, use the skill for specific questions, and sign out when session persistence is no longer wanted.

Risk: One authenticated portal account can cover multiple client profiles.

Mitigation: Verify which client profile is active before reporting appointments, billing, paperwork, documents, or other portal details.

Risk: Portal billing and appointment data can be over-interpreted.

Mitigation: Report only what the portal returns; do not infer that no portal invoices means no balance, and do not tell the user they can cancel unless the portal policy and flags support it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with MCP tool names and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal queries; compact views may omit media while preserving dates, amounts, links, and document data.]

## Skill Version(s):

0.4.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
