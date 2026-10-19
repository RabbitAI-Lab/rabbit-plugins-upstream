## Description:

Helps agents research Weibo trends, posts, comments, engagement, and creator profiles using SocialDataX data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and analysts use this skill to review Weibo hot searches, find posts, examine comments and replies, assess engagement, and explore creator profiles and posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unpinned npm package runs with the user's SocialDataX API key available, so later package updates may change its behavior.

Mitigation: Review and pin an exact package version before execution; install only if the package is trusted.

Risk: Automatic dependency restoration may install or execute code without explicit user review.

Mitigation: Require user approval before installing or restoring dependencies.

## Reference(s):

- [SocialDataX Weibo skill on ClawHub](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with CLI examples and summaries of retrieved data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups; partial results should retain their pagination state.]

## Skill Version(s):

0.1.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
