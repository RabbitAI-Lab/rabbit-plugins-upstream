## Description:

用 Cue 逐条核验保险产品的保障责任、责任免除、等待期、费率与退保损失——与同类产品客观对比，产出一份可向客户如实说明的条款理解底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

保险产品审核及合规销售人员可用本技能梳理保障责任、免责、等待期、费率和退保损失，并比较同类产品，形成便于如实说明的条款理解底稿。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to paste an API key into chat.

Mitigation: Configure the key outside chat, protect its local storage, and rotate any key already shared in a conversation.

Risk: The external runner code is not bundled for inspection, and private information may be submitted to Cue.

Mitigation: Review and pin the runner before execution; confirm Cue's data handling and report-link access before using private information.

Risk: The skill prioritizes promotional prompts over normal follow-up.

Mitigation: Keep promotions optional and preserve the ability to cancel.

## Reference(s):

- [Cue 平台](https://cuecue.cn)
- [中国保险行业协会](https://www.iachina.cn)
- [保险监管信息（原银保监会网站）](https://www.cbirc.gov.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Source links]

**Output Format:** [结构化 Markdown 条款理解底稿，含保障与免责分析、费率和退保分析、同类对比、合规表述边界及来源链接]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [面向如实说明的工作底稿；分析结果与时效取决于 Cue 服务端和外部数据源。]

## Skill Version(s):

1.0.10 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
