## Description:

Create a read-only Shopify store performance overview for a day, week, month, or valid custom period. Use it to review sales, orders, promotions, shipping speed, low stock on products that sold, and upcoming seasonal preparation; never use it to change store data, campaigns, or themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lvsao](https://clawhub.ai/user/lvsao)

### License/Terms of Use:

MIT-0

## Use Case:

Shopify merchants, ecommerce operators, and their supporting agents use this skill to generate private read-only sales, fulfillment, promotion, inventory, and seasonal-preparation briefs for a selected reporting period.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read-only Shopify access can still expose orders, products, inventory, discounts, fulfillment status, and aggregate customer/order context.

Mitigation: Install only when this access is acceptable, use the smallest read-only scopes, and keep generated reports private.

Risk: Environment files and generated HTML reports may contain private merchant information.

Mitigation: Store the env file and generated reports only in a private working directory and do not publish or paste their contents into public channels.

Risk: Admin API token mode increases local credential handling responsibility.

Mitigation: Avoid Admin API token mode unless a merchant intentionally created a local read-only token for this run.

## Reference(s):

- [Shopify Operations Brief onboarding](references/onboarding-guide.md)
- [What each number means](references/metric-definitions.md)
- [Seasonal selling calendar](references/marketing-calendar.md)
- [Report layout and writing standard](references/design-tokens.md)
- [Project homepage](https://github.com/lvsao/shopify-skill-hub)
- [ClawHub skill page](https://clawhub.ai/lvsao/skills/shopify-operations-brief)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, text, files, json]

**Output Format:** [Markdown-style agent instructions that lead to a private HTML report or JSON output from the Node.js script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a private Shopify store domain and read-only Shopify access; generated reports should remain private.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
