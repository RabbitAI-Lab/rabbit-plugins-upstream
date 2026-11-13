## Description:

Checks marketplace product evidence, compares listings, analyzes review signals, and scores stores to help agents assess trust before shopping decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[digitalmentes7-maker](https://clawhub.ai/user/digitalmentes7-maker)

### License/Terms of Use:

MIT-0

## Use Case:

AI shopping agents use this skill to compare evidence behind marketplace listings, inspect review integrity signals, and assess independent stores before advising on purchases. It can also help apply GoBuy's GPV-1 checks before checkout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the service sends shopping queries and disclosed caller identifiers to GoBuy; hosted-service privacy practices are unverified.

Mitigation: Confirm the service's privacy practices and ensure this data sharing is acceptable before using it.

Risk: Product and store scores are evidence signals, not guarantees of safety or authorization to purchase.

Mitigation: Present scores with their verdict and limitations, and apply the documented verification checks before checkout.

## Reference(s):

- [GPV-1 pre-purchase verification specification](https://docs.gobuy.ai/standard)
- [GPV-1 machine-readable ruleset](https://docs.gobuy.ai/standard/v1.json)
- [Universal Cart integration](https://docs.gobuy.ai/ucp)
- [Evidence Passport position paper](https://docs.gobuy.ai/passport)
- [Agent channel statistics](https://mcp.gobuy.ai/stats)
- [Product evidence reports](https://audit.gobuy.ai)
- [Store scoring API](https://stores.gobuy.ai/store/{domain}?format=json)
- [Store scan API](https://stores.gobuy.ai/api/scan)

## Skill Output:

**Output Type(s):** [Guidance, Analysis, API Calls]

**Output Format:** [Text or Markdown with scores, verdicts, evidence signals, and review findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-focused shopping guidance; review findings are heuristic signals from a limited sample.]

## Skill Version(s):

1.2.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
