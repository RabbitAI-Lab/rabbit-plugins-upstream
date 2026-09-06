## Description:

面向品牌市场、电商商家、广告公司、门店和内容营销团队，这个 Skill 通过 AI-HIVE MCP 查询实时模型与价格，并生成围绕真实卖点和受众洞察的开箱测评种草广告视频计划、素材和验收清单。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

品牌市场、电商商家、广告公司、门店和内容营销团队 use this skill to plan and generate original AI-HIVE advertising assets for unboxing review and recommendation videos. It helps produce a work order, selling-point evidence table, creative direction, scripts, key frames, final video variants, task records, and compliance checks while requiring confirmation before paid generation or publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses credentials for a remote AI-HIVE MCP service, and credential handling is broader than the advertised advertising workflow.

Mitigation: Prefer OAuth through a trusted MCP client, keep API keys in a secret store, avoid setting AI_HIVE_MCP_URL unless reviewed, and never place tokens or API keys in prompts, screenshots, logs, or the repository.

Risk: AI-HIVE generation, upload, batch, sending, or public publishing actions may incur cost or expose user-provided materials.

Mitigation: Require separate user confirmation before any paid generation, upload, batch action, sending, or public publishing, and verify model pricing and parameters at runtime before proceeding.

Risk: Remote model availability, pricing, limits, and long-running task state can change between planning and execution.

Mitigation: Query ai_hive_list_models before generation, record the price snapshot and taskId, and use ai_hive_get_task to check the original task before retrying after a timeout.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-090-77ba653)
- [AI-HIVE workbench](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [Original workflow card](artifact/references/original-workflow.md)
- [MCP binding guide](artifact/references/mcp-binding.md)
- [OAuth MCP configuration example](artifact/references/mcp-config.example.json)
- [API-key MCP configuration example](artifact/references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and generated local JSON work orders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE task identifiers, model and price snapshots, rights checklists, and acceptance criteria when the user confirms runtime actions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
