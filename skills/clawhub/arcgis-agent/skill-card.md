## Description:

ArcGIS Agent lets an AI assistant drive ArcGIS Pro geoprocessing through a local ArcPy HTTP API for spatial analysis, raster processing, geostatistics, network analysis, image analysis, GeoAI, multidimensional rasters, utility networks, geocoding, and related GIS automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaojj662](https://clawhub.ai/user/zhaojj662)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, GIS analysts, and agent users use this skill to translate natural-language GIS requests into ArcGIS Pro ArcPy tool discovery and execution workflows on a local Windows workstation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local ArcPy automation server can create, modify, overwrite, publish, and process GIS resources available to the user's Windows account and ArcGIS session.

Mitigation: Run the server only during active GIS work, confirm mutating and portal-connected operations before execution, and keep backups of important GIS data.

Risk: Broad toolbox exposure increases the chance that an agent can call tools beyond the immediate task.

Mitigation: Restrict INCLUDE_MODULES to only the ArcPy modules needed for the current workflow.

Risk: Filesystem scoping is limited by the configured ArcPy path whitelist.

Mitigation: Keep ARCPY_ALLOWED_PATHS narrow and limited to task-specific working directories.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaojj662/skills/arcgis-agent)
- [Usage examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON API payloads, and ArcPy tool-call examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct a local ArcPy HTTP server to create, modify, overwrite, publish, and process GIS resources available to the user's Windows account and ArcGIS session.]

## Skill Version(s):

1.1.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
