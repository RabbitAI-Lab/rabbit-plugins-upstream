## Description: <br>
Fuses crop distribution, hazard intensity, and NDVI anomaly to estimate agricultural disaster impact, classify mild, moderate, or severe damage, and generate field-level damage maps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to assess crop damage after floods, drought, or heat events by combining crop masks, hazard rasters, and NDVI inputs into severity maps and summary outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional bbox/AOI date-range mode can make external geospatial data requests and download or cache files. <br>
Mitigation: Confirm external data access is acceptable, use an output/cache directory you control, and review generated download metadata. <br>
Risk: Unpinned dependencies can make installs less reproducible. <br>
Mitigation: Use a pinned dependency lockfile or controlled environment before production use. <br>
Risk: Raster analysis results depend on input quality, raster alignment, and selected hazard and anomaly thresholds. <br>
Mitigation: Validate input rasters, CRS and shape compatibility, and threshold settings before using outputs for operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-agricultural-disaster-assessment) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, guidance, files] <br>
**Output Format:** [Markdown guidance with CLI commands; runtime outputs include GeoTIFF, GeoJSON, HTML, and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes affected_crops.tif, field_damage.geojson, report.html, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
