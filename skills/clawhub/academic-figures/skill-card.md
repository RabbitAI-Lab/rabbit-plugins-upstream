## Description:

Generates publication-oriented scientific figures from data files using a local command-line workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[docsor1212](https://clawhub.ai/user/docsor1212)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers can turn JSON, CSV, or Excel data into static scientific figures for papers and journal submissions, or rerender figures in batches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A publication-ready bundle may include the original input data.

Mitigation: Use de-identified inputs, inspect each reproduction bundle before sharing, and choose explicit export flags when the input copy should be omitted.

Risk: Regression tests execute commands stored in example files.

Mitigation: Run tests only with trusted examples in an isolated environment.

Risk: Statistical figures may be used in a publication without independent confirmation of the results.

Mitigation: Independently verify statistical results before publication.

Risk: Dependency versions and optional MCP source revisions can change behavior across environments.

Mitigation: Pin dependencies and any optional MCP source revision.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/docsor1212/skills/academic-figures)
- [Academic Figures documentation site](https://docsor.cn)
- [Quickstart guide](artifact/references/quickstart.md)
- [Data format reference](artifact/references/data-formats.md)
- [Usage limits and flag interactions](artifact/references/limits.md)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Configuration]

**Output Format:** [Static PNG, TIFF, PDF, SVG, or EPS figures; command-line instructions and JSON/YAML configuration as needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single or multi-panel figures; raster output is typically 600 dpi and vector formats are available.]

## Skill Version(s):

7.2.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
