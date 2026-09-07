## Description:

帮助评估从 B612咔叽（B612）迁移生成式视觉任务到 AI-HIVE 的可行性，通过真实样本、实时模型查询、小样评分和回退条件形成迁移结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, creators, and developers use this skill to compare B612咔叽 visual-generation workflows with AI-HIVE using the same inputs, budget checks, model discovery, and acceptance criteria. It supports migration decisions for validated generative steps while preserving workflows that depend on third-party proprietary features, accounts, data, templates, or member benefits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE credentials could be sent to an environment-selected endpoint.

Mitigation: Prefer OAuth through the MCP client, avoid overriding AI_HIVE_MCP_URL, keep API keys in secret storage, and revoke any exposed credential immediately.

Risk: Private prompts, reference media, or paid generation requests may be sent to AI-HIVE.

Mitigation: Review each invocation before execution, confirm rights to input media, and require explicit budget approval before paid tools are called.

Risk: Retrying after a timeout can duplicate paid generation work.

Mitigation: Use the original taskId and query task status before submitting another paid request.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wubin1836/skills/ai-hive-cn-name-b612-kaji)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [B612咔叽 official Chinese-name source](https://www.b612kaji.com/)
- [中文名来源与去重](references/chinese-name-evidence.md)
- [AI-HIVE MCP 登录与绑定指南](references/mcp-binding.md)
- [B612咔叽迁移工作流](references/migration-workflow.md)
- [来源与品牌边界](references/source-and-boundary.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, MCP configuration examples, and optional JSON migration work-plan files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce a local migration-plan.json; paid AI-HIVE generation calls require explicit confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
