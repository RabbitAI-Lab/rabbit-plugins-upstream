## Description: <br>
Fuses multispectral and panchromatic imagery with Brovey or IHS pan-sharpening to create higher spatial resolution raster outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and remote-sensing practitioners use this skill to run local pan-sharpening on multispectral and panchromatic GeoTIFF inputs, or on synthetic data for offline testing. The skill produces fused imagery plus JSON parameters and run manifests for inspection. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports under-disclosed geocoding, credential, cache, and download helpers that are unrelated to the advertised pan-sharpening workflow. <br>
Mitigation: Review the package before installation or execution, and remove or clearly gate unrelated helper code before deployment. <br>
Risk: The security guidance calls out a hardcoded credential and unpinned dependencies. <br>
Mitigation: Remove hardcoded credentials, avoid placing real secrets in artifacts, and pin dependencies before production use. <br>
Risk: The security verdict is suspicious even though the documented entrypoint appears suitable for local pan-sharpening. <br>
Mitigation: Limit execution to reviewed local workflows and re-scan the release after the security guidance has been addressed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-image-fusion-pan-sharpening) <br>
- [Artifact README](README.md) <br>
- [Artifact SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [files, JSON, shell commands, guidance] <br>
**Output Format:** [GeoTIFF and JSON files, with CLI text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates fused_pansharpened.tif, fusion_params.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
