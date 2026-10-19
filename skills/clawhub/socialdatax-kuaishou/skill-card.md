## Description:

Helps agents research Kuaishou trends, videos, comments, and creators using SocialDataX data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and content teams use this skill to find Kuaishou trends and videos, inspect creator profiles and posts, and analyze video comments and replies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unpinned npm package may change after review while using the user's SocialDataX API key.

Mitigation: Pin and review the package version, or use a locked internal install before use in sensitive environments.

Risk: Interrupted pagination may leave comment or reply research incomplete.

Mitigation: Preserve partial results, label them incomplete, and resume with the corresponding returned pagination token.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown summaries of Kuaishou data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source links, engagement counts, and notices of incomplete paginated results.]

## Skill Version(s):

0.1.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
