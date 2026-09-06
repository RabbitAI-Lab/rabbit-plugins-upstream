## Description:

Helps agents plan and run AI-HIVE workflows for original ensemble entrance animations using model routing, rights checks, draft generation, task tracking, and acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and content teams use this skill to turn a request for ensemble entrance animation into an AI-HIVE execution plan, rights checklist, model and cost lookup, sample generation path, task record, and review checklist. It is aimed at anime, short drama, game, original IP, and character-content workflows that need consistent characters and explicit confirmation before paid generation or publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials could be sent to an environment-selected MCP endpoint.

Mitigation: Use the OAuth/client MCP configuration pointed at https://ai-hive.iclip.cn/api/mcp and set AI_HIVE_MCP_URL only when the endpoint is fully trusted.

Risk: Tool access is broader than the core workflow and may include paid generation, uploads, batch work, sending, or publishing.

Mitigation: Require explicit user confirmation before any upload, paid generation, batch action, send, or public publish step.

Risk: API keys or OAuth tokens may be exposed through prompts, logs, screenshots, or repository files.

Mitigation: Store API keys in a secret store or environment variable and avoid placing credentials in skill text, prompts, screenshots, logs, or code.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-animation-160-ea8eda1)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [Original workflow card](references/original-workflow.md)
- [AI-HIVE MCP login and binding guide](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and optional local JSON work-order files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE model and price snapshots, task IDs, rights notes, and confirmation checkpoints.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
