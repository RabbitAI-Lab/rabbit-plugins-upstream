## Description:

This skill helps brand marketing teams, e-commerce sellers, agencies, stores, and content marketing teams create AI-HIVE product advertising short-video workflows that begin with real product claims and audience insight, query current model availability and pricing, and produce reviewable advertising plans, samples, task records, and acceptance checks before any paid generation or publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External brand, e-commerce, agency, retail, and content marketing users use this skill to plan and execute original product advertising short videos through AI-HIVE. It guides claim substantiation, rights checks, storyboard planning, model routing, sample generation, task recovery, multi-ratio deliverables, and acceptance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials could be sent to an untrusted MCP destination if AI_HIVE_MCP_URL is changed.

Mitigation: Use the official AI-HIVE MCP endpoint, prefer OAuth through a trusted client, and only set AI_HIVE_MCP_URL when the destination is fully trusted.

Risk: API keys, OAuth tokens, private prompts, user assets, or billing details could be exposed through prompts, logs, screenshots, or repositories.

Mitigation: Store API keys in client secrets or environment variables, revoke leaked keys immediately, and keep tokens, private prompts, assets, and billing details out of shared records.

Risk: Paid generation, uploads, batch actions, sending, or public posting could create cost or publication impact without user intent.

Mitigation: Require explicit user confirmation before paid generation, uploads, batch operations, sending, or public release, and use read-only model listing or task lookup for validation where possible.

## Reference(s):

- [AI-HIVE Homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP Endpoint](https://ai-hive.iclip.cn/api/mcp)
- [MCP Login and Binding Guide](references/mcp-binding.md)
- [Original Advertising Workflow Card](references/original-workflow.md)
- [OAuth MCP Configuration Example](references/mcp-config.example.json)
- [API Key MCP Configuration Example](references/mcp-config-api-key.example.json)
- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-002-c8910ba)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and local JSON work-order files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference AI-HIVE task IDs, model and pricing snapshots, rights records, acceptance checklists, and confirmation gates for paid or public actions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
