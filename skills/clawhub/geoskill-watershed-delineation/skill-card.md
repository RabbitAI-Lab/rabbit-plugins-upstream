## Description: <br>
Automated watershed delineation from DEM. Computes D8 flow direction, flow accumulation, delineates watersheds from outlet points, extracts stream networks, and generates statistics. Use when the user wants to delineate a watershed, compute flow accumulation, extract streams, or analyze hydrological characteristics from a DEM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, geospatial analysts, and hydrology practitioners use this skill to run watershed delineation from a DEM, including D8 flow direction, flow accumulation, stream extraction, watershed masks, and summary reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill writes GeoTIFF rasters, an HTML report, a JSON manifest, and optional downloaded DEM files to local directories. <br>
Mitigation: Run it with an explicit output directory and, in stricter environments, restrict output and cache paths to approved locations. <br>
Risk: When invoked with bbox or AOI inputs and no local DEM, the skill may contact Microsoft Planetary Computer to download public DEM data. <br>
Mitigation: Use a local DEM for offline runs, or restrict network access when external public data downloads are not allowed. <br>
Risk: The dependency list is not fully pinned. <br>
Mitigation: Pin and review dependencies before deployment in controlled or production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-watershed-delineation) <br>
- [Publisher profile](https://clawhub.ai/user/ruiduobao) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Files] <br>
**Output Format:** [Markdown guidance with CLI commands; generated artifacts are GeoTIFF rasters, an HTML report, and a JSON manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local output directories and optionally download a public Copernicus DEM tile when bbox or AOI inputs are used.] <br>

## Skill Version(s): <br>
3.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
