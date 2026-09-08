## Description:

Helps users study Li Mu's public content methods and use AI-HIVE to plan or produce original, source-traceable scripts, outlines, visuals, short-video plans, and methodology-advisor analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, AI learners, product managers, and technology practitioners use this skill to convert public-source research about Li Mu's content methods into their own original content plans, scripts, knowledge-base analysis, and AI-HIVE generation workflows. It is also useful for agents that need MCP setup guidance for AI-HIVE model discovery, media upload, generation task creation, and task status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can connect an agent to AI-HIVE remote MCP tools that upload media and create billable generation tasks.

Mitigation: Install only when an AI-HIVE account connection is intended, query models and pricing first, and require explicit user confirmation before uploads, paid generation, batch generation, or public posting.

Risk: Credentials and configurable AI-HIVE endpoints could expose accounts or route requests to an untrusted host if handled carelessly.

Mitigation: Keep API keys in a secret store or environment variable and do not set AI_HIVE_BASE_URL or AI_HIVE_MCP_URL to untrusted hosts.

Risk: Generated content about a real person could imply impersonation, endorsement, cloned voice or likeness, fabricated quotes, or reuse of protected expression.

Mitigation: Use only public or authorized materials, preserve source attribution, require original wording, avoid voice and face cloning, disclose that outputs do not represent Li Mu, and perform human review before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-simulate-li-mu)
- [AI-HIVE homepage](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP login and binding guide](references/mcp-binding.md)
- [AI-HIVE OAuth MCP configuration example](references/mcp-config.example.json)
- [AI-HIVE API-key MCP configuration example](references/mcp-config-api-key.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and optional generated JSON plan files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include source ledgers, method maps, originality checks, AI-HIVE model and pricing snapshots, task IDs, and follow-up task status guidance.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
