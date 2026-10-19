## Description:

Helps agents retrieve and summarize Douyin creators' published videos, image/text posts, and short-drama series through SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, marketers, and developers use this skill to review Douyin creators' posts and series, track recent publishing, and compare content and engagement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The suggested command runs the latest published npm package with the user's SocialDataX API key available.

Mitigation: Use a pinned, reviewed package version or a preconfigured MCP tool in sensitive environments; provide the API key only to a trusted runtime.

Risk: Unbounded pagination can consume substantial API credits.

Mitigation: Set page or item limits and avoid --all unless broad retrieval and its credit use are intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-videos)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Analysis, JSON]

**Output Format:** [Markdown summaries or structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include creator posts or series, engagement metrics, media links, and pagination status.]

## Skill Version(s):

0.1.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
