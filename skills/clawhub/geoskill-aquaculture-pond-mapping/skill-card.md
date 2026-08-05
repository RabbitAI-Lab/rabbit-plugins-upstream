## Description: <br>
Identify and monitor aquaculture ponds from multi-temporal remote sensing, including coastal and inland pond detection, area statistics, expansion and abandonment tracking, and wetland or cropland conversion analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and environmental monitoring teams use this skill to run pond-mapping workflows from remote-sensing inputs, generate aquaculture pond inventories, assess pond dynamics, and review area and change summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: No-input or incomplete-data runs can produce synthetic or incomplete pond-mapping outputs that may be mistaken for real analysis. <br>
Mitigation: Require a real --input-ndwi dataset or a verified bbox/date-range download workflow before relying on results, and label default no-input outputs as demo or synthetic. <br>
Risk: The workflow can download satellite data and depends on unpinned Python packages. <br>
Mitigation: Review the download path for the intended area of interest, control cache and network access, and install from pinned dependencies or a reviewed lockfile in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-aquaculture-pond-mapping) <br>
- [pond_features.json](references/pond_features.json) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, files] <br>
**Output Format:** [CLI guidance with GeoJSON, CSV, and JSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include ponds.geojson, aquaculture_zones.geojson, change.geojson, area_by_admin.csv, accuracy.json, request.json, dataset-manifest.json, output-manifest.json, and qa.json.] <br>

## Skill Version(s): <br>
2.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
