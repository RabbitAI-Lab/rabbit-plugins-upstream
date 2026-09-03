## Description:

Design agent-native applications where agents replace UI users as the primary actor.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan agent-native systems, MCP tool surfaces, agent execution loops, prompt architecture, shared workspaces, hooks policy, mobile agent behavior, and self-modifying agent patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches broad agent file, API, and self-deployment patterns with incomplete safety and privacy guardrails.

Mitigation: Before production use, add workspace-only file scoping, canonical path validation, protected-path blocks, approval gates for sensitive writes and deployments, scoped credentials, audit logs, privacy disclosures, redaction, retention limits, and opt-in controls for cloud LLM, iCloud, HealthKit, analytics, and public publishing.

Risk: Examples or proposed architectures could be copied too literally into production systems.

Mitigation: Treat examples as design patterns, then review and test them against the target system's security, privacy, governance, and operational requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/iliaal/skills/compound-eng-agent-native-architecture)
- [SPEC.md](SPEC.md)
- [Quick Start](references/quick-start.md)
- [Core Principles](references/core-principles.md)
- [Architecture Patterns](references/architecture-patterns.md)
- [MCP Tool Design](references/mcp-tool-design.md)
- [Shared Workspace Architecture](references/shared-workspace-architecture.md)
- [Agent Execution Patterns](references/agent-execution-patterns.md)
- [System Prompt Design](references/system-prompt-design.md)
- [Dynamic Context Injection](references/dynamic-context-injection.md)
- [Action Parity Discipline](references/action-parity-discipline.md)
- [Self Modification](references/self-modification.md)
- [Product Implications](references/product-implications.md)
- [Mobile Patterns](references/mobile-patterns.md)
- [Agent Native Testing](references/agent-native-testing.md)
- [Refactoring to Prompt Native](references/refactoring-to-prompt-native.md)
- [Anti Patterns](references/anti-patterns.md)
- [Success Criteria](references/success-criteria.md)
- [Hooks Patterns](references/hooks-patterns.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with structured checklists, examples, code snippets, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory architecture guidance; users should adapt examples to their own safety, privacy, and approval requirements.]

## Skill Version(s):

4.5.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
