## Description:

Query and control a SimpliSafe alarm system from the shell with curl: read system state, sensors, locks, events, and settings, and arm, disarm, lock, or unlock devices after a one-time browser login.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect and operate a SimpliSafe home security system through shell commands. It is suited for checking alarm state, sensors, locks, events, and settings, and for deliberate arm, disarm, lock, and unlock actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a long-lived SimpliSafe refresh token and caches temporary access tokens locally.

Mitigation: Use only in an environment where the refresh token, .env file, and token cache are protected from other local users and processes; move the token cache to a private user-owned directory with atomic writes before routine use.

Risk: Write commands can arm, disarm, lock, or unlock a real physical security system.

Mitigation: Confirm user intent before running any write command and verify the resulting alarm or lock state after the API call.

Risk: Some settings endpoints may return alarm PIN codes in cleartext.

Mitigation: Avoid PIN-reading endpoints unless the user specifically needs those codes, and project only non-sensitive settings by default.

## Reference(s):

- [SimpliSafe curl and jq recipes](references/recipes.md)
- [SimpliSafe shell helpers](references/ss-helpers.sh)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash, curl, and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may call the SimpliSafe API and can affect a real alarm system or door locks.]

## Skill Version(s):

0.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
