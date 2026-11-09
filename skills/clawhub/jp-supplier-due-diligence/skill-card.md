## Description:

Combines Japanese corporate, qualified-invoice, and address evidence, with optional FSA licence and EDINET checks, to prepare a supplier due-diligence summary for human review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[japanverify](https://clawhub.ai/user/japanverify)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, accounts payable, and compliance teams use this skill to prepare a public-registry pre-check when onboarding Japanese suppliers or reviewing invoices; a human makes the final decision.

### Deployment Geography for Use:

Japan

## Known Risks and Mitigations:

Risk: Supplier identifiers are sent to an external JPVerify service, and successful calls incur per-call charges.

Mitigation: Send only information you are entitled to process, avoid unnecessary personal details, and confirm costs and any required budget approval before batches.

Risk: The security review is benign with medium confidence but partial, and public-registry results may be ambiguous or incomplete.

Mitigation: Treat results as a public-registry pre-check, retain coverage and freshness caveats, and route ambiguous or incomplete cases to a human; do not treat results as legal or KYB conclusions.

## Reference(s):

- [JPVerify API key documentation](https://api.jpverify.com/docs/api-key)
- [JPVerify x402 payment documentation](https://api.jpverify.com/docs/x402)
- [Endpoint reference](artifact/references/endpoints.md)
- [Request examples](artifact/references/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown evidence summary with per-counterparty decision signals, matched identifiers, source freshness, and next actions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Japanese and English registry details; does not approve vendors or payments.]

## Skill Version(s):

1.2.1 (source: server-resolved release, SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
