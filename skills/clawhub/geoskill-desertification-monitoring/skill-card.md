## Description: <br>
Fuses NDVI trend, albedo, and vegetation scarcity to grade desertification severity and produce raster and area-statistics outputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and land-management teams use this skill to analyze multi-epoch NDVI rasters or synthetic validation data for desertification severity, degradation hotspots, and restoration-effectiveness assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Undisclosed network, caching, downloader, and credential-handling code may surprise users expecting an offline raster-analysis skill. <br>
Mitigation: Review the package before installation and remove or clearly disclose those modules before deployment. <br>
Risk: Credential-handling code and hardcoded credentials can expose secrets or create unsafe default behavior. <br>
Mitigation: Eliminate hardcoded credentials and require users to provide secrets explicitly through documented local configuration. <br>
Risk: Unpinned dependencies can change behavior across installations. <br>
Mitigation: Pin runtime dependencies before production use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-desertification-monitoring) <br>
- [Semantic Versioning](https://semver.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with shell commands; generated analysis artifacts include GeoTIFF rasters, JSON area statistics, and a JSON run manifest.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces desertification grade, NDVI trend, and score rasters plus area statistics and an output manifest.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
