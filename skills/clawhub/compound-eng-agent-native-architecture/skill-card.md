## Description:

Guides developers in designing agent-native applications, including tool interfaces, agent loops, shared workspaces, prompts, approvals, and testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design or review agent-native systems, choose suitable tools and workspace patterns, and evaluate agent capabilities and safeguards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recommended architectures may grant agents broad file or shell access or expose credentials.

Mitigation: Require explicit user approval, scoped workspaces, sandboxing, protected credentials, and audit logs.

Risk: Self-modification or deployment authority may change running systems unexpectedly.

Mitigation: Apply review gates and rollback for code, prompt, dependency, and deployment changes.

Risk: Agent-initiated payments, posts, or external sends may have irreversible effects.

Mitigation: Require review and approval before consequential external actions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iliaal/skills/compound-eng-agent-native-architecture)
- [Core principles](references/core-principles.md)
- [Architecture review checklist](references/architecture-review-checklist.md)
- [Tool design](references/mcp-tool-design.md)
- [Agent-native testing](references/agent-native-testing.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions]

**Output Format:** [Markdown with design recommendations, checklists, and optional examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory output; the skill does not automatically execute proposed changes.]

## Skill Version(s):

5.1.2 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
