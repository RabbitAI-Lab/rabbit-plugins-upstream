## Description:

Helps an agent check SimpliSafe alarm, sensor, lock, event, and settings information and, with user confirmation, arm or disarm the system or lock or unlock doors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SimpliSafe users can ask an agent to check home security status, sensors, locks, and recent activity, or to control the alarm and locks after explicitly confirming the action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent can disarm the alarm or unlock a real door, potentially leaving a home unprotected.

Mitigation: Require explicit user confirmation for every arm, disarm, lock, or unlock action; check the resulting device state.

Risk: The skill can expose cleartext alarm PINs and long-lived credentials, and its token cache may be accessible on a shared machine.

Mitigation: Avoid retrieving or displaying PINs unless specifically requested; use a single-user machine and a private TMPDIR or corrected token-cache location.

## Reference(s):

- [SimpliSafe shell recipes](references/recipes.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/simplisafe-mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report security-system status and propose or run user-confirmed control commands; responses may contain sensitive device information.]

## Skill Version(s):

1.2.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
