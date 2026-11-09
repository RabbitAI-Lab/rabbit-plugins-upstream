## Description:

Normalize, parse, validate, and geocode Japanese addresses, look up postal codes, and review evidence for each match with JPVerify.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data teams use this skill to standardize and check Japanese addresses, split them into components, find coordinates, and look up postal-code areas.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Address fields sent for a check are processed by an external API.

Mitigation: Send only address data the user is entitled to process, and omit names, phone numbers, and email addresses when they are not needed.

Risk: API calls are paid per successful request, and x402 calls can spend funds.

Mitigation: Use the balance check before a large batch, confirm batch cost with the user, and use x402 only within an approved budget.

## Reference(s):

- [Endpoint reference](references/endpoints.md)
- [Request examples](references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)
- [JPVerify](https://www.jpverify.com)

## Skill Output:

**Output Type(s):** [API results, JSON, Guidance]

**Output Format:** [Structured results with concise explanatory guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Address matching may be partial or ambiguous; results include confidence and match evidence.]

## Skill Version(s):

1.2.1 (source: server-resolved release evidence and skill text)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
