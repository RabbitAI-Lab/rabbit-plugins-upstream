## Description:

Manage AI coding agent sessions via Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to launch, organize, monitor, and capture output from AI coding agent sessions in tmux using aoe.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes examples that skip permission prompts or use force deletion, which can remove worktrees or reduce execution safeguards.

Mitigation: Review commands before execution, keep normal permission prompts enabled by default, and treat --force, cleanup, delete, and --delete-worktree operations as destructive.

Risk: Autonomous agent sessions can modify project files or produce incorrect code without direct supervision.

Mitigation: Run agents in sandboxed or disposable worktrees when possible and review captured session output and file changes before merging.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/njbrake/skills/aoe)
- [Agent of Empires homepage](https://github.com/agent-of-empires/agent-of-empires)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires aoe and tmux binaries.]

## Skill Version(s):

1.14.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
