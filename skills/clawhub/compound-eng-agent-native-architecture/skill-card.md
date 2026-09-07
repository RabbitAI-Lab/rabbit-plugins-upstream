## Description:

Design agent-native applications where agents replace UI users as the primary actor. Use when designing MCP tools, agent-loop architectures, system prompt design, hooks policy, shared-workspace file patterns, or self-modifying agent systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design agent-native systems, including MCP tools, agent-loop architectures, shared workspaces, prompt behavior, hooks policy, testing, and self-modifying agent patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill discusses broad agent access and self-changing deployment patterns that can exceed intended workspace or operational boundaries.

Mitigation: Add explicit workspace scoping, approval gates for writes and irreversible actions, and review any deployment, restart, git, publishing, or self-update behavior before use.

Risk: Agent-native workflows may expose secrets, prompts, synced data, or sensitive logs if implemented without controls.

Mitigation: Protect secrets and prompts, minimize and redact logs, obtain consent for health or synced data, and use HTTP destination allowlists.

Risk: Applying architecture guidance directly may introduce unsafe permission, provenance, or attestation assumptions.

Mitigation: Treat the material as high-risk architecture reference material, verify self-update sources, and perform security review before production adoption.

## Reference(s):

- [Skill Source](artifact/SKILL.md)
- [Specification](artifact/SPEC.md)
- [Core Principles](artifact/references/core-principles.md)
- [Architecture Patterns](artifact/references/architecture-patterns.md)
- [MCP Tool Design](artifact/references/mcp-tool-design.md)
- [Shared Workspace Architecture](artifact/references/shared-workspace-architecture.md)
- [Dynamic Context Injection](artifact/references/dynamic-context-injection.md)
- [Action Parity Discipline](artifact/references/action-parity-discipline.md)
- [Agent Execution Patterns](artifact/references/agent-execution-patterns.md)
- [Agent-Native Testing](artifact/references/agent-native-testing.md)
- [Self Modification](artifact/references/self-modification.md)
- [Hooks Patterns](artifact/references/hooks-patterns.md)
- [Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-agent-native-architecture)
- [Publisher Profile](https://clawhub.ai/user/iliaal)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown prose with checklists and code or shell blocks when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory architecture guidance and implementation patterns; review before applying to production systems.]

## Skill Version(s):

4.5.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
