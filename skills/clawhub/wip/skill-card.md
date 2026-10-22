## Description:

Tracks multi-step work, records progress, and helps resume unfinished tasks across supported agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users track multi-step work, review remaining tasks, and preserve progress for later sessions in Claude Code, Antigravity, or OpenClaw.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Edit-blocking hooks may interrupt ordinary work.

Mitigation: Review hook registration and enable enforcement only where it fits your workflow.

Risk: Transcript inspection and persistent task-state changes may expose or retain sensitive work context.

Mitigation: Check what the hooks read and where task state is stored before use.

Risk: Automatic external checks or global cache behavior may proceed without the confirmation you expect.

Mitigation: Disable those behaviors when explicit user approval is required.

## Reference(s):

- [WIP skill on ClawHub](https://clawhub.ai/drumrobot/skills/wip)
- [Claude Code task tracking guide](claude.md)
- [Antigravity task tracking guide](antigravity.md)
- [OpenClaw task tracking guide](openclaw.md)
- [Task resume workflow](resume.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Markdown checklists and progress summaries with optional commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can update session task state or persistent checklists.]

## Skill Version(s):

0.8.0 (source: ClawHub release metadata and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
