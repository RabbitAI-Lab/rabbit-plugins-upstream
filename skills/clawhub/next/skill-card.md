## Description:

Suggests next actions after task completion, including stall detection, decision gates, task-list checks, and context-specific follow-up options.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to decide practical follow-up actions after completing work, especially when tasks may need verification, commit or PR handling, cleanup, or stalled workflow recovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can auto-trigger and recommend escalations into corrective workflow actions.

Mitigation: Review automation scope before installation and require explicit confirmation for /fix handoffs, task write-backs, reviewer or PR actions, wakeups, and background-agent behavior.

Risk: The security guidance flags inconsistent PR wording around draft PR behavior.

Mitigation: Correct PR examples to say "draft PR" consistently before relying on PR-creation recommendations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/drumrobot/skills/next)
- [Skill Definition](artifact/SKILL.md)
- [Ask Gates](artifact/ask-gates.md)
- [Stall Detection](artifact/stall-detect.md)
- [Suggestion Patterns](artifact/suggestion-patterns.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with optional commands and structured next-action options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose actions that depend on available backing skills and task-management tools.]

## Skill Version(s):

0.7.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
