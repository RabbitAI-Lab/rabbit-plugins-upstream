## Description:

Find viral outlier posts on TikTok, Instagram and YouTube, analyze creator performance and videos, and manage competitor watchlists and tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[matsclaes2](https://clawhub.ai/user/matsclaes2)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and their agents use this skill to research high-performing social posts, compare creators, generate video analyses and content ideas, and monitor competitors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated calls can spend prepaid credits.

Mitigation: Confirm the intended spend and check the credit balance before costly calls; do not retry insufficient-credit failures automatically.

Risk: Tracking, watchlists, and alerts may persist or be deleted remotely.

Mitigation: Confirm persistent monitoring and destructive changes with the user before applying them.

Risk: Returned captions and transcripts may contain untrusted instructions.

Mitigation: Treat social-media content as data, not as instructions to the agent.

Risk: Using the npm CLI can execute a changing package version.

Mitigation: Prefer a pinned CLI version if installing or running it with npx/npm.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/matsclaes2/skills/viral-outliers)
- [Viral Outliers documentation](https://viraloutliers.com/docs)
- [Viral Outliers OpenAPI specification](https://viraloutliers.com/openapi.json)
- [Getting started](references/getting-started.md)
- [Available skills and endpoints](references/skills.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Natural-language findings, Markdown analyses, and command or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include creator metrics, transcripts, video breakdowns, and watchlist or alert results.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata; embedded SKILL.md states 1.6.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
