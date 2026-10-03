## Description:

Helps an agent inspect and control a SimpliSafe alarm system, sensors, and door locks using authenticated shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SimpliSafe users can ask an agent to check alarm status, sensors, locks, events, and settings, or to arm, disarm, lock, and unlock with their authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated commands can disarm the alarm or unlock physical doors without an enforced confirmation gate.

Mitigation: Require explicit user confirmation for each arm, disarm, lock, or unlock command and verify the resulting state.

Risk: The refresh token grants broad control over the security system.

Mitigation: Keep the token file private and revoke the token when the skill is no longer used.

Risk: Settings responses can expose alarm PINs in cleartext.

Mitigation: Avoid requesting PINs unless necessary and return only the settings fields needed for the request.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/simplisafe-mcp)
- [SimpliSafe command recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require authenticated SimpliSafe access; physical security changes require explicit user confirmation.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
