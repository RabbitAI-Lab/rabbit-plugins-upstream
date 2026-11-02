## Description:

用 Cue 一键穿透企业的工商、股权、财务与经营全维基本面，评估业务模式与合作适配性，挖掘供应链金融与产业债机会，并产出可用于内部决策的尽调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

面向金融机构和企业业务团队，用于授信前初步尽调、客户准入、供应链金融机会分析和同业对标。它根据公开信息生成结构化尽调底稿，供内部决策参考；不能替代正式尽调，也不覆盖银行流水、合同等私有资料。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: 设置说明要求把 Cue API Key 粘贴到聊天中，可能导致密钥暴露。

Mitigation: 在聊天以外的本地配置中设置密钥并限制配置文件访问；如果密钥已经发到聊天中，请更换密钥。

Risk: 研究查询会发送给 Cue 和外部数据源，并可能消耗 Cue 积分。

Mitigation: 运行前检查查询中包含的信息，并留意积分消耗。

## Reference(s):

- [Cue 平台](https://cuecue.cn/)
- [Cue research runner（技能文档引用）](https://github.com/sensedeal/cue-skills)
- [国家企业信用信息公示系统](https://www.gsxt.gov.cn)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [带公开来源链接的结构化企业尽调 Markdown 底稿]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [按工商股权、经营、财务、司法合规、供应链金融机会、风险和待核实缺口组织；结论附来源链接。]

## Skill Version(s):

1.0.11 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
