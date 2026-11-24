## Description:

Garmin Connect integration for Clawdbot: sync fitness data (steps, HR, calories, workouts, sleep) every 5 minutes using OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lovefromio](https://clawhub.ai/user/lovefromio)

### License/Terms of Use:

MIT-0

## Use Case:

Clawdbot users can sync Garmin activity, sleep, and workout metrics for access in their scripts and scheduled workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance exposes account credentials and suggests weakening account protection; the local OAuth session also contains an account token.

Mitigation: Review the authentication steps before use, keep two-factor authentication enabled where possible, and protect the session file with restricted access.

Risk: Dependencies are not pinned, and the scan cannot determine whether installed versions are affected by cited advisories.

Mitigation: Review and pin dependency versions, then verify whether the cited advisories apply before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lovefromio/skills/garmin-connect)
- [Garmin Connect sign-in](https://sso.garmin.com/sso/signin)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Configuration instructions]

**Output Format:** [JSON fitness data and formatted Markdown text, with shell setup instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes locally cached personal activity, sleep, and workout metrics.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
