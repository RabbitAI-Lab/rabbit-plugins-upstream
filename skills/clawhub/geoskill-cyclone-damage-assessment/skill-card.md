## Description: <br>
Estimates cyclone-related wind speed, damage ratio, and pixel-wise loss using a Holland parametric wind field, precipitation and storm-surge effects, and exposure data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and disaster-risk teams use this skill to run local cyclone damage assessments over a bounding box or a local exposure GeoTIFF and generate geospatial loss outputs for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release includes extra network, geocoding, and credential-management code beyond the advertised local cyclone assessment workflow. <br>
Mitigation: Review and remove unused vendored modules before deployment, or restrict execution to the documented local command path. <br>
Risk: Evidence reports hardcoded Earthdata credentials in the package. <br>
Mitigation: Remove embedded credentials, rotate the account if the credentials are real, and require users to supply their own secrets through environment variables or a managed secret store. <br>
Risk: The package has mismatched release and artifact metadata. <br>
Mitigation: Confirm the intended release version and regenerate provenance or vendored metadata before publishing to sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-cyclone-damage-assessment) <br>
- [Semantic Versioning](https://semver.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, files] <br>
**Output Format:** [Markdown guidance plus GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Typical run artifacts include wind_speed.tif, damage_ratio.tif, loss.tif, cyclone_params.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact CHANGELOG.md and openai.yaml show 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
