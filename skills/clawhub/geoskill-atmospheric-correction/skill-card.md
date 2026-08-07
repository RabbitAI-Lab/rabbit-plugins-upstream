## Description: <br>
Performs DOS and simplified 6S atmospheric correction for multispectral imagery, converting DN or TOA reflectance to surface reflectance with Landsat 8 and Sentinel-2 metadata support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and remote-sensing practitioners use this skill to preprocess multispectral raster imagery into surface reflectance products for downstream geospatial analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports bundled network geocoding, persistent location caching, and credential-handling helper code beyond the main local correction workflow. <br>
Mitigation: Review the package before sensitive deployment, remove or clearly isolate unused network and cache helpers, and document any geocoding or cache behavior. <br>
Risk: The security evidence reports hardcoded Earthdata credentials in bundled helper code. <br>
Mitigation: Delete and rotate hardcoded credentials before deployment and use environment-based or managed secret storage for any required credentials. <br>


## Reference(s): <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-atmospheric-correction) <br>


## Skill Output: <br>
**Output Type(s):** [files, json, shell commands] <br>
**Output Format:** [GeoTIFF files, JSON manifests, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes surface_reflectance.tif, correction_params.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
