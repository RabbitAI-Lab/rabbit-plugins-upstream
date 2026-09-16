## Description:

Generates publication-ready scientific figures locally from JSON, CSV, Excel, or YAML pipeline inputs, with journal presets, statistical chart support, multi-format export, and verification checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and publication teams use this skill to turn structured study data into journal-ready scientific figures, legends, accessibility text, and validation reports while keeping data local.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may change the local Python environment or clear matplotlib font-cache state.

Mitigation: Install and run the skill in a virtual environment, pin dependencies where reproducibility matters, and review setup steps before running them.

Risk: Generated scientific figures can be misleading if source data, chart type, statistical options, or journal presets are inappropriate.

Mitigation: Use the documented validation, limits, PDF overlap checks, font-size audits, and human review before publication or submission.

Risk: Optional webpage scraping notes may be mistaken for the normal figure-generation workflow.

Mitigation: Treat scraping guidance as optional research material and keep normal workflows local with explicit input files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Data Format Reference](references/data-formats.md)
- [Limits & Compatibility](references/limits.md)
- [Python API](references/python-api.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with command examples, JSON/YAML configuration patterns, and generated figure file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local execution can produce PDF, PNG, TIFF, SVG, EPS, legend text, alt-text sidecars, and validation or audit reports.]

## Skill Version(s):

2.7.0 (source: server release metadata; artifact SKILL.md version history)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
