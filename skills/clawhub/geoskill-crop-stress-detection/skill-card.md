## Description: <br>
Detects crop stress by fusing CWSI water stress, red-edge chlorophyll, and SAR water content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to classify crop stress over a WGS84 bounding box or a local multiband GeoTIFF using local or synthetic raster inputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled helper code includes exposed Earthdata credentials and can read local credential stores. <br>
Mitigation: Review the package before installation, remove unused credential helpers when possible, and rotate or replace any exposed credentials before deployment. <br>
Risk: Bundled helper code includes network download and geocoding utilities that are not central to the visible local crop-stress command. <br>
Mitigation: Prefer synthetic or local-input mode for offline use, and remove or block unused network helpers if network access is not required. <br>
Risk: The skill writes GeoTIFF and JSON outputs to a user-specified directory. <br>
Mitigation: Run it in a controlled workspace and review output paths before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-crop-stress-detection) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>
- [Vendored geoskill core manifest](artifact/_geoskill_core/VENDORED.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Files, JSON] <br>
**Output Format:** [GeoTIFF raster, JSON run manifest, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a WGS84 bounding box or local GeoTIFF input; synthetic mode can run offline.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, target metadata, script VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
