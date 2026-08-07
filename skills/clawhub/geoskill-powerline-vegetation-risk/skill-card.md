## Description: <br>
Identifies vegetation encroachment, rapid growth, and tree fall risks along powerline corridors and generates prioritized inspection points. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Utility maintenance teams, geospatial analysts, and agent developers use this skill to screen powerline corridors for vegetation encroachment, tree fall exposure, and inspection priorities. It supports local analysis from supplied GeoJSON inputs and optional remote imagery download when a bbox or AOI plus date range are provided. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive corridor coordinates can be sent to remote geospatial services when bbox or AOI plus date range are used. <br>
Mitigation: Use local image and GeoJSON inputs in restricted environments, or only use approved non-sensitive bbox/AOI values for remote-download mode. <br>
Risk: Generated request metadata and output manifests can persist raw run parameters, paths, bbox, date range, and download metadata. <br>
Mitigation: Review and redact request.json and output-manifest.json before sharing outputs outside the approved project context. <br>
Risk: Risk scores can be misleading if conductor height, vegetation height, fall direction, or imagery-derived tree information is incomplete. <br>
Mitigation: Treat outputs as inspection-prioritization evidence and require field or engineering verification before safety or maintenance decisions. <br>


## Reference(s): <br>
- [Risk scoring schema](references/risk_scoring.json) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-powerline-vegetation-risk) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, files, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; runtime outputs include GeoJSON, GeoTIFF, CSV, and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces risk points, risk segments, clearance raster, ranked inspection CSV, request metadata, output manifest, and QA JSON in the selected output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
