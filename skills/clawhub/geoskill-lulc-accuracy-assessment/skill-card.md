## Description: <br>
Assesses land-use and land-cover classification rasters against reference samples using confusion-matrix metrics including OA, Kappa, PA, UA, and F1, with optional stratified random sampling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to evaluate classified land-use or land-cover rasters against reference labels, generate confusion-matrix accuracy metrics, and produce local report artifacts for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes network, download, and credential helper modules that are not needed for the main local accuracy-assessment workflow. <br>
Mitigation: Use a minimized build for deployment or remove unused geocoding, download, and credential modules before installing in sensitive environments. <br>
Risk: The security evidence reports embedded Earthdata credentials in the distributed package. <br>
Mitigation: Do not rely on bundled credentials; rotate any exposed credentials and supply required secrets through reviewed environment variables or a managed secret store. <br>
Risk: The security guidance recommends dependency pinning before deployment. <br>
Mitigation: Pin and review runtime dependencies such as numpy, rasterio, scipy, and scikit-learn before production or commercial use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-lulc-accuracy-assessment) <br>
- [README](artifact/README.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with CLI commands; generated artifacts include JSON metrics, an HTML report, an optional GeoTIFF, and a run manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally by default and supports synthetic offline data or a local two-band GeoTIFF input.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
