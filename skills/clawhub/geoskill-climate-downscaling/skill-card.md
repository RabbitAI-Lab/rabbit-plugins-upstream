## Description: <br>
Uses terrain regression and residual spatial interpolation to downscale coarse climate variables into high-resolution climate rasters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and climate practitioners use this skill to refine coarse temperature or precipitation data over complex terrain and prepare raster forcing fields for ecological or hydrological workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The distributed package includes credential and network-capable helper modules beyond the documented local downscaling workflow. <br>
Mitigation: Review and remove unused vendored helpers before deployment, or run only the main downscaling script in a constrained environment. <br>
Risk: Credential helpers can read user-level credential files and include fallback Earthdata credentials if invoked. <br>
Mitigation: Audit credential handling, remove fallback credentials, and avoid running the package with sensitive home directories mounted. <br>
Risk: Runtime dependencies are listed without pinned versions. <br>
Mitigation: Pin and review numpy, rasterio, scipy, and scikit-learn versions before installing in sensitive environments. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Skill Documentation](SKILL.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-climate-downscaling) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands] <br>
**Output Format:** [GeoTIFF raster files plus JSON validation and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes downscaled.tif, downscaling_components.tif, validation_report.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact openai.yaml and CHANGELOG report 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
