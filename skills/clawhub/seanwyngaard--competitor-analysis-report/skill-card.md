## Description:

Generate structured competitive analysis reports with feature comparisons, pricing analysis, SWOT, and strategic recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seanwyngaard](https://clawhub.ai/user/seanwyngaard)

### License/Terms of Use:


## Use Case:

External users, developers, and analysts use this skill to research competitors and produce client-ready competitive intelligence reports with feature comparisons, pricing analysis, SWOT, positioning, and recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has shell-command capability even though the reported workflow does not require it.

Mitigation: Install only when shell access is acceptable, or remove Bash from allowed tools before use.

Risk: The skill writes fixed output filenames under output/competitor-analysis/.

Mitigation: Check that directory before use or run the skill in a restricted workspace to avoid overwriting existing report files.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown, HTML, and CSV files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes report.md, report.html, executive-summary.md, and feature-matrix.csv under output/competitor-analysis/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
