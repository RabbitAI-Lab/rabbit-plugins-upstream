## Description: <br>
Multi-criteria site selection for solar PV and wind projects that applies hard constraints and weighted suitability analysis for renewable energy development screening. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and renewable-energy planners use this skill to screen solar PV or wind farm sites, compare development zones, estimate candidate capacity, and apply terrain, water, land-cover, protected-area, and grid-distance constraints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may download external geospatial data from NASA POWER and Planetary Computer when bbox/AOI and date-range inputs are used. <br>
Mitigation: Run it in a project-specific directory, set explicit output and cache directories, and review or pin dependencies for reproducible installs. <br>
Risk: The skill writes analysis artifacts to disk, including rasters, candidate-site geometry, reports, manifests, and optional downloaded source data. <br>
Mitigation: Choose an explicit output directory, inspect generated files before reuse, and avoid running it where unexpected file creation would be disruptive. <br>
Risk: Suitability results depend on the quality of input rasters, masks, weights, thresholds, and external data sources. <br>
Mitigation: Validate inputs and parameters with GIS or renewable-energy domain experts before using candidate sites for planning, permitting, or investment decisions. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/ruiduobao/skills/geoskill-renewable-energy-site-selection) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance and CLI commands that produce GeoTIFF, GeoJSON, HTML, and JSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes suitability.tif, candidate_sites.geojson, report.html, and output-manifest.json to the configured output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
