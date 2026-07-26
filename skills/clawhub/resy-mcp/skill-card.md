## Description: <br>
Manage Resy restaurant reservations via MCP by searching venues, booking tables, listing and canceling reservations, managing favorites, and subscribing to Priority Notify. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent interact with a Resy account for restaurant discovery, booking, cancellation, favorites, payment-method lookup, and Priority Notify management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make live Resy account changes, including booking, cancellation, favorites, and Priority Notify updates. <br>
Mitigation: Confirm the restaurant, date, time, party size, payment or fee details, and intended account action before allowing changes. <br>
Risk: The skill requires Resy credentials for account access. <br>
Mitigation: Keep RESY_EMAIL and RESY_PASSWORD out of shared project files and use local environment or secret storage. <br>
Risk: The skill relies on Resy's private web-app API behavior. <br>
Mitigation: Expect endpoint changes or failures and verify actions in Resy before relying on the result. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/resy-mcp) <br>
- [resy-mcp npm package](https://www.npmjs.com/package/resy-mcp) <br>
- [resy-mcp repository link declared by the artifact](https://github.com/chrischall/resy-mcp) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, configuration, shell commands] <br>
**Output Format:** [Markdown with JSON and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes MCP setup guidance and examples for live Resy reservation workflows.] <br>

## Skill Version(s): <br>
0.6.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
