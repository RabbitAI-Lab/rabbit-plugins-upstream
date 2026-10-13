## Description:

根据公开招投标数据生成客户采购背景调查报告，梳理采购习惯、预算规模、供应商关系、竞争格局及公开风险，支持单一客户分析和双单位对比。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dragonzu](https://clawhub.ai/user/dragonzu)

### License/Terms of Use:

MIT-0

## Use Case:

销售和商务拓展人员在拜访或投标前，使用公开招投标记录了解潜在客户的采购历史、供应商及竞争状况，并获得附有来源的调查报告。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: 免费试用注册会向服务提供方提交设备指纹。

Mitigation: 仅在知情同意后注册；自行配置 ZLBX_API_KEY 可跳过自动注册。

Risk: 本地保存的 API 凭证可能被其他有权读取该配置的程序使用。

Mitigation: 限制 ~/.zlbx/config.json 的访问权限，避免分享配置文件或在报告中暴露凭证。

Risk: 生成的 HTML 报告可能包含可访问企业记录的签名链接。

Mitigation: 仅向预期收件人分享报告，并在转发前检查报告中的链接与内容。

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/dragonzu/skills/client-background-check)
- [知了标讯技能文档](https://ai.zhiliaobiaoxun.com/docs/skill)
- [调查工作流](artifact/references/workflow.md)
- [报告模板](artifact/references/report-template.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML report]

**Output Format:** [带来源链接的中文调查报告，可另行导出 HTML 文件]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [支持单客户分析与双单位对比；报告可能包含可分享的签名访问链接。]

## Skill Version(s):

1.0.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
