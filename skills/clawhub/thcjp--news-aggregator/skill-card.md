## Description:

This skill aggregates domestic and international technology, military, and social news, searches multiple sources, filters and deduplicates results, and returns structured summaries with source, time, key points, category, and confidence notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to request news aggregation over technology, military, social, industry, competitor, or event topics and receive a categorized digest with deduplication and source credibility notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad read/exec capability even though the release has no executable payload.

Mitigation: Review before installing and run it only with agent permissions you are comfortable granting.

Risk: The optional callback_url may transmit generated content outside the agent session.

Mitigation: Use callback_url only with trusted endpoints and avoid sensitive queries, credentials, or confidential source material unless the destination is clear.

Risk: News summaries can contain incorrect, stale, or unverified information, especially for military topics.

Mitigation: Cross-check important items against authoritative sources and filter anonymous or unconfirmed military information before relying on the output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/news-aggregator)
- [Declared homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown structured news summaries with optional shell environment setup snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries include title, link, source, time, key points, category grouping, and confidence notes when available.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 1.0.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
