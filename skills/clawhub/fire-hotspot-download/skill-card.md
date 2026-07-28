## Description: <br>
Downloads MODIS and VIIRS active fire hotspot data from NASA FIRMS with date range, bounding box, instrument, and output format options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, analysts, and geospatial teams use this skill to download NASA FIRMS MODIS and VIIRS active fire hotspot data for monitoring, air quality studies, land management, and geospatial analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bundled credential helper includes plaintext Earthdata credential defaults. <br>
Mitigation: Remove the embedded defaults, rotate the affected credential, and require users to provide secrets through environment variables, netrc, or a local secrets file. <br>
Risk: API keys can be stored locally and may appear in request URLs or verbose diagnostic output. <br>
Mitigation: Prefer FIRMS_API_KEY from the environment, avoid verbose mode with real keys, and review shell history and logs after use. <br>
Risk: Unresolved place names may be sent to third-party geocoding services. <br>
Mitigation: Use explicit bounding boxes or offline presets for sensitive locations, and document when online geocoding fallback is enabled. <br>
Risk: Dependencies are not pinned to exact versions. <br>
Mitigation: Pin dependency versions and review updates before installing in production or shared environments. <br>


## Reference(s): <br>
- [NASA FIRMS API documentation](https://firms.modaps.eosdis.nasa.gov/api/) <br>
- [NASA FIRMS MAP_KEY registration](https://firms.modaps.eosdis.nasa.gov/api/map_key/) <br>
- [Fire Information for Resource Management System citation](https://doi.org/10.1109/TGRS.2009.2014067) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/fire-hotspot-download) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Files, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; generated data files are CSV, GeoJSON, and optional JSON QA summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a NASA FIRMS API key and may call NASA FIRMS plus online geocoding services when place-name resolution is used.] <br>

## Skill Version(s): <br>
0.3.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
