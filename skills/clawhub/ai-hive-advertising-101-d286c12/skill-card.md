## Description:

Helps brand marketing, ecommerce, advertising, retail, and content teams plan and produce AI-HIVE ecommerce advertising visuals from product facts and audience insight, with model and price checks before paid generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External business and content teams use this skill to turn ecommerce product requirements into advertising plans, rights checklists, scripts, key frames, generated visual assets, task records, and acceptance checks. The workflow supports AI-HIVE MCP setup and model routing while requiring explicit confirmation before paid generation, bulk actions, sending, or public publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials could be sent to an untrusted endpoint if the MCP URL is overridden.

Mitigation: Prefer client-managed OAuth, keep the default AI-HIVE endpoint, store API keys only in secrets or environment variables, and do not set AI_HIVE_MCP_URL unless the destination is fully trusted.

Risk: AI-HIVE generation, uploads, bulk actions, sending, or public publishing may incur cost or expose user assets.

Mitigation: Review current models, prices, uploaded materials, task parameters, and rights status before approving any paid, bulk, send, or publish action.

Risk: Broad implicit invocation could start the workflow when the user did not intend to use AI-HIVE advertising generation.

Mitigation: Install and enable the skill only for AI-HIVE ecommerce advertising workflows, and require explicit confirmation before external tool calls beyond read-only model or task checks.

Risk: Advertising outputs may contain unsupported product claims or use assets without sufficient rights.

Mitigation: Maintain the product fact card and material rights checklist, verify claims against supplied evidence, and run the acceptance checklist before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-101-d286c12)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [Original workflow card](references/original-workflow.md)
- [MCP login and binding guide](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API-key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and local JSON work orders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May query AI-HIVE MCP tools for model information and task status; paid generation, uploads, bulk actions, sending, and publishing require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
