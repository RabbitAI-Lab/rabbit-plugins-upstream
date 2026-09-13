## Description:

Manage AI coding agent sessions via Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to launch, organize, monitor, capture output from, and manage multiple AI coding agent sessions in tmux via the aoe CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YOLO mode can skip permission prompts for coding agents.

Mitigation: Use YOLO mode only when the agent is tightly sandboxed and the repository or workspace can tolerate automated changes.

Risk: Force-delete worktree commands can remove workspace state or uncommitted work.

Mitigation: Verify the exact target, check for uncommitted work, and proceed only when losing that worktree is acceptable.

Risk: The skill may be used against real repositories managed by aoe.

Mitigation: Review the skill before installing it for production repositories and scan changes produced by managed agents before merging.

## Reference(s):

- [Agent of Empires project homepage](https://github.com/agent-of-empires/agent-of-empires)
- [ClawHub skill page](https://clawhub.ai/njbrake/skills/aoe)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash command examples and JSON output shapes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the aoe and tmux binaries; some workflows create, manage, or delete git worktrees.]

## Skill Version(s):

1.16.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
