## Description:

Checks restaurant availability and manages easyTable bookings from a shell with the fpx CLI, including listing booking areas, dates, and times, looking up bookings by phone, and cancelling bookings through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query easyTable availability and perform booking-management tasks from shell workflows when the easyTable MCP server is not available. It is most appropriate for guided workflows where side-effecting actions such as create, modify, or cancel are explicitly reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables an agent to perform real restaurant booking actions through a user's browser session, including cancellation and create or modify requests.

Mitigation: Require explicit user confirmation before any create, modify, or cancel command is executed, and avoid running side-effecting calls as tests.

Risk: Booking lookup and write flows can involve personal details such as phone numbers, names, email addresses, and comments.

Mitigation: Only send personal details with clear user consent and keep command examples free of real customer data unless the user provides it for the task.

Risk: The manual Turnstile-token workaround is the highest-risk part of the flow because it reuses a browser-derived challenge token outside the normal page interaction.

Mitigation: Prefer normal browser-mediated booking flows for create or modify operations, or restrict token use to short-lived, user-approved sessions.

## Reference(s):

- [easyTable requests for fpx](references/easytable-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read calls return HTML fragments; cancellation and booking endpoints can have real-world side effects and require response-body checks.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
