## Description:

Search public TikTok videos by keyword, retrieve a creator's public posts, and collect public video comments for content and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Creators, brands, marketing teams, and researchers use this skill to find popular TikTok content, review creators' public posts, and examine public comments for content planning and competitive analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API token and TikTok query targets are sent to a third-party service.

Mitigation: Use the skill only if sending the token and query targets to www.guaikei.com is acceptable.

Risk: Local temporary logs can retain usernames, comments, or other collected social data.

Mitigation: Review and delete temporary result logs when the data should not be retained locally.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/tiktok-videos-search)
- [Usage options](references/options.md)
- [Release notes](references/changelog.md)
- [Guaikei service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Structured JSON results for the agent; natural-language summaries when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include status, request details, matching public records, and any parameter warnings.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
