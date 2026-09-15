## Description:

Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI, including listing booking areas, dates, and times, finding bookings by phone, and cancelling bookings through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect easyTable restaurant availability and perform selected booking-management actions from shell workflows. It is intended for reservations the user is authorized to manage and requires confirmation before actions that create, modify, or cancel real bookings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent browser-mediated access can continue after setup and may have weak scoping.

Mitigation: Pair only for the easyTable profile needed for the task, keep browser site access limited to easytable.com, and revoke the fpx/Transporter pairing when finished.

Risk: Create, modify, and cancel workflows can affect real restaurant reservations.

Mitigation: Use the skill only for reservations the user is authorized to manage, confirm each write action out of band, and inspect the parsed Status field rather than relying on HTTP success alone.

Risk: Phone numbers, booking IDs, and manual tokens can be exposed through shell commands, files, or shell history.

Mitigation: Avoid placing real personal data in shell history, use temporary files carefully, and delete booking payloads or copied tokens after use.

Risk: Create and modify flows are manual or hybrid because the fpx CLI cannot harvest the Turnstile token directly.

Mitigation: Treat create and modify actions as operator-supervised workflows and harvest any token immediately before use because it is single-use and short-lived.

## Reference(s):

- [easyTable requests for fpx](references/easytable-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-fpx)
- [easyTable booking host](https://book.easytable.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, endpoint examples, extraction commands, and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include commands that query or change live restaurant reservations; users should verify parsed booking status and avoid storing sensitive values in shell history.]

## Skill Version(s):

0.4.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
