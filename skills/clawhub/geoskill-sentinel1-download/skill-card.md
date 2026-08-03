## Description: <br>
Searches for and downloads Sentinel-1 SAR GRD imagery through STAC APIs, with filters for bounding box, date range, polarization, and orbit direction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing practitioners use this skill to find Sentinel-1 SAR scenes and optionally download selected VV/VH assets for analysis workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release includes an unrelated credential helper with a hardcoded Earthdata credential fallback. <br>
Mitigation: Remove the fallback credential and keep user credentials only in environment variables or user-managed secret files before broad use. <br>
Risk: Place-name lookup may call Open-Meteo or Nominatim and cache AOI lookup data in the user's home directory. <br>
Mitigation: Document lookup behavior, provide privacy-aware defaults, and allow users to disable online geocoding or clear the local AOI cache. <br>
Risk: The dependency declaration allows any requests version newer than 2.28.0. <br>
Mitigation: Use a tighter supported version range or lockfile for reviewed deployments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sentinel1-download) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1/) <br>
- [Element84 Earth Search STAC API](https://earth-search.aws.element84.com/v1/) <br>
- [Landsat Downloader skill](https://clawhub.ai/skills/landsat-download) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files, shell commands, configuration, guidance] <br>
**Output Format:** [CLI text or JSON search results, optional CSV/JSON metadata files, and downloaded Sentinel-1 asset files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports search-only operation, optional downloads, safe .part writes, progress display, and user-selected output directories.] <br>

## Skill Version(s): <br>
5.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
