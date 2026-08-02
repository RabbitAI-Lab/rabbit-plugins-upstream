## Description: <br>
Read LAS/LAZ/COPC point clouds, compute statistics, classification QA, DEM/DSM/CHM rasters, cross-sections, density maps, and quality reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, engineers, and geospatial analysts use this skill to run local LiDAR point cloud workflows for terrain models, canopy height models, point density maps, cross-sections, and QA reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Python dependency versions can affect reproducibility and supply-chain review. <br>
Mitigation: Install the skill in a project or virtual environment, pin dependency versions, and scan dependencies before release or production use. <br>
Risk: Generated files use standard names and may overwrite previous outputs in the selected output directory. <br>
Mitigation: Run each analysis in a fresh output directory or archive existing outputs before rerunning the workflow. <br>
Risk: LiDAR processing quality depends on prepared local LAS/LAZ data and consistent vertical datum assumptions. <br>
Mitigation: Validate input data, coordinate registration, and output QA artifacts before using generated terrain or canopy products for decisions. <br>


## Reference(s): <br>
- [LiDAR standards reference](references/lidar_standards.json) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Files] <br>
**Output Format:** [Markdown guidance with bash commands; generated outputs include GeoTIFF, GeoJSON, JSON, manifest, QA, and log files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes standard output filenames such as dem.tif, dsm.tif, chm.tif, density.tif, profiles.geojson, pointcloud_qa.json, request.json, dataset-manifest.json, output-manifest.json, qa.json, and run.log.] <br>

## Skill Version(s): <br>
3.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
