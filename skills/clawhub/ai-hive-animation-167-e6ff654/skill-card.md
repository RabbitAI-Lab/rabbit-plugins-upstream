## Description:

Guides an agent through an AI-HIVE workflow for planning and producing original 8-bit retro arcade animation or game-oriented content with model, cost, rights, task-tracking, and acceptance checkpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, animation teams, game teams, and original-IP content teams use this skill to turn a brief into a plan, rights checklist, storyboard, key-frame approach, AI-HIVE model route, task record, and acceptance checklist for original 8-bit retro arcade content. It is intended to query current AI-HIVE model and pricing data before paid image or video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-bearing endpoint override could send AI-HIVE credentials or content to an untrusted MCP destination.

Mitigation: Use OAuth or API keys only with the official AI-HIVE endpoint, and set AI_HIVE_MCP_URL only when the destination is fully trusted.

Risk: Paid image, video, batch, send, or publish actions can be triggered through external AI-HIVE tools.

Mitigation: Confirm model, price, budget, upload, generation, batch, send, and publish actions explicitly before running them.

Risk: Tokens, private prompts, source materials, or billing details could be exposed through prompts, logs, screenshots, or repositories.

Mitigation: Store OAuth tokens and API keys in client secrets or environment variables, redact sensitive data from support reports, and keep private materials out of public logs and skill files.

Risk: Reference works or uploaded assets may introduce IP or usage-rights issues for public creative output.

Mitigation: Use references only for structure, rhythm, composition, or functional goals, and keep a rights checklist for characters, brands, music, fonts, images, and video assets.

## Reference(s):

- [Original workflow card](references/original-workflow.md)
- [AI-HIVE MCP login and binding guide](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API key MCP configuration example](references/mcp-config-api-key.example.json)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-animation-167-e6ff654)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and optional local JSON work-order files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE MCP tools after explicit user confirmation; the bundled planning script can produce a local non-billable JSON work order.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
