## Description: <br>
Detects bright or high-contrast objects in remote-sensing imagery using a local sliding-window and non-maximum suppression pipeline, then writes WGS-84 detection GeoJSON and a score raster. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and GIS or remote-sensing analysts use this skill to run local object detection on GeoTIFF or synthetic scenes and generate geospatial detections for inspection or downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes network, cache, and credential-handling helpers that are unrelated to the advertised offline detector. <br>
Mitigation: Install and run the skill only in an isolated environment without valuable credentials, or remove the unrelated helper modules before use. <br>
Risk: The offline and no-upload statements may not cover the bundled helper modules. <br>
Mitigation: Restrict network access for offline runs and review the packaged helpers before relying on the privacy claim. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/ruiduobao/skills/geoskill-object-detection-yolo) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, files] <br>
**Output Format:** [Console text plus GeoJSON, GeoTIFF, and JSON manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes detections.geojson, score_map.tif, and output-manifest.json under the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; entrypoint VERSION agrees; CHANGELOG and openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
