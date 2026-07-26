## Description: <br>
Coordinates multi-agent swarms for parallel reviews, pipeline workflows, and divide-and-conquer subagent work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this workflow to coordinate multiple coding agents for parallel analysis, code review, research, implementation handoffs, and staged pipelines. It helps define task ownership, dispatch discipline, verification gates, and cleanup steps for agent swarms. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Background or persistent teammates can remain active or leave coordination files after the main work is complete. <br>
Mitigation: Request shutdown, wait for shutdown approval or idle status, review any needed task history, and run cleanup only after confirming work is complete. <br>
Risk: Parallel implementation agents can overwrite shared files or race on repository state when they are not isolated. <br>
Mitigation: Assign exclusive owned files, check for overlapping paths before dispatch, use separate worktrees for parallel implementation, and keep implementation serial when isolation is unavailable. <br>
Risk: Multi-agent review or judge panels can converge on a wrong answer when agents see each other's conclusions too early. <br>
Mitigation: Use cold-start isolation for parallel reviewers, collect independent outputs before synthesis, and use fresh instances for later review rounds. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [SPEC.md](artifact/SPEC.md) <br>
- [Codex collaboration quick reference](artifact/references/codex-quick-reference.md) <br>
- [Orchestration Patterns](artifact/references/orchestration-patterns.md) <br>
- [Preset Team Compositions](artifact/references/team-compositions.md) <br>
- [Agent Types](artifact/references/agent-types.md) <br>
- [Handoff Templates](artifact/references/handoff-templates.md) <br>
- [Dispatch Anti-Patterns](artifact/references/dispatch-anti-patterns.md) <br>
- [Anti-Sycophancy Patterns](artifact/references/anti-sycophancy.md) <br>
- [Swarm Resilience Patterns](artifact/references/resilience-patterns.md) <br>
- [Spawn Backends](artifact/references/spawn-backends.md) <br>
- [Environment Variables & Team Config](artifact/references/environment-config.md) <br>
- [Task System Integration](artifact/references/task-system.md) <br>
- [TeammateTool Operations](artifact/references/teammate-operations.md) <br>
- [Message Formats](artifact/references/message-formats.md) <br>
- [Context Carry-Forward Strategies](artifact/references/context-carry-forward.md) <br>
- [Orchestration Primitives](artifact/references/primitives.md) <br>
- [Orchestrating Swarms Quick Reference](artifact/references/quick-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code examples, JSON examples, shell command snippets, and structured handoff templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces coordination plans, task prompts, handoff templates, verification checklists, and cleanup guidance for the active agent harness.] <br>

## Skill Version(s): <br>
4.3.1 (source: server evidence release.version and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
