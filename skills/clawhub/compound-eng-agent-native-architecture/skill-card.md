## Description: <br>
Design agent-native applications where agents replace UI users as the primary actor, including MCP tools, agent-loop architectures, system prompt design, hooks policy, shared-workspace file patterns, and self-modifying agent systems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan, review, and refactor applications where agents are primary actors. It provides architecture patterns for tool design, agent loops, prompts, hooks, shared workspaces, mobile execution, testing, and governance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill promotes broad agent file and API access patterns that can exceed intended workspace boundaries. <br>
Mitigation: Use explicit workspace allowlists, secret exclusions, audit logs, retention limits, and confirmation gates for sensitive reads, writes, publishes, and deploys. <br>
Risk: Self-modifying agent patterns can weaken prompts, code, or governance if changes are accepted without review. <br>
Mitigation: Require human review, rollback paths, scanning, and approval before applying code or prompt self-modification. <br>
Risk: Persistent user context can retain sensitive or stale information longer than intended. <br>
Mitigation: Define retention limits, redact secrets and personal data, and review stored context before reuse across sessions. <br>


## Reference(s): <br>
- [Specification](SPEC.md) <br>
- [Action Parity Discipline](references/action-parity-discipline.md) <br>
- [Agent Execution Patterns](references/agent-execution-patterns.md) <br>
- [Agent-Native Testing](references/agent-native-testing.md) <br>
- [Anti-Patterns](references/anti-patterns.md) <br>
- [Architecture Patterns](references/architecture-patterns.md) <br>
- [Core Principles](references/core-principles.md) <br>
- [Dynamic Context Injection](references/dynamic-context-injection.md) <br>
- [Files as Universal Interface](references/files-universal-interface.md) <br>
- [From Primitives to Domain Tools](references/from-primitives-to-domain-tools.md) <br>
- [Hooks Patterns](references/hooks-patterns.md) <br>
- [MCP Tool Design](references/mcp-tool-design.md) <br>
- [Mobile Cost](references/mobile-cost.md) <br>
- [Mobile Execution](references/mobile-execution.md) <br>
- [Mobile Patterns](references/mobile-patterns.md) <br>
- [Mobile Storage](references/mobile-storage.md) <br>
- [Product Implications](references/product-implications.md) <br>
- [Quick Start](references/quick-start.md) <br>
- [Refactoring to Prompt-Native](references/refactoring-to-prompt-native.md) <br>
- [Self-Modification](references/self-modification.md) <br>
- [Shared Workspace Architecture](references/shared-workspace-architecture.md) <br>
- [Success Criteria](references/success-criteria.md) <br>
- [System Prompt Design](references/system-prompt-design.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown prose with checklists, examples, and inline code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; no executable files or API calls are produced by the skill itself.] <br>

## Skill Version(s): <br>
4.3.3 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
