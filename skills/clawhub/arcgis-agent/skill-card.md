## Description:

ArcGIS Agent helps agents drive ArcGIS Pro through a local arcpy-mcp-server HTTP API for GIS, spatial analysis, ArcGIS automation, and arcpy operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaojj662](https://clawhub.ai/user/zhaojj662)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and GIS practitioners use this skill to translate natural-language GIS requests into ArcGIS Pro arcpy tool calls for vector analysis, raster analysis, spatial statistics, geostatistics, data management, and multi-step site-selection workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose broad write-capable local GIS tools through an unauthenticated local HTTP service.

Mitigation: Run it only in a controlled local environment with trusted local users and processes, and add authentication before broader use.

Risk: Included ArcGIS modules may allow editing, publishing, sharing, or resource-management operations beyond the user's intended task.

Mitigation: Narrow INCLUDE_MODULES and remove server, sharing, and edit modules unless they are explicitly required.

Risk: GIS operations may write, overwrite, delete, edit, publish, or manage local or GIS resources.

Mitigation: Disable overwrite by default where practical and require explicit confirmation before destructive or publishing operations.

Risk: Path scoping may be too broad for sensitive local data.

Mitigation: Set ARCPY_ALLOWED_PATHS to the smallest required directories before running the service.

## Reference(s):

- [ArcGIS Agent examples](references/examples.md)
- [ClawHub skill page](https://clawhub.ai/zhaojj662/skills/arcgis-agent)
- [Publisher profile](https://clawhub.ai/user/zhaojj662)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, HTTP API examples, JSON response examples, and arcpy tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Windows, ArcGIS Pro 3.x, a valid ArcGIS license, and a local arcpy HTTP service.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
