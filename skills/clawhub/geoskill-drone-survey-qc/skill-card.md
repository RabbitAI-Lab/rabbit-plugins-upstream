## Description: <br>
Automated quality inspection for UAV/drone survey deliverables including aerial images, orthomosaics, DSM/DEM, control points, and aerial triangulation reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial QA teams use this skill to inspect UAV survey deliverables for coverage, blur, seam, nodata, overlap, GSD, DSM/DEM, and control-point accuracy issues before acceptance reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports an under-scoped mode that can fetch external satellite data and cache it when bbox/date inputs are supplied without a local orthomosaic. <br>
Mitigation: Use explicit local file paths such as --orthomosaic for local-only runs, avoid bbox/date inputs unless external network access is acceptable, and set a controlled cache/output directory. <br>
Risk: The skill is a survey quality aid and does not replace certified survey inspection for legal or compliance decisions. <br>
Mitigation: Have qualified survey personnel review generated QC metrics, thresholds, and reports before acceptance or regulatory use. <br>
Risk: Dependency and threshold behavior can affect results, especially raster processing and sensor-specific blur calibration. <br>
Mitigation: Pin dependencies, review the QC standards configuration, and calibrate blur and accuracy thresholds for the project sensor and acceptance criteria. <br>


## Reference(s): <br>
- [QC standards configuration](references/qc_standards.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-drone-survey-qc) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance plus generated JSON, GeoJSON, CSV, HTML, manifests, and logs from the QC script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces qc.json, issues.geojson, image_quality.csv, control_point_residuals.csv, qc_report.html, request.json, dataset-manifest.json, output-manifest.json, and qa.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
