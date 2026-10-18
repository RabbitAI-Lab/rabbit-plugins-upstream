## Description:

Suggests context-aware next actions after a task, including follow-up options for stalled work and pending decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users use this skill to identify practical next steps after completing work, check stalled follow-ups, and choose context-relevant actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local hooks can read session transcripts and workspace backlog files and may record transcript snippets in debug logs.

Mitigation: Review hook registration and debug-log behavior before installation, especially when handling sensitive session content.

## Reference(s):

- [Next on ClawHub](https://clawhub.ai/drumrobot/skills/next)
- [Stall detection guide](artifact/stall-detect.md)
- [Next-action suggestion patterns](artifact/suggestion-patterns.md)
- [Follow-up decision gates](artifact/ask-gates.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with suggested next actions and a question for user selection]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Suggestions depend on the current task and available session context.]

## Skill Version(s):

0.12.0 (source: ClawHub release metadata and changelog, released 2026-10-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
