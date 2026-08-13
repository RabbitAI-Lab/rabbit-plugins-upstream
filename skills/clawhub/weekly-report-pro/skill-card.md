## Description:

Weekly Report Pro helps an agent collect local Git activity and user-provided work notes, then draft concise weekly or monthly work reports in role- and channel-specific formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tangbinbinm](https://clawhub.ai/user/tangbinbinm)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, technical leads, and operators use this skill to turn local Git commits, optional code statistics, and supplemental work notes into polished weekly or monthly status reports. It is especially useful when the user wants a results-oriented report without manually reconstructing completed work from commit history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local Git history, repository names, paths, commit messages, and optional code-change statistics may contain sensitive project or business context.

Mitigation: Only provide directories that are appropriate to summarize in the current chat, and review generated reports before sharing them outside the intended audience.

Risk: The generated report may be incomplete when local Git history does not cover non-code work, meetings, planning, or blockers.

Mitigation: Provide supplemental notes when prompted, including non-code work, metrics, blockers, and next-period plans.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tangbinbinm/skills/weekly-report-pro)
- [Artifact README](artifact/README.md)
- [Artifact skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Guidance]

**Output Format:** [Markdown report drafts with optional shell commands for local Git collection and JSON summaries from the collection script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports weekly and monthly report modes, optional merge commits, optional code statistics, author filtering, and DingTalk, Feishu, or email-oriented report styles.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
