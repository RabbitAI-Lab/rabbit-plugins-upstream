## Description:

研林Skill — 公司公告采集+实质影响过滤，标注核心影响与标的价值

This skill is ready for commercial/non-commercial use.

## Publisher:

[caoling7878-arch](https://clawhub.ai/user/caoling7878-arch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and market-analysis agents use this skill to collect and filter Chinese public-company announcements from public finance and exchange disclosure sources, score materiality, classify direction, and return a concise filings digest for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill contacts public Chinese financial-information websites during execution.

Mitigation: Review and approve outbound network access before installation; use a runtime network allowlist for the disclosed Sina Finance, Shanghai Stock Exchange, and Shenzhen Stock Exchange sources where supported.

Risk: Fetched market and announcement data may be incomplete, stale, or misclassified by keyword scoring.

Mitigation: Use the output as a screening aid and verify material announcements against official exchange disclosures before relying on them for investment decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/caoling7878-arch/skills/yanlin-company-filings)
- [Sina Finance roll news API endpoint](https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.1)
- [Shanghai Stock Exchange disclosure announcements](http://www.sse.com.cn/disclosure/listedinfo/announcement/)
- [Shenzhen Stock Exchange disclosure announcements](http://www.szse.cn/disclosure/listedinfo/announcement/)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis]

**Output Format:** [JSON or plain text filings digest]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the run date, raw and filtered counts, top filtered filings, data sources, company, stock code, event, category, importance, direction, and sector.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
