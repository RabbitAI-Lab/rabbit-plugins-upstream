## Description: <br>
Helps users check restaurant availability and make, change, or cancel table reservations at restaurants that use an easyTable booking widget. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to inspect easyTable restaurant availability, find existing reservations by phone number, and manage bookings through their own loaded browser session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, modify, or cancel real restaurant reservations using the user's provided name and phone number. <br>
Mitigation: Review the dry-run preview and confirm the restaurant, date, time, party size, name, and phone number before setting confirm to true. <br>
Risk: The skill relies on a browser extension bridge to use the user's active easyTable tab. <br>
Mitigation: Install and pair the extension only when comfortable with that session bridge, and approve the pairing code deliberately. <br>
Risk: Booking confirmations depend on a loaded easyTable widget tab and a short-lived Turnstile token. <br>
Mitigation: Keep the relevant booking widget tab open and reload it before retrying if a create or modify action fails because the token expired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/easytable-mcp) <br>
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Configuration] <br>
**Output Format:** [Markdown or plain text with reservation details, setup steps, and confirmation prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Booking create, modify, and cancel actions are confirm-gated and return a dry-run preview before applying changes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
