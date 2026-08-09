## Description: <br>
Assesses VIIRS night-time light radiance against ecological thresholds to produce light-pollution grades, an ecological impact index, and a skyglow proxy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, conservation planners, and urban-lighting teams use this skill to assess light pollution over a bounding box or local VIIRS raster. It supports dark-sky reserve delineation, ecological light-environment assessment, and urban lighting planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes credential helper code and hardcoded Earthdata credentials that are not explained in the user-facing instructions. <br>
Mitigation: Remove or isolate unused credential modules and rotate the exposed credential before broad use. <br>
Risk: The documented CLI is local, but bundled helper modules can perform network geocoding, downloads, and caching. <br>
Mitigation: Document any optional online behavior clearly and review network-related modules before deployment. <br>
Risk: Dependencies are not pinned, which can make repeatability and supply-chain review harder. <br>
Mitigation: Pin dependencies and review the resolved environment before commercial use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-light-pollution-assessment) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, JSON, Guidance] <br>
**Output Format:** [Markdown guidance with bash examples; runtime outputs GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces light_pollution_grade.tif, ecological_impact.tif, skyglow_proxy.tif, light_pollution_params.json, and output-manifest.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
