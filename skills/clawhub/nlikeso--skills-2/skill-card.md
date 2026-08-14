## Description:

Ljxp uses the Blue Whale Product Selection API and local scripts to analyze Mercado Libre products, categories, keywords, prices, competitors, sellers, brands, catalog listings, shipping, and exchange rates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nlikeso](https://clawhub.ai/user/nlikeso)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, ecommerce analysts, and Mercado Libre sellers use this skill to run market research workflows for product opportunity, competition, pricing, keyword, seller, brand, catalog, shipping, exchange-rate, and profit analysis. The skill returns business conclusions, supporting data, API credit usage, and recommended next analysis steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends an authorization token and Mercado Libre research queries to the LJXP service.

Mitigation: Install and use the skill only when the LJXP service is trusted with those credentials and queries; avoid exposing tokens in chat or shared logs.

Risk: Optional HTML output may display API data in a browser view.

Mitigation: Prefer Markdown or JSON for routine use, and generate HTML only when a browser view is needed and the API data is trusted.

Risk: Package or credit queries may show the account nickname and phone number in the chat.

Mitigation: Run account queries only when needed and review outputs before sharing them outside the current workspace.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/nlikeso/skills/skills-2)
- [Server-resolved source repository](https://github.com/Nlikeso/skills)
- [Ljxp API base](https://xpskills.lingdongsz.com/api)
- [API Reference](artifact/references/api_reference.md)
- [Items API](artifact/references/api/items.md)
- [Category API](artifact/references/api/category.md)
- [Trends API](artifact/references/api/trends.md)
- [Keywords API](artifact/references/api/keywords.md)
- [Sellers API](artifact/references/api/sellers.md)
- [Catalogs API](artifact/references/api/catalogs.md)
- [Rate and Shipping API](artifact/references/api/rate-shipping.md)
- [Users API](artifact/references/api/users.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown with optional JSON or HTML file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routine output is Markdown or JSON; optional HTML output may be generated for browser viewing when requested.]

## Skill Version(s):

0.1.0 (source: server release evidence; artifact frontmatter declares 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
