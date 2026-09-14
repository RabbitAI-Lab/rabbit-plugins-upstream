## Description:

Generates publication-ready scientific figures from JSON, CSV, or Excel data with local Python scripts, journal presets, accessibility sidecars, and verification gates for text overlap and font size.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, clinicians, and developer agents use this skill to turn structured data into journal-ready figures such as bar charts, scatter plots, heatmaps, forest plots, Kaplan-Meier curves, ROC curves, PRISMA flows, funnel plots, PCA plots, and composite panels. It is also useful for producing supplementary legends, alt text, and PDF quality checks before publication or review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs local Python scripts that read user data files and write figure outputs.

Mitigation: Review commands before execution, use a virtual environment, and pin dependencies for sensitive or regulated work.

Risk: Users may confuse the local skill with the separately advertised Pro/cloud service.

Mitigation: Keep unpublished, proprietary, or regulated data in the local workflow unless the cloud service upload, retention, and privacy terms have been reviewed.

Risk: Generated publication figures can be misleading if input data, statistical settings, or journal constraints are wrong.

Mitigation: Validate input data, use the documented limits and compatibility matrix, and run the PDF overlap and font-size verification gates before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Data formats](references/data-formats.md)
- [Limits and compatibility](references/limits.md)
- [Common pitfalls](references/pitfalls.md)
- [Composite layouts](references/composite-layouts.md)
- [FAQ](references/faq.md)
- [Examples](examples/README.md)
- [Scenario templates](templates/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands and generated figure files such as PNG, SVG, PDF, TIFF, EPS, plus optional text sidecars]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local file input and output; supports JSON, CSV, TSV, Excel, journal presets, CJK fonts, alt text, supplementary legends, and PDF verification gates.]

## Skill Version(s):

2.5.1 (source: server release metadata and archived SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
