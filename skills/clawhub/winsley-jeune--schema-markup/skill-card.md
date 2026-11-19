## Description:

Audit and write structured data (JSON-LD) for a website: list the site's page types, read each page's source to see what schema it has now, check which rich results Google supports today, write correct JSON-LD that matches the visible content, and validate it with the Rich Results Test, the Schema Markup Validator and Search Console URL Inspection. Use when the user asks about schema markup, structured data, JSON-LD, rich results or rich snippets, review stars, or Organization, LocalBusiness, Product, Article, Breadcrumb or FAQ schema.

This skill is ready for commercial/non-commercial use.

## Publisher:

[winsley-jeune](https://clawhub.ai/user/winsley-jeune)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SEO practitioners, and site owners use this skill to audit structured data by page type and prepare JSON-LD that matches visible page content. It provides validation guidance and helps avoid misleading markup or promises about search results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated JSON-LD may be submitted to external validation services.

Mitigation: Review the content and confirm it is appropriate to submit before using the Rich Results Test or Schema Markup Validator.

Risk: The workflow includes a README follow-up instruction that can modify project documentation.

Mitigation: Review the follow-up entry and destination before applying the README change.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/winsley-jeune/harborrank-skills/tree/main/skills/schema-markup)
- [ClawHub skill release](https://clawhub.ai/winsley-jeune/skills/schema-markup)
- [Google structured data search gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [Schema Markup Validator](https://validator.schema.org)
- [HarborRank MCP setup documentation](https://harborrank.com/docs/mcp)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code, Configuration instructions]

**Output Format:** [Markdown report with page-type findings, JSON-LD code blocks, and validation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [JSON-LD is drafted per page template and should reflect content visible on the page.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
