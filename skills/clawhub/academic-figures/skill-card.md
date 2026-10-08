## Description:

Helps agents turn research data into publication-ready scientific figures with local rendering, journal presets, and figure-quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, authors, and developers use this skill to select chart types, prepare figure-generation commands, and export journal-ready plots from JSON, CSV, or Excel data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MCP server uses predictable shared temporary output paths, which may expose or overwrite files on multi-user machines.

Mitigation: Avoid the MCP server on shared machines until output paths are private and unpredictable; for sensitive data, use the local CLI with explicit output paths.

Risk: Local figure generation writes output files that can replace existing files at the selected path.

Mitigation: Review output paths and use a dedicated destination before rendering.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Quickstart](references/quickstart.md)
- [Data formats](references/data-formats.md)
- [Limits and flag interactions](references/limits.md)
- [Python API](references/python-api.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with command examples and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can render local PNG, TIFF, PDF, SVG, or EPS figure files; PDF overlap checks require --verify.]

## Skill Version(s):

4.6.0 (source: ClawHub release evidence and bundled version history)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
