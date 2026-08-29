## Description:

Suggests next actions after task completion, including stall detection, ask gates, task-list checks, and follow-up option templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to surface concrete follow-up actions after work completes, especially when task state, stalled progress, pull requests, or session wrap-up decisions need explicit disposition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic hooks can inspect local conversation transcripts to detect task-completion and continuation-chain signals.

Mitigation: Install only in workspaces where transcript inspection is acceptable, and review or disable the hook behavior for sensitive sessions.

Risk: The hook scripts can write local debug snippets while diagnosing missed next-action triggers.

Mitigation: Review the debug logging behavior and rotate or remove logs according to workspace privacy requirements.

Risk: Follow-up suggestions may use project, task, or GitHub state to steer broad next actions.

Mitigation: Treat suggested actions as proposals and confirm the selected work before making changes or delegating follow-up tasks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/next)
- [Ask Gates](ask-gates.md)
- [Stall Detection](stall-detect.md)
- [Suggestion Patterns](suggestion-patterns.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with optional shell commands and structured next-action options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May inspect task state and local hook transcripts when installed with its automation scripts.]

## Skill Version(s):

0.9.1 (source: server release metadata and CHANGELOG, released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
