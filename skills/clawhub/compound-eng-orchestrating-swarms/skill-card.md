## Description: <br>
Coordinate multi-agent swarms for parallel and pipeline workflows, including parallel reviews, pipeline workflows, and divide-and-conquer work with subagents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this workflow to coordinate multiple agents for code review, research, implementation pipelines, and complex tasks that benefit from bounded parallelism or staged handoffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow may spawn or coordinate background teammates and leave local team resources active. <br>
Mitigation: Confirm all work is complete, request teammate shutdown, and run cleanup before ending an orchestrated session. <br>
Risk: Local team inboxes and task state may contain sensitive project details or partial work products. <br>
Mitigation: Review inbox and task contents before sharing summaries, and avoid storing secrets, private URLs, customer data, or machine-specific paths. <br>
Risk: Parallel implementation agents can overwrite one another or race on shared files when they are not isolated. <br>
Mitigation: Use exclusive file ownership, run a pre-dispatch file-intersection check, and use separate worktrees for parallel implementation. <br>
Risk: Multi-agent reviews and judge panels can converge on incorrect answers when agents see each other's outputs too early. <br>
Mitigation: Use cold-start isolation, collect independent outputs before synthesis, and use fresh reviewers for each re-dispatch round. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms) <br>
- [Agent Types](references/agent-types.md) <br>
- [Anti-Sycophancy Patterns](references/anti-sycophancy.md) <br>
- [Codex Collaboration Quick Reference](references/codex-quick-reference.md) <br>
- [Context Carry-Forward Strategies](references/context-carry-forward.md) <br>
- [Dispatch Anti-Patterns](references/dispatch-anti-patterns.md) <br>
- [Environment Variables and Team Config](references/environment-config.md) <br>
- [Handoff Templates](references/handoff-templates.md) <br>
- [Message Formats](references/message-formats.md) <br>
- [Orchestration Patterns](references/orchestration-patterns.md) <br>
- [Orchestration Primitives](references/primitives.md) <br>
- [Orchestrating Swarms Quick Reference](references/quick-reference.md) <br>
- [Swarm Resilience Patterns](references/resilience-patterns.md) <br>
- [Spawn Backends](references/spawn-backends.md) <br>
- [Task System Integration](references/task-system.md) <br>
- [Preset Team Compositions](references/team-compositions.md) <br>
- [TeammateTool Operations](references/teammate-operations.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline code, shell command snippets, and structured task or handoff templates.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces orchestration plans, task prompts, handoff instructions, verification guidance, and agent coordination commands for the active harness.] <br>

## Skill Version(s): <br>
4.3.2 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
