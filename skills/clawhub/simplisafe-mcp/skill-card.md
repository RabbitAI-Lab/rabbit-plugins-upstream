## Description:

Query and control a SimpliSafe alarm system from the shell with curl, including system state, sensors, locks, events, settings, and arm/disarm or lock/unlock actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect SimpliSafe alarm state, sensor health, lock state, events, and settings from an agent-assisted shell workflow. It can also propose or run authenticated commands that arm, disarm, lock, or unlock real home-security devices when the user explicitly confirms the action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can arm or disarm a physical alarm system and lock or unlock real doors.

Mitigation: Confirm user intent before any write action and re-read the specific alarm or lock state after the command before treating it as successful.

Risk: SimpliSafe refresh tokens, cached access tokens, and cleartext PIN payloads can expose home-security control or alarm codes.

Mitigation: Use the skill only on trusted machines, prefer a private TMPDIR or XDG_RUNTIME_DIR, harden token-cache storage, and avoid requesting PIN payloads unless the user explicitly asks for them.

Risk: Cached or delayed device state can make lock, sensor, or alarm status look fresher or more successful than it is.

Mitigation: Use fresh reads when freshness matters, poll lock state long enough for the device to report, and verify specific fields rather than diffing whole API objects.

## Reference(s):

- [SimpliSafe curl + jq recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplisafe-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that call the SimpliSafe API through curl and jq; write actions require explicit user confirmation and follow-up state verification.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
