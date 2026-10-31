## Description:

通过 Cue 汇总全球宏观、国内政策与资金流向，生成包含股、债、商品配置逻辑和比例建议的月度报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

为财富顾问、投资顾问和投委会准备月度资产配置参考报告，汇总全球宏观及国内流动性信号并形成股、债、商品配置建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to send an API key in chat.

Mitigation: Configure the key locally instead of sharing it in chat, and rotate any key already shared.

Risk: The setup flow updates external runner code before execution.

Mitigation: Use a reviewed, fixed runner revision and control updates explicitly.

Risk: Queries are processed by Cue and reports receive share links.

Mitigation: Avoid including confidential client information in queries or reports.

## Reference(s):

- [Cue platform](https://cuecue.cn/)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-asset-allocation)
- [Cue runner source (as documented by the skill)](https://github.com/sensedeal/cue-skills)
- [Cue runner mirror (as documented by the skill)](https://gitee.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Structured Markdown monthly report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes macro conditions, domestic policy and liquidity, allocation reasoning and proportions, risks, and source links.]

## Skill Version(s):

1.0.11 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
