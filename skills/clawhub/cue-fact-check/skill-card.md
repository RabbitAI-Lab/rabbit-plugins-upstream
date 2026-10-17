## Description:

使用 Cue 对新闻、研报和其他待核查内容进行多源交叉验证，生成包含原文对照、核查结论和纠偏证据的结构化报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

读者、研究人员和尽调人员可核查新闻、研报和经营数据中的数字、时间线及误导性表述，并查看证据来源。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs and updates an external Cue runner.

Mitigation: Review or pin the runner before use and approve updates deliberately.

Risk: Fact-check material is sent to Cue and the resulting report has a shareable link.

Mitigation: Submit only material suitable for that service and review sharing before distributing the link.

Risk: The Cue API key could be exposed or misused.

Mitigation: Have the user create and manage the key; keep it scoped and protected.

Risk: Optional Word or PDF conversion may request privileged package installation.

Mitigation: Avoid sudo installs unless the user explicitly needs conversion and approves the dependencies.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/panting09266-ai/skills/cue-fact-check)
- [Cue platform](https://cuecue.cn)
- [Cue runner linked in skill instructions](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Text]

**Output Format:** [Markdown fact-check report with claim-by-claim findings, supporting sources and a shareable report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report may be saved locally; Word or PDF conversion is optional.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
