## Description: <br>
Analyze vegetation recovery at mining sites by comparing pre-mining and post-reclamation NDVI rasters, generating reports and recovery statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Geospatial analysts, environmental consultants, and developers use this skill to assess mine reclamation progress from NDVI raster inputs and produce machine-readable and human-readable recovery reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The documented bbox/date workflow may make outbound requests for AOI and date parameters and may cache local geospatial data. <br>
Mitigation: Confirm the target environment permits those outbound requests and review cache location and retention before use. <br>
Risk: The documentation mentions flags that the included script does not currently accept, which may cause setup or runtime failures. <br>
Mitigation: Run a small local validation command before operational use and rely on the script-supported raster input workflow when unsupported flags fail. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-mine-reclamation-monitor) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; generated artifacts include JSON and HTML reports.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The documented workflow writes reclamation-report.json, report.html, and output-manifest.json to an output directory.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
