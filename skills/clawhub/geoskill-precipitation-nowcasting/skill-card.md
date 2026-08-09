## Description: <br>
Optical-flow Lagrangian persistence nowcasting that extrapolates precipitation fields 0-6 hours ahead and outputs a forecast GeoTIFF stack plus displacement-field JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and weather or geospatial analysts use this skill to generate very-short-range precipitation forecasts from local multi-band radar or satellite GeoTIFF input, or from synthetic offline test data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes undisclosed network, credential, and provenance-risk code outside the documented offline precipitation-nowcasting workflow. <br>
Mitigation: Review before installing and remove or clearly document unrelated credential, download, and geocoding helpers before deployment. <br>
Risk: Security evidence reports an exposed Earthdata fallback credential. <br>
Mitigation: Remove the fallback credential and rotate it before any release or use in sensitive environments. <br>
Risk: Dependencies are not pinned. <br>
Mitigation: Pin dependencies and review transitive packages before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-precipitation-nowcasting) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated files include a multi-band GeoTIFF forecast stack, displacement JSON, and output-manifest JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Forecast lead times are configurable up to the documented 0-6 hour nowcasting window; outputs are written locally.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact changelog and openai.yaml state 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
