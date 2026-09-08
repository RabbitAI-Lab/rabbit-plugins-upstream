## Description:

Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI instead of running the easytable-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to generate fpx CLI commands and request recipes for listing easyTable booking areas, dates, and times, looking up bookings by phone number, and cancelling bookings through an authorized browser-backed session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches commands that can view, create, modify, or cancel real restaurant bookings through a user's browser-backed easyTable session.

Mitigation: Confirm every create, modify, or cancel action manually and use the skill only for bookings and restaurants the user is authorized to manage.

Risk: The skill documents manual reuse of Turnstile or session-derived values, which can create privacy or service-compliance concerns.

Mitigation: Avoid copying or replaying Turnstile and session-derived values unless the user understands the implications, and discard any token values after the intended operation.

## Reference(s):

- [easyTable request recipes](references/easytable-requests.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are guidance and command recipes; commands may perform real booking operations when run by an authorized user.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
