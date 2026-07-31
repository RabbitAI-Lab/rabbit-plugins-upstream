## Description: <br>
Extract building footprints and estimate height, floor count proxy, and volume from DSM/DTM/LiDAR data for 2.5D urban modeling, population downscaling, and risk exposure analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and urban modeling teams use this skill to estimate building-level height, floor-count proxy, volume, and quality flags from DSM/DTM rasters, LiDAR point clouds, building footprints, or a downloaded DEM tile. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional bbox/AOI mode downloads DEM data and writes local cache/output files, which may be unsuitable for sensitive AOIs or offline environments. <br>
Mitigation: Use local DSM/DTM inputs for sensitive or offline work, set a controlled cache/output directory, and run only where outbound DEM downloads are acceptable. <br>
Risk: The geospatial dependencies are not pinned to exact versions. <br>
Mitigation: Pin and audit geospatial dependencies before production deployment. <br>
Risk: Height, floor-count, and volume values are estimates that can be affected by coarse DEMs, missing DTM data, tree mixing, or shadow measurement assumptions. <br>
Mitigation: Prefer DSM+DTM or LiDAR inputs, avoid coarse DEMs for individual building heights, and review quality flags, manifests, and QA outputs before relying on results. <br>


## Reference(s): <br>
- [Building height standards](artifact/references/building_height_standards.json) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; generated artifacts include GeoJSON, CSV, JSON, HTML, and raster sidecar files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include buildings_3d.geojson, height raster metadata, building_stats.csv, quality_flags.geojson, report.html, request.json, dataset-manifest.json, output-manifest.json, and qa.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and standards reference) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
