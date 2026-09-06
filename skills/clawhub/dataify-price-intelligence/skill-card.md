## Description:

Compare product or service prices across multiple sellers, marketplaces, or official pricing pages and produce normalized, evidence-backed pricing findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and operators use this skill to collect comparable current offers, normalize pricing details, and support price monitoring, offer comparison, channel pricing, and pricing-change decisions. It is intended for multi-source price comparison rather than single-product lookup or broad competitor strategy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pricing lookups can spend Dataify credits.

Mitigation: Use dry-run or max-actions when cost or scope matters.

Risk: Raw responses and reports may be retained in the output directory.

Mitigation: Review the output location and avoid collecting sensitive pricing inputs unless they are needed.

Risk: A Dataify token can be exposed if shared in chat or printed in logs.

Mitigation: Provide the token through an environment variable and verify only whether the variable is present.

## Reference(s):

- [Dataify Price Intelligence on ClawHub](https://clawhub.ai/dataify-server/skills/dataify-price-intelligence)
- [Dataify Account Dashboard](https://dashboard.dataify.com/login?utm_source=skill)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown report with JSON artifacts and concise shell commands when setup or dry-run execution is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include comparable offer counts, price ranges, the lowest comparable offer, channel differences, anomalies, gaps, and recommended next actions; raw responses, hashes, state, and reports may be retained in the output directory.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
