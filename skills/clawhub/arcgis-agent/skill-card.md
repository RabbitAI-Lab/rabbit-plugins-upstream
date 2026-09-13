## Description:

ArcGIS Agent lets an assistant drive ArcGIS Pro geoprocessing tools through a localhost HTTP API for GIS and spatial analysis workflows on Windows with ArcGIS Pro 3.x.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaojj662](https://clawhub.ai/user/zhaojj662)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, GIS analysts, and agent users use this skill to automate ArcGIS Pro spatial analysis, data management, raster, geostatistical, geocoding, and related arcpy workflows from natural-language requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local API can trigger powerful ArcGIS operations that may write, overwrite, edit, delete, publish, or run for a long time.

Mitigation: Confirm destructive, publishing, credentialed, and long-running operations explicitly before execution.

Risk: The server exposes broad local GIS automation through an unauthenticated localhost API.

Mitigation: Keep the server bound to localhost, run it only while needed, restrict exposed modules, and use a tightly controlled workspace.

Risk: Portal or ArcGIS Online modules may use active ArcGIS credentials.

Mitigation: Avoid active portal sessions unless required and confirm the intended portal target before credentialed operations.

## Reference(s):

- [ArcGIS Agent ClawHub Page](https://clawhub.ai/zhaojj662/skills/arcgis-agent)
- [ArcGIS Agent Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline shell commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include localhost HTTP calls and ArcGIS geoprocessing output paths or JSON responses.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
