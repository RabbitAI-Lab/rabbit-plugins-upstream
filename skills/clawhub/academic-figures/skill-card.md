## Description:

Creates publication-ready scientific charts from local data, with journal presets and multi-format figure export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to turn local JSON, CSV, or Excel data into publication-ready scientific figures, including clinical and statistical charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP mode writes figures to predictable shared temporary files, which could expose or overwrite data on shared machines.

Mitigation: Use single-user local chart generation; avoid privileged or shared-machine MCP deployments until output uses private permissions and unpredictable filenames.

Risk: Optional dependency installation can change the Python environment.

Mitigation: Use a virtual environment for --fix or uvx installs and review dependencies before installation.

Risk: A test run against modified, untrusted examples may execute unsafe content.

Mitigation: Do not run the test suite against untrusted modified examples.

## Reference(s):

- [ClawHub release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quick start](artifact/references/quickstart.md)
- [Data formats](artifact/references/data-formats.md)
- [Limits and flag interactions](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Figure files]

**Output Format:** [Text guidance and commands; generated PNG, PDF, TIFF, or other figure files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional alt text and journal-oriented export presets; figures are rendered locally.]

## Skill Version(s):

4.10.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
