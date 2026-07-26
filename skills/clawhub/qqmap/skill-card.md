## Description: <br>
腾讯地图 Web 服务 API 集成，用于地点搜索、逆地理编码、地理编码和周边 POI 搜索，并以 JSON 返回结果。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyleung-art](https://clawhub.ai/user/coreyleung-art) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to query Tencent Maps for location search, geocoding, reverse geocoding, and nearby POI lookup with a Tencent Maps API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Map searches, addresses, and coordinates are sent to Tencent Maps using the user's API key. <br>
Mitigation: Avoid sensitive location queries unless appropriate, and review Tencent Maps handling for the intended use case. <br>
Risk: The Tencent Maps API key can be exposed or misused, causing unauthorized requests or quota consumption. <br>
Mitigation: Keep TENCENT_MAP_KEY secret, prefer a restricted or rotatable key, and monitor quota usage. <br>
Risk: The documented route command is not implemented in the current script. <br>
Mitigation: Use the supported search, geocode, reverse_geocode, and around commands until route behavior is implemented and verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/coreyleung-art/skills/qqmap) <br>
- [Tencent Location Service console](https://lbs.qq.com/dev/console/application/) <br>
- [Tencent Maps Web Service API base URL](https://apis.map.qq.com/ws) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON responses with Markdown usage guidance and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, python3, TENCENT_MAP_KEY, and network access to Tencent Maps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release, SKILL.md frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
