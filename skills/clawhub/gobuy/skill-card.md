## Description:

Checks marketplace product trust for Amazon, Walmart, Target, and Best Buy listings before recommending or buying, returning GoBuy Evidence Scores from 0 to 100 with signal breakdowns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[digitalmentes7-maker](https://clawhub.ai/user/digitalmentes7-maker)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping assistants use this skill to evaluate whether marketplace listing evidence supports a product recommendation. It is intended for trust checks, review-authenticity checks, seller-trust checks, and comparisons of 2 to 20 products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product IDs submitted for trust checks may be sent to GoBuy's external API or MCP service.

Mitigation: Use only listing identifiers that are appropriate to share with the GoBuy service, and avoid treating private shopping intent as local-only processing.

Risk: An Evidence Score can be misread as a guarantee of product quality, safety, or value.

Mitigation: Report the score as evidence-quality context with its date, verdict label, and missing signals; do not present it as an endorsement or safety finding.

Risk: A product may be unavailable to the engine or return a not-indexed result.

Mitigation: State that the engine has not indexed the product yet and avoid guessing a score.

## Reference(s):

- [GoBuy REST scoring endpoint](https://gobuy.ai/api/gobuy/extension/score?retailer={retailer}&productId={id})
- [GoBuy MCP endpoint](https://mcp.gobuy.ai/mcp)
- [GoBuy visual audit](https://audit.gobuy.ai)
- [ClawHub skill page](https://clawhub.ai/digitalmentes7-maker/skills/gobuy)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional REST URL, MCP configuration JSON, and product trust score reporting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports score, verdict label, freshness state, computed date, product context, and observed or missing trust signals when available.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
