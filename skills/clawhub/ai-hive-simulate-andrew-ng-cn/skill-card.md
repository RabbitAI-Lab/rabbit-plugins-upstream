## Description:

Helps Chinese-speaking users study Andrew Ng's publicly available content methods, build source-backed methodology maps, and create original scripts, visual plans, short-video plans, and AI-HIVE execution plans without impersonation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, AI learners, technology workers, product managers, and teams use this skill to analyze public Andrew Ng content patterns, separate reusable methods from protected identity or expression, and produce their own source-grounded content plans. Users can also connect AI-HIVE to discover models, upload authorized materials, and create image, video, advertising, or ecommerce generation tasks after review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose an agent to a broad authenticated AI-HIVE remote tool connection, including upload and paid media-generation tools.

Mitigation: Prefer OAuth, list tools first, call only read-only tools for connection checks, and require explicit user confirmation of model, quantity, parameters, price, and budget before generation tasks.

Risk: User materials uploaded to AI-HIVE may include content the user is not authorized to process, private information, or business secrets.

Mitigation: Require users to confirm source, usage rights, privacy status, and authorization scope before upload, and reject paid, private, or confidential materials without permission.

Risk: Generated content could be mistaken for Andrew Ng's own words, endorsement, likeness, or authorized advice.

Mitigation: Keep outputs source-grounded, use original wording and user-owned facts, prohibit voice or face cloning, fabricated quotes, false endorsements, and claims that the output is from Andrew Ng or his representative.

Risk: Custom AI_HIVE_MCP_URL or AI_HIVE_BASE_URL settings and API keys can redirect traffic or expose credentials if misused.

Mitigation: Use the default AI-HIVE endpoints unless the endpoint is trusted, store API keys only in secure environment variables or client secret stores, and revoke OAuth grants or API keys when finished.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-simulate-andrew-ng-cn)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [AI-HIVE MCP login and binding guide](references/mcp-binding.md)
- [OAuth MCP configuration example](references/mcp-config.example.json)
- [API key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON plan files, shell commands, and MCP configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source ledgers, method maps, originality checks, model and pricing snapshots, task IDs, task status, and AI-HIVE execution records.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
