## Description: <br>
Downloads Sentinel-1, Sentinel-2, and Sentinel-5P satellite imagery through STAC API search and optional file download workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing users can use this skill to search Sentinel imagery for a geographic area and date range, filter results, and optionally download matching assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The ClawHub security summary reports hidden, overbroad credential-handling code and hardcoded Earthdata fallback credentials. <br>
Mitigation: Remove the fallback credentials before use, rotate the exposed account, and rely on user-provided environment variables, .netrc, or a local secrets file. <br>
Risk: The ClawHub security guidance warns that the dependency-check path may install Python packages on the host system. <br>
Mitigation: Use a virtual environment and avoid the --check-deps option on shared or production systems unless package installation is intended. <br>
Risk: The artifact can download remote satellite assets into a local output directory, and the README notes that large downloads require a stable network connection. <br>
Mitigation: Test with a small result limit, review selected scenes before downloading, and choose an output directory with adequate storage. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-sentinel-downloader-skill) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>
- [AWS Earth Search STAC API](https://earth-search.aws.element84.com/v1) <br>
- [Sentinel Hub Catalog API](https://services.sentinel-hub.com/api/v1/catalog) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands] <br>
**Output Format:** [Console text tables or JSON summaries, with optional downloaded imagery files and QA JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a bounding box or place, date range, Sentinel mission, optional cloud-cover limit, and optional output directory.] <br>

## Skill Version(s): <br>
5.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
