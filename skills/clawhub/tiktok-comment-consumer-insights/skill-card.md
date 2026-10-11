## Description:

Retrieves public TikTok videos, creator posts, and comments to help analyze audience questions, sentiment, and consumer feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Brands, marketers, researchers, and content creators use the skill to collect public TikTok search results, creator posts, and video comments for audience insight, competitor research, and content planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, target URLs or IDs, and the API token are sent to Guaikei.

Mitigation: Use the skill only when this third-party transmission is acceptable; avoid sensitive queries and protect the token.

Risk: Downloaded comments, nicknames, and identifiers may be personal data and can persist in local result logs.

Mitigation: Limit sharing of results and periodically delete temporary logs, especially for sensitive research.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/tiktok-comment-consumer-insights)
- [Usage and parameter guide](artifact/references/options.md)
- [Release notes](artifact/references/changelog.md)
- [Guaikei service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Analysis, Text, Shell commands, JSON data]

**Output Format:** [Markdown summaries and structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public TikTok data; results include status, request details, records, and warnings.]

## Skill Version(s):

1.0.0 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
