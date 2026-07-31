## Description: <br>
Fuses crop distribution, hazard intensity, and NDVI anomaly to estimate agricultural disaster impact, classify damage severity, and generate field-level damage maps for flood, drought, or heat events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Agricultural analysts, geospatial developers, and emergency-response teams use this skill to assess crop damage from hazard rasters and NDVI changes, generate severity maps, and prioritize field inspection after disasters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional bbox/date-range operation may contact Microsoft Planetary Computer and cache downloaded geospatial data. <br>
Mitigation: Use local raster inputs when network access is not desired, and set an explicit cache directory for controlled deployments. <br>
Risk: The skill writes geospatial analysis outputs and reports to disk. <br>
Mitigation: Set an explicit output directory and review generated files before using them in operational decisions. <br>
Risk: Dependencies include unpinned geospatial packages. <br>
Mitigation: Pin and review dependencies before deployment in controlled or production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-agricultural-disaster-assessment) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Files, Shell commands] <br>
**Output Format:** [GeoTIFF raster, GeoJSON, HTML report, JSON manifest, and CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes affected_crops.tif, field_damage.geojson, report.html, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
