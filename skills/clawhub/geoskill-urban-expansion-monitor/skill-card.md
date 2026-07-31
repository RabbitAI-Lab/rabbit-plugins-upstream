## Description: <br>
Detect and quantify urban expansion from multi-temporal built-up rasters for change analysis, raster comparison, index computation, and assessment reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT License <br>


## Use Case: <br>
Developers, geospatial analysts, and planning teams use this skill to compare before-and-after built-up rasters, quantify expansion and contraction, and generate machine-readable and human-readable urban expansion reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic bbox/date download mode may produce misleading urban-expansion reports from raw satellite imagery. <br>
Mitigation: Use validated before-and-after built-up rasters for planning or policy decisions, and treat auto-downloaded runs as preliminary until a proper built-up classification step is added. <br>
Risk: The skill can perform optional network downloads and writes local report files. <br>
Mitigation: Run it in a controlled environment with reviewed dependencies, a constrained output directory, and explicit approval for any network-backed data fetch. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-urban-expansion-monitor) <br>
- [Skill usage documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, files] <br>
**Output Format:** [Markdown guidance with CLI examples; generated JSON, HTML, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes expansion-report.json, report.html, and output-manifest.json to the configured output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script --version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
