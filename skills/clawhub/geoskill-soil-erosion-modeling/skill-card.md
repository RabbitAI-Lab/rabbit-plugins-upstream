## Description: <br>
Computes RUSLE-based soil erosion modulus from spatialized rainfall, soil, topography, vegetation, and conservation-practice factors, then outputs erosion modulus and intensity-grade GeoTIFFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and soil-and-water conservation planners use this skill to run local RUSLE-based erosion modeling for hotspot identification, conservation planning, and watershed sediment source analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports undisclosed network, download, caching, and credential code alongside a local erosion-modeling workflow. <br>
Mitigation: Audit or remove the extra modules before using the skill in sensitive environments, and run it with network restrictions unless online behavior is explicitly required. <br>
Risk: The security evidence reports hardcoded Earthdata credentials in packaged code. <br>
Mitigation: Rotate the exposed credentials and require users to provide their own secrets through approved local secret-management mechanisms. <br>
Risk: Dependencies are listed without pins. <br>
Mitigation: Pin and review numpy, rasterio, and scipy versions before deployment in controlled or commercial environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-soil-erosion-modeling) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; runtime outputs are GeoTIFF, JSON, and manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces erosion_modulus.tif, erosion_grade.tif, rusle_params.json, and output-manifest.json when executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
