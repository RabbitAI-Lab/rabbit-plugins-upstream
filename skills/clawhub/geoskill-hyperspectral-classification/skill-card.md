## Description: <br>
Performs per-pixel supervised hyperspectral image classification using PCA dimensionality reduction with Random Forest or SVM classifiers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing practitioners use this skill to classify hyperspectral raster pixels into land-cover classes and compare PCA plus Random Forest or SVM workflows on synthetic or local GeoTIFF data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Server security review reports that the package ships undisclosed geocoding, downloader, cache, and credential-handling modules beyond the stated offline classifier purpose. <br>
Mitigation: Install only after the publisher removes those modules or clearly documents why they are included and how their network, cache, and credential behavior is controlled. <br>
Risk: Server security guidance identifies a hardcoded credential fallback as a security hygiene issue. <br>
Mitigation: Review credential-handling code before execution and require explicit user-provided credentials or disabled credential paths for deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-hyperspectral-classification) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [Semantic Versioning](https://semver.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Code, Shell commands, Analysis] <br>
**Output Format:** [GeoTIFF classification raster, JSON accuracy report, JSON output manifest, and console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written locally to the selected output directory; synthetic mode can run without external input data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION; artifact CHANGELOG.md and openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
