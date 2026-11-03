## Description:

Helps shopping agents assess marketplace product evidence and reviews, compare listings, evaluate independent storefronts, and apply pre-purchase verification checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nil001133](https://clawhub.ai/user/nil001133)

### License/Terms of Use:

MIT-0

## Use Case:

External users and shopping agents use the skill to evaluate listing evidence, compare products, inspect review integrity and storefront trust, and apply a verification gate before checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product and storefront checks send submitted information to GoBuy, and pseudonymous caller tracking is disclosed.

Mitigation: Use public storefront addresses and remove credentials, private paths, query tokens, and fragments.

Risk: Scores and review-forensics results are evidence signals, not guarantees of product quality or safety; review analysis uses a limited sample.

Mitigation: Present the score with its verdict and computed date, explain the evidence limits, and avoid treating the result as proof of safety or quality.

## Reference(s):

- [GPV-1 Pre-Purchase Verification Specification](https://docs.gobuy.ai/standard)
- [GPV-1 machine-readable ruleset](https://docs.gobuy.ai/standard/v1.json)
- [Universal Cart integration](https://docs.gobuy.ai/ucp)
- [Evidence Passport position paper](https://docs.gobuy.ai/passport)
- [The Verification Gap position paper](https://docs.gobuy.ai/verification-gap)
- [Checkout WebMCP integration pattern](https://docs.gobuy.ai/webmcp)
- [GoBuy product evidence reports](https://audit.gobuy.ai)
- [GoBuy service agent-channel statistics](https://mcp.gobuy.ai/stats)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown with evidence scores, verdicts, comparisons, and caveats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes observed and missing evidence signals; review analysis is based on a limited sample and may take up to two minutes.]

## Skill Version(s):

1.2.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
