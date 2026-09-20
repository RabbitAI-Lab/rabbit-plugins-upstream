## Description:

元忆 yotta-memory provides boundary-aware, file-based long-term memory for AI agents, with recall, remember, context restoration, local storage, permission boundaries, and diff/rollback workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to give agents persistent local memory across sessions, restore context at the start of work, save important facts, preferences, boundaries, and commitments, and maintain auditable memory files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent local memory can retain sensitive personal or project context.

Mitigation: Keep encrypted private memory enabled, review what is stored, and avoid placing unnecessary secrets or sensitive context into memory.

Risk: The skill manages agent keys, tokens, and identity boundaries.

Mitigation: Use explicit agent IDs and agent keys, avoid sharing keys in plaintext chat, and rotate or revoke unused credentials.

Risk: Installation and operation can alter MCP configuration or run scheduled background services with user consent.

Mitigation: Review install and runtime commands before applying them, pin package versions, prefer the core MCP tool profile for regular use, and check MCP/autostart configuration after changes.

Risk: Sharing one plaintext memory root across untrusted agents can expose cross-agent memory.

Mitigation: Do not share one plaintext memory root across untrusted agents; use encrypted private memory and separate trusted roots until cross-agent authorization issues are resolved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage](https://github.com/YottaMeta/yotta-memory)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-memory)
- [User guide](USER_GUIDE.md)
- [Protocol reference](references/protocol.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI/MCP command patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide agents to invoke the yotta-memory CLI or MCP tools that read, write, retrieve, archive, and maintain local memory stores.]

## Skill Version(s):

0.16.1 (source: server release, SKILL.md frontmatter, package.json, CHANGELOG released 2026-09-19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
