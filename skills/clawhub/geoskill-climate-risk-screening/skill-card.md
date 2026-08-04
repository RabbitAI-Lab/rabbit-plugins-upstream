## Description: <br>
Assess climate hazards from temperature and precipitation data, including local raster inputs or NASA POWER data downloaded for a bounding box and date range. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and climate-risk reviewers use this skill to generate climate hazard statistics and reports from temperature and precipitation data. It supports file-based raster analysis and optional NASA POWER download mode for area and date range screening. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: NASA POWER download mode can make external requests and cache downloaded data locally. <br>
Mitigation: Use local rasters for stricter environments, set an explicit cache and output directory, and avoid submitting sensitive areas or dates unless approved. <br>
Risk: The skill depends on geospatial and data-processing packages that may change over time. <br>
Mitigation: Pin or review dependencies before installation in controlled environments. <br>
Risk: Generated reports summarize climate screening results and may be shared outside the execution environment. <br>
Mitigation: Review generated JSON, HTML, and manifest outputs before distributing them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-climate-risk-screening) <br>
- [Skill usage documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; generated JSON, HTML, and manifest files when the script is executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces climate-report.json, report.html, and output-manifest.json; optional download mode can cache NASA POWER data locally.] <br>

## Skill Version(s): <br>
2.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
