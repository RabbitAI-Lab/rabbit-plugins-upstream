## Description:

Manage AI coding agent sessions via Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to launch, monitor, and organize local AI coding agent sessions, including parallel worktree sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YOLO mode bypasses agent permission prompts.

Mitigation: Avoid YOLO mode unless you understand and accept the reduced safeguards.

Risk: Forced session or worktree deletion can remove unintended work.

Mitigation: Verify the target before using force or delete-worktree options.

Risk: Bulk pane capture can expose secrets or confidential work.

Mitigation: Avoid bulk capture when session output may contain sensitive information.

## Reference(s):

- [Agent of Empires project](https://github.com/agent-of-empires/agent-of-empires)
- [Agent of Empires on ClawHub](https://clawhub.ai/njbrake/skills/aoe)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes examples of JSON session and status output; requires aoe and tmux.]

## Skill Version(s):

1.18.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
