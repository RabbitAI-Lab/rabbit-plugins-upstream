## Description: <br>
Extracts shorelines, centerlines, channel widths, migration rates, change hotspots, and migration zones from multi-temporal water body masks for river morphology change analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and environmental teams use this skill to analyze river channel migration, identify erosion and deposition areas, compare shorelines across time periods, compute width changes, and generate morphology change outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can download Sentinel-2 imagery from Microsoft Planetary Computer and cache local geospatial data. <br>
Mitigation: Use it only where that outbound access and local file creation are acceptable; set explicit output and cache directories so downloaded imagery can be reviewed and cleaned up. <br>
Risk: River morphology outputs may be affected by water-level changes, narrow channels near pixel resolution, and complex braided or anastomosing channel topology. <br>
Mitigation: Treat outputs as auxiliary analysis, prefer same-season imagery when comparing periods, and require manual review before engineering or operational decisions. <br>


## Reference(s): <br>
- [River morphology algorithm parameters](artifact/references/river_morphology.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-river-morphology-change) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, files] <br>
**Output Format:** [Markdown guidance with CLI commands; when executed, GeoJSON, CSV, and JSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces shorelines.geojson, centerlines.geojson, transects.geojson, migration_rates.csv, change_hotspots.geojson, request.json, dataset-manifest.json, output-manifest.json, and qa.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact reference metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
