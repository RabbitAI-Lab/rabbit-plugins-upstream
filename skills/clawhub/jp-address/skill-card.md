## Description:

Normalize, parse, validate and geocode Japanese addresses, and look up Japanese postal codes with evidence for each match.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to clean and standardize Japanese addresses, check address precision, find coordinates, and look up postal-code areas for tasks such as shipping and onboarding.

### Deployment Geography for Use:

Japan

## Known Risks and Mitigations:

Risk: Submitted addresses are sent to JPVerify's external API.

Mitigation: Send only information the user is entitled to process, and consider whether the API is trusted to receive it.

Risk: Successful API calls use prepaid credits, or x402 payments may use USDC.

Mitigation: Use an API key only with available credits; make x402 payments only within a user-approved budget.

Risk: The security assessment is benign with medium confidence, and scanner coverage was partial.

Mitigation: Review the skill and its external API use before installation; treat the security verdict as limited by the stated partial coverage.

## Reference(s):

- [Endpoint reference](references/endpoints.md)
- [Request examples](references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [Structured data, API results, Address validation and geocoding evidence]

**Output Format:** [Structured address results with match status, confidence, and supporting evidence]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be partial or ambiguous; they are public-registry pre-checks, not legal or compliance determinations.]

## Skill Version(s):

1.0.1 (source: release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
