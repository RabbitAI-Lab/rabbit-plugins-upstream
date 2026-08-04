## Description: <br>
Detect forest disturbance from multi-temporal NDVI and generate assessment reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and environmental teams use this skill to compare baseline and current NDVI rasters, identify disturbance severity, and produce local reports for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unpinned Python dependencies can make installs less reproducible. <br>
Mitigation: Review and pin Python dependencies before production deployment. <br>
Risk: Auto-download mode contacts Microsoft Planetary Computer and writes imagery to cache and output paths. <br>
Mitigation: Choose cache and output directories deliberately, especially when working with sensitive project data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-forest-disturbance-alert) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, HTML, Shell commands] <br>
**Output Format:** [CLI output plus local JSON and HTML report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes disturbance-report.json, report.html, output-manifest.json, and optional downloaded or synthetic raster inputs to the selected output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
