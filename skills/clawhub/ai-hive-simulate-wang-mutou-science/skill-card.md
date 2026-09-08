## Description:

Researches the public content methods of 王木头学科学, builds a source ledger and reusable method map, and helps generate original scripts, cover concepts, storyboards, and short-video plans through AI-HIVE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, product teams, marketers, and AI learners use this skill to analyze authorized public materials, extract reusable content methods, and create their own original knowledge-content plans. Developers can also use the bundled AI-HIVE MCP and helper scripts to configure model discovery, media generation, task tracking, and local plan validation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentialed remote AI-HIVE MCP/API access may expose account capabilities or secrets if configured carelessly.

Mitigation: Use OAuth where supported or store API keys only in client secret storage or local environment variables; do not commit keys or paste tokens into prompts, screenshots, logs, or repository files.

Risk: Custom MCP or API base URLs could route credentials and generation requests to an untrusted endpoint.

Mitigation: Use the documented AI-HIVE endpoints unless the alternate endpoint is fully trusted and reviewed.

Risk: Uploads and image or video generation may process private materials or incur charges.

Mitigation: Confirm rights, privacy, task count, model, parameters, live pricing, and budget before uploads or paid generation; use read-only model discovery first.

Risk: A content-method simulation workflow can be misused for impersonation, false endorsement, or copying protected expression.

Mitigation: Use only public or authorized materials, require original wording and user-owned facts, and prohibit voice cloning, face cloning, fabricated quotes, implied authorization, and misleading persona claims.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-hive-simulate-wang-mutou-science)
- [AI-HIVE Workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP Endpoint](https://ai-hive.iclip.cn/api/mcp)
- [MCP Login and Binding Guide](references/mcp-binding.md)
- [OAuth MCP Configuration Example](references/mcp-config.example.json)
- [API Key MCP Configuration Example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and optional local JSON plan files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call credentialed AI-HIVE MCP/API workflows for model discovery, uploads, media generation, and task lookup; paid or batch generation should require explicit user confirmation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
