## Description:

Helps users check Kia vehicle status, location, and charging and request confirmation-gated vehicle commands through their Kia Access account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Kia owners use this skill to ask an agent about their vehicle's status, location, and EV charging, and to approve climate, charging, or door commands for a selected vehicle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vehicle location and Kia account data are sensitive.

Mitigation: Install only when comfortable granting access; keep passwords, remember-me tokens, and session files out of chat and shared logs.

Risk: Vehicle commands can change climate, charging, or door lock state; unlocking leaves the vehicle unsecured.

Mitigation: Use read-only mode unless writes are needed, restrict write permissions to the required actions, and confirm the selected vehicle and user approval before each command.

Risk: An accepted command or cached status may not reflect the vehicle's current state.

Mitigation: Re-read vehicle status to verify changes; do not resend a command merely because confirmation times out.

## Reference(s):

- [kiaaccess on ClawHub](https://clawhub.ai/chrischall/skills/kiaaccess)
- [kiaaccess-mcp npm package](https://www.npmjs.com/package/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown and structured vehicle tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Vehicle commands require user confirmation; reported command acceptance does not necessarily confirm the vehicle changed state.]

## Skill Version(s):

2.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
