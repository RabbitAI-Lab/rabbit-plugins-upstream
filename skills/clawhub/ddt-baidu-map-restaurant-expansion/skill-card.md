## Description:

餐饮拓店机会区域、候选地址竞争与现场验证优先级分析。可将百度地图中复制出的地点名称和地址文本作为地点输入；基于店店通已发布门店快照生成可核验结论。本 Skill 非百度地图官方产品，和百度地图不存在合作、授权或数据来源关系。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and business teams use this skill to analyze restaurant chain expansion opportunities, candidate-address competition, regional trends, and field-validation priorities from 店店通 published store snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant brand, region, and candidate-address queries are sent to 店店通's external API service.

Mitigation: Use the skill only when that data sharing is acceptable, and keep the API key in a local environment variable rather than chat or generated outputs.

Risk: Published store snapshots may omit revenue, same-store growth, profit, closure reasons, or official opening and closing dates.

Mitigation: Present conclusions with coverage period and data definitions, and require field validation before acting on site-selection recommendations.

Risk: Detailed store, nearby, and event endpoints are limited previews rather than export interfaces.

Mitigation: Use aggregate totals and regional summaries for broad questions, and narrow the query when preview results are truncated or require refinement.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-baidu-map-restaurant-expansion)
- [店店通 ClawHub homepage](https://gotoshop-ai.com/ddtclaw/)
- [店店通 API key setup](https://gotoshop-ai.com/ddtclaw/open)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown with concise findings, metrics, provenance notes, and limited detail tables when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a user-provided DDT_API_KEY; avoids exposing API keys, internal identifiers, and unsupported full-store exports.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
