## Description: <br>
Download Sentinel satellite imagery (Sentinel-1/2/5P) via STAC API with cloud cover filtering and batch download support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and geospatial analysts use this skill to search for Sentinel-1, Sentinel-2, and Sentinel-5P imagery by bounding box and date range, filter Sentinel-2 results by cloud cover, and optionally download matching assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Custom STAC endpoints can direct the tool to unexpected network services or asset links. <br>
Mitigation: Review the STAC endpoint before using --stac-api and prefer trusted catalog providers. <br>
Risk: The optional dependency check can install Python packages into the active environment. <br>
Mitigation: Install and run the skill in a virtual environment, and avoid --check-deps in shared Python environments unless package installation is acceptable. <br>
Risk: Downloading imagery can transfer large files and depends on the availability and access rules of the selected data source. <br>
Mitigation: Start with a small --limit value, preview search results before using --download, and confirm any required source registration or authentication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/sentinel-downloader-skill) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1) <br>
- [AWS Earth Search STAC API](https://earth-search.aws.element84.com/v1) <br>
- [Sentinel Hub Catalog API](https://services.sentinel-hub.com/api/v1/catalog) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Text, JSON, Files] <br>
**Output Format:** [CLI output as table text or JSON, with optional downloaded imagery files organized under product-specific directories.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bounding box, start date, and end date; supports mission, cloud cover, STAC API endpoint, result limit, output directory, and download options.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release metadata; artifact frontmatter and package.json report 1.0.1, artifact _meta.json reports 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
