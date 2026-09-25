## Description:

Query and control a SimpliSafe alarm system from the shell with curl: read system state, sensors, locks, events, and settings, and perform requested arm, disarm, lock, or unlock actions after setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect SimpliSafe alarm status, sensors, locks, events, and settings from shell workflows. It can also help perform explicitly requested arming, disarming, locking, and unlocking actions after confirming intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform live alarm and lock changes without an enforced confirmation gate.

Mitigation: Use read-only queries by default and require explicit user confirmation before arm, disarm, lock, or unlock commands.

Risk: SimpliSafe refresh tokens and cached access tokens grant access to a live security system if exposed.

Mitigation: Protect SIMPLISAFE_REFRESH_TOKEN and token cache files, keep credential files private, and avoid shared or untrusted shell environments.

Risk: A successful HTTP response may not prove that an alarm or lock state changed as intended.

Mitigation: Re-read the specific alarm or lock state after a change, request fresh lock state when needed, and treat unconfirmed results as failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/simplisafe-mcp)
- [SimpliSafe curl + jq recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live SimpliSafe API calls that require credentials and explicit user confirmation for control actions.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
