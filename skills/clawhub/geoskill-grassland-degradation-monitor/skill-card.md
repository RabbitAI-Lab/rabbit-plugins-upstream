## Description: <br>
Monitor grassland degradation and recovery trends from multi-temporal vegetation cover, phenology, bare ground and climate baselines, and output management zones for restoration prioritization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and geospatial practitioners use this skill to assess grassland health trends, identify degraded or recovering areas, evaluate restoration effectiveness, and generate restoration-priority management outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: BBox/date download runs may produce outputs that appear to be based on downloaded imagery while the analysis can use local NDVI input or synthetic data instead. <br>
Mitigation: For real management decisions, provide validated NDVI input or verify and fix the download-to-analysis path; clearly label any synthetic or demonstration outputs. <br>
Risk: The skill can perform external geospatial downloads and local caching. <br>
Mitigation: Install and run it only in environments where external data access and local cached data are acceptable, and review output-manifest.json for data-source details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-grassland-degradation-monitor) <br>
- [Grassland degradation schema](references/degradation_schema.json) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, files] <br>
**Output Format:** [CLI-generated GeoTIFF, GeoJSON, CSV, and JSON files, with console status messages.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include degradation_status.tif, trend.tif, priority_areas.geojson, management_summary.csv, timeseries.csv, request.json, output-manifest.json, and qa.json.] <br>

## Skill Version(s): <br>
2.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
