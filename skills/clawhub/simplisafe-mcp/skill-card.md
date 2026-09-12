## Description:

Query and control a SimpliSafe alarm system from the shell with curl: read system state, sensors, locks, events, and settings, and arm, disarm, lock, or unlock after a one-time browser login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect SimpliSafe alarm, sensor, lock, event, and settings state from an agent-accessible shell. It can also propose or run authenticated commands for arming, disarming, locking, and unlocking when the user confirms the action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate a physical home-security system, including disarming alarms and locking or unlocking doors.

Mitigation: Use only in a trusted local account and require explicit user confirmation before every arm, disarm, lock, or unlock action.

Risk: SimpliSafe settings can expose alarm PINs in cleartext.

Mitigation: Avoid requesting PIN data unless the user explicitly asks for it, and prefer settings queries that exclude the PIN block.

Risk: Access tokens are cached under $TMPDIR.

Mitigation: Review and harden or disable the token cache before deployment in shared or less trusted environments.

Risk: A successful HTTP response does not always prove a physical action completed.

Mitigation: Re-read the specific alarm or lock state after any write and account for exit-delay and lock-reporting latency.

Risk: The one-time authentication flow depends on an external bootstrap-auth.mjs source that was not included in the artifact.

Mitigation: Verify the bootstrap-auth.mjs source before using it to mint or store a refresh token.

## Reference(s):

- [SimpliSafe API recipes](artifact/references/recipes.md)
- [SimpliSafe shell helpers](artifact/references/ss-helpers.sh)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplisafe-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command output interpretation, confirmation prompts for physical security actions, and credential setup guidance.]

## Skill Version(s):

0.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
