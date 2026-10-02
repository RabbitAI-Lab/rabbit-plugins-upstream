## Description:

Analyzes agent behavior feedback, updates the relevant guidance to prevent recurrence, and resumes the interrupted task.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users invoke this skill after a behavior correction request to diagnose the mistake, improve applicable agent guidance, and finish the original task.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to global agent rules, memory, hooks, or settings can persist across projects and sessions.

Mitigation: Prefer --local and review each proposed edit; approve global changes only when their broader effects are intended.

Risk: Recurrence analysis may inspect previous agent logs, failed attempts, task state, and rule files.

Mitigation: Limit access to the relevant history and review any sensitive information before sharing the analysis.

## Reference(s):

- [Fix on ClawHub](https://clawhub.ai/drumrobot/skills/fix)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions]

**Output Format:** [Text and Markdown, including proposed or applied rule and configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update persistent agent guidance and resume the interrupted task.]

## Skill Version(s):

0.7.0 (source: ClawHub release and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
