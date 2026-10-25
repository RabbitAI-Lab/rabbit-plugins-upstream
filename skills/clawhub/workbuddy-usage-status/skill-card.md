## Description:

Generates an offline dashboard and data exports from a user's local WorkBuddy usage, including token and credit consumption, model costs, errors, and activity trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clancy-feng](https://clawhub.ai/user/clancy-feng)

### License/Terms of Use:

MIT

## Use Case:

WorkBuddy users can inspect their own local usage, compare model costs, investigate errors and usage peaks, and export reports for personal review or reconciliation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated reports can contain session titles and truncated prompt text.

Mitigation: Review and keep HTML, JSON, JavaScript, CSV, and XLSX outputs private; do not share, upload, or commit them without review.

Risk: The default local history archive retains usage data beyond WorkBuddy's trace retention period.

Mitigation: Use --no-archive if persistent local history is not wanted.

## Reference(s):

- [WorkBuddy Usage Status on ClawHub](https://clawhub.ai/clancy-feng/skills/workbuddy-usage-status)
- [Usage and troubleshooting guide](artifact/README.md)
- [Data and calculation guide](artifact/DATA-GUIDE.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Local HTML dashboard with JSON, JavaScript, CSV, and XLSX exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Contains local usage details; generated reports should be treated as private.]

## Skill Version(s):

1.6.0 (source: skill frontmatter, CHANGELOG, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
