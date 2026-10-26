## Description:

Helps users check and control their own Kia vehicle through their Kia Access account, with confirmation before vehicle commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners use this skill to check vehicle status, location, and charging information and, with their approval, request climate, charging, or door actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installed package can access Kia credentials, location data, and vehicle controls.

Mitigation: Install only if you trust the package; use read-only mode when vehicle commands are not needed and remove the local session when access is no longer wanted.

Risk: Door unlock and other commands can affect a real vehicle.

Mitigation: Require user confirmation for each command and enable door unlock only when needed.

Risk: Cached status or an accepted command can be mistaken for a confirmed vehicle state.

Mitigation: Refresh and re-read vehicle status when freshness or command outcome matters.

## Reference(s):

- [kiaaccess on ClawHub](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vehicle status may be cached; an accepted command does not confirm a vehicle state change.]

## Skill Version(s):

2.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
