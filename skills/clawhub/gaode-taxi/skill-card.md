## Description: <br>
零配置即装即用，一键唤起高德地图APP打车，另含驾车/公交/步行/骑行路线规划、IP定位、周边搜索、POI搜索，免申请Key即用。暑期出行打车、目的地接送。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-focused agents use this skill to request taxi app handoff links, route planning, IP-based location lookup, nearby search, and POI details for trip planning and local navigation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive travel-related queries, addresses, coordinates, destination names, and possible IP-derived location information are sent through a remote proxy service. <br>
Mitigation: Install only when that data flow is acceptable, avoid sharing unnecessary precise location data, and review the configured proxy service before use. <br>
Risk: The proxy endpoint is overridable, which can redirect map and taxi requests to an untrusted host. <br>
Mitigation: Review or pin GAODE_PROXY_URL to an approved endpoint before deployment. <br>
Risk: The bundled/default proxy token should be treated as exposed rather than private. <br>
Mitigation: Do not rely on the default token as a secret; configure an approved token through the deployment environment if required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/gaode-taxi) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [JSON responses with route, location, POI, weather, static map URL, and app URI data] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on remote proxy responses and may include real-time map, route, place, location, and app handoff data.] <br>

## Skill Version(s): <br>
1.2.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
