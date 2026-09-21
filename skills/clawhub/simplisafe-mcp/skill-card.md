## Description:

Query and control a SimpliSafe alarm system from the shell with curl, including system state, sensors, locks, events, settings, arming, disarming, locking, and unlocking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SimpliSafe alarm status, inspect sensors and locks, review recent events, and run confirmed arm, disarm, lock, or unlock operations from an agent-guided shell workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can arm or disarm an alarm system and lock or unlock real doors.

Mitigation: Require explicit user confirmation before every arm, disarm, lock, or unlock command, and verify the resulting state with a fresh read.

Risk: The workflow handles SimpliSafe account credentials, cached access tokens, and endpoints that can expose alarm PINs in cleartext.

Mitigation: Use environment-based credentials or a private per-user secrets store, avoid shared TMPDIR token cache locations, and query PIN fields only when the user explicitly requests them.

Risk: Cached device state and asynchronous lock or alarm transitions can make a successful operation look failed or a failed operation look successful.

Mitigation: Poll the specific state field after writes, use forceUpdate when freshness matters, and avoid whole-object diffs for verification.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplisafe-mcp)
- [SimpliSafe curl + jq recipes](artifact/references/recipes.md)
- [SimpliSafe shell helpers](artifact/references/ss-helpers.sh)
- [SimpliSafe API base](https://api.simplisafe.com/v1)
- [SimpliSafe OAuth token endpoint](https://auth.simplisafe.com/oauth/token)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and jq commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, jq, a SimpliSafe OAuth refresh token, and explicit user confirmation before physical security actions.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
