## Description:

餐饮拓店机会区域、候选地址竞争与现场验证优先级分析，可将腾讯地图中复制出的地点名称和地址文本作为地点输入，并基于店店通已发布门店快照生成可核验结论。

This skill is ready for commercial/non-commercial use.

## Publisher:

[horacetu](https://clawhub.ai/user/horacetu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and expansion teams use this skill to analyze restaurant chain site-selection opportunities, candidate-address competition, market coverage, and field-verification priorities from published DDT restaurant-store snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant brand, address, and candidate-site queries are sent to the GotShop/DDT API.

Mitigation: Use the skill only when that external processing is acceptable, store DDT_API_KEY locally, and do not expose API keys in prompts or responses.

Risk: Bounded preview endpoints can return truncated or under-specified results that are unsuitable for full store-list export or unsupported business conclusions.

Mitigation: Refine the brand, address, date, province, city, or district filters and rely on aggregate endpoints for broad conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/horacetu/skills/ddt-tencent-map-restaurant-expansion)
- [DDT homepage](https://gotoshop-ai.com/ddtclaw/)
- [DDT API key setup](https://gotoshop-ai.com/ddtclaw/open)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with concise analysis, metrics, caveats, and occasional bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bounded API calls and limited-detail previews; avoids full store-list export behavior.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
