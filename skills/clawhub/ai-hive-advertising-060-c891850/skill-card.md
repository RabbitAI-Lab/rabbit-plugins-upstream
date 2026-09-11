## Description:

This Chinese-language skill guides agents through an AI-HIVE workflow for multi-grid advertising video production, including planning, sample generation, task tracking, and acceptance checks before any paid generation, bulk action, sending, or public publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand marketing, ecommerce, agency, retail, and content marketing teams use this skill to create AI-HIVE advertising video plans, samples, task records, and review checklists grounded in real product claims and audience needs. It helps agents query current AI-HIVE model and pricing information, prepare non-billable work orders, and require confirmation before paid generation or publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send credentials to an environment-selected MCP URL.

Mitigation: Prefer OAuth through the client UI, keep API keys in a secret store, and set AI_HIVE_MCP_URL only when the destination is fully trusted.

Risk: The skill can invoke remote AI-HIVE tools that may upload media or create paid generation tasks.

Mitigation: Require explicit confirmation before uploads, paid generation, bulk actions, sending, or public publishing; use read-only model and task queries for diagnostics.

Risk: Advertising outputs may rely on unsupported product claims or media without sufficient rights.

Mitigation: Maintain a product fact card, rights inventory, source-material boundaries, model parameters, task IDs, price snapshots, and acceptance checklist before delivery.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-060-c891850)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [多宫格生视频：原创实施卡](references/original-workflow.md)
- [AI-HIVE MCP 登录与绑定指南](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API-key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and local JSON work-order output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces plans, rights checklists, model-routing guidance, task records, acceptance checks, and optional local work-order JSON; paid generation and publishing require explicit confirmation.]

## Skill Version(s):

1.0.0 (source: evidence.json release.version and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
