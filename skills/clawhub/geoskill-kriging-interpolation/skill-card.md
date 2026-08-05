## Description: <br>
Performs semivariogram fitting, ordinary kriging interpolation, and leave-one-out cross-validation to produce interpolated raster outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and geospatial engineers use this skill to interpolate spatial sample values over a WGS84 area, evaluate fit quality, and generate raster and JSON outputs for downstream geospatial workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The visible kriging CLI is mostly local, but the package includes helper modules with network geocoding and home-directory cache behavior that is not disclosed by the offline description. <br>
Mitigation: Review or isolate those helper modules before deployment, and run the kriging workflow with local inputs or synthetic mode when offline behavior is required. <br>
Risk: The package includes credential-handling helpers for unrelated services and the security evidence recommends removing hardcoded credentials. <br>
Mitigation: Remove hardcoded defaults, audit environment and local secret usage, and deploy in a restricted runtime with only required credentials available. <br>
Risk: Vendored helper metadata appears unrelated to the kriging skill, which can make maintenance and review harder. <br>
Mitigation: Fix vendored metadata and document any optional network or credential behavior before broader release. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-kriging-interpolation) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands] <br>
**Output Format:** [GeoTIFF rasters and JSON files, with optional CLI stdout] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces kriging_result.tif, kriging_variance.tif, variogram_params.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
