## Description: <br>
Identifies and maps mineral distribution from hyperspectral imagery using SAM spectral angle mapping and continuum removal, outputting mineral class and confidence rasters plus a report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to classify local or synthetic hyperspectral imagery into mineral distribution and confidence outputs with SAM and continuum removal. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes credential, network/download, geocoding, and home-directory cache helpers that are not fully described by the user-facing offline workflow. <br>
Mitigation: Review the helper modules before installation, run in an isolated environment, and avoid using it where sensitive .netrc, geospatial project names, or shared Earthdata/OpenAI-style credentials are present unless the publisher clearly scopes or removes those helpers. <br>


## Reference(s): <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact Skill Definition](artifact/SKILL.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-hyperspectral-mineral-mapping) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, JSON] <br>
**Output Format:** [GeoTIFF rasters and JSON reports/manifests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces mineral class and confidence rasters, mineral_report.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script constant) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
