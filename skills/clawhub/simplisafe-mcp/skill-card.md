## Description:

Query and control a SimpliSafe alarm system from the shell with curl -- read system state, sensors, locks, events and settings, and arm/disarm or lock/unlock.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SimpliSafe alarm status, inspect sensors, locks, events, and settings, and prepare shell commands for controlled alarm or lock operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable high-impact operations on a physical security system, including disarming alarms and unlocking doors.

Mitigation: Require explicit user confirmation before any disarm, unlock, arm, or lock operation, and re-read the relevant system or lock state after the command.

Risk: The skill uses persistent SimpliSafe credentials and can expose sensitive alarm data, including cleartext PINs when requested.

Mitigation: Protect the refresh token, revoke it if the machine or account may be compromised, and avoid PIN-reading requests unless the user explicitly asks for the codes.

Risk: The security scan verdict is suspicious because the skill has broad activation and high-impact access to alarms, locks, and account data.

Mitigation: Install only in environments where the agent is trusted to operate SimpliSafe from the shell, and review the bootstrap script before running it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplisafe-mcp)
- [SimpliSafe curl + jq recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, jq, and a SimpliSafe OAuth refresh token for live API use.]

## Skill Version(s):

0.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
