## Description:

Guides agents through an AI-HIVE workflow for planning and producing original warm farm-life pixel-game short videos with model routing, local work orders, task tracking, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Content, animation, game, and original-IP teams use this skill to turn a brief for a warm farm-life pixel-game short into an auditable AI-HIVE production plan, model route, sample-generation workflow, task record, and acceptance checklist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials can be exposed if API keys or OAuth tokens are pasted into prompts, logs, screenshots, or repositories.

Mitigation: Use OAuth through the MCP client where possible; otherwise store API keys only in a secret store or local environment variable and revoke leaked keys immediately.

Risk: The helper can send credentials to an environment-selected MCP URL if AI_HIVE_MCP_URL is changed to an untrusted endpoint.

Mitigation: Keep the default AI-HIVE MCP endpoint unless the alternate endpoint is fully trusted and reviewed.

Risk: AI-HIVE uploads, generation, batch actions, or publishing may incur costs or release content unintentionally.

Mitigation: Require explicit user confirmation for paid generation, uploads, batch actions, sending, or public publishing, and query existing tasks before retrying after timeouts.

Risk: Generated media can misuse protected IP, brands, likenesses, music, fonts, or unauthorized input assets.

Mitigation: Use original or properly licensed assets, document material rights, and check IP originality before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-animation-110-7382dc5)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [MCP binding guide](references/mcp-binding.md)
- [Original workflow card](references/original-workflow.md)
- [OAuth MCP config example](references/mcp-config.example.json)
- [API-key MCP config example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, Python helper outputs, and local work-order JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE model and price snapshots, task IDs, rights checks, and explicit confirmation gates for paid or publishing actions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
