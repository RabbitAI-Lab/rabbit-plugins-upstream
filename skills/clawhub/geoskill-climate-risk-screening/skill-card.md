## Description: <br>
Assess climate hazards from temperature and precipitation data when a user wants to analyze changes, detect hazards, or generate assessment reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and geospatial practitioners use this skill to screen heat and drought exposure from local temperature and precipitation rasters or optional NASA POWER climate data, then produce machine-readable and human-readable assessment reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional NASA POWER fetching can send geospatial and date inputs to an external climate-data service. <br>
Mitigation: Use local raster-file mode when locations or date ranges are sensitive, and review outbound data-fetching behavior before installation. <br>
Risk: Dependencies and climate-data libraries may change behavior or introduce supply-chain exposure over time. <br>
Mitigation: Pin and review dependencies in a controlled environment before operational use. <br>
Risk: Climate-risk summaries may be misleading when source rasters, bounding boxes, or date ranges are unsuitable for the decision being made. <br>
Mitigation: Validate input data quality and treat generated reports as screening outputs that need domain review before consequential use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-climate-risk-screening) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, files] <br>
**Output Format:** [Markdown guidance with bash commands; generated artifacts include JSON, HTML, and an output manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can be generated from local rasters, synthetic data, or optional NASA POWER downloads and are written to a user-selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
