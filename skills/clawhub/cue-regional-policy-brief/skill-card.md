## Description:

用 Cue 聚合指定区域的政策发布、招商动态及市场数据，筛选高价值合规线索与潜客名单，并产出结构化周度情报简报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External business development and legal operations teams use this skill to request regional policy, investment promotion, market, compliance lead, and prospect-list briefs for a target area. The agent runs the Cue regional-policy template and returns the generated Markdown report with source links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on an external cue-skills runner that may change outside this release.

Mitigation: Review the runner before installation, prefer a pinned commit or verified release, and run it with ordinary user privileges.

Risk: The workflow uses Cue API credentials and may process client or business-development information through Cue services.

Mitigation: Limit API key exposure, restrict report output locations, and avoid sensitive, regulated, or confidential data unless Cue's handling is approved.

Risk: Brief quality and timeliness depend on Cue service availability and external public data sources.

Mitigation: Preserve source links in reports, retry after service issues, and use the listed government and ministry sources for manual fallback.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-regional-policy-brief)
- [Cue report example](https://cuecue.cn/share/TRk4KUxsHw1y89JrEnsRH)
- [cue-skills runner source](https://github.com/sensedeal/cue-skills)
- [cue-skills Gitee mirror](https://gitee.com/sensedeal/cue-skills)
- [Cue API key page](https://cuecue.cn/hub/api-key)
- [China Government policy portal](https://www.gov.cn)
- [National Development and Reform Commission](https://www.ndrc.gov.cn)
- [Ministry of Commerce](https://www.mofcom.gov.cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown brief with source links and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Cue API key and the external cue-skills runner; optional Pandoc conversion can produce Word or PDF files.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
