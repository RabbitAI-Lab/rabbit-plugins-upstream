## Description: <br>
SAR soil moisture retrieval skill that analytically estimates bare-soil volumetric water content from SAR backscatter, incidence angle, and surface roughness using simplified Dubois/Oh semi-empirical models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, analysts, and agricultural or hydrology practitioners can use this skill to retrieve soil moisture from local SAR backscatter GeoTIFFs or synthetic scenes for farmland monitoring, drought assessment, hydrological model assimilation, and irrigation planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes credential handling, embedded fallback credentials, network geocoding, and persistent location caching that are not aligned with the advertised offline-only posture. <br>
Mitigation: Review before installing, remove embedded credentials or split unrelated helpers, disclose network calls and cache paths, pin dependencies, and avoid using the package with sensitive locations or local credential files until those issues are addressed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sar-soil-moisture) <br>
- [README](artifact/README.md) <br>
- [Skill documentation](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, files, json, guidance] <br>
**Output Format:** [CLI guidance plus GeoTIFF output, JSON statistics, and JSON run manifest files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces soil_moisture.tif, soil_moisture_stats.json, and output-manifest.json in the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact openai.yaml and CHANGELOG list 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
