## Description:

Weekly Report Pro helps an agent collect local Git history, optional code statistics, Markdown checklist progress, and user-provided work notes to draft structured weekly or monthly reports in Chinese or English.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tangbinbinm](https://clawhub.ai/user/tangbinbinm)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and team leads use this skill to turn local commit activity, checklist status, and concise user notes into results-oriented weekly or monthly work reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose sensitive project names, file paths, commit messages, or checklist content in generated reports.

Mitigation: Point it only at specific project folders and review generated reports before sharing them outside the intended audience.

Risk: Broad directory scans may collect more local Git history than the user intended.

Mitigation: Use narrow --dirs values and avoid pointing the helper at home directories or unrelated workspace roots.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tangbinbinm/skills/weekly-report-pro)
- [Artifact README](artifact/README.md)
- [Artifact skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Guidance]

**Output Format:** [Markdown reports with optional JSON evidence collected by a local helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce weekly or monthly report drafts, metrics summaries, plan completion summaries, and next-period plans.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
