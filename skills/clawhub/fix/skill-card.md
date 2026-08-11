## Description:

Fix is a behavior-correction skill that responds to fix-prefixed feedback by analyzing the agent's mistake, improving the relevant persistent guidance, and completing the current issue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to turn correction feedback into a structured root-cause analysis, a recurrence-prevention update, and completion of the interrupted task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify persistent agent behavior across rules, memories, hooks, settings, and project knowledge.

Mitigation: Use explicit fix invocations, review proposed persistent edits before applying them, and prefer scoped workspace or project changes when the correction is not globally applicable.

Risk: Broad trigger language can cause the correction workflow to activate from ambiguous feedback.

Mitigation: Clarify ambiguous requests before changing behavior and use the skill's planning path for complex or multi-file changes.

Risk: Hook or settings changes can affect future agent turns beyond the immediate correction.

Mitigation: Review hook registrations and settings changes before enabling them, and keep a clear rollback path for global configuration changes.

## Reference(s):

- [Fix skill source](artifact/SKILL.md)
- [Step 2 prompt improvement procedure](artifact/step2-improvement.md)
- [Step 3 resume procedure](artifact/step3-resume.md)
- [Step 4 wrap-up procedure](artifact/step4-wrapup.md)
- [Behavior discipline rules](artifact/behavior-discipline.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code, shell commands, and configuration edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or revise persistent agent guidance, hook scripts, task plans, and verification steps when the correction workflow calls for them.]

## Skill Version(s):

0.3.11 (source: server-resolved release metadata and CHANGELOG top entry; artifact frontmatter reports 0.1.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
