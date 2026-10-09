## Description:

Helps an agent check SimpliSafe alarm, sensor, lock, event, and system status and, with authorization, control alarms and locks using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SimpliSafe account holders and authorized operators can ask an agent to check alarm state, sensor and lock status, and recent events, or explicitly request arming, disarming, locking, or unlocking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated commands can disarm the alarm or unlock physical doors without an enforced confirmation gate.

Mitigation: Require explicit user confirmation before physical control commands; consider a separate read-only helper for routine checks.

Risk: A long-lived refresh token grants the agent access to the SimpliSafe account.

Mitigation: Protect the refresh token, limit agent access, and revoke it if exposed.

Risk: Settings responses may expose cleartext alarm PINs.

Mitigation: Request PIN data only when necessary and exclude the PIN block from ordinary settings queries.

Risk: A successful command response may not mean an alarm or lock changed state.

Mitigation: Re-read the relevant state, allowing for arming delays and fresh lock status updates.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/simplisafe-mcp)
- [SimpliSafe curl and jq recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell examples and command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live state may lag; verify physical control changes with a fresh status read.]

## Skill Version(s):

1.3.0 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
