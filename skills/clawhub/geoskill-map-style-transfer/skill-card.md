## Description: <br>
Transfer map styles via color mapping and histogram matching with style templates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to restyle local raster map data with histogram matching, predefined visual templates, and palette quantization. It can generate synthetic offline inputs for testing or process local GeoTIFF inputs into stylized map artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says the main style-transfer tool is local and coherent, but the package also ships unrelated credential, geocoding, download, and cache utilities that are not disclosed for this skill. <br>
Mitigation: Review the package before installation, run only the documented style-transfer entrypoint, and prefer a minimal release that excludes credential, network, and cache utilities not needed for map-style transfer. <br>
Risk: The security guidance notes that bundled helper modules can access credentials, make network requests, and write a persistent location cache if used. <br>
Mitigation: Do not provide credentials to this skill unless those behaviors are explicitly required and documented; run in an isolated environment when evaluating third-party releases. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-map-style-transfer) <br>
- [Publisher Profile](https://clawhub.ai/user/ruiduobao) <br>
- [README](artifact/README.md) <br>
- [Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Text] <br>
**Output Format:** [PNG image, GeoTIFF raster, JSON metadata, JSON run manifest, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include styled.png, styled.tif, style_meta.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
