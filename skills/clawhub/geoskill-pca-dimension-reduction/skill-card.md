## Description: <br>
Performs PCA dimension reduction on multi-band imagery and outputs principal-component GeoTIFFs, variance contribution statistics, and a loading matrix. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing practitioners use this skill to reduce correlated bands in local or synthetic multi-band imagery and inspect the retained principal components and explained variance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence says the package includes under-disclosed network, credential, cache, and downloader code that does not fit the advertised offline PCA workflow. <br>
Mitigation: Review the package before installation, require explicit opt-in for network or credential use, and ask the publisher to remove or clearly document the geocoding, downloader, cache, and credential modules. <br>
Risk: The security evidence calls out a hardcoded Earthdata password in bundled credential code. <br>
Mitigation: Delete and rotate the hardcoded credential before use, and rely only on user-managed secrets such as environment variables or local secret stores. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-pca-dimension-reduction) <br>
- [README](artifact/README.md) <br>
- [Skill source documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance for a Python CLI that produces GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill's CLI writes PCA component rasters, PCA statistics JSON, an output manifest, and optionally a reconstruction raster.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
