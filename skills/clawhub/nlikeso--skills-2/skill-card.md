## Description:

使用蓝鲸选品 API 和本地脚本分析 Mercado Libre 商品、类目、关键词、价格、竞品、店铺、品牌、目录链接、运费和汇率。

This skill is ready for commercial/non-commercial use.

## Publisher:

[nlikeso](https://clawhub.ai/user/nlikeso)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce analysts use this skill to research Mercado Libre markets, products, categories, keywords, competitor listings, sellers, brands, catalog links, shipping, exchange rates, and profit assumptions through the Lan Jing Xuan Pin API and bundled local scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional HTML export can expose API result data in a browser and leave generated result files on disk.

Mitigation: Use Markdown output for sensitive searches and delete generated ljxp_search_*.html files when finished.

Risk: Authentication tokens may be exposed if passed directly on command lines.

Mitigation: Prefer the LJXP_TOKEN environment variable and avoid including tokens in agent-visible replies or saved command history.

Risk: Account or package lookup responses may include phone numbers.

Mitigation: Ask the agent to mask phone numbers before presenting package or account lookup results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/nlikeso/skills/skills-2)
- [Publisher profile](https://clawhub.ai/user/nlikeso)
- [API reference](references/api_reference.md)
- [Items API](references/api/items.md)
- [Category API](references/api/category.md)
- [Keywords API](references/api/keywords.md)
- [Catalogs API](references/api/catalogs.md)
- [Trends API](references/api/trends.md)
- [Sellers API](references/api/sellers.md)
- [Users API](references/api/users.md)
- [Rate and shipping API](references/api/rate-shipping.md)
- [Lan Jing Xuan Pin API base](https://xpskills.lingdongsz.com/api)
- [Lingdong official site](https://www.lingdongsz.com/)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown responses with tables and optional local HTML result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May invoke bundled Python scripts against authenticated API endpoints and may create ljxp_search_*.html files when HTML export is requested.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact frontmatter reports 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
