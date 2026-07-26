## Description: <br>
Provides Baidu Maps Web Service API guidance for place search, weather lookup, route planning, geocoding, administrative district queries, and IP location. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyleung-art](https://clawhub.ai/user/coreyleung-art) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Agents and developers use this skill to answer location-related requests through Baidu Maps APIs, including finding places, converting addresses and coordinates, planning routes, checking weather, and locating IP addresses when explicitly requested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Map queries, addresses, coordinates, route endpoints, and requested IP addresses are sent to Baidu Maps. <br>
Mitigation: Use the skill only for intended location requests, avoid sending unnecessary sensitive location data, and use IP-based location only when the user explicitly asks for it. <br>
Risk: BAIDU_MAP_AK is an API credential required for calls to Baidu Maps. <br>
Mitigation: Store BAIDU_MAP_AK as a secret environment variable and avoid logging, sharing, or embedding it in generated commands beyond the environment variable reference. <br>
Risk: Baidu Maps API calls may be limited by the configured application quota or fail when parameters are invalid. <br>
Mitigation: Check API error responses, confirm required request parameters, and account for service limits when using the generated curl commands. <br>


## Reference(s): <br>
- [Baidu Maps Open Platform](https://lbsyun.baidu.com/) <br>
- [ClawHub skill page](https://clawhub.ai/coreyleung-art/skills/baidu-map-api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with curl command examples and environment variable setup] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and BAIDU_MAP_AK; API responses depend on Baidu Maps service limits and user-supplied location data.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
