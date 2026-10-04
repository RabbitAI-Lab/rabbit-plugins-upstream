## Description:

抖音定向舆情监测助手 retrieves public Douyin search results, hot榜 items, creator posts, and comments for keyword-based sentiment and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Content, marketing, operations, and data-analysis users can use this skill to collect public Douyin content, rankings, creator posts, and comments for topic research, competitor monitoring, trend tracking, and sentiment reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin keywords or links and the GUAIKEI_API_TOKEN to www.guaikei.com.

Mitigation: Use the skill only when that third-party data transfer is acceptable, and avoid submitting sensitive or unauthorized queries.

Risk: Results may include public user, creator, interaction, or comment metadata.

Mitigation: Collect only the amount of data needed for the task and handle exported results according to the user's privacy and retention requirements.

Risk: Generated logs may retain result data locally.

Mitigation: Periodically delete or protect the logs directory when outputs contain user or comment metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-sentiment-monitor)
- [Publisher profile](https://clawhub.ai/user/why20261)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [GUAIKEI API portal](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON envelopes with concise human-facing summaries and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results are emitted as JSON.]

## Skill Version(s):

1.3.0 (source: frontmatter and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
