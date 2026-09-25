## Description:

Helps Kia owners check vehicle status, location, and charge state and request confirmed vehicle commands through their Kia account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners use this skill to ask an agent about their vehicle's status, location, and charging, or to approve climate, charging, and door commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and persistent session tokens could expose vehicle access if shared.

Mitigation: Keep MCP configuration out of source control and shared folders, restrict file permissions, and forget the session when access should be removed.

Risk: Vehicle location and enabled remote commands could expose sensitive information or alter the vehicle's state.

Mitigation: Use read-only mode until commands are needed, and obtain user confirmation before each enabled command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package (linked in skill)](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports vehicle information and command outcomes; requests user approval before actions.]

## Skill Version(s):

1.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
