## Description: <br>
Detects land surface changes from bi-temporal imagery using a Siamese fully convolutional change-detection network and outputs change probability maps, binary change maps, and change-region polygons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to run local GPU-accelerated bi-temporal land-surface change detection on GeoTIFF imagery or synthetic sample data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security summary rates the package suspicious because bundled geospatial helper modules include credential lookup, external geocoding, downloading, and home-directory caching capabilities beyond the stated offline workflow. <br>
Mitigation: Review the bundled helper modules before installing in sensitive environments, remove or split unused network and credential helpers when possible, and pin dependencies before deployment. <br>
Risk: The bundled model weights were trained on synthetic spectra, so real-imagery probability outputs are screening-level and not field-validated map-grade results. <br>
Mitigation: Validate outputs against representative real imagery and calibrated ground truth before relying on results for operational mapping or decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-change-detection-dl) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Analysis, Shell commands] <br>
**Output Format:** [GeoTIFF, GeoJSON, JSON manifest, and CLI status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces change_probability.tif, change_binary.tif, change_regions.geojson, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
