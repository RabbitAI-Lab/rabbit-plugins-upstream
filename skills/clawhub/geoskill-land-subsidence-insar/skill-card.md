## Description: <br>
Analyze land subsidence from InSAR displacement data for change analysis, hazard detection, and assessment reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Geospatial analysts, engineers, and developers use this skill to run land-subsidence analysis from displacement rasters or supported area/date inputs and generate machine-readable and human-readable assessment outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-downloaded Sentinel-1 GRD data is treated as a rough proxy and may not represent validated InSAR displacement. <br>
Mitigation: Use validated InSAR displacement rasters for real hazard, engineering, insurance, or policy decisions. <br>
Risk: Python dependencies are not pinned in requirements.txt. <br>
Mitigation: Install in a controlled environment and lock dependency versions before operational use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-land-subsidence-insar) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands; generated runtime outputs include JSON, HTML, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The analysis script writes subsidence-report.json, report.html, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
