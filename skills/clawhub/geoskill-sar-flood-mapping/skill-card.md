## Description: <br>
Maps flood extent from SAR backscatter using Otsu thresholding, morphological cleanup, optional DEM slope exclusion, and GeoJSON vectorization. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run local SAR flood extent mapping over a bounding box or input SAR GeoTIFF, with optional DEM slope masking and synthetic offline data for testing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release security summary reports unused or under-documented network and credential modules, embedded fallback Earthdata credentials, and home-directory cache behavior. <br>
Mitigation: Review before installing, prefer a cleaned package that removes unrelated vendored modules and hardcoded credentials, and document any retained network or cache behavior. <br>
Risk: The security guidance reports unpinned dependencies. <br>
Mitigation: Pin dependencies and scan the resolved environment before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sar-flood-mapping) <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance and shell commands; generated artifacts include GeoTIFF, GeoJSON, JSON statistics, and a JSON run manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can run fully offline in synthetic mode; local input mode expects a SAR intensity/backscatter GeoTIFF and can accept an optional DEM GeoTIFF.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata and script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
