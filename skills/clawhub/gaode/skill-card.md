## Description: <br>
Gaode provides an AMap Web API CLI and development guide for geocoding, POI search, routing, weather, IP location, and China coordinate-system handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhangifonly](https://clawhub.ai/user/zhangifonly) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to perform AMap-based location lookups, route planning, weather checks, and API integration guidance for China-focused mapping workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends map, location, route, weather, or IP lookup queries to AMap and requires an AMap API key. <br>
Mitigation: Install only when this data sharing is acceptable, use a Web Service AMAP_KEY with appropriate quota controls, and avoid submitting sensitive locations unless necessary. <br>
Risk: The release metadata does not clearly declare AMAP_KEY and outbound access to restapi.amap.com. <br>
Mitigation: Review the skill package and operational environment before deployment, and prefer metadata that explicitly declares required credentials and network destinations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhangifonly/skills/gaode) <br>
- [AMap Web Service API endpoint](https://restapi.amap.com) <br>
- [AMap Web Service documentation](https://lbs.amap.com/api/webservice/summary) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an AMAP_KEY for live AMap Web Service requests.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
