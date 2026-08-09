## Description: <br>
Computes confusion matrices, overall accuracy, mIoU, F1, Cohen's Kappa, and spatial accuracy maps for classification or segmentation model predictions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, data scientists, and geospatial analysts use this skill to evaluate classification or segmentation outputs against ground-truth label rasters and produce accuracy evidence for model review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes unrelated network, credential, cache, and downloader helpers that are not described by the skill. <br>
Mitigation: Review the package before installation and remove or split out unrelated helpers before production use. <br>
Risk: Security evidence reports an exposed Earthdata password in bundled credential helper code. <br>
Mitigation: Rotate the exposed credential and install only in a constrained test environment until the issue is fixed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-ai-accuracy-assessment) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [License](LICENSE) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, files, shell commands] <br>
**Output Format:** [JSON accuracy report, GeoTIFF spatial accuracy map, run manifest, and console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include accuracy_report.json, spatial_accuracy.tif, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
