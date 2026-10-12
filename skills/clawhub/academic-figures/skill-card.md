## Description:

Helps create publication-ready scientific charts from local data, with journal presets, accessible themes, and multi-format export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to turn local JSON, CSV, or Excel data into scientific figures and journal-ready exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional dependency repair downloads packages from PyPI or configured mirrors.

Mitigation: Use a dedicated virtual environment and run setup_env.py --fix only when package downloads are acceptable.

Risk: Generated figures and temporary previews may remain on local disk.

Mitigation: Review output locations and delete unneeded figures or previews, especially when using sensitive data.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](artifact/references/quickstart.md)
- [Limits and compatibility](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Markdown instructions and locally rendered figure files (TIFF, PNG, PDF, SVG, or EPS)]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional journal presets, accessible themes, and figure verification.]

## Skill Version(s):

4.9.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
