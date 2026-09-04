## Description:

高德地图 API 技能，支持路径规划、距离计算、地理位置搜索等，用于查询两地之间的骑行、驾车、步行路线、距离和时间，并需要配置 AMap API Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lanlan314](https://clawhub.ai/user/lanlan314)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to query AMap Web Service route planning, geocoding, and distance information for cycling, driving, and walking trips.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Route origins, destinations, and resulting coordinates may be sent to AMap.

Mitigation: Use only locations acceptable to disclose, and avoid sensitive home, client, or confidential business locations unless that disclosure is acceptable.

Risk: The skill requires an AMap Web Service API key in local credentials.

Mitigation: Configure a dedicated AMap Web Service API key in ~/.openclaw/credentials/amap.json and manage it separately from other secrets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/lanlan314/skills/amap)
- [AMap Open Platform Console](https://console.amap.com)
- [AMap Web Service Key Console](https://console.amap.com/dev/key/app)
- [AMap Direction API Endpoint](https://restapi.amap.com/v3/direction/:type)
- [AMap Geocoding API Endpoint](https://restapi.amap.com/v3/geocode/geo)
- [AMap Distance API Endpoint](https://restapi.amap.com/v3/distance)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and API JSON summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses AMap route, geocoding, and distance responses; requires a locally configured AMap Web Service API key.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
