## Description: <br>
Detects crop rotation by encoding multi-year classifications into sequences, recognizing patterns, and counting frequencies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to classify multi-year crop sequences, identify rotation patterns, and produce frequency summaries for agricultural analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release includes network, downloader, and credential-management helpers that are broader than the stated local crop-rotation workflow. <br>
Mitigation: Review or remove the bundled helper modules before use, especially in environments containing sensitive .netrc or ~/.geoskill/secrets.json credentials. <br>
Risk: The authoritative security verdict is suspicious because the bundled helper code is under-disclosed relative to the offline-purpose documentation. <br>
Mitigation: Install only after security review and run in a constrained environment with only the credentials and network access required for the intended workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-crop-rotation-detection) <br>
- [README](README.md) <br>
- [LICENSE](LICENSE) <br>


## Skill Output: <br>
**Output Type(s):** [files, json, guidance] <br>
**Output Format:** [GeoTIFF rasters, JSON frequency report, JSON output manifest, and concise console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include rotation sequence and pattern rasters plus crop-rotation frequency statistics.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and executable VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
