## Description: <br>
Extracts urban and built-up areas from single-temporal SAR backscatter using Otsu or fixed sigma0 thresholding, GLCM contrast texture, and morphological closing, producing a binary urban extent GeoTIFF and area statistics JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to run local SAR urban or built-up area extraction workflows from a SAR sigma0 GeoTIFF or synthetic test scene. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Server security evidence flags the package as suspicious because it bundles network geocoding, downloader, persistent cache, and credential-management code that is not disclosed in the skill instructions. <br>
Mitigation: Review the package before installation, remove or clearly scope unused network and credential modules, and run only the documented local SAR mapping workflow when handling sensitive locations or credentials. <br>
Risk: Server security guidance notes hardcoded fallback credential behavior and recommends avoiding sensitive credentials unless the extra modules are removed or scoped. <br>
Mitigation: Rotate any exposed Earthdata credential and avoid providing API keys or other secrets to this package until the credential code is audited. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sar-urban-mapping) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, GeoTIFF, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF raster, JSON statistics and manifest files, and concise terminal status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include urban_mask.tif, urban_statistics.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
