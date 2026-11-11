## Description:

Search Google Shopping with FlashData for products, merchant names, prices and product links. Use for product discovery, comparing listed offers and collecting product-price data by market. Requires a FlashData API key and paid Credits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and shopping researchers can search Google Shopping by product, category, market, and language. They use the returned listings to compare merchant offers, prices, and product links or prepare product data for further analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search requests use the hosted FlashData MCP service, and data queries spend paid FlashData Credits.

Mitigation: Keep FLASHDATA_API_KEY in protected secret configuration, review FlashData pricing, and run only task-approved queries within the authorized budget.

Risk: ClawScan reports a benign result with medium confidence, but its analysis was partial because two local path-like references could not be resolved.

Mitigation: Review the unresolved references and the skill's behavior before installation.

## Reference(s):

- [FlashData Google Shopping documentation](https://flashdata.dev/docs/sources/google_shopping?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_shopping-task)
- [FlashData MCP endpoint](https://data.flashdata.dev/mcp)
- [FlashData pricing](https://flashdata.dev/pricing?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_shopping-task)
- [Get a FlashData API key](https://flashdata.dev/signup?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_shopping-task)
- [Input schema](references/schema.json)
- [Example query](references/query.json)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Analysis]

**Output Format:** [Structured JSON product listings, with optional Markdown offer comparisons or text summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returned results vary by query. Listed prices may not include shipping, stock status, or final checkout price.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
