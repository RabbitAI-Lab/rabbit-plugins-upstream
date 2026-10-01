## Description:

Data Analyzer queries bundled sales data, creates sales and profit charts, generates business insight text, and exports PDF sales reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[goo2200](https://clawhub.ai/user/goo2200)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business users can use this skill to query sales metrics, generate sales or profit visualizations, analyze profit trends, and compile the results into a PDF business report from the bundled CSV dataset.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated PDF filenames can be influenced by report titles and may write outside the intended report folder.

Mitigation: Generate server-controlled filenames or strictly validate report titles against a safe filename pattern in a fixed output directory.

Risk: PDF reports can embed caller-selected local image paths.

Mitigation: Allow only chart paths created by the skill, validate path prefix and file type, and reject sensitive or untrusted local files.

Risk: Generated chart and report files use predictable temporary paths and cleanup behavior is not documented.

Mitigation: Use isolated per-run directories with controlled permissions and document retention and cleanup expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/goo2200/skills/data-analyzer)

## Skill Output:

**Output Type(s):** [text, files, guidance]

**Output Format:** [Plain text analysis plus local file paths for generated PNG charts and PDF reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are derived from the bundled sales.csv dataset.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter and auto changelog mention 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
