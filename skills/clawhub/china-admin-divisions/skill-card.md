## Description: <br>
Download Chinese administrative-division vector data for provinces, cities, counties, towns, and villages from the public map.ruiduobao.com API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, GIS analysts, and mapping workflows use this skill to search Chinese administrative divisions, inspect metadata such as bounding boxes and area estimates, and download boundary files for mapping or data-processing tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The tool contacts map.ruiduobao.com and writes downloaded vector files to user-selected paths. <br>
Mitigation: Review commands before execution and choose output paths that are appropriate for the workspace and data handling policy. <br>
Risk: The release includes unpinned dependencies and unused bundled utility code. <br>
Mitigation: Pin dependencies in stricter environments and avoid importing bundled helpers unless their network and cache behavior is acceptable. <br>
Risk: Upstream administrative-boundary data may have separate usage terms from the skill code. <br>
Mitigation: Confirm the source data terms before using downloaded boundary data in regulated or commercial workflows. <br>


## Reference(s): <br>
- [Ruiduobao Map API Documentation](https://map.ruiduobao.com/others/API%E6%96%87%E6%A1%A3.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/china-admin-divisions) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON, GeoJSON, Shapefile, KML, GeoPackage, SVG, or PNG file outputs from the described CLI.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The CLI can print JSON metadata and write downloaded vector or image files to user-selected output paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
