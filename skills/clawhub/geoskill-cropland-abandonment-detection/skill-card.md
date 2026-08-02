## Description: <br>
Multi-year cropland abandonment detection using NDVI time series. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to screen for suspected abandoned cropland, generate field verification priorities, and monitor cultivation continuity from multi-year NDVI stacks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The optional download mode may disclose sensitive AOIs or date ranges to external data services. <br>
Mitigation: Use vetted local NDVI stacks for sensitive work, or only use download mode when sharing the AOI and date range is acceptable. <br>
Risk: The optional download mode can feed non-NDVI imagery into NDVI-based results, which may make abandonment outputs scientifically unreliable. <br>
Mitigation: Prefer validated NDVI stacks, review the output manifest and downloaded inputs, and treat auto-download results as screening outputs requiring field or data validation. <br>
Risk: Unexpected output or cache locations can make data handling harder to audit. <br>
Mitigation: Set explicit output and cache directories before running the script. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-cropland-abandonment-detection) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands and generated GeoTIFF, GeoJSON, HTML, and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces abandonment_status.tif, suspected_fields.geojson, report.html, and output-manifest.json when the detection script is run.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
