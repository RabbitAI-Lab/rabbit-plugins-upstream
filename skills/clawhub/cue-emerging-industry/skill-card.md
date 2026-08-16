## Description:

用 Cue 一键梳理陌生赛道的行业天花板、竞争格局与核心商业模式，同时映射 IPO/并购中常见的合规风险与法律争议点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, investors, and legal or diligence teams use this skill to build a fast research frame for emerging industries, including market ceiling, competitive landscape, business models, and common IPO or M&A compliance issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Industry topics and related prompt text are sent to Cue and external data sources through an external runner.

Mitigation: Avoid confidential deal names, non-public diligence facts, and sensitive client information unless organizational policy approves that use.

Risk: The resulting research depends on Cue service availability and external source quality.

Mitigation: Review generated reports and source links before relying on them for investment, IPO, M&A, or legal diligence decisions.

Risk: The skill requires installing and using an external Cue runner.

Mitigation: Review the external runner before first use and install only in environments approved for Cue access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/panting09266-ai/skills/cue-emerging-industry)
- [Publisher profile](https://clawhub.ai/user/panting09266-ai)
- [Cue](https://cuecue.cn)
- [Cue report example](https://cuecue.cn/share/770a002e0d43)

## Skill Output:

**Output Type(s):** [markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown research report with setup commands and troubleshooting guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The report can include source links and may be converted to Word or PDF with pandoc.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
