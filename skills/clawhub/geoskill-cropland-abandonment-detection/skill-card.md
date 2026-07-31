## Description: <br>
Multi-year cropland abandonment detection using NDVI time series; identifies suspected abandoned cropland based on consecutive years without cultivation signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to screen cropland for suspected abandonment, generate field verification priorities, and monitor cultivation continuity from multi-year NDVI stacks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional download mode may present non-NDVI imagery as NDVI-based abandonment results. <br>
Mitigation: Use validated NDVI stacks where possible, or audit and correct the download path before relying on auto-downloaded outputs. <br>
Risk: Abandonment classifications can affect land-use decisions if treated as ground truth. <br>
Mitigation: Use generated suspected-field outputs as screening and field-verification priorities, with independent validation before operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-cropland-abandonment-detection) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Analysis, Configuration instructions] <br>
**Output Format:** [Markdown guidance with CLI examples; generated GeoTIFF, GeoJSON, HTML report, and JSON manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces abandonment_status.tif, suspected_fields.geojson, report.html, and output-manifest.json; supports synthetic input, user-provided NDVI stacks, and optional data download mode.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and CLI version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
