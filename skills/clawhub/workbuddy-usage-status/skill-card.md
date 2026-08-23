## Description:

WorkBuddy Usage Status generates a local offline dashboard from WorkBuddy usage data, showing token consumption, estimated or imported credit use, thinking efficiency, model distribution, error counts, date filters, and usage-spike analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

WorkBuddy users and teams use this skill to audit their own local or account-level WorkBuddy usage, identify high-consumption sessions or models, compare model cost-performance, and export a portable local report.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local WorkBuddy usage database and trace files to build reports.

Mitigation: Run it only for your own WorkBuddy data or an approved local data root, and review the selected --home path before execution.

Risk: Generated HTML, JSON, and JavaScript reports may contain usage patterns, session titles, and account activity details.

Mitigation: Treat generated reports as sensitive local usage data and share or retain them only according to the user's privacy requirements.

Risk: Credit values are locally estimated unless the user supplies an official usage export with --credit-xlsx.

Mitigation: Use token totals as the primary metric for trend analysis, and use --credit-xlsx when exact daily credit reconciliation is required.

Risk: Damaged or unparsable trace files can make a generated report incomplete.

Mitigation: Check the generated warning messages and dashboard warning banner before relying on the report for audit or cost review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [README.md](README.md)
- [DATA-GUIDE.md](DATA-GUIDE.md)
- [CHANGELOG.md](CHANGELOG.md)
- [WorkBuddy usage export page](https://www.workbuddy.cn/profile/plans-usage)

## Skill Output:

**Output Type(s):** [Files, JSON, Shell commands, Guidance]

**Output Format:** [Self-contained HTML dashboard plus JSON and JavaScript data files, with concise Markdown-style guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated locally from the selected WorkBuddy data root; the default data root is ~/.workbuddy and the default output directory is the current working directory.]

## Skill Version(s):

1.2.2 (source: evidence release and CHANGELOG, released 2026-08-19; artifact SKILL.md frontmatter reports 1.2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
