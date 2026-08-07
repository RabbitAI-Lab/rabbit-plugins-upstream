## Description: <br>
Detects heatwaves, cold spells, and heavy rainfall from temperature or precipitation time series using percentile thresholds, then reports event intensity, duration, spatial extent, an event-list JSON, and a spatial raster. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and climate-risk teams can use this skill to catalog extreme weather events from local multi-temporal rasters or synthetic validation data. It supports heatwave, cold-spell, and heavy-rainfall screening with per-event statistics and geospatial output files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes under-disclosed network and credential-handling code unrelated to the main local weather detector. <br>
Mitigation: Review before installing, remove or clearly disclose unrelated geocoding, download, and credential modules, and make network or cache behavior opt-in. <br>
Risk: The security review reports hardcoded Earthdata credentials and possible reading of unrelated local secrets. <br>
Mitigation: Remove and rotate hardcoded credentials, avoid reading unrelated local secrets, and require users to provide credentials explicitly through documented configuration. <br>
Risk: The security review recommends dependency pinning before use. <br>
Mitigation: Pin runtime dependencies and review dependency updates before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-extreme-weather-detection) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>
- [Artifact license](artifact/LICENSE) <br>


## Skill Output: <br>
**Output Type(s):** [Files, JSON, Geospatial raster, Text] <br>
**Output Format:** [GeoTIFF raster, JSON event list, JSON run manifest, and command-line status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are written to a local output directory and may include synthetic-data validation artifacts.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
