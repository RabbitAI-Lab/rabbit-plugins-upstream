## Description: <br>
Removes cloud contamination and enhances single-band remote-sensing imagery using a local U-Net and PatchGAN workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and remote-sensing practitioners use this skill to run local cloud-removal or image-enhancement workflows on single-band GeoTIFF imagery, with synthetic-data support for offline testing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled credential helper includes a hardcoded Earthdata fallback credential. <br>
Mitigation: Treat the exposed credential as compromised, rotate it if applicable, and remove or disable fallback defaults before deployment. <br>
Risk: Bundled helper modules include network geocoding, download, and credential lookup behavior that is not central to the documented local image-processing CLI. <br>
Mitigation: Review the package before installation, restrict network egress in sensitive environments, and remove or clearly disable unused helper modules. <br>
Risk: The model weights are trained on synthetic spectral pairs and are not field-calibrated for real satellite imagery. <br>
Mitigation: Use outputs for screening-level analysis only unless validated against representative ground truth for the intended area and sensor. <br>


## Reference(s): <br>
- [Skill documentation](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-generative-adversarial-rs) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF raster files, JSON metrics and run manifests, and console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include cloud_removed.tif or enhanced.tif, cloud_mask.tif for cloud-removal mode, metrics.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact CHANGELOG reports 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
