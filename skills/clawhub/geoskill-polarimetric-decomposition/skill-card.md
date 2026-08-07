## Description: <br>
Performs polarimetric SAR decomposition with Cloude-Pottier H/A/alpha and simplified Freeman-Durden methods, producing scattering entropy, anisotropy, scattering angle, and scattering power outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing engineers use this skill to extract physical scattering features from fully polarimetric SAR GeoTIFF inputs or synthetic test scenes for land-cover analysis, forestry monitoring, crop monitoring, and feature engineering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper modules include network geocoding, download, and credential-handling capability beyond the advertised local SAR decomposition workflow. <br>
Mitigation: Review the package before installing, remove or disable unrelated helper modules when they are not needed, and run the skill in a restricted environment. <br>
Risk: The package may inspect credential stores and the security guidance calls out exposed Earthdata credentials. <br>
Mitigation: Rotate exposed credentials, audit credential handling before deployment, and provide only scoped credentials when credential-dependent helpers are required. <br>
Risk: Local-only operation can be weakened if workflows invoke geocoding or download helper paths. <br>
Mitigation: Use explicit local inputs, bounding boxes, or synthetic data for offline runs, and block network egress where local-only processing is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-polarimetric-decomposition) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF and JSON files, with concise text guidance and shell commands when invoked by an agent] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes decomposition rasters, statistics, and an output manifest to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
