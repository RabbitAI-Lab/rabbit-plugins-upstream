## Description: <br>
Assesses snow avalanche susceptibility by combining slope, aspect, terrain roughness, snow depth, and temperature into a classified susceptibility map. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
GIS, climate, and geospatial engineering users can run this skill to generate local avalanche susceptibility outputs for a bounding box or a multi-band terrain GeoTIFF. The results support screening and analysis workflows, not emergency response decisions without expert review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review reports that the advertised avalanche CLI is mostly local, but bundled helper modules include credential access, geocoding, cache, and download behavior outside the offline-only purpose. <br>
Mitigation: Review the bundled helper modules before installation, remove or disable unused credential, geocoding, cache, and download helpers where possible, and install only after resolving any hardcoded credential concerns. <br>
Risk: Avalanche susceptibility outputs are model-derived screening artifacts and may be incorrect or incomplete for operational safety decisions. <br>
Mitigation: Use outputs for analysis with expert review, validate inputs and local conditions, and avoid using the generated maps as the sole basis for field safety or emergency decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-snow-avalanche-susceptibility) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>
- [Vendored core manifest](_geoskill_core/VENDORED.txt) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Analysis] <br>
**Output Format:** [GeoTIFF susceptibility rasters, JSON factor weights, and a JSON run manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include susceptibility.tif, susceptibility_level.tif, avalanche_params.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and CLI VERSION; changelog/openai.yaml list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
