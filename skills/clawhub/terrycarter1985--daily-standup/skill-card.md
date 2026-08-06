## Description:

Generate structured daily standup summaries from recent activity such as git commits, completed tasks, and blockers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and team contributors use this skill to turn recent repository activity and task context into concise daily standup updates for team meetings or async status reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recent git commit messages and changed file names can contain sensitive project details.

Mitigation: Run the activity-gathering helper only in intended repositories and review generated standup summaries before sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/daily-standup)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown or plain-text standup summary with optional shell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries are organized into Done, Doing, and Blockers sections.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
