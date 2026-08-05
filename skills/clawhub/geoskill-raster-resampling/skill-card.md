## Description: <br>
Resample raster resolution with nearest-neighbor, bilinear, or cubic convolution methods and emit a resampled GeoTIFF plus run statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial engineers use this skill to resample local or synthetic raster data while preserving geographic extent and choosing interpolation behavior appropriate to categorical or continuous rasters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release is flagged suspicious because it includes credential, AOI/geocoding, and download helper modules outside the documented raster-resampling purpose. <br>
Mitigation: Review before installation, remove or clearly isolate those helpers, and invoke only the documented resampling entrypoint in sensitive environments. <br>
Risk: The security evidence reports an exposed embedded Earthdata credential and possible interaction with local credential files. <br>
Mitigation: The credential owner should rotate the exposed credential, and users should avoid running the package where sensitive ~/.netrc or ~/.geoskill/secrets.json files are present unless entrypoint isolation has been verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-raster-resampling) <br>
- [README](README.md) <br>
- [SKILL](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with CLI examples; generated artifacts are GeoTIFF and JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces resampled.tif as float32 EPSG:4326 output and output-manifest.json with input/output shapes and value ranges.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
