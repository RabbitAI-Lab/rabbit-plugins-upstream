## Description:

Looks up tracked GPU rental prices and work-stack deals through the Lantern Works hosted service or public JSON API, with vendor sources, verification dates, price changes, and disclosed referral links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[connormatthewdouglas](https://clawhub.ai/user/connormatthewdouglas)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams can compare tracked GPU rental prices, price changes, and work-stack deals when estimating or selecting tools for an agent. Use the vendor links and verification dates to confirm current prices and terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Provider prices and deal terms can change, and the lowest-price results cover tracked providers only.

Mitigation: Check the verification date and source link in each result, then confirm current prices, availability, and terms with the provider.

Risk: Free-text workload descriptions may contain private information.

Mitigation: Keep submitted descriptions generic and omit confidential or personal information.

Risk: Some result links are referral links.

Mitigation: Disclose flagged referral links and offer the vendor's direct pricing page when sharing a result.

Risk: The optional local alternative uses a separately installed package.

Mitigation: Review the package and pin its version when using the local installation.

## Reference(s):

- [Lantern Works hosted MCP server](https://lantern-works-mcp.lantern-works.workers.dev/mcp?ref=clawhub)
- [GPU prices API](https://thelanternworks.com/api/v1/gpu-prices.json)
- [GPU price changes API](https://thelanternworks.com/api/v1/gpu-price-changes.json)
- [Work-stack deals API](https://thelanternworks.com/api/v1/deals.json)
- [Lantern Works installation and service information](https://thelanternworks.com/install/?ref=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured price and deal results with concise comparisons]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include vendor source links, verification dates, billing details, and referral flags.]

## Skill Version(s):

1.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
