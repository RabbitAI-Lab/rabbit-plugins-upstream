## Description:

Verify Japanese companies against registry sources, resolve English or romanized names to legal entities, and retrieve company status, profiles, filings, and selected financial licences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Business teams and developers use this skill to identify Japanese legal entities and review registry-backed details before onboarding, contracting, or payment. It provides a public-registry pre-check, not full KYC/KYB or legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company lookup fields may be sent to JPVerify, an external service.

Mitigation: Send only the company fields needed for the lookup and avoid unnecessary personal details.

Risk: Successful lookups may incur per-call charges or require payment.

Mitigation: Check the stated price and available credits before large batches; get user approval before paying through x402.

## Reference(s):

- [JPVerify release page](https://clawhub.ai/japanverify/skills/jp-company-verify)
- [JPVerify website](https://www.jpverify.com)
- [API endpoints](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)
- [API key documentation](https://api.jpverify.com/docs/api-key)
- [x402 documentation](https://api.jpverify.com/docs/x402)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [Structured JSON registry results with concise explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results include match status and source evidence where available; calls may be billed per successful request. This is not full KYC/KYB or legal advice.]

## Skill Version(s):

1.2.1 (source: release metadata, artifact/SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
