## Description:

Helps research Douyin trends, posts, comments, creators, and short-drama series using SocialDataX data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers, marketers, and developers use this skill to investigate Douyin trends, find posts and creators, and analyze post details, comments, replies, and creator series.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned npm package with the SocialDataX API key available can expose the key to changed package code.

Mitigation: Review the package before installing, pin it to a reviewed version, or run it in a restricted environment with only the required API key exposed.

Risk: Interrupted pagination or partial reply retrieval can produce incomplete analysis.

Mitigation: Retain partial results, report incompleteness, and resume with the appropriate parent or reply page token within the remaining page and item limits.

## Reference(s):

- [SocialDataX Douyin skill on ClawHub](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown responses with Douyin data summaries and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only data lookups; paginated results may be incomplete and require continuation.]

## Skill Version(s):

0.1.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
