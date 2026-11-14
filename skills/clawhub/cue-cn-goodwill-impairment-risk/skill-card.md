## Description:

将年报、半年报或收购公告中的商誉项目整理为逐项附原文引句与定位锚的八节台账，并仅照录披露金额和比例，不自行推算。

This skill is ready for commercial/non-commercial use.

## Publisher:

[huhoo](https://clawhub.ai/user/huhoo)

### License/Terms of Use:

MIT

## Use Case:

面向需要核对 A 股公司商誉披露的投资者、分析人员和财务从业者，用于将单份年报、半年报或收购公告中的余额、业绩承诺、减值测试假设及计提信息整理成可回查的台账。不用于判断减值可能性或计提充分性。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: ClawScan 将此技能评为中等置信度的可疑项：扫描报告指出远程服务发现和带认证的请求可能暴露 API 密钥，与技能所述的离线台账用途不一致；扫描未能解析部分引用，证据不完整。

Mitigation: 仅在有明确使用理由时安装；配置 CUE_API_KEY 前先检查远程服务示例及凭据发送位置，并将扫描结果视为不完整。

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huhoo/skills/cue-cn-goodwill-impairment-risk)
- [Cue MCP catalog](https://cuecue.cn/api/mcp-catalog)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [带原文引句、定位锚和来源编号的八节台账 Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [单份披露的结构化摘录；金额和比例照录原文，不自行计算。]

## Skill Version(s):

0.1.1 (source: ClawHub release, SKILL.md frontmatter, CHANGELOG.md; released 2026-11-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
