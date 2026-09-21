## Description:

Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI instead of running the easytable-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list easyTable booking areas, dates, and times, find bookings by phone, and prepare or run fpx commands for authorized booking management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cancel, create, or modify commands can change real restaurant reservations.

Mitigation: Use the skill only for bookings the user is authorized to manage, and require explicit final confirmation before any write command.

Risk: The workflow can handle personal data such as names, phone numbers, and emails.

Mitigation: Limit data exposure to the minimum needed for the booking task and avoid retaining copied payloads or command outputs.

Risk: Browser-extension pairing persists and can continue to route requests through the user's browser session.

Mitigation: Confirm the intended browser profile and easyTable tab before use, and disconnect or unpair the fpx profile when access is no longer needed.

## Reference(s):

- [easyTable requests for fpx](references/easytable-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, endpoint URLs, and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes cautions for real booking changes, confirmation checks, browser pairing, and personal data handling.]

## Skill Version(s):

1.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
