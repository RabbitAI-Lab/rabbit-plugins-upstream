## Description: <br>
Assess crop health from NDVI time series for change analysis, hazard detection, and assessment reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and agricultural operators use this skill to run crop-condition monitoring from NDVI raster inputs or downloaded satellite preview data and produce human-readable and machine-readable reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-download mode can present visual satellite previews as NDVI crop-health analysis. <br>
Mitigation: Treat auto-download results as preview or proxy analysis, and use true red and near-infrared bands to compute NDVI before making real agricultural or hazard decisions. <br>
Risk: Unpinned dependencies can produce non-reproducible installs. <br>
Mitigation: Pin dependencies for reviewed deployments that require reproducible behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-crop-condition-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with CLI commands and generated JSON, HTML, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces crop-report.json, report.html, and output-manifest.json in the configured output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
