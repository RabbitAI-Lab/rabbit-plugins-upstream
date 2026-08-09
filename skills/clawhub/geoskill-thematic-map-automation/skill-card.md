## Description:

Automate choropleth, proportional symbol and dot density thematic maps to PNG or PDF.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, GIS analysts, and geospatial teams use this skill to generate thematic maps from local vector or raster data, including choropleth, proportional symbol, and dot density outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports under-documented helper behavior around network access, caching, credential handling, and unpinned dependencies.

Mitigation: Review the package before installing it in environments with real credentials or sensitive project locations; remove, narrow, or document helper modules before deployment.

Risk: Security evidence gives the release a suspicious verdict despite the main map generator being mostly local.

Mitigation: Treat offline map generation as the intended path and scan the release before use in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-thematic-map-automation)
- [README](README.md)
- [SKILL.md](SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated geospatial files such as PNG, PDF, GeoJSON, GeoTIFF, JSON metadata, and a run manifest.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally by default and can use synthetic data without network access.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact openai.yaml and CHANGELOG list 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
