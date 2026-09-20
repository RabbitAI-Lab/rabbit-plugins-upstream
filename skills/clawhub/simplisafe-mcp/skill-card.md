## Description:

Query and control a SimpliSafe alarm system from the shell with curl, including reading system state, sensors, locks, events, and settings, and arming, disarming, locking, or unlocking after a one-time browser login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SimpliSafe alarm, sensor, lock, event, and settings state from an agent-accessible shell. It can also guide authenticated arm, disarm, lock, and unlock operations when the user explicitly confirms the physical-security action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated commands can disarm monitoring, arm a system that may trigger a siren or dispatch, or lock and unlock real doors.

Mitigation: Require explicit user confirmation before arm, disarm, lock, or unlock actions, and re-read the relevant status after each write.

Risk: Long-lived refresh tokens and cached access tokens can expose SimpliSafe account access on shared or weakly protected hosts.

Mitigation: Keep the refresh token in a protected user-only location, use a private TMPDIR or token cache, and avoid running the skill on shared hosts.

Risk: Settings calls can return cleartext alarm PINs.

Mitigation: Do not request PIN payloads unless the user explicitly asks for them; query non-PIN settings projections by default.

Risk: Cached or delayed device state can make a write look successful or failed incorrectly.

Mitigation: Poll and re-read specific status fields after writes, and use fresh lock reads when state freshness matters.

## Reference(s):

- [SimpliSafe curl + jq recipes](artifact/references/recipes.md)
- [SimpliSafe shell helpers](artifact/references/ss-helpers.sh)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplisafe-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include jq filters and explicit confirmation and verification steps before physical-security writes.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
