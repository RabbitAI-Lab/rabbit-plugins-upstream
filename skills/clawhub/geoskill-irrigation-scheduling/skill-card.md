## Description: <br>
Computes crop water demand with Penman-Monteith, runs a soil water balance, and triggers an irrigation calendar. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers, GIS analysts, and agricultural decision-support teams use this skill to estimate crop water demand, simulate soil water balance, and generate irrigation schedules for a supplied area of interest or local soil raster. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed vendored credential, geocoding, caching, and download helpers even though the main irrigation scheduler appears local. <br>
Mitigation: Review or remove unneeded vendored helpers and ask the publisher to document all network and credential behavior before installation. <br>
Risk: The release should be reviewed before use in sensitive environments because the security verdict is suspicious and dependency pinning is not documented. <br>
Mitigation: Pin and review dependencies, scan the package, and validate the vendored metadata before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-irrigation-scheduling) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files] <br>
**Output Format:** [Console text plus GeoTIFF and JSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes irrigation_requirement.tif, irrigation_calendar.json, and an output-manifest.json file when the manifest helper is available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
