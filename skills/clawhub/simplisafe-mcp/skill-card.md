## Description:

Helps an agent check SimpliSafe alarm, sensor, lock, event, and settings information and, with user approval, arm or disarm the system and lock or unlock doors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SimpliSafe account holders use this skill to ask an agent about home security status and device activity, or to request explicit changes to alarm and door-lock states.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated commands can disarm the alarm or unlock a door without a technical confirmation gate.

Mitigation: Require explicit user review and approval before arming, disarming, locking, or unlocking; verify the resulting state.

Risk: A refresh token grants persistent access to the SimpliSafe account.

Mitigation: Protect the refresh token and give agent access only when authenticated security-system control is intended.

Risk: Reading settings can disclose alarm PINs in cleartext.

Mitigation: Exclude PIN fields from routine responses and retrieve them only when explicitly requested.

## Reference(s):

- [SimpliSafe curl and jq recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/simplisafe-mcp)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated SimpliSafe account; device changes require user confirmation.]

## Skill Version(s):

1.3.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
