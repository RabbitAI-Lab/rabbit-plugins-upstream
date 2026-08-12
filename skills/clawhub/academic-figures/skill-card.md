## Description:

Academic Figures helps agents generate publication-ready academic charts from JSON or CSV data with journal presets, color themes, CJK support, and PDF quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, clinicians, and academic authors use this skill to turn JSON or CSV data into publication-ready figures and supplementary legends for manuscripts, journal submission, and technical reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill bundles a hospital lab-report PDF parser and may be used on sensitive patient reports.

Mitigation: Use it on patient reports only after approved data handling and independent sanitization; remove or split extract_lab_pdf.py when that parser is not needed.

Risk: Server security evidence marks the release suspicious because sensitive PDF extraction is bundled with the chart generator and de-identification is overstated.

Mitigation: Review and scan the skill before installation, and keep use limited to local chart generation unless the PDF extraction path has been approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Data formats reference](references/data-formats.md)
- [Clinical lab trends reference](references/clinical-lab-trends.md)
- [Chinese lab report extraction reference](references/chinese-lab-report-extraction.md)
- [Composite layouts reference](references/composite-layouts.md)
- [Pitfalls reference](references/pitfalls.md)
- [Reverse-engineering colors reference](references/reverse-engineering-colors.md)
- [v1.5 upgrade analysis](references/v1.5-upgrade-analysis.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Code, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated figure files such as PNG, SVG, PDF, TIFF, or EPS]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local execution; generated chart and legend outputs depend on the user's data and requested format.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
