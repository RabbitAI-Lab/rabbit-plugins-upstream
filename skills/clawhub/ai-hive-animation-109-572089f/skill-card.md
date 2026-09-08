## Description:

Guides animation, comics, game, original IP, and character-content teams through an AI-HIVE workflow for original stick-figure break-through-character animation or game-style content, from planning and model selection through samples, task tracking, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and production teams use this skill to plan and execute AI-HIVE image and video generation for original stick-figure animation or game-like content. It emphasizes rights tracking, model and price checks, task recovery, and acceptance criteria before paid generation, batching, sending, or publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad auto-activation could apply the workflow when the user did not intend to use AI-HIVE for this specific animation workflow.

Mitigation: Confirm the request is for this AI-HIVE stick-figure workflow before invoking tools or preparing generation steps.

Risk: AI-HIVE credentials could be sent to an environment-selected server if AI_HIVE_MCP_URL is changed.

Mitigation: Prefer OAuth, store API keys only in a client secret store, and leave AI_HIVE_MCP_URL unset unless the destination is fully trusted.

Risk: Uploads, paid generation, batching, sending, or publishing could expose content or incur costs.

Mitigation: Use read-only model and task checks first, create a local work order or minimal sample plan, and require separate confirmation before those actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/ai-hive-animation-109-572089f)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [火柴人破字闯关：原创实施卡](references/original-workflow.md)
- [AI-HIVE MCP 登录与绑定指南](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API-key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON work orders, shell commands, and MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a local JSON work order; AI-HIVE generation, upload, batching, sending, and publishing actions require separate user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
