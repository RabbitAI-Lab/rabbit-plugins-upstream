## Description:

Creates an offline dashboard and data exports from your local WorkBuddy usage, including token consumption, credit costs, model activity, and errors.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

WorkBuddy users can review and export their own local usage statistics to understand token and credit consumption, model activity, and errors. The skill is not intended for other products or arbitrary datasets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports can disclose session titles and truncated prompt text if shared or committed.

Mitigation: Review and redact generated JSON, JavaScript, HTML, CSV, and XLSX files before sharing or committing them.

Risk: The default local usage archive persists usage records between runs.

Mitigation: Use --no-archive if you do not want a persistent local usage archive.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [Usage documentation](README.md)
- [Data and methodology guide](DATA-GUIDE.md)

## Skill Output:

**Output Type(s):** [Files, Guidance]

**Output Format:** [Offline HTML dashboard with local JSON, JavaScript, CSV, and XLSX data exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated files may include session titles and truncated prompt text; a persistent local archive is enabled by default.]

## Skill Version(s):

1.5.1 (source: frontmatter, CHANGELOG; released 2026-10-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
