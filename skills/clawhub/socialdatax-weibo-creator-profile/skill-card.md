## Description:

Looks up Weibo creator profiles, account details, audience size, and related profile information through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing Weibo creators can look up profiles by Weibo user ID or profile URL and review available account details and audience metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries send the selected Weibo ID or profile URL and attribution tags to SocialDataX, and may consume credits.

Mitigation: Only submit information appropriate to share with the service, check expected credit use, and use a reviewed, pinned CLI with only the credentials and local access it needs.

## Reference(s):

- [SocialDataX access information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-profile)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON profile data with a concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available fields may include creator name, profile IDs, bio, verification, follower and following counts, received likes, IP location, and gender.]

## Skill Version(s):

0.1.19 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
