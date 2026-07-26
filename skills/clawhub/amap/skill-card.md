## Description: <br>
Uses the Gaode (Amap) Web Service API for place search, weather lookup, route planning, geocoding, reverse geocoding, and administrative district lookup. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dboy233](https://clawhub.ai/user/dboy233) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to answer map, weather, location search, address lookup, and driving-route questions through Amap Web Service API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Map, weather, address, coordinate, routing, and search queries are sent to Amap and may reveal sensitive location context. <br>
Mitigation: Use the skill only when sharing those query details with Amap is acceptable, and avoid querying highly sensitive locations unless needed. <br>
Risk: The skill depends on an AMAP_KEY API key that could be exposed through shared logs or shell history. <br>
Mitigation: Use a dedicated Amap API key where possible and avoid printing or storing AMAP_KEY in shared command logs, transcripts, or shell history. <br>


## Reference(s): <br>
- [Amap Open Platform](https://lbs.amap.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with curl command examples and concise API usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and an AMAP_KEY environment variable; API calls send user-requested locations, addresses, coordinates, route endpoints, and search keywords to Amap.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
