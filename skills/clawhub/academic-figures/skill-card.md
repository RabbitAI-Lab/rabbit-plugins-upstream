## Description:

Creates publication-ready scientific charts from research data with local rendering, journal presets, and figure-quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to turn JSON, CSV, or Excel data into publication figures and check their layout for journal submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rendering reads selected research files and writes figures to local paths.

Mitigation: Use approved input data and review output paths before running commands.

Risk: A generated figure may contain layout or labeling problems unsuitable for submission.

Mitigation: Review figures and use the available PDF overlap and font-size checks before submission.

## Reference(s):

- [Academic Figures on ClawHub](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](artifact/references/quickstart.md)
- [Data formats](artifact/references/data-formats.md)
- [Limits and flag interactions](artifact/references/limits.md)
- [Python API](artifact/references/python-api.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Executing the commands writes local figure files, including PDF, PNG, TIFF, SVG, and EPS.]

## Skill Version(s):

3.6.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
