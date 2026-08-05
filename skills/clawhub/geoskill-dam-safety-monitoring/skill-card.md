## Description: <br>
Assesses dam safety risk by combining InSAR deformation, water level change, NDVI anomaly, and thermal infrared seepage signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and infrastructure safety teams can use this skill to run local or synthetic dam-safety remote-sensing checks for a specified area of interest and produce reviewable geospatial outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports under-disclosed credential and network helper code, including a hardcoded Earthdata password. <br>
Mitigation: Review before installation, remove committed credentials, and rely on user-controlled environment variables, .netrc, or an external secrets file before routine use. <br>
Risk: The security evidence says external geocoding and home-directory caches are not fully documented or disabled. <br>
Mitigation: Use synthetic or local-input mode for privacy-sensitive work, and document or disable network lookups and cache locations before deployment. <br>
Risk: The security guidance says dependencies should be pinned before routine use. <br>
Mitigation: Pin and review geospatial dependencies, then scan the resolved environment before production or shared deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-dam-safety-monitoring) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands] <br>
**Output Format:** [GeoTIFF raster, JSON manifest, and CLI text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The documented output directory contains result.tif and output-manifest.json; synthetic mode can run without network access.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
