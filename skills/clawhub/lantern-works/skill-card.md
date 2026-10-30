## Description:

Looks up tracked GPU rental prices and work-stack deals through the Lantern Works hosted MCP server or public JSON API, with vendor links, check dates, price changes, and referral links flagged.

This skill is ready for commercial/non-commercial use.

## Publisher:

[connormatthewdouglas](https://clawhub.ai/user/connormatthewdouglas)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams use the skill to compare tracked GPU rental prices and work-stack deals, review recent price changes, and estimate monthly service costs. Results include vendor sources and verification dates so users can assess availability, billing terms, and referral links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hosted queries can contain private details.

Mitigation: Keep private details out of hosted queries; use the public JSON API for lookups when appropriate.

Risk: The optional local server uses an installable package.

Mitigation: Review and pin the package version before using the local server.

Risk: Prices may change, cover tracked providers only, or include referral links.

Mitigation: Check and share the verification date, clarify the tracked-provider scope, and offer the vendor's direct page when a result uses a referral link.

## Reference(s):

- [Lantern Works installation and service information](https://thelanternworks.com/install/)
- [Hosted Lantern Works MCP server](https://lantern-works-mcp.lantern-works.workers.dev/mcp)
- [GPU rental prices API](https://thelanternworks.com/api/v1/gpu-prices.json)
- [GPU price changes API](https://thelanternworks.com/api/v1/gpu-price-changes.json)
- [Work-stack deals API](https://thelanternworks.com/api/v1/deals.json)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Structured price and deal results with comparisons, cost estimates, dates, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prices cover tracked providers; results can include referral links and verification dates.]

## Skill Version(s):

1.0.0 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
