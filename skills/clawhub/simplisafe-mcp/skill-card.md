## Description:

Helps agents check SimpliSafe alarm, sensor, lock, and event status and issue alarm or lock commands through the shell.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

SimpliSafe account holders and their agents can inspect home security status and, with explicit authorization, arm or disarm the alarm and control door locks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated commands can disarm the alarm or unlock doors without an enforced confirmation step.

Mitigation: Require explicit human confirmation before every arm, disarm, lock, or unlock action; prefer a version that enforces write confirmation and restricts allowed actions.

Risk: A long-lived refresh token can grant ongoing account access if exposed in logs, shell history, or shared files.

Mitigation: Keep the token private and avoid exposing credentials in logs, shell history, or shared files.

Risk: The settings response can contain cleartext alarm PINs, and lock status can be stale after a write.

Mitigation: Request PINs only with explicit consent; exclude them from routine settings output and refresh lock status before reporting a change as complete.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/simplisafe-mcp)
- [SimpliSafe command recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON-query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an authenticated SimpliSafe account, curl, and jq.]

## Skill Version(s):

1.3.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
