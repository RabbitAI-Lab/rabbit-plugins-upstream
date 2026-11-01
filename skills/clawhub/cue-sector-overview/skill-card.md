## Description:

根据行业名称与时间窗口，生成包含六个部分、带可比数据与来源锚点的 A 股行业景气报告，并标明数据覆盖缺口。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT

## Use Case:

供行业研究人员用于研究开题、会前准备和尽职调查中的行业章节，整理有来源锚点的行业景气证据。报告不提供荐股、择时或评级建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cue 连接检查可能将 API 密钥暴露给未获批准的目标地址。

Mitigation: 在凭据处理修正前使用不带 API 密钥的用户自备材料路径；启用 Cue 身份验证前，先确认 HTTPS 目标校验和重定向处理不会转发密钥。

## Reference(s):

- [ClawHub release page](https://clawhub.ai/huhoo/skills/cue-sector-overview)
- [Cue API key setup](https://cuecue.cn/hub/api-key)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)
- [六节报告骨架](artifact/references/section-skeleton.md)
- [政策时间线规格](artifact/references/policy-timeline.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [中文六节 Markdown 行业报告，附来源索引与运行记录。]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [逐项标注数据日期和来源锚点，申报覆盖缺口；不生成投资评级或荐股择时建议。]

## Skill Version(s):

0.1.30 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
