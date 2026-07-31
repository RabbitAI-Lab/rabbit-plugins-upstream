## Description: <br>
Monitor surface disturbance at mining sites using multi-temporal optical, SAR, and DEM data to detect disturbance types, track changes across years, identify boundary violations, and generate area statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and mining compliance teams use this skill to analyze mine-boundary and imagery inputs, monitor surface disturbance over time, flag possible disturbances outside permit boundaries, and produce reviewable geospatial outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A bbox/date-only run can make outbound satellite-data queries and fall back to synthetic inputs, which may produce compliance-style outputs without clear real-data provenance. <br>
Mitigation: For monitoring or compliance use, provide explicit mine-boundary and imagery inputs, review generated manifests and files before relying on results, and treat outputs as untrusted unless provenance confirms real input data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-mine-disturbance-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and generated geospatial files such as GeoJSON, GeoTIFF, CSV, and JSON manifests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can create local output files including disturbance_by_year.geojson, outside_boundary.geojson, disturbance_type.tif, summary.csv, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
