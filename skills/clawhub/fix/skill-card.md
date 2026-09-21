## Description:

User behavior correction skill that responds to fix-style feedback by analyzing agent mistakes, improving durable behavior guidance, and resuming the interrupted work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill when a coding agent misses a required behavior, skips a step, or mishandles feedback. It guides the agent through root-cause analysis, recurrence prevention, and completion of the original task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad correction prompts may lead to persistent changes in agent rules, memory, settings, or hooks.

Mitigation: Install only when durable behavior correction is intended, prefer local scope, and review proposed diffs before accepting global rule or settings changes.

Risk: Hook registration or home-directory configuration edits can alter future agent behavior beyond the current task.

Mitigation: Require explicit approval before any hook registration or home-directory configuration edit.

Risk: The skill may produce recurrence-prevention guidance that changes how an agent handles future work.

Mitigation: Review and scan the skill before deployment, and keep behavior changes narrowly scoped to the demonstrated issue.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/fix)
- [CHANGELOG.md](artifact/CHANGELOG.md)
- [Step 2: Prompt Improvement](artifact/step2-improvement.md)
- [Step 3: Resume Original Work](artifact/step3-resume.md)
- [Behavior Discipline](artifact/behavior-discipline.md)
- [Step 4: Wrap-up](artifact/step4-wrapup.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with shell command examples and configuration or prompt-editing procedures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct durable changes to agent rules, memory, settings, hooks, or skill files when the host agent follows the procedure.]

## Skill Version(s):

0.6.2 (source: server release metadata and CHANGELOG, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
