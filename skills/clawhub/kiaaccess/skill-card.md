## Description:

Helps users check their Kia vehicle's status and location and request confirmation-gated climate, charging, and door commands through their Kia account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners and their assistants use this skill to check vehicle status, location, and charging and, with confirmation, control climate, charging, and door locks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials and refresh tokens could expose vehicle access if shared.

Mitigation: Keep credentials private and never share exported refresh tokens; use a trusted environment.

Risk: Vehicle controls can change climate, charging, or door-lock state; unlocking leaves the vehicle unsecured.

Mitigation: Use read-only mode when possible, enable door controls only when needed, and confirm every command with the user.

Risk: Cached status or an accepted command may not reflect the vehicle's current state.

Mitigation: Refresh and re-read vehicle status before relying on it; verify outcomes instead of repeating commands.

## Reference(s):

- [kiaaccess ClawHub release](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [Text, Configuration instructions, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vehicle readings may be cached; command acceptance does not guarantee the vehicle changed state.]

## Skill Version(s):

1.1.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
