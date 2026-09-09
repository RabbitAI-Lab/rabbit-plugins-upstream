## Description:

Query and control a SimpliSafe alarm system from the shell with curl, including system state, sensors, locks, events, settings, arming, disarming, locking, and unlocking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with a SimpliSafe system use this skill to inspect alarm, sensor, lock, event, and settings data and to issue confirmed arm, disarm, lock, or unlock commands from an agent-assisted shell workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can control physical security actions such as disarming alarms and locking or unlocking doors.

Mitigation: Require explicit user confirmation before any arm, disarm, lock, or unlock request, then re-read the relevant state instead of assuming a 2xx response means the action completed.

Risk: The skill uses a long-lived SimpliSafe refresh token and caches access tokens locally.

Mitigation: Protect the refresh token and TMPDIR token cache, avoid shell tracing or logs that expose token commands, and use this only in a trusted local environment.

Risk: Settings responses can expose alarm PINs in cleartext.

Mitigation: Project non-PIN settings by default and request PIN data only after explicit user confirmation.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chrischall/skills/simplisafe-mcp)
- [SimpliSafe curl + jq recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, jq, and a SimpliSafe OAuth refresh token; helper commands return response bodies and non-2xx failures explicitly.]

## Skill Version(s):

0.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
