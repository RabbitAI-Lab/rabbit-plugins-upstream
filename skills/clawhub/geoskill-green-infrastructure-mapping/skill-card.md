## Description: <br>
Map green infrastructure from high-resolution NDVI, tree crown detection, green-space classification and patch connectivity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and environmental planning teams use this skill to generate green-space masks, NDVI summaries, tree-crown candidate counts, and patch-connectivity indicators from multispectral imagery or synthetic offline test data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The main mapping workflow is local, but bundled helper code includes credential and network functionality broader than the advertised offline NDVI workflow. <br>
Mitigation: Review before installing, run in a restricted environment, and remove or disable unused credential and network helper modules if they are not needed. <br>
Risk: Tree-crown candidate counts and connectivity values are heuristic and may not match field-validated tree inventories or planning-grade ecological assessments. <br>
Mitigation: Calibrate NDVI thresholds and tree-detection settings against trusted local imagery or ground truth before using outputs for operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-green-infrastructure-mapping) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with bash commands; generated artifacts are GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Main outputs are green_infrastructure.tif, green_stats.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and CLI VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
