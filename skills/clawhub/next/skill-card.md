## Description:

Suggests practical next actions after a task, including follow-up options for stalled work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other assistant users use this skill to find actionable follow-ups after finishing a task, spot stalled steps, and choose what to do next.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent hooks can automatically prompt for next actions.

Mitigation: Review hook paths and enable them only if automatic suggestions are wanted.

Risk: Next-action discovery may inspect transcripts, task state, GitHub/CI context, and planning files across visited workspaces.

Mitigation: Limit use to trusted workspaces and review the scope of accessible project information.

Risk: A helper-script lookup may execute code from agent plugin directories.

Mitigation: Verify the helper-script path and contents before enabling hooks.

## Reference(s):

- [Next skill listing](https://clawhub.ai/drumrobot/skills/next)
- [Stall detection](artifact/stall-detect.md)
- [Ask gates](artifact/ask-gates.md)
- [Suggestion patterns](artifact/suggestion-patterns.md)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Markdown with next-action options and a user-selection prompt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Suggestions depend on the current task and available skills.]

## Skill Version(s):

0.11.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
