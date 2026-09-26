## Description:

Creates publication-ready scientific figures from local data using chart templates, journal presets, and statistical visualization tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers use this skill to turn local JSON, CSV, or Excel data into academic charts, multi-panel figures, and journal-ready exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch or pipeline manifests may read local data and write figures, text sidecars, or reports to unintended paths.

Mitigation: Review manifests before execution and choose input and output paths deliberately.

Risk: Optional environment setup may clear the local matplotlib font cache.

Mitigation: Run the optional setup script only when that local cache change is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Getting started](artifact/references/quickstart.md)
- [Data formats](artifact/references/data-formats.md)
- [Limits and compatibility](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can create local figure files and optional text sidecars or batch reports.]

## Skill Version(s):

3.5.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
