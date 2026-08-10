## Description: <br>
Download Chinese administrative-division vector data from the public map.ruiduobao.com API, including province, city, county, town, and village metadata and optional vector downloads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS users, and data analysts use this skill to search Chinese administrative divisions, drill down through hierarchy levels, inspect bounding boxes and area estimates, and download administrative boundary data in common GIS and image formats. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install requirements include an unexpected unpinned dependency. <br>
Mitigation: Review or remove the admin_core requirement before installation, and install dependencies only from trusted package indexes. <br>
Risk: PNG support depends on Pillow and may inherit dependency risk if left broadly versioned. <br>
Mitigation: Pin Pillow to a vetted current version when PNG rendering is needed. <br>
Risk: The skill downloads public map data from an upstream service with its own data-use terms. <br>
Mitigation: Confirm that intended use complies with the upstream map.ruiduobao.com data terms before redistributing or using downloaded administrative boundary data. <br>


## Reference(s): <br>
- [Ruiduobao Map API documentation](https://map.ruiduobao.com/others/API%E6%96%87%E6%A1%A3.html) <br>
- [Ruiduobao Map public API](https://map.ruiduobao.com) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-china-admin-divisions) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Files, Code, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; CLI output may be JSON metadata or files in GeoJSON, Shapefile, KML, GeoPackage, SVG, or PNG formats.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads require network access to map.ruiduobao.com; PNG output requires Pillow.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
