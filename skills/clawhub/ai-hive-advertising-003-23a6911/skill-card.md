## Description:

Guides agents through an AI-HIVE workflow for planning and producing declaration-style concept advertising shorts, including model and price checks, work orders, samples, task records, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Brand marketers, ecommerce merchants, advertising teams, stores, and content marketing teams use this skill to create AI-HIVE-assisted concept advertising shorts from real product claims and audience insights. The workflow emphasizes rights checks, price-aware model routing, user confirmation before paid or public actions, and reviewable deliverables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses credentials with a remote MCP helper whose endpoint and available tool calls are broader than the stated advertising workflow needs.

Mitigation: Use OAuth or a scoped API key only with the documented AI-HIVE endpoint, keep credentials out of prompts, logs, screenshots, and repositories, and avoid setting AI_HIVE_MCP_URL unless the target is fully trusted.

Risk: Generation, upload, batch, send, or publish actions may cost money or expose private materials.

Mitigation: Require explicit confirmation before any paid, batch, send, upload, generation, or public publishing action, and first use read-only model listing plus a local non-billable work order.

Risk: Remote generation can duplicate costs if a local timeout is mistaken for task failure.

Mitigation: Record task IDs and query the original AI-HIVE task before retrying or submitting a replacement generation request.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-003-23a6911)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [原创实施卡](artifact/references/original-workflow.md)
- [MCP登录与绑定指南](artifact/references/mcp-binding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, bash commands, and optional local JSON work orders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE MCP tools for model listing, media upload, image generation, advertising video generation, and task lookup after credential setup and required user confirmations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
