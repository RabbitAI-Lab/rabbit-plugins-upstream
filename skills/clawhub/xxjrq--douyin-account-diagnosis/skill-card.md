## Description:

读取指定抖音账号的公开可见资料和作品样本，生成有证据、有时间范围、可解释的账号诊断与选题建议。用户要求分析抖音账号、对比近期作品、整理公开数据或制定今日选题时使用；不用于推断后台权重、限流原因或保证增长。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

抖音创作者和运营人员可用此技能检查指定账号近期公开作品的主题、发布频率和可计算互动表现，并据此整理有来源的诊断与选题建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial, and the skill points users to external downloads and installation instructions.

Mitigation: Review the linked download and setup instructions before installing, and treat the benign verdict as evidence rather than a guarantee.

## Reference(s):

- [EasyBR official download page](https://www.ebrower.com/down.html)
- [EasyBR v1.7.8 release](https://github.com/xxjrq/easybr/releases/tag/v1.7.8)
- [Easy WebBridge source and setup](https://github.com/xxjrq/easy-webbridge)
- [Easy WebBridge Gitee mirror](https://gitee.com/xxjrq/easy-webbridge)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Evidence-linked account diagnosis in JSON and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sample scope, reproducible metrics, prioritized findings, topic suggestions, evidence links, and limitations; analyzes only publicly visible account information.]

## Skill Version(s):

1.0.2 (source: package.json, manifest.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
