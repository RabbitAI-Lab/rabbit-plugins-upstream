## Description: <br>
Detect forest disturbance from multi-temporal NDVI and generate assessment reports from local rasters or downloaded geospatial imagery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to compare baseline and current NDVI rasters, flag forest disturbance, and produce machine-readable and human-readable assessment outputs. It can also fetch imagery for a supplied AOI and date range when local raster inputs are not provided. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads user-provided raster files and writes reports, manifests, downloaded imagery, and cache files locally. <br>
Mitigation: Run it in a controlled workspace with explicit output and cache directories, then review generated files before sharing or using them downstream. <br>
Risk: When AOI and date inputs are used, the skill may contact Microsoft Planetary Computer and download geospatial imagery. <br>
Mitigation: Use trusted AOI/date inputs, apply normal network controls, and pin dependencies when reproducibility or supply-chain control matters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-forest-disturbance-alert) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, HTML, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; generated artifacts include JSON, HTML, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes disturbance-report.json, report.html, output-manifest.json, and optionally downloaded imagery or synthetic input rasters.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
