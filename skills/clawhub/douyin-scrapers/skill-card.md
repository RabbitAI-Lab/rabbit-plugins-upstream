## Description:

Retrieves public Douyin search results, hot-list entries, creator posts, and comments as structured JSON for trend tracking, content research, competitor monitoring, and sentiment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to collect public Douyin data for short-video topic research, trend monitoring, competitor analysis, creator-post review, and comment analysis. It is intended for read-only data retrieval followed by downstream analysis or reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin search terms, public URLs or IDs, and the GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Install and run it only when that data transfer is acceptable, and keep the API token in a local environment variable.

Risk: Generated local logs may contain public comments, nicknames, account IDs, or business research.

Mitigation: Review, protect, and delete logs when they contain sensitive analysis or personal data from public Douyin content.

Risk: Public Douyin data may be subject to authorization, redistribution, or privacy constraints.

Mitigation: Use the tool only for public data and avoid public redistribution or commercial reuse unless the required authorization has been confirmed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-scrapers)
- [Server-resolved source repository](https://github.com/why20261/douyin-scrapers)
- [GuaiKei API site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Files, Text]

**Output Format:** [Structured JSON on stdout, diagnostics on stderr, and optional local JSON logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; supported commands retrieve search results, hot-list entries, creator posts, and comments.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
