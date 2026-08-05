## Description: <br>
Search and download Landsat 8/9 Collection 2 Level 2 images via STAC API with filters for cloud cover, WRS-2 path/row, band selection, and visual progress. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and remote-sensing practitioners use this skill to search public Landsat 8/9 Collection 2 Level 2 scenes by area, date, cloud cover, WRS-2 path/row, and band, then download selected assets with progress reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The package includes an unrelated credential helper with embedded credentials and under-disclosed local secret/profile handling. <br>
Mitigation: Review before installing in environments with real credentials or sensitive location work; remove or fix the credential helper, rotate exposed credentials, and disclose or make geocoding/cache behavior opt-in. <br>
Risk: The downloader contacts external STAC and data endpoints and writes downloaded geospatial files locally. <br>
Mitigation: Restrict network egress to documented public data endpoints and run with a controlled output directory for downloaded assets. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-landsat-download) <br>
- [Microsoft Planetary Computer Landsat Collection 2 Level 2](https://planetarycomputer.microsoft.com/dataset/landsat-c2-l2) <br>
- [Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1/) <br>
- [Element84 Earth Search API](https://earth-search.aws.element84.com/v1/) <br>
- [STAC specification](https://stacspec.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline bash commands, plus optional text or JSON command output and downloaded raster assets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads are written to a user-selected output directory and may use .part temporary files before finalizing assets.] <br>

## Skill Version(s): <br>
5.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
