## Description: <br>
Searches and downloads MODIS Land Surface Temperature products from NASA LAADS DAAC for Terra and Aqua daily and 8-day datasets, with GeoTIFF output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, researchers, and geospatial analysts use this skill to search for MODIS LST granules, configure Earthdata access, and download or list temperature data for a date range and area of interest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ClawScan reported that the release ships and silently uses a hardcoded Earthdata fallback account. <br>
Mitigation: Require explicit user-provided Earthdata credentials, remove the embedded fallback account, and rotate the exposed account before use. <br>
Risk: ClawScan reported under-disclosed credential and location-query handling, including remote place geocoding and local caching. <br>
Mitigation: Disclose when place names or credentials are sent to remote services, provide a way to disable remote geocoding and caching, and clear local caches where appropriate. <br>
Risk: ClawScan guidance calls for dependency versions to be reviewed before installation. <br>
Mitigation: Pin dependencies to reviewed versions and install in an isolated environment before running download workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/modis-lst-download) <br>
- [NASA Earthdata Login](https://urs.earthdata.nasa.gov/) <br>
- [NASA LAADS DAAC](https://ladsweb.modaps.eosdis.nasa.gov/) <br>
- [CMR STAC LAADS endpoint](https://cmr.earthdata.nasa.gov/stac/LAADS) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands and generated GeoTIFF or URL-list outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads can require user-provided Earthdata credentials and may call remote data or geocoding services.] <br>

## Skill Version(s): <br>
0.3.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
