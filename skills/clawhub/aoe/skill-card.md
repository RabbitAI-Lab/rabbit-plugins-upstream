## Description:

Manage AI coding agent sessions via Agent of Empires (aoe)

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to launch, organize, monitor, and manage AI coding agent sessions in tmux, including sessions that use worktrees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented purge options can permanently remove a session and its worktree.

Mitigation: Confirm the target session and worktree before using purge or delete options, and preserve needed work before deletion.

Risk: The documented YOLO option skips permission prompts for an agent session.

Mitigation: Use it only when the agent's allowed actions and project scope are understood.

## Reference(s):

- [Agent of Empires repository](https://github.com/agent-of-empires/agent-of-empires)
- [Agent of Empires sandbox guide](https://github.com/agent-of-empires/agent-of-empires/blob/main/docs/guides/sandbox.md)
- [Agent of Empires on ClawHub](https://clawhub.ai/njbrake/skills/aoe)
- [Publisher profile](https://clawhub.ai/user/njbrake)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples and instructions for managing aoe sessions through tmux.]

## Skill Version(s):

1.22.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
