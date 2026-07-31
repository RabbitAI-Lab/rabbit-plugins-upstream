## Description: <br>
Assess crop health from NDVI time series for change analysis, hazard detection, and local assessment reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Agronomists, GIS analysts, and developers use this skill to assess crop condition from NDVI raster time series, detect condition trends, and generate local crop-health reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-supplied geospatial files and writes reports, manifests, downloaded data, or synthetic inputs to local directories. <br>
Mitigation: Run it only against intended input and output directories, and review generated artifacts before sharing or downstream use. <br>
Risk: Optional public satellite-data downloads and geospatial Python dependencies can affect repeatability and operational exposure. <br>
Mitigation: Use pinned dependencies or a lockfile for repeatable installs, and enable downloads only when public external data access is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-crop-condition-monitor) <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [Crop condition monitor script](artifact/scripts/crop_condition_monitor.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration] <br>
**Output Format:** [CLI guidance plus generated JSON, HTML, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes outputs to a local directory and may download public Sentinel-2 L2A preview data when bbox or AOI and date-range inputs are supplied.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script --version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
