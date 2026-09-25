## Description:

Creates publication-ready scientific charts and multi-panel figures from local JSON, CSV, or Excel data, with journal presets and multi-format export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to turn local research data into journal-ready scientific figures, check PDF layout, and export figures in publication formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch or pipeline runs may write figure files to unintended paths.

Mitigation: Review output paths before running batch or pipeline jobs.

Risk: Local chart generation requires Python dependencies that may not be installed.

Mitigation: Review and install the required dependencies before running the local scripts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Getting started](artifact/references/quickstart.md)
- [Data formats](artifact/references/data-formats.md)
- [Limits and compatibility](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Figure files]

**Output Format:** [Markdown guidance and commands; locally rendered PNG, TIFF, PDF, SVG, or EPS figures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Raster figures default to 600 dpi; optional PDF overlap and font-size checks.]

## Skill Version(s):

3.4.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
