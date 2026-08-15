## Description:

腾讯地图·地图助手 Skill，一句自然语言调用腾讯地图全套能力，开箱即用。提供 AI 旅游攻略、地点搜索（含评分/人均/营业时间）、关键词提示、路线规划（驾车/步行/公交/骑行）、地址解析与逆解析、行政区划、IP 定位、距离计算、天气查询，并可将行程或多 POI 渲染成网页地图或生成腾讯地图小程序指南。涉及找地点、规划路线、旅游行程、查天气、坐标转换等出行场景时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to access Tencent Maps capabilities through an agent, including travel itinerary generation, POI search, route planning, geocoding, reverse geocoding, administrative district lookup, IP location, distance calculation, weather lookup, and map or mini-program guide generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can request a phone-number-based Tencent Maps API key or reuse an existing Tencent Maps key.

Mitigation: Use a dedicated Tencent Maps key with limited scope, monitor quota usage, and rotate or delete saved keys when access is no longer needed.

Risk: Phone-linked API keys may be stored locally in plaintext under ~/.tencentmap/tempkey.json.

Mitigation: Review local file permissions, avoid shared machines for key setup, and remove the saved key file if the skill is uninstalled or access should be revoked.

Risk: Location, route, weather, trip, and POI queries are sent to Tencent Maps services.

Mitigation: Avoid submitting sensitive personal, regulated, or confidential location data unless sharing it with Tencent Maps services is acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/tencent-adm/skills/tencentmap-map-assistant-skill)
- [Tencent Maps API Reference](references/api_reference.md)
- [Agent Notes](references/agent-notes.md)
- [Error Codes](references/error-codes.md)
- [JSAPI Guide](references/jsapi-guide/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and text with optional Python snippets, shell commands, generated files, and HTML map artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call Tencent Maps services, create or reuse API keys, and produce travel guide Markdown, QR-code image references, or HTML map visualizations.]

## Skill Version(s):

1.5.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
