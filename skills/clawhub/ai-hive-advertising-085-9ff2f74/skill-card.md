## Description:

This skill guides an agent through an AI-HIVE workflow for one-shot advertising shorts, including planning, model and price lookup, sample generation, task tracking, acceptance checks, and explicit confirmation before paid generation, batch actions, sending, or public publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Brand marketers, ecommerce sellers, advertising agencies, stores, and content marketing teams use this skill to create AI-assisted advertising video assets from verified product claims, audience context, authorized materials, and channel requirements. The workflow helps agents produce plans, scripts, key frames, finished cuts, multi-ratio variants, task records, and compliance checks while requiring separate approval for paid or public actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials could be sent to a non-official MCP endpoint if AI_HIVE_MCP_URL is overridden.

Mitigation: Keep AI_HIVE_MCP_URL unset or verify it is exactly https://ai-hive.iclip.cn/api/mcp before using API-key based tooling.

Risk: Remote generation, uploads, batch actions, sending, or publishing may create cost or release content publicly.

Mitigation: Use ai_hive_list_models for current model and price information, create only a minimal sample first, and require explicit user confirmation before paid or public actions.

Risk: Secrets or private materials may be exposed through prompts, logs, screenshots, command history, or issue reports.

Mitigation: Use OAuth where supported, store API keys only in secure client secrets or environment variables, revoke leaked keys immediately, and share only redacted diagnostics.

Risk: Advertising outputs may contain unsupported claims, unauthorized assets, or insufficient originality relative to references.

Mitigation: Maintain a product fact card, asset rights list, reference-use boundaries, task records, and acceptance checks for claim visibility, brand consistency, early-message clarity, and deployability.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-085-9ff2f74)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [原创实施卡](references/original-workflow.md)
- [MCP 登录与绑定指南](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples, shell commands, and local JSON work-order output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires runtime model and price lookup; paid generation, batch actions, sending, and public publishing require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
