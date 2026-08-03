## Description: <br>
Extract flood extent from SAR backscatter imagery for change analysis, hazard detection, and assessment reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial operators use this skill to run flood extent analysis from a local SAR raster or a Sentinel-1 GRD scene fetched for a specified area and date range. It produces machine-readable statistics and a human-readable assessment report for downstream review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Geospatial Python dependencies and the shared data fetcher are resolved from the installation environment. <br>
Mitigation: Install in a controlled environment and prefer pinned dependency versions before production use. <br>
Risk: Auto-download mode fetches public Sentinel-1 GRD data and writes downloaded assets under the chosen output directory. <br>
Mitigation: Use local SAR input when network access is not desired, and review output paths and downloaded data before sharing results. <br>
Risk: Flood extent results depend on SAR calibration, scene suitability, and the selected backscatter threshold. <br>
Mitigation: Validate source imagery, threshold settings, and generated reports before using outputs for operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-flood-extent-mapping) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, code, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with bash commands; runtime outputs include JSON, HTML, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes flood-report.json, report.html, and output-manifest.json under the selected output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
