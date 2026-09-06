## Description:

Helps marketing, commerce, agency, retail, and content teams plan and produce car or racing advertising shorts with AI-HIVE, including model lookup, rights checks, drafts, task records, and acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketing and commerce teams use this skill to create AI-HIVE advertising workflows for car or racing short videos. It guides planning, model and price lookup, sample generation, task tracking, rights review, and final acceptance checks before any paid generation or publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: AI-HIVE API keys or OAuth tokens could be exposed through prompts, logs, screenshots, or checked-in configuration.

Mitigation: Use OAuth or a client secret store when available, keep keys out of prompts and logs, and store API keys only in supported secret fields or environment variables.

Risk: Image or video generation and publishing actions can incur cost or expose content publicly.

Mitigation: Query available models and pricing first, create a low-risk sample or local work order, and require separate confirmation before paid generation, batch operations, sending, or publishing.

Risk: Using an incorrect remote MCP endpoint or stale model assumptions can produce unreliable behavior.

Mitigation: Use the documented AI-HIVE MCP endpoint and verify current models, parameters, prices, and limits with read-only tools before generation.

Risk: Advertising outputs may include unsupported claims or assets without sufficient rights.

Mitigation: Maintain a rights checklist and brand fact card, require evidence for product claims, and review final outputs against the documented acceptance and compliance checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-advertising-104-359c71d)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [Original workflow card](references/original-workflow.md)
- [MCP login and binding guide](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API-key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and shell commands; generated work orders are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call AI-HIVE MCP tools after OAuth or API-key authentication; paid generation and publishing require separate confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
