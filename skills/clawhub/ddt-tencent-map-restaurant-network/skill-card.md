## Description:

餐饮品牌开关店、区域扩张、竞对密度与候选点机会分析；可将腾讯地图中复制出的地点名称和地址文本作为地点输入，并基于店店通已发布门店快照生成可核验结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business analysts use this skill to analyze restaurant brand expansion, closures, competitor density, nearby stores, and candidate site opportunities from published store-network snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant brand, address, and candidate-site queries are sent to the publisher's API service.

Mitigation: Confirm that the user is comfortable sharing those queries with the publisher service and keep the API key private.

Risk: The skill is scoped to published restaurant data snapshots and can produce unsupported conclusions if used for other industries or unavailable brands.

Mitigation: Use the brand directory and capability checks first; stop when data, coverage, or required capabilities are unavailable.

Risk: Preview endpoints are limited and may be truncated, so treating them as full exports can mislead users.

Mitigation: Prefer aggregate endpoints for conclusions and request narrower filters for specific store, address, or date checks.

## Reference(s):

- [Skill homepage](https://gotoshop-ai.com/ddtclaw/)
- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-tencent-map-restaurant-network)
- [Publisher profile](https://clawhub.ai/user/horacetu)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with concise conclusions, key metrics, coverage notes, limited details, and caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a user-provided API key and returns aggregate restaurant-network findings before limited store-level details.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
