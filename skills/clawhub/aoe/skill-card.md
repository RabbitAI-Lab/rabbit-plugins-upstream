## Description:

Manage AI coding agent sessions via Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to create, monitor, organize, and inspect AI coding-agent sessions managed by Agent of Empires in tmux.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YOLO mode can skip permission prompts when launching agent sessions.

Mitigation: Use YOLO mode only when that behavior is intended; prefer normal permission prompts on sensitive repositories.

Risk: Force deletion and worktree deletion commands can remove session state or worktree contents.

Mitigation: Review the target session and path before using --force or --delete-worktree.

Risk: Agent sessions execute in project directories and may affect repository state.

Mitigation: Prefer sandboxed sessions or scoped worktrees for sensitive repositories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/njbrake/skills/aoe)
- [Agent of Empires homepage](https://github.com/agent-of-empires/agent-of-empires)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the aoe and tmux binaries; some examples produce JSON output.]

## Skill Version(s):

1.15.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
