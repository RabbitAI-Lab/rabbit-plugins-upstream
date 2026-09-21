## Description:

SCVD General Store guides agents through x402 verification, endpoint inspection, payment diagnosis, history retrieval, MPP interpretation, buyer and seller testing, and optional real-money SCVD store purchases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external agents use this skill to inspect and verify x402 artifacts, test buyer and seller flows, diagnose payment outcomes, read SCVD history, and complete explicitly authorized SCVD store purchases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid x402 calls can transfer real USDC.

Mitigation: Confirm the exact item, network, and maximum spend with the user before any signing or paid retry.

Risk: Wallet secrets or private keys could be exposed if requested in chat or sent to a service.

Mitigation: Use only an authorized wallet or client that signs locally, and never ask for private keys, seed phrases, access tokens, or wallet secrets.

Risk: Retrying a lost or failed purchase with new identity can create duplicate charges.

Mitigation: Preserve the original request, payment evidence, and idempotency key, and use recovery or status checks before authorizing a new payment.

Risk: Verification results and signed artifacts can be overread beyond their stated scope.

Mitigation: Report scope, exclusions, unobserved checks, freshness, and unsupported or inconclusive states alongside any verdict.

Risk: Optional operator metadata or memory-anchor summaries may contain sensitive information.

Mitigation: Send optional metadata only when useful, and exclude personal data, credentials, confidential business information, and sensitive memory summaries.

## Reference(s):

- [SCVD homepage](https://scvd.store)
- [SCVD menu](https://scvd.store/menu.json)
- [SCVD OpenAPI](https://scvd.store/openapi.json)
- [SCVD ClawHub skill page](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [Buyer and seller testing](references/buyer-seller-testing.md)
- [History](references/history.md)
- [Endpoint inspection](references/inspection.md)
- [MPP and mixed-protocol inspection](references/mpp.md)
- [Packages](references/packages.md)
- [Payment diagnosis](references/payment-debugging.md)
- [Purchases and recovery](references/purchases.md)
- [Store tasks](references/store.md)
- [Transports](references/transports.md)
- [Verification](references/verification.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with endpoint URLs, HTTP examples, JSON request shapes, package names, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe x402 payment flows that transfer real USDC; paid actions require explicit user authorization for item, network, and maximum spend before signing.]

## Skill Version(s):

3.18.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
