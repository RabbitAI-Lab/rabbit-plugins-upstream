## Description:

CN Model Gateway is a Python MCP server that lets agent frameworks call multiple Chinese model providers through a unified JSON-RPC interface for chat, vision, embeddings, reranking, transcription, video understanding, provider health checks, and usage reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to connect Claude Code, Cursor, Cline, n8n, Claude Desktop, and similar frameworks to configured Chinese model APIs through one MCP gateway. It supports model selection and comparison, multimodal requests, embeddings, reranking, transcription, video summarization, provider health checks, and local usage tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, documents, images, audio, and video references may be sent to the model providers configured by the user.

Mitigation: Use only approved providers, avoid submitting sensitive data unless provider terms allow it, and specify a provider or disable failover for sensitive workflows.

Risk: API keys can be exposed if stored in config.json or committed with the skill configuration.

Mitigation: Prefer environment variables for provider credentials and keep local configuration files out of version control.

Risk: The skill keeps local usage data, and the security guidance calls out unused cache or arena helpers that may retain prompts locally.

Mitigation: Review local storage locations before deployment, limit filesystem access, and avoid cache or arena helpers unless local prompt retention is intended.

Risk: Model calls can consume paid provider quota and auto failover may route work to a backup provider.

Mitigation: Monitor usage statistics, configure provider quotas or alerts, and disable failover when routing must stay with a specific provider.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/cn-model-gateway)
- [artifact/SKILL.md](artifact/SKILL.md)
- [artifact/README.md](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, JSON, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON-RPC tool results, command-line text, configuration snippets, and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include third-party model responses, embeddings, rerank scores, transcriptions, video summaries, provider status, and local usage statistics.]

## Skill Version(s):

1.7.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
