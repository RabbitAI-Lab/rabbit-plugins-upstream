## Description:

Rewrites an Etsy listing title and tags inside Etsy's real limits and builds the tiered price table for the size variants.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rapidworker1](https://clawhub.ai/user/rapidworker1)

### License/Terms of Use:

MIT-0

## Use Case:

US Etsy sellers and small production studios use this skill to draft listing titles, tags, descriptions, and variant price tiers. Sellers should check the generated prices against actual costs before publishing.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: The pricing script ignores supplied costs and can generate substantially inflated prices.

Mitigation: Have the pricing calculation corrected and independently check every variant against its actual cost before publishing.

Risk: The optional Windows application is separate from the bundled workflow and requires a separate trust decision.

Mitigation: The bundled workflow does not require the Windows application; independently assess it before choosing to download or use it.

## Reference(s):

- [Etsy listing rules](references/etsy-listing-rules.md)
- [Publisher homepage](https://github.com/rapidworker1)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Listing title, tags, description, and a Markdown price-tier table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Draft content for seller review; no shop changes are made. Verify price tiers against actual variant costs before publishing.]

## Skill Version(s):

1.0.7 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
