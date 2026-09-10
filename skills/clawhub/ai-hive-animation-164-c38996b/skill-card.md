## Description:

This skill helps anime, webcomic, game, and original-IP teams plan and produce a "million protagonist entrance" animation workflow through AI-HIVE, including model and price checks, originality constraints, task tracking, and explicit confirmation before paid generation or publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creative teams and agent users use this skill to turn text and image inputs into an AI-HIVE production plan, storyboard, character and scene definitions, keyframes, animation clips, task records, and acceptance checks for original animation or game-style content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be sent to an environment-selected MCP endpoint if the helper script is run with an overridden AI_HIVE_MCP_URL.

Mitigation: Prefer OAuth through https://ai-hive.iclip.cn/api/mcp, avoid AI_HIVE_MCP_URL, and keep API keys in a trusted secret store.

Risk: The skill can be invoked for creative requests beyond its intended AI-HIVE animation workflow.

Mitigation: Confirm the agent is using the skill only for the intended workflow before allowing generation, uploads, batching, sending, or publishing.

Risk: Image and video generation, uploads, batching, sending, or publishing may create cost or distribution risk.

Mitigation: Require explicit user confirmation for paid or public actions, and use read-only model lookup or task status checks before generation.

Risk: Reference materials may lack the rights needed for public use.

Mitigation: Maintain a materials and rights checklist, use references only for structure or style mechanisms, and verify rights for people, brands, products, music, fonts, images, and video.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-hive-animation-164-c38996b)
- [AI-HIVE Workspace](https://ai-hive.iclip.cn/chat)
- [MCP Login and Binding Guide](artifact/references/mcp-binding.md)
- [Original Workflow Card](artifact/references/original-workflow.md)
- [OAuth MCP Configuration Example](artifact/references/mcp-config.example.json)
- [API Key MCP Configuration Example](artifact/references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and optional local JSON work-order files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use AI-HIVE MCP tools after model, price, budget, paid-action, upload, batching, sending, and publishing confirmations.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
