## Description: <br>
Extracts building footprints, normalized digital surface models, height estimates, volume estimates, and run manifests from local LiDAR point clouds or synthetic point-cloud examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and urban-modeling teams use this skill to process local LiDAR point clouds into 2.5D building models for footprint extraction, height estimation, stock assessment, and volume analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release was marked suspicious because bundled helper modules can use network services and read local credential stores, including hardcoded Earthdata credentials, even though the main LiDAR command appears local. <br>
Mitigation: Review and clean the package before installing it in environments with valuable credentials; remove unused network and credential helpers, rotate or remove embedded credentials, document any online features, and pin dependencies. <br>
Risk: Model outputs can be misleading when source point clouds are sparse, unprojected, or missing expected xyz columns. <br>
Mitigation: Use projected or local metric coordinates for real inputs, review stats.json and output-manifest.json, and inspect the GeoJSON and GeoTIFF outputs before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-lidar-urban-modeling) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash commands; runtime outputs include GeoTIFF, GeoJSON, JSON, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Processes local .npy, .csv, or .txt point-cloud inputs or synthetic point clouds; dependencies include numpy, rasterio, scipy, geopandas, and shapely.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
