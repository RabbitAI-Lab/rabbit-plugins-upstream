## Description:

用高德 995 万 POI 数据库解析任意地名（商圈、地铁站、网红餐厅、小区等），再调飞猪实时房价和预订链接；突破飞猪 --poi-name 只认头部景区的限制，实现任意地点锚定。

This skill is ready for commercial/non-commercial use.

## Publisher:

[han815757857-cmd](https://clawhub.ai/user/han815757857-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

外部旅行者通过旅行代理使用此技能，以自然语言或城市、地点和入住日期查询目的地附近的飞猪酒店、房价及预订链接；也可选择查看周边餐饮。

### Deployment Geography for Use:

China (documented POI coverage spans 102 cities)

## Known Risks and Mitigations:

Risk: This release sends the POI API key and destination searches over an unencrypted connection.

Mitigation: Wait for a release using authenticated HTTPS that identifies the POI service operator and required credential; rotate the key if it has already been used.

Risk: Destination searches reach the POI service, while hotel locations and stay dates are passed to FlyAI.

Mitigation: Avoid sharing sensitive destination or date details unless those external disclosures are acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/han815757857-cmd/skills/gaode-hotel)
- [FlyAI](https://open.fly.ai/)
- [POI service endpoint (HTTP)](http://82.156.169.110/poi/v1)

## Skill Output:

**Output Type(s):** [Markdown]

**Output Format:** [Markdown hotel listings with destination details, prices, ratings, and booking links; nearby dining is optional.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hotel images, destination coordinates, and nearby dining details.]

## Skill Version(s):

1.0.2 (source: frontmatter, CHANGELOG; released 2026-10-21)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
