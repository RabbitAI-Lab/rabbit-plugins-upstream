## Description:

借助 Cue 汇总企业的工商、股权、经营、财务与合规信息，生成附公开来源的预尽调底稿。

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

授信、客户准入和供应链金融团队可用它汇总公开企业资料，初步识别经营与财务风险、梳理合作机会；结果不替代正式尽调。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 安装时拉取并运行未固定版本的外部 Cue runner。

Mitigation: 在敏感环境中先审查 runner 并固定可信版本，再执行。

Risk: 企业研究查询会发送至 Cue，且 API Key 保存在本地。

Mitigation: 保护本地密钥；仅提交已获准向 Cue 分享的数据，避免未经批准的内部财务文件或客户隐私。

Risk: 公开数据可能不足以支持正式授信或尽调判断。

Mitigation: 核对原始出处与待核实缺口，并在决策前完成正式尽调。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/panting09266-ai/skills/cue-enterprise-panorama)
- [Cue 平台](https://cuecue.cn/)
- [Cue API Key 获取](https://cuecue.cn/api-key?src=clawhub-enterprise-panorama)
- [Cue runner（运行依赖，非技能来源证明）](https://github.com/sensedeal/cue-skills)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [附来源链接的结构化 Markdown 尽调底稿]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [涵盖工商股权、经营、财务、司法合规、融资机会、风险及待核实缺口；成功生成时附 Cue 原始报告链接。]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
