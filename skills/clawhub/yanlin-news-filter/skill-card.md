## Description:

Filters public finance news from Sina Finance to retain events likely to have material market impact.

This skill is ready for commercial/non-commercial use.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and finance analysts use this skill to fetch current public finance headlines, filter out low-impact items, score event importance, and map retained events to related sectors for market-monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill makes outbound requests to Sina Finance to retrieve current public news.

Mitigation: Run it only in environments where this network access is approved and disclose the external news source to users.

Risk: Keyword-based filtering may miss important events or rank routine headlines too highly.

Mitigation: Treat results as triage for market monitoring and review important outputs before using them for financial decisions.

Risk: The documented date argument is not implemented, so historical-date requests may still return current news.

Mitigation: Verify the returned date field and do not rely on the date argument for backtesting or historical research.

## Reference(s):

- [Sina Finance roll news feed endpoint](https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=30&page=1&r=0.1)
- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/yanlin-news-filter)

## Skill Output:

**Output Type(s):** [text, json, shell commands]

**Output Format:** [Plain text summary or JSON event list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns the current date, raw and filtered item counts, and up to 8 ranked events with title, source, importance, category, related sectors, and marginal-event flag.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
