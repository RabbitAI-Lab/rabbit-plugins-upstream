## Description: <br>
RUSLE soil erosion modeling with a Sediment Delivery Ratio (SDR) estimates watershed sediment yield and identifies key sediment source areas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and watershed modelers use this skill to run local sediment-yield analyses from a WGS84 bounding box or local raster inputs, including an offline synthetic-data mode for testing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled credential, download, and geocoding helpers conflict with the documented offline privacy posture. <br>
Mitigation: Review the package before installation and remove or clearly document unused credential and network helpers before broad use. <br>
Risk: The security evidence calls out hardcoded credentials and sensitive-service helpers. <br>
Mitigation: Do not run the skill in environments containing Earthdata, OpenAI, FIRMS, EOG, CMA, or similar secrets until those helpers and defaults have been reviewed. <br>
Risk: Unpinned dependencies may change behavior across installations. <br>
Mitigation: Pin and review runtime dependencies before production or shared-environment deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sediment-transport-modeling) <br>
- [README](README.md) <br>
- [CHANGELOG](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance for running a Python CLI; the tool writes GeoTIFF and JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Primary generated files are result.tif and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
