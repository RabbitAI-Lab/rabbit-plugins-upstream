## Description:

Retrieves public TikTok search results, creator posts, and video comments to support content research and audience analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and analysts use this skill to gather public TikTok videos, creator posts, and comments for content research, competitor monitoring, and audience insights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API token and TikTok search terms, profile URLs, video IDs, and request metadata are sent to Guaikei.

Mitigation: Use the service only if its data handling is acceptable; protect the token and avoid submitting sensitive inputs.

Risk: Public creator and comment records may contain personal data.

Mitigation: Handle returned data under applicable privacy rules and TikTok terms.

Risk: Result logs are saved to local temporary storage.

Mitigation: Restrict access to logs and delete them when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/tiktok-data-research)
- [Command options and output format](references/options.md)
- [Guaikei data service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Human-readable analysis or structured JSON records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [JSON records include status, request details, results, and warnings; runs also save temporary JSON logs.]

## Skill Version(s):

1.0.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
