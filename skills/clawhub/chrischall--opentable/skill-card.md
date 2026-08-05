## Description: <br>
Manage OpenTable reservations via MCP: search restaurants, check slot availability, book tables, list or cancel reservations, and manage favorites from a signed-in OpenTable browser session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to help manage OpenTable restaurant reservations through an MCP server and a signed-in browser session. It supports restaurant discovery, availability checks, booking previews, booking, reservation changes, cancellations, and favorites management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can act on a signed-in OpenTable account and may book, modify, cancel, or change favorites. <br>
Mitigation: Require the user to confirm account-affecting actions before execution, including the restaurant, date, time, party size, and intended operation. <br>
Risk: Some reservations may include cancellation policies or card holds. <br>
Mitigation: Surface booking preview details and obtain explicit user confirmation for cancellation terms and any card hold before committing the reservation. <br>
Risk: The MCP server and fetchproxy extension use the user's active OpenTable browser session. <br>
Mitigation: Install and run the skill only when the user is comfortable granting access to the signed-in OpenTable session. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable) <br>
- [opentable-mcp npm package](https://www.npmjs.com/package/opentable-mcp) <br>
- [opentable-mcp repository](https://github.com/chrischall/opentable-mcp) <br>
- [fetchproxy extension](https://github.com/chrischall/fetchproxy) <br>
- [OpenTable](https://www.opentable.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls, Markdown] <br>
**Output Format:** [Markdown with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can initiate reservation, cancellation, modification, and favorites actions through an authenticated OpenTable browser session.] <br>

## Skill Version(s): <br>
0.16.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
