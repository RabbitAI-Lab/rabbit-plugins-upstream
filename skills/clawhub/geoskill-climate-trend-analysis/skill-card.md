## Description: <br>
Performs pixel-wise Mann-Kendall trend testing and Sen slope estimation for temperature or precipitation time series, producing trend slope rasters, significance rasters, and time-series JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to screen multi-temporal climate raster data for warming, cooling, wetting, or drying trends. It supports local GeoTIFF inputs and offline synthetic data generation for validation workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes network, cache, and credential helper modules that are not part of the advertised offline climate trend workflow. <br>
Mitigation: Review the package before installation and remove or clearly disclose unused network, cache, and credential modules before broad distribution. <br>
Risk: Credential helper code includes fallback credential behavior that does not match the documented offline purpose. <br>
Mitigation: Delete hardcoded credential fallback paths and require explicit user-provided credentials only when a documented network workflow needs them. <br>
Risk: The release has unpinned dependencies and metadata inconsistencies around vendored provenance and version/license signals. <br>
Mitigation: Pin dependencies, correct vendored provenance metadata, and reconcile server and artifact metadata before production deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-climate-trend-analysis) <br>
- [README](artifact/README.md) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Release changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Analysis] <br>
**Output Format:** [GeoTIFF rasters plus JSON time-series summary and run manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces trend_slope.tif, significance.tif, timeseries.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
