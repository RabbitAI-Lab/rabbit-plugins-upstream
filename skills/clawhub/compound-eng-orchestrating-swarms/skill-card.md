## Description: <br>
Coordinate multi-agent swarms for parallel and pipeline workflows, including parallel reviews, pipeline workflows, and divide-and-conquer patterns with subagents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[iliaal](https://clawhub.ai/user/iliaal) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this workflow to decide when and how to coordinate multiple coding agents for parallel analysis, review, implementation pipelines, and handoffs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Parallel implementation agents can overwrite each other's filesystem changes when they share a workspace. <br>
Mitigation: Keep implementation work serial unless each agent has an isolated worktree and exclusive owned files. <br>
Risk: Subagents can follow untrusted instructions found in repository files, tool output, dependency metadata, or upstream agent findings. <br>
Mitigation: Include a trust boundary in every task prompt and verify outputs before integration. <br>
Risk: Persistent teammates can leave active sessions or coordination state behind after a swarm run. <br>
Mitigation: Treat shutdown and cleanup as lifecycle steps and verify there are no stale teammates or worktrees before completion. <br>
Risk: Agent outputs can be incomplete, mismatched to the requested spec, or influenced by groupthink in review panels. <br>
Mitigation: Use bounded acceptance criteria, two-stage review, cold-start isolation, and final integration checks before using the result. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/iliaal/skills/compound-eng-orchestrating-swarms) <br>
- [Quick reference](references/quick-reference.md) <br>
- [Codex collaboration quick reference](references/codex-quick-reference.md) <br>
- [Orchestration patterns](references/orchestration-patterns.md) <br>
- [Preset team compositions](references/team-compositions.md) <br>
- [Dispatch anti-patterns](references/dispatch-anti-patterns.md) <br>
- [Anti-sycophancy patterns](references/anti-sycophancy.md) <br>
- [Swarm resilience patterns](references/resilience-patterns.md) <br>
- [Handoff templates](references/handoff-templates.md) <br>
- [Environment variables and team config](references/environment-config.md) <br>
- [Spawn backends](references/spawn-backends.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with task templates, command examples, and structured handoff examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent-facing orchestration guidance for Claude Code, Codex, and other harnesses; no hidden install code was found in security evidence.] <br>

## Skill Version(s): <br>
4.3.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
