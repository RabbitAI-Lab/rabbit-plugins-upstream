## Description:

Manage AI coding agent sessions via Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to launch, organize, and monitor AI coding agents in aoe-managed tmux sessions, including parallel worktree sessions and captured output for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The -y option bypasses agent approval prompts.

Mitigation: Avoid -y outside controlled environments; retain approval prompts for routine use.

Risk: Captured tmux pane output may contain sensitive information.

Mitigation: Capture only selected sessions and review output before sharing or storing it.

Risk: Forceful removal, worktree cleanup, or profile deletion can disrupt sessions or remove work.

Mitigation: Check the target session, worktree, or profile and confirm the intended effect before destructive commands.

## Reference(s):

- [Agent of Empires project homepage](https://github.com/agent-of-empires/agent-of-empires)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires aoe and tmux; includes JSON command-output examples for session inspection.]

## Skill Version(s):

1.17.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
