## Description:

Design agent-native applications where agents replace UI users as the primary actor, including MCP tools, agent-loop architectures, system prompt design, hooks policy, shared-workspace file patterns, and self-modifying agent systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design agent-native products and agent loops where agents are primary actors, including MCP tools, prompt behavior, hooks policy, shared workspaces, self-modification, mobile execution, and testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill promotes high-authority agent designs such as self-modifying prompts or code, broad file and HTTP tools, hooks, and deployment control.

Mitigation: Review the referenced patterns before applying them, scan the skill before deployment, and require explicit human approval for code, prompt, deployment, and external actions.

Risk: Copying broad file, bash, HTTP, hook, or self-modification examples directly into production can grant agents more authority than intended.

Mitigation: Add workspace containment, deny-by-default path checks, destination allowlists, audit logs, rollback, and dry-run or approval paths for live effects.

Risk: Shared workspace and runtime-context patterns can expose sensitive information if secrets are stored in agent-readable state.

Mitigation: Keep secrets separate from agent-readable state and enforce protected-path checks for credentials, tokens, private URLs, and customer data.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/iliaal/skills/compound-eng-agent-native-architecture)
- [SPEC.md](SPEC.md)
- [Quick Start](references/quick-start.md)
- [Core Principles](references/core-principles.md)
- [Architecture Patterns](references/architecture-patterns.md)
- [Architecture Review Checklist](references/architecture-review-checklist.md)
- [MCP Tool Design](references/mcp-tool-design.md)
- [Files Universal Interface](references/files-universal-interface.md)
- [Shared Workspace Architecture](references/shared-workspace-architecture.md)
- [From Primitives to Domain Tools](references/from-primitives-to-domain-tools.md)
- [Agent Execution Patterns](references/agent-execution-patterns.md)
- [System Prompt Design](references/system-prompt-design.md)
- [Dynamic Context Injection](references/dynamic-context-injection.md)
- [Action Parity Discipline](references/action-parity-discipline.md)
- [Self Modification](references/self-modification.md)
- [Product Implications](references/product-implications.md)
- [Hooks Patterns](references/hooks-patterns.md)
- [CLI Agent Interface](references/cli-agent-interface.md)
- [Operator Approval Loop](references/operator-approval-loop.md)
- [Durability and Attestation](references/durability-and-attestation.md)
- [Agent Native Testing](references/agent-native-testing.md)
- [Refactoring to Prompt Native](references/refactoring-to-prompt-native.md)
- [Anti Patterns](references/anti-patterns.md)
- [Success Criteria](references/success-criteria.md)
- [Mobile Patterns](references/mobile-patterns.md)
- [Mobile Storage](references/mobile-storage.md)
- [Mobile Execution](references/mobile-execution.md)
- [Mobile Cost](references/mobile-cost.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with architecture checklists, examples, code snippets, and command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-stream advisory output selected by the requested architecture focus area.]

## Skill Version(s):

4.5.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
