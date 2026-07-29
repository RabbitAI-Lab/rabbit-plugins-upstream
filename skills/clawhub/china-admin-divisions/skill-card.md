## Description: <br>
Downloads Chinese administrative-division vector data for province, city, county, town, and village levels from the public map.ruiduobao.com API, with search, drill-down, bbox/area calculation, and vector or image exports. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
GIS analysts, developers, and mapping workflows use this skill to search Chinese administrative divisions, inspect metadata and bounding boxes, and download boundaries for analysis, visualization, or reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The server security review marks the package suspicious because it includes an undisclosed bundled credential helper with hardcoded Earthdata defaults. <br>
Mitigation: Review the package before installation, remove or strip the bundled credential module, and run only the documented china_admin_divisions CLI entrypoint unless the helper is audited. <br>
Risk: The server security review notes unpinned dependencies. <br>
Mitigation: Pin dependencies and install the skill in an isolated environment before using it in repeatable or shared workflows. <br>


## Reference(s): <br>
- [Ruiduobao Map API documentation](https://map.ruiduobao.com/others/API%E6%96%87%E6%A1%A3.html) <br>
- [Ruiduobao Map](https://map.ruiduobao.com) <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/china-admin-divisions) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with shell commands; CLI results may be JSON metadata or GeoJSON, Shapefile ZIP, KML, GeoPackage, SVG, or PNG files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Downloads write to the requested output path or current directory; info and bbox commands return structured JSON.] <br>

## Skill Version(s): <br>
1.0.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
