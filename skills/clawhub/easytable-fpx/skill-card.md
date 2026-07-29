## Description: <br>
Check restaurant availability and manage easyTable bookings from a shell with the fpx CLI instead of running the easytable-mcp server. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to check easyTable restaurant availability, list booking areas, retrieve bookings by phone number, and run cancellation workflows from shell-based fpx commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide live booking changes, including cancellation, through the user's browser session. <br>
Mitigation: Verify the restaurant, phone number, booking id, party size, date, and time before running create, modify, or cancel commands. <br>
Risk: The security summary flags instructions for copying a browser anti-bot token into scripted requests. <br>
Mitigation: Prefer the normal easyTable website or an approved API for booking writes, and avoid copying anti-bot tokens from DevTools. <br>
Risk: Write endpoints may return HTTP 200 even when a booking action is rejected. <br>
Mitigation: Inspect the parsed response status and error fields rather than relying only on the command exit code. <br>


## Reference(s): <br>
- [easyTable requests for fpx](references/easytable-requests.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-fpx) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill describes fpx commands that can return HTML fragments or JSONP-wrapped booking responses.] <br>

## Skill Version(s): <br>
0.2.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
