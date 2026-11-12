## Description:

Manage AI coding agent sessions via Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to launch, organize, monitor, and manage AI coding agent sessions in tmux, including parallel work in Git worktrees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending a message can start a stopped agent session, and sending before its prompt is ready can leave the message unsent.

Mitigation: Wait until session capture confirms the agent is ready; use --no-revive when a stopped session must not be started.

Risk: YOLO mode skips permission prompts, and purge options can permanently delete session data or worktrees.

Mitigation: Use these options only when intended, and confirm the target session and worktree before running them.

## Reference(s):

- [Agent of Empires project homepage](https://github.com/agent-of-empires/agent-of-empires)
- [Sandbox guide](https://github.com/agent-of-empires/agent-of-empires/blob/main/docs/guides/sandbox.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown instructions with shell command examples and JSON output schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples cover session management, monitoring, and worktree workflows.]

## Skill Version(s):

1.23.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
