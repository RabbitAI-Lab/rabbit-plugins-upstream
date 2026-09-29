## Description:

Provides shell-based guidance to check SimpliSafe alarms, sensors, locks, events, and settings, and to arm, disarm, lock, or unlock devices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SimpliSafe account holders and their agents use this skill to inspect system status and device activity or, with explicit approval, change alarm and lock states.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored credentials give the agent access to the SimpliSafe account.

Mitigation: Use a private environment, keep the refresh token out of shared workspaces, and set TMPDIR to a private 0700 directory.

Risk: Alarm and lock commands can change physical security without an enforced confirmation gate.

Mitigation: Require explicit user confirmation before arming, disarming, locking, or unlocking, and verify the resulting device state.

Risk: Settings routes may expose alarm PINs in cleartext.

Mitigation: Avoid PIN-retrieval routes unless specifically needed and limit settings output to the requested fields.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/simplisafe-mcp)
- [SimpliSafe command recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with shell commands and human-readable API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SimpliSafe account, a browser-issued refresh token, curl, and jq.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
