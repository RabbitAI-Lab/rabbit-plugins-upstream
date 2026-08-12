## Description: <br>
Detect parking lots using asphalt spectral signature, regular row and column texture, and painted marking density. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to identify parking-lot candidates in local multispectral GeoTIFFs or offline synthetic test scenes for urban facility surveys and land-use mapping. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Evidence security reports that the visible detector runs locally, but the package also includes unrelated credential, geocoding, and downloader code plus a hardcoded Earthdata password that are not disclosed to users. <br>
Mitigation: Review the package before installing, avoid the bundled credential and place helpers unless their network and credential-store behavior is acceptable, and remove or disclose unused modules and rotate the password before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-parking-lot-detection) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, files] <br>
**Output Format:** [Markdown guidance with CLI examples; generated GeoTIFF and JSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces parking_score.tif, parking_stats.json, and output-manifest.json when executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
