## Description:

Design agent-native applications where agents replace UI users as the primary actor, including MCP tools, agent-loop architectures, system prompt design, hooks policy, shared-workspace file patterns, and self-modifying agent systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design or review agent-native application architectures, including tool parity, workspace patterns, execution loops, prompt design, hooks, mobile behavior, testing, and self-modification controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives architecture guidance for broad agent file access, self-modification, public deployment, synced personal data, and sensitive API access with uneven guardrails.

Mitigation: Require workspace allowlists, secret blocking, explicit approval for writes, deployments, and self-modification, privacy notices and consent for synced or logged data, and stricter controls around health or other sensitive APIs.

Risk: Architecture proposals may be incorrect, incomplete, or unsafe if applied directly to production systems.

Mitigation: Treat examples as design sketches, review proposed changes before execution, scan the skill before deployment, and add project-specific safety boundaries.

## Reference(s):

- [Skill source](SKILL.md)
- [Skill specification](SPEC.md)
- [Core Principles](references/core-principles.md)
- [Architecture Patterns](references/architecture-patterns.md)
- [Files as Universal Interface](references/files-universal-interface.md)
- [Shared Workspace Architecture](references/shared-workspace-architecture.md)
- [MCP Tool Design](references/mcp-tool-design.md)
- [From Primitives to Domain Tools](references/from-primitives-to-domain-tools.md)
- [Agent Execution Patterns](references/agent-execution-patterns.md)
- [System Prompt Design](references/system-prompt-design.md)
- [Dynamic Context Injection](references/dynamic-context-injection.md)
- [Action Parity Discipline](references/action-parity-discipline.md)
- [Self Modification](references/self-modification.md)
- [Product Implications](references/product-implications.md)
- [Mobile Patterns](references/mobile-patterns.md)
- [Mobile Storage](references/mobile-storage.md)
- [Mobile Execution](references/mobile-execution.md)
- [Mobile Cost](references/mobile-cost.md)
- [Agent-Native Testing](references/agent-native-testing.md)
- [Refactoring to Prompt Native](references/refactoring-to-prompt-native.md)
- [Anti-Patterns](references/anti-patterns.md)
- [Success Criteria](references/success-criteria.md)
- [Hooks Patterns](references/hooks-patterns.md)
- [Quick Start](references/quick-start.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with checklists, examples, and code or command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces architecture recommendations and implementation guidance for the user's stated agent-native design context.]

## Skill Version(s):

4.4.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
