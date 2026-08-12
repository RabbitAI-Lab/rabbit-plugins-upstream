## Description: <br>
Detects newly invaded pixels from multi-temporal remote-sensing indices, computes relative spread rate, and predicts invasive-species risk from environmental suitability and distance decay. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
GIS, biodiversity, and environmental monitoring practitioners use this skill to analyze local or synthetic raster inputs for invasive-species spread, risk surfaces, and control-priority ranking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes helper code that can access local credential stores and external geocoding services if invoked. <br>
Mitigation: Review the package before installation and avoid placing sensitive credentials in ~/.netrc or ~/.geoskill/secrets.json unless the full package contents are trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-invasive-species-spread) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands; runtime outputs include GeoTIFF rasters, JSON statistics, and a JSON run manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces new_invasion.tif, invasion_risk.tif, invasive_params.json, and output-manifest.json when executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and executable VERSION constant) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
