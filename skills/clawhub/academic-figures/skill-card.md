## Description:

Helps agents turn research data into publication-ready scientific figures with chart templates, journal presets, and export checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to prepare scientific charts and multi-panel figures from JSON, CSV, TSV, or Excel data for publications and journal submissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Environment setup or optional installation paths can install packages or fetch code over the network.

Mitigation: Review and approve setup commands and dependencies before using installation options.

Risk: Generated figures, audits, reproduction bundles, and temporary files may contain sensitive research data.

Mitigation: Keep generated files in approved local storage and inspect them before sharing.

Risk: Modified or untrusted regression fixtures may contain executable commands.

Mitigation: Do not run the regression suite or fixture commands from untrusted copies.

## Reference(s):

- [Academic Figures on ClawHub](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Getting started](references/quickstart.md)
- [Data formats](references/data-formats.md)
- [Limits and constraints](references/limits.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for producing local PNG, TIFF, PDF, SVG, and EPS figures.]

## Skill Version(s):

5.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
