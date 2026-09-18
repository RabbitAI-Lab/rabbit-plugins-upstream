## Description:

Academic Figures generates publication-ready scientific charts from JSON, CSV, or Excel data with local rendering, journal presets, multi-format export, and validation checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, clinicians, analysts, and developers use this skill to turn tabular study data into publication-ready figures, batch figure pipelines, legends, and alt text while keeping data local.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local data files and writes generated figures, captions, alt text, and batch reports.

Mitigation: Review input and output paths before running batch or pipeline commands, especially when using user-supplied configuration files.

Risk: Dependency setup may modify the local matplotlib font cache.

Mitigation: Use a virtual environment for Python dependencies and run setup in an environment where font-cache changes are acceptable.

Risk: The artifact mentions a separate Pro or cloud offering that is not part of the local skill.

Mitigation: Do not upload sensitive data to external services unless that service has been separately reviewed and trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Data Format Reference](references/data-formats.md)
- [Limits and Compatibility](references/limits.md)
- [Advanced Usage](references/advanced.md)
- [Python API](references/python-api.md)
- [Templates Index](templates/README.md)
- [Examples Index](examples/README.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON templates, and generated local figure files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-selected data and may write figures, captions, alt text, and batch reports to configured output paths.]

## Skill Version(s):

2.8.0 (source: server release metadata and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
