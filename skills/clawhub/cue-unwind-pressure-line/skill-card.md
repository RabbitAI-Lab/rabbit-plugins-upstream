## Description:

用 Cue 帮你看清被套的股票上方还有哪几道坎——从筹码分布定位套牢盘、用均线校验阻力强度、推演反弹每一步需要的量能，产出可复核的解套压力线底稿，辅助判断反弹到哪容易卡住、哪里该减仓。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Stockholders use this skill to review one stock's overhanging chip distribution, resistance levels, moving-average context, and rebound volume requirements in a structured report. It supports their assessment of where a rebound may encounter resistance; the skill describes analysis rather than promising an outcome or issuing buy/sell instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance asks users to paste a Cue API key into chat and gives conflicting assurances about agent access to it.

Mitigation: Configure the key locally through a protected mechanism and rotate any key already shared in chat.

Risk: Stock queries and optional holding costs are sent to Cue, and scheduled runs consume credits.

Mitigation: Review the information sent to Cue and enable schedules only for stocks and times explicitly selected by the user.

Risk: The skill downloads and runs an external Cue runner.

Mitigation: Review and pin the runner version before use.

## Reference(s):

- [Cue platform](https://cuecue.cn/)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-unwind-pressure-line)
- [Cue subscription](https://cuecue.cn/pay)
- [Cue skills runner repository](https://github.com/sensedeal/cue-skills)
- [Cue skills runner Gitee mirror](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown stock-analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes resistance and rebound-volume analysis with source links; conclusions depend on Cue and external market-data availability.]

## Skill Version(s):

1.0.1 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
