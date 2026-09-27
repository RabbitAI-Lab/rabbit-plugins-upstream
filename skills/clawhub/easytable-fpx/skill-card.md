## Description:

Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical operators use this skill to query easyTable restaurant availability and manage reservations from shell workflows without running the easytable MCP server. The workflow can perform real booking changes, so write actions should be reviewed before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Confirmed create, modify, or cancel operations can change real restaurant reservations.

Mitigation: Require explicit user confirmation before any write action and do not run real create or cancel calls as tests.

Risk: The workflow can use browser-backed session access and booking details such as phone numbers.

Mitigation: Use it only with the user's own easyTable session and booking details, and avoid handling other people's reservation information.

Risk: Write endpoints can return HTTP 200 even when a booking action is rejected.

Mitigation: Inspect the parsed Status field and response body before treating a write action as successful.

Risk: Create and modify flows require manual Turnstile token handling that is time-limited and easy to misuse.

Mitigation: Harvest the token only immediately before the POST and re-check all payload fields before submission.

## Reference(s):

- [easyTable request recipes](references/easytable-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with shell command examples and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands operate through the user's browser-backed easyTable session and may return HTML fragments or JSONP-wrapped responses.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
