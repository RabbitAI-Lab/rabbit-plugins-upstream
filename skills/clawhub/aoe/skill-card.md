## Description:

Manage AI coding agent sessions via Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to launch, organize, monitor, and inspect AI coding agent sessions running in tmux, including grouped sessions, profiles, worktree-backed tasks, and captured session output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands that enable YOLO mode can bypass approval prompts for an agent session.

Mitigation: Allow YOLO mode only when explicitly requested and when the target repository or sandbox can tolerate broad agent actions.

Risk: Forced worktree deletion can remove repository state that still contains needed changes.

Mitigation: Use forced worktree deletion only after confirming the affected worktree has no required changes.

## Reference(s):

- [Agent of Empires GitHub repository](https://github.com/agent-of-empires/agent-of-empires)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, json]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the aoe and tmux command-line binaries.]

## Skill Version(s):

1.15.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
