## Description: <br>
Detects and classifies cropland changes from before/after NDVI rasters, identifies suspected construction, water, forest, and bare soil changes, and generates compliance investigation materials. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and compliance analysts use this skill to compare before/after NDVI GeoTIFFs or AOI/date-range imagery and prepare investigation materials for suspected cropland conversion. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote-download mode can generate compliance reports from satellite assets that are not verified NDVI rasters. <br>
Mitigation: Prefer verified local NDVI GeoTIFFs for compliance work and avoid relying on bbox/date-range auto-download mode for enforcement decisions until validation and NDVI derivation are fixed. <br>
Risk: Remote download may use outbound network access and local caching. <br>
Mitigation: Review network access before installation and set cache/output locations according to local data-handling requirements. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/ruiduobao/skills/geoskill-cropland-change-compliance) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown usage guidance plus generated HTML, JSON, GeoJSON, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generates report.html, compliance-report.json, suspected_changes.geojson, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and CLI --version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
