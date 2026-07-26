## Description: <br>
自驾出行规划助手，基于高德地图实时数据，支持路线规划与过路费估算、沿途加油站/充电桩/服务区搜索和天气查询，零配置即装即用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to plan self-drive trips, compare route strategies, estimate toll and energy costs, find nearby services, and get weather-based driving advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trip locations, city queries, and route details are sent through the skill publisher's cloud proxy before reaching Gaode Maps. <br>
Mitigation: Avoid entering sensitive home, workplace, or private itinerary details unless the user trusts the publisher-operated proxy and its no-storage claim. <br>
Risk: Route costs, facility availability, and weather guidance are planning aids and may differ from current road, vehicle, or weather conditions. <br>
Mitigation: Confirm routes, tolls, charging or fuel stops, and severe-weather decisions in a current navigation or weather app before driving. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/self-drive-planner) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>
- [Disclosed cloud proxy endpoint](https://1439498936-bl10af74fl.ap-guangzhou.tencentscf.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [JSON tool responses for route plans, facility search results, weather summaries, and driving advice] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include estimates for tolls, fuel or EV costs, rest segments, nearby POIs, and weather-related driving suggestions.] <br>

## Skill Version(s): <br>
1.1.4 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
