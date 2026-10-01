## Description:

Data Analyzer supports sales data queries, chart generation, trend analysis, and PDF business reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiziluk](https://clawhub.ai/user/shiziluk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business analysts use this skill to query bundled sales data, generate sales and profit charts, analyze profit trends, and create PDF business reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes an unrelated installer-named HTML page that loads remote scripts.

Mitigation: Remove the file or document why it is required before installing the skill.

Risk: Dependencies are listed without pinned versions.

Mitigation: Pin and review dependency versions before deployment.

Risk: Generated chart and PDF outputs use predictable fixed /tmp filenames.

Mitigation: Use safe private temporary paths or unique filenames for generated outputs.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, files]

**Output Format:** [Plain text responses plus generated PNG chart files and PDF report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated charts and reports are written to fixed /tmp paths.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
