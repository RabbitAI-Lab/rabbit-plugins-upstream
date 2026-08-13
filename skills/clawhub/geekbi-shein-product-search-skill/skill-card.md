## Description:

Searches and analyzes SHEIN product data through GeekBI Cloud to help evaluate sales, pricing, trends, fulfillment modes, same-item competition, and product opportunities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[geekbi](https://clawhub.ai/user/geekbi)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce analysts use this skill to search SHEIN goods, compare product candidates, and decide which items merit further validation. It supports keyword, site, category, fulfillment, sales, price, rating, listing-time, and competition filters while keeping conclusions tied to returned GeekBI data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reuses and persists GeekBI login state, including a credential store that may be shared with another GeekBI/Temu-named skill path.

Mitigation: Install only in a profile where that session reuse is acceptable; use an isolated profile or clear the .geekbi auth state when cross-skill session sharing is not desired.

Risk: The skill makes authenticated requests to GeekBI's API to retrieve SHEIN product and site data.

Mitigation: Review account access expectations before installation and pause when the service asks the user to complete login, quota, or other account actions.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/geekbi/geekbi-shein-product-search-skill)
- [ClawHub skill page](https://clawhub.ai/geekbi/skills/geekbi-shein-product-search-skill)
- [SHEIN product search reference](artifact/references/SHEIN商品搜索.md)
- [SHEIN product search API reference](artifact/references/SHEIN商品搜索接口.md)
- [SHEIN product ranking presets](artifact/references/SHEIN商品榜单预设.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise Chinese business analysis, data scope, key evidence, risks, and clickable product links when product URLs are returned.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API-backed search results, computed comparisons, opportunity notes, and validation steps; incomplete pagination or missing values should be stated explicitly.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
