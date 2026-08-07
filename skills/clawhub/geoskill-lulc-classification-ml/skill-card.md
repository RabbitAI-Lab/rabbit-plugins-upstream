## Description: <br>
Classifies multispectral imagery into land-use and land-cover rasters using Random Forest or gradient boosting, with accuracy metrics, area statistics, optional majority filtering, and offline synthetic data generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing practitioners use this skill to run local land-use and land-cover classification workflows for regional mapping, inventory, teaching, validation, and pre-classification before change detection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package is flagged as suspicious because it includes undeclared credential and network helper modules, including hardcoded Earthdata credentials. <br>
Mitigation: Review or remove the unused credential, geocoding, and download helper modules before installation, and rotate the exposed Earthdata credential. <br>
Risk: Bundled code can read local credential stores such as ~/.netrc or ~/.geoskill/secrets.json when present. <br>
Mitigation: Avoid running the skill on machines with sensitive local credential files unless those files are isolated or the credential-reading code has been reviewed and accepted. <br>
Risk: Reported accuracy for real imagery may be misleading when the workflow uses pseudo-labels instead of independent ground-truth labels. <br>
Mitigation: Validate real-image outputs against independent labeled samples before relying on the reported accuracy metrics. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-lulc-classification-ml) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with bash command examples; runtime outputs include a GeoTIFF classification raster and JSON accuracy, area-statistics, and manifest files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally by default; synthetic mode requires no network access.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
