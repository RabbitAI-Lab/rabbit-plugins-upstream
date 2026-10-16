## Description:

Manage AI coding agent sessions via Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to launch, monitor, and organize AI coding agent sessions, including parallel worktree-based development.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Launching agents or sending messages can start or revive sessions and initiate work unexpectedly.

Mitigation: Review commands and messages before running them; verify that the target agent is ready before sending.

Risk: YOLO mode and unsandboxed sessions can reduce permission or isolation safeguards.

Mitigation: Prefer sandboxed sessions and standard permission prompts; enable elevated modes only when necessary.

Risk: Group and profile changes can affect other sessions, while purge or worktree deletion can permanently remove data.

Mitigation: Confirm the target and review destructive flags before changing groups or profiles or purging sessions and worktrees.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/njbrake/skills/aoe)
- [Agent of Empires project homepage](https://github.com/agent-of-empires/agent-of-empires)
- [Sandbox guide](https://github.com/agent-of-empires/agent-of-empires/blob/main/docs/guides/sandbox.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires aoe and tmux.]

## Skill Version(s):

1.20.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
