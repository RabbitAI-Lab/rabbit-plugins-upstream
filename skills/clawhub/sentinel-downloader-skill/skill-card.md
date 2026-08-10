## Description: <br>
Helps an agent search for and download Sentinel-1, Sentinel-2, and Sentinel-5P satellite imagery through STAC APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and geospatial agents use this skill to find Sentinel imagery for a geographic bounding box, date range, mission, and optional cloud-cover filter, then prepare or run download commands for selected scenes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release evidence reports under-disclosed credential-management code with hardcoded Earthdata fallback credentials. <br>
Mitigation: Remove or ignore bundled fallback credentials and provide credentials only through trusted environment variables, .netrc, or a user-controlled secret store. <br>
Risk: The release evidence reports host-level dependency installation behavior. <br>
Mitigation: Install and test the skill in an isolated virtual environment, and avoid running dependency checks against a system Python installation. <br>
Risk: Large satellite downloads can consume substantial storage and network bandwidth. <br>
Mitigation: Start with small limits, inspect search results before downloading, and write outputs to a controlled directory with adequate space. <br>


## Reference(s): <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>
- [AWS Earth Search STAC API](https://earth-search.aws.element84.com/v1) <br>
- [Sentinel Hub Catalog API](https://services.sentinel-hub.com/api/v1/catalog) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and file path guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference downloaded imagery files, manifests, product identifiers, dates, cloud cover, geographic bounds, and STAC item metadata.] <br>

## Skill Version(s): <br>
3.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
