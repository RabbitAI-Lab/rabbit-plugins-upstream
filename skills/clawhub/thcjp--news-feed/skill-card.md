## Description:

Fetches and filters current headlines from major RSS feeds such as BBC, Reuters, AP, Al Jazeera, NPR, and The Guardian, with optional deduplication and summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research or content teams use this skill to collect RSS news items, filter by source, keyword, and time range, deduplicate overlapping stories, and produce concise news briefs or structured exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags broad command execution and file-writing behavior that is not clearly scoped to RSS headline aggregation.

Mitigation: Install only after review, require explicit approval for command execution, and use explicit output paths for any file export.

Risk: The skill references API key configuration even though public RSS fetching should usually not require sensitive credentials.

Mitigation: Do not provide API keys unless a specific workflow requires them and the purpose is understood.

Risk: RSS fetching depends on external feeds and network access, so sources can be unavailable, stale, or inconsistent.

Mitigation: Check returned source-response metadata, retry failed feeds, and verify important stories against the linked publisher pages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/news-feed)
- [BBC News RSS feed](http://feeds.bbci.co.uk/news/rss.xml)
- [Reuters Top News RSS feed](https://feeds.reuters.com/reuters/topNews)
- [Associated Press RSS feed](https://feeds.apnews.com/rss/apf-topnews)
- [Al Jazeera RSS feed](https://www.aljazeera.com/xml/rss/all.xml)
- [NPR News RSS feed](https://feeds.npr.org/1001/rss.xml)
- [The Guardian World RSS feed](https://www.theguardian.com/world/rss)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON news lists with titles, links, timestamps, summaries, source labels, and optional export commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May export structured results to explicit JSON or Markdown paths when requested.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
