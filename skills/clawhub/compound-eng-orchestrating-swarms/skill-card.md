## Description:

Coordinate multi-agent swarms for parallel and pipeline workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to coordinate multi-agent code reviews, parallel implementation waves, pipeline workflows, and divide-and-conquer investigation while keeping ownership, verification, and completion status explicit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill teaches direct inspection and live monitoring of local agent team inbox and task files.

Mitigation: Review the skill before installation in environments with sensitive team messages, task records, prompts, or operational metadata, and use authorized runtime APIs where possible.

Risk: Live-tailing inboxes can expose session messages or operational metadata beyond the user's intended scope.

Mitigation: Avoid live-tailing inboxes unless you own the session and need the diagnostic.

Risk: Optional backend tools can alter how persistent teammates execute and what local resources they use.

Mitigation: Pin or verify optional backend tooling before installation and confirm the active runtime's supported team mode.

## Reference(s):

- [Skill Source](SKILL.md)
- [Skill Specification](SPEC.md)
- [Agent Types](references/agent-types.md)
- [Anti-Sycophancy Patterns](references/anti-sycophancy.md)
- [Codex Collaboration Quick Reference](references/codex-quick-reference.md)
- [Context Carry-Forward Strategies](references/context-carry-forward.md)
- [Cross-Run Coordination](references/cross-run-coordination.md)
- [Dispatch Anti-Patterns](references/dispatch-anti-patterns.md)
- [Dispatch Contract](references/dispatch-contract.md)
- [Environment Variables and Team Config](references/environment-config.md)
- [Handoff Templates](references/handoff-templates.md)
- [Message Formats](references/message-formats.md)
- [Orchestration Patterns](references/orchestration-patterns.md)
- [Orchestration Primitives](references/primitives.md)
- [Orchestrating Swarms Quick Reference](references/quick-reference.md)
- [Swarm Resilience Patterns](references/resilience-patterns.md)
- [Review and Delivery](references/review-and-delivery.md)
- [Session Coordination](references/session-coordination.md)
- [Spawn Backends](references/spawn-backends.md)
- [Task System Integration](references/task-system.md)
- [Preset Team Compositions](references/team-compositions.md)
- [Claude Code Teammate Operations](references/teammate-operations.md)
- [Wave Contract and QA Escalation](references/wave-contract.md)
- [Worker Lifecycle](references/worker-lifecycle.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with task briefs, handoff templates, code-style tool examples, shell commands, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the active agent runtime and available collaboration tools; active tool schemas override examples in the references.]

## Skill Version(s):

4.5.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
