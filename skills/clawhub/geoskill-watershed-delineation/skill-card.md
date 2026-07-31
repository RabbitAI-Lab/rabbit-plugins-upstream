## Description: <br>
Automates watershed delineation from DEM data by computing D8 flow direction, flow accumulation, watershed masks, stream networks, and summary statistics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to run watershed analysis from a local DEM, synthetic test data, or an auto-downloaded Copernicus DEM tile for a supplied bounding box or AOI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may make outbound requests to Microsoft Planetary Computer and store downloaded DEM or cache files locally. <br>
Mitigation: Run it only where that network access and local storage are acceptable, and set explicit output and cache directories for sensitive locations. <br>
Risk: The dependency set is not fully pinned, including geoskill-data-fetcher. <br>
Mitigation: Use a pinned or locked dependency set and verify the provenance of geoskill-data-fetcher before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-watershed-delineation) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, guidance, configuration] <br>
**Output Format:** [Markdown with bash commands and parameter guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI run produces GeoTIFF rasters, an HTML report, and output-manifest.json with parameters, output files, timestamps, and summary statistics.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and CLI --version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
