## Description:

Coordinate multi-agent swarms for parallel and pipeline workflows, including parallel reviews, pipeline workflows, and divide-and-conquer work with subagents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iliaal](https://clawhub.ai/user/iliaal)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan and coordinate multi-agent work across parallel review, research, implementation, integration, and recovery workflows. It helps agents choose dispatch patterns, set file ownership boundaries, structure handoffs, and verify completed swarm work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Multi-agent orchestration can create uncontrolled long-running workers or unclear ownership of concurrent edits.

Mitigation: Review the skill guidance on background teammates, tmux/iTerm sessions, worktree isolation, and cleanup before installation and use.

Risk: Parallel implementation without isolation can cause conflicting file edits or integration failures.

Mitigation: Use the skill's one-owner-per-file discipline, pre-dispatch file-intersection checks, and worktree isolation guidance before dispatching implementation agents.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms)
- [Skill Instructions](SKILL.md)
- [Skill Specification](SPEC.md)
- [Preset Team Compositions](references/team-compositions.md)
- [Agent Types](references/agent-types.md)
- [TeammateTool Operations](references/teammate-operations.md)
- [Task System Integration](references/task-system.md)
- [Codex Collaboration Quick Reference](references/codex-quick-reference.md)
- [Message Formats](references/message-formats.md)
- [Orchestration Patterns](references/orchestration-patterns.md)
- [Spawn Backends](references/spawn-backends.md)
- [Environment Variables and Team Config](references/environment-config.md)
- [Handoff Templates](references/handoff-templates.md)
- [Context Carry-Forward Strategies](references/context-carry-forward.md)
- [Dispatch Anti-Patterns](references/dispatch-anti-patterns.md)
- [Anti-Sycophancy Patterns](references/anti-sycophancy.md)
- [Swarm Resilience Patterns](references/resilience-patterns.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are advisory orchestration instructions for the active agent harness.]

## Skill Version(s):

4.4.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
