## Description:

Read a SimplePractice Client Portal through the simplepractice-mcp server for upcoming appointments, billing documents, balances, saved cards, pending paperwork, and practice announcements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users who authorize an agent to read their SimplePractice Client Portal can ask about appointments, billing records, balances, saved cards, pending paperwork, and practice announcements. The skill guides read-only portal access and cautions the agent to report only the requested health or billing information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive health-related, billing, and portal records.

Mitigation: Install only when agent access to those records is acceptable, and report only the information the user requested.

Risk: Repeated sign-in email requests can consume portal limits and disrupt access.

Mitigation: Check session status first, require explicit approval before sending a one-time sign-in email, and avoid retry loops.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplepractice)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance with tool names, parameters, and concise text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal guidance; compact views are used by default where supported.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
