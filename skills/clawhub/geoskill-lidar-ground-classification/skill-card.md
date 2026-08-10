## Description: <br>
Classifies LiDAR point clouds into ground and non-ground points using PMF or slope filtering, then generates DTM, density, classification, statistics, and manifest outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing engineers use this skill to preprocess LiDAR point clouds, separate ASPRS ground class 2 from non-ground class 1 points, and create bare-earth terrain products for DEM/DTM workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented LiDAR workflow is local, but the package includes under-disclosed helper code for network access and credential handling. <br>
Mitigation: Use only the documented LiDAR script path for this release and do not reuse bundled helper modules unless network, cache, and credential behavior has been removed or narrowly reviewed. <br>
Risk: The security evidence reports a plaintext fallback credential in the package. <br>
Mitigation: Do not grant this package credentials; the publisher should remove and rotate the fallback credential before trusted deployment. <br>


## Reference(s): <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Release changelog](artifact/CHANGELOG.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-lidar-ground-classification) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Analysis] <br>
**Output Format:** [NumPy classification array, GeoTIFF rasters, JSON statistics, and JSON run manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written to the selected output directory; synthetic mode includes accuracy against generated ground truth.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
