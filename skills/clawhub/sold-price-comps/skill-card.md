## Description:

Look up recent sold prices / current market comps for any product via the 3rd Place Provisions sold-prices MCP endpoint (pay-per-call, x402, no API keys).

This skill is ready for commercial/non-commercial use.

## Publisher:

[lilnomie](https://clawhub.ai/user/lilnomie)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query product resale comps through the sold_prices MCP tool. It is suited for reseller, collector, and market-research workflows that need structured price, condition, source, and date signals while distinguishing sold data from active asking prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger paid x402 calls.

Mitigation: Use MCP client approval prompts, spending caps, or other payment controls before enabling automatic calls.

Risk: Some responses may contain active listing prices rather than completed sale prices.

Mitigation: Check the response data_type and treat active listings as asking prices, not confirmed market-clearing sales.

Risk: Product queries are logged by the provider.

Mitigation: Avoid sending confidential inventory, customer, pricing-strategy, or business-plan details in queries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lilnomie/skills/sold-price-comps)
- [3rd Place Provisions Pulse](https://3rdplaceprovisions.com/pulse)
- [sold-price-comps MCP endpoint](https://api.3rdplaceprovisions.com/mcp)

## Skill Output:

**Output Type(s):** [text, JSON, configuration, guidance]

**Output Format:** [Markdown instructions and JSON MCP responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The sold_prices tool accepts a product query and a limit from 1 to 10; responses may contain sold-price data or active listing data.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
