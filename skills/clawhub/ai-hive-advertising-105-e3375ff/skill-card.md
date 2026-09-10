## Description:

This skill guides brand, ecommerce, advertising, retail, and content marketing teams through an AI-HIVE workflow for planning, generating, tracking, and reviewing new-product visual TVC advertising assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, ecommerce, advertising, retail, and content marketing teams use this skill to produce new-product visual TVC advertising plans, scripts, key frames, videos, multi-ratio variants, task records, and acceptance checks through AI-HIVE.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials may be sent to a non-default MCP endpoint if AI_HIVE_MCP_URL is deliberately overridden.

Mitigation: Prefer OAuth through the MCP client, keep API keys in a proper secret store, and only set AI_HIVE_MCP_URL after explicitly trusting the endpoint.

Risk: Paid generation, batch actions, sending, or public publishing can create cost or release content before final approval.

Mitigation: Query current model capabilities and prices first, produce a low-risk work order or sample, and require separate confirmation before paid, batch, sending, or publishing actions.

Risk: Advertising outputs can include unsupported product claims or assets without sufficient usage rights.

Mitigation: Maintain a product fact card and rights list, require source authorization for media, and verify claims, brand consistency, and acceptance criteria before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-105-e3375ff)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [原创实施卡](references/original-workflow.md)
- [MCP登录与绑定指南](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and local JSON work orders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE task IDs, model and price snapshots, rights checklists, acceptance criteria, and generated asset planning records.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
