## Description:

The fix skill guides an agent through behavior-correction feedback by analyzing the mistake, updating the relevant prompt, rule, memory, hook, or setting to reduce recurrence, and resuming the interrupted work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users invoke this skill when an agent misses a requirement, behaves incorrectly, or needs a structured fix-and-resume workflow. It supports root-cause analysis, behavioral instruction updates, optional hook or settings changes, and completion of the original interrupted deliverable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make lasting changes to agent rules, memory, hooks, settings, tasks, wiki content, and commits.

Mitigation: Use explicit /fix or fix: triggers, review every proposed rule, hook, settings, and commit change, and prefer --plan or --local when changes are broad or workspace-specific.

Risk: Broad feedback triggers can cause the workflow to modify more persistent agent behavior than the user intended.

Mitigation: Clarify ambiguous correction requests before acting, scope changes to the current project when possible, and verify the resulting behavior before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix)
- [Skill definition](SKILL.md)
- [Step 2 improvement guide](step2-improvement.md)
- [Step 3 resume guide](step3-resume.md)
- [Step 4 wrap-up guide](step4-wrapup.md)
- [Behavior discipline guide](behavior-discipline.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline commands, code edits, configuration changes, and task-status updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or apply persistent changes to agent instructions, hooks, settings, tasks, wiki content, or repository commits when the workflow calls for them.]

## Skill Version(s):

0.4.1 (source: server release metadata and CHANGELOG, released 2026-08-26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
