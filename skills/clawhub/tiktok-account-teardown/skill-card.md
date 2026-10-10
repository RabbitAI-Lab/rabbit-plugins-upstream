## Description:

Retrieves public TikTok videos, creator posts, and comments to support account and competitor analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content marketers and analysts use this skill to research public TikTok posts, compare creator accounts, and summarize engagement and comment trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, profile URLs, video IDs, and the API token are sent to guaikei.com.

Mitigation: Use the skill only when sharing those inputs and the token with the provider is acceptable.

Risk: Locally saved result logs may contain public usernames, comments, and engagement metrics.

Mitigation: Review and remove sensitive result logs before sharing a machine or committing files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/tiktok-account-teardown)
- [Usage and options](references/options.md)
- [Guaikei API provider](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown analysis based on structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public video, creator, engagement, and comment data; successful queries also save JSON result logs locally.]

## Skill Version(s):

1.0.0 (source: ClawHub release, frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
