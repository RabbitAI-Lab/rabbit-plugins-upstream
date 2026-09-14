## Description:

用 Cue 一键梳理陌生赛道的行业天花板、竞争格局与核心商业模式，同时映射 IPO/并购中常见的合规风险与法律争议点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Business, investment, IPO advisory, and M&A diligence users use this skill to quickly build a research frame for emerging industries, including market ceiling, competitive landscape, business models, and common compliance issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external Cue runner is installed from mutable repositories and may access local files and credentials.

Mitigation: Review the runner source before installation, prefer a pinned and verified revision, and use a narrowly scoped Cue API key.

Risk: Generated reports depend on Cue service availability and external data sources, so results may be incomplete or outdated.

Mitigation: Treat generated reports as untrusted research output, verify cited sources, and rerun health checks before relying on time-sensitive findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-emerging-industry)
- [Cue sample report](https://cuecue.cn/share/770a002e0d43)
- [Cue API key](https://cuecue.cn/hub/api-key)
- [Cue runner source](https://github.com/sensedeal/cue-skills)
- [Cue runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown research report with optional Word or PDF conversion commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report is generated through the external Cue service and may include source links.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
