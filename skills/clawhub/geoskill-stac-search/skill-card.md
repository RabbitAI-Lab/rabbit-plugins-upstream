## Description: <br>
STAC Universal Search Tool for searching geospatial data across any STAC. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and geospatial analysts use this skill to search STAC endpoints for remote-sensing collections, filter results by collection, bounding box, date range, and cloud cover, and inspect assets or collection metadata. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Embedded Earthdata credential handling can expose or reuse credentials unexpectedly. <br>
Mitigation: Remove embedded credentials, rotate any affected credentials, and require users to provide credentials explicitly through their own environment or approved secret store. <br>
Risk: Extra network and location lookup behavior may contact external geocoding or STAC providers beyond the primary search endpoint. <br>
Mitigation: Document all external providers, review endpoint choices before use, and run the skill only in environments where those outbound requests are allowed. <br>
Risk: The requests dependency is only lower-bounded. <br>
Mitigation: Constrain requests to a reviewed patched version before deployment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ruiduobao/skills/geoskill-stac-search) <br>
- [README](README.md) <br>
- [Microsoft Planetary Computer STAC API](https://planetarycomputer.microsoft.com/api/stac/v1/) <br>
- [Element84 Earth Search STAC API](https://earth-search.aws.element84.com/v1/) <br>
- [Google Earth Engine STAC Endpoint](https://earthengine-stac.storage.googleapis.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Text tables, JSON, and Markdown guidance with shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results depend on the selected STAC endpoint, collection, spatial filters, temporal filters, and network availability.] <br>

## Skill Version(s): <br>
5.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
