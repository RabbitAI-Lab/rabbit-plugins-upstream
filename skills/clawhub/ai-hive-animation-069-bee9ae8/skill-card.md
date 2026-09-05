## Description:

This skill helps animation, manhua, game, original IP, and character-content teams plan and execute an AI-HIVE workflow for original character-based image and video content, including model lookup, work planning, sample generation, task tracking, and acceptance checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, content teams, and developers use this skill to turn a dimensional-wall-breaking interactive animation or game-content request into an original AI-HIVE production plan, rights checklist, model route, small sample, task record, and acceptance checklist. It is intended for original or properly licensed assets and requires separate confirmation before paid generation, bulk actions, sending, or public publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The external AI-HIVE MCP service may receive prompts, task details, uploaded materials, and authorized tool calls.

Mitigation: Install only for intended AI-HIVE use, prefer OAuth through the official endpoint, and avoid sending private or unlicensed materials unless the user has approved that use.

Risk: Credential or endpoint configuration mistakes could expose API keys or route requests to an untrusted MCP endpoint.

Mitigation: Keep API keys and OAuth tokens out of prompts, screenshots, logs, and repositories; do not set AI_HIVE_MCP_URL unless the endpoint is fully controlled and trusted.

Risk: Image, video, upload, bulk, send, or publish actions may create cost, rights, or public-disclosure exposure.

Mitigation: Require explicit confirmation for paid generation, bulk actions, uploads, sending, and public publishing, and keep a rights checklist for source assets.

## Reference(s):

- [Original Workflow Card](references/original-workflow.md)
- [AI-HIVE MCP Login and Binding Guide](references/mcp-binding.md)
- [OAuth MCP Configuration Example](references/mcp-config.example.json)
- [API Key MCP Configuration Example](references/mcp-config-api-key.example.json)
- [AI-HIVE Workspace](https://ai-hive.iclip.cn/chat)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-hive-animation-069-bee9ae8)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets, shell commands, and optional local JSON work-order files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose AI-HIVE MCP tool calls; paid generation, bulk actions, uploads, sending, and public publishing require explicit confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
