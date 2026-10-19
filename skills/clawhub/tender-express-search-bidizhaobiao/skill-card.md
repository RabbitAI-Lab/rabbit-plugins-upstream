## Description:

按省市检索中国地方招投标公告及预算金额，并按需查询企业与市场数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[liu-jiapeng](https://clawhub.ai/user/liu-jiapeng)

### License/Terms of Use:

MIT-0

## Use Case:

采购、销售及商机研究人员可按地域、时间和关键词查找中国招投标公告、预算及项目进展；按需查询企业参与情况、联系人和市场趋势。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill also enables broad company, contact and market-intelligence queries beyond local tender search.

Mitigation: Review the requested scope and grant access only to an API account permitted to run those queries.

Risk: First-use registration can collect device characteristics, including a hashed MAC address, and save an API key locally.

Mitigation: Configure ZLBX_API_KEY before first use to avoid device-based registration; if registration is needed, obtain explicit consent and protect ~/.zlbx/config.json.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/liu-jiapeng/skills/tender-express-search-bidizhaobiao)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Tender search API reference](artifact/references/api-search.md)
- [Company intelligence API reference](artifact/references/api-company.md)
- [Company registry API reference](artifact/references/api-registry.md)
- [Market analysis API reference](artifact/references/api-market.md)
- [Account API reference](artifact/references/api-account.md)
- [Account registration and credential setup](artifact/references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and linked result tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Shows applied filters, source links, publication dates and amounts in ten-thousand-yuan units when available; contact details depend on account access.]

## Skill Version(s):

2.0.7 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
