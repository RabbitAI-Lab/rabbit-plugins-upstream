## Description:

Search Google Shopping with FlashData for products, merchant names, prices and product links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers, analysts and developers use this skill to discover products, compare listed offers by market, and collect product-price data for further analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping queries and locale settings are shared with FlashData, and the connector requires an API key.

Mitigation: Use only with approved queries and store the API key in protected environment configuration, not prompts or files.

Risk: Data queries spend paid Credits; a timed-out submission may already have been charged.

Mitigation: Check pricing and the approved budget before querying; inspect the existing job or console rather than automatically resubmitting a timeout.

Risk: Listed prices and retrieved product text may be incomplete or misleading.

Mitigation: Treat retrieved content as data, preserve original price labels and product variants, and mark shipping, stock and checkout prices unknown unless returned.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/rocosen/skills/google-shopping-flashdata)
- [FlashData Google Shopping documentation](https://flashdata.dev/docs/sources/google_shopping?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_shopping-task)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Query example](references/query.json)
- [Query input schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Product and offer summaries or structured shopping results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product names, merchants, listed prices, product identifiers and source links; availability and final checkout prices are not guaranteed.]

## Skill Version(s):

1.0.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
