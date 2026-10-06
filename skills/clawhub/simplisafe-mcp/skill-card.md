## Description:

Helps an agent check SimpliSafe alarm, sensor, lock, event, and settings data and, when requested, control alarm and door-lock state using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SimpliSafe account holders and their agents can inspect home security status, sensors, locks, and recent activity, or request alarm and door-lock changes. A one-time browser login provides the required refresh token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated commands can arm or disarm the alarm and lock or unlock doors without an enforced confirmation step.

Mitigation: Require explicit human confirmation before every alarm or lock state change; do not execute such commands speculatively.

Risk: Access to the SimpliSafe account uses a long-lived refresh token, and settings can expose alarm PINs in cleartext.

Mitigation: Protect and revoke the refresh token when needed, and require explicit human confirmation before reading PINs; return only requested settings.

Risk: A successful command response or cached lock reading may not reflect the actual physical state.

Mitigation: Re-read the specific state after an action, poll locks for a fresh reading, and check for jams before reporting success.

## Reference(s):

- [SimpliSafe command recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/simplisafe-mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May report account security status or propose actions affecting physical alarm and lock state.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
