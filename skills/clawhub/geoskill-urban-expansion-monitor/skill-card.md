## Description: <br>
Detects and quantifies urban expansion from multi-temporal built-up rasters for change analysis, index comparison, and assessment reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers and geospatial analysts use this skill to compare before and after built-up rasters, quantify expansion and contraction, and generate machine-readable and human-readable assessment reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Auto-download mode can produce urban-expansion reports from raw satellite bands that do not match the built-up raster inputs expected by the analysis. <br>
Mitigation: Prefer validated built-up rasters for before and after inputs, or review and disable the auto-download path when those inputs are not available. <br>
Risk: Bounding-box and date-range reports may be misleading if treated as planning-grade outputs before the skill adds a real built-up classification step and stronger input validation. <br>
Mitigation: Use bbox/date-range reports only as preliminary analysis and validate inputs, thresholds, and outputs before using results for planning or operational decisions. <br>
Risk: Unpinned geospatial and data-fetching dependencies can change behavior across installs. <br>
Mitigation: Pin and audit dependencies in controlled environments before relying on the skill for repeatable runs. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Guidance] <br>
**Output Format:** [Markdown guidance with bash examples; generated run artifacts include JSON, HTML, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI writes expansion-report.json, report.html, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
