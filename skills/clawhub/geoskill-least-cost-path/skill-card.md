## Description: <br>
Computes a cost-distance raster and extracts a least-cost path from a cost raster using Dijkstra back-links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS analysts use this skill to compute least-cost paths from local cost rasters or synthetic test data, producing GIS artifacts for route or suitability analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Server security review flags undisclosed network, download, and credential-handling code outside the stated offline path-tool purpose. <br>
Mitigation: Review the bundle before installation, remove unrelated helper modules or hardcoded credentials if not needed, and restrict network and file-system access during execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-least-cost-path) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, shell commands, configuration, guidance] <br>
**Output Format:** [GeoTIFF, GeoJSON, JSON, and Markdown guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary files are cost_distance.tif, least_cost_path.geojson, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
