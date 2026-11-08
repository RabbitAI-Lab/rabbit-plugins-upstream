## Description:

This skill combines JPVerify’s Japanese corporate-number, qualified-invoice, address, and relevant FSA or EDINET checks into a paid supplier evidence summary for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, accounts payable, and compliance teams use this skill to review Japanese suppliers during onboarding or before invoice payment. It gathers public registry evidence and flags cases for human review; it does not approve vendors or payments.

### Deployment Geography for Use:

Japan

## Known Risks and Mitigations:

Risk: Supplier and company information is sent to an external paid service.

Mitigation: Send only information the user is entitled to process, and avoid including unnecessary personal details.

Risk: Public registry coverage may be incomplete, and results are not a legal, KYB, AML, or sanctions determination.

Mitigation: Review source coverage and unresolved or ambiguous evidence manually; do not treat a missing match as proof that an entity does not exist or is risky.

## Reference(s):

- [Endpoint reference](references/endpoints.md)
- [Request examples](references/examples.md)
- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Markdown evidence summary for human review]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes public registry evidence for Japanese suppliers; paid API calls may incur per-call charges.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
