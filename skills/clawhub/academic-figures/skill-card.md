## Description:

Helps generate publication-ready scientific figures from data using local plotting commands and journal presets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to turn JSON, CSV, or Excel data into scientific charts and journal-ready figures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local input files may contain sensitive research data, and generated figures and reports are written to disk.

Mitigation: Provide only intended data files and check the destination and access controls for generated outputs.

Risk: Optional environment setup clears the local matplotlib font cache.

Mitigation: Review setup behavior before running it, especially in shared or managed environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](references/quickstart.md)
- [Data formats](references/data-formats.md)
- [Limitations](references/limits.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands produce local PNG, TIFF, or PDF figures and optional text descriptions, captions, and reports.]

## Skill Version(s):

3.10.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
