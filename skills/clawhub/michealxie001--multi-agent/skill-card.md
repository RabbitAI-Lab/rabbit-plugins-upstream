## Description:

Production-ready multi-agent orchestration system for OpenClaw that implements Coordinator Mode with parallel worker spawning, XML task notifications, state persistence, and a four-phase Research, Synthesis, Implementation, and Verification workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[michealxie001](https://clawhub.ai/user/michealxie001)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to coordinate multiple OpenClaw worker agents across research, synthesis, implementation, and verification tasks for larger code analysis or code-change workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Spawned worker sessions may read or edit a broad workspace during delegated tasks.

Mitigation: Use the skill only in a sandbox or repository where worker file access and edits are acceptable, and review worker prompts before running sessions_spawn.

Risk: Task details, prompts, results, and specifications may persist under .openclaw/scratchpad after a run.

Mitigation: Avoid placing secrets or sensitive data in tasks, and delete .openclaw/scratchpad when the run is finished if it may contain private information.

Risk: Worker outputs and XML notifications can produce incorrect or misleading implementation guidance.

Mitigation: Review collected notifications, generated specifications, and proposed changes before applying or relying on them.

## Reference(s):

- [Architecture Design](references/ARCHITECTURE.md)
- [Test Report](test-report-phase2.5.md)
- [Claude Code Coordinator Mode](https://zread.ai/instructkr/claude-code/19-coordinator-mode)
- [ClawHub Skill Page](https://clawhub.ai/michealxie001/skills/multi-agent)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with XML notification examples, JSON state files, generated prompts, shell commands, and implementation specification files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist worker state, prompts, results, and specifications under .openclaw/scratchpad.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
