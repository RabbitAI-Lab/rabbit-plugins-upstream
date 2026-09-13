## Description:

Academic Figures helps agents generate publication-ready academic charts from JSON, CSV, or Excel data with local Python scripts, journal presets, PDF verification, statistics helpers, CJK support, and PNG/SVG/PDF/TIFF/EPS exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, clinicians, and developers use this skill to turn structured study data into submission-ready visualizations, figure legends, and accessibility text while keeping local workflows local.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local Python scripts read selected data files and write figure outputs where the user specifies.

Mitigation: Run the skill in a controlled workspace, review input and output paths, and keep backups for important datasets or generated figures.

Risk: The documentation mentions a separate cloud Pro service with a different privacy boundary.

Mitigation: Use the local skill for confidential research or clinical data unless cloud upload has been reviewed and approved.

Risk: Publication charts can be misleading if data formats, statistical options, or verification results are ignored.

Mitigation: Follow the data-format and limits references, and run the provided PDF verification and audit checks for deliverable figures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Data Format Reference](references/data-formats.md)
- [Limits & Compatibility](references/limits.md)
- [FAQ](references/faq.md)
- [Academic Figures Pitfalls](references/pitfalls.md)
- [Composite Figure Layout Patterns](references/composite-layouts.md)
- [Clinical Lab Parameter Trend Figure](references/clinical-lab-trends.md)
- [Examples](examples/README.md)
- [Scenario Templates](templates/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python shell commands and JSON configuration examples; generated figure files may be PNG, SVG, PDF, TIFF, or EPS.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can also generate sidecar figure legends and accessibility alt text.]

## Skill Version(s):

2.4.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
