## Description:

Run a pre-payment supplier and counterparty check with JPVerify, combining Japanese corporate-number, qualified-invoice (T-number), and address evidence with FSA licence and EDINET checks when relevant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Accounts payable, procurement, and compliance teams use this workflow to gather public-registry evidence when onboarding Japanese suppliers, checking invoices, or reviewing counterparties. It summarizes evidence for a human decision and does not approve vendors or payments.

### Deployment Geography for Use:

Japan

## Known Risks and Mitigations:

Risk: The security assessment has medium confidence and reports unresolved local path-like references; information sent to the referenced external service may also be sensitive.

Mitigation: Review unresolved references and decide what information to send; share only information appropriate for JPVerify and only fields the user is entitled to process.

Risk: Successful JPVerify API calls incur per-call charges against prepaid credits.

Mitigation: Check the applicable price and obtain approval before batch work or plans exceeding the skill's $0.50 threshold.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/japanverify/skills/jp-supplier-due-diligence)
- [JPVerify website](https://www.jpverify.com)
- [API key documentation](https://api.jpverify.com/docs/api-key)
- [x402 documentation](https://api.jpverify.com/docs/x402)
- [Endpoint reference](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown evidence summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One evidence block per counterparty; Japanese suppliers only. Supports human review and does not make legal, KYB, AML, sanctions, tax, or accounting determinations.]

## Skill Version(s):

1.3.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
