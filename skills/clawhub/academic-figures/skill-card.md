## Description:

Generates publication-oriented scientific figures from data through command-line workflows and reusable templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use it to turn scientific data into figures for papers, reports, and journal submissions. It supports reusable templates and repeatable command-line rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags an MCP installation route and test commands for review, and notes that some files were only partially inspected.

Mitigation: Review the MCP installation source and dependency versions before use; avoid running bundled tests with untrusted or modified fixtures.

Risk: Scientific figures or statistical summaries may be incorrect or misleading.

Mitigation: Check statistical results independently and verify each figure against its source data before relying on it.

Risk: Reproducibility packages may expose raw data when shared.

Mitigation: Check privacy requirements and authorization before sharing any package containing raw data.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Project documentation site](https://docsor.cn)
- [Quickstart guide](references/quickstart.md)
- [Data formats](references/data-formats.md)
- [Technical limits](references/limits.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration instructions]

**Output Format:** [Static scientific figure files (PNG, TIFF, PDF, SVG, or EPS), with JSON/YAML inputs and command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Static figures; supported input formats and chart types vary by workflow.]

## Skill Version(s):

7.5.0 (source: changelog, released 2026-11-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
