## Description: <br>
Design agent-native applications where agents replace UI users as the primary actor for MCP tools, agent-loop architectures, system prompt design, hooks policy, shared-workspace file patterns, and self-modifying agent systems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to design or review agent-native systems, including MCP tools, agent loops, prompt architecture, shared workspaces, hooks policy, mobile execution patterns, and safety-oriented self-modification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill promotes high-impact agent capabilities such as broad file access, shell and HTTP primitives, persistent memory, sensitive-data access, public publishing, and self-modification. <br>
Mitigation: Review proposed architectures before implementation and add least-privilege scopes, user consent, approval gates, audit logs, rollback, and retention limits before using these patterns in real systems. <br>
Risk: Copying architectural examples directly into production can preserve unsafe defaults or insufficient safety scoping. <br>
Mitigation: Treat examples as design guidance, then adapt them to the application's threat model, data sensitivity, governance requirements, and deployment constraints. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-agent-native-architecture) <br>
- [Skill Definition](SKILL.md) <br>
- [Skill Specification](SPEC.md) <br>
- [Core Principles](references/core-principles.md) <br>
- [Architecture Patterns](references/architecture-patterns.md) <br>
- [MCP Tool Design](references/mcp-tool-design.md) <br>
- [Agent Execution Patterns](references/agent-execution-patterns.md) <br>
- [Dynamic Context Injection](references/dynamic-context-injection.md) <br>
- [Action Parity Discipline](references/action-parity-discipline.md) <br>
- [Shared Workspace Architecture](references/shared-workspace-architecture.md) <br>
- [Files as Universal Interface](references/files-universal-interface.md) <br>
- [System Prompt Design](references/system-prompt-design.md) <br>
- [Hooks Patterns](references/hooks-patterns.md) <br>
- [Self-Modification](references/self-modification.md) <br>
- [Agent-Native Testing](references/agent-native-testing.md) <br>
- [Anti-Patterns](references/anti-patterns.md) <br>
- [Success Criteria](references/success-criteria.md) <br>
- [Quick Start](references/quick-start.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with code blocks, command examples, checklists, and configuration recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route the agent to focused reference material before producing design or review guidance.] <br>

## Skill Version(s): <br>
4.2.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
