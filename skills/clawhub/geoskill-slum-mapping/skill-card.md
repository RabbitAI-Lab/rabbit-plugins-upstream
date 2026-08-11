## Description: <br>
Map slums and shanty areas using a multi-indicator index of texture, building density, night light and population density. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users, developers, and geospatial analysts can use this skill to run local raster-based slum or shanty-area mapping over a WGS84 bounding box or local GeoTIFF inputs. It supports settlement-environment analysis using texture, building density, population density, and night-light indicators. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package contains under-disclosed network, credential, and caching helpers, including hardcoded fallback credentials. <br>
Mitigation: Review before installation in sensitive environments; remove unused credential, geocoding, and download helpers or gate them behind explicit user opt-in and managed secrets. <br>
Risk: Slum or shanty-area mapping can be misused for enforcement, eviction, discrimination, or punitive targeting. <br>
Mitigation: Use only for aggregate settlement-environment monitoring with human rights, privacy, and governance review; prohibit individual, household, or punitive targeting. <br>
Risk: Optional location-resolution and cache behavior can create privacy or data-governance exposure when enabled. <br>
Mitigation: Prefer offline synthetic mode or local raster inputs, disable network and cache features unless needed, and clear any local location cache after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-slum-mapping) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, files] <br>
**Output Format:** [Markdown guidance with bash commands; runtime outputs include GeoTIFF and JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces slum_index.tif, slum_stats.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
