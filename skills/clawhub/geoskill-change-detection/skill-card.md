## Description: <br>
Detect and quantify land cover changes between two co-registered satellite images using NDVI difference, image differencing, or Change Vector Analysis (CVA). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run satellite image change detection workflows over co-registered raster imagery and produce change magnitude rasters, binary masks, vector outputs, and summary reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill claims local-only processing while also exposing a networked image-fetch workflow. <br>
Mitigation: Use local detect and report workflows when confidentiality matters; avoid fetch and place options if location, date, or project-interest disclosure is unacceptable. <br>
Risk: Unpinned geospatial dependencies can change behavior or supply-chain exposure over time. <br>
Mitigation: Install in a controlled environment and pin dependency versions before sensitive or repeatable production use. <br>
Risk: Misregistered imagery, clouds, cloud shadows, or cross-sensor differences can produce misleading change detections. <br>
Mitigation: Co-register inputs, mask clouds, compare similar seasons, and review output masks before using results for decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-change-detection) <br>
- [README](artifact/README.md) <br>
- [Skill Instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated workflow artifacts can include GeoTIFF, GeoJSON, JSON, and CSV files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires co-registered satellite imagery and local Python geospatial dependencies.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
