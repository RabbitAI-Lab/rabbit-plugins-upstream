## Description:

Manage AI coding agent sessions via Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to launch, organize, monitor, and review AI coding agent sessions, including parallel worktree-based work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YOLO mode skips permission prompts for coding agents.

Mitigation: Avoid YOLO mode except in a constrained sandbox.

Risk: Captured agent sessions may contain sensitive output.

Mitigation: Review captured session output before sharing it.

Risk: Force deletion or worktree cleanup may remove needed work.

Mitigation: Confirm the target and save needed work before deleting sessions or cleaning up worktrees.

## Reference(s):

- [Agent of Empires project homepage](https://github.com/agent-of-empires/agent-of-empires)
- [Agent of Empires on ClawHub](https://clawhub.ai/njbrake/skills/aoe)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires aoe and tmux.]

## Skill Version(s):

1.17.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
