## Description:

Query and control a SimpliSafe alarm system from the shell with curl, including system state, sensors, locks, events, settings, arming, disarming, and lock control after one-time browser login setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query SimpliSafe alarm state, inspect sensors, locks, events, and settings, and issue confirmed shell commands that arm, disarm, lock, or unlock a real security system.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a physical alarm system and door locks, including disarming, arming, unlocking, and reading security state.

Mitigation: Require explicit user confirmation before commands that change arming state, unlock doors, or read sensitive alarm data, then re-read the specific state field to verify the result.

Risk: The SimpliSafe refresh token and cached access token effectively grant access to the user's alarm system.

Mitigation: Keep token files at restrictive permissions, avoid shared machines, protect TMPDIR token cache access, and revoke or rotate credentials if exposure is suspected.

Risk: Some settings endpoints can return alarm PINs in cleartext.

Mitigation: Prefer safe projections that omit PIN blocks and only retrieve PINs when the user explicitly asks for them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplisafe-mcp)
- [SimpliSafe curl + jq recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)
- [SimpliSafe API base](https://api.simplisafe.com/v1)
- [SimpliSafe OAuth token endpoint](https://auth.simplisafe.com/oauth/token)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can read account state and, with explicit confirmation, operate physical alarm and lock hardware.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
