## Description: <br>
Estimates carbon stocks from NDVI-based biomass allometry and soil carbon density, producing aboveground carbon, soil carbon, total carbon GeoTIFFs, and summary JSON outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and environmental teams use this skill to run local screening-level carbon stock estimates for regional carbon baselines, dual-carbon target assessment, and ecological carbon sequestration measurement. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes helper code that can use network geocoding, write a home-directory cache, and read local credential stores, even though the advertised carbon-estimation command is local. <br>
Mitigation: Review the package before deployment in sensitive environments and restrict or remove helper paths that are not needed for the carbon-estimation workflow. <br>
Risk: Evidence reports embedded plaintext fallback credentials in the package. <br>
Mitigation: Remove or rotate the embedded credentials before release or installation, and verify that runtime credentials come only from approved local secret-management paths. <br>
Risk: The carbon model uses screening-level default allometry, root-to-shoot ratio, and soil carbon densities that may be unsuitable for project-level accounting. <br>
Mitigation: Calibrate scale, power, biomass, and soil-carbon parameters by region and vegetation type before using results for MRV, compliance, or financial decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-carbon-stock-estimation) <br>
- [SKILL.md](SKILL.md) <br>
- [README.md](README.md) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [GeoTIFF, JSON, Markdown, Python, YAML, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local geospatial raster outputs plus run summaries and manifests; real inputs are expected as local NDVI raster data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
