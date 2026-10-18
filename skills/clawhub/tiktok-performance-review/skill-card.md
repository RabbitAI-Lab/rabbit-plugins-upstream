## Description:

Retrieves public TikTok posts, creator activity, and comments for content-performance reviews and social listening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, brands, marketing teams, and researchers use the skill to review public TikTok content performance, compare creators, and summarize comment trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The GUAIKEI service receives the API token and TikTok search terms, URLs, or video IDs.

Mitigation: Use only with approved credentials and research targets; avoid sending sensitive queries.

Risk: Fetched public results are retained in temporary local JSON logs.

Mitigation: Remove temporary logs after use if local retention is a concern.

Risk: Public comments and creator details may be included in shared reports.

Mitigation: Check redistribution rights and redact identifying details before external publication.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/tiktok-performance-review)
- [GUAIKEI service](https://www.guaikei.com)
- [Skill parameter guide](references/options.md)

## Skill Output:

**Output Type(s):** [Data, Analysis, Guidance]

**Output Format:** [Structured JSON results and Markdown summaries or tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only public TikTok search, creator-post, and comment data; reports empty results and parameter warnings.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
