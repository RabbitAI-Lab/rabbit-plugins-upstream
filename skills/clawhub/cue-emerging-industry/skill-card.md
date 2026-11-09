## Description:

用 Cue 梳理陌生赛道的行业天花板、竞争格局与核心商业模式，并映射 IPO 和并购中常见的合规风险与法律争议点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

投资、IPO 辅导及并购尽调人员可用它快速建立新兴产业认知，梳理市场空间、竞争格局、商业模式和相关合规争议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests an API key in chat, which can expose the credential.

Mitigation: Provide the key through a protected local secret entry instead of chat, and rotate it if it has already been shared.

Risk: The external runner and its dependencies can update without review, and the runner's complete behavior is not established by the artifact review.

Mitigation: Review and pin the runner and its dependencies before allowing execution or updates.

Risk: Research queries are sent to Cue and reports receive share links, which may expose confidential work.

Mitigation: Use only information suitable for the service and confirm the intended audience before sharing report links.

## Reference(s):

- [Cue 平台](https://cuecue.cn)
- [中国政府网](https://www.gov.cn)
- [工业和信息化部](https://www.miit.gov.cn)
- [艾瑞咨询](https://www.iresearch.cn)
- [36氪研究院](https://research.36kr.com)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Structured Markdown research report with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Organized into industry overview, market ceiling, competition, business models, and compliance risks.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
