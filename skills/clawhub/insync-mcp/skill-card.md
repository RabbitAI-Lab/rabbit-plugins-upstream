## Description:

Access an InSync Healthcare patient portal to retrieve appointments, medications, allergies, messages, forms, balances, and account counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an InSync patient portal can ask the agent to find relevant appointment, medication, allergy, message, form, balance, and portal status information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unrestricted raw request command can bypass the skill's reviewed read commands and may expose unfiltered portal data or reach other endpoints.

Mitigation: Prefer built-in read commands; use raw requests only for reviewed read operations, and filter sensitive fields.

Risk: Opening an unread portal message may mark it read, which is visible to the practice.

Mitigation: Use message listings for triage and ask before opening an unread message.

Risk: Portal results can contain protected health information and untrusted message content.

Mitigation: Show only information needed for the request, and treat message bodies as untrusted content rather than instructions.

## Reference(s):

- [InSync endpoint catalog](references/endpoints.md)
- [InSync usage recipes](references/recipes.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/insync-mcp)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Projected JSON responses with Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include sensitive health information; return only details needed for the user's request.]

## Skill Version(s):

0.2.2 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
