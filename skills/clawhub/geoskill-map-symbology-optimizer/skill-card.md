## Description: <br>
Optimize map symbology using color theory, contrast, visual hierarchy and accessible palettes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and map production teams use this skill to classify local raster or vector map data and produce accessible color symbology with contrast and color-vision checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes credential, geocoding, cache, and download helpers that are not disclosed by the documented local optimizer workflow. <br>
Mitigation: Audit the bundled helper modules before installation and remove or clearly disclose code that is outside the documented map symbology workflow. <br>
Risk: The security guidance warns against use in environments with sensitive netrc, geoskill secrets, or service credentials before review. <br>
Mitigation: Run the skill in a constrained environment without sensitive credentials unless those modules have been reviewed and explicitly approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-map-symbology-optimizer) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Analysis] <br>
**Output Format:** [PNG map image, GeoTIFF class raster, JSON symbology report, and JSON run manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally by default and supports synthetic offline input mode.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata; artifact CHANGELOG.md and openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
