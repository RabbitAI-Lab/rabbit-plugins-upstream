## Description:

Generate structured weekly work reports from Git commit history and file-change statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zoeee886](https://clawhub.ai/user/zoeee886)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use this skill to summarize repository activity into Markdown weekly, daily, sprint, or progress reports over a selected time range.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports may contain internal commit messages, author names, filenames, or project details.

Mitigation: Review and redact the generated Markdown report before sharing it outside the intended audience.

Risk: The bundled workflow reads Git history and writes a Markdown report for the selected repository path.

Mitigation: Confirm the repository path, date range, author filter, and output path before running the report generation command.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zoeee886/skills/weekly-report-2)
- [Server-resolved GitHub provenance](https://github.com/zoeee886/clawhub-skills/tree/main/weekly-report)
- [Examples](examples.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance, Files]

**Output Format:** [Markdown report with optional PowerShell command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports can include commit summaries, file-change counts, contributors, risks, plans, and commit-detail tables.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
