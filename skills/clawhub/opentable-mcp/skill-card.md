## Description: <br>
Manage OpenTable reservations via MCP by searching restaurants, checking availability, booking tables, listing or canceling reservations, and managing favorites through a signed-in OpenTable browser session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to let an agent help manage OpenTable reservations from natural-language requests. It is intended for workflows such as finding restaurants, checking slots, booking or modifying reservations, canceling reservations, and managing saved restaurants. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can act on the user's real signed-in OpenTable session, including bookings, modifications, cancellations, and favorite changes. <br>
Mitigation: Install only after reviewing the MCP package and fetchproxy extension, and require explicit confirmation before actions that book, modify, cancel, or change favorites. <br>
Risk: Some reservations may involve cancellation policies or saved-card no-show fees. <br>
Mitigation: Use the preview flow to surface cancellation policy and saved-card details before committing a booking or modification. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/opentable-mcp) <br>
- [npm package](https://www.npmjs.com/package/opentable-mcp) <br>
- [Source repository](https://github.com/chrischall/opentable-mcp) <br>
- [fetchproxy extension](https://github.com/chrischall/fetchproxy) <br>
- [OpenTable](https://www.opentable.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration, Shell commands, MCP tool calls, Text] <br>
**Output Format:** [Markdown with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires opentable-mcp, the fetchproxy browser extension, and a signed-in opentable.com browser tab.] <br>

## Skill Version(s): <br>
0.15.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
