## Description:

This Chinese-language skill helps users study public content methods associated with 同济子豪兄, build source-backed methodology notes, and generate original scripts, visuals, voiceover plans, short-video plans, and AI-HIVE execution plans without impersonation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, product teams, AI learners, and knowledge-content operators use this skill to turn legally usable public or user-owned materials into source-led content analysis, original drafts, media-generation plans, and methodology-advisor outputs. It is intended for AI-HIVE workflows that require MCP login, runtime model selection, budget review, and human approval before paid or public output.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The workflow connects to AI-HIVE over network APIs and may use API keys or OAuth tokens.

Mitigation: Prefer OAuth or a client secret store, keep API keys out of prompts and files, and do not override AI_HIVE_MCP_URL or AI_HIVE_BASE_URL unless the endpoint is controlled.

Risk: Image, video, advertising, upload, or other generation tools may incur costs.

Mitigation: Confirm budget, model, quantity, parameters, and current price snapshots before creating paid tasks; use read-only model listing for connection tests.

Risk: The skill studies a real person's public methods and could be misused for impersonation or false endorsement.

Mitigation: Require no-impersonation review: do not clone voice or face, fabricate quotes, imply authorization, copy protected expression, or publish outputs without human checks.

Risk: Uploaded material may contain copyrighted, private, paid, or confidential content.

Mitigation: Use only materials the user has rights to analyze and publish, preserve source and authorization records, and avoid uploading personal data, trade secrets, or unauthorized paid content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-simulate-tongji-zihao)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP login and binding guide](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, JSON configuration examples, Python helper commands, and structured plan files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local JSON planning ledgers and may call AI-HIVE MCP tools for model discovery, uploads, image generation, video generation, and task lookup when credentials and user confirmation are provided.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
