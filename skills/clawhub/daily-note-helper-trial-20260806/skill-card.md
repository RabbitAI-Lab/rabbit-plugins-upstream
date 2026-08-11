## Description:

Create and organize daily work notes with consistent structure, date-based filenames, and lightweight summaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[terrycarter1985](https://clawhub.ai/user/terrycarter1985)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers can use this skill to create, append, review, and summarize local daily work notes with consistent date-based files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Daily notes and MEMORY.md can retain sensitive or durable information in the workspace.

Mitigation: Avoid saving sensitive information that should not persist, and review retained notes before sharing or committing the workspace.

Risk: Using the runtime date can place a note under an unintended day when timezone context is unclear.

Mitigation: Confirm the intended local date for important entries or pass an explicit YYYY-MM-DD date to the scaffold command.

## Reference(s):

- [Daily Note Template](references/note-template.md)
- [ClawHub Skill Page](https://clawhub.ai/terrycarter1985/skills/daily-note-helper-trial-20260806)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown notes and concise text guidance, with optional shell command usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or appends local workspace note files under memory/ when used for note capture.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
