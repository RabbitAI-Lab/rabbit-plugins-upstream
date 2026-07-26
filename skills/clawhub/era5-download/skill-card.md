## Description: <br>
Download ERA5 single-level reanalysis data from Microsoft Planetary Computer without an API key, with support for temperature, precipitation, wind, pressure, and other climate variables. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and external users can use this skill to search for and download ERA5 climate reanalysis data from Microsoft Planetary Computer for a specified variable, date range, and optional geographic subset. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Place-name geocoding can send location queries to OpenStreetMap Nominatim. <br>
Mitigation: Use explicit --bbox values instead of --place for sensitive locations. <br>
Risk: Open-ended dependency requirements can resolve to newer package versions with different behavior. <br>
Mitigation: Install with a locked dependency set for reviewed or production environments. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/era5-download) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Files, JSON] <br>
**Output Format:** [Markdown guidance with bash commands; downloaded NetCDF, CSV, JSON, and optional QA JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports search, download, variable listing, bounding-box or place-based subsetting, output format selection, and quiet or verbose operation.] <br>

## Skill Version(s): <br>
0.3.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
