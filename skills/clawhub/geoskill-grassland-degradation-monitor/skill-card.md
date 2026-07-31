## Description: <br>
Monitor grassland degradation and recovery trends from multi-temporal vegetation cover, phenology, bare ground and climate baselines, then output management zones for restoration prioritization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial analysts use this skill to assess grassland health, identify degraded areas, evaluate restoration effectiveness, and generate management recommendations from multi-temporal remote sensing and climate baseline data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote-download mode may send location and date parameters and download satellite assets when bbox, AOI, and date-range inputs are used. <br>
Mitigation: Run in a controlled environment, prefer explicit local --input-ndvi inputs for sensitive locations, and use bbox or AOI remote downloads only when that data sharing is intended. <br>
Risk: Generated request and manifest files may include request metadata. <br>
Mitigation: Review request.json and output-manifest.json before sharing analysis outputs. <br>


## Reference(s): <br>
- [Degradation Classification Schema](references/degradation_schema.json) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-grassland-degradation-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files] <br>
**Output Format:** [Markdown guidance with CLI examples; generated analysis artifacts include GeoTIFF, GeoJSON, CSV, and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include degradation status, trend maps, priority restoration areas, management summaries, time series, request metadata, an output manifest, and QA checks.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
