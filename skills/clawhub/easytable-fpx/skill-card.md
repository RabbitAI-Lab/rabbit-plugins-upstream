## Description:

Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI, including listing booking areas, dates, and times, looking up bookings by phone, and canceling bookings through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators use this skill to guide agents through easyTable availability checks and authorized booking lookup or cancellation workflows using fpx shell commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide live cancellation, creation, or modification of restaurant bookings.

Mitigation: Require explicit user confirmation before any cancel, create, or modify request, and verify the restaurant, phone number, party size, date, time, and booking id before execution.

Risk: Booking lookup and cancellation workflows may expose phone numbers or booking details.

Mitigation: Avoid logging personal data, redact booking details in shared transcripts, and only process reservations the user is authorized to manage.

Risk: The browser-backed fpx workflow can reuse a Cloudflare-cleared browser session.

Mitigation: Pair fpx only with an intended easyTable browser tab, confirm browser site access settings, and disconnect or close the session when the workflow is complete.

Risk: Write endpoints may return HTTP 200 even when a booking action is rejected or malformed.

Mitigation: Parse the response status body after write calls and do not treat exit code alone as proof that a booking action succeeded.

## Reference(s):

- [easyTable requests for fpx](references/easytable-requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes fpx setup, request recipes, response parsing notes, and live-action cautions.]

## Skill Version(s):

0.2.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
