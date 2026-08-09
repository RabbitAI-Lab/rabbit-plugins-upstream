## Description: <br>
基于 NDVI 覆盖度、物候生长季与峰值及退化指数评估草地质量。Assesses pasture quality from NDVI cover, phenology (season and peak) and a degradation index. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Agriculture, GIS, and remote-sensing users can run this skill to assess pasture quality for a WGS84 area or local multi-year NDVI raster. It computes vegetation cover, phenology, degradation trend, quality rasters, and run metadata for local analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The authoritative security summary reports under-disclosed credential and network helper code, including hardcoded Earthdata credentials. <br>
Mitigation: Review the package before installation, remove hardcoded credentials and unrelated credential providers, and require explicit user opt-in for any network or credential behavior. <br>
Risk: The authoritative security guidance calls out network geocoding and home-directory caches that may not be clearly disclosed. <br>
Mitigation: Clearly disclose or disable network geocoding and home-directory cache behavior unless the user explicitly enables it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-pasture-quality-assessment) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, guidance] <br>
**Output Format:** [CLI guidance plus generated GeoTIFF rasters and JSON manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces pasture_quality.tif, fractional_cover.tif, degradation_slope.tif, phenology.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
