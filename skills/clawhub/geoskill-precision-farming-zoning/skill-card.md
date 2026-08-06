## Description: <br>
Standardizes multi-source geospatial layers, uses K-means to create precision-farming management zones, and produces per-zone recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers, agronomists, and geospatial analysts use this skill to convert local or synthetic agricultural raster layers into K-means management zones with zone-level irrigation, fertilization, and scouting advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Packaged helper code includes undocumented network geocoding and hardcoded service credentials. <br>
Mitigation: Review or remove unused credential and geocoding helper code before installation, and rotate or remove embedded credentials. <br>
Risk: The package has a suspicious security verdict despite a mostly local advertised zoning workflow. <br>
Mitigation: Run it in an isolated environment, prefer local or synthetic input when network access is not intended, and inspect generated files before downstream use. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Skill definition](SKILL.md) <br>
- [Changelog](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Geospatial raster, Text guidance] <br>
**Output Format:** [GeoTIFF management-zone raster, JSON zone recommendations, JSON run manifest, and console text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local GeoTIFF input or synthetic offline data; writes outputs to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata, target metadata, and runtime VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
