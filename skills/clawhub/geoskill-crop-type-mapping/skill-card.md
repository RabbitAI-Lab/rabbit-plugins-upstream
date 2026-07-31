## Description: <br>
Identifies major crop types from multi-temporal optical/SAR imagery using phenological features and produces classification, area statistics, and confidence outputs. <br>

This skill is for demonstration purposes and not for production usage. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and remote-sensing analysts can use this skill to prototype crop type mapping workflows for an AOI and time range, producing maps, area summaries, manifests, and QA files for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says the skill claims to analyze real satellite imagery while the inspected code generates synthetic crop maps. <br>
Mitigation: Treat outputs as demo or prototype artifacts and do not rely on maps, area statistics, or accuracy numbers for operational, financial, insurance, or government decisions. <br>
Risk: Running the skill can install geospatial dependencies and write files to local output paths. <br>
Mitigation: Run it in a contained workspace, choose an explicit output directory, and pin and review dependencies before use. <br>


## Reference(s): <br>
- [Crop phenology schema](references/crop_phenology.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Analysis, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and geospatial output files including GeoTIFF, GeoJSON, CSV, JSON, and logs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include crop_classes.tif, crop_confidence.tif, crop_polygons.geojson, area_by_admin.csv, accuracy.json, request.json, dataset-manifest.json, output-manifest.json, qa.json, and run.log.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
