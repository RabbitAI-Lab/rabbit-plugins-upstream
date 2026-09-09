## Description:

SCVD General Store helps agents and developers practice live x402 payments, run free conformance checks for signed offers and receipts, and obtain signed observations of endpoint and settlement behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[seancrecord](https://clawhub.ai/user/seancrecord)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent builders, and operators use this skill to test x402 clients against a live payment endpoint, check signed offer and receipt conformance, inspect endpoint readiness, and purchase signed attestations or store artifacts with buyer-authorized payments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is payment-oriented and paid actions can involve real USDC settlement.

Mitigation: Review the live quote, amount, network, recipient, and idempotency key before signing; use free endpoints for initial checks where possible.

Risk: Context-anchor summaries are externally persisted and may be retrieved later.

Mitigation: Do not include secrets, private keys, access tokens, personal data, or confidential business information in context-anchor summaries.

Risk: The scvd-tab MCP install uses an npm package that runs local code.

Mitigation: Pin and verify the package version, and run it with minimal filesystem and environment access.

## Reference(s):

- [SCVD Store Homepage](https://scvd.store)
- [ClawHub Skill Page](https://clawhub.ai/seancrecord/skills/scvd-general-store)
- [OpenAPI Document](https://scvd.store/openapi.json)
- [x402 Practice Guide](https://scvd.store/try)
- [Conformance Vectors](https://scvd.store/.well-known/conformance/offer-receipt-vectors.json)
- [Live Menu](https://scvd.store/menu.json)
- [Attestation Reference](https://scvd.store/attestation)
- [Criteria](https://scvd.store/criteria)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTTPS endpoints, JSON examples, and shell command/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May involve live USDC settlement; paid actions require buyer-authorized wallet signing.]

## Skill Version(s):

3.16.1 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
