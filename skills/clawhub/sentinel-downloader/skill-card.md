## Description: <br>
Download Sentinel satellite imagery (Sentinel-1/2/5P) via STAC API with cloud cover filtering and batch download support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, geospatial analysts, and remote-sensing users can search for Sentinel-1, Sentinel-2, and Sentinel-5P imagery over a bounding box and date range, filter results, and optionally download imagery files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports network requests, imagery and QA file writes, optional Python package installation, and credential/geocoding helper code beyond the basic documented workflow. <br>
Mitigation: Run in an isolated virtual environment, review commands before execution, avoid dependency installation on shared systems, and restrict output directories to intended locations. <br>
Risk: The security scan reports hardcoded Earthdata credential defaults and under-disclosed credential handling. <br>
Mitigation: Remove or replace bundled credential defaults before use, prefer environment variables or local user secrets, and rotate any exposed credentials. <br>
Risk: The security scan notes that place-name searches may contact third-party geocoders and leave a local cache. <br>
Mitigation: Use explicit bounding boxes for sensitive locations when possible, review geocoding behavior, and clear local geocoding caches after use. <br>


## Reference(s): <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>
- [AWS Earth Search STAC API](https://earth-search.aws.element84.com/v1) <br>
- [AWS Earth Search STAC API v0](https://earth-search.aws.element84.com/v0) <br>
- [Sentinel Hub Catalog API](https://services.sentinel-hub.com/api/v1/catalog) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, JSON, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; runtime output may be table text, JSON, and downloaded imagery files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires network access to STAC services and writes downloads to a user-selected output directory.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
