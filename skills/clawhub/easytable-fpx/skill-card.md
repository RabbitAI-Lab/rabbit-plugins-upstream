## Description:

Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI instead of running the easytable-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to query easyTable availability, inspect existing bookings by phone number, and run booking cancellation workflows through an authorized browser-mediated fpx session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide real booking cancellations, creations, or modifications for restaurant reservations.

Mitigation: Use it only for bookings the user is authorized to manage, confirm booking details before any write action, and do not run create or cancel commands only to test the flow.

Risk: The workflow may send personal contact details, such as phone numbers, to easyTable through a browser-mediated session.

Mitigation: Limit use to necessary booking data, confirm user consent and authorization, and avoid exposing collected contact details in logs or shared outputs.

Risk: The manual Turnstile-token workaround has automation and session implications.

Mitigation: Avoid the workaround unless the user understands the implications and accepts the short-lived, manual browser-token handling step.

## Reference(s):

- [easyTable requests for fpx](references/easytable-requests.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands, request examples, and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes browser-mediated easyTable request recipes and cautions for real booking changes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
