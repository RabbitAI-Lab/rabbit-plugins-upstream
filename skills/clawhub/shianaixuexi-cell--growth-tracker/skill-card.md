## Description:

Growth Tracker generates quantified progress reports for AI and user growth, tasks, learning outcomes, efficiency, achievements, and goals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shianaixuexi-cell](https://clawhub.ai/user/shianaixuexi-cell)

### License/Terms of Use:

MIT-0

## Use Case:

External OpenClaw users and developers use this skill to turn conversation activity into quantified reports covering growth, task completion, learning, efficiency, achievements, and goals. It is suited for personal progress tracking and periodic summaries based on locally stored history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic tracking can accumulate interaction-derived progress and task history over time.

Mitigation: Review or disable auto_track if ongoing local history is not desired, and limit retention to what the user needs.

Risk: Exporting all data can disclose the full locally stored history.

Mitigation: Review exported data before sharing and avoid full-history exports unless the user is comfortable with the contents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shianaixuexi-cell/skills/growth-tracker)
- [Publisher profile](https://clawhub.ai/user/shianaixuexi-cell)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with progress bars, optional JSON or CSV exports, and setup or configuration command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May maintain local JSON history when automatic tracking is enabled.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
