## Description:

自驾出行规划助手，基于高德地图实时数据，支持路线规划与过路费估算、沿途加油站/充电桩/服务区搜索和天气查询，零配置即装即用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel-planning agents use this skill to plan self-driving trips, estimate toll and fuel or EV costs, find nearby travel facilities, and check weather for route cities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Route, waypoint, POI, and city weather queries are sent through a cloud proxy to Gaode Maps.

Mitigation: Use the skill only for trips where that data flow is acceptable, avoid highly sensitive itineraries, and prefer a scoped, rotatable PROXY_TOKEN.

Risk: Toll, fuel, EV cost, and driving-time outputs are estimates that can differ from actual travel conditions and vehicle behavior.

Mitigation: Treat outputs as planning guidance and confirm live navigation, prices, weather, and road conditions before driving.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/self-drive-planner)
- [Publisher profile](https://clawhub.ai/user/travel-skills)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [JSON strings with route, POI, weather, cost, and driving-advice fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on cloud proxy and Gaode Maps responses; toll, fuel, EV cost, and weather advice are estimates.]

## Skill Version(s):

1.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
