## Description:

This skill performs paid VIN-based vehicle transfer history lookups through Juhe Data and returns prior transfer records, transfer months, cities before and after transfer, and total transfer counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[juhemcp](https://clawhub.ai/user/juhemcp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to query a specific vehicle's ownership-transfer history by VIN for used-car, finance, or insurance risk checks after confirming the paid lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The queried VIN is sent to Juhe for a paid vehicle-transfer-history lookup.

Mitigation: Show the payment and privacy notice before the lookup, send only the VIN needed for the query, and avoid storing or logging the full VIN.

Risk: Users may over-rely on third-party vehicle transfer records for transaction, finance, or insurance decisions.

Mitigation: Present the results as reference information, keep the source disclaimer visible, and avoid making definitive legal or valuation conclusions.

Risk: Payment details or the HTTP 402 payment response could be mishandled during the Alipay payment flow.

Mitigation: Confirm price and order details with the user before approval and pass the payment response to the payment skill without changing order, price, or resource fields.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/juhemcp/skills/juhe-vehicle-owner-a2a)
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query)

## Skill Output:

**Output Type(s):** [Markdown, API Calls, Shell commands, Guidance]

**Output Format:** [Markdown tables with structured vehicle-transfer lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a valid 17-character VIN and user payment confirmation; output should use only returned API fields and include the stated data-source disclaimer.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
