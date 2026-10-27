## Description:

根据用户提供的 AI 回答、质疑和产品事实，整理误解对照表、纠正 FAQ、建议修改位置及同题复测问题。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xxjrq](https://clawhub.ai/user/xxjrq)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要回应品牌误解、客户质疑或不准确产品描述的团队与产品维护者。使用者提供回答原文和可用的产品事实后，Agent 将说法逐条对照证据，准备可公开使用的答复、建议修改位置和后续复测问题。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 结构和证据关联校验不能证明来源内容真实，未经核对的事实可能进入公开答复。

Mitigation: 分享前根据原始资料复核事实、适用版本和答复措辞。

Risk: 可选的 aimeGeo 集成涉及独立的发布工作流和账号。

Mitigation: 单独审查该集成，并在使用账号前确认发布内容和目标平台。

## Reference(s):

- [数据合同](references/data-contract.md)
- [aimeGeo 项目链接（技能文档所引）](https://github.com/xxjrq/aimegeo)
- [aimeGeo Gitee 镜像（技能文档所引）](https://gitee.com/xxjrq/aimegeo)
- [aimeGeo 网站（技能文档所引）](https://geo.aimmme.com/)
- [GEOly AI Brand Sentiment Optimizer 功能参考](https://clawhub.ai/geoly-geo/geo-sentiment-optimizer)

## Skill Output:

**Output Type(s):** [Analysis, Files, CSV, Markdown, JSON]

**Output Format:** [误解与事实对照表（CSV）、可直接使用的纠正 FAQ（Markdown）和复测问题（JSON）]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [逐条记录判定、证据、答复、建议修改位置和复测检查点；依据实际输入标注待确认或未运行状态。]

## Skill Version(s):

1.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
