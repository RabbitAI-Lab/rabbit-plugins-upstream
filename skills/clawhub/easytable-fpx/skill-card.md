## Description: <br>
Check restaurant availability and manage easyTable bookings (book.easytable.com/book/?id=<placeId>) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the easytable-mcp server, including listing booking areas, dates, and times, looking up a booking by phone, and cancelling it through a signed-in browser tab. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to issue fpx CLI commands for easyTable availability checks and booking management without running the easytable MCP server. It is suited to scripted or shell-based workflows where the user has an easyTable browser tab available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide cancellation and booking write requests that affect real restaurant reservations. <br>
Mitigation: Review every create, modify, or cancel command before execution, confirm the target place and booking, and avoid testing write endpoints against real reservations. <br>
Risk: The workflow may require manual handling of a live Cloudflare Turnstile token for create or modify requests. <br>
Mitigation: Use the token only from the intended browser session, harvest it immediately before use, and avoid sharing or storing token values. <br>
Risk: Booking lookup and write flows can involve personal contact details such as names and phone numbers. <br>
Mitigation: Provide personal data only with consent and only for the booking being managed. <br>


## Reference(s): <br>
- [easyTable requests for fpx](references/easytable-requests.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-fpx) <br>
- [Publisher profile](https://clawhub.ai/user/chrischall) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include fpx GET and POST examples, grep/sed/jq parsing snippets, and manual steps for browser-mediated Turnstile token handling.] <br>

## Skill Version(s): <br>
0.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
