## Description: <br>
Classifies local or synthetic remote-sensing imagery with a NumPy-equivalent few-shot prototype classifier and outputs a classification raster. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to classify multispectral raster imagery with 1-5 support samples per class, run synthetic offline examples, and inspect episode accuracy and confidence reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review found undocumented network, download, cache, and credential-handling modules bundled alongside the offline classifier. <br>
Mitigation: Review the bundled modules before routine use, remove or clearly gate capabilities that are not needed, and run offline synthetic or local-file workflows without credentials unless those extra modules have been approved. <br>
Risk: Few-shot raster classification with very small support sets can produce misleading labels or confidence estimates if the support samples are not representative. <br>
Mitigation: Validate outputs with held-out labels or domain review, inspect few_shot_report.json before using results downstream, and document input data assumptions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-few-shot-classification) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces classification.tif, few_shot_report.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
