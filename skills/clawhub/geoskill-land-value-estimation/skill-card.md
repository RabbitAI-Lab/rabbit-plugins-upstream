## Description: <br>
Estimate land value with a hedonic price model driven by accessibility, POI density and green proximity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, GIS analysts, and location-analysis teams use this skill to estimate spatial land value from local feature rasters or synthetic data using a linear hedonic model. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes unrelated network, downloader, cache, and credential-handling helpers beyond the advertised local land-value workflow. <br>
Mitigation: Review and sandbox the package before installation; remove unused helpers or restrict execution to the main CLI and synthetic or local input modes. <br>
Risk: Credential-related helpers may read local credential stores or use embedded fallback credentials. <br>
Mitigation: Run in an environment without sensitive secrets unless the package is cleaned up, and avoid supplying API keys to the runtime. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-land-value-estimation) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Shell commands, Guidance] <br>
**Output Format:** [GeoTIFF and JSON files with concise command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a land value raster, hedonic coefficients, value statistics, and an output manifest.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
