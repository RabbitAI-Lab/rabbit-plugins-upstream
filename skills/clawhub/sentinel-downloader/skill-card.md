## Description: <br>
Download Sentinel satellite imagery for Sentinel-1, Sentinel-2, and Sentinel-5P through STAC APIs with cloud-cover filtering and batch download support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing users can search Sentinel imagery by bounding box or place, date range, mission, cloud cover, and STAC endpoint, then optionally download selected assets and write QA output. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can contact external STAC providers and geocoding services. <br>
Mitigation: Review the selected STAC endpoint and place-name resolution settings before running it with sensitive locations. <br>
Risk: Satellite imagery downloads can be large and are written to local output directories. <br>
Mitigation: Use a test limit first and choose an output directory with adequate storage and appropriate access controls. <br>
Risk: The dependency check path can install Python packages. <br>
Mitigation: Install and run the skill in a virtual environment and review dependency installation before using dependency checks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/sentinel-downloader) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>
- [AWS Earth Search STAC API](https://earth-search.aws.element84.com/v0) <br>
- [Sentinel Hub Catalog API](https://services.sentinel-hub.com/api/v1/catalog) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, JSON, Files] <br>
**Output Format:** [Command-line output in table or JSON format, with optional downloaded imagery files and QA JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May contact STAC and geocoding services, install Python dependencies when requested, and write large satellite imagery files to the selected output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
