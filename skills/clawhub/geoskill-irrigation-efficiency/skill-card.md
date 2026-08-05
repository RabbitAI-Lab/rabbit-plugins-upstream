## Description: <br>
Computes irrigation water demand from crop evapotranspiration and effective precipitation, and assesses the spatial distribution of irrigation efficiency. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External developers, GIS analysts, and agricultural water-management teams use this skill to run local raster-based irrigation demand, efficiency, and water-deficit analysis for irrigation districts, allocation planning, and drought or shortage assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security evidence reports that the package bundles auxiliary credential, network, and cache helpers, including a plaintext Earthdata password, even though the main irrigation workflow is local. <br>
Mitigation: Review the bundled helpers before installation, run in a constrained environment, avoid exposing personal API keys or .netrc secrets, and require the publisher to remove or scope credential handling before trusted deployment. <br>
Risk: Auxiliary code can access local credentials, call external geocoding services, and write a home-directory cache. <br>
Mitigation: Limit network and home-directory access where possible, and install only in environments where those capabilities are acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-irrigation-efficiency) <br>
- [README](README.md) <br>
- [Skill instructions](SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Text] <br>
**Output Format:** [GeoTIFF rasters, JSON report and manifest files, and brief console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces irrigation_demand.tif, irrigation_efficiency.tif, water_deficit.tif, irrigation_report.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and main script VERSION; local openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
