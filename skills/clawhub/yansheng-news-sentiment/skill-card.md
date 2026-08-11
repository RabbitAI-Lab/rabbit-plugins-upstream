## Description:

Analyzes public finance news for selected stock codes using simple rule-based sentiment scoring and event summaries.

This skill is for demonstration purposes and not for production usage.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Students, educators, and developers use this skill to collect public finance-news signals for selected stock codes and produce a classroom-oriented sentiment summary. It is not suitable as the sole basis for investment, compliance, or reputation decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rule-based sentiment scores and fixed percentage math can be misleading if read as market intelligence.

Mitigation: Use the output only for classroom or demonstration workflows unless the analyzer is replaced and independently validated.

Risk: Network fetch failures fall back to synthetic article counts, which can hide missing or stale source data.

Mitigation: Verify the underlying news source and source availability before relying on any generated summary.

Risk: Finance-news sentiment can be misused as investment, compliance, or reputation advice.

Mitigation: Pair results with human review and independent evidence, and do not use the skill as the sole basis for consequential decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/yansheng-news-sentiment)
- [Publisher profile](https://clawhub.ai/user/caoling7878-arch)
- [Sina Finance stock news source](https://finance.sina.com.cn/realstock/company/{code}/nc.shtml)

## Skill Output:

**Output Type(s):** [text, json]

**Output Format:** [Plain text report or JSON object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes article count, sentiment distribution, sentiment score, label, hot topics, and key events when available.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
