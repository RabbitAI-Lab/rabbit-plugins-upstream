## Description: <br>
Automated quality inspection for UAV/drone survey deliverables including aerial images, orthomosaics, DSM/DEM, control points, and aerial triangulation reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Survey, mapping, and geospatial engineering teams use this skill to inspect UAV survey deliverables for coverage, blur, seam, overlap, GSD, DSM/DEM nodata, and control-point residual issues before acceptance reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional bbox/date mode may contact Microsoft Planetary Computer and download or cache imagery for the area and dates supplied by the user. <br>
Mitigation: Use explicit local orthomosaic, DSM, camera-position, and control-point files for UAV deliverable acceptance; reserve remote bbox/date results for reference imagery. <br>
Risk: Downloaded public satellite imagery may be mistaken for the UAV deliverable that was supposed to be checked. <br>
Mitigation: Review request.json and dataset-manifest.json for the input mode and data source before relying on QC results in acceptance decisions. <br>


## Reference(s): <br>
- [QC standards thresholds](references/qc_standards.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-drone-survey-qc) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, CSV, GeoJSON, HTML, shell commands, guidance] <br>
**Output Format:** [Command guidance plus generated QC files: qc.json, issues.geojson, image_quality.csv, control_point_residuals.csv, qc_report.html, request.json, dataset-manifest.json, output-manifest.json, and qa.json.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes results to a local output directory; optional bbox/date mode may download and cache public Sentinel-2 imagery.] <br>

## Skill Version(s): <br>
2.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
