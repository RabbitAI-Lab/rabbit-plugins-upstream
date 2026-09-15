## Description:

零配置即装即用，一键唤起高德地图APP打车，另含驾车/公交/步行/骑行路线规划、IP定位、周边搜索、POI搜索，免申请Key即用。暑期出行打车、目的地接送。

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to ask an agent for Gaode taxi app links, route planning, IP-based location, nearby place search, POI lookup, and related travel guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home or work addresses, exact coordinates, trip endpoints, or IP addresses may be sent to a third-party proxy using a default shared token.

Mitigation: Review before installing, use only if you trust the proxy operator, and prefer a version that lets you configure your own trusted endpoint and credential with clear privacy terms.

## Reference(s):

- [ClawHub skill page: gaode-taxi](https://clawhub.ai/travel-skills/skills/gaode-taxi)
- [Publisher profile: travel-skills](https://clawhub.ai/user/travel-skills)
- [Configured Gaode proxy endpoint](https://1439498936-bl10af74fl.ap-guangzhou.tencentscf.com)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [JSON responses with route, POI, location, weather, map URL, or Gaode app URI fields for the agent to summarize.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include externally generated Gaode map or app URLs and real-time location-related API results.]

## Skill Version(s):

1.2.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
