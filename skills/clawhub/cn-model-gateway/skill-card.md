## Description:

CN Model Gateway is a Python MCP server that lets agent frameworks route text, multimodal, embedding, reranking, transcription, video, batch, and health-check requests to configured Chinese model providers through a unified JSON-RPC interface.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to connect MCP-compatible clients such as Claude Code, Cursor, Cline, n8n, and Claude Desktop to multiple Chinese model providers through one local gateway. It supports provider selection, multimodal calls, embeddings, reranking, transcription, video understanding, batch jobs, status checks, and usage monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted text, images, audio, or video may be sent to configured third-party model providers.

Mitigation: Use only providers whose terms and data-handling practices are acceptable for the workload, and avoid sending sensitive data unless approved.

Risk: API keys may be exposed if stored in a local config file or committed with the skill.

Mitigation: Prefer environment variables for API keys and keep config.json out of source control.

Risk: Local SQLite databases may retain prompts, batch results, usage history, or other sensitive operational data.

Mitigation: Protect local database files and periodically clear them when stored prompts or batch results may contain sensitive data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/cn-model-gateway)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON-RPC tool responses, command-line text, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include provider responses, model comparison output, usage statistics, batch task status, and configuration guidance.]

## Skill Version(s):

1.8.0 (source: frontmatter, artifact/version.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
