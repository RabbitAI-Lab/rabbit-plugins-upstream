## Description:

Generates publication-ready scientific figures from JSON, CSV, or Excel data across a broad range of chart types and journal styles.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use the skill to turn structured data into static, publication-ready scientific figures, including journal-formatted charts and multi-panel layouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publication or reproducibility packages may include the full original dataset, including unused workbook contents, and command paths, which could expose confidential research or patient data.

Mitigation: Use sanitized input files, inspect every bundled file and path, and confirm permission to share the data before submitting the package.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Source repository linked in release documentation](https://github.com/docsor1212/academic-figures)
- [Quickstart guide](references/quickstart.md)

## Skill Output:

**Output Type(s):** [Images, Files, Shell commands, Guidance]

**Output Format:** [Static figure files (PNG, SVG, PDF, TIFF, or EPS), with shell commands and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Figures are rendered locally; output formats and chart options depend on the selected command and data.]

## Skill Version(s):

5.9.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
