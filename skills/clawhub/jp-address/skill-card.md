## Description:

Normalize, parse, validate, and geocode Japanese addresses, and look up Japanese postal codes with evidence for each match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can standardize Japanese addresses, inspect address components, check match precision, find coordinates, and look up postal areas. JPVerify requests are paid per successful call.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Address information is sent to the external JPVerify API.

Mitigation: Send only information you are entitled to process, and consider the service privacy terms before submitting addresses.

Risk: Scanner coverage was partial, so not every referenced local item was confirmed reviewed.

Mitigation: Review unresolved references before relying on the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/japanverify/skills/jp-address)
- [JPVerify website](https://www.jpverify.com)
- [Endpoint reference](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)
- [API key documentation](https://api.jpverify.com/docs/api-key)
- [x402 payment documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [API results, JSON, Address analysis]

**Output Format:** [Structured address results with concise explanations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be partial or ambiguous; normalize does not infer missing postal codes. Paid per successful API call.]

## Skill Version(s):

1.0.9 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
