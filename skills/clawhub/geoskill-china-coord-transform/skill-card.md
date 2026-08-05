## Description: <br>
Converts between WGS-84, GCJ-02, and BD-09 coordinates for approximate location display, control-point fitting, Helmert transforms, and GeoJSON/Shapefile batch conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT No Attribution License (MIT-0) <br>


## Use Case: <br>
Developers and GIS or data engineers use this skill to guide coordinate conversion workflows for China map systems, including approximate point conversion, control-point-based transforms, and batch vector file conversion. It is best suited to non-survey visualization and application workflows unless users supply and validate their own high-quality control points. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Approximate GCJ-02 conversion can produce materially inaccurate coordinates and may be unsuitable for regulated or high-accuracy location decisions. <br>
Mitigation: Use approximate conversion only for non-survey visualization or product-display workflows; for high-accuracy needs, use validated local control points with affine or Helmert methods and review legal or operational requirements. <br>
Risk: The release artifact appears to contain documentation and requirements only, so advertised Python modules and CLI commands may not run unless supplied elsewhere. <br>
Mitigation: Confirm the implementation files are available and tested before relying on the skill for execution. <br>
Risk: Optional Shapefile support depends on pyshp with only a lower-bound requirement. <br>
Mitigation: Pin pyshp to a reviewed version in deployment environments that process Shapefiles. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-china-coord-transform) <br>
- [qgis-geohey-toolbox](https://github.com/GeoHey-Team/qgis-geohey-toolbox) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with Python and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe coordinate-conversion parameters, CLI invocations, Python usage, and file-conversion guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
