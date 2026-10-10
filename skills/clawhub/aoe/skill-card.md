## Description:

Manage AI coding agent sessions with Agent of Empires (aoe).

This skill is ready for commercial/non-commercial use.

## Publisher:

[njbrake](https://clawhub.ai/user/njbrake)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to launch, organize, monitor, and review coding-agent sessions, including parallel worktree sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YOLO mode bypasses normal permission prompts for coding agents.

Mitigation: Prefer normal prompts and sandboxed sessions; require explicit human confirmation before using YOLO mode.

Risk: Force deletion and cleanup commands can remove sessions, worktrees, groups, or profiles.

Mitigation: Inspect command targets and affected sessions or worktrees first; require explicit human confirmation for --force, --delete-worktree, cleanup, and profile deletion.

## Reference(s):

- [Agent of Empires project homepage](https://github.com/agent-of-empires/agent-of-empires)
- [Agent of Empires on ClawHub](https://clawhub.ai/njbrake/skills/aoe)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include session status or captured agent output when requested.]

## Skill Version(s):

1.19.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
