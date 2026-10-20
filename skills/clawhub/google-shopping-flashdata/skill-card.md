## Description:

Search Google Shopping through FlashData for product listings, merchants, prices, and links by market.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rocosen](https://clawhub.ai/user/rocosen)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers, analysts, and developers use this skill to find products, compare listed offers by market, and collect merchant and price information for further analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and the API key are sent to FlashData.

Mitigation: Trust the service before use, and provide the key only through protected secret configuration.

Risk: Product searches consume paid FlashData Credits; repeating a timed-out request may incur another charge.

Mitigation: Check pricing and the approved budget first; check existing jobs rather than automatically retrying timed-out requests.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/rocosen/skills/google-shopping-flashdata)
- [FlashData Google Shopping documentation](https://flashdata.dev/docs/sources/google_shopping?utm_source=clawhub&utm_medium=integration&utm_campaign=intent_gtm_2026q4&utm_content=google_shopping-task)
- [FlashData pricing](https://flashdata.dev/pricing)
- [Query reference](references/query.json)
- [Search parameter schema](references/schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Product listings as JSON or a Markdown offer comparison]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include product identifiers, merchants, original price labels, and source links; result counts can vary.]

## Skill Version(s):

1.0.1 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
