## Description:

Performs DEM-based line-of-sight viewshed analysis with Earth-curvature correction and multi-observer overlay.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruiduobao](https://clawhub.ai/user/ruiduobao)

### License/Terms of Use:

MIT

## Use Case:

Developers, GIS analysts, and geospatial automation agents use this skill to run local viewshed analysis over synthetic or local DEM inputs and generate visibility rasters, observer-count rasters, statistics, and a run manifest.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure through helper code that includes a hardcoded Earthdata password and can read local credential stores.

Mitigation: Remove hardcoded credentials, document all credential access paths, and review the package in an isolated environment before installing it near valuable ~/.netrc, ~/.geoskill/secrets.json, or service API keys.

Risk: Underdocumented helper modules can make network requests if invoked, even though the documented viewshed command appears local.

Mitigation: Limit use to the documented local viewshed workflow or inspect and disable unused network-capable helpers before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-viewshed-analysis)
- [README](README.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; runtime outputs include GeoTIFF rasters, JSON statistics, and a JSON run manifest.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The documented CLI writes viewshed.tif, viewshed_count.tif, viewshed_stats.json, and output-manifest.json to the selected output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata and script VERSION; artifact openai.yaml and CHANGELOG report 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
