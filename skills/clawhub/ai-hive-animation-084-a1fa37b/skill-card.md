## Description:

Helps animation, comics, game, original IP, and character content teams use AI-HIVE MCP to plan and produce original minimalist cyber-style image and video assets with model, price, task, rights, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, production teams, and developers use this skill to create original animation or game-oriented content through AI-HIVE, starting with a non-billable plan and small sample before any paid generation. It is intended to preserve task records, model and price checks, rights information, and acceptance criteria for image and video outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials could be sent to an environment-selected MCP endpoint if AI_HIVE_MCP_URL is changed.

Mitigation: Prefer OAuth or a scoped API key stored in the client secret manager, and do not set AI_HIVE_MCP_URL unless the destination is fully trusted.

Risk: Implicit invocation and generation tools may lead to paid uploads or generation before the user has reviewed cost and publishing impact.

Mitigation: Confirm the model, price snapshot, uploaded materials, and any paid, bulk, sending, or public publishing action before generation.

Risk: Generated character or media work could use unauthorized references, brands, likenesses, music, fonts, images, or videos.

Mitigation: Maintain a rights checklist, use original characters and brands or clearly licensed materials, and require human confirmation before public release.

Risk: Retrying after a timeout can duplicate a generation task and potentially duplicate cost.

Mitigation: Record task IDs and query the original task with ai_hive_get_task before submitting any retry.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/ai-hive-animation-084-a1fa37b)
- [AI-HIVE workbench](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP login and binding guide](references/mcp-binding.md)
- [Original workflow card](references/original-workflow.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API-key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, API Calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, optional local JSON work orders, and AI-HIVE MCP tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid generation, bulk actions, sending, and public publishing require separate user confirmation; model, price, and capability details are checked at runtime.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
