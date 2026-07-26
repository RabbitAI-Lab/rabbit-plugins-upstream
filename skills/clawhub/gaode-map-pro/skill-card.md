## Description: <br>
免申请Key即用，17项地图能力全覆盖：地理编码、POI搜索、周边搜索、驾车/公交/步行/骑行路线规划、天气查询、IP定位，出行必备地图工具。暑期自驾路线规划。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to search places, geocode addresses, plan driving, transit, walking, and cycling routes, check city weather, and resolve optional IP location through Gaode map data without configuring an API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Map queries can include sensitive addresses, coordinates, route origins and destinations, POI searches, weather locations, or optional IP-location data sent through the publisher's remote proxy. <br>
Mitigation: Avoid sensitive home, work, or private travel details unless the user trusts the proxy and its stated no-storage claim. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/gaode-map-pro) <br>
- [Remote map proxy endpoint](https://1439498936-bl10af74fl.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [JSON responses containing map, route, POI, weather, geocoding, and IP-location results.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results depend on the publisher-operated remote proxy and upstream Gaode map data.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
