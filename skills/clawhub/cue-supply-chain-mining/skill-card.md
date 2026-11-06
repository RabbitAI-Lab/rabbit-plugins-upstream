## Description:

根据公开信息梳理 A 股产业链上下游、景气传导与细分公司弹性，形成带来源链接和风险提示的研究报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向行业研究人员和个人投资者，围绕一条产业链梳理 A 股上下游公司、景气传导与细分企业线索，辅助开展进一步研究；不提供买卖时点建议。

### Deployment Geography for Use:

中国（A 股市场：沪深北）

## Known Risks and Mitigations:

Risk: Setup guidance asks users to paste a Cue API key into chat.

Mitigation: Configure CUE_API_KEY through secure secret or environment settings, and rotate any key already shared in chat.

Risk: Setup updates external runner code before running it; that implementation was not included in this artifact and remains unverified.

Mitigation: Pin and inspect the runner revision, and control subsequent updates.

## Reference(s):

- [Cue 平台](https://cuecue.cn)
- [Cue 示例研究报告](https://cuecue.cn/share/F8PzjKYbVBgYX2oN9clWB)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured Markdown research report with source links and risk notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One report per industry-chain query; findings depend on public information and source availability.]

## Skill Version(s):

1.1.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
