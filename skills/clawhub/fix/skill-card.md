## Description:

Guides an agent through behavior-correction feedback by analyzing the mistake, updating the relevant prompt or rule to prevent recurrence, and resuming the interrupted work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to respond to corrective feedback, strengthen agent behavior rules, and complete the original interrupted task after the correction is made.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Casual corrective feedback can trigger broad, persistent changes to agent memory, rules, hooks, and global configuration.

Mitigation: Use explicit fix triggers, review proposed global changes carefully, and prefer --local when the correction should remain scoped to one project or workspace.

Risk: Prompt or rule updates can introduce incorrect or misleading behavior guidance.

Mitigation: Review the planned change and scan the skill before deployment, especially when the workflow proposes lasting rule or hook updates.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command snippets and configuration-edit instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct persistent edits to agent memory, rules, hooks, settings, task records, or skill files when used by an agent with write access.]

## Skill Version(s):

0.4.2 (source: server release metadata and changelog, released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
