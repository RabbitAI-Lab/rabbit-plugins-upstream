## Description:

新闻 aggregates domestic and international news across social, technology, military, finance, sports, and international topics, then filters, deduplicates, summarizes, and organizes the results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation workflows use this skill to track news topics, create daily briefs, follow events over time, analyze public sentiment, and export structured summaries for review or downstream processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News topics and keywords may be sent to external news, search, or social-trending sources.

Mitigation: Avoid sensitive private investigations, confidential business topics, secrets, and other private material in queries.

Risk: Some news sources may require API keys or other credentials.

Mitigation: Keep credentials in environment variables and do not place them in files or chats.

Risk: Generated summaries, scores, sentiment labels, and timelines can be incomplete, delayed, or misleading if source coverage is limited.

Mitigation: Verify important facts against original source links and compare multiple independent sources before acting on the output.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance, configuration]

**Output Format:** [Markdown briefs or structured JSON summaries with source links, categories, scores, timelines, and extracted entities.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports query, date range, categories, language, max results, output format, content, and style inputs.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
