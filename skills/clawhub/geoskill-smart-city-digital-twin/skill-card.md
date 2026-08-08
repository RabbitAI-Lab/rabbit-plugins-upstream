## Description: <br>
Multi-source data fusion to build 3D scene configuration and API interface descriptions for a city digital twin. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial engineers use this skill to convert DEM/DSM or synthetic city data into digital twin scene assets, API descriptions, and completeness reports for downstream 3D engines. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Security evidence marks the release suspicious because extra reusable core code includes undisclosed credential-handling and network-capable helper behavior. <br>
Mitigation: Review before installation and require the publisher to document or remove network and credential helpers before deployment. <br>
Risk: Security guidance reports hardcoded credentials in the package. <br>
Mitigation: Do not deploy until the publisher removes hardcoded secrets and rotates any exposed credentials. <br>
Risk: Security guidance reports unpinned dependencies. <br>
Mitigation: Pin and review dependencies in a controlled environment before running the skill. <br>
Risk: Server-resolved provenance is unavailable for this version. <br>
Mitigation: Treat source provenance as unverified and avoid inferring GitHub origin from artifact text. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-smart-city-digital-twin) <br>
- [Semantic Versioning](https://semver.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands plus generated GeoTIFF, GeoJSON, JSON scene configuration, OpenAPI-style API specification, report, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written locally to the configured output directory; synthetic mode can run offline.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact CHANGELOG lists 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
