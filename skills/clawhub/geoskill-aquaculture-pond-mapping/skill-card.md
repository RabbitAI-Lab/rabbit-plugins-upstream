## Description: <br>
Identify and monitor aquaculture ponds from multi-temporal remote sensing, including pond distribution mapping, area statistics, change detection, and inventory generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and fisheries or environmental teams use this skill to run pond mapping workflows from NDWI time-series imagery and generate pond inventories, change indicators, and area summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can produce normal-looking outputs from synthetic data when no real NDWI raster is provided. <br>
Mitigation: Require an explicit real input raster path and verify dataset-manifest.json records real input data before relying on outputs. <br>
Risk: BBox/date auto-download results may not prove that the downloaded imagery was actually analyzed. <br>
Mitigation: Do not rely on bbox/date auto-download runs until the manifests prove the downloaded asset was used; prefer --input-ndwi with a validated GeoTIFF for operational use. <br>
Risk: Wetlands/cropland conversion, ML classification, and protected-area claims may be unsupported by the current artifacts. <br>
Mitigation: Treat those claims as unsupported unless updated artifacts and validation evidence prove the relevant methods and data are implemented. <br>


## Reference(s): <br>
- [Pond feature parameters](references/pond_features.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, files] <br>
**Output Format:** [Markdown guidance with CLI examples; generated outputs include GeoJSON, CSV, and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include ponds.geojson, aquaculture_zones.geojson, change.geojson, area_by_admin.csv, accuracy.json, request.json, dataset-manifest.json, output-manifest.json, and qa.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
