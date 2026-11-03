## Description:

用 Cue 逐条核验保险产品的保障责任、责任免除、等待期、费率与退保损失，并与同类产品客观对比，产出可向客户如实说明的条款理解底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向保险产品审核人员及合规销售团队，用于核验产品条款、客观比较同类产品，并整理可向客户如实说明的要点与表述边界。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup workflow can automatically update and execute a runner that uses credentials.

Mitigation: Review and pin a fixed runner revision, disable automatic pulls before installation, and retain the ability to stop runs.

Risk: Product queries are sent to Cue and reports are available through hosted links, which could expose private client information.

Mitigation: Do not include private client information in queries or reports.

Risk: The Cue API key is used by the skill and its local configuration could be exposed.

Mitigation: Use a dedicated Cue key and protect its configuration file.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/panting09266-ai/skills/cue-insurance-policy-check)
- [Cue platform](https://cuecue.cn/)
- [Cue API key management](https://cuecue.cn/api-key?src=clawhub-insurance-policy-check)
- [中国保险行业协会](https://www.iachina.cn)
- [国家金融监督管理总局](https://www.cbirc.gov.cn)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [结构化 Markdown 条款理解底稿，附来源链接]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [涵盖保障责任、免责、等待期、费率、退保损失、同类产品对比及合规表述边界；结论取决于 Cue 服务与外部数据源。]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
