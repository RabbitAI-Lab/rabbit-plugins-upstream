## Description: <br>
Performs per-pixel semantic segmentation on multispectral remote-sensing imagery using sklearn KMeans or RandomForest classifiers, tiled prediction, and majority-filter post-processing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to segment local multispectral GeoTIFF imagery or synthetic scenes into pixel classes and generate class-area statistics for QA and downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that the advertised offline segmentation skill bundles unrelated online geocoding, downloading, and credential-handling code. <br>
Mitigation: Review or remove bundled shared core modules before deployment, and treat the package as not purely offline until the publisher documents the network, cache, and credential behavior. <br>
Risk: The security guidance recommends avoiding sensitive locations or local credential stores until a hardcoded credential fallback and scope concerns are resolved. <br>
Mitigation: Run with non-sensitive test data first, inspect credential handling, and deploy only after the credential fallback and module scope are reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-semantic-segmentation) <br>
- [README](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, text, shell commands] <br>
**Output Format:** [GeoTIFF raster, JSON files, and brief console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes segmentation.tif, class_stats.json, and output-manifest.json to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
