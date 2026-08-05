## Description: <br>
Retrieves shallow-water bathymetry from blue and green bands using the Stumpf log-ratio or Lyzenga linear transform, with calibration and accuracy assessment. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing practitioners use this skill to estimate shallow-water depth from blue and green spectral bands, either from a local multiband GeoTIFF or from synthetic offline test data. It supports Stumpf and Lyzenga retrieval methods, optional calibration points, and accuracy reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary reports broader credential, network, and download helpers than the stated bathymetry purpose. <br>
Mitigation: Review before installing, run the documented synthetic or local-input CLI path in an isolated environment, and restrict network access unless it is required. <br>
Risk: The server security guidance notes that bundled code can read local credential stores if imported or invoked. <br>
Mitigation: Avoid storing unrelated secrets in ~/.netrc or ~/.geoskill/secrets.json on systems where this package is used. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-bathymetry-estimation) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands] <br>
**Output Format:** [GeoTIFF raster, JSON manifest, JSON accuracy metrics, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary outputs include bathymetry.tif, accuracy.json, and output-manifest.json; synthetic mode is documented as offline.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
