## Description:

Analyzes public TikTok videos, creator posts, and comments through keyword search, creator retrieval, and video-comment collection, returning structured JSON for market research, competitor monitoring, topic discovery, and sentiment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, market researchers, and agent developers use this skill to retrieve public TikTok search results, creator works, and video comments for trend analysis, competitor monitoring, influencer research, topic discovery, and comment insight workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok search terms, target URLs or IDs, and GUAIKEI_API_TOKEN are sent to the third-party service www.guaikei.com.

Mitigation: Install and run the skill only when that data sharing is acceptable; keep the token in environment variables and avoid using sensitive research terms unless approved.

Risk: Successful runs save fetched public results as JSON files under the system temp directory.

Mitigation: Clear the generated temp logs when research topics, creator lists, or fetched comments are sensitive.

Risk: Fetched public TikTok comments and profile fields may include personal information such as nicknames and user-generated text.

Mitigation: Use the data for approved analysis workflows and redact or aggregate personal fields before sharing results externally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/tiktok-market-insight)
- [Publisher profile](https://clawhub.ai/user/why20261)
- [Guaikei API service](https://www.guaikei.com)
- [Parameter reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON envelopes on stdout, with human-facing Markdown guidance or analysis from the calling agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; progress and errors are written to stderr, and successful runs save result JSON files under the system temp directory.]

## Skill Version(s):

1.0.0 (source: server release, frontmatter, package.json, changelog released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
