## Description:

Design agent-native applications where agents replace UI users as the primary actor, including MCP tools, agent-loop architectures, system prompt design, hooks policy, shared-workspace file patterns, and self-modifying agent systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to design and review agent-native applications. It helps them plan MCP tool surfaces, agent loops, prompt behavior, shared workspaces, approval flows, mobile execution patterns, and self-modifying systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Architecture guidance may include self-modification, hooks, file-workspace, deployment, or external-action patterns that are unsafe without runtime controls.

Mitigation: Require scoped workspaces, protected secrets, explicit approval for destructive or irreversible actions, audit logs, rollback, and OS or orchestration-level sandboxing.

Risk: Prompt instructions could be mistaken for enforcement of authority, scope, approval, or runtime isolation.

Mitigation: Keep enforcement in trusted orchestration and validate the resulting system with real tasks, including failure and interruption paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-agent-native-architecture)
- [Core principles](references/core-principles.md)
- [Architecture patterns](references/architecture-patterns.md)
- [Architecture review checklist](references/architecture-review-checklist.md)
- [Files as a universal interface](references/files-universal-interface.md)
- [Shared workspace architecture](references/shared-workspace-architecture.md)
- [MCP tool design](references/mcp-tool-design.md)
- [From primitives to domain tools](references/from-primitives-to-domain-tools.md)
- [Agent execution patterns](references/agent-execution-patterns.md)
- [System prompt design](references/system-prompt-design.md)
- [Dynamic context injection](references/dynamic-context-injection.md)
- [Action parity discipline](references/action-parity-discipline.md)
- [Self-modification](references/self-modification.md)
- [Product implications](references/product-implications.md)
- [Mobile patterns](references/mobile-patterns.md)
- [Mobile storage](references/mobile-storage.md)
- [Mobile execution](references/mobile-execution.md)
- [Mobile cost](references/mobile-cost.md)
- [Agent-native testing](references/agent-native-testing.md)
- [Refactoring to prompt-native](references/refactoring-to-prompt-native.md)
- [Anti-patterns](references/anti-patterns.md)
- [Success criteria](references/success-criteria.md)
- [Hooks patterns](references/hooks-patterns.md)
- [CLI agent interface](references/cli-agent-interface.md)
- [Operator approval loop](references/operator-approval-loop.md)
- [Durability and attestation](references/durability-and-attestation.md)
- [Quick start](references/quick-start.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown prose with checklists, tables, examples, and code or shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

4.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
