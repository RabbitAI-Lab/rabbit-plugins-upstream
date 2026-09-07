## Description:

Use TokST for durable memory, automatic Session capture, and user-directed Agent Tasks in cloud workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthemty](https://clawhub.ai/user/anthemty)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use TokST Memory to install and operate durable memory, Session capture, and user-assigned Agent Tasks across cloud workspaces, with local mode for private SQLite workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill instructs agents to persist broad user and project context, including silently stored facts, decisions, preferences, tasks, architecture, and notes.

Mitigation: Use TokST only when durable memory is desired, avoid storing secrets or raw reasoning, and regularly review or delete stored memories and Session candidates.

Risk: Cloud memory and Session capture can send workspace context to TokST cloud services.

Mitigation: Use local mode or explicit Session capture for sensitive work, and verify workspace, Atlas, role, and quota status before writes.

Risk: Installer and automatic memory workflows can integrate with agent clients and run background capture bridges.

Mitigation: Review installer commands before execution, enable only the specific agent integration needed, and check automatic memory status, verification, and privacy settings.

Risk: Static API keys can authorize non-interactive MCP or CLI access.

Mitigation: Store API keys only in protected client settings, keep them out of source code and transcripts, and revoke unused keys.

## Reference(s):

- [TokST documentation](https://tokst.com/docs)
- [TokST Agent guide](https://tokst.com/llms.txt)
- [TokST full Agent context](https://tokst.com/llms-full.txt)
- [TokST OpenAPI contract](https://api.tokst.com/openapi.json)
- [TokST MCP manifest](https://api.tokst.com/.well-known/mcp)
- [TokST MCP setup](https://tokst.com/docs/mcp)
- [TokST Sessions](https://tokst.com/docs/sessions)
- [TokST Local](https://tokst.com/docs/local)
- [TokST Tasks guide](https://tokst.com/docs/tasks)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI and MCP examples use JSON output modes; no fixed token cap is specified.]

## Skill Version(s):

0.8.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
