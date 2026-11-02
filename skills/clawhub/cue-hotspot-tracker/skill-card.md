## Description:

用 Cue 通常 5-10 分钟（最长约 15 分钟）实时扫描今日 A 股热点板块与近 24h 催化资讯，拆解盘中催化逻辑与受益方向；跑完自动生成「看板图」与「报告长图」，报告全文以 Cue 链接交付。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向关注 A 股盘中行情的市场参与者，用于追踪热点板块、梳理公开催化因素和资金流向，并生成便于查看的报告图表；内容用于信息参考，不构成投资建议。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Setup instructions ask the user to paste a Cue API key into chat while claiming the agent cannot view it.

Mitigation: Enter the key locally through Cue login or a protected secret input instead of chat; rotate any key already shared.

Risk: The skill runs an external Cue runner, and its version can affect execution risk.

Mitigation: Review the runner version before execution and use a trusted source.

Risk: Scheduled runs consume Cue credits each time they run.

Mitigation: Enable scheduling only when recurring credit use is acceptable, and disable it when no longer needed.

## Reference(s):

- [SOP schema](references/sop-schema.md)
- [Cue API key setup](https://cuecue.cn/api-key?src=clawhub-hotspot-tracker)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Images, Links]

**Output Format:** [Markdown research report, dashboard image, report image, and Cue report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The full report is delivered through a Cue link; scheduling is optional and requires user choice.]

## Skill Version(s):

1.0.12 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
