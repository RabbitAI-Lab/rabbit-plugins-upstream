## Description: <br>
Monitors glacier retreat by extracting multi-temporal NDSI glacier boundaries, vectorizing them, and reporting terminus retreat and area change. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to process synthetic or user-provided multi-temporal green/SWIR imagery into glacier boundary, area, and retreat-rate outputs for monitoring and inventory updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package bundles geocoding, network download, credential, and cache helpers that are not reflected in the offline-facing glacier CLI description. <br>
Mitigation: Review the package before installation for offline-only deployments, remove or disable unused helper modules, rotate any embedded credentials, and pin dependencies before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-glacier-retreat-monitoring) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [README](README.md) <br>
- [SKILL](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Configuration] <br>
**Output Format:** [GeoJSON, GeoTIFF, JSON, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces glacier boundary polygons, final-period glacier mask, retreat and area metrics, and an output manifest.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact script VERSION agrees, while artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
