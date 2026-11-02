## Description:

Searches public Douyin content and trends, retrieves creator posts, and returns structured data for video, comment, and account analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search public Douyin videos and image posts, check trending topics, retrieve creators’ public works and metrics, and analyze comments for content planning, competitor research, and trend monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and supplied links are sent to www.guaikei.com, and provider charges may apply.

Mitigation: Use a dedicated API token and confirm you trust the provider before sending searches or links.

Risk: Retrieved search, creator, and comment data remains in local logs/ until removed.

Mitigation: Review access to the log directory and remove stored results when they are no longer needed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/why20261/skills/douyin-data-assistant)
- [Guaikei API provider](https://www.guaikei.com)
- [CLI options](references/options.md)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON output envelope with public Douyin search, creator, trend, and comment data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output timestamps use Beijing time; retrieved results are also saved locally under logs/.]

## Skill Version(s):

1.4.0 (source: changelog, released 2026-10-22; package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
