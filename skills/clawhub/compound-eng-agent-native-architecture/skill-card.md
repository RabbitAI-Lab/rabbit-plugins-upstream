## Description:

Design agent-native applications where agents replace UI users as the primary actor, including MCP tools, agent-loop architectures, system prompts, hooks policy, shared-workspace files, and self-modifying agent systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and product engineers use this skill to design or review agent-native systems where agents operate as primary actors. It provides architecture guidance for MCP tool design, agent loops, prompt-native behavior, shared workspaces, context injection, hooks, mobile constraints, testing, and self-modification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill recommends broad agent capabilities that can exceed appropriate workspace or system access.

Mitigation: Apply least-privilege file scopes, exclude secrets, and keep approval gates around sensitive writes, publication, deployment, and other irreversible actions.

Risk: Self-modification guidance can lead to unreviewed code, prompt, or deployment changes.

Mitigation: Require human review for self-modification, preserve rollback points, and verify changes before allowing deployment or restart.

Risk: Cloud LLM use, iCloud storage, checkpoints, logs, and context files can expose or retain sensitive information.

Mitigation: Provide privacy notices, avoid storing credentials or private data, and set retention limits for checkpoints, logs, and context files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-agent-native-architecture)
- [Skill instructions](artifact/SKILL.md)
- [Skill specification](artifact/SPEC.md)
- [Core principles](artifact/references/core-principles.md)
- [Architecture patterns](artifact/references/architecture-patterns.md)
- [MCP tool design](artifact/references/mcp-tool-design.md)
- [System prompt design](artifact/references/system-prompt-design.md)
- [Dynamic context injection](artifact/references/dynamic-context-injection.md)
- [Shared workspace architecture](artifact/references/shared-workspace-architecture.md)
- [Action parity discipline](artifact/references/action-parity-discipline.md)
- [Agent execution patterns](artifact/references/agent-execution-patterns.md)
- [Self-modification](artifact/references/self-modification.md)
- [Hooks patterns](artifact/references/hooks-patterns.md)
- [Agent-native testing](artifact/references/agent-native-testing.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with checklists, tables, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes to focused reference files based on the user's requested architecture topic.]

## Skill Version(s):

4.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
